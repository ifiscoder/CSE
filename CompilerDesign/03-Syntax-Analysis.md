# Chapter 3: Syntax Analysis (Parsing)

## 🎯 The Atomic Truth
> **"Parser = Token Stream → Parse Tree"**

---

## 3.1 What is Syntax Analysis?

### Definition
**Syntax Analysis** (Parsing) is the second phase of a compiler that takes the token stream from the lexical analyzer and checks if it conforms to the grammatical rules of the language, producing a **Parse Tree** or **Syntax Tree**.

```
┌────────────────────────────────────────────────────────────────────────┐
│                          SYNTAX ANALYZER                               │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   ┌─────────────┐                              ┌─────────────────┐    │
│   │   Token     │                              │   Parse Tree    │    │
│   │   Stream    │ ─────────────────────────►   │  (Derivation)   │    │
│   │ from Lexer  │          PARSER              │                 │    │
│   └─────────────┘                              └─────────────────┘    │
│          │                                              │             │
│          │         ┌─────────────────────┐              │             │
│          └────────►│  Grammar Rules (CFG) │◄────────────┘             │
│                    │                     │                            │
│                    └─────────────────────┘                            │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 🧠 Analogy: The Grammar Police
Parser is like a grammar teacher checking your sentence:
- **Input:** "The cat sat mat on" (tokens)
- **Grammar rules:** Subject + Verb + Preposition + Object
- **Output:** ❌ "Syntax error! Expected preposition before object"

---

## 3.2 Context-Free Grammar (CFG)

### Definition
A **Context-Free Grammar** G is a 4-tuple: **G = (V, T, P, S)**

| Component | Symbol | Description | Example |
|-----------|--------|-------------|---------|
| **Variables** | V | Non-terminal symbols | {E, T, F} |
| **Terminals** | T | Token types from lexer | {id, +, *, (, )} |
| **Productions** | P | Grammar rules | E → E + T |
| **Start Symbol** | S | Initial variable | E |

### Example Grammar for Arithmetic Expressions
```
E → E + T | T
T → T * F | F
F → (E) | id
```

### Notation
- **Non-terminals:** Uppercase letters (E, T, F, A, B)
- **Terminals:** Lowercase letters, digits, symbols (a, b, id, +)
- **Production:** A → α (A produces α)
- **|** : "or" (alternative productions)

---

## 3.3 Derivations

### Definition
A **derivation** is a sequence of production rule applications starting from the start symbol and ending at a string of terminals.

### Types of Derivation

| Type | Symbol | Description |
|------|--------|-------------|
| **Leftmost** | ⇒_lm | Always expand leftmost non-terminal first |
| **Rightmost** | ⇒_rm | Always expand rightmost non-terminal first |

### Example
**Grammar:**
```
E → E + E | E * E | id
```

**Derive:** `id + id * id`

**Leftmost Derivation:**
```
E ⇒ E + E
  ⇒ id + E
  ⇒ id + E * E
  ⇒ id + id * E
  ⇒ id + id * id
```

**Rightmost Derivation:**
```
E ⇒ E + E
  ⇒ E + E * E
  ⇒ E + E * id
  ⇒ E + id * id
  ⇒ id + id * id
```

---

## 3.4 Parse Trees

### Definition
A **Parse Tree** is a graphical representation of a derivation.

### Properties
1. **Root:** Start symbol
2. **Interior nodes:** Non-terminals
3. **Leaves:** Terminals (yield/frontier = input string)
4. **Children:** Represent RHS of production

### Example Parse Tree for `id + id * id`
```
            E
          / | \
         E  +  E
         |    / | \
        id   E  *  E
             |     |
            id    id
```

### 🎯 GATE Critical Insight
**Parse tree shows derivation structure, NOT operator precedence!**
Same string can have multiple parse trees in ambiguous grammar.

---

## 3.5 Ambiguity

### Definition
A grammar is **ambiguous** if there exists a string that has:
- More than one **leftmost derivation**, OR
- More than one **rightmost derivation**, OR
- More than one **parse tree**

### Example of Ambiguous Grammar
```
E → E + E | E * E | id
```

**String:** `id + id * id`

**Parse Tree 1:** (+ has higher precedence)
```
            E
          / | \
         E  *  E
       / | \   |
      E  +  E  id
      |     |
     id    id
```

**Parse Tree 2:** (* has higher precedence)
```
            E
          / | \
         E  +  E
         |   / | \
        id  E  *  E
            |     |
           id    id
```

### 🔥 The Genius Trap
**Q:** Is the grammar ambiguous: E → E + E | id?
**A:** YES! String `id + id + id` has two parse trees:
- ((id + id) + id) - left associative
- (id + (id + id)) - right associative

### Eliminating Ambiguity

#### Technique 1: Operator Precedence (Layer the grammar)
**Ambiguous:**
```
E → E + E | E * E | id
```

**Unambiguous:**
```
E → E + T | T
T → T * F | F
F → id
```
This makes * bind tighter than +.

#### Technique 2: Associativity
**Left-associative:** E → E + T (left recursion)
**Right-associative:** E → T + E (right recursion)

### 🎯 GATE Formula: Checking Ambiguity
1. Find a string with **multiple parse trees**
2. Or find a string with **multiple leftmost derivations**
3. If found → Grammar is **ambiguous**

---

## 3.6 Left Recursion and Its Elimination

### Definition
A grammar is **left-recursive** if there exists a non-terminal A such that:
$$A \Rightarrow^+ A\alpha$$

#### Immediate Left Recursion
```
A → Aα | β
```

#### Indirect Left Recursion
```
A → Bα
B → Aβ
```

### Why Eliminate?
**Top-down parsers (LL parsers) cannot handle left recursion!**
They go into infinite loops.

### Algorithm to Eliminate Immediate Left Recursion
**Original:**
```
A → Aα₁ | Aα₂ | ... | Aαₘ | β₁ | β₂ | ... | βₙ
```

**Transformed:**
```
A  → β₁A' | β₂A' | ... | βₙA'
A' → α₁A' | α₂A' | ... | αₘA' | ε
```

### Example
**Original:**
```
E → E + T | T
```

**After elimination:**
```
E  → TE'
E' → +TE' | ε
```

### 🎯 Memory Trick
> **"Move the left recursion to the RIGHT with a new prime symbol"**

### General Algorithm for All Left Recursion
1. Order non-terminals: A₁, A₂, ..., Aₙ
2. For i = 1 to n:
   - For j = 1 to i-1:
     - Replace Aᵢ → Aⱼγ with Aᵢ → δ₁γ | δ₂γ | ... where Aⱼ → δ₁ | δ₂ | ...
   - Eliminate immediate left recursion from Aᵢ

---

## 3.7 Left Factoring

### Definition
**Left Factoring** is a grammar transformation that extracts common prefixes to help with parsing.

### When Needed?
When two productions for the same non-terminal start with the same symbol(s).

### Algorithm
**Original:**
```
A → αβ₁ | αβ₂
```

**After left factoring:**
```
A  → αA'
A' → β₁ | β₂
```

### Example
**Original:**
```
S → if E then S else S
S → if E then S
```

**After left factoring:**
```
S  → if E then S S'
S' → else S | ε
```

### 🎯 The Dangling Else Problem
This is the classic ambiguity with if-then-else statements.
Left factoring doesn't remove ambiguity but helps parsers decide.

---

## 3.8 Types of Parsers

### The Grand Classification

```
                        PARSERS
                           │
           ┌───────────────┴───────────────┐
           │                               │
      TOP-DOWN                        BOTTOM-UP
    (Start → Input)                 (Input → Start)
           │                               │
    ┌──────┴──────┐              ┌─────────┴─────────┐
    │             │              │                   │
Recursive    Predictive      Operator         LR Parsers
 Descent      (LL(1))       Precedence      (Shift-Reduce)
                                             │
                                     ┌───────┼───────┐
                                     │       │       │
                                   SLR    CLR(1)   LALR
                                  (LR(0))  (LR(1))
```

---

## 3.9 Top-Down Parsing

### Concept
Build parse tree from **root (start symbol) to leaves (input)**.
Uses **leftmost derivation**.

### 3.9.1 Recursive Descent Parser

#### Definition
A **recursive descent parser** uses a set of recursive procedures, one for each non-terminal.

#### Structure
```c
void A() {
    // For each production A → X₁X₂...Xₖ
    // Try to match X₁, X₂, ..., Xₖ
    if (X₁ is terminal) {
        match(X₁);
    } else {
        call X₁();
    }
    // ... repeat for X₂, X₃, etc.
}
```

#### Example
**Grammar:**
```
S → aB
B → bB | c
```

**Parser:**
```c
void S() {
    match('a');
    B();
}

void B() {
    if (lookahead == 'b') {
        match('b');
        B();
    } else if (lookahead == 'c') {
        match('c');
    } else {
        error();
    }
}
```

### 3.9.2 LL(1) Parsing

#### Definition
**LL(1)** means:
- **L:** Left-to-right scanning
- **L:** Leftmost derivation
- **(1):** 1 symbol lookahead

#### Requirements for LL(1) Grammar
1. No left recursion
2. Grammar is left-factored
3. For each pair of productions A → α | β:
   - FIRST(α) ∩ FIRST(β) = ∅
   - If ε ∈ FIRST(α), then FIRST(β) ∩ FOLLOW(A) = ∅

---

## 3.10 FIRST and FOLLOW (CRITICAL FOR GATE!)

### 3.10.1 FIRST Set

#### Definition
**FIRST(α)** = Set of terminals that begin strings derived from α.
If α ⇒* ε, then ε ∈ FIRST(α).

#### Rules for Computing FIRST(X)

1. **If X is terminal:** FIRST(X) = {X}

2. **If X is non-terminal with productions X → Y₁Y₂...Yₖ:**
   - Add FIRST(Y₁) - {ε} to FIRST(X)
   - If ε ∈ FIRST(Y₁), add FIRST(Y₂) - {ε}
   - If ε ∈ FIRST(Y₁) and ε ∈ FIRST(Y₂), add FIRST(Y₃) - {ε}
   - Continue until Yᵢ doesn't have ε
   - If all Y₁...Yₖ have ε, add ε to FIRST(X)

3. **If X → ε:** Add ε to FIRST(X)

#### Example
```
E  → TE'
E' → +TE' | ε
T  → FT'
T' → *FT' | ε
F  → (E) | id
```

**FIRST Sets:**
```
FIRST(F)  = { (, id }
FIRST(T') = { *, ε }
FIRST(T)  = { (, id }
FIRST(E') = { +, ε }
FIRST(E)  = { (, id }
```

### 3.10.2 FOLLOW Set

#### Definition
**FOLLOW(A)** = Set of terminals that can appear immediately to the **right** of A in some sentential form.

#### Rules for Computing FOLLOW(A)

1. **FOLLOW(S) contains $** (end marker for start symbol)

2. **If A → αBβ:**
   - Add FIRST(β) - {ε} to FOLLOW(B)

3. **If A → αB or A → αBβ where ε ∈ FIRST(β):**
   - Add FOLLOW(A) to FOLLOW(B)

#### Example (Continued)
```
E  → TE'
E' → +TE' | ε
T  → FT'
T' → *FT' | ε
F  → (E) | id
```

**FOLLOW Sets:**
```
FOLLOW(E)  = { $, ) }        [S = E, and F → (E)]
FOLLOW(E') = { $, ) }        [E → TE', so FOLLOW(E') = FOLLOW(E)]
FOLLOW(T)  = { +, $, ) }     [E' → +T E', and E → TE']
FOLLOW(T') = { +, $, ) }     [T → FT', so FOLLOW(T') = FOLLOW(T)]
FOLLOW(F)  = { *, +, $, ) }  [T' → *F T', and T → FT']
```

### 🎯 GATE Master Formula for FIRST/FOLLOW

#### FIRST Quick Rules:
```
FIRST(terminal) = {terminal}
FIRST(ε) = {ε}
FIRST(Aα) = FIRST(A) if ε ∉ FIRST(A)
          = (FIRST(A) - {ε}) ∪ FIRST(α) if ε ∈ FIRST(A)
```

#### FOLLOW Quick Rules:
```
1. $ ∈ FOLLOW(Start)
2. A → αBβ: FIRST(β) - {ε} ⊆ FOLLOW(B)
3. A → αB or β ⇒* ε: FOLLOW(A) ⊆ FOLLOW(B)
```

---

## 3.11 LL(1) Parsing Table Construction

### Algorithm
For each production A → α:
1. For each terminal a ∈ FIRST(α), add A → α to M[A, a]
2. If ε ∈ FIRST(α):
   - For each terminal b ∈ FOLLOW(A), add A → α to M[A, b]
   - If $ ∈ FOLLOW(A), add A → α to M[A, $]

### Example LL(1) Parsing Table
```
E  → TE'          E' → +TE' | ε          T  → FT'
T' → *FT' | ε     F  → (E) | id
```

|    | id | + | * | ( | ) | $ |
|----|----|----|----|----|----|----|
| E  | E→TE' | | | E→TE' | | |
| E' | | E'→+TE' | | | E'→ε | E'→ε |
| T  | T→FT' | | | T→FT' | | |
| T' | | T'→ε | T'→*FT' | | T'→ε | T'→ε |
| F  | F→id | | | F→(E) | | |

### LL(1) Parsing Algorithm
```
Stack: $ E (start with end marker and start symbol)
Input: id + id * id $

while stack not empty:
    X = top of stack
    a = current input symbol
    
    if X == a:
        pop stack
        advance input
    else if X is terminal:
        error
    else if M[X, a] is empty:
        error
    else if M[X, a] = X → Y₁Y₂...Yₖ:
        pop X
        push Yₖ...Y₂Y₁ (reverse order!)
```

---

## 3.12 Bottom-Up Parsing

### Concept
Build parse tree from **leaves (input) to root (start symbol)**.
Uses **rightmost derivation in reverse**.

### Key Idea: Handle
A **handle** is a substring that matches the RHS of a production and can be reduced.

### Shift-Reduce Parsing
Two main operations:
1. **Shift:** Push next input symbol onto stack
2. **Reduce:** Replace handle on stack with LHS of production

### Example
**Grammar:** E → E + T | T, T → id

**Parse:** `id + id`
```
Stack         Input          Action
$             id + id $      Shift
$ id          + id $         Reduce T → id
$ T           + id $         Reduce E → T
$ E           + id $         Shift
$ E +         id $           Shift
$ E + id      $              Reduce T → id
$ E + T       $              Reduce E → E + T
$ E           $              Accept
```

---

## 3.13 LR Parsing (The Most Powerful!)

### Definition
**LR(k)** means:
- **L:** Left-to-right scanning
- **R:** Rightmost derivation (in reverse)
- **(k):** k symbols lookahead

### LR Parser Variants

| Parser | Lookahead | Table Size | Power |
|--------|-----------|------------|-------|
| SLR(1) | 1 | Small | Weakest |
| LALR(1) | 1 | Medium | Middle |
| CLR(1) | 1 | Large | Strongest |

### LR(0) Items
An **LR(0) item** is a production with a **dot** (•) at some position in the RHS.

For production A → XYZ:
- A → •XYZ (initial)
- A → X•YZ (after X)
- A → XY•Z (after XY)
- A → XYZ• (complete)

### Augmented Grammar
Add new start symbol S' → S to handle acceptance.

**Original:** E → E + T | T
**Augmented:** E' → E, E → E + T | T

---

## 3.14 SLR(1) Parsing

### Algorithm for SLR(1) Table Construction

**Step 1:** Construct canonical collection of LR(0) items

**Closure Operation:**
```
closure(I):
    repeat
        for each item A → α•Bβ in I:
            for each production B → γ:
                add B → •γ to I
    until no more items can be added
    return I
```

**Goto Operation:**
```
goto(I, X):
    J = empty set
    for each item A → α•Xβ in I:
        add A → αX•β to J
    return closure(J)
```

**Step 2:** Construct canonical collection C = {I₀, I₁, ..., Iₙ}
1. I₀ = closure({S' → •S})
2. For each Iᵢ and symbol X:
   - If goto(Iᵢ, X) is not empty and not in C, add to C

**Step 3:** Construct parsing table
- **Shift:** If A → α•aβ in Iᵢ and goto(Iᵢ, a) = Iⱼ, then ACTION[i, a] = Shift j
- **Reduce:** If A → α• in Iᵢ, then for all a ∈ FOLLOW(A), ACTION[i, a] = Reduce A → α
- **Accept:** If S' → S• in Iᵢ, then ACTION[i, $] = Accept
- **Goto:** If goto(Iᵢ, A) = Iⱼ for non-terminal A, then GOTO[i, A] = j

### SLR Parsing Example
**Grammar:**
```
1. E' → E
2. E → E + T
3. E → T
4. T → T * F
5. T → F
6. F → (E)
7. F → id
```

**Item Sets:**
```
I₀: E' → •E
    E → •E + T
    E → •T
    T → •T * F
    T → •F
    F → •(E)
    F → •id

I₁: E' → E•
    E → E• + T

I₂: E → T•
    T → T• * F

I₃: T → F•

I₄: F → (•E)
    E → •E + T
    E → •T
    T → •T * F
    T → •F
    F → •(E)
    F → •id

I₅: F → id•

I₆: E → E +• T
    T → •T * F
    T → •F
    F → •(E)
    F → •id

I₇: T → T *• F
    F → •(E)
    F → •id

I₈: F → (E•)
    E → E• + T

I₉: E → E + T•
    T → T• * F

I₁₀: T → T * F•

I₁₁: F → (E)•
```

**SLR Parsing Table:**

| State | id | + | * | ( | ) | $ | E | T | F |
|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 0 | s5 | | | s4 | | | 1 | 2 | 3 |
| 1 | | s6 | | | | acc | | | |
| 2 | | r3 | s7 | | r3 | r3 | | | |
| 3 | | r5 | r5 | | r5 | r5 | | | |
| 4 | s5 | | | s4 | | | 8 | 2 | 3 |
| 5 | | r7 | r7 | | r7 | r7 | | | |
| 6 | s5 | | | s4 | | | | 9 | 3 |
| 7 | s5 | | | s4 | | | | | 10 |
| 8 | | s6 | | | s11 | | | | |
| 9 | | r2 | s7 | | r2 | r2 | | | |
| 10 | | r4 | r4 | | r4 | r4 | | | |
| 11 | | r6 | r6 | | r6 | r6 | | | |

---

## 3.15 CLR(1) and LALR(1) Parsing

### LR(1) Items
An LR(1) item is: **[A → α•β, a]**
- A → α•β: LR(0) core
- a: Lookahead symbol

### CLR(1) (Canonical LR)
- Uses LR(1) items with full lookahead
- Most powerful deterministic parser
- Largest table size: Can be O(2ⁿ) states

### LALR(1) (Look-Ahead LR)
- Merges LR(1) states with same core but different lookaheads
- Same power as SLR for most grammars
- Used by YACC/Bison

### Comparison

| Feature | SLR(1) | CLR(1) | LALR(1) |
|---------|--------|--------|---------|
| Lookahead | FOLLOW | Item-specific | Merged |
| States | Fewest | Most | Same as SLR |
| Conflicts | Most | Fewest | Middle |
| Power | Weakest | Strongest | Middle |

### 🎯 GATE Key Insight
```
CLR(1) > LALR(1) > SLR(1) > LL(1)
(Power of grammar recognition)
```

---

## 3.16 Parsing Conflicts

### Shift-Reduce Conflict
When parser can either shift or reduce:
```
In state I:
  A → α•aβ (can shift on a)
  B → γ•   (can reduce if a ∈ FOLLOW(B))
```

### Reduce-Reduce Conflict
When parser can reduce by different productions:
```
In state I:
  A → α•   (can reduce by A → α)
  B → β•   (can reduce by B → β)
And FOLLOW(A) ∩ FOLLOW(B) ≠ ∅
```

### 🎯 GATE Critical: Grammar Classification

| Grammar Type | No Conflicts In |
|--------------|-----------------|
| LL(1) | LL(1) table |
| SLR(1) | SLR table |
| LALR(1) | LALR table |
| CLR(1) | CLR table |

---

## 3.17 Operator Precedence Parsing

### Concept
Uses precedence relations between operators to parse expressions.

### Precedence Relations
- **a ⋖ b:** a has lower precedence (a yields to b)
- **a ≐ b:** a has equal precedence
- **a ⋗ b:** a has higher precedence (a takes from b)

### Operator Precedence Table for Expressions
```
    + | * | id | $
  +-------------
+ | ⋗ | ⋖ | ⋖  | ⋗
* | ⋗ | ⋗ | ⋖  | ⋗
id| ⋗ | ⋗ |    | ⋗
$ | ⋖ | ⋖ | ⋖  |
```

### Algorithm
1. Scan left to right
2. If current ⋖ or ≐ next: Shift
3. If current ⋗ next: Reduce (find handle from right to left)

---

## 3.18 Error Recovery in Parsing

### Panic Mode Recovery
1. Pop stack until state with goto on error symbol
2. Skip input until synchronizing token
3. Push error symbol and continue

### Phrase-Level Recovery
1. Insert/delete/replace symbols locally
2. More refined than panic mode

### Error Productions
Add productions that match common errors:
```
E → E + + E  // Handle double + as error
```

---

## 3.19 GATE Previous Year Patterns

### Pattern 1: FIRST/FOLLOW Computation
**Most frequent!** Always compute step by step.

### Pattern 2: LL(1) Check
1. Compute FIRST sets for all alternatives
2. Check for intersection
3. Check nullable alternatives with FOLLOW

### Pattern 3: SLR Table Entry
Given grammar and state, find ACTION/GOTO entries.

### Pattern 4: Parse Tree Construction
Trace derivation and draw tree.

### Pattern 5: Conflict Identification
Given grammar, identify if SLR/LALR has conflicts.

---

## 📝 Quick Revision Points

1. **Parser:** Tokens → Parse Tree
2. **CFG:** G = (V, T, P, S)
3. **Ambiguous:** Multiple parse trees for same string
4. **Left Recursion:** Eliminated for top-down parsing
5. **FIRST(α):** Terminals that begin strings from α
6. **FOLLOW(A):** Terminals that can follow A
7. **LL(1):** Top-down, predictive, 1 lookahead
8. **LR:** Bottom-up, shift-reduce, most powerful
9. **SLR < LALR < CLR** in power
10. **Handle:** Substring to reduce

---

## 🧠 Mnemonic Summary

### Parser Hierarchy
> **"Silly Lions Love Cats Really"**
> SLR < LALR < CLR (in power)

### FIRST/FOLLOW
> **"FIRST looks at what starts, FOLLOW looks at what follows"**

### Derivation Types
> **"Left expands left, Right expands right"**

### LR Items
> **"Dot moves through production like a reader"**

---

## 🔥 The Adversarial Vault

### Trap 1: LL(1) vs LR
**Q:** Every LL(1) grammar is LR(1)?
**A:** TRUE. LL(1) ⊂ LR(1)

### Trap 2: Left Recursion
**Q:** Can SLR handle left-recursive grammars?
**A:** YES! Only LL parsers need left-recursion removal.

### Trap 3: Ambiguity
**Q:** Can we always remove ambiguity?
**A:** NO! Some languages are inherently ambiguous.

---

## ✅ Self-Assessment Questions

1. Compute FIRST and FOLLOW for a given grammar.
2. Construct LL(1) parsing table.
3. Build LR(0) item sets and SLR table.
4. Identify if grammar is LL(1)/SLR(1)/LALR(1).
5. Trace parsing of a string using shift-reduce.

---

**Next Chapter:** [Syntax Directed Translation →](04-Syntax-Directed-Translation.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
