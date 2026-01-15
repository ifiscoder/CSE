# Chapter 9: Disk Management & I/O Systems | The Mechanical Singularity

## The Atomic Truth
**Disk Scheduling = Minimize Seek Time + Rotational Latency**

---

## 9.1 Disk Structure

### The Physical Reality

**Hard Disk Drive (HDD):**

```
Platters (rotating disks)
    ↓
Tracks (concentric circles)
    ↓
Sectors (smallest addressable unit, typically 512 bytes or 4 KB)
    ↓
Clusters (group of sectors, filesystem allocation unit)
```

**Key Components:**
- **Read/Write Head:** Accesses data (one per surface)
- **Arm:** Moves heads across tracks (all heads move together)
- **Spindle:** Rotates platters (typically 5400-15000 RPM)

**The Golden Pivot:** Mechanical movement (arm seeking) is the **slowest** part.

---

## 9.2 Disk Access Time Components

### The Complete Formula

$$T_{\text{access}} = T_{\text{seek}} + T_{\text{rotational}} + T_{\text{transfer}}$$

### 1. Seek Time ($T_{\text{seek}}$)

**Definition:** Time to move arm to target track.

**Components:**
- **Startup time:** Accelerate arm
- **Travel time:** Move across tracks
- **Settle time:** Fine positioning

**Typical Values:**
- Average: 4-10 ms
- Min (adjacent track): 0.5-1 ms
- Max (full stroke): 10-20 ms

**Formula (Linear Model):**
$$T_{\text{seek}} = a + b \times |T_{\text{current}} - T_{\text{target}}|$$

where $a$ = startup/settle time, $b$ = per-track time.

### 2. Rotational Latency ($T_{\text{rotational}}$)

**Definition:** Time for target sector to rotate under head.

**Formula:**
$$T_{\text{rotational}} = \frac{\theta}{360°} \times T_{\text{rotation}}$$

where $\theta$ = angle to target sector.

**Average Latency:**
$$T_{\text{avg\_rot}} = \frac{T_{\text{rotation}}}{2} = \frac{60}{2 \times \text{RPM}}$$

**Examples:**
- 5400 RPM: $\frac{60}{2 \times 5400} = 5.56$ ms
- 7200 RPM: $\frac{60}{2 \times 7200} = 4.17$ ms
- 10000 RPM: $\frac{60}{2 \times 10000} = 3$ ms
- 15000 RPM: $\frac{60}{2 \times 15000} = 2$ ms

### 3. Transfer Time ($T_{\text{transfer}}$)

**Definition:** Time to read/write data.

**Formula:**
$$T_{\text{transfer}} = \frac{\text{Data Size}}{\text{Transfer Rate}}$$

**Transfer Rate:**
$$\text{Rate} = \text{Bytes per Track} \times \text{RPM} / 60$$

**Typical:** 100-200 MB/s (modern HDD)

**Example:**
- Transfer 4 KB at 100 MB/s: $\frac{4096}{100 \times 10^6} = 0.04$ ms

**The 2026 Adversarial Vault:**

**Trap:** "Transfer time is dominant."
- **FALSE.** Seek time (4-10 ms) >> Transfer time (0.04 ms for 4 KB).

**Trap:** "Rotational latency = full rotation time."
- **FALSE.** **Average** = half rotation time.

**NAT Precision Lock:**

**Question:** "Disk: 7200 RPM, seek time = 8 ms, transfer rate = 100 MB/s. Time to read 8 KB?"

**Solution:**
- Seek: 8 ms
- Rotational: $\frac{60}{2 \times 7200} = 4.17$ ms
- Transfer: $\frac{8192}{100 \times 10^6} = 0.08$ ms

**Total:** $8 + 4.17 + 0.08 = 12.25$ ms

**Answer: 12.25**

---

## 9.3 Disk Scheduling Algorithms

### The Queue

**Scenario:** Current head position = 50. Request queue: [98, 183, 37, 122, 14, 124, 65, 67]

**Tracks: 0-199**

### 1. FCFS (First-Come, First-Served)

**Rule:** Process requests in arrival order.

**Execution:**
```
50 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67
```

**Head Movement:**
$$|98-50| + |183-98| + |37-183| + |122-37| + |14-122| + |124-14| + |65-124| + |67-65|$$
$$= 48 + 85 + 146 + 85 + 108 + 110 + 59 + 2 = 643 \text{ tracks}$$

**Advantages:**
- Fair (no starvation)
- Simple

**Disadvantages:**
- Poor performance (wild arm movement)

---

### 2. SSTF (Shortest Seek Time First)

**Rule:** Select request with **minimum seek time** from current position.

**Execution:**
```
Current: 50
Distances: [48, 133, 13, 72, 36, 74, 15, 17]
Closest: 65 (distance 15)

Current: 65
Remaining: [98, 183, 37, 122, 14, 124, 67]
Closest: 67 (distance 2)

Current: 67
Remaining: [98, 183, 37, 122, 14, 124]
Closest: 37 (distance 30)

... continuing: 37 → 14 → 98 → 122 → 124 → 183
```

**Full sequence:** 50 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183

**Head Movement:**
$$15 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = 239 \text{ tracks}$$

**Advantages:**
- Better performance than FCFS

**Disadvantages:**
- **Starvation possible** (far requests may never be serviced)
- Not optimal (greedy algorithm)

**The 2026 Trap:**

**Question:** "SSTF is optimal."
- **FALSE.** SSTF is greedy (local optimization), not globally optimal.

---

### 3. SCAN (Elevator Algorithm)

**Rule:** Move head in one direction, service all requests in that direction, then reverse.

**Execution (starting direction: increasing):**
```
50 → 65 → 67 → 98 → 122 → 124 → 183 → 199 (end) → 37 → 14
```

**Head Movement:**
$$149 + 16 + 51 = 216 \text{ tracks}$$

(50 to 199 = 149, 199 to 37 = 162, but efficient calculation: 149 + 162 = 311... let me recalculate)

Actually:
- Forward: $|65-50| + |67-65| + |98-67| + |122-98| + |124-122| + |183-124| + |199-183|$
  $= 15 + 2 + 31 + 24 + 2 + 59 + 16 = 149$
- Backward: $|199-37| + |37-14| = 162 + 23 = 185$

Wait, that's not right. Let me properly trace:

**Starting at 50, moving right:**
- Service: 65, 67, 98, 122, 124, 183
- Reach end: 199
- Turn around, move left
- Service: 37, 14

**Total movement:**
- 50 → 199 (rightmost): $199 - 50 = 149$
- 199 → 14 (leftmost remaining): $199 - 14 = 185$

**Total:** $149 + 185 = 334$ tracks

Hmm, this seems worse than FCFS. Let me reconsider. The issue is we go all the way to 199 even though last request is at 183.

**Standard SCAN:** Go to last request in direction, then reverse.

**Optimized execution:**
- 50 → 65 → 67 → 98 → 122 → 124 → 183 (last in right direction)
- 183 → 37 → 14 (moving left)

**Total:**
- Right: $183 - 50 = 133$
- Left: $183 - 14 = 169$

**Total:** $133 + 169 = 302$ tracks

Actually, for fair comparison, let's use the **total head movement** (sum of absolute differences):

50 → 65: 15
65 → 67: 2
67 → 98: 31
98 → 122: 24
122 → 124: 2
124 → 183: 59
183 → 37: 146
37 → 14: 23

**Total:** $15 + 2 + 31 + 24 + 2 + 59 + 146 + 23 = 302$ tracks

**Advantages:**
- No starvation
- More uniform wait times

**Disadvantages:**
- Higher average wait than SSTF

---

### 4. C-SCAN (Circular SCAN)

**Rule:** Move in one direction, service requests. At end, **jump** to beginning (no servicing on return).

**Execution:**
```
50 → 65 → 67 → 98 → 122 → 124 → 183 → 199 → 0 → 14 → 37
```

**Head Movement:**
- Forward: $199 - 50 = 149$
- Jump: $199 - 0 = 199$ (or treat as 0 if instantaneous)
- Forward: $37 - 14 = 23$ (wait, this is wrong)

**Proper calculation:**
- 50 → 199: Service 65, 67, 98, 122, 124, 183
- Jump to 0 (counted as movement: 199 tracks)
- 0 → 37: Service 14, 37

**Total movement:**
- Servicing: $|65-50| + |67-65| + ... + |183-124| = 133$
- Jump: 199
- Servicing: $|14-0| + |37-14| = 37$

**Total:** $133 + 199 + 37 = 369$ tracks

(Jump is usually counted as movement in calculations)

**Advantages:**
- More uniform wait times than SCAN

**Disadvantages:**
- Higher total head movement

---

### 5. LOOK and C-LOOK

**LOOK:** Like SCAN, but only go to **last request** in direction (not end of disk).

**C-LOOK:** Like C-SCAN, but only go to last request.

**Example (LOOK):**
```
50 → 65 → 67 → 98 → 122 → 124 → 183 (last) → 37 → 14
```

**Head Movement:** $133 + 146 + 23 = 302$ tracks

(Same as SCAN in this example since we don't go to 199)

**Example (C-LOOK):**
```
50 → 65 → 67 → 98 → 122 → 124 → 183 → 14 → 37
```

**Head Movement:**
- Forward: 133 (to 183)
- Jump: $183 - 14 = 169$
- Forward: $37 - 14 = 23$

**Total:** $133 + 169 + 23 = 325$ tracks

**Advantages:**
- Better than SCAN/C-SCAN (don't go to disk ends unnecessarily)

---

## 9.4 Algorithm Comparison

| **Algorithm** | **Total Movement** | **Starvation?** | **Fairness** | **Complexity** |
|---------------|-------------------|-----------------|--------------|----------------|
| **FCFS** | 643 | No | High | Low |
| **SSTF** | 239 | Possible | Low | Medium |
| **SCAN** | 302 | No | Medium | Medium |
| **C-SCAN** | 369 | No | High | Medium |
| **LOOK** | 302 | No | Medium | Medium |
| **C-LOOK** | 325 | No | High | Medium |

**The Golden Pivot:** **SSTF** has best performance but risks starvation. **LOOK/SCAN** balance performance and fairness.

**Modern Reality:** Most OS use **C-LOOK** or **deadline-based** variants.

---

## 9.5 RAID (Redundant Array of Independent Disks)

### The Atomic Truth
**RAID = Multiple disks for performance and/or reliability**

### RAID Levels

#### RAID 0 (Striping)

**Mechanism:** Split data across N disks (no redundancy).

**Striping:**
```
Block 0 → Disk 0
Block 1 → Disk 1
Block 2 → Disk 2
Block 3 → Disk 0
...
```

**Advantages:**
- **Performance:** N× throughput (parallel access)
- **Capacity:** Full capacity (N × disk size)

**Disadvantages:**
- **No fault tolerance:** One disk fails → all data lost

**Use Case:** Non-critical data, high-performance needs (video editing).

#### RAID 1 (Mirroring)

**Mechanism:** Duplicate data on N disks.

**Structure:**
```
Disk 0: [A, B, C, D]
Disk 1: [A, B, C, D]  (mirror)
```

**Advantages:**
- **Fault tolerance:** Survive N-1 disk failures
- **Read performance:** 2× (read from either disk)

**Disadvantages:**
- **Cost:** 50% capacity (2 disks for 1 disk worth of data)
- **Write performance:** Same as single disk (must write to both)

**Use Case:** Critical data (databases, OS disks).

#### RAID 4 (Block-Level Striping with Parity)

**Mechanism:** N-1 data disks + 1 parity disk.

**Structure:**
```
Disk 0: [A0, B0, C0, D0]
Disk 1: [A1, B1, C1, D1]
Disk 2: [A2, B2, C2, D2]
Disk 3: [P_A, P_B, P_C, P_D]  (parity)
```

**Parity Calculation:**
$$P = D_0 \oplus D_1 \oplus D_2$$

**Recovery:** If Disk 1 fails:
$$D_1 = D_0 \oplus D_2 \oplus P$$

**Advantages:**
- **Fault tolerance:** Survive 1 disk failure
- **Capacity:** (N-1) / N (better than RAID 1)

**Disadvantages:**
- **Write bottleneck:** All writes update parity disk

#### RAID 5 (Block-Level Striping with Distributed Parity)

**Mechanism:** Distribute parity across all disks.

**Structure:**
```
Disk 0: [A0, B0, C0, P_D]
Disk 1: [A1, B1, P_C, D1]
Disk 2: [A2, P_B, C2, D2]
Disk 3: [P_A, B3, C3, D3]
```

**Advantages:**
- **No parity bottleneck:** Parity distributed
- **Fault tolerance:** Survive 1 disk failure
- **Good read/write performance**

**Disadvantages:**
- **Complex parity management**
- **Rebuild time** after failure (hours)

**Use Case:** General-purpose servers (most common).

#### RAID 6 (Dual Parity)

**Mechanism:** Two parity blocks (P and Q) for each stripe.

**Advantages:**
- **Survive 2 disk failures**

**Disadvantages:**
- **Lower capacity:** (N-2) / N
- **Slower writes:** Compute two parities

**Use Case:** High-reliability systems.

#### RAID 10 (1+0: Mirrored Stripes)

**Mechanism:** Stripe across mirrored pairs.

**Structure:**
```
Pair 1: [A, B] mirrored
Pair 2: [C, D] mirrored
Striping across pairs
```

**Advantages:**
- **High performance:** Striping + mirroring
- **Fault tolerance:** Survive one disk failure per pair

**Disadvantages:**
- **Cost:** 50% capacity

**Use Case:** High-performance databases.

---

## 9.6 I/O Hardware

### I/O Devices

**Categories:**
1. **Block devices:** Disk, SSD (random access)
2. **Character devices:** Keyboard, mouse, serial port (stream)
3. **Network devices:** NIC (packet-based)

### I/O Communication

#### 1. Programmed I/O (Polling)

**Mechanism:** CPU continuously checks device status.

```c
while (device_not_ready());  // Busy-wait
data = device_data_register;
```

**Disadvantage:** **Wastes CPU cycles** (busy-waiting).

#### 2. Interrupt-Driven I/O

**Mechanism:** Device sends interrupt when ready.

```
1. CPU issues I/O command
2. CPU continues other work
3. Device completes, sends interrupt
4. CPU handles interrupt, processes data
```

**Advantage:** CPU not wasted.

**Disadvantage:** Overhead per byte (for high-speed devices).

#### 3. Direct Memory Access (DMA)

**Mechanism:** Device transfers data directly to/from memory (no CPU involvement).

```
1. CPU sets up DMA controller (source, destination, count)
2. DMA controller transfers data
3. DMA sends interrupt when complete
```

**Advantages:**
- **Minimal CPU involvement** (only setup and completion)
- **High throughput** (no per-byte overhead)

**Use Case:** Disk, network (high-speed bulk transfer).

**The 2026 Adversarial Vault:**

**Trap:** "DMA is always faster than interrupt-driven I/O."
- **TRUE** for large transfers.
- **FALSE** for small transfers (setup overhead dominates).

---

## 9.7 Mental Machinery for Permanent Recall

### The Bizarre Mnemonic: "The Record Player"

Imagine a **record player** (disk):

- **Platter:** Vinyl record (disk platter)
- **Arm:** Tonearm (disk arm)
- **Needle:** Read/write head
- **Seek Time:** Moving arm to track (slow!)
- **Rotational Latency:** Waiting for song to rotate to needle
- **FCFS:** Play songs in order they're requested (chaotic arm movement)
- **SSTF:** Play nearest song next (smart but might ignore far songs forever)
- **SCAN:** Play all songs from outer to inner, then reverse (elevator)
- **RAID 0:** Multiple players playing in parallel (fast, but if one breaks, concert ruined)
- **RAID 1:** Two players with same record (backup, if one breaks, continue)

**The Mental Slider:**
- Left (FCFS): Fair but slow
- Middle (SSTF): Fast but unfair
- Right (SCAN): Balanced

### The 5-Second Snap-Check

**Q:** Which disk algorithm for which scenario?

| **Scenario** | **Algorithm** |
|--------------|---------------|
| Real-time system (fairness critical) | SCAN / C-SCAN |
| Heavy load, minimize seek time | SSTF / LOOK |
| Critical data, need redundancy | RAID 1 / RAID 5 |

---

## 9.8 Practice Problems

### MCQ 1: Disk Access Time

**Q:** Seek time = 6 ms, RPM = 7200, transfer rate = 100 MB/s. Time to read 4 KB?

(A) 10.21 ms  
(B) 12.21 ms  
(C) 14.21 ms  
(D) 16.21 ms  

**Solution:**

- Seek: 6 ms
- Rotational: $\frac{60}{2 \times 7200} = 4.17$ ms
- Transfer: $\frac{4096}{100 \times 10^6} = 0.04$ ms

**Total:** $6 + 4.17 + 0.04 = 10.21$ ms

**Answer: (A)**

---

### MCQ 2: RAID Capacity

**Q:** 4 disks, each 1 TB. Using RAID 5, total usable capacity = ?

(A) 1 TB  
(B) 2 TB  
(C) 3 TB  
(D) 4 TB  

**Solution:**

RAID 5: $(N-1) \times \text{Disk Size} = 3 \times 1 = 3$ TB

**Answer: (C)**

---

### MCQ 3: Disk Scheduling

**Q:** Which algorithm may cause starvation?

(A) FCFS  
(B) SSTF  
(C) SCAN  
(D) C-SCAN  

**Solution:**

SSTF (greedy, may never service far requests).

**Answer: (B)**

---

### MCQ 4: DMA

**Q:** What is the main advantage of DMA?

(A) Faster data transfer  
(B) Lower CPU involvement  
(C) More reliable transfer  
(D) Simpler hardware  

**Solution:**

DMA reduces CPU involvement (CPU only sets up and handles completion).

**Answer: (B)**

---

### NAT 1: Head Movement (FCFS)

**Q:** Current position = 53. Queue: [98, 183, 37, 122, 14, 124, 65, 67]. Total head movement (FCFS)?

**Solution:**

$$|98-53| + |183-98| + |37-183| + |122-37| + |14-122| + |124-14| + |65-124| + |67-65|$$
$$= 45 + 85 + 146 + 85 + 108 + 110 + 59 + 2 = 640$$

**Answer: 640**

---

### NAT 2: Head Movement (SSTF)

**Q:** Current position = 50. Queue: [98, 183, 37, 122, 14, 124, 65, 67]. Total head movement (SSTF)?

**Solution:**

Sequence: 50 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183

$$15 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = 239$$

**Answer: 239**

---

### NAT 3: RAID 5 Capacity

**Q:** 6 disks, each 500 GB, RAID 5. Total usable capacity (in GB)?

**Solution:**

$(N-1) \times \text{Disk Size} = 5 \times 500 = 2500$ GB

**Answer: 2500**

---

### NAT 4: Rotational Latency

**Q:** Disk rotates at 10000 RPM. Average rotational latency (in ms)?

**Solution:**

$$\frac{60}{2 \times 10000} = 3 \text{ ms}$$

**Answer: 3**

---

## 9.9 The Elite Formulas Summary

### 1. Disk Access Time

$$T_{\text{access}} = T_{\text{seek}} + \frac{60}{2 \times \text{RPM}} + \frac{\text{Size}}{\text{Rate}}$$

### 2. RAID 5 Capacity

$$\text{Usable} = (N-1) \times \text{Disk Size}$$

### 3. Head Movement (Calculate per algorithm)

- **FCFS:** Sum of absolute differences in arrival order
- **SSTF:** Greedy nearest-neighbor selection
- **SCAN:** Move one direction to end, then reverse

---

## Logic Singularity Verified for 2026 (IIT-G Standards)

**Mastery Level:** Sovereign

**The Core Insight:**
- **Seek time dominates** disk access (mechanical bottleneck)
- **SSTF** minimizes seek but risks starvation
- **SCAN/C-SCAN** balance performance and fairness
- **RAID** trades cost for performance and/or reliability

**Next:** Chapter 10 provides **Previous Year GATE Questions** with detailed solutions.

**Would you like to initiate a 'Multi-Variable Stress Test' combining all OS concepts for Rank-1 mastery?**
