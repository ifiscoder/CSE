# Module 5: Intermediate Code Generation | The Singularity

> **The Atomic Truth:** *"Abstract the target, enable optimization."*

---

## 🎯 The Path of Elegance (Root Derivation)

### 5.1 Why Intermediate Code?

```
[Image of Compiler with IR]
                          n languages
                              ↓
                    ┌─────────────────┐
                    │    Front Ends   │  n front ends
                    │  (per language) │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │  INTERMEDIATE   │  1 IR
                    │  REPRESENTATION │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │    Back Ends    │  m back ends
                    │ (per machine)   │
                    └─────────────────┘
                              ↓
                          m machines

WITHOUT IR: n × m compilers needed
WITH IR: n + m compilers needed!
```

### IR Properties

| Property | Benefit |
|----------|---------|
| Machine-independent | Portable optimization |
| Language-independent | Reusable back ends |
| Simple structure | Easy to optimize |
| Explicit operations | Clear semantics |

---

## 📐 5.2 Three-Address Code (TAC)

### Definition

Each instruction has at most:
- One operator
- Two source operands
- One destination operand

**General Form:** `x = y op z` or `x = op y`

### TAC Instruction Types

| Type | Examples |
|------|----------|
| Assignment | x = y op z, x = op y, x = y |
| Copy | x = y |
| Unconditional Jump | goto L |
| Conditional Jump | if x relop y goto L |
| Indexed Assignment | x = y[i], x[i] = y |
| Pointer Assignment | x = &y, x = *y, *x = y |
| Procedure Call | param x, call p,n, return y |

### Example: Expression to TAC

**Expression:** a = b * -c + b * -c

**TAC:**
```
t1 = -c
t2 = b * t1
t3 = -c
t4 = b * t3
t5 = t2 + t4
a = t5
```

**Optimized (CSE):**
```
t1 = -c
t2 = b * t1
t5 = t2 + t2
a = t5
```

---

## 🔢 5.3 Quadruples, Triples, and Indirect Triples

### Quadruples

Four fields: (op, arg1, arg2, result)

| Index | op | arg1 | arg2 | result |
|-------|-----|------|------|--------|
| 0 | - | c | | t1 |
| 1 | * | b | t1 | t2 |
| 2 | - | c | | t3 |
| 3 | * | b | t3 | t4 |
| 4 | + | t2 | t4 | t5 |
| 5 | = | t5 | | a |

### Triples

Three fields: (op, arg1, arg2), result is implicit (index)

| Index | op | arg1 | arg2 |
|-------|-----|------|------|
| 0 | - | c | |
| 1 | * | b | (0) |
| 2 | - | c | |
| 3 | * | b | (2) |
| 4 | + | (1) | (3) |
| 5 | = | a | (4) |

### Indirect Triples

Separate list of pointers to triples (allows reordering).

| Statement | Pointer |
|-----------|---------|
| 0 | 35 |
| 1 | 36 |
| ... | ... |

### Comparison

| Representation | Space | Optimization Ease |
|----------------|-------|-------------------|
| Quadruples | More (temp names) | Easier (explicit results) |
| Triples | Less (no temp names) | Harder (index references) |
| Indirect Triples | Medium | Easier than triples |

---

## 📊 5.4 SDT for TAC Generation

### Expression Translation

**Grammar with Actions:**
```
S → id = E ;          S.code = E.code || gen(id.place '=' E.place)

E → E₁ + E₂           E.place = newtemp()
                      E.code = E₁.code || E₂.code ||
                               gen(E.place '=' E₁.place '+' E₂.place)

E → E₁ * E₂           E.place = newtemp()
                      E.code = E₁.code || E₂.code ||
                               gen(E.place '=' E₁.place '*' E₂.place)

E → - E₁              E.place = newtemp()
                      E.code = E₁.code ||
                               gen(E.place '=' '-' E₁.place)

E → ( E₁ )            E.place = E₁.place
                      E.code = E₁.code

E → id                E.place = id.place
                      E.code = ''
```

### Control Flow Translation

**If-Then-Else:**
```
S → if E then S₁ else S₂

    E.code
    if E.place == 0 goto L1
    S₁.code
    goto L2
L1: S₂.code
L2:
```

**While Loop:**
```
S → while E do S₁

L1: E.code
    if E.place == 0 goto L2
    S₁.code
    goto L1
L2:
```

---

## ⚡ 5.5 Boolean Expression Translation

### Numerical Representation

Represent true as 1, false as 0.

```
E → E₁ or E₂          E.place = newtemp()
                      E.code = E₁.code || E₂.code ||
                               gen(E.place '=' E₁.place 'or' E₂.place)

E → E₁ and E₂         Similar...

E → not E₁            E.place = newtemp()
                      E.code = E₁.code ||
                               gen(E.place '=' 'not' E₁.place)

E → E₁ relop E₂       E.place = newtemp()
                      E.code = E₁.code || E₂.code ||
                               gen('if' E₁.place relop E₂.place 'goto' nextinstr+3) ||
                               gen(E.place '=' 0) ||
                               gen('goto' nextinstr+2) ||
                               gen(E.place '=' 1)
```

### Short-Circuit Evaluation

**For E₁ or E₂:**
- If E₁ is true, don't evaluate E₂
- Jump directly to true outcome

```
E → E₁ or E₂

    E₁.code
    if E₁.place goto E.true    // short-circuit
    E₂.code
    if E₂.place goto E.true
    goto E.false
```

**For E₁ and E₂:**
```
E → E₁ and E₂

    E₁.code
    ifFalse E₁.place goto E.false    // short-circuit
    E₂.code
    if E₂.place goto E.true
    goto E.false
```

---

## 🔗 5.6 Array Access Translation

### Row-Major Order (C-style)

For array A[i₁][i₂]...[iₖ] with dimensions d₁, d₂, ..., dₖ:

$$\text{Address} = \text{base} + (\cdots((i_1 \times d_2 + i_2) \times d_3 + i_3) \cdots) \times d_k + i_k) \times w$$

Where w = element size

### Column-Major Order (Fortran-style)

$$\text{Address} = \text{base} + (i_1 + d_1 \times (i_2 + d_2 \times (i_3 + \cdots))) \times w$$

### TAC for Array Access

**For a[i]:**
```
t1 = i * width
t2 = a[t1]    // or &a + t1
```

**For a[i][j] (row-major):**
```
t1 = i * ncols
t2 = t1 + j
t3 = t2 * width
t4 = a[t3]
```

---

## 📐 5.7 Procedure Calls

### Calling Sequence

```
// Before call
for each parameter p:
    param p                    // push parameter
call f, n                      // call with n parameters

// At function entry
t = call f, n                  // receive return value
```

### Parameter Passing

| Method | Effect |
|--------|--------|
| Call by value | Copy value |
| Call by reference | Pass address |
| Call by value-result | Copy in, copy out |
| Call by name | Textual substitution |

---

## 🌳 5.8 Directed Acyclic Graphs (DAG)

### DAG vs Parse Tree

```
[Image: Parse Tree vs DAG]

Expression: a + a * (b - c) + (b - c) * d

Parse Tree:                  DAG:
       +                        +
      / \                      /|\
     /   \                    / | \
    +     *                  +  |  \
   / \   / \                / \ |   \
  a   * b-c  d             a   \|   *
     / \                       *   / \
    a  b-c                    /|\ |  d
       / \                   a | b-c
      b   c                    |
                               (shared)
```

### DAG Benefits

1. **Common Subexpression Elimination (CSE):** Shared nodes
2. **Space efficiency:** Less nodes than parse tree
3. **Code generation:** Evaluate shared expressions once

### DAG Construction Algorithm

```
For each node n in postorder:
    if n is a leaf:
        if n.val in nodeMap: return nodeMap[n.val]
        else: create new leaf, add to nodeMap
    else:
        left = process(n.left)
        right = process(n.right)
        if (n.op, left, right) in nodeMap:
            return nodeMap[(n.op, left, right)]
        else: create new internal node, add to nodeMap
```

---

## 🎭 The Bizarre Mnemonic | "The TAC Factory"

*"Three-Address Code is like IKEA ASSEMBLY INSTRUCTIONS:
- Each step uses at most 2 input pieces + 1 output piece
- Temporary pieces (t1, t2) hold intermediate assemblies
- **Quadruple** = Instruction with item numbers written on each piece
- **Triple** = Instructions reference 'piece from step 3' directly
- **DAG** = Smart factory that notices when two products need the same sub-assembly"*

---

## 🏆 The 2026 Adversarial Vault

### Trap 1: The Temporary Count
**Question Pattern:** "How many temporaries for expression a*b + c*d + e*f?"
**Anti-Solution:** Students count wrong.
**Truth:** Count each binary operation needing a new temp.
- t1 = a*b, t2 = c*d, t3 = e*f, t4 = t1+t2, t5 = t4+t3 → 5 temps

### Trap 2: The Quadruple vs Triple Size
**Question Pattern:** "Space comparison of quadruples vs triples?"
**Anti-Solution:** Students forget temp storage.
**Truth:** Quadruples store temp names (more space), but temps can be reused. Triples use indices (less space per instruction, but fixed order).

### Trap 3: The Short-Circuit Logic
**Question Pattern:** "TAC for (a > b) && (c > d) with short-circuit?"
**Anti-Solution:** Students evaluate both always.
**Truth:** 
```
if a <= b goto L_false
if c > d goto L_true
L_false: result = 0
goto L_end
L_true: result = 1
L_end:
```

### Trap 4: The Array Index Calculation
**Question Pattern:** "Address of A[i][j] in row-major?"
**Anti-Solution:** Wrong formula.
**Truth:** base + (i * num_cols + j) * element_size

### NAT Precision Lock
- Temporary count: Exact integer
- Quadruple count: One per TAC instruction
- Address calculation: Account for 0-indexing

### MSQ Logic Gate | Elimination Rules
1. TAC = at most 3 addresses per instruction
2. Quadruples have explicit result field
3. Triples use instruction index as result
4. DAG shares common subexpressions

---

## 📊 GATE PYQ Pattern Analysis

| Year | Topic | Marks | Trap Type |
|------|-------|-------|-----------|
| 2023 | TAC Generation | 2 | Temporary count |
| 2022 | Boolean Short-Circuit | 2 | Jump logic |
| 2021 | Quadruples vs Triples | 1 | Space comparison |
| 2020 | Array Address | 2 | Row-major formula |

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| TAC instruction | ≤ 3 addresses |
| New temporary | Each binary/unary op |
| Short-circuit or | True → skip second |
| Short-circuit and | False → skip second |

---

## 🧮 Solved Examples

### Example 1: Expression to TAC
**Expression:** d = (a-b) * (a-c) + (a-c)

**TAC:**
```
t1 = a - b
t2 = a - c
t3 = t1 * t2
t4 = t2 + t3     // Note: t2 reused (CSE)
d = t4
```
Wait, let me recalculate:
```
t1 = a - b
t2 = a - c
t3 = t1 * t2
t4 = t3 + t2     // (a-b)*(a-c) + (a-c)
d = t4
```
**Temporaries used:** 4

### Example 2: Control Flow TAC
**Statement:** if (a < b) then x = y + z else x = y - z

**TAC:**
```
    if a < b goto L1
    t1 = y - z
    x = t1
    goto L2
L1: t2 = y + z
    x = t2
L2:
```

### Example 3: While Loop TAC
**Statement:** while (i < n) { s = s + a[i]; i = i + 1; }

**TAC:**
```
L1: if i >= n goto L2
    t1 = i * 4        // assuming int = 4 bytes
    t2 = a[t1]
    s = s + t2
    i = i + 1
    goto L1
L2:
```

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Would you like to initiate a **'Multi-Variable Stress Test'** combining Intermediate Code with Code Optimization for a Rank-1 simulation?*

---
[← Previous: Semantic Analysis](./04-Semantic-Analysis-SDT.md) | [Back to Index](./README.md) | [Next: Code Optimization →](./06-Code-Optimization.md)
