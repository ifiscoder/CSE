# Module 4: Semantic Analysis & Syntax-Directed Translation | The Singularity

> **The Atomic Truth:** *"Attach meaning to syntax through attributes."*

---

## 🎯 The Path of Elegance (Root Derivation)

### 4.1 Semantic Analysis Overview

```
[Image of Semantic Analysis Position]
    Lexical       Syntax        SEMANTIC       Code
    Analysis  →  Analysis  →   ANALYSIS   →  Generation
                     ↓             ↓
                Parse Tree   Annotated Tree
                              + Type Info
                              + Symbol Table
```

### Semantic Analysis Tasks

| Task | Description |
|------|-------------|
| **Type Checking** | Verify operand types match operators |
| **Scope Resolution** | Bind identifiers to declarations |
| **Flow Control** | Verify break/continue in loops |
| **Uniqueness** | No duplicate declarations |
| **Coercion** | Insert implicit type conversions |

---

## 📐 4.2 Attribute Grammars

### Syntax-Directed Definition (SDD)

**Components:**
1. **Context-Free Grammar**
2. **Attributes** for each grammar symbol
3. **Semantic Rules** for each production

**Example: Simple Calculator**
```
Production          Semantic Rule
──────────          ─────────────
L → E n            L.val = E.val
E → E₁ + T         E.val = E₁.val + T.val
E → T              E.val = T.val
T → T₁ * F         T.val = T₁.val × F.val
T → F              T.val = F.val
F → ( E )          F.val = E.val
F → digit          F.val = digit.lexval
```

### Attribute Types

| Type | Definition | Flow Direction |
|------|------------|----------------|
| **Synthesized** | Computed from children | Up the tree ↑ |
| **Inherited** | Computed from parent/siblings | Down the tree ↓ |

```
[Image of Attribute Flow]
         S (val = synthesized ↑)
        /|\
       / | \
      A  B  C
      ↓     ↓
    (inh)  (inh)
   inherited flows DOWN
```

### Example: Both Attribute Types

```
Production          Semantic Rules
──────────          ──────────────
D → T L            L.in = T.type
T → int            T.type = integer
T → float          T.type = float
L → L₁, id         L₁.in = L.in
                   addtype(id.entry, L.in)
L → id             addtype(id.entry, L.in)
```

Here:
- `T.type` is **synthesized** (computed from T's children)
- `L.in` is **inherited** (passed from parent D)

---

## ⚡ 4.3 S-Attributed and L-Attributed Grammars

### S-Attributed Definition

**Definition:** Uses ONLY synthesized attributes.

**Properties:**
- Can be evaluated bottom-up
- Single post-order traversal
- Compatible with LR parsing

### L-Attributed Definition

**Definition:** For production A → X₁X₂...Xₙ:
- Each inherited attribute of Xᵢ depends only on:
  - Inherited attributes of A
  - Attributes of X₁, X₂, ..., Xᵢ₋₁ (left siblings only)

**Properties:**
- Can be evaluated left-to-right, depth-first
- Single traversal (with care)
- S-attributed ⊂ L-attributed

### The Golden Pivot | Evaluation Order

```
[Attribute Flow Summary]
                S-Attributed          L-Attributed
                ────────────          ─────────────
                    ↑                    ↓ then ↑
                   / \                  / \
                  /   \                /   \
                 ↑     ↑              ↓     ↓→
                                    (left-to-right)
```

### ⚠️ What's NOT L-Attributed?

```
Production: A → BC
Rule: B.inh = C.syn    ← INVALID! B depends on RIGHT sibling C
```

---

## 📊 4.4 Syntax-Directed Translation Schemes (SDT)

### SDT Definition

Grammar with **semantic actions** embedded in production bodies.

```
Production with Actions:
E → E₁ + T  { print('+') }
```

### Action Placement

**For S-Attributed (LR parsing):**
- Actions at END of production only

**For L-Attributed (LL parsing):**
- Actions anywhere, evaluate left-to-right

### Converting SDD to SDT

**S-Attributed SDD:**
```
E → E₁ + T    E.val = E₁.val + T.val
```
**Becomes SDT:**
```
E → E₁ + T    { E.val = E₁.val + T.val }
```
(Action at end)

**L-Attributed with Inherited:**
```
D → T L      L.in = T.type
```
**Becomes SDT:**
```
D → T { L.in = T.type } L
```
(Action between T and L)

---

## 🔄 4.5 Bottom-Up Evaluation

### Implementing SDT in LR Parsing

**Challenge:** Actions must be at production end.

**Solution:** Marker non-terminals

**Original:**
```
A → B { action } C
```

**Transformed:**
```
A → B M C
M → ε { action }
```

### Stack-Based Evaluation

In LR parsing:
- Attributes stored on parsing stack
- Synthesized attributes computed on reduce
- Inherited require markers or re-structuring

---

## 📐 4.6 Type Checking

### Type Expressions

| Constructor | Meaning | Example |
|-------------|---------|---------|
| Basic types | int, float, bool, char | int |
| Array | array(size, type) | array(10, int) |
| Record | record{fields} | record{x:int, y:float} |
| Pointer | pointer(type) | pointer(int) |
| Function | type → type | int × int → int |

### Type System Rules

**Example Rules:**
```
E → E₁ + E₂
    if (E₁.type == int && E₂.type == int)
        E.type = int
    else if (E₁.type == float || E₂.type == float)
        E.type = float  // coercion
    else
        error

E → E₁[E₂]
    if (E₁.type == array(n, t) && E₂.type == int)
        E.type = t
    else
        error
```

### Type Equivalence

| Type | Structural | Name |
|------|------------|------|
| Definition | Same structure | Same name |
| array(10, int) vs array(10, int) | Equal | Depends |
| typedef int myint; myint vs int | Equal | Not equal |

---

## 🔧 4.7 Symbol Table Management

### Symbol Table Structure

```
[Image of Symbol Table]
┌─────────────────────────────────────────────┐
│              Symbol Table                   │
├───────┬──────┬───────┬─────────┬───────────┤
│ Name  │ Type │ Scope │ Offset  │ Other     │
├───────┼──────┼───────┼─────────┼───────────┤
│ x     │ int  │ 0     │ 0       │           │
│ y     │ float│ 0     │ 4       │           │
│ arr   │ [10] │ 0     │ 8       │ elem: int │
│ foo   │ func │ 0     │ -       │ params... │
└───────┴──────┴───────┴─────────┴───────────┘
```

### Scope Implementation

**Stack of Hash Tables:**
```
Enter scope:  push new table
Exit scope:   pop table
Lookup:       search from top to bottom
Insert:       always in top table
```

### Symbol Table Operations

| Operation | Time (Hash) | Action |
|-----------|-------------|--------|
| insert | O(1) avg | Add new entry |
| lookup | O(1) avg | Search all scopes |
| enterScope | O(1) | Push new table |
| exitScope | O(n) | Pop and clean |

---

## 🎭 The Bizarre Mnemonic | "The Attribute Assembly Line"

*"Attributes flow through the parse tree like a FACTORY ASSEMBLY LINE:
- **Synthesized** = Products moving UP the conveyor to the final assembly point
- **Inherited** = Instructions passed DOWN from management
- **S-Attributed** = Simple factory: only products move up
- **L-Attributed** = Complex factory: instructions can flow down, but only to workers on your LEFT (already seen)"*

---

## 🏆 The 2026 Adversarial Vault

### Trap 1: The S vs L-Attributed Confusion
**Question Pattern:** "Is this grammar S-attributed or L-attributed?"
**Anti-Solution:** Students confuse the definitions.
**Truth:**
- S-attributed: ONLY synthesized attributes
- L-attributed: Inherited can depend on LEFT siblings only

### Trap 2: The Right Sibling Dependency
**Question Pattern:** "Is B.inh = f(C.syn) L-attributed in A → BC?"
**Anti-Solution:** Students say yes.
**Truth:** NO! B depends on C (RIGHT sibling). NOT L-attributed.

### Trap 3: The SDT Action Placement
**Question Pattern:** "Where to place action for inherited attribute in SDT?"
**Anti-Solution:** Students place at end.
**Truth:** BEFORE the symbol that uses the inherited attribute.

### Trap 4: The Type Coercion Direction
**Question Pattern:** "int + float = ?"
**Anti-Solution:** Students forget coercion rules.
**Truth:** int is coerced to float, result is float.

### NAT Precision Lock
- Attribute computation: Follow rules exactly
- Type sizes: int=4, float=4, double=8 (typically)

### MSQ Logic Gate | Elimination Rules
1. S-attributed → Only synthesized
2. L-attributed → No right sibling dependencies
3. Inherited → Passed down or from left
4. Synthesized → Computed from children

---

## 📊 GATE PYQ Pattern Analysis

| Year | Topic | Marks | Trap Type |
|------|-------|-------|-----------|
| 2023 | S vs L-attributed | 2 | Definition confusion |
| 2022 | SDT Action Placement | 2 | Inherited handling |
| 2021 | Attribute Dependencies | 2 | Dependency graph |
| 2020 | Type Checking | 1 | Coercion rules |

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| Synthesized | Depends on children only |
| Inherited | Depends on parent/left siblings |
| S-attributed | All attributes synthesized |
| L-attributed | No right sibling dependency |

---

## 🧮 Solved Examples

### Example 1: Identify Attribute Types
**SDD:**
```
S → AB     A.in = S.inh; B.in = A.syn
A → a      A.syn = f(A.in)
B → b      B.syn = g(B.in)
```

**Analysis:**
- S.inh: inherited (comes from outside)
- A.in: inherited (from parent S)
- A.syn: synthesized (from A's own attribute)
- B.in: inherited (from sibling A)
- B.syn: synthesized (from B's own attribute)

**Is it L-attributed?**
B.in depends on A.syn (LEFT sibling) ✓
Yes, it is L-attributed.

### Example 2: SDT Conversion
**Given SDD:**
```
D → T L     L.in = T.type
L → id      addtype(id.entry, L.in)
```

**Convert to SDT:**
```
D → T { L.in = T.type } L
L → id { addtype(id.entry, L.in) }
```

### Example 3: Evaluation Order
**Grammar:**
```
S → ABC
A.s = 1
B.i = A.s
B.s = B.i + 1
C.i = B.s
```

**Evaluation:**
1. A.s = 1 (synthesized from A)
2. B.i = A.s = 1 (inherited)
3. B.s = B.i + 1 = 2 (synthesized)
4. C.i = B.s = 2 (inherited)

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Would you like to initiate a **'Multi-Variable Stress Test'** combining SDT with Intermediate Code Generation for a Rank-1 simulation?*

---
[← Previous: Bottom-Up Parsing](./03-Syntax-Analysis-BottomUp.md) | [Back to Index](./README.md) | [Next: Intermediate Code Generation →](./05-Intermediate-Code-Generation.md)
