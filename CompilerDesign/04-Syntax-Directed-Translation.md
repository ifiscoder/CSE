# Chapter 4: Syntax Directed Translation (SDT)

## 🎯 The Atomic Truth
> **"SDT = Grammar + Semantic Rules"**

---

## 4.1 What is Syntax Directed Translation?

### Definition
**Syntax Directed Translation (SDT)** is a method of attaching semantic rules to grammar productions, allowing the compiler to compute values and generate code alongside parsing.

```
┌────────────────────────────────────────────────────────────────────────┐
│                    SYNTAX DIRECTED TRANSLATION                         │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   ┌─────────────┐      ┌─────────────────┐      ┌─────────────────┐   │
│   │   Parse     │      │  Semantic Rules │      │   Translation   │   │
│   │   Tree      │  +   │  (Attributes)   │  =   │   (Annotated    │   │
│   │             │      │                 │      │    Parse Tree)  │   │
│   └─────────────┘      └─────────────────┘      └─────────────────┘   │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 🧠 Analogy: The Calculator Parse Tree
When you parse "3 + 5 * 2":
- **Parse tree:** Shows structure
- **SDT:** Computes value (3 + 10 = 13) alongside parsing

---

## 4.2 Attributes

### Definition
**Attributes** are values associated with grammar symbols that carry semantic information.

### Types of Attributes

| Type | Direction | Computed From | Notation |
|------|-----------|---------------|----------|
| **Synthesized** | ↑ Bottom-up | Children | S-attribute |
| **Inherited** | ↓ Top-down | Parent/Siblings | I-attribute |

### Visual Representation
```
           E (synthesized = 13)
          /|\
         / | \
        E  +  T (synthesized = 10)
        |    /|\
        3   / | \
           T  *  F
           |     |
           5     2
```

---

## 4.3 Syntax Directed Definition (SDD)

### Definition
An **SDD** is a CFG with semantic rules attached to productions. Rules define how to compute attribute values.

### Example: Calculator SDD
```
Production          Semantic Rule
─────────────────────────────────────────
L → E n            L.val = E.val
E → E₁ + T         E.val = E₁.val + T.val
E → T              E.val = T.val
T → T₁ * F         T.val = T₁.val * F.val
T → F              T.val = F.val
F → (E)            F.val = E.val
F → digit          F.val = digit.lexval
```

### Annotated Parse Tree for "3 + 5 * 2"
```
             L.val = 13
             │
             E.val = 13
            /│\
           / │ \
    E.val=3  +  T.val = 10
      │         /│\
    T.val=3    / │ \
      │       T  *  F.val=2
    F.val=3   │      │
      │       5      2
      3    T.val=5
           │
         F.val=5
           │
           5
```

---

## 4.4 S-Attributed Definitions

### Definition
An SDD is **S-attributed** if it uses **only synthesized attributes**.

### Properties
1. Attributes computed bottom-up
2. Can be evaluated during LR parsing
3. No inherited attributes

### Example
```
Production          Semantic Rule
─────────────────────────────────────────
E → E₁ + T         { E.val = E₁.val + T.val }
E → T              { E.val = T.val }
T → T₁ * F         { T.val = T₁.val * F.val }
T → F              { T.val = F.val }
F → (E)            { F.val = E.val }
F → digit          { F.val = digit.lexval }
```

### Implementation with LR Parser
```
Use parser stack to hold attribute values:

Stack: $ E + T      (E.val=3, T.val=10)
Action: Reduce E → E + T
New Stack: $ E      (E.val=13)
```

---

## 4.5 L-Attributed Definitions

### Definition
An SDD is **L-attributed** if each inherited attribute depends only on:
1. Inherited attributes of parent
2. Attributes of left siblings
3. Synthesized attributes of left siblings

### Key Rule
Information flows **left-to-right** (hence "L"-attributed).

### Example: Type Declaration
```
Production              Semantic Rules
─────────────────────────────────────────────────────
D → T L                 L.in = T.type
T → int                 T.type = integer
T → float               T.type = float
L → L₁, id              L₁.in = L.in
                        addtype(id.entry, L.in)
L → id                  addtype(id.entry, L.in)
```

### Annotated Parse Tree for "int a, b, c"
```
                D
               / \
              /   \
         T.type   L.in = integer
           =        /\
        integer    /  \
           │      L.in  id (c)
          int       =   ↑
                integer addtype(c, int)
                   /\
                  /  \
             L.in    id (b)
               =     ↑
            integer addtype(b, int)
               │
              id (a)
               ↑
            addtype(a, int)
```

---

## 4.6 S-Attributed vs L-Attributed

### Comparison

| Feature | S-Attributed | L-Attributed |
|---------|--------------|--------------|
| Attributes | Synthesized only | Synthesized + Left-flowing inherited |
| Direction | Bottom-up only | Left-to-right, bottom-up |
| Evaluation | Single bottom-up pass | Depth-first, left-to-right |
| Parser | LR parser | LL parser or modified LR |
| Power | Less powerful | More powerful |

### 🎯 GATE Critical Insight
```
S-attributed ⊂ L-attributed
```
Every S-attributed SDD is also L-attributed!

---

## 4.7 Syntax Directed Translation Schemes

### Definition
An **SDT Scheme** is an SDD with semantic actions embedded at specific positions within production bodies.

### Notation
```
A → { action1 } B { action2 } C { action3 }
```
Actions are enclosed in braces {}.

### Example: Postfix Translation
```
E → T R
R → + T { print('+') } R | ε
T → num { print(num.value) }
```

**Input:** "9 - 5 + 2"
**Output:** "9 5 - 2 +"

### Placement Rules

#### For S-attributed SDT (with LR parser)
- Actions at **end of production** only
```
A → B C D { semantic action }
```

#### For L-attributed SDT (with LL parser)
- Actions can be **anywhere** in production
- But must respect dependency order
```
A → { inherited setup } B { action } C { final action }
```

---

## 4.8 Dependency Graphs

### Definition
A **dependency graph** shows the order in which attributes must be computed based on semantic rules.

### Construction
1. Create node for each attribute
2. Draw edge from X.a to Y.b if computing Y.b requires X.a

### Example
```
Production: E → E₁ + T
Rule: E.val = E₁.val + T.val

Dependency Graph:
    E₁.val ──┐
             ├───► E.val
    T.val  ──┘
```

### Evaluation Order
1. Topological sort of dependency graph
2. Process attributes in this order

### 🎯 GATE Trap
**Q:** Can dependency graph have cycles?
**A:** NO! Cycles mean attributes can't be computed. SDD would be **ill-defined**.

---

## 4.9 Evaluation Methods

### 1. Parse-Tree Methods
Build full parse tree, then evaluate attributes.

### 2. Rule-Based Methods
Analyze rules at compiler-construction time, pre-compute evaluation order.

### 3. Oblivious Methods
Fixed evaluation strategy regardless of rules.

#### Bottom-Up for S-attributed
```
- Evaluate during reduce
- Store values on parser stack
```

#### Left-to-Right for L-attributed
```
- Use recursive descent with inherited parameters
- Return synthesized values
```

---

## 4.10 Implementing S-attributed SDDs

### Using LR Parser Stack
```
Parser Stack:    State   Value
                 ─────   ─────
                   s₃     F.val=3
                   s₂     ─
                   s₁     ─
                   $      ─

When reducing T → F:
- Pop: F.val = 3
- Compute: T.val = F.val = 3
- Push: T.val = 3
```

### Example: Desk Calculator
```c
%{
int val;
%}

%%
lines   : lines expr '\n'  { printf("%d\n", $2); }
        | /* empty */
        ;

expr    : expr '+' term    { $$ = $1 + $3; }
        | term             { $$ = $1; }
        ;

term    : term '*' factor  { $$ = $1 * $3; }
        | factor           { $$ = $1; }
        ;

factor  : '(' expr ')'     { $$ = $2; }
        | DIGIT            { $$ = $1; }
        ;
%%
```

### $$ Notation in YACC
- `$$` = LHS attribute value
- `$1, $2, $3, ...` = RHS symbol values (left to right)

---

## 4.11 Implementing L-attributed SDDs

### Method 1: Recursive Descent
```c
// D → T L
void D() {
    int t = T();        // T.type (synthesized)
    L(t);               // L.in (inherited)
}

// L → L₁ , id | id
void L(int in) {
    if (lookahead == ID) {
        addtype(currentId, in);
        match(ID);
        if (lookahead == COMMA) {
            match(COMMA);
            L(in);      // Pass inherited attribute
        }
    }
}
```

### Method 2: Markers in LR Parsing
Insert marker non-terminals to trigger actions.

```
Original: A → X { Y.i = f(X.s) } Y
With marker: A → X M Y
             M → ε { M.i = f(stack[top-1].s) }
```

---

## 4.12 Type Checking (Application of SDT)

### Type Expressions
```
T → char           { T.type = char }
T → int            { T.type = int }
T → T₁ [ num ]     { T.type = array(num.val, T₁.type) }
T → ↑ T₁           { T.type = pointer(T₁.type) }
T → T₁ → T₂        { T.type = function(T₁.type, T₂.type) }
```

### Type Checking Rules
```
E → E₁ + E₂        
    if E₁.type == int AND E₂.type == int then
        E.type = int
    else if E₁.type == float OR E₂.type == float then
        E.type = float
    else
        E.type = error

E → E₁[E₂]
    if E₁.type == array(s, t) AND E₂.type == int then
        E.type = t
    else
        E.type = error
```

### Type Coercion
```
int → float (widening, allowed)
float → int (narrowing, may lose precision)
```

---

## 4.13 Symbol Table Management (Application of SDT)

### Symbol Table Operations in SDT
```
Production              Semantic Action
─────────────────────────────────────────────────────
P → D ; S              { }
D → D₁ ; D₂            { }
D → id : T             { addtype(id.entry, T.type) }
S → id := E            { if lookup(id.entry) ≠ E.type
                           then type_error() }
```

### Scope Management
```
P → { createTable() } D ; S { deleteTable() }
```

---

## 4.14 Common SDT Patterns for GATE

### Pattern 1: Expression Evaluation
```
E → E₁ op E₂   { E.val = E₁.val op E₂.val }
E → num        { E.val = num.lexval }
```

### Pattern 2: Type Synthesis
```
E → E₁ + E₂    { E.type = max(E₁.type, E₂.type) }
```

### Pattern 3: Code Generation
```
E → E₁ + E₂    { E.place = newtemp()
                 emit(E.place '=' E₁.place '+' E₂.place) }
```

### Pattern 4: String Concatenation
```
E → E₁ || E₂   { E.code = E₁.code || E₂.code }
```

---

## 4.15 Solved Examples

### Example 1: Count Operators
**Problem:** Design SDD to count operators in expression.

```
Production              Semantic Rule
─────────────────────────────────────────────────────
E → E₁ + T             E.count = E₁.count + T.count + 1
E → T                  E.count = T.count
T → T₁ * F             T.count = T₁.count + F.count + 1
T → F                  T.count = F.count
F → (E)                F.count = E.count
F → id                 F.count = 0
```

### Example 2: Binary to Decimal
**Problem:** Convert binary string to decimal.

```
Production              Semantic Rule
─────────────────────────────────────────────────────
S → L                  S.val = L.val
L → L₁ B               L.val = L₁.val * 2 + B.val
L → B                  L.val = B.val
B → 0                  B.val = 0
B → 1                  B.val = 1
```

**For "1101":** val = ((1*2+1)*2+0)*2+1 = 13

### Example 3: Infix to Postfix
**Problem:** Translate infix to postfix using SDT.

```
Production              Semantic Action
─────────────────────────────────────────────────────
E → T R                { }
R → + T                { print('+') } R₁ | ε
T → num                { print(num.lexval) }
```

---

## 4.16 GATE Previous Year Patterns

### Pattern 1: Identify Attribute Type
**Q:** In rule "A.s = f(B.i)", is A.s synthesized or inherited?
**A:** Synthesized (defined for LHS symbol)

### Pattern 2: Check S-attributed/L-attributed
**Q:** Given SDD, is it S-attributed? L-attributed?
**Approach:**
1. S-attributed: Only synthesized attributes?
2. L-attributed: Inherited depends only on left/parent?

### Pattern 3: Compute Attribute Values
**Q:** Compute attribute value for given string.
**Approach:** Build annotated parse tree bottom-up.

### Pattern 4: Count Temporaries
**Q:** How many temporaries for expression?
**A:** Count intermediate results needed.

---

## 📝 Quick Revision Points

1. **SDT:** Grammar + Semantic Rules
2. **Synthesized:** Computed from children (↑)
3. **Inherited:** Computed from parent/siblings (↓)
4. **S-attributed:** Synthesized only, bottom-up
5. **L-attributed:** Left-to-right flow, more general
6. **S-attributed ⊂ L-attributed**
7. **Dependency Graph:** Shows computation order
8. **$$ in YACC:** LHS value, $1,$2 for RHS
9. **No cycles** allowed in dependency graphs
10. **Markers:** Enable inherited attrs in LR parsing

---

## 🧠 Mnemonic Summary

### S vs L Attributed
> **"S goes Up (Synthesized, bottom-Up)"**
> **"L goes Left (Left-to-right flow)"**

### Attribute Direction
> **"Children SYNTHESIZE value for parent"**
> **"Parent INHERITS value to children"**

### SDT Scheme Placement
> **"S at END, L ANYWHERE (respecting order)"**

---

## 🔥 The Adversarial Vault

### Trap 1: Attribute Type
**Q:** A → B { A.s = B.s } — Is A.s synthesized?
**A:** YES! A.s is on LHS and defined by rule.

### Trap 2: L-attributed Check
**Q:** A → B C where C.i = f(A.i, B.s, C.s)?
**A:** NOT L-attributed! C.i cannot depend on C.s (its own synthesized attribute).

### Trap 3: S-attributed in LL
**Q:** Can S-attributed SDD be evaluated with LL parser?
**A:** YES! S-attributed ⊂ L-attributed, and L-attributed works with LL.

---

## ✅ Self-Assessment Questions

1. Differentiate between synthesized and inherited attributes.
2. Design SDD for computing length of a string.
3. Check if given SDD is S-attributed or L-attributed.
4. Draw dependency graph for expression evaluation.
5. Write YACC-style actions for infix to postfix.

---

**Next Chapter:** [Intermediate Code Generation →](05-Intermediate-Code-Generation.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
