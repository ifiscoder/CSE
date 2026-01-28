# Instruction Pipelining | The Parallelism Singularity

> **The Atomic Truth:** *Overlap instructions, multiply throughput.*

[Image of assembly line with 5 stages processing different instructions simultaneously - the fundamental pipeline concept]

---

## I. THE PATH OF ELEGANCE

### 1.1 Pipelining Concept

**The Car Wash Analogy:**
- Non-pipelined: Wash→Dry→Wax one car completely, then next car
- Pipelined: Car 1 in wash, Car 2 in dry, Car 3 in wax (all simultaneous)

**Throughput:** $3\times$ faster (with 3 stages)

---

### 1.2 5-Stage RISC Pipeline

**Stages:**
1. **IF:** Instruction Fetch
2. **ID:** Instruction Decode / Register Read
3. **EX:** Execute / ALU operation
4. **MEM:** Memory Access (Load/Store)
5. **WB:** Write Back to register

**Ideal:** 1 instruction completes per cycle (CPI = 1).

---

### 1.3 Pipeline Hazards (The Bottlenecks)

#### A. Data Hazards (RAW, WAR, WAW)

**1. RAW (Read After Write)** - **True Dependency** ⭐
```
ADD R1, R2, R3  # R1 written in WB stage (cycle 5)
SUB R4, R1, R5  # R1 needed in EX stage (cycle 4 of SUB)
```

**Problem:** SUB needs R1 before ADD writes it.

**Solution:** **Forwarding (Bypassing)** - Send data from EX/MEM to EX of next instruction.

---

**2. WAR (Write After Read)** - **Anti-Dependency**
Not a problem in 5-stage pipeline (writes happen in order).

---

**3. WAW (Write After Write)** - **Output Dependency**
Not a problem in 5-stage pipeline (writes in WB stage are in order).

---

#### B. Control Hazards (Branch Hazards)

**Problem:** Branch target not known until EX stage (cycle 3).

**Branch taken?** Fetched instructions may be wrong → pipeline flush.

**Solutions:**
1. **Stall:** Wait for branch resolution (3 cycle penalty)
2. **Predict:** Guess branch direction (static/dynamic prediction)
3. **Delayed Branch:** Execute instruction after branch (branch delay slot)

---

#### C. Structural Hazards

**Problem:** Two instructions need same hardware resource simultaneously.

**Example:** Unified cache - IF of Inst 4 and MEM of Inst 1 conflict.

**Solution:** Separate I-cache and D-cache, or stall.

---

### 1.4 Pipeline Performance

**Ideal CPI:** 1.0 (one instruction per cycle)

**Actual CPI:** $1 + \text{Stall cycles per instruction}$

**Example:** 20% branches, 30% branch penalty = 3 cycles
$$\text{CPI} = 1 + (0.20 \times 0.30 \times 3) = 1 + 0.18 = 1.18$$

**Speedup:**
$$\text{Speedup} = \frac{\text{Time}_{\text{non-pipelined}}}{\text{Time}_{\text{pipelined}}} = \frac{n \times k}{k + (n-1)} \approx \frac{nk}{n} = k$$

For large $n$, speedup → $k$ (# stages).

---

## II. THE 2026 ADVERSARIAL VAULT

### Trap #1: Forwarding Cannot Solve Load-Use Hazard
**Setup:**
```
LW R1, 0(R2)    # R1 available after MEM (cycle 4)
ADD R3, R1, R4  # R1 needed in EX (cycle 3)
```

**Truth:** 1 cycle stall required (data not ready even with forwarding).

---

### Trap #2: Branch Penalty Depends on Detection Stage
- If branch resolved in **ID:** 1 cycle penalty
- If branch resolved in **EX:** 2 cycle penalty
- If branch resolved in **MEM:** 3 cycle penalty

**Mental Checkpoint:** Check when branch is detected in the given pipeline.

---

### Trap #3: Pipeline Depth Trade-off
**More stages:**
- ✓ Higher frequency (shorter stage time)
- ✗ More hazard penalties
- ✗ Deeper pipeline flush on misprediction

**Not always faster!**

---

## III. PERMANENT RECALL

### Mnemonic: "IF ID EX MEM WB" = "I Identify Excellent Memory Work"

### Mnemonic: "RAW is Real, WAR/WAW Won't"
- **RAW:** Real hazard in 5-stage (needs forwarding)
- **WAR/WAW:** Not hazards in simple 5-stage pipeline

### Mental Slider: Turn "forwarding dial" - watch data jump from later stage to earlier stage.

---

## IV. THE SOVEREIGNTY DRILLS

### Problem 1 (GATE 2018): CPI with Hazards
**20% loads, load-use hazard = 1 stall. 30% branches, 50% taken, penalty = 2. Find CPI.**

**Solution:**
$$\text{CPI} = 1 + (0.20 \times 1) + (0.30 \times 0.50 \times 2)$$
$$= 1 + 0.20 + 0.30 = 1.50$$

---

### Problem 2: Speedup Calculation
**5-stage pipeline, 100 instructions. Non-pipelined = 500 cycles. Find pipeline cycles.**

**Solution:**
- First instruction: 5 cycles (fill pipeline)
- Remaining 99: 1 cycle each
- Total = $5 + 99 = 104$ cycles

**Speedup:** $500 / 104 = 4.81\times$

---

**Logic Singularity verified for 2026 (IIT-G Standards).**

*"Pipeline: Parallelism's first victory over latency."*
