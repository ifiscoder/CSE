# Module 6: Code Optimization | The Singularity

> **The Atomic Truth:** *"Same semantics, better performance."*

---

## 🎯 The Path of Elegance (Root Derivation)

### 6.1 Optimization Overview

```
[Image of Optimization Position]
    Source → Front End → IR → OPTIMIZATION → Code Gen → Target
                              ↓
                    ┌─────────────────────────┐
                    │   Machine-Independent   │
                    │   - CSE                 │
                    │   - Dead code removal   │
                    │   - Loop optimization   │
                    └─────────────────────────┘
                              ↓
                    ┌─────────────────────────┐
                    │   Machine-Dependent     │
                    │   - Register allocation │
                    │   - Instruction select  │
                    │   - Peephole            │
                    └─────────────────────────┘
```

### Optimization Principles

1. **Preserve semantics:** Output must be equivalent
2. **Improve performance:** Reduce time/space/power
3. **Worth the effort:** Benefit > compilation cost

### Classification

| Level | Scope | Examples |
|-------|-------|----------|
| Local | Basic block | CSE, algebraic simplification |
| Global | Procedure | Live variable, reaching definitions |
| Interprocedural | Whole program | Inlining, alias analysis |

---

## 📐 6.2 Basic Blocks and Control Flow Graphs

### Basic Block Definition

A **basic block** is a maximal sequence of consecutive statements such that:
1. Control enters only at the first statement
2. Control leaves only from the last statement

### Identifying Basic Blocks

**Leaders (first statements of blocks):**
1. First statement of the program
2. Target of any jump
3. Statement immediately after a jump

### Example

```
1: i = 1
2: j = 1
3: t1 = 10 * i
4: t2 = t1 + j
5: t3 = 8 * t2
6: t4 = t3 - 88
7: a[t4] = 0.0
8: j = j + 1
9: if j <= 10 goto 3
10: i = i + 1
11: if i <= 10 goto 2
12: ...
```

**Leaders:** 1, 2, 3, 10, 12
**Blocks:**
- B1: {1}
- B2: {2}
- B3: {3, 4, 5, 6, 7, 8, 9}
- B4: {10, 11}
- B5: {12, ...}

### Control Flow Graph (CFG)

```
[Image of CFG]
    ┌───────┐
    │  B1   │
    └───┬───┘
        ↓
    ┌───────┐
    │  B2   │◄─────┐
    └───┬───┘      │
        ↓          │
    ┌───────┐      │
    │  B3   │──────┼──┐
    └───┬───┘      │  │
        │ (j > 10) │  │ (j ≤ 10)
        ↓          │  │
    ┌───────┐      │  │
    │  B4   │──────┘  │
    └───┬───┘         │
        │ (i > 10)    │
        ↓             │
    ┌───────┐         │
    │  B5   │         │
    └───────┘         │
                      │
        └─────────────┘
```

---

## ⚡ 6.3 Local Optimizations

### Common Subexpression Elimination (CSE)

**Before:**
```
t1 = a + b
t2 = a + b
t3 = t1 * t2
```

**After:**
```
t1 = a + b
t3 = t1 * t1
```

### Dead Code Elimination

**Definition:** Code whose result is never used.

**Before:**
```
x = y + z    // x never used after this
a = b + c
return a
```

**After:**
```
a = b + c
return a
```

### Algebraic Simplification

| Pattern | Replacement |
|---------|-------------|
| x + 0 | x |
| x * 1 | x |
| x * 0 | 0 |
| x / 1 | x |
| x - 0 | x |
| x ^ 2 | x * x |

### Strength Reduction

| Expensive | Cheaper |
|-----------|---------|
| x * 2 | x + x or x << 1 |
| x * 2^n | x << n |
| x / 2^n | x >> n |
| x % 2^n | x & (2^n - 1) |

### Constant Folding

**Before:**
```
x = 2 + 3
y = x * 4
```

**After:**
```
x = 5
y = 20
```

### Constant Propagation

**Before:**
```
x = 5
y = x + z
```

**After:**
```
x = 5
y = 5 + z
```

### Copy Propagation

**Before:**
```
x = y
z = x + 1
```

**After:**
```
x = y
z = y + 1
```
(x may become dead and removable)

---

## 🔄 6.4 Loop Optimization

### Loop Invariant Code Motion

**Before:**
```
while (i < n) {
    t = a * b;      // invariant: a, b don't change in loop
    x[i] = t + i;
    i++;
}
```

**After:**
```
t = a * b;          // moved outside loop
while (i < n) {
    x[i] = t + i;
    i++;
}
```

### Induction Variable Elimination

**Induction Variable:** Variable that changes by constant amount each iteration.

**Before:**
```
i = 0
t = 4 * i
while (i < n) {
    a[t] = 0
    i = i + 1
    t = 4 * i
}
```

**After:**
```
t = 0
while (t < 4*n) {
    a[t] = 0
    t = t + 4
}
```
(i eliminated entirely!)

### Loop Unrolling

**Before:**
```
for (i = 0; i < 100; i++) {
    a[i] = 0;
}
```

**After:**
```
for (i = 0; i < 100; i += 4) {
    a[i] = 0;
    a[i+1] = 0;
    a[i+2] = 0;
    a[i+3] = 0;
}
```

**Benefits:**
- Fewer loop overhead (compare, branch)
- More instruction-level parallelism

---

## 📊 6.5 Data Flow Analysis

### The Framework

For each statement s, compute:
- **IN[s]:** Facts true before s
- **OUT[s]:** Facts true after s

**Transfer Function:**
$$OUT[s] = f_s(IN[s])$$

**Meet Operation (at join points):**
$$IN[s] = \bigwedge_{p \in pred(s)} OUT[p]$$

### Reaching Definitions

**Definition:** A definition d **reaches** point p if there's a path from d to p with no redefinition.

**Transfer Function:**
$$OUT[B] = GEN[B] \cup (IN[B] - KILL[B])$$

Where:
- GEN[B] = definitions generated in B
- KILL[B] = definitions killed (redefined) by B

**Meet:** Union (may analysis)

### Live Variable Analysis

**Definition:** Variable v is **live** at point p if v's current value may be used on some path from p.

**Transfer Function (backward):**
$$IN[B] = USE[B] \cup (OUT[B] - DEF[B])$$

Where:
- USE[B] = variables used before definition in B
- DEF[B] = variables defined in B

**Meet:** Union

### Available Expressions

**Definition:** Expression e is **available** at point p if e is computed on all paths to p and not killed.

**Transfer Function:**
$$OUT[B] = GEN[B] \cup (IN[B] - KILL[B])$$

**Meet:** Intersection (must analysis)

### Summary Table

| Analysis | Direction | Meet | For |
|----------|-----------|------|-----|
| Reaching Definitions | Forward | ∪ | CSE, constant prop |
| Live Variables | Backward | ∪ | Dead code elim |
| Available Expressions | Forward | ∩ | CSE |
| Very Busy Expressions | Backward | ∩ | Code hoisting |

---

## 🔧 6.6 Peephole Optimization

### Definition

Examine small "window" (peephole) of instructions, apply local transformations.

### Common Peephole Optimizations

| Pattern | Replacement |
|---------|-------------|
| `MOV R1, R2; MOV R2, R1` | `MOV R1, R2` |
| `JUMP L1; L1: ...` | Remove jump |
| `JUMP L1; L1: JUMP L2` | `JUMP L2` |
| `if a < b goto L; goto M` | `if a >= b goto M` |
| `ADD R, 0` | Remove |
| `MUL R, 1` | Remove |

### Jump Chain Elimination

**Before:**
```
    goto L1
...
L1: goto L2
...
L2: goto L3
```

**After:**
```
    goto L3
...
L1: goto L3
...
L2: goto L3
```

---

## 🎭 The Bizarre Mnemonic | "The Code Diet"

*"Code optimization is like putting code on a DIET:
- **Dead Code Elimination:** Remove the fat (unused code)
- **CSE:** Don't cook the same meal twice
- **Constant Folding:** Pre-calculate the recipe quantities
- **Strength Reduction:** Use microwave instead of oven (cheaper operation)
- **Loop Invariant Motion:** Don't bring groceries into the kitchen each time you cook
- **Peephole:** Quick fixes at the final check"*

---

## 🏆 The 2026 Adversarial Vault

### Trap 1: The CSE Validity
**Question Pattern:** "Can we apply CSE to a + b across a function call?"
**Anti-Solution:** Students say yes.
**Truth:** NO! Function call may modify a or b. Must check for intervening modifications.

### Trap 2: The Live Variable Direction
**Question Pattern:** "Live variable analysis direction?"
**Anti-Solution:** Students say forward.
**Truth:** BACKWARD! We check if current value is used later.

### Trap 3: The Loop Invariant Condition
**Question Pattern:** "When can x = a + b be moved out of loop?"
**Anti-Solution:** Students ignore multiple definitions.
**Truth:** a and b must not be modified in the loop AND x has only one definition in the loop.

### Trap 4: The Meet Operation
**Question Pattern:** "Meet operation for available expressions?"
**Anti-Solution:** Students say union.
**Truth:** INTERSECTION! Expression must be available on ALL paths (must analysis).

### Trap 5: The Basic Block Identification
**Question Pattern:** "How many basic blocks in this code?"
**Anti-Solution:** Wrong leader identification.
**Truth:** Count leaders correctly: first statement, jump targets, statements after jumps.

### NAT Precision Lock
- Basic block count: Exact integer
- GEN/KILL set cardinality: Count carefully

### MSQ Logic Gate | Elimination Rules
1. Live analysis = Backward
2. Reaching definitions = Forward
3. Available expressions = Intersection (∩)
4. Dead code = Never used result

---

## 📊 GATE PYQ Pattern Analysis

| Year | Topic | Marks | Trap Type |
|------|-------|-------|-----------|
| 2023 | Basic Block Count | 1 | Leader identification |
| 2022 | Live Variables | 2 | Direction confusion |
| 2021 | CSE | 2 | Modification check |
| 2020 | Data Flow Equations | 2 | GEN/KILL sets |

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| Basic block | Single entry, single exit |
| Live variable | Backward analysis |
| Available expression | Intersection meet |
| Loop invariant | Not modified in loop |

---

## 🧮 Solved Examples

### Example 1: Basic Block Identification
**Code:**
```
1: sum = 0
2: i = 1
3: t = 2 * i
4: sum = sum + t
5: i = i + 1
6: if i <= n goto 3
7: print sum
```

**Leaders:** 1, 3, 7
**Blocks:**
- B1: {1, 2} - statements 1-2
- B2: {3, 4, 5, 6} - statements 3-6
- B3: {7} - statement 7

**Count: 3 basic blocks**

### Example 2: GEN/KILL for Reaching Definitions
**Block B:**
```
d1: x = a + b
d2: y = x + 1
d3: x = c + d
```

**GEN[B] = {d2, d3}** (d1 is killed by d3)
**KILL[B] = {all other definitions of x, y}**

### Example 3: Loop Invariant Code Motion
**Before:**
```
while (i < 100) {
    a = 5;          // invariant
    b = a * 3;      // invariant (a is invariant)
    c[i] = b + i;
    i = i + 1;
}
```

**After:**
```
a = 5;
b = a * 3;
while (i < 100) {
    c[i] = b + i;
    i = i + 1;
}
```

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Would you like to initiate a **'Multi-Variable Stress Test'** combining Code Optimization with Register Allocation for a Rank-1 simulation?*

---
[← Previous: Intermediate Code](./05-Intermediate-Code-Generation.md) | [Back to Index](./README.md) | [Next: Code Generation & Runtime →](./07-Code-Generation-Runtime.md)
