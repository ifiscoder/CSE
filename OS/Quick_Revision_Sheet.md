# Quick Revision Sheet - 1 Hour Before GATE 2026

## ⚡ The Atomic Truths (30 seconds)

1. **OS** = Resource Manager + Abstraction Layer
2. **Process** = Program in Execution State
3. **Scheduling** = Optimal Resource Allocation Under Constraints
4. **Synchronization** = Ordering Concurrent Accesses to Shared State
5. **Deadlock** = Circular Wait for Resources
6. **Memory Management** = Illusion of Infinite, Private Address Space
7. **Virtual Memory** = Execute Programs Larger Than Physical Memory
8. **File System** = Abstraction Over Raw Storage Blocks
9. **Disk Scheduling** = Minimize Seek Time + Rotational Latency

---

## 🎯 Critical Formulas (5 minutes)

### CPU Scheduling
```
TAT = T_completion - T_arrival
WT = TAT - T_burst = (Total time - Arrival) - Burst
RT = T_first_run - T_arrival
CPU Utilization = 1 - p^n  (p = I/O fraction, n = multiprogramming degree)
```

### Context Switching
```
Overhead % = T_cs / (T_cs + Q) × 100
Number of switches = N - 1  (for N processes, NOT N!)
```

### Process Creation
```
Total processes after N sequential forks = 2^N
Total processes after N conditional forks (break after child) = N + 1
```

### Memory Management
```
Logical Address = p × PageSize + d
  where p = page number, d = offset
Physical Address = f × PageSize + d
  where f = frame number (from page table)

Page Number = ⌊Logical Address / PageSize⌋
Offset = Logical Address mod PageSize

Page Table Entries = 2^(address_bits - offset_bits)
Page Table Size = Entries × Entry_Size

Internal Fragmentation (average) = 0.5 × Page_Size
```

### TLB & Virtual Memory
```
EAT (with TLB) = α × T_mem + (1-α) × 2T_mem
  Simplified: EAT = (2 - α) × T_mem
  where α = TLB hit ratio

EAT (with Page Faults) = (1-p) × T_mem + p × T_pf
  where p = page fault rate, T_pf ≈ 10 ms = 10,000,000 ns
```

### Disk Management
```
T_access = T_seek + T_rotational + T_transfer

Average Rotational Latency = 60 / (2 × RPM)  seconds
  Examples:
    7200 RPM → 4.17 ms
    10000 RPM → 3 ms

T_transfer = Size / Transfer_Rate
```

### RAID Capacity
```
RAID 0 (Striping): N × Disk_Size
RAID 1 (Mirroring): N / 2 × Disk_Size  (50% capacity)
RAID 5: (N - 1) × Disk_Size
RAID 6: (N - 2) × Disk_Size
RAID 10: N / 2 × Disk_Size
```

### File Systems
```
Pointers per Block = Block_Size / Pointer_Size

Direct Pointers Max = D × Block_Size
Single Indirect Max = N × Block_Size
Double Indirect Max = N² × Block_Size
Triple Indirect Max = N³ × Block_Size

where D = number of direct pointers, N = pointers per block
```

---

## ⚠️ Top 20 Traps (10 minutes)

### Process Management
1. ✋ **Context switch after last process:** NO switch after completion
2. ✋ **Fork tree exponential:** Only if ALL processes fork (conditional fork = linear)
3. ✋ **Zombie vs Orphan:**
   - Zombie = terminated but parent hasn't called `wait()` (holds PID)
   - Orphan = parent terminated first (adopted by init)
4. ✋ **Thread creation is free:** FALSE (costs 10-100 μs for stack allocation)

### CPU Scheduling
5. ✋ **SRTF is always optimal:** TRUE for TAT/WT, FALSE for other metrics
6. ✋ **RR optimizes TAT:** FALSE (RR optimizes **response time**, not TAT)
7. ✋ **As quantum → ∞:** RR → FCFS
8. ✋ **FCFS has lowest overhead:** TRUE (fewest context switches: N-1)

### Synchronization
9. ✋ **Semaphore init for mutex:** 1 (not 0!)
10. ✋ **Binary semaphore = Mutex:** Mostly, but mutex requires same thread to unlock
11. ✋ **Signal before wait:** Increments value, no deadlock (but semantically wrong)
12. ✋ **Peterson's on modern CPUs:** Requires memory barriers (instruction reordering breaks it)

### Deadlocks
13. ✋ **Cycle in RAG → Deadlock:** TRUE for **single-instance** resources only
14. ✋ **Safe state means no deadlock currently:** TRUE, and no deadlock CAN occur
15. ✋ **Banker's prevents deadlock:** TRUE (ensures safe state always)

### Memory & Virtual Memory
16. ✋ **Paging eliminates all fragmentation:** FALSE (eliminates external, but internal remains)
17. ✋ **Larger page size reduces internal frag:** FALSE (INCREASES it! avg = 0.5 × page size)
18. ✋ **TLB miss = Page fault:** FALSE!
    - TLB miss → access page table in memory
    - Page fault → page is on disk (must read from disk)
19. ✋ **Belady's Anomaly:** Only **FIFO** suffers (not LRU/Optimal)
20. ✋ **1% page fault rate is acceptable:** FALSE (causes 1000× slowdown!)

---

## 🧮 Quick Calculation Shortcuts (5 minutes)

### 1. Page Table Entries (Fast)
**Given:** 32-bit address, 4 KB pages
**Shortcut:** $2^{32} / 2^{12} = 2^{20} = 1$ million entries

**Given:** 64-bit address, 4 KB pages
**Shortcut:** $2^{64} / 2^{12} = 2^{52}$ entries (way too large → use multi-level)

### 2. TLB Hit Ratio Effect
**Quick Estimate:**
- 80% hit: EAT = 1.2 × T_mem
- 90% hit: EAT = 1.1 × T_mem
- 95% hit: EAT = 1.05 × T_mem
- 100% hit: EAT = 1.0 × T_mem

### 3. SRTF Gantt Chart (Fast Method)
1. List arrivals on timeline
2. At each decision point, pick smallest remaining time
3. Mark preemptions clearly

### 4. Banker's Algorithm (Fast Check)
1. Find process with Need ≤ Available
2. Add its allocation to available
3. Repeat until all finish (safe) or stuck (unsafe)

### 5. Disk Scheduling Head Movement
**FCFS:** Sum absolute differences in order
**SSTF:** Greedy (pick nearest each time)
**SCAN:** Go to end, then reverse (or last request for LOOK)

---

## 🎯 Elimination Strategy (MCQs) (2 minutes)

### Step 1: Eliminate Absurd Options
**Example:** "Acceptable page fault rate?"
- 50% ← **Absurd** (system would crawl)
- 0.01% ← **Realistic**

### Step 2: Check Units
**If calculating time, all must be same unit (ns, μs, ms)**

### Step 3: Dimensional Analysis
**If result doesn't match expected dimension, formula is wrong**

---

## 📊 Algorithm Comparison Tables (5 minutes)

### CPU Scheduling Algorithms

| Algorithm | Preemptive? | Starvation? | Optimal? | Overhead |
|-----------|-------------|-------------|----------|----------|
| FCFS | No | No | No | Lowest |
| SJF | No | Yes | Yes (for TAT) | Low |
| SRTF | Yes | Yes | Yes (for TAT) | Medium |
| Priority | Both | Yes (without aging) | No | Medium |
| RR | Yes | No | No (but fair) | High |
| MLFQ | Yes | No (with aging) | Adaptive | High |

### Page Replacement Algorithms

| Algorithm | Page Faults | Belady's? | Clairvoyance? | Practical? |
|-----------|-------------|-----------|---------------|------------|
| FIFO | High | Yes | No | Yes (simple) |
| Optimal | Minimum | No | Yes (needs future) | No (benchmark) |
| LRU | Low | No | No | Yes (with approx) |
| Clock | Medium | No | No | Yes (common) |

### Disk Scheduling Algorithms

| Algorithm | Starvation? | Fairness | Performance | Use Case |
|-----------|-------------|----------|-------------|----------|
| FCFS | No | High | Poor | Simple systems |
| SSTF | Yes | Low | Best | Heavy load |
| SCAN | No | Medium | Good | Balanced |
| C-SCAN | No | High | Good | Uniform wait |
| LOOK | No | Medium | Better | Modern OS |

---

## 🧠 Mental Imagery (Quick Recall) (5 minutes)

### Process States (Draw This in 10 seconds)
```
NEW → READY ⇄ RUNNING → TERMINATED
         ↓       ↑
       WAITING ──┘
```

### Deadlock Conditions (4 Horsemen)
1. **Mutual Exclusion** (resource non-shareable)
2. **Hold and Wait** (hold one, wait for another)
3. **No Preemption** (can't forcibly take resource)
4. **Circular Wait** (P1 → P2 → ... → P1)

**ALL FOUR must hold for deadlock!**

### RAID Levels (Visual)
```
RAID 0: [A|B|C|D]  (stripe, fast, no redundancy)
RAID 1: [A|A][B|B]  (mirror, safe, 50% capacity)
RAID 5: [A|B|C|P]  (parity distributed)
```

---

## ⚡ 5-Second Decision Trees (5 minutes)

### Q: Which scheduling algorithm?
```
Real-time system? → Priority (with EDF)
Minimize TAT, know burst times? → SJF/SRTF
Fair time-sharing? → RR
Adaptive I/O vs CPU? → MLFQ
```

### Q: Which page replacement?
```
Benchmark comparison? → Optimal
Good practical performance? → LRU or Clock
Simplest implementation? → FIFO
```

### Q: Which disk scheduling?
```
Fairness critical? → SCAN/C-SCAN
Minimize seek time? → SSTF (but risks starvation)
Modern OS default? → C-LOOK
```

### Q: Which RAID level?
```
Critical data (no downtime)? → RAID 1 or RAID 10
Balance performance + redundancy? → RAID 5
Survive 2 disk failures? → RAID 6
High performance, no redundancy? → RAID 0 (risky!)
```

---

## 🎲 Common Question Patterns (5 minutes)

### Pattern 1: "Calculate Average TAT/WT"
**Steps:**
1. Draw Gantt chart (or timeline table)
2. Mark completion times
3. TAT = Completion - Arrival (for each process)
4. WT = TAT - Burst (for each process)
5. Average = Sum / N

**Trap:** Don't forget arrival time in TAT calculation!

### Pattern 2: "Is system safe? (Banker's)"
**Steps:**
1. Calculate Need = Max - Allocation
2. Find process where Need ≤ Available
3. Execute it (add allocation to available)
4. Repeat until all finish (safe) or stuck (unsafe)

**Trap:** Don't modify original allocation/max during algorithm!

### Pattern 3: "How many page faults?"
**Steps:**
1. Trace reference string
2. Mark fault when page not in memory
3. Apply replacement algorithm when frames full

**Trap:** Don't count a "fault" when page is already in memory (hit)!

### Pattern 4: "Total head movement (disk)"
**Steps:**
1. Sort requests if needed (for SCAN/C-SCAN)
2. Trace head movement
3. Sum absolute differences

**Trap:** For C-SCAN, count the "jump" from end to start!

---

## 🔥 Pre-Exam Mantra (1 minute)

**Repeat 3 times before entering exam hall:**

1. **"I recognize patterns, not memorize."**
2. **"I identify traps before I fall."**
3. **"I check units and dimensions."**
4. **"I eliminate absurd options first."**
5. **"I stay calm and execute surgically."**

---

## ⏱️ Time Management (Exam Day)

### OS Section (17 marks in GATE)
- **1-mark questions:** 60-90 seconds each
- **2-mark questions:** 2-3 minutes each
- **If stuck beyond 1 minute:** Mark for review, move on

### Panic Reset Protocol
1. Close eyes (5 seconds)
2. Deep breath (3 seconds)
3. Re-read question (10 seconds)
4. Identify topic (5 seconds)
5. Execute (remaining time)

---

## ✅ Final Checklist (30 seconds before exam)

- [ ] Formula sheet reviewed
- [ ] Top 20 traps memorized
- [ ] Calculator/rough paper ready
- [ ] Water bottle (stay hydrated)
- [ ] Confidence: HIGH
- [ ] Panic: ZERO

---

**YOU ARE READY FOR RANK-1.**

**Execute with surgical precision. 🚀**

**All the best for GATE/ESE 2026! 🏆**
