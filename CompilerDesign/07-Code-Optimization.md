# Chapter 7: Code Optimization

## 🎯 The Atomic Truth
> **"Optimization = Same Result, Fewer Resources"**

---

## 7.1 What is Code Optimization?

### Definition
**Code Optimization** is the phase that transforms code to use fewer resources (time, space) while preserving the program's semantics.

```
┌────────────────────────────────────────────────────────────────────────┐
│                       CODE OPTIMIZATION                                │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   ┌─────────────┐      ┌─────────────────┐      ┌─────────────────┐   │
│   │ Intermediate│      │   OPTIMIZER     │      │   Optimized     │   │
│   │    Code     │ ──►  │                 │ ──►  │     Code        │   │
│   │             │      │ - Faster        │      │                 │   │
│   └─────────────┘      │ - Smaller       │      └─────────────────┘   │
│                        │ - Less power    │                            │
│                        └─────────────────┘                            │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### The Golden Rules of Optimization
1. **Correctness:** Never change program behavior
2. **Worth the effort:** Optimization benefits > Optimization cost
3. **Focus on hot spots:** 90% of time in 10% of code (80-20 rule)

### 🧠 Analogy: The Efficient Chef
A chef optimizing a recipe:
- **Constant Folding:** Pre-measure ingredients
- **Dead Code Elimination:** Don't prepare unused garnishes
- **Loop Optimization:** Batch similar operations
- **Common Subexpression:** Chop onions once for multiple dishes

---

## 7.2 Classification of Optimizations

### By Scope

| Type | Scope | Examples |
|------|-------|----------|
| **Local** | Basic block | Constant folding, CSE |
| **Global** | Function/Procedure | Live variable analysis |
| **Interprocedural** | Across functions | Inline expansion |

### By Dependence

| Type | Requires |
|------|----------|
| **Machine Independent** | Works on IR, any target |
| **Machine Dependent** | Specific to target architecture |

### Machine Independent Optimizations
- Constant folding
- Constant propagation
- Copy propagation
- Dead code elimination
- Common subexpression elimination
- Loop optimizations

### Machine Dependent Optimizations
- Register allocation
- Instruction scheduling
- Peephole optimization

---

## 7.3 Basic Blocks and Flow Graphs

### Basic Block
A **Basic Block** is a maximal sequence of consecutive statements with:
- One entry point (first statement)
- One exit point (last statement)
- No jumps in (except to first)
- No jumps out (except from last)

### Algorithm to Identify Basic Blocks
```
1. Identify leaders (first statement of each block):
   a) First statement is a leader
   b) Target of any jump is a leader
   c) Statement after a jump is a leader

2. A basic block = Leader + all statements until next leader
```

### Example
```
1.  i = 1            ← Leader (first)
2.  j = 1
3.  t1 = 10 * i
4.  t2 = t1 + j
5.  t3 = 8 * t2
6.  t4 = t3 - 88
7.  a[t4] = 0
8.  j = j + 1
9.  if j <= 10 goto 3  ← End of B1
10. i = i + 1        ← Leader (after jump)
11. if i <= 10 goto 2  ← End of B2
12. i = 1            ← Leader (after jump)
```

**Basic Blocks:**
- B1: Statements 1-9
- B2: Statements 10-11
- B3: Statement 12...

### Control Flow Graph (CFG)
A **CFG** is a directed graph where:
- Nodes = Basic blocks
- Edges = Control flow between blocks

```
        ┌─────┐
        │ B1  │
        └──┬──┘
           │
     ┌─────▼─────┐
     │    B2     │◄────┐
     └─────┬─────┘     │
           │           │
     ┌─────▼─────┐     │
     │    B3     │─────┘
     └─────┬─────┘
           │
     ┌─────▼─────┐
     │   EXIT    │
     └───────────┘
```

---

## 7.4 Local Optimizations

### 7.4.1 Constant Folding
**Definition:** Evaluate constant expressions at compile time.

```
Before:                After:
x = 2 + 3              x = 5
y = x * 4              y = 20  (if x known)
```

### 7.4.2 Constant Propagation
**Definition:** Replace variables with their constant values.

```
Before:                After:
pi = 3.14              pi = 3.14
r = 10                 r = 10
area = pi * r * r      area = 3.14 * 10 * 10  →  area = 314.0
```

### 7.4.3 Copy Propagation
**Definition:** Replace uses of copied variable with original.

```
Before:                After:
x = y                  x = y
z = x + 5              z = y + 5  (x replaced by y)
```

### 7.4.4 Dead Code Elimination
**Definition:** Remove code that has no effect on program output.

```
Before:                After:
x = y + 1              // removed (x never used)
z = 5                  z = 5
print(z)               print(z)
```

**Types of Dead Code:**
1. Unreachable code (never executed)
2. Dead assignments (result never used)

### 7.4.5 Common Subexpression Elimination (CSE)
**Definition:** Reuse previously computed expression values.

```
Before:                After:
t1 = a + b             t1 = a + b
t2 = a + b             t2 = t1      (reuse t1)
t3 = t1 * t2           t3 = t1 * t1
```

### 7.4.6 Algebraic Simplification
**Definition:** Apply algebraic identities to simplify code.

| Original | Optimized | Rule |
|----------|-----------|------|
| x + 0 | x | Additive identity |
| x * 1 | x | Multiplicative identity |
| x * 0 | 0 | Multiplication by zero |
| x / 1 | x | Division identity |
| x - x | 0 | Self-subtraction |
| x * 2 | x + x or x << 1 | Strength reduction |

### 7.4.7 Strength Reduction
**Definition:** Replace expensive operations with cheaper ones.

| Expensive | Cheap |
|-----------|-------|
| x * 2 | x + x or x << 1 |
| x * 8 | x << 3 |
| x / 2 | x >> 1 |
| x^2 | x * x |
| x % 8 | x & 7 (for positive x) |

---

## 7.5 Data Flow Analysis

### Definition
**Data Flow Analysis** collects information about how data flows through the program.

### Key Concepts

| Term | Definition |
|------|------------|
| **Definition** | Assignment to variable |
| **Use** | Read of variable |
| **Live** | Variable may be used later |
| **Dead** | Variable won't be used later |
| **Available** | Expression already computed |
| **Reaching** | Definition can reach a point |

### 7.5.1 Reaching Definitions
**Definition:** A definition d **reaches** point p if there's a path from d to p with no other definition of the same variable.

**Used for:** Constant propagation, detecting uninitialized variables

### Data Flow Equations
```
GEN[B] = Definitions in B that reach end of B
KILL[B] = Definitions killed (overwritten) by B

OUT[B] = GEN[B] ∪ (IN[B] - KILL[B])
IN[B] = ∪ OUT[P] for all predecessors P of B
```

### 7.5.2 Live Variable Analysis
**Definition:** Variable v is **live** at point p if there's a path from p to a use of v with no definition of v.

**Used for:** Register allocation, dead code elimination

### Data Flow Equations (Backward)
```
USE[B] = Variables used in B before definition
DEF[B] = Variables defined in B

IN[B] = USE[B] ∪ (OUT[B] - DEF[B])
OUT[B] = ∪ IN[S] for all successors S of B
```

### 7.5.3 Available Expressions
**Definition:** Expression e is **available** at point p if every path to p computes e and no operand of e is modified after that.

**Used for:** Common subexpression elimination

---

## 7.6 Loop Optimizations

### Why Focus on Loops?
Most programs spend 90% of execution time in loops.

### 7.6.1 Loop Invariant Code Motion
**Definition:** Move computations that don't change within loop to outside.

```
Before:                After:
for (i = 0; i < n;) {  t1 = n * m    // moved out
    x = n * m + i;     for (i = 0; i < n;) {
    i++;                   x = t1 + i;
}                          i++;
                       }
```

### 7.6.2 Induction Variables
**Definition:** Variables that change by constant amount each iteration.

**Types:**
- **Basic:** Loop counter (i)
- **Dependent:** Derived from basic (j = 4*i)

### 7.6.3 Strength Reduction for Loops
Replace multiplication with addition in loops.

```
Before:                After:
for (i = 0; i < n;) {  t = 0
    t = i * 4;         for (i = 0; i < n;) {
    a[t] = 0;              a[t] = 0;
    i++;                   t = t + 4;  // cheaper!
}                          i++;
                       }
```

### 7.6.4 Loop Unrolling
**Definition:** Replicate loop body to reduce loop overhead.

```
Before:                After:
for (i=0; i<100; i++)  for (i=0; i<100; i+=4) {
    a[i] = 0;              a[i] = 0;
                           a[i+1] = 0;
                           a[i+2] = 0;
                           a[i+3] = 0;
                       }
```

**Benefits:**
- Fewer loop control instructions
- More opportunities for other optimizations

**Drawbacks:**
- Larger code size
- May cause cache issues

### 7.6.5 Loop Fusion (Loop Jamming)
**Definition:** Combine adjacent loops with same bounds.

```
Before:                After:
for (i=0; i<n; i++)    for (i=0; i<n; i++) {
    a[i] = 0;              a[i] = 0;
for (i=0; i<n; i++)        b[i] = 1;
    b[i] = 1;          }
```

### 7.6.6 Loop Fission (Loop Distribution)
**Definition:** Split loop into multiple loops.

**Use:** Improve cache locality, enable vectorization

---

## 7.7 Global Optimizations

### 7.7.1 Global Common Subexpression Elimination
CSE across basic blocks using available expressions.

```
B1: t1 = a + b

B2: if (...) {        B3: else {
    t2 = a + b            t3 = a + b
    // t2 = t1            // t3 = t1
}                     }
```

### 7.7.2 Global Copy Propagation
Propagate copies across basic blocks.

### 7.7.3 Global Dead Code Elimination
Remove dead code using live variable analysis.

---

## 7.8 Peephole Optimization

### Definition
**Peephole optimization** examines a small window (peephole) of instructions and replaces with better sequence.

### Common Peephole Optimizations

#### 1. Redundant Load/Store Elimination
```
Before:                After:
MOV R1, a              MOV R1, a
MOV a, R1              // second instruction removed
```

#### 2. Unreachable Code Elimination
```
Before:                After:
    goto L2                goto L2
    x = y + z              // removed (unreachable)
L2: ...                L2: ...
```

#### 3. Jump Optimization
```
Before:                After:
    goto L1                goto L2
L1: goto L2            // L1 eliminated
```

#### 4. Algebraic Simplification
```
Before:                After:
x = x + 0              // removed
x = x * 1              // removed
```

#### 5. Reduction in Strength
```
Before:                After:
x = x * 2              x = x << 1
x = x / 4              x = x >> 2
```

---

## 7.9 Register Allocation

### Problem
Map unlimited virtual registers/variables to limited physical registers.

### Graph Coloring Approach
1. Build **interference graph:**
   - Node = Variable
   - Edge = Variables live simultaneously

2. **Color the graph:**
   - Colors = Registers
   - Adjacent nodes need different colors

3. If not colorable with k colors (k registers):
   - **Spill** some variables to memory

### Example
```
Variables: a, b, c, d
Live ranges:
  a: [1, 5]
  b: [2, 4]
  c: [3, 6]
  d: [5, 7]

Interference graph:
    a ── b
    │ ╲  │
    │  ╲ │
    c ── d

With 2 registers (colors):
  R1: a, d  (not simultaneous)
  R2: b, c  (b ends before c needs R2)

Actually: a-b conflict, a-c conflict, b-c conflict, c-d conflict
Need 3 colors minimum!
```

---

## 7.10 Instruction Scheduling

### Problem
Reorder instructions to minimize stalls (due to dependencies, cache misses).

### Types of Dependencies
- **True (RAW):** Read After Write - can't reorder
- **Anti (WAR):** Write After Read - can reorder with renaming
- **Output (WAW):** Write After Write - can reorder with renaming

### Example
```
Before (with stall):       After (scheduled):
LOAD R1, a                 LOAD R1, a
ADD R2, R1, R1  ; stall!   LOAD R3, b  ; no stall
LOAD R3, b                 ADD R2, R1, R1  ; R1 ready now
MUL R4, R2, R3             MUL R4, R2, R3
```

---

## 7.11 Optimization Summary Table

| Optimization | Type | What It Does |
|--------------|------|--------------|
| Constant Folding | Local | Compute constants at compile time |
| Constant Propagation | Local/Global | Replace variable with constant |
| Copy Propagation | Local/Global | Replace copy with original |
| Dead Code Elimination | Local/Global | Remove unused code |
| CSE | Local/Global | Reuse computed expressions |
| Strength Reduction | Local/Loop | Replace expensive ops with cheaper |
| Loop Invariant Motion | Loop | Move invariant code out of loop |
| Induction Variable | Loop | Simplify loop variable calculations |
| Loop Unrolling | Loop | Replicate body, reduce overhead |
| Peephole | Target | Optimize small instruction windows |
| Register Allocation | Target | Map variables to registers |

---

## 7.12 GATE Previous Year Patterns

### Pattern 1: Identify Optimization
**Q:** What optimization is applied?
```
Before: x = 2 * 3 + y
After:  x = 6 + y
```
**A:** Constant Folding

### Pattern 2: Apply Optimization
**Q:** Apply CSE to given code.
**Approach:** Find repeated expressions, use temporaries.

### Pattern 3: Basic Block Identification
**Q:** How many basic blocks?
**Approach:** Count leaders.

### Pattern 4: Live Variable Analysis
**Q:** Is variable live at point P?
**Approach:** Trace usage paths.

---

## 📝 Quick Revision Points

1. **Optimization:** Same semantics, fewer resources
2. **Basic Block:** Single entry, single exit, no jumps
3. **CFG:** Nodes = blocks, Edges = control flow
4. **Constant Folding:** Evaluate constants at compile time
5. **CSE:** Reuse computed expressions
6. **Dead Code:** Code with no effect on output
7. **Loop Invariant:** Move unchanging code out of loop
8. **Strength Reduction:** Replace expensive with cheap ops
9. **Peephole:** Small window optimization
10. **Register Allocation:** Graph coloring approach

---

## 🧠 Mnemonic Summary

### Local Optimizations
> **"CCCD-CS"**
> - **C**onstant folding
> - **C**onstant propagation
> - **C**opy propagation
> - **D**ead code elimination
> - **C**ommon **S**ubexpression elimination

### Loop Optimizations
> **"ISUF"**
> - **I**nvariant code motion
> - **S**trength reduction
> - **U**nrolling
> - **F**usion

### Data Flow Directions
> **"Reaching goes Forward, Liveness goes Backward"**

---

## 🔥 The Adversarial Vault

### Trap 1: Dead vs Unreachable
**Q:** What's the difference?
- **Dead code:** Executed but result unused
- **Unreachable code:** Never executed (after goto)

### Trap 2: CSE Conditions
**Q:** Can always apply CSE?
**A:** NO! Must ensure operands haven't changed between uses.

### Trap 3: Loop Invariant Safety
**Q:** Always safe to move invariant out?
**A:** NO! Must ensure:
- Dominates all uses in loop
- Not modified by any statement in loop
- Loop executes at least once (or check first)

---

## ✅ Self-Assessment Questions

1. Identify basic blocks in given code.
2. Apply constant propagation and folding to code.
3. Find common subexpressions and optimize.
4. Perform loop invariant code motion.
5. Build interference graph for register allocation.

---

**Next Chapter:** [Code Generation →](08-Code-Generation.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
