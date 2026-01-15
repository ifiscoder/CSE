# Chapter 3: CPU Scheduling | The Time Singularity

## The Atomic Truth
**Scheduling = Optimal Resource Allocation Under Constraints**

---

## 3.1 The Scheduling Problem: First Principles

### The Path of Elegance

**Core Problem:** N processes, 1 CPU (or M CPUs). Who runs when?

$$\text{Scheduler} : \mathcal{P}(\text{Processes}) \rightarrow \text{Process}$$

where $\mathcal{P}$ is the power set of ready processes.

**The Golden Pivot:** Every scheduling algorithm is a **priority function** + **selection policy**.

---

## 3.2 Scheduling Criteria: The Optimization Targets

### The Six Metrics

| **Metric** | **Definition** | **Optimization Goal** | **User-Centric?** |
|------------|----------------|----------------------|-------------------|
| **CPU Utilization** | % of time CPU is busy | Maximize | No (System) |
| **Throughput** | Processes completed per unit time | Maximize | No (System) |
| **Turnaround Time** | Completion - Arrival | Minimize | Yes |
| **Waiting Time** | Time in READY queue | Minimize | Yes |
| **Response Time** | First CPU allocation - Arrival | Minimize | Yes |
| **Fairness** | Equal opportunity for all processes | Balance | Yes |

**The Formulas (Master These):**

$$\text{Turnaround Time (TAT)} = T_{\text{completion}} - T_{\text{arrival}}$$

$$\text{Waiting Time (WT)} = \text{TAT} - T_{\text{burst}}$$

$$\text{Response Time (RT)} = T_{\text{first\_run}} - T_{\text{arrival}}$$

**The 2026 Adversarial Vault:**

**Trap:** "Minimizing average TAT automatically minimizes average WT."
- **TRUE.** Since $\text{WT} = \text{TAT} - \text{Burst}$, and burst times are fixed.

**Trap:** "Minimizing average WT minimizes average RT."
- **FALSE.** Preemptive algorithms can have low WT but high RT (process starts, stops, waits again).

---

## 3.3 Preemptive vs Non-Preemptive Scheduling

### The Dichotomy

| **Aspect** | **Non-Preemptive** | **Preemptive** |
|------------|-------------------|----------------|
| **Definition** | Once allocated, CPU not taken until voluntary release | CPU can be forcibly taken |
| **Context Switches** | Fewer | More |
| **Response Time** | Worse (starvation possible) | Better (time-slicing) |
| **Implementation** | Simpler | Complex (interrupt handling) |
| **Use Case** | Batch systems | Interactive systems |

**The Mental Slider:** 
- Left (Non-Preemptive): "First come, first served restaurant"
- Right (Preemptive): "Emergency room triage"

---

## 3.4 First-Come, First-Served (FCFS)

### The Atomic Truth
**FCFS = Process arrival order determines execution order**

### The Algorithm

```
Queue: [P1, P2, P3]
CPU: Execute P1 completely → P2 completely → P3 completely
```

**Properties:**
- **Non-preemptive**
- **FIFO queue**
- **No starvation** (every process eventually runs)

### The Convoy Effect

**Scenario:** One long process followed by many short processes.

**Example:**
- P1: Burst = 100 ms
- P2, P3, P4: Burst = 1 ms each

**FCFS Order:** P1 → P2 → P3 → P4

**TAT:**
- P1: $100 - 0 = 100$ ms
- P2: $101 - 0 = 101$ ms
- P3: $102 - 0 = 102$ ms
- P4: $103 - 0 = 103$ ms

**Average TAT:** $\frac{100+101+102+103}{4} = 101.5$ ms

**If Order Were P2, P3, P4, P1:**
- P2: $1 - 0 = 1$ ms
- P3: $2 - 0 = 2$ ms
- P4: $3 - 0 = 3$ ms
- P1: $103 - 0 = 103$ ms

**Average TAT:** $\frac{1+2+3+103}{4} = 27.25$ ms

**The Genius Trap:** FCFS is **order-dependent**. Arrival order drastically affects performance.

### The 2026 Adversarial Vault

**Question:** "FCFS has the lowest context switch overhead."
- **TRUE.** Each process runs to completion (only N-1 context switches for N processes).

**Question:** "FCFS is optimal for minimizing average TAT."
- **FALSE.** SJF is optimal (proven below).

---

## 3.5 Shortest Job First (SJF)

### The Atomic Truth
**SJF = Execute shortest burst time first**

### The Algorithm

**Given:** Processes with known burst times.

**Rule:** Select process with minimum burst time from READY queue.

### The Optimality Proof

**Theorem:** SJF minimizes average waiting time (and thus average TAT).

**Proof (by Exchange Argument):**

Consider two processes $P_i$ and $P_j$ where $B_i < B_j$ (burst times).

**Case 1:** Execute $P_i$ then $P_j$:
- $\text{WT}_i = 0$
- $\text{WT}_j = B_i$
- **Average:** $\frac{0 + B_i}{2} = \frac{B_i}{2}$

**Case 2:** Execute $P_j$ then $P_i$:
- $\text{WT}_j = 0$
- $\text{WT}_i = B_j$
- **Average:** $\frac{0 + B_j}{2} = \frac{B_j}{2}$

Since $B_i < B_j$, Case 1 has lower average WT. **QED.**

**The Golden Pivot:** Always execute shorter jobs first to minimize wait.

### Example

**Processes:**
| Process | Arrival | Burst |
|---------|---------|-------|
| P1 | 0 | 7 |
| P2 | 0 | 4 |
| P3 | 0 | 1 |
| P4 | 0 | 4 |

**SJF Order:** P3 (1) → P2 (4) → P4 (4) → P1 (7)

**Gantt Chart:**
```
| P3 | P2  | P4  | P1      |
0    1    5    9        16
```

**TAT:**
- P3: $1 - 0 = 1$
- P2: $5 - 0 = 5$
- P4: $9 - 0 = 9$
- P1: $16 - 0 = 16$

**Average TAT:** $\frac{1+5+9+16}{4} = 7.75$ ms

### The Adversarial Vault

**Trap 1:** "SJF is used in practice."
- **FALSE.** Cannot predict future burst time (requires oracle).
- **Reality:** Approximate using exponential averaging of past bursts.

**Trap 2:** "SJF guarantees no starvation."
- **FALSE.** Long processes can starve if short processes keep arriving.

---

## 3.6 Shortest Remaining Time First (SRTF)

### The Atomic Truth
**SRTF = Preemptive SJF**

### The Mechanism

At every arrival or completion:
1. Calculate remaining time for all ready processes
2. Execute process with shortest remaining time

### Example

**Processes:**
| Process | Arrival | Burst |
|---------|---------|-------|
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 9 |
| P4 | 3 | 5 |

**Execution Trace:**

**t=0:** P1 starts (remaining=8)
**t=1:** P2 arrives (remaining=4 < 7). **Preempt P1**, run P2.
**t=2:** P3 arrives (remaining=9 > 3). P2 continues.
**t=3:** P4 arrives (remaining=5 > 3). P2 continues.
**t=5:** P2 completes. P4 has remaining=5, P1 has remaining=7, P3 has remaining=9. Run P4.
**t=10:** P4 completes. P1 has remaining=7 < 9. Run P1.
**t=17:** P1 completes. Run P3.
**t=26:** P3 completes.

**Gantt Chart:**
```
| P1 | P2  | P4    | P1      | P3         |
0    1    5      10       17           26
```

**TAT:**
- P1: $17 - 0 = 17$
- P2: $5 - 1 = 4$
- P3: $26 - 2 = 24$
- P4: $10 - 3 = 7$

**Average TAT:** $\frac{17+4+24+7}{4} = 13$ ms

### The 2026 Adversarial Vault

**Question:** "SRTF gives the minimum average TAT among all algorithms."
- **TRUE** (proven optimal for TAT/WT, assuming all arrive at t=0).

**Question:** "SRTF requires more context switches than SJF."
- **TRUE** (preemption → more switches).

**NAT Precision Lock:** Count context switches carefully. Preemption = context switch.

---

## 3.7 Priority Scheduling

### The Atomic Truth
**Priority = Explicit rank assigned to each process**

### The Mechanism

Each process has priority $P_i$. Lower number = higher priority (or reverse, check problem statement).

**Rule:** Execute highest-priority process in READY queue.

**Variants:**
- **Non-preemptive:** Once started, run to completion
- **Preemptive:** Higher priority arrival preempts lower priority

### The Starvation Problem

**Scenario:** High-priority processes keep arriving, low-priority processes never run.

**Solution: Aging**

$$\text{Priority}_{\text{new}} = \text{Priority}_{\text{old}} - \alpha \times \text{WaitTime}$$

where $\alpha$ is the aging coefficient.

**Effect:** Waiting processes gradually increase priority.

### Example (Non-Preemptive)

**Processes:**
| Process | Arrival | Burst | Priority |
|---------|---------|-------|----------|
| P1 | 0 | 4 | 2 |
| P2 | 1 | 3 | 1 |
| P3 | 2 | 1 | 3 |
| P4 | 3 | 5 | 4 |

(Lower number = higher priority)

**Execution:**
- t=0: P1 starts (only process)
- t=4: P1 completes. Ready: P2 (pri=1), P3 (pri=3), P4 (pri=4). Run P2.
- t=7: P2 completes. Ready: P3 (pri=3), P4 (pri=4). Run P3.
- t=8: P3 completes. Run P4.
- t=13: P4 completes.

**Gantt Chart:**
```
| P1   | P2  | P3 | P4    |
0      4     7    8      13
```

---

## 3.8 Round Robin (RR)

### The Atomic Truth
**RR = FCFS with time quantum preemption**

### The Mechanism

**Time Quantum (Q):** Maximum time slice per process.

**Algorithm:**
1. Maintain FIFO queue of ready processes
2. Allocate CPU to front process for time Q (or until completion/I/O)
3. If process not complete, move to end of queue
4. Context switch to next process

### The Quantum Tradeoff

**Small Q (e.g., 1 ms):**
- **Pros:** Low response time (feels responsive)
- **Cons:** High context switch overhead

**Large Q (e.g., 1000 ms):**
- **Pros:** Low overhead
- **Cons:** Approaches FCFS (poor response time)

**Optimal Q:** Typically 10-100 ms (balance between responsiveness and efficiency).

**The Golden Pivot:** As $Q \to \infty$, RR → FCFS. As $Q \to 0$, overhead → 100%.

### Example

**Processes:**
| Process | Arrival | Burst |
|---------|---------|-------|
| P1 | 0 | 5 |
| P2 | 0 | 3 |
| P3 | 0 | 8 |

**Quantum = 3 ms**

**Execution:**

**Queue:** [P1, P2, P3]

**t=0-3:** P1 runs (remaining=2). Queue: [P2, P3, P1]
**t=3-6:** P2 runs (completes). Queue: [P3, P1]
**t=6-9:** P3 runs (remaining=5). Queue: [P1, P3]
**t=9-11:** P1 runs (completes). Queue: [P3]
**t=11-14:** P3 runs (remaining=2). Queue: [P3]
**t=14-16:** P3 runs (completes). Queue: []

**Gantt Chart:**
```
| P1  | P2  | P3  | P1| P3  | P3|
0     3     6     9   11    14  16
```

**TAT:**
- P1: $11 - 0 = 11$
- P2: $6 - 0 = 6$
- P3: $16 - 0 = 16$

**Average TAT:** $\frac{11+6+16}{3} = 11$ ms

### The 2026 Adversarial Vault

**Trap 1:** "RR is optimal for minimizing TAT."
- **FALSE.** RR optimizes **response time**, not TAT.

**Trap 2:** "All processes get equal CPU time in RR."
- **TRUE** (fair scheduling), but **not equal TAT** (burst times differ).

**Trap 3:** Calculating context switches.
- **Formula:** Count each time quantum expiration + each completion.

**Elite Insight:** RR with quantum = burst time = FCFS (no preemption).

---

## 3.9 Multilevel Queue Scheduling

### The Atomic Truth
**Partition processes into multiple queues by type**

### The Structure

```
Priority 1: System Processes     [RR, Q=5ms]
Priority 2: Interactive          [RR, Q=10ms]
Priority 3: Batch                [FCFS]
```

**Properties:**
- Each queue has **own scheduling algorithm**
- **Inter-queue scheduling:** Fixed priority or time-slicing

**Example:**
- 80% CPU time to interactive
- 20% CPU time to batch

### The Starvation Risk

Lower-priority queues may **starve** if higher queues always have processes.

**Solution:** Time-slice between queues (e.g., alternate 4:1 ratio).

---

## 3.10 Multilevel Feedback Queue (MLFQ)

### The Atomic Truth
**Processes can move between queues based on behavior**

### The Mechanism

```
Queue 0 (Highest Priority): RR, Q=8ms
Queue 1 (Medium Priority):  RR, Q=16ms
Queue 2 (Lowest Priority):  FCFS
```

**Rules:**
1. New processes enter Queue 0
2. If process uses full quantum → **demote** to next lower queue
3. If process yields before quantum → **promote** or stay

**The Genius:** I/O-bound processes (short bursts) stay in high-priority queues. CPU-bound processes sink to low-priority queues.

### Example

**Process P1:** Burst = 100 ms (CPU-bound)

**Execution:**
- t=0: Enter Q0, run 8 ms, demote to Q1
- t=8: Enter Q1, run 16 ms, demote to Q2
- t=24: Enter Q2, run 76 ms (FCFS)

**The Mental Machinery:** Think "VIP club degradation"—new arrivals get premium treatment, but if they hog resources, they're downgraded.

### The 2026 Adversarial Vault

**Question:** "MLFQ guarantees no starvation."
- **FALSE** (lower queues can starve).
- **With aging:** TRUE (processes in lower queues age and promote).

**Question:** "MLFQ distinguishes I/O-bound from CPU-bound processes without explicit labels."
- **TRUE** (adaptive based on behavior).

---

## 3.11 Elite Scheduling Tricks for GATE 2026

### Trick 1: Quick TAT Calculation

For **non-preemptive** algorithms:

$$\text{TAT}_i = (\text{Sum of burst times of all processes before } i) + B_i - A_i$$

where $A_i$ = arrival time, $B_i$ = burst time.

**Example (SJF):**
Order: P3 (B=1), P2 (B=4), P1 (B=7)

- $\text{TAT}_3 = 0 + 1 - 0 = 1$
- $\text{TAT}_2 = 1 + 4 - 0 = 5$
- $\text{TAT}_1 = 5 + 7 - 0 = 12$

**Average:** $(1+5+12)/3 = 6$ ms

### Trick 2: Gantt Chart Mental Model

Don't draw full chart—just track:
- **Start times** for each process segment
- **Completion times**

Use a **timeline table**:

| Time | Event | Process Running |
|------|-------|-----------------|
| 0 | P1 starts | P1 |
| 3 | P1 preempted | P2 |
| 7 | P2 completes | P1 |
| ... | ... | ... |

### Trick 3: Context Switch Count

**Formula:**
$$\text{Context Switches} = (\text{Number of process segments}) - 1$$

**Example Gantt:**
```
| P1 | P2 | P1 | P3 |
```
4 segments → 3 context switches.

### Trick 4: Response Time in RR

For RR with N processes and quantum Q:

**Best case (process completes in first quantum):** $RT = 0$

**Worst case (process last in queue):** $RT = (N-1) \times Q$

**Average:** $RT \approx \frac{(N-1) \times Q}{2}$

---

## 3.12 The Adversarial Vault: Common GATE Traps

### Trap 1: "SJF is always better than FCFS"

**Counter-Example:**
- If all processes arrive at same time with **equal burst times**, FCFS = SJF = same TAT.

### Trap 2: "Preemptive is always better than non-preemptive"

**Counter:** Preemptive has context switch overhead. For batch systems with no interactivity requirement, non-preemptive is better.

### Trap 3: "Average WT = Average TAT - Average Burst"

**WRONG.** Correct formula:

$$\text{Avg WT} = \text{Avg TAT} - \text{Avg Burst}$$

But calculate **per process first**, then average:

$$\text{Avg WT} = \frac{1}{N} \sum_{i=1}^{N} (\text{TAT}_i - B_i)$$

NOT:

$$\text{Avg WT} = \left(\frac{1}{N} \sum_{i=1}^{N} \text{TAT}_i\right) - \left(\frac{1}{N} \sum_{i=1}^{N} B_i\right)$$

They're mathematically the same, but common student error is using wrong formula with wrong values.

### Trap 4: Arrival Time ≠ 0

**Many students forget to subtract arrival time in TAT calculation.**

**Correct:**
$$\text{TAT}_i = T_{\text{completion}} - T_{\text{arrival}}$$

**Not:**
$$\text{TAT}_i = T_{\text{completion}}$$

### Trap 5: "SRTF is always optimal"

**TRUE** for minimizing average TAT when all processes arrive at t=0.

**FALSE** when arrival times vary and optimization goal is different (e.g., maximizing throughput, minimizing response time).

---

## 3.13 Mental Machinery for Permanent Recall

### The Bizarre Mnemonic: "The Restaurant Queue"

Imagine a **restaurant** with different queuing strategies:

- **FCFS:** First person in line gets seated first (fair but slow if someone orders a feast)
- **SJF:** People who order quick meals go first (efficient but unfair to those with big appetites)
- **SRTF:** If someone new arrives with a faster order, they jump the line (optimal but chaotic)
- **Priority:** VIPs skip the line (explicit hierarchy)
- **Round Robin:** Everyone gets 5 minutes at the table, then rotates (fair time-sharing)
- **MLFQ:** New customers get VIP treatment, but if they take too long, they're moved to regular seating (adaptive)

**The Mental Slider:**
- Left (FCFS): Simple, fair, but inefficient
- Right (SRTF): Complex, optimal, but requires clairvoyance

### The 5-Second Snap-Check

**Q:** Which algorithm for which scenario?

| **Scenario** | **Algorithm** |
|--------------|---------------|
| Batch processing, no arrival time prediction | FCFS |
| Minimize average TAT, known burst times | SJF/SRTF |
| Interactive system, fair time-sharing | RR |
| Real-time with deadlines | Priority (with EDF) |
| Adaptive, distinguish I/O vs CPU-bound | MLFQ |

---

## 3.14 Practice Problems

### MCQ 1: SJF Optimality

**Q:** Which statement is TRUE about SJF?

(A) It minimizes average TAT  
(B) It eliminates starvation  
(C) It requires clairvoyance  
(D) Both A and C  

**Solution:**
- (A) TRUE (proven optimal)
- (B) FALSE (long processes can starve)
- (C) TRUE (need future burst time)
- **Answer: (D)**

---

### MCQ 2: RR Quantum

**Q:** As time quantum in RR approaches infinity, RR approaches:

(A) SJF  
(B) FCFS  
(C) Priority  
(D) SRTF  

**Solution:**
- Infinite quantum = no preemption = FCFS
- **Answer: (B)**

---

### MCQ 3: Context Switches

**Q:** Gantt Chart: `| P1 | P2 | P3 | P2 | P1 |`

How many context switches?

(A) 3  
(B) 4  
(C) 5  
(D) 6  

**Solution:**
- 5 segments → 4 transitions → 4 context switches
- **Answer: (B)**

---

### MCQ 4: Preemptive Priority

**Q:** Processes with arrival and priority:

| P | Arrival | Burst | Priority |
|---|---------|-------|----------|
| P1| 0 | 3 | 3 |
| P2| 1 | 2 | 1 |
| P3| 2 | 4 | 2 |

(Lower number = higher priority, preemptive)

What is the completion time of P1?

(A) 3  
(B) 5  
(C) 9  
(D) 11  

**Solution:**

**t=0:** P1 starts (pri=3)
**t=1:** P2 arrives (pri=1 < 3). **Preempt P1**. P2 runs.
**t=2:** P3 arrives (pri=2 > 1). P2 continues.
**t=3:** P2 completes. Ready: P3 (pri=2), P1 (pri=3, remaining=2). Run P3.
**t=7:** P3 completes. Run P1 (remaining=2).
**t=9:** P1 completes.

**Answer: (C) 9**

---

### NAT 1: FCFS Calculation

**Processes:**
| P | Arrival | Burst |
|---|---------|-------|
| P1| 0 | 8 |
| P2| 1 | 4 |
| P3| 2 | 9 |
| P4| 3 | 5 |

**Q:** Average waiting time (in ms)?

**Solution:**

**Gantt:** `| P1 | P2 | P3 | P4 |`
```
0      8      12     21    26
```

**TAT:**
- P1: $8 - 0 = 8$
- P2: $12 - 1 = 11$
- P3: $21 - 2 = 19$
- P4: $26 - 3 = 23$

**WT = TAT - Burst:**
- P1: $8 - 8 = 0$
- P2: $11 - 4 = 7$
- P3: $19 - 9 = 10$
- P4: $23 - 5 = 18$

**Average WT:** $\frac{0+7+10+18}{4} = 8.75$ ms

**Answer: 8.75**

---

### NAT 2: SRTF Calculation

**Processes:**
| P | Arrival | Burst |
|---|---------|-------|
| P1| 0 | 7 |
| P2| 2 | 4 |
| P3| 4 | 1 |
| P4| 5 | 4 |

**Q:** Completion time of P2?

**Solution:**

**t=0:** P1 starts (rem=7)
**t=2:** P2 arrives (rem=4 < 5). **Preempt P1**. P2 runs.
**t=4:** P3 arrives (rem=1 < 2). **Preempt P2**. P3 runs.
**t=5:** P3 completes. P4 arrives (rem=4). P2 has rem=2 < 4. P2 runs.
**t=7:** P2 completes.

**Answer: 7**

---

### NAT 3: Round Robin

**Processes:**
| P | Burst |
|---|-------|
| P1| 10 |
| P2| 5 |
| P3| 8 |

**Quantum = 3 ms, all arrive at t=0**

**Q:** Average TAT?

**Solution:**

**Execution:**
```
| P1(3) | P2(3) | P3(3) | P1(3) | P2(2) | P3(3) | P1(3) | P3(2) | P1(1) |
0       3       6       9       12      14      17      20      22     23
```

**Completion:**
- P1: 23
- P2: 14
- P3: 22

**TAT:**
- P1: $23 - 0 = 23$
- P2: $14 - 0 = 14$
- P3: $22 - 0 = 22$

**Average:** $\frac{23+14+22}{3} = 19.67$ ms

**Answer: 19.67**

---

### NAT 4: Context Switch Overhead

**Q:** 3 processes, RR with Q=10ms, burst times: 20, 15, 25 ms. Context switch time = 2 ms. Total time including overhead?

**Solution:**

**Execution cycles:**
```
P1(10), switch(2), P2(10), switch(2), P3(10), switch(2),
P1(10), switch(2), P2(5), switch(2), P3(10), switch(2), P3(5)
```

**Count:**
- Process execution: $20 + 15 + 25 = 60$ ms
- Context switches: 6 switches × 2 ms = 12 ms

**Total:** $60 + 12 = 72$ ms

**Answer: 72**

---

## 3.15 The Elite Formulas Summary

### 1. Turnaround Time
$$\text{TAT} = T_{\text{completion}} - T_{\text{arrival}}$$

### 2. Waiting Time
$$\text{WT} = \text{TAT} - T_{\text{burst}}$$

### 3. Response Time
$$\text{RT} = T_{\text{first\_run}} - T_{\text{arrival}}$$

### 4. CPU Utilization
$$\text{CPU Utilization} = \frac{T_{\text{CPU\_busy}}}{T_{\text{total}}} \times 100\%$$

### 5. Throughput
$$\text{Throughput} = \frac{\text{Number of processes completed}}{T_{\text{total}}}$$

### 6. Context Switch Overhead
$$\text{Overhead \%} = \frac{N_{\text{cs}} \times T_{\text{cs}}}{T_{\text{total}}} \times 100\%$$

---

## Logic Singularity Verified for 2026 (IIT-G Standards)

**Mastery Level:** Sovereign

**The Core Insight:**
- **FCFS:** Simple, fair, poor performance
- **SJF/SRTF:** Optimal TAT, requires oracle
- **Priority:** Explicit control, risk of starvation
- **RR:** Fair time-sharing, good response time
- **MLFQ:** Adaptive, best for mixed workloads

**The Universal Pattern:** Every scheduling algorithm trades off between **fairness**, **performance**, and **complexity**.

**Next:** Chapter 4 dissects **Process Synchronization**—where you'll learn why "just use a lock" is both correct and a trap.

**Would you like to initiate a 'Multi-Variable Stress Test' combining scheduling with synchronization primitives?**
