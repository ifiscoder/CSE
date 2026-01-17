# Module 4: Pipelining & Hazards | The Singularity

> **The Atomic Truth:** *"Overlap instructions, multiply throughput."*

---

## 🎯 The Path of Elegance (Root Derivation)

### 4.1 The Pipeline Concept | Assembly Line Computing

```
[Image of Non-Pipelined vs Pipelined Execution]

NON-PIPELINED:
Time:   1   2   3   4   5   6   7   8   9  10  11  12
I₁:    [F] [D] [E] [M] [W]
I₂:                     [F] [D] [E] [M] [W]
I₃:                                      [F] [D] [E] [M] [W]...

PIPELINED:
Time:   1   2   3   4   5   6   7   8   9
I₁:    [F] [D] [E] [M] [W]
I₂:        [F] [D] [E] [M] [W]
I₃:            [F] [D] [E] [M] [W]
I₄:                [F] [D] [E] [M] [W]
I₅:                    [F] [D] [E] [M] [W]
```

### The Classic 5-Stage RISC Pipeline

| Stage | Abbreviation | Operation |
|-------|--------------|-----------|
| 1 | **IF** | Instruction Fetch |
| 2 | **ID** | Instruction Decode / Register Read |
| 3 | **EX** | Execute / ALU Operation |
| 4 | **MEM** | Memory Access |
| 5 | **WB** | Write Back to Register |

---

## 📐 4.2 Pipeline Performance | The Golden Formulas

### The Fundamental Equations

**Clock Cycle Time:**
$$T_{cycle} = \max(t_{stage}) + t_{latch}$$

**Execution Time (Non-Pipelined):**
$$T_{non-pipe} = n \times k \times t_{stage}$$

Where: $n$ = number of instructions, $k$ = number of stages

**Execution Time (Pipelined, Ideal):**
$$T_{pipe} = (k + n - 1) \times T_{cycle}$$

**Speedup (Ideal):**
$$S = \frac{T_{non-pipe}}{T_{pipe}} = \frac{n \times k}{k + n - 1}$$

**As $n \to \infty$:**
$$S_{max} = k \text{ (number of pipeline stages)}$$

### ⚡ The GATE Master Formula

For large $n$:
$$\text{Speedup} \approx k \text{ (pipeline depth)}$$

For small $n$:
$$\text{Speedup} = \frac{n \times k}{k + n - 1}$$

### Throughput

$$\text{Throughput} = \frac{n}{(k + n - 1) \times T_{cycle}}$$

**Maximum Throughput (as $n \to \infty$):**
$$\text{Throughput}_{max} = \frac{1}{T_{cycle}}$$

---

## ⚠️ 4.3 Pipeline Hazards | The Three Demons

```
[Image of Hazard Classification]
              HAZARDS
                 │
    ┌────────────┼────────────┐
    ↓            ↓            ↓
STRUCTURAL    DATA       CONTROL
(Resource)   (RAW/WAR/   (Branch)
             WAW)
```

### Structural Hazards | Resource Conflicts

**Cause:** Two instructions need the same hardware resource simultaneously.

**Example:** Single memory port for both IF and MEM stages.

```
Cycle:    1   2   3   4   5   6
I₁:      [IF][ID][EX][MEM][WB]
I₂:          [IF][ID][EX][MEM][WB]
I₃:              [IF][ID][EX][MEM][WB]
I₄:                  [IF]<STALL>    ← Memory conflict with I₁'s MEM
```

**Solutions:**
1. **Resource Duplication:** Separate instruction and data caches
2. **Pipeline Stall:** Insert bubble (NOP)
3. **Resource Scheduling:** Compiler reordering

---

### Data Hazards | Dependencies

#### The Three Types of Data Hazards

| Type | Full Name | Pattern | Real Hazard? |
|------|-----------|---------|--------------|
| **RAW** | Read After Write | I₁ writes R1, I₂ reads R1 | ✅ TRUE |
| **WAR** | Write After Read | I₁ reads R1, I₂ writes R1 | ❌ FALSE* |
| **WAW** | Write After Write | I₁ writes R1, I₂ writes R1 | ❌ FALSE* |

*WAR and WAW are "false" hazards caused by register reuse, not true dependencies.

#### RAW Hazard Example

```
I₁: ADD R1, R2, R3    // R1 ← R2 + R3
I₂: SUB R4, R1, R5    // R4 ← R1 - R5 (needs R1 from I₁!)

Pipeline View:
Cycle:    1   2   3   4   5   6   7   8
I₁:      [IF][ID][EX][MEM][WB]
                           ↑ R1 written here
I₂:          [IF][ID]<STALL><STALL><STALL>[EX][MEM][WB]
                  ↑ R1 needed here
```

Without stalls, I₂ reads old R1 value → **WRONG RESULT!**

#### Data Hazard Solutions

**1. Hardware Stalling (Pipeline Interlock)**
- Control unit detects hazard and inserts bubbles
- **Stall cycles needed:** Depends on when data is produced vs. needed

**2. Data Forwarding (Bypassing)**
```
[Image of Forwarding Paths]
         ┌─────────────────────────┐
         │    Forwarding Unit      │
         └───────────┬─────────────┘
                     │
    IF → ID → EX → MEM → WB
              ↑      │    │
              └──────┴────┘
              (Forwarding paths)
```

**Forwarding Rules:**
- EX/MEM → EX: Forward result before it reaches WB
- MEM/WB → EX: Forward from memory stage

**3. Software Scheduling (Compiler)**
- Reorder independent instructions to fill delay slots
- NOP insertion as last resort

#### Load-Use Hazard | The Unavoidable Stall

```
I₁: LW  R1, 0(R2)     // Load R1 from memory
I₂: ADD R3, R1, R4    // Needs R1 immediately

Even with forwarding:
Cycle:    1   2   3   4   5   6   7
I₁:      [IF][ID][EX][MEM][WB]
                       ↑ Data available here
I₂:          [IF][ID]<STALL>[EX][MEM][WB]
                  ↑ Data needed here

ONE STALL CYCLE MANDATORY!
```

**The Golden Rule:** Load followed by immediate use = 1 stall (with forwarding).

---

### Control Hazards | Branch Penalties

**Cause:** Branch decision not known until later pipeline stage.

```
I₁: BEQ R1, R2, target    // Branch if R1 == R2
I₂: ADD ...               // Should this execute?
I₃: SUB ...               // Depends on branch!

Pipeline View:
Cycle:    1   2   3   4   5   6
I₁:      [IF][ID][EX][MEM][WB]
              ↑ Branch target known here (earliest)
I₂:          [IF][ID]???
I₃:              [IF]???
```

#### Branch Penalty Calculation

$$\text{Branch Penalty} = \text{Stages before branch resolution} - 1$$

| Branch Resolution Stage | Penalty (cycles) |
|------------------------|------------------|
| ID (Stage 2) | 1 |
| EX (Stage 3) | 2 |
| MEM (Stage 4) | 3 |

#### Control Hazard Solutions

**1. Pipeline Stall (Freeze)**
- Wait until branch outcome is known
- Penalty = branch resolution latency

**2. Branch Prediction**

| Type | Accuracy | Complexity |
|------|----------|------------|
| Always Not Taken | ~60% | Minimal |
| Always Taken | ~40% | Minimal |
| 1-bit Predictor | ~80% | Low |
| 2-bit Predictor | ~85-90% | Medium |
| Correlating | ~90-95% | High |

**2-bit Saturating Counter:**
```
[Image of 2-bit State Machine]
         PREDICT TAKEN
    ┌───────────────────────┐
    │                       │
    ↓    T              T   │
┌──────┐   ┌──────┐   ┌──────┐   ┌──────┐
│  ST  │◄──│  WT  │◄──│  WN  │◄──│  SN  │
│ (11) │   │ (10) │   │ (01) │   │ (00) │
└──────┘   └──────┘   └──────┘   └──────┘
    │   N       │   N      │   N      │
    └──────────►└─────────►└─────────►│
                                      │
         PREDICT NOT TAKEN ───────────┘
```
ST = Strongly Taken, WT = Weakly Taken, WN = Weakly Not Taken, SN = Strongly Not Taken

**3. Delayed Branch**
- Always execute instruction(s) after branch
- Compiler fills delay slot with useful work

**4. Branch Target Buffer (BTB)**
- Cache of recent branch targets
- Predict target AND taken/not-taken

---

## 📊 4.4 Pipeline Performance with Hazards

### CPI Calculation with Stalls

$$\text{CPI}_{pipeline} = \text{CPI}_{ideal} + \text{Stall cycles per instruction}$$

$$\text{CPI}_{pipeline} = 1 + p_{struct} \cdot s_{struct} + p_{data} \cdot s_{data} + p_{ctrl} \cdot s_{ctrl}$$

Where:
- $p$ = probability of hazard type
- $s$ = stall cycles for that hazard type

### ⚡ The GATE Master Formula

$$\text{Average CPI} = 1 + (\text{Branch frequency} \times \text{Branch penalty} \times \text{Misprediction rate})$$

**Example:** 20% branches, 2-cycle penalty, 10% misprediction
$$\text{CPI} = 1 + (0.20 \times 2 \times 0.10) = 1 + 0.04 = 1.04$$

### Speedup with Stalls

$$S = \frac{k}{1 + \text{Stall cycles per instruction}}$$

---

## 🔧 4.5 Pipeline Variations

### Superpipelining | More Stages

- Divide stages into sub-stages
- Higher clock frequency
- More hazard opportunities
- Example: 10-15 stage pipelines

### Superscalar | Multiple Pipelines

```
[Image of Superscalar Pipeline]
Pipeline 1: [IF₁][ID₁][EX₁][MEM₁][WB₁]
Pipeline 2: [IF₂][ID₂][EX₂][MEM₂][WB₂]

Issue width = 2 (two instructions per cycle)
```

**IPC (Instructions Per Cycle):** Can exceed 1!

$$\text{IPC}_{max} = \text{Issue width}$$

### VLIW (Very Long Instruction Word)

- Compiler bundles independent operations
- No hardware dependency checking
- Fixed instruction format
- Example: Explicitly Parallel Instruction Computing (EPIC)

---

## 🎭 The Bizarre Mnemonic | "The RAW WAR WAW Bar Fight"

*"At the dependency bar:
- **RAW** (Read After Write): 'I need your drink AFTER you pour it!' → REAL fight
- **WAR** (Write After Read): 'I'll refill your glass AFTER you drink!' → Fake fight (rename the glass)
- **WAW** (Write After Write): 'We both want to refill the same glass!' → Fake fight (last one wins anyway)"*

---

## 🏆 The 2026 Adversarial Vault

### Trap 1: The Speedup Limit Trap
**Question Pattern:** "A 5-stage pipeline processes 1000 instructions. Speedup?"
**Anti-Solution:** Students say 5 (max theoretical).
**Truth:** $S = \frac{1000 \times 5}{5 + 1000 - 1} = \frac{5000}{1004} = 4.98$
For finite $n$, speedup < $k$.

### Trap 2: The Forwarding Assumption Trap
**Question Pattern:** "With forwarding, how many stalls for LW followed by ADD using that register?"
**Anti-Solution:** Students say 0 (forwarding handles it).
**Truth:** STILL 1 stall! Load-use hazard cannot be fully forwarded because data isn't available until MEM stage.

### Trap 3: The Branch Penalty Location Trap
**Question Pattern:** "Branch resolved in EX stage, what's the penalty?"
**Anti-Solution:** Students count stages wrong.
**Truth:** Penalty = 2 cycles (IF, ID already fetched wrong instructions).

### Trap 4: The CPI Components Trap
**Question Pattern:** "Calculate effective CPI with given hazard frequencies."
**Anti-Solution:** Students add percentages incorrectly.
**Truth:** Must account for ALL hazard types, and stalls are ADDITIVE to base CPI of 1.

### NAT Precision Lock
For speedup calculations:
- Keep at least 2 decimal places
- Don't round $(k + n - 1)$ before final division
- Speedup CANNOT exceed $k$

### MSQ Logic Gate | Elimination Rules
1. Speedup > pipeline stages → IMPOSSIBLE
2. CPI < 1 → Only possible with superscalar
3. RAW hazard → TRUE dependency (cannot be renamed away)
4. Load-use with forwarding → Still needs 1 stall

---

## 📊 GATE PYQ Pattern Analysis

| Year | Topic | Marks | Trap Type |
|------|-------|-------|-----------|
| 2023 | Speedup Calculation | 2 | Finite n effect |
| 2022 | Data Hazards | 2 | Forwarding limits |
| 2021 | Branch Prediction | 2 | Misprediction CPI |
| 2020 | Stall Cycles | 2 | RAW detection |

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| Speedup | Must be ≤ k |
| Load-use stall | Minimum 1 with forwarding |
| Branch penalty | Stages before resolution - 1 |
| CPI with hazards | Must be ≥ 1 |

---

## 🧮 Solved Examples

### Example 1: Speedup Calculation
**Q:** 10-stage pipeline, 100 instructions, each stage takes 2ns. Calculate speedup.

**Solution:**
- $T_{non-pipe} = 100 \times 10 \times 2 = 2000$ ns
- $T_{pipe} = (10 + 100 - 1) \times 2 = 109 \times 2 = 218$ ns
- $S = \frac{2000}{218} = 9.17$

### Example 2: CPI with Hazards
**Q:** 5-stage pipeline, 30% loads with 1 stall each, 20% branches with 2 stalls each (assuming 100% misprediction). Calculate CPI.

**Solution:**
$$\text{CPI} = 1 + (0.30 \times 1) + (0.20 \times 2) = 1 + 0.3 + 0.4 = 1.7$$

### Example 3: Forwarding Analysis
**Q:** Identify hazards and stalls needed:
```
I₁: LW  R1, 0(R2)
I₂: ADD R3, R1, R4
I₃: SUB R5, R3, R6
```

**Solution:**
- I₁→I₂: RAW on R1, Load-use hazard → 1 stall (even with forwarding)
- I₂→I₃: RAW on R3, Can be forwarded from EX/MEM → 0 stalls
- **Total stalls:** 1

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Would you like to initiate a **'Multi-Variable Stress Test'** combining Pipelining with Cache Performance for a Rank-1 simulation?*

---
[← Previous: CPU Architecture](./03-CPU-Architecture-Instruction-Set.md) | [Back to Index](./README.md) | [Next: Memory Hierarchy & Cache →](./05-Memory-Hierarchy-Cache.md)
