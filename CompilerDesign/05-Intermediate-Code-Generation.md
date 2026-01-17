# Chapter 5: Intermediate Code Generation

## 🎯 The Atomic Truth
> **"Intermediate Code = Machine-Independent Bridge"**

---

## 5.1 What is Intermediate Code?

### Definition
**Intermediate Code** is a machine-independent representation of source code that serves as a bridge between the front-end (analysis) and back-end (synthesis) of a compiler.

```
┌────────────────────────────────────────────────────────────────────────┐
│                     INTERMEDIATE CODE GENERATION                       │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   ┌─────────────┐      ┌─────────────────┐      ┌─────────────────┐   │
│   │  Annotated  │      │   Intermediate  │      │   Optimized /   │   │
│   │ Parse Tree  │ ──►  │   Code (TAC)    │ ──►  │  Target Code    │   │
│   │             │      │                 │      │                 │   │
│   └─────────────┘      └─────────────────┘      └─────────────────┘   │
│                                                                        │
│           FRONT END                    BACK END                        │
│     (Language Dependent)         (Machine Dependent)                   │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### Why Intermediate Code?

1. **Retargeting:** Same front-end, different back-ends
2. **Machine Independence:** Optimization done on IR, applies to all targets
3. **Modularity:** Easier to develop and maintain

### 🧠 Analogy: The Universal Recipe
IR is like writing a recipe in a universal format:
- **Source (French recipe)** → **IR (standard recipe)** → **Target (English recipe)**
- Change front-end for different source languages
- Change back-end for different machines

---

## 5.2 Types of Intermediate Representations

### Hierarchy
```
           HIGH-LEVEL IR
         (Close to source)
                │
                ▼
         AST, Parse Tree
                │
                ▼
          MEDIUM-LEVEL IR
       (Most optimizations here)
                │
                ▼
           Three Address Code
                │
                ▼
           LOW-LEVEL IR
        (Close to machine)
                │
                ▼
        Register Transfer Language
```

### Common IR Forms

| IR Type | Level | Example |
|---------|-------|---------|
| Parse Tree | High | Concrete syntax tree |
| Abstract Syntax Tree (AST) | High | Simplified tree |
| Three Address Code (TAC) | Medium | x = y op z |
| Quadruples | Medium | (op, arg1, arg2, result) |
| Triples | Medium | (op, arg1, arg2) |
| DAG | Medium | Directed Acyclic Graph |
| RTL | Low | Register operations |
| SSA | Medium | Static Single Assignment |

---

## 5.3 Three Address Code (TAC)

### Definition
**Three Address Code** is an IR where each instruction has at most three operands (addresses).

### General Form
```
x = y op z
```
Where:
- `x` = result (target)
- `y`, `z` = operands
- `op` = operator

### Types of TAC Instructions

#### 1. Assignment Statements
```
x = y op z       (binary operation)
x = op y         (unary operation)
x = y            (copy)
```

#### 2. Indexed Assignment
```
x = y[i]         (array access)
x[i] = y         (array assignment)
```

#### 3. Pointer Operations
```
x = &y           (address of)
x = *y           (dereference)
*x = y           (indirect assignment)
```

#### 4. Control Flow
```
goto L           (unconditional jump)
if x relop y goto L   (conditional jump)
if x goto L      (conditional jump)
```

#### 5. Function Calls
```
param x          (push parameter)
call p, n        (call function p with n params)
y = call p, n    (call with return value)
return x         (return from function)
```

### Example: TAC for Expression
**Source:** `a = b * -c + b * -c`

**TAC:**
```
t1 = -c
t2 = b * t1
t3 = -c
t4 = b * t3
t5 = t2 + t4
a = t5
```

**Optimized TAC (with CSE):**
```
t1 = -c
t2 = b * t1
t3 = t2 + t2
a = t3
```

---

## 5.4 Quadruples

### Definition
A **Quadruple** is a 4-field representation of TAC.

### Format
```
(operator, arg1, arg2, result)
```

### Example: Quadruples for `a = b * -c + b * -c`
| # | op | arg1 | arg2 | result |
|---|-----|------|------|--------|
| 0 | uminus | c | | t1 |
| 1 | * | b | t1 | t2 |
| 2 | uminus | c | | t3 |
| 3 | * | b | t3 | t4 |
| 4 | + | t2 | t4 | t5 |
| 5 | = | t5 | | a |

### Advantages
- Direct reference to temporaries
- Easy to rearrange code
- Constant space per instruction

### Disadvantages
- Extra space for result field (especially for temporaries)

---

## 5.5 Triples

### Definition
A **Triple** is a 3-field representation where results are referenced by their position number.

### Format
```
(operator, arg1, arg2)
```
Result is implicitly the triple's index.

### Example: Triples for `a = b * -c + b * -c`
| # | op | arg1 | arg2 |
|---|-----|------|------|
| 0 | uminus | c | |
| 1 | * | b | (0) |
| 2 | uminus | c | |
| 3 | * | b | (2) |
| 4 | + | (1) | (3) |
| 5 | = | a | (4) |

**(n)** means reference to result of triple n

### Advantages
- Saves space (no result field)

### Disadvantages
- Moving instructions requires updating references
- Not good for optimization

---

## 5.6 Indirect Triples

### Definition
**Indirect Triples** use a separate list of pointers to triples, allowing reordering without changing the triples.

### Example
**Pointer List:**
| # | Triple Ptr |
|---|------------|
| 0 | (35) |
| 1 | (36) |
| 2 | (37) |
| ... | ... |

**Triple Storage:**
| # | op | arg1 | arg2 |
|---|-----|------|------|
| 35 | uminus | c | |
| 36 | * | b | (35) |
| ... | ... | ... | ... |

### Advantages
- Easy to reorder (just change pointers)
- Optimizations don't affect triple references

---

## 5.7 Directed Acyclic Graph (DAG)

### Definition
A **DAG** is a compact representation of expressions where common subexpressions share nodes.

### Properties
- Leaves: Identifiers or constants
- Interior nodes: Operators
- **Shared nodes:** Common subexpressions

### Example: DAG for `a = b * -c + b * -c`

**Without CSE (Tree):**
```
               =
              / \
             a   +
                / \
               *   *
              /|   |\
             b -   - b
               |   |
               c   c
```

**With CSE (DAG):**
```
               =
              / \
             a   +
                / \
               ┌───┘
               *
              / \
             b   -
                 |
                 c
```

### Constructing DAG

**Algorithm:**
```
For each node n = (op, left, right):
    1. If n already exists in DAG, return pointer to it
    2. Otherwise, create new node
    3. Add to DAG table

Value Number Method:
- Hash (op, left_num, right_num)
- If found, reuse
- If not, create new entry
```

### 🎯 GATE Trap: DAG vs Tree
**Q:** How many nodes in DAG for (a+b)*(a+b)?
**A:** 3 nodes: a, b, and (+, a, b) — the + is shared!

---

## 5.8 TAC for Control Statements

### If-Then Statement
**Source:**
```c
if (x < y) then
    z = 1
```

**TAC:**
```
    if x < y goto L1
    goto L2
L1: z = 1
L2:
```

### If-Then-Else Statement
**Source:**
```c
if (x < y) then
    z = 1
else
    z = 2
```

**TAC:**
```
    if x < y goto L1
    goto L2
L1: z = 1
    goto L3
L2: z = 2
L3:
```

### While Loop
**Source:**
```c
while (x < y) do
    x = x + 1
```

**TAC:**
```
L1: if x < y goto L2
    goto L3
L2: x = x + 1
    goto L1
L3:
```

### For Loop
**Source:**
```c
for (i = 1; i <= 10; i++)
    sum = sum + i
```

**TAC:**
```
    i = 1
L1: if i <= 10 goto L2
    goto L3
L2: sum = sum + i
    i = i + 1
    goto L1
L3:
```

---

## 5.9 Boolean Expressions

### Two Methods

#### Method 1: Numerical Representation
- True = 1, False = 0
- Compute value like arithmetic expression

#### Method 2: Control Flow (Short-Circuit)
- Jump to true/false label based on condition
- More efficient for control statements

### Short-Circuit Evaluation
**Source:** `if (a < b || c > d) x = 1`

**TAC (Short-Circuit):**
```
    if a < b goto L_true    ; First condition true → done
    goto L_check            ; Check second condition
L_check:
    if c > d goto L_true    ; Second condition true → done
    goto L_false            ; Both false
L_true:
    x = 1
L_false:
```

### Boolean Expression TAC Patterns

#### AND (&&)
```
a && b:
    if a goto L1
    goto L_false
L1: if b goto L_true
    goto L_false
```

#### OR (||)
```
a || b:
    if a goto L_true
    goto L1
L1: if b goto L_true
    goto L_false
```

#### NOT (!)
```
!a:
    if a goto L_false
    goto L_true
```

---

## 5.10 Backpatching

### Problem
When generating code for control flow, we don't know jump target addresses yet.

### Solution: Backpatching
1. Generate jumps with empty targets
2. Keep lists of incomplete instructions
3. Fill in targets when they become known

### Key Operations
- `makelist(i)`: Create list containing only i
- `merge(p1, p2)`: Merge two lists
- `backpatch(p, i)`: Fill all instructions in list p with target i

### Example: If-Then-Else with Backpatching
**Source:** `if (a < b) then x = 1 else x = 2`

**Generation with Backpatching:**
```
Step 1: Generate condition
    100: if a < b goto _    ; true list = {100}
    101: goto _             ; false list = {101}

Step 2: Generate then-part
    102: x = 1
    103: goto _             ; next list = {103}

Step 3: Backpatch true list with 102
    100: if a < b goto 102

Step 4: Generate else-part
    104: x = 2

Step 5: Backpatch false list with 104
    101: goto 104

Step 6: Backpatch next list with 105
    103: goto 105

Final:
    100: if a < b goto 102
    101: goto 104
    102: x = 1
    103: goto 105
    104: x = 2
    105: ...
```

---

## 5.11 TAC for Array Access

### One-Dimensional Array
**Source:** `x = a[i]`

**Address Calculation:**
```
address(a[i]) = base(a) + i * width
```

**TAC:**
```
t1 = i * width
t2 = a[t1]      ; or t2 = a + t1; x = *t2
x = t2
```

### Two-Dimensional Array (Row-Major)
**Source:** `x = a[i][j]`

**Address Calculation:**
```
address(a[i][j]) = base(a) + (i * cols + j) * width
```

**TAC:**
```
t1 = i * cols
t2 = t1 + j
t3 = t2 * width
t4 = a[t3]
x = t4
```

### 🎯 GATE Formula: Array Address
```
Row-Major: base + ((i - low1) * n2 + (j - low2)) * width
Column-Major: base + ((j - low2) * n1 + (i - low1)) * width
```
Where n1, n2 are dimensions, low1, low2 are lower bounds.

---

## 5.12 TAC for Function Calls

### Calling Convention
**Source:**
```c
result = foo(a, b, c);
```

**TAC:**
```
param a
param b  
param c
result = call foo, 3
```

### Function Definition
**Source:**
```c
int add(int x, int y) {
    return x + y;
}
```

**TAC:**
```
add:
    t1 = x + y
    return t1
```

---

## 5.13 Counting Temporaries

### 🎯 GATE Favorite Question
**Q:** How many temporaries needed for expression?

### Method 1: Using Ershov Numbers (for Trees)
```
Label leaves with 1
For interior node n with children c1, c2:
    if label(c1) == label(c2):
        label(n) = label(c1) + 1
    else:
        label(n) = max(label(c1), label(c2))
```

### Example
```
Expression: a * b + c * d
Tree:
           +
          / \
         *   *
        /|   |\
       a b   c d

Labels:
         2        (max(1,1)+1 since equal)
        / \
       1   1      (max(1,1)+1 since equal)
      /|   |\
     1 1   1 1    (leaves)

Temporaries needed = 2
```

### Method 2: Trace TAC
```
t1 = a * b    ; t1 active
t2 = c * d    ; t1, t2 active (max = 2)
t3 = t1 + t2  ; t3 active (t1, t2 freed)

Max temporaries = 2
```

---

## 5.14 Static Single Assignment (SSA)

### Definition
**SSA** is an IR form where each variable is assigned exactly once.

### Conversion to SSA
```
Original:
    x = 1
    x = 2
    y = x

SSA:
    x1 = 1
    x2 = 2
    y = x2
```

### Φ (Phi) Function
Used at control flow merge points:
```
if (cond) 
    x = 1
else 
    x = 2
y = x

SSA:
if (cond)
    x1 = 1
else
    x2 = 2
x3 = φ(x1, x2)
y = x3
```

### Benefits
- Simplifies optimization
- Each definition has unique name
- Def-use chains are trivial

---

## 5.15 GATE Previous Year Patterns

### Pattern 1: Generate TAC
**Q:** Generate TAC for given expression/statement.
**Approach:** Apply rules systematically.

### Pattern 2: Count Temporaries
**Q:** Minimum temporaries for expression?
**Approach:** Use Ershov numbers or trace TAC.

### Pattern 3: DAG Construction
**Q:** Draw DAG, count nodes.
**Approach:** Identify common subexpressions.

### Pattern 4: Quadruples/Triples
**Q:** Represent TAC in quadruples/triples.
**Approach:** Convert each TAC instruction.

---

## 📝 Quick Revision Points

1. **IR Purpose:** Bridge between front-end and back-end
2. **TAC:** x = y op z (at most 3 addresses)
3. **Quadruple:** (op, arg1, arg2, result) - 4 fields
4. **Triple:** (op, arg1, arg2) - result is index
5. **Indirect Triple:** Pointers to triples (easy reorder)
6. **DAG:** Compact tree with shared nodes for CSE
7. **Backpatching:** Fill jump targets later
8. **Short-circuit:** Jump-based boolean evaluation
9. **Array access:** base + offset calculation
10. **Ershov Numbers:** Count minimum temporaries

---

## 🧠 Mnemonic Summary

### TAC Forms
> **"QTI: Quadruple has 4, Triple has 3, Indirect points"**

### DAG vs Tree
> **"DAG Shares, Tree Separates"**

### Boolean Methods
> **"Numerical Computes, Control Jumps"**

### Backpatching
> **"Generate now, Fill later"**

---

## 🔥 The Adversarial Vault

### Trap 1: Quadruple vs Triple Space
**Q:** Which saves space?
**A:** Triples save space (no result field), but harder to optimize.

### Trap 2: DAG Node Count
**Q:** Nodes in DAG for (a+a)+(a+a)?
**A:** Only 2 nodes! 'a' and '+' (the + is computed once and reused twice)

### Trap 3: Short-Circuit
**Q:** In `false && f()`, is f() called?
**A:** NO! Short-circuit skips when first operand determines result.

---

## ✅ Self-Assessment Questions

1. Generate TAC for `a = b + c * d`.
2. Represent TAC in quadruples and triples.
3. Construct DAG for `(a + b) * (a + b) + c`.
4. Generate TAC with backpatching for while loop.
5. Calculate temporaries using Ershov numbers.

---

**Next Chapter:** [Runtime Environment →](06-Runtime-Environment.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
