# Virtual Memory | The Abstraction Singularity

> **The Atomic Truth:** *Illusion of infinite memory through paging.*

[Image of virtual address space (large, contiguous) mapping to scattered physical memory pages through page table - the fundamental address translation]

---

## I. THE PATH OF ELEGANCE

### 1.1 Virtual Memory (The Core Concept)

**The Golden Pivot:** **Page table** translates virtual → physical addresses.

**Why Virtual Memory?**
1. **Larger address space** than physical RAM (illusion of infinity)
2. **Process isolation** (security: each process has own address space)
3. **Efficient memory use** (load only needed pages)
4. **Relocation** (programs run anywhere in physical memory)

**Address Translation:**
$$\text{Virtual Address} \xrightarrow{\text{Page Table}} \text{Physical Address}$$

---

### 1.2 Paging Fundamentals

**Page:** Fixed-size block of virtual memory (typically 4 KB)
**Frame:** Fixed-size block of physical memory (same size as page)

**Virtual Address Structure:**
$$\text{VA} = \boxed{\text{Virtual Page Number (VPN)}} \mid \boxed{\text{Page Offset}}$$

**Physical Address Structure:**
$$\text{PA} = \boxed{\text{Physical Frame Number (PFN)}} \mid \boxed{\text{Page Offset}}$$

**Key Insight:** Offset bits are **same** in VA and PA (intra-page location unchanged).

**Address Translation:**
1. Extract VPN from VA
2. Look up VPN in page table → get PFN
3. Concatenate PFN with offset → PA

---

### 1.3 Page Table Entry (PTE)

**Each entry contains:**
- **Valid Bit (V):** Is page in memory? (1 = yes, 0 = page fault)
- **Frame Number:** Physical frame where page is loaded
- **Protection Bits:** Read/Write/Execute permissions
- **Dirty Bit (D):** Has page been modified?
- **Reference/Access Bit (R):** Has page been accessed recently?
- **Other:** Caching policy, etc.

**Example PTE (32-bit system, 4KB pages):**
```
| V | R | D | Protection (2) | Frame Number (20) | ... |
  1   1   1        11               FFFFF...
```

---

### 1.4 Page Table Size Problem

**Example:** 32-bit virtual address, 4 KB pages

**Calculation:**
- Page size = 4 KB = $2^{12}$ bytes → Offset = 12 bits
- VPN = $32 - 12 = 20$ bits
- # Pages = $2^{20} = 1,048,576$ pages

**Page table size (assuming 4-byte PTE):**
$$1,048,576 \times 4 \text{ bytes} = 4 MB$$

**Per process!**

**For 64-bit systems:** Would be astronomically large!

**Solution:** Multi-level page tables.

---

### 1.5 Multi-Level Page Tables

**Idea:** Hierarchical structure (tree of page tables).

**2-Level Page Table:**
$$\text{VA} = \boxed{\text{PT1 Index}} \mid \boxed{\text{PT2 Index}} \mid \boxed{\text{Offset}}$$

**Translation:**
1. Use PT1 index → locate PT2 (second-level table)
2. Use PT2 index → locate frame number
3. Combine frame + offset → PA

**Advantage:** Only allocate second-level tables for **used** portions of address space.

**Example:** 32-bit VA, 4 KB pages, 2-level

- Offset = 12 bits
- PT2 Index = 10 bits (1024 entries)
- PT1 Index = 10 bits

**Space savings:** If process uses only 10% of address space, only 10% of PT2 tables allocated.

---

### 1.6 Translation Lookaside Buffer (TLB)

**The Performance Crisis:** Every memory access requires 2 accesses (PT + data) → 2× slower!

**Solution:** **TLB** - A **cache** for page table entries.

**TLB Structure:**
- Small (16-256 entries), fully associative
- Stores recent VPN → PFN mappings

**Address Translation with TLB:**
1. Check TLB for VPN
   - **TLB Hit:** Get PFN directly, form PA
   - **TLB Miss:** Access page table, update TLB
2. Access memory at PA

**Effective Access Time:**
$$\text{EAT} = T_{\text{TLB}} + (1 - h_{\text{TLB}}) \times T_{\text{PT}} + T_{\text{mem}}$$

Where $h_{\text{TLB}}$ = TLB hit rate

**Example:** TLB access = 1 ns, PT access = 10 ns, mem = 100 ns, TLB hit = 98%

$$\text{EAT} = 1 + (0.02 \times 10) + 100 = 101.2 \text{ ns}$$

(vs. 110 ns without TLB)

---

### 1.7 Page Replacement Algorithms

**When:** Physical memory full, need to evict a page to load new one.

**Goal:** Minimize page faults.

#### 1. Optimal (OPT) - Theoretical Benchmark
**Replace:** Page that will be used **farthest in future**.

**Problem:** Requires future knowledge (impossible in practice).

**Use:** Lower bound for comparison.

---

#### 2. First-In-First-Out (FIFO)
**Replace:** Oldest page in memory.

**Advantage:** Simple (queue).

**Disadvantage:** May replace frequently used pages.

**Belady's Anomaly:** More frames can cause **more** page faults with FIFO!

---

#### 3. Least Recently Used (LRU) ⭐
**Replace:** Page not used for **longest time**.

**Advantage:** Exploits temporal locality (best practical algorithm).

**Implementation:**
- **Stack:** Maintain access order (expensive)
- **Counter:** Timestamp per page
- **Approximation:** Reference bits + aging

---

#### 4. Clock (Second Chance)
**Approximation of LRU:**
- Maintain circular list of pages
- Each page has reference bit (R)
- **Clock hand** sweeps:
  - If R=1: Set R=0, move to next
  - If R=0: Replace this page

**Advantage:** Simple, good performance.

---

#### 5. Not Recently Used (NRU)
**Use:** Reference (R) and Modified (M) bits.

**Classes (priority for replacement):**
1. R=0, M=0 (not referenced, not modified) - **Best to replace**
2. R=0, M=1 (not referenced, but modified)
3. R=1, M=0 (referenced, not modified)
4. R=1, M=1 (referenced and modified) - **Worst to replace**

**Replace:** Random page from lowest non-empty class.

---

### 1.8 Thrashing

**Definition:** System spends more time paging than executing.

**Cause:** Too many processes, not enough frames → constant page faults.

**Solution:**
- **Working Set Model:** Keep pages of working set in memory
- **Page Fault Frequency:** Monitor PF rate, adjust allocation
- **Reduce multiprogramming degree:** Suspend processes

---

### 1.9 Segmentation

**Alternative to paging:** Variable-size segments (code, data, stack, heap).

**Segment Table Entry:**
- **Base:** Physical start address of segment
- **Limit:** Length of segment
- **Protection bits**

**Address Translation:**
$$\text{Physical Address} = \text{Segment Base} + \text{Offset}$$

**Check:** $\text{Offset} < \text{Limit}$ (else segmentation fault)

**Advantage:** Logical division matches program structure.

**Disadvantage:** **External fragmentation** (variable sizes).

**Segmentation + Paging:** Combine both (e.g., x86 architecture).

---

## II. THE 2026 ADVERSARIAL VAULT

### Trap #1: TLB Miss ≠ Page Fault
**Setup:** "TLB miss occurs. Does a page fault occur?"

**Anti-Solution:** "Yes, TLB miss means page not in memory."

**Truth:** NO!
- **TLB miss:** VPN→PFN mapping not in TLB (go to page table)
- **Page fault:** Page not in physical memory (valid bit = 0)

**TLB miss does NOT imply page fault.** TLB is just a cache for PT.

---

### Trap #2: Page Table Size with Multi-Level
**Setup:** "32-bit VA, 4KB pages, 2-level PT. What is total PT size?"

**Anti-Solution:** Calculate full 2-level size.

**Truth:** Size depends on **how much address space is used**. Sparse usage = small PT.

**For worst case (full):** Calculate all PT1 + all PT2 tables.

---

### Trap #3: TLB Reach Confusion
**Setup:** "TLB has 64 entries, 4KB pages. What is TLB reach?"

**Answer:** $64 \times 4 \text{ KB} = 256 \text{ KB}$

**TLB Reach:** Total virtual address space covered by TLB.

**Implication:** If working set > 256 KB, TLB thrashing.

---

### Trap #4: Effective Access Time Calculation
**Setup:** Miss whether TLB is included in page table access time.

**Clarify:**
$$\text{EAT} = T_{\text{TLB}} + (\text{TLB miss rate}) \times T_{\text{PT}} + T_{\text{mem}}$$

**If page fault:** Add $(\text{PF rate}) \times T_{\text{disk}}$

---

## III. PERMANENT RECALL

### Mnemonic #1: "TLB is Cache, PT is Truth"
- **TLB:** Fast cache, small, may miss
- **Page Table:** Complete mapping, slow

### Mnemonic #2: "FIFO is Foolish, LRU is Logical"
- **FIFO:** Belady's anomaly (can be worse)
- **LRU:** Exploits locality (best practical)

### Mnemonic #3: "Offset Never Changes"
- Virtual → Physical: Only VPN→PFN translates
- Offset bits: Same in VA and PA

---

## IV. THE SOVEREIGNTY DRILLS

### Problem 1: Page Table Size
**32-bit VA, 8 KB pages, 4-byte PTE. What is page table size?**

**Solution:**
- Offset = $\log_2(8192) = 13$ bits
- VPN = $32 - 13 = 19$ bits
- # Pages = $2^{19} = 524,288$
- PT Size = $524,288 \times 4 = 2,097,152 \text{ bytes} = 2 \text{ MB}$

---

### Problem 2 (GATE 2020): TLB + Cache
**TLB: 20 ns, PT: 100 ns, Cache: 10 ns, Mem: 200 ns. TLB hit = 80%, Cache hit = 90%. Find EAT.**

**Solution:**

**With TLB hit (80%):**
- TLB access: 20 ns
- Cache access: 10 ns (90% hit) or 200 ns (10% miss)
- Time = $20 + 0.9(10) + 0.1(200) = 20 + 9 + 20 = 49$ ns

**With TLB miss (20%):**
- TLB: 20 ns
- PT access: 100 ns
- Then cache access: 10 or 200 ns
- Time = $20 + 100 + 0.9(10) + 0.1(200) = 149$ ns

**EAT:**
$$0.8(49) + 0.2(149) = 39.2 + 29.8 = 69 \text{ ns}$$

---

**Logic Singularity verified for 2026 (IIT-G Standards).**

*"Virtual memory: The greatest illusion in computing."*
