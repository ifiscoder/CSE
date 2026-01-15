# Chapter 7: Virtual Memory | The Demand Singularity

## The Atomic Truth
**Virtual Memory = Execute programs larger than physical memory**

---

## 7.1 Demand Paging: The Core Mechanism

### The Path of Elegance

**Key Insight:** Load pages **only when needed** (on demand), not all at once.

**The Illusion:**
- Logical address space: 4 GB (32-bit)
- Physical RAM: 512 MB
- **Process thinks it has 4 GB!**

**How:** Most pages stay on **disk** until accessed.

### Page Table Entry with Valid Bit

```c
struct PTE {
    unsigned int frame : 20;
    unsigned int valid : 1;    // 1 = in memory, 0 = on disk
    unsigned int dirty : 1;    // Modified since load?
    unsigned int reference : 1; // Recently accessed?
};
```

**Valid = 0 → Page Fault**

---

## 7.2 Page Fault Handling

### The Complete Sequence

```
1. CPU generates logical address
2. MMU checks page table
3. If valid = 0 → Page Fault (trap to OS)
4. OS checks if address is legal (in process's address space)
5. If illegal → Segmentation Fault (kill process)
6. If legal:
   a. Find free frame (or evict a page)
   b. Read page from disk to frame (I/O operation)
   c. Update page table (valid = 1, frame number)
   d. Restart instruction
7. Instruction re-executes, now page is in memory
```

**The Golden Pivot:** Step 6b (disk I/O) takes **~10,000,000 ns** (10 ms) vs memory access (~100 ns). **Page faults are expensive!**

### Effective Access Time with Page Faults

$$\text{EAT} = (1-p) \times T_{\text{mem}} + p \times T_{\text{page\_fault}}$$

where:
- $p$ = page fault rate (0 ≤ $p$ ≤ 1)
- $T_{\text{mem}}$ = memory access time (~100 ns)
- $T_{\text{page\_fault}}$ = page fault service time (~10 ms = 10,000,000 ns)

**Example:**

**Given:**
- Memory access: 100 ns
- Page fault time: 10 ms
- Page fault rate: 0.01% (1 in 10,000 accesses)

**Solution:**
$$\text{EAT} = 0.9999 \times 100 + 0.0001 \times 10,000,000$$
$$= 99.99 + 1000 = 1099.99 \text{ ns}$$

**Slowdown:** $1099.99 / 100 \approx 11\times$ slower!

**The 2026 Adversarial Vault:**

**Trap:** "Even 1% page fault rate is acceptable."
- **FALSE!** 1% page fault rate:
$$\text{EAT} = 0.99 \times 100 + 0.01 \times 10,000,000 = 99 + 100,000 = 100,099 \text{ ns}$$
- **1000× slowdown!**

**NAT Precision Lock:** For acceptable performance, page fault rate must be **< 0.0001** (1 in 10,000).

---

## 7.3 Page Replacement Algorithms

### The Problem

**Scenario:** Page fault occurs, but **all frames are occupied**.

**Solution:** **Evict** (replace) a page to free a frame.

**Goal:** Minimize page faults (choose victim wisely).

### The Reference String

**Definition:** Sequence of page accesses.

**Example:** `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5`

**Unique pages:** {1, 2, 3, 4, 5}
**If frames = 3:** Not all pages can be in memory simultaneously.

---

## 7.4 FIFO (First-In, First-Out)

### The Algorithm

**Rule:** Replace the **oldest** page (first loaded).

**Implementation:** Queue (FIFO).

### Example

**Reference String:** `7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2`
**Frames:** 3

**Execution:**

```
Page   | Frames       | Fault?
-------|--------------|-------
7      | 7            | F
0      | 7 0          | F
1      | 7 0 1        | F
2      | 2 0 1        | F (evict 7)
0      | 2 0 1        | -
3      | 2 3 1        | F (evict 0)
0      | 2 3 0        | F (evict 1)
4      | 4 3 0        | F (evict 2)
2      | 4 2 0        | F (evict 3)
3      | 4 2 3        | F (evict 0)
0      | 0 2 3        | F (evict 4)
3      | 0 2 3        | -
2      | 0 2 3        | -
```

**Total Faults:** 10

### Belady's Anomaly

**Definition:** Increasing the number of frames can **increase** page faults (counterintuitive!).

**Example:**

**Reference String:** `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5`

**With 3 frames:** 9 faults
**With 4 frames:** 10 faults (more!)

**The Trap:** "More memory always reduces page faults."
- **FALSE for FIFO, TRUE for optimal/LRU.**

---

## 7.5 Optimal Page Replacement (OPT / MIN)

### The Atomic Truth
**Replace the page that will NOT be used for the longest time**

### The Algorithm

**Rule:** Replace page whose **next use** is farthest in the future.

**The Genius:** Provably **optimal** (Belady's Algorithm).

**The Problem:** Requires **clairvoyance** (future knowledge).

### Example

**Reference String:** `7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2`
**Frames:** 3

**Execution:**

```
Page   | Frames       | Fault? | Next Uses
-------|--------------|--------|--------------------
7      | 7            | F      | 7: never
0      | 7 0          | F      | 7: never, 0: 4
1      | 7 0 1        | F      | 7: never, 0: 4, 1: 10
2      | 2 0 1        | F      | Replace 7 (never used)
0      | 2 0 1        | -      |
3      | 2 0 3        | F      | Replace 1 (used at 10 vs 0 at 6)
0      | 2 0 3        | -      |
4      | 4 0 3        | F      | Replace 2 (used at 8 vs 0 at 6, 3 at 9)
2      | 4 0 2        | F      | Replace 3 (used at 9 vs 0 at 10, 2 at 8)
3      | 4 3 2        | F      | Replace 0 (used at 10 vs 2 at 12, 3 at 9)
0      | 0 3 2        | F      | Replace 4 (never used)
3      | 0 3 2        | -      |
2      | 0 3 2        | -      |
```

**Total Faults:** 7 (optimal)

**The 2026 Trap:**

**Question:** "Optimal algorithm is used in practice."
- **FALSE.** Cannot predict future (used only as **benchmark**).

---

## 7.6 LRU (Least Recently Used)

### The Atomic Truth
**Replace the page NOT used for the longest time (in the past)**

### The Algorithm

**Rule:** Replace page with **oldest last access** time.

**Heuristic:** Past behavior predicts future (temporal locality).

### Implementation Approaches

#### 1. Counter-Based

Each page has a counter (timestamp of last access).
**Overhead:** Update counter on every memory access (expensive).

#### 2. Stack-Based

Maintain a stack of page numbers (most recent on top).
**Overhead:** Update stack on every memory access (expensive).

### Example

**Reference String:** `7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2`
**Frames:** 3

**Execution:**

```
Page   | Frames       | Fault? | LRU Order (top = most recent)
-------|--------------|--------|--------------------------------
7      | 7            | F      | [7]
0      | 7 0          | F      | [0, 7]
1      | 7 0 1        | F      | [1, 0, 7]
2      | 2 0 1        | F      | Replace 7 (LRU)
0      | 2 0 1        | -      | [0, 2, 1]
3      | 2 0 3        | F      | Replace 1 (LRU)
0      | 2 0 3        | -      | [0, 2, 3]
4      | 4 0 3        | F      | Replace 2 (LRU)
2      | 4 0 2        | F      | Replace 3 (LRU)
3      | 4 3 2        | F      | Replace 0 (LRU)
0      | 0 3 2        | F      | Replace 4 (LRU)
3      | 0 3 2        | -      | [3, 0, 2]
2      | 0 3 2        | -      | [2, 3, 0]
```

**Total Faults:** 9

**The Golden Pivot:** LRU approximates optimal (good in practice, no clairvoyance needed).

### The Problem: Implementation Cost

True LRU requires updating on **every memory reference** → **unacceptable overhead**.

**Solution:** Use approximations (next section).

---

## 7.7 LRU Approximations

### 1. Reference Bit (Second Chance / Clock)

**Mechanism:**
- Each page has a **reference bit** (set by hardware on access)
- Periodically, OS clears all reference bits
- On replacement: Find page with reference bit = 0

**Clock Algorithm:**

```
Circular queue of pages (like a clock hand)
On page fault:
    Loop:
        If current page's reference bit = 0:
            Replace this page
        Else:
            Clear reference bit
            Move to next page
```

**The Genius:** Give pages a "second chance" (clear bit instead of immediate eviction).

### 2. Enhanced Second Chance (4-Class)

**Use two bits:** (reference, modified)

**Classes (in order of preference to replace):**
1. **(0, 0):** Not recently used, not modified (best to replace)
2. **(0, 1):** Not recently used, but modified (need to write back)
3. **(1, 0):** Recently used, not modified
4. **(1, 1):** Recently used and modified (worst to replace)

**Rule:** Replace lowest class page. If all in same class, use FIFO within that class.

**The Mental Machinery:** Prefer evicting **clean** (not modified) pages to avoid disk write.

---

## 7.8 Other Page Replacement Algorithms

### LFU (Least Frequently Used)

**Rule:** Replace page with **lowest access count**.

**Problem:** Old pages with high initial count never evicted (even if not used recently).

### MFU (Most Frequently Used)

**Rule:** Replace page with **highest access count**.

**Rationale:** Page with high count probably finished its work.

**Reality:** **Rarely used** (counterintuitive, performs poorly).

---

## 7.9 Thrashing: The Death Spiral

### The Atomic Truth
**Thrashing = Page fault rate > 90%, CPU utilization → 0%**

### The Mechanism

```
1. OS notices low CPU utilization
2. OS increases degree of multiprogramming (more processes)
3. More processes → less memory per process
4. Less memory → more page faults
5. More page faults → processes spend time in I/O wait
6. Low CPU utilization (back to step 1)
```

**Result:** System spends all time paging, no useful work.

**The Mental Slider:** Pull slider right (more processes) → initially good, then **cliff** → thrashing.

### The Working Set Model

**Definition:** Set of pages a process is **actively using**.

**Working Set $W(t, \Delta)$:** Set of pages referenced in the last $\Delta$ time units.

**Principle:** Allocate enough frames for each process's working set.

**Condition to prevent thrashing:**
$$\sum_{i=1}^{n} |W_i| \leq \text{Total Frames}$$

If violated, **suspend a process** (reduce multiprogramming).

### Page Fault Frequency (PFF)

**Approach:** Monitor page fault rate per process.

**Rule:**
- If PF rate **too high** → allocate **more frames**
- If PF rate **too low** → reclaim frames (give to other processes)

**Threshold Example:**
- Upper threshold: 10 faults/second
- Lower threshold: 1 fault/second

---

## 7.10 Memory-Mapped Files

### The Mechanism

**Concept:** Map a file directly into virtual address space.

**Benefits:**
1. File I/O via memory access (no `read()` / `write()` syscalls)
2. Shared memory between processes (map same file)

**System Call:**
```c
void *addr = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
```

**Use Case:** Database engines, shared libraries, IPC.

---

## 7.11 Allocation of Frames

### Global vs Local Replacement

| **Policy** | **Description** | **Pros** | **Cons** |
|------------|-----------------|----------|----------|
| **Global** | Process can replace any frame (system-wide) | Adaptive (gives frames to processes that need them) | One process can steal from others |
| **Local** | Process can only replace its own frames | Isolation (fair allocation) | Inflexible (can't adapt to working set changes) |

**Modern OS:** Combination (local with periodic global adjustment).

---

## 7.12 Mental Machinery for Permanent Recall

### The Bizarre Mnemonic: "The Restaurant Kitchen"

Imagine a **restaurant kitchen** (RAM):

- **Pages:** Dishes (recipes)
- **Frames:** Counters (workspace)
- **Disk:** Cookbook shelf (storage)
- **Page Fault:** Chef needs dish not on counter, must fetch from shelf (slow!)
- **FIFO:** Remove oldest dish on counter
- **Optimal:** Remove dish won't be needed for longest time (clairvoyant chef)
- **LRU:** Remove dish not used recently (sensible heuristic)
- **Thrashing:** Too many chefs, constant trips to shelf, no cooking done
- **Working Set:** Set of dishes chef actively uses

**The Mental Slider:**
- Left (FIFO): Simple, but might remove dish needed soon
- Right (LRU): Smart, but expensive to track

### The 5-Second Snap-Check

**Q:** Which algorithm for which scenario?

| **Scenario** | **Algorithm** |
|--------------|---------------|
| Benchmark (theoretical best) | Optimal |
| Good practical performance | LRU / Clock |
| Low overhead needed | FIFO / Second Chance |
| Memory-constrained system | Working Set model |

---

## 7.13 Practice Problems

### MCQ 1: EAT with Page Faults

**Q:** Memory access = 200 ns, page fault = 8 ms, page fault rate = 0.001. EAT = ?

(A) 200 ns  
(B) 8 μs  
(C) 8.2 μs  
(D) 8000 μs  

**Solution:**

$$\text{EAT} = 0.999 \times 200 + 0.001 \times 8,000,000$$
$$= 199.8 + 8000 = 8199.8 \text{ ns} \approx 8.2 \text{ μs}$$

**Answer: (C)**

---

### MCQ 2: Page Replacement

**Q:** Which algorithm suffers from Belady's Anomaly?

(A) FIFO  
(B) LRU  
(C) Optimal  
(D) All of the above  

**Solution:**

Only **FIFO** suffers from Belady's Anomaly.

**Answer: (A)**

---

### MCQ 3: Page Faults (FIFO)

**Q:** Reference string: `1, 2, 3, 4, 1, 2, 5, 1, 2, 3`. Frames = 3. Using FIFO, how many page faults?

(A) 7  
(B) 8  
(C) 9  
(D) 10  

**Solution:**

```
1: [1] F
2: [1,2] F
3: [1,2,3] F
4: [4,2,3] F (replace 1)
1: [4,1,3] F (replace 2)
2: [4,1,2] F (replace 3)
5: [5,1,2] F (replace 4)
1: [5,1,2] - (hit)
2: [5,1,2] - (hit)
3: [5,3,2] F (replace 1)
```

**Total: 8 faults**

**Answer: (B)**

---

### MCQ 4: LRU

**Q:** Reference string: `7, 0, 1, 2, 0, 3, 0`. Frames = 3. Using LRU, how many page faults?

(A) 4  
(B) 5  
(C) 6  
(D) 7  

**Solution:**

```
7: [7] F
0: [7,0] F
1: [7,0,1] F
2: [2,0,1] F (replace 7, LRU)
0: [2,0,1] - (hit)
3: [2,0,3] F (replace 1, LRU)
0: [2,0,3] - (hit)
```

**Total: 5 faults**

**Answer: (B)**

---

### NAT 1: Optimal Page Faults

**Q:** Reference string: `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5`. Frames = 4. Using Optimal, how many page faults?

**Solution:**

```
1: [1] F
2: [1,2] F
3: [1,2,3] F
4: [1,2,3,4] F
1: [1,2,3,4] - (hit)
2: [1,2,3,4] - (hit)
5: [1,2,5,4] F (replace 3, next use at index 9 vs 4 at 10)
1: [1,2,5,4] - (hit)
2: [1,2,5,4] - (hit)
3: [1,2,5,3] F (replace 4, next use at index 10 vs 3 at index 9)
4: [1,2,4,3] F (replace 5, never used again)
5: [1,2,4,5] F (replace 3, never used again)
```

**Wait, let me recalculate more carefully:**

```
Index: 0  1  2  3  4  5  6  7  8  9  10 11
Page:  1  2  3  4  1  2  5  1  2  3  4  5

1: [1] F
2: [1,2] F
3: [1,2,3] F
4: [1,2,3,4] F
1: hit
2: hit
5: [5,2,3,4] F (replace 1, next use of 1 at 7, others at 5,8,9,10 - wait, need to check future)

Let me use next-use positions:
At index 6 (inserting 5):
- 1: next at 7
- 2: next at 8
- 3: next at 9
- 4: next at 10
Replace 4 (farthest)

5: [1,2,3,5] F
1: hit
2: hit
3: hit
4: [1,2,4,5] F (replace 3, no future use)
5: hit
```

**Recounting:**
```
1: F
2: F
3: F
4: F
5: F
4: F (at index 10)
```

**Total: 6 faults**

**Answer: 6**

---

### NAT 2: EAT Calculation

**Q:** Page fault rate = 0.0005, memory access = 100 ns, page fault service = 10 ms. What is EAT in nanoseconds?

**Solution:**

$$\text{EAT} = (1 - 0.0005) \times 100 + 0.0005 \times 10,000,000$$
$$= 99.95 + 5000 = 5099.95 \text{ ns}$$

**Answer: 5099.95** (or 5100 if rounding)

---

### NAT 3: Thrashing Threshold

**Q:** System has 100 frames. 4 processes with working sets: 30, 25, 20, 35 frames. Will thrashing occur? (1=yes, 0=no)

**Solution:**

Total working set: $30 + 25 + 20 + 35 = 110$ frames

System has 100 frames → $110 > 100$ → **Thrashing will occur**

**Answer: 1**

---

### NAT 4: Page Faults with Modified Frames

**Q:** Frames = 3. Reference string: `A, B, C, D, B, E`. All pages modified on first access. Using FIFO, how many total disk writes?

**Solution:**

```
A: [A] F (clean load)
B: [A,B] F (clean load)
C: [A,B,C] F (clean load)
D: [D,B,C] F (replace A, A is dirty → write back) +1 write
B: hit
E: [D,E,C] F (replace B, B is dirty → write back) +1 write
```

**Total disk writes: 2**

**Answer: 2**

---

## 7.14 The Elite Formulas Summary

### 1. Effective Access Time with Page Faults

$$\text{EAT} = (1-p) \times T_{\text{mem}} + p \times T_{\text{page\_fault}}$$

### 2. Page Fault Service Time

$$T_{\text{page\_fault}} = T_{\text{trap}} + T_{\text{page\_out}} + T_{\text{page\_in}} + T_{\text{restart}}$$

Typically: $T_{\text{page\_fault}} \approx 1-10 \text{ ms}$

### 3. Thrashing Condition

$$\sum_{i=1}^{n} |W_i| > \text{Total Frames} \Rightarrow \text{Thrashing}$$

---

## Logic Singularity Verified for 2026 (IIT-G Standards)

**Mastery Level:** Sovereign

**The Core Insight:**
- **Demand Paging:** Load pages on-demand (lazy loading)
- **Page Replacement:** FIFO (simple), Optimal (benchmark), LRU (practical)
- **Thrashing:** Too many processes, too little memory per process

**The Universal Pattern:** Virtual memory trades **disk space** for **RAM**, but page faults are **expensive** (factor of 100,000×).

**Next:** Chapter 8 dissects **File Systems**—where you'll learn why "deleting a file" doesn't always delete it.

**Would you like to initiate a 'Multi-Variable Stress Test' combining page replacement with disk scheduling?**
