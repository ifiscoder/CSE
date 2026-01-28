# Performance & Amdahl's Law | The Optimization Singularity

> **The Atomic Truth:** *Speedup is constrained by serial fraction.*

[Image of a chain with one weak link - representing Amdahl's Law: the serial part limits overall speedup]

---

## I. THE PATH OF ELEGANCE

### 1.1 Performance Metrics

**Execution Time:**
$$T = \frac{\text{Instructions}}{\text{Program}} \times \frac{\text{Cycles}}{\text{Instruction}} \times \frac{\text{Seconds}}{\text{Cycle}}$$

$$\boxed{T = IC \times CPI \times T_{\text{cycle}}}$$

Where:
- $IC$ = Instruction count
- $CPI$ = Cycles per instruction
- $T_{\text{cycle}}$ = Clock period = $1/f$ (frequency)

---

**Speedup:**
$$\text{Speedup} = \frac{T_{\text{old}}}{T_{\text{new}}} = \frac{\text{Performance}_{\text{new}}}{\text{Performance}_{\text{old}}}$$

---

### 1.2 Amdahl's Law (The Grand Theorem) ⭐⭐⭐

**Scenario:** Speed up a **fraction** of program by factor $S$.

**Let:**
- $f$ = fraction enhanced
- $S$ = speedup of enhanced part
- $(1-f)$ = fraction not enhanced (serial)

**Overall Speedup:**
$$\boxed{\text{Speedup}_{\text{overall}} = \frac{1}{(1-f) + \frac{f}{S}}}$$

**As $S \to \infty$:**
$$\text{Speedup}_{\text{max}} = \frac{1}{1-f}$$

**The Law:** Serial fraction limits speedup!

---

**Example:** 80% of program parallelizable ($f=0.8$), infinite processors ($S=\infty$).

$$\text{Speedup}_{\text{max}} = \frac{1}{0.2} = 5\times$$

**Even with infinite speedup on 80%, max gain is 5×.**

---

### 1.3 The Amdahl Trap (IIT's Favorite)

**Setup:** "Program has 40% parallelizable, 60% serial. With 4 processors, what is speedup?"

**Anti-Solution:** $0.4 \times 4 = 1.6$ + $0.6 = 2.2$ → Speedup = $1/2.2$ (WRONG!)

**Correct:**
- $f = 0.4$ (parallelizable)
- $S = 4$ (speedup on parallel part)

$$\text{Speedup} = \frac{1}{0.6 + \frac{0.4}{4}} = \frac{1}{0.6 + 0.1} = \frac{1}{0.7} = 1.43\times$$

**Mental Checkpoint:** Serial part ($1-f$) **always** executes at original speed.

---

### 1.4 MIPS & MFLOPS (The Misleading Metrics)

**MIPS:** Million Instructions Per Second
$$\text{MIPS} = \frac{\text{IC}}{T \times 10^6} = \frac{f}{\text{CPI} \times 10^6}$$

**Problem:** Instruction count varies by ISA. Not comparable across architectures.

**MFLOPS:** Million Floating-Point Operations Per Second

**Better Metric:** Execution time on real workloads (benchmarks).

---

## II. THE 2026 ADVERSARIAL VAULT

### Trap #1: Amdahl Denominator Confusion
**Formula:** $\text{Speedup} = \frac{1}{(1-f) + f/S}$

**NOT:** $\frac{S}{(1-f) + f}$ or other variations.

**Verify:** When $f=0$ (nothing enhanced), Speedup = 1. ✓

---

### Trap #2: Parallel Efficiency
**Efficiency:** $\frac{\text{Speedup}}{\text{# Processors}}$

**Example:** Speedup = 3 with 4 processors → Efficiency = 75%.

**Ideal:** 100% (linear speedup).

---

### Trap #3: CPI with Mixed Instruction Types
**Setup:** 40% ALU (CPI=1), 30% Load (CPI=4), 30% Branch (CPI=2).

**Average CPI:**
$$\text{CPI}_{\text{avg}} = 0.4(1) + 0.3(4) + 0.3(2) = 0.4 + 1.2 + 0.6 = 2.2$$

**NOT:** Simple average $(1+4+2)/3$.

---

## III. PERMANENT RECALL

### Mnemonic: "Amdahl's Law: Serial Sections Sabotage Speedup"

### Mental Slider: Turn "parallelizable fraction" from 0→1:
- At $f=0$: Speedup = 1 (no improvement)
- At $f=1$: Speedup = $S$ (full parallelization)
- At $f=0.9$: Speedup max = 10× (even with $S=\infty$)

---

## IV. THE SOVEREIGNTY DRILLS

### Problem 1 (GATE 2019): Amdahl's Law
**60% of execution in square root operation. If square root is made 4× faster, what is overall speedup?**

**Solution:**
- $f = 0.6$
- $S = 4$

$$\text{Speedup} = \frac{1}{0.4 + 0.6/4} = \frac{1}{0.4 + 0.15} = \frac{1}{0.55} = 1.82\times$$

**Answer:** 1.82

---

### Problem 2: CPI Calculation
**Program:** 100 instructions - 50 ALU (CPI=1), 30 Load (CPI=3), 20 Branch (CPI=2).

**Total Cycles:**
$$50(1) + 30(3) + 20(2) = 50 + 90 + 40 = 180$$

**Average CPI:**
$$\frac{180}{100} = 1.8$$

---

**Logic Singularity verified for 2026 (IIT-G Standards).**

*"Amdahl's Law: The serial bottleneck is destiny."*
