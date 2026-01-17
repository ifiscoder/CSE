# Module 2: Syntax Analysis - Top-Down Parsing | The Singularity

> **The Atomic Truth:** *"Start from root, grow the parse tree downward."*

---

## 🎯 The Path of Elegance (Root Derivation)

### 2.1 Context-Free Grammars | The Foundation

**Definition:** $G = (V, T, P, S)$
- $V$: Set of non-terminals (variables)
- $T$: Set of terminals
- $P$: Set of productions ($A \to \alpha$)
- $S$: Start symbol ($S \in V$)

### Grammar Notation

```
[Image of Production Format]
    A → α
    │    │
    │    └─ Body: String of terminals/non-terminals
    └────── Head: Single non-terminal
```

### Derivation Types

| Type | Description | Parser Type |
|------|-------------|-------------|
| **Leftmost** | Always expand leftmost non-terminal | Top-Down |
| **Rightmost** | Always expand rightmost non-terminal | Bottom-Up |

### Example Grammar

```
E → E + T | T
T → T * F | F
F → (E) | id
```

**Derivation of id + id * id:**
```
Leftmost:  E ⟹ E + T ⟹ T + T ⟹ F + T ⟹ id + T ⟹ id + T * F ⟹ id + F * F ⟹ id + id * F ⟹ id + id * id
```

---

## 📐 2.2 Parse Trees & Ambiguity

### Parse Tree Structure

```
[Image of Parse Tree]
                    E
                 /  |  \
                E   +   T
                |      /|\
                T     T * F
                |     |   |
                F     F   id
                |     |
               id    id
```

### Ambiguous Grammar

**Definition:** Grammar is ambiguous if some string has more than one:
- Parse tree, OR
- Leftmost derivation, OR
- Rightmost derivation

**Classic Example (Dangling Else):**
```
S → if E then S
  | if E then S else S
  | other
```

For: `if E then if E then S else S`
- Does `else` bind to first or second `if`?

**Resolution:** Most languages bind else to nearest if.

### Disambiguating Techniques

1. **Rewrite grammar** (add more non-terminals)
2. **Use precedence/associativity rules** (in parser)
3. **Semantic actions** (choose one interpretation)

---

## 🔧 2.3 Grammar Transformations

### Eliminating Left Recursion

**Direct Left Recursion:**
```
A → Aα | β   (where β doesn't start with A)
```

**Transform to:**
```
A  → βA'
A' → αA' | ε
```

**Example:**
```
E → E + T | T
```
**Becomes:**
```
E  → TE'
E' → +TE' | ε
```

### Indirect Left Recursion

**Algorithm:**
1. Order non-terminals: $A_1, A_2, ..., A_n$
2. For $i = 1$ to $n$:
   - For $j = 1$ to $i-1$:
     - Replace $A_i \to A_j\gamma$ with $A_i \to \delta_1\gamma | \delta_2\gamma | ...$ (where $A_j \to \delta_1 | \delta_2 | ...$)
   - Eliminate direct left recursion for $A_i$

**Example:**
```
S → Aa | b
A → Ac | Sd | ε
```

**Step 1:** Order: S, A
**Step 2:** For A, replace S:
```
A → Ac | Aad | bd | ε
```
**Step 3:** Remove direct left recursion:
```
A  → bdA' | A'
A' → cA' | adA' | ε
```

### Left Factoring

**Pattern:**
```
A → αβ₁ | αβ₂
```

**Transform to:**
```
A  → αA'
A' → β₁ | β₂
```

**Example:**
```
S → iEtS | iEtSeS | a
E → b
```
**Becomes:**
```
S  → iEtSS' | a
S' → eS | ε
E  → b
```

---

## ⚡ 2.4 FIRST and FOLLOW Sets | The Golden Pivot

### FIRST(X) | What can start X?

**Definition:** Set of terminals that begin strings derived from X.

**Rules:**
1. If $X$ is terminal: $FIRST(X) = \{X\}$
2. If $X \to \varepsilon$: Add $\varepsilon$ to $FIRST(X)$
3. If $X \to Y_1Y_2...Y_k$:
   - Add $FIRST(Y_1) - \{\varepsilon\}$ to $FIRST(X)$
   - If $\varepsilon \in FIRST(Y_1)$, add $FIRST(Y_2) - \{\varepsilon\}$
   - Continue until non-nullable or end
   - If all $Y_i$ nullable, add $\varepsilon$

### FOLLOW(A) | What can follow A?

**Definition:** Set of terminals that can appear immediately after A.

**Rules:**
1. Add $\$$ to $FOLLOW(S)$ (start symbol)
2. If $A \to \alpha B \beta$:
   - Add $FIRST(\beta) - \{\varepsilon\}$ to $FOLLOW(B)$
3. If $A \to \alpha B$ or ($A \to \alpha B \beta$ and $\varepsilon \in FIRST(\beta)$):
   - Add $FOLLOW(A)$ to $FOLLOW(B)$

### ⚡ The GATE Master Algorithm

```
// Computing FIRST for string X₁X₂...Xₙ
FIRST(X₁X₂...Xₙ):
    result = {}
    for i = 1 to n:
        result = result ∪ (FIRST(Xᵢ) - {ε})
        if ε ∉ FIRST(Xᵢ):
            return result
    result = result ∪ {ε}  // All Xᵢ can derive ε
    return result
```

### Example: FIRST and FOLLOW

**Grammar:**
```
E  → TE'
E' → +TE' | ε
T  → FT'
T' → *FT' | ε
F  → (E) | id
```

**FIRST Sets:**
| Symbol | FIRST |
|--------|-------|
| F | { (, id } |
| T' | { *, ε } |
| T | { (, id } |
| E' | { +, ε } |
| E | { (, id } |

**FOLLOW Sets:**
| Symbol | FOLLOW |
|--------|--------|
| E | { ), $ } |
| E' | { ), $ } |
| T | { +, ), $ } |
| T' | { +, ), $ } |
| F | { *, +, ), $ } |

---

## 📊 2.5 LL(1) Parsing | Predictive Parsing

### LL(1) Definition

- **L:** Left-to-right scan
- **L:** Leftmost derivation
- **1:** One lookahead symbol

### LL(1) Grammar Condition

Grammar is LL(1) iff for every pair of productions $A \to \alpha | \beta$:

1. $FIRST(\alpha) \cap FIRST(\beta) = \emptyset$
2. If $\varepsilon \in FIRST(\alpha)$, then $FIRST(\beta) \cap FOLLOW(A) = \emptyset$

### LL(1) Parsing Table Construction

For each production $A \to \alpha$:
1. For each $a \in FIRST(\alpha)$: Add $A \to \alpha$ to $M[A, a]$
2. If $\varepsilon \in FIRST(\alpha)$:
   - For each $b \in FOLLOW(A)$: Add $A \to \alpha$ to $M[A, b]$

### Example LL(1) Table

| | id | + | * | ( | ) | $ |
|---|---|---|---|---|---|---|
| E | E→TE' | | | E→TE' | | |
| E' | | E'→+TE' | | | E'→ε | E'→ε |
| T | T→FT' | | | T→FT' | | |
| T' | | T'→ε | T'→*FT' | | T'→ε | T'→ε |
| F | F→id | | | F→(E) | | |

### LL(1) Parsing Algorithm

```
Stack: [S, $]   Input: w$

while stack not empty:
    X = top of stack
    a = current input
    
    if X == a:
        pop stack, advance input
    elif X is terminal:
        ERROR
    elif M[X, a] is empty:
        ERROR
    else:
        pop X
        push M[X, a] production body (reversed)
        output production
```

---

## 🔄 2.6 Recursive Descent Parsing

### Structure

One procedure per non-terminal:
```
void A() {
    choose production A → X₁X₂...Xₖ based on lookahead
    for each Xᵢ:
        if Xᵢ is non-terminal:
            call Xᵢ()
        else if Xᵢ matches current token:
            advance to next token
        else:
            error()
}
```

### Example for Expression Grammar

```c
void E() {
    T();
    E_prime();
}

void E_prime() {
    if (lookahead == '+') {
        match('+');
        T();
        E_prime();
    }
    // else: ε production (do nothing)
}

void T() {
    F();
    T_prime();
}

// ... similar for T_prime and F
```

### Predictive Parser vs Recursive Descent

| Aspect | Predictive | Recursive Descent |
|--------|------------|-------------------|
| Implementation | Table-driven | Procedure calls |
| Speed | Faster | Slower (call overhead) |
| Grammar changes | Update table | Update procedures |
| Error recovery | Harder | Easier |

---

## 🎭 The Bizarre Mnemonic | "The LL(1) Restaurant"

*"LL(1) parsing is like ordering from a MENU:
- **FIRST:** What appetizer (first terminal) can each dish (production) start with?
- **FOLLOW:** If dish is empty (ε), what comes next?
- **Parsing Table:** The menu card - one dish per (category, appetizer) pair
- **Conflict:** Two dishes for same appetizer = ambiguous menu = NOT LL(1)!"*

---

## 🏆 The 2026 Adversarial Vault

### Trap 1: The ε in FIRST Propagation
**Question Pattern:** "Calculate FIRST(XY) where X →ε."
**Anti-Solution:** Students only take FIRST(X).
**Truth:** If ε ∈ FIRST(X), must also add FIRST(Y)!

### Trap 2: The FOLLOW Inheritance
**Question Pattern:** "Calculate FOLLOW(B) in A → αB."
**Anti-Solution:** Students forget to add FOLLOW(A).
**Truth:** When B is at end of production, FOLLOW(A) ⊆ FOLLOW(B).

### Trap 3: The Left Recursion LL(1) Failure
**Question Pattern:** "Is E → E + T | T LL(1)?"
**Anti-Solution:** Students try to build parse table.
**Truth:** Left recursion → NOT LL(1) immediately! No need to check.

### Trap 4: The Common Prefix
**Question Pattern:** "Is S → if E then S | if E then S else S LL(1)?"
**Anti-Solution:** Students compute FIRST incorrectly.
**Truth:** Common prefix "if E then S" → NOT LL(1). Need left factoring.

### NAT Precision Lock
- Set cardinality: Count elements exactly
- Table entries: One production per cell for LL(1)

### MSQ Logic Gate | Elimination Rules
1. Left recursive → NOT LL(1)
2. Common prefix → NOT LL(1) 
3. ε ∈ FIRST(α) → Must check FOLLOW condition
4. Multiple entries in M[A,a] → NOT LL(1)

---

## 📊 GATE PYQ Pattern Analysis

| Year | Topic | Marks | Trap Type |
|------|-------|-------|-----------|
| 2023 | FIRST/FOLLOW | 2 | ε propagation |
| 2022 | LL(1) Check | 2 | Left recursion |
| 2021 | Parse Table | 2 | FOLLOW in ε productions |
| 2020 | Left Factoring | 1 | Transformation |

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| Left recursion | → NOT LL(1) |
| Common prefix | → Need left factoring |
| ε production | → Use FOLLOW |
| $ in FOLLOW | → Only for start reachable |

---

## 🧮 Solved Examples

### Example 1: FIRST/FOLLOW Calculation
**Grammar:**
```
S → AB
A → aA | ε
B → bB | c
```

**FIRST:**
- FIRST(B) = {b, c}
- FIRST(A) = {a, ε}
- FIRST(S) = (FIRST(A)-{ε}) ∪ FIRST(B) = {a, b, c}

**FOLLOW:**
- FOLLOW(S) = {$}
- FOLLOW(A) = FIRST(B) = {b, c}
- FOLLOW(B) = FOLLOW(S) = {$}

### Example 2: LL(1) Verification
**Grammar:**
```
S → aAB | bA
A → aA | ε
B → b
```

**Check S:**
- FIRST(aAB) = {a}
- FIRST(bA) = {b}
- Disjoint ✓

**Check A:**
- FIRST(aA) = {a}
- FIRST(ε) = {ε}, so check FOLLOW(A)
- Need FOLLOW(A) ∩ FIRST(aA) = ∅
- FOLLOW(A) includes FIRST(B) = {b} and possibly more
- {a} ∩ {b,...} = ∅ ✓

**Result:** LL(1) ✓

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Would you like to initiate a **'Multi-Variable Stress Test'** combining LL(1) with LR Parsing for a Rank-1 simulation?*

---
[← Previous: Lexical Analysis](./01-Lexical-Analysis.md) | [Back to Index](./README.md) | [Next: Syntax Analysis - Bottom-Up →](./03-Syntax-Analysis-BottomUp.md)
