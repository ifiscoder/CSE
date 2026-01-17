# Module 8: Parallel Processing & Multiprocessors | The Singularity

> **The Atomic Truth:** *"Divide work, multiply throughput."*

---

## 🎯 The Path of Elegance (Root Derivation)

### 8.1 Flynn's Taxonomy | The Classification

```
[Image of Flynn's Taxonomy]
                     Data Streams
                   Single    Multiple
              ┌──────────┬──────────┐
    Single    │   SISD   │   SIMD   │
 Instruction  │ (Serial) │ (Vector) │
   Streams    ├──────────┼──────────┤
    Multiple  │   MISD   │   MIMD   │
              │ (Rare)   │(Parallel)│
              └──────────┴──────────┘
```

| Type | Description | Examples |
|------|-------------|----------|
| **SISD** | Single instruction, single data | Classic CPU |
| **SIMD** | Single instruction, multiple data | GPU, SSE/AVX |
| **MISD** | Multiple instruction, single data | Fault tolerance |
| **MIMD** | Multiple instruction, multiple data | Multiprocessors |

---

## 📐 8.2 Amdahl's Law | The Parallel Limit

### The Fundamental Equation

$$\text{Speedup} = \frac{1}{(1-P) + \frac{P}{N}}$$

Where:
- $P$ = Fraction of program that can be parallelized
- $N$ = Number of processors

### The Maximum Speedup Limit

As $N \to \infty$:
$$S_{max} = \frac{1}{1-P}$$

**Example:** If 90% parallelizable ($P = 0.9$):
$$S_{max} = \frac{1}{1-0.9} = \frac{1}{0.1} = 10$$

**No matter how many processors, speedup capped at 10x!**

### Amdahl's Law Visualization

```
[Image of Amdahl's Law]
    Speedup
       ↑
   20 ─┤                         ●───── P = 0.95
       │                    ●────
   15 ─┤              ●─────
       │         ●────
   10 ─┤    ●────────────────●───────── P = 0.90
       │ ●──
    5 ─┤────●────●────●────●───────── P = 0.75
       │
    0 ─┼────┬────┬────┬────┬────► Processors
       0    5   10   15   20
```

---

## ⚡ 8.3 Gustafson's Law | The Scaled Perspective

### The Alternative Equation

$$\text{Speedup} = N + (1-N) \times S$$

Or equivalently:
$$\text{Speedup} = N - (N-1) \times S$$

Where:
- $N$ = Number of processors
- $S$ = Serial fraction of PARALLEL program

**Key Insight:** As problem size grows, parallel fraction often grows too!

### Amdahl vs Gustafson

| Aspect | Amdahl | Gustafson |
|--------|--------|-----------|
| Problem size | Fixed | Scaled |
| Serial part | Fixed | Fixed |
| Parallel part | Fixed | Grows with N |
| Pessimistic/Optimistic | Pessimistic | Optimistic |

---

## 🔗 8.4 Multiprocessor Architectures

### UMA (Uniform Memory Access)

```
[Image of UMA/SMP]
    ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
    │CPU 0│ │CPU 1│ │CPU 2│ │CPU 3│
    └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘
       │       │       │       │
    ┌──┴───────┴───────┴───────┴──┐
    │      Shared Bus/Crossbar    │
    └──────────────┬──────────────┘
                   │
            ┌──────┴──────┐
            │   Shared    │
            │   Memory    │
            └─────────────┘

All CPUs: Same access time to memory
```

**Characteristics:**
- Symmetric Multiprocessor (SMP)
- Equal memory access latency
- Bus becomes bottleneck
- Limited scalability (8-16 cores typically)

### NUMA (Non-Uniform Memory Access)

```
[Image of NUMA]
    Node 0                      Node 1
┌─────────────────┐        ┌─────────────────┐
│ ┌───┐   ┌───┐   │        │ ┌───┐   ┌───┐   │
│ │CPU│   │CPU│   │        │ │CPU│   │CPU│   │
│ └─┬─┘   └─┬─┘   │        │ └─┬─┘   └─┬─┘   │
│   └───┬───┘     │        │   └───┬───┘     │
│   ┌───┴───┐     │◄──────►│   ┌───┴───┐     │
│   │ Local │     │ Inter- │   │ Local │     │
│   │Memory │     │ connect│   │Memory │     │
│   └───────┘     │        │   └───────┘     │
└─────────────────┘        └─────────────────┘

Local access: Fast
Remote access: Slow (2-10x)
```

**Characteristics:**
- Better scalability (100s of cores)
- Programming complexity (data placement matters)
- Cache coherence challenges

---

## 🔄 8.5 Cache Coherence Protocols

### The Coherence Problem

```
[Image of Coherence Problem]
     CPU 0                CPU 1
   Cache: X=5           Cache: X=5
       │                    │
       └────────┬───────────┘
                │
            Memory
             X=5

CPU 0 writes X=10:
   Cache 0: X=10
   Cache 1: X=5  ← STALE!
   Memory:  X=? (depends on write policy)
```

### Snooping Protocols

**Write-Invalidate:**
- On write, invalidate all other copies
- Most common approach
- MESI protocol

**Write-Update:**
- On write, update all other copies
- More bus traffic
- Less common

### MESI Protocol | The Standard

| State | Meaning | Exclusive | Modified | Valid |
|-------|---------|-----------|----------|-------|
| **M** | Modified | Yes | Yes | Yes |
| **E** | Exclusive | Yes | No | Yes |
| **S** | Shared | No | No | Yes |
| **I** | Invalid | — | — | No |

```
[MESI State Diagram]
                Read miss
        ┌─────────────────────┐
        ↓                     │
    ┌───────┐   Write     ┌───────┐
    │   E   │────────────►│   M   │
    │Exclus.│             │ Modif │
    └───┬───┘             └───┬───┘
        │ Snoop read          │ Snoop write
        ↓                     │ (invalidate)
    ┌───────┐                 ↓
    │   S   │◄────────────┌───────┐
    │Shared │             │   I   │
    └───┬───┘             │Invalid│
        │ Snoop write     └───────┘
        └──────────────────►  ↑
                              │
                         Write miss
```

### Directory-Based Coherence

For large-scale systems (NUMA):
- Central directory tracks which caches have copies
- Point-to-point messages instead of broadcast
- More scalable than snooping

---

## 🧮 8.6 Synchronization Primitives

### Atomic Operations

| Operation | Description |
|-----------|-------------|
| **Test-and-Set** | Read, set to 1, return old value |
| **Compare-and-Swap** | If (loc == expected) then loc = new |
| **Fetch-and-Add** | Return old value, add to location |
| **Load-Linked/Store-Conditional** | Detect intervening writes |

### Lock Implementation

```
// Test-and-Set Lock
lock:
    while (test_and_set(&lock_var) == 1)
        ; // spin
    // critical section
unlock:
    lock_var = 0;
```

**Problem:** High bus traffic (every spin = bus transaction)

**Solution:** Test-and-Test-and-Set
```
lock:
    while (true) {
        while (lock_var == 1)
            ; // spin locally (cached)
        if (test_and_set(&lock_var) == 0)
            break; // got the lock
    }
```

---

## 📊 8.7 Interconnection Networks

### Topology Comparison

| Topology | Diameter | Bisection BW | Cost |
|----------|----------|--------------|------|
| Bus | 1 | 1 | O(1) |
| Ring | N/2 | 2 | O(N) |
| Mesh (√N × √N) | 2(√N-1) | √N | O(N) |
| Torus | √N | 2√N | O(N) |
| Hypercube | log N | N/2 | O(N log N) |
| Crossbar | 1 | N | O(N²) |

### Key Metrics

- **Diameter:** Maximum hops between any two nodes
- **Bisection Bandwidth:** Bandwidth across minimum cut
- **Scalability:** How cost grows with N

---

## 🎭 The Bizarre Mnemonic | "The Kitchen Parallel Processing"

*"A kitchen is a parallel processor:
- **SISD:** One chef, one dish (sequential)
- **SIMD:** One chef commands, all stations do same step (GPU)
- **MIMD:** Many chefs, different dishes (multiprocessor)
- **Amdahl's Law:** The 'plating' step can't be parallelized—no matter how many sous chefs, the head chef still finishes each dish alone
- **Cache Coherence:** If two chefs have copies of the recipe and one changes it, the other's is stale!"*

---

## 🏆 The 2026 Adversarial Vault

### Trap 1: The Amdahl Numerator/Denominator
**Question Pattern:** "90% parallelizable with 10 processors, speedup?"
**Anti-Solution:** Students invert the formula.
**Truth:** $S = \frac{1}{0.1 + 0.9/10} = \frac{1}{0.1 + 0.09} = \frac{1}{0.19} = 5.26$

### Trap 2: The Maximum Speedup
**Question Pattern:** "With infinite processors, speedup for 95% parallel?"
**Anti-Solution:** Students say infinity.
**Truth:** $S_{max} = \frac{1}{1-0.95} = 20$, NOT infinity!

### Trap 3: The UMA vs NUMA Identification
**Question Pattern:** "Which architecture if access time varies by location?"
**Anti-Solution:** Students confuse definitions.
**Truth:** Variable access time = NUMA, Uniform = UMA.

### Trap 4: The MESI State Transitions
**Question Pattern:** "After CPU 0 writes to shared line, CPU 1's state?"
**Anti-Solution:** Students forget invalidation.
**Truth:** CPU 1 → Invalid (I) state! Write-invalidate protocol.

### NAT Precision Lock
- Amdahl speedup: 2-3 decimal places
- Don't round intermediate fractions
- $P + (1-P) = 1$ always (sanity check)

### MSQ Logic Gate | Elimination Rules
1. Speedup > N processors → Impossible (unless superlinear)
2. SIMD → Same instruction on all data
3. UMA → Equal memory access time
4. MESI: Write to shared → Others invalidated

---

## 📊 GATE PYQ Pattern Analysis

| Year | Topic | Marks | Trap Type |
|------|-------|-------|-----------|
| 2023 | Amdahl's Law | 2 | Speedup calculation |
| 2022 | Cache Coherence | 2 | MESI states |
| 2021 | Flynn's Taxonomy | 1 | Classification |
| 2020 | UMA vs NUMA | 2 | Identification |

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| Amdahl speedup | ≤ 1/(1-P) |
| SIMD | Vector/GPU operations |
| Write to shared (MESI) | Others → Invalid |
| Snooping vs Directory | Bus vs Point-to-point |

---

## 🧮 Solved Examples

### Example 1: Amdahl's Law
**Given:** Program is 80% parallelizable, 4 processors

**Solution:**
$$S = \frac{1}{(1-0.8) + 0.8/4} = \frac{1}{0.2 + 0.2} = \frac{1}{0.4} = 2.5$$

### Example 2: Break-Even Processors
**Given:** 90% parallelizable, want speedup of 8x

**Solution:**
$$8 = \frac{1}{0.1 + 0.9/N}$$
$$0.1 + 0.9/N = 0.125$$
$$0.9/N = 0.025$$
$$N = 36 \text{ processors}$$

### Example 3: MESI State Sequence
**Given:** CPUs 0 and 1, initially both have X in Shared (S) state.
CPU 0 writes to X.

**Solution:**
1. CPU 0 broadcasts write intent
2. CPU 1 snoops, transitions S → I (Invalid)
3. CPU 0 transitions S → M (Modified)
4. Memory NOT updated yet (write-back)

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Would you like to initiate a **'Multi-Variable Stress Test'** combining Parallel Processing with Pipelining Speedup for a Rank-1 simulation?*

---
[← Previous: I/O Systems](./07-IO-Systems.md) | [Back to Index](./README.md) | [Next: Exam Traps & Techniques →](./09-Exam-Traps-Techniques.md)
