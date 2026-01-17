# Module 3: Syntax Analysis - Bottom-Up Parsing | The Singularity

> **The Atomic Truth:** *"Reduce handles to non-terminals, build tree upward."*

---

## 🎯 The Path of Elegance (Root Derivation)

### 3.1 Bottom-Up Parsing Overview

```
[Image of Bottom-Up vs Top-Down]
        TOP-DOWN                      BOTTOM-UP
        (LL Parsing)                  (LR Parsing)
        
           S                            S
          /|\                          /|\
         / | \                        / | \ 
        A  B  C     ←── Build ───   A  B  C
        |     |     ←── DOWN  ──    |     |
        a     c                     a     c
        
     Start: S                    Start: input
     Goal: input                 Goal: S
```

### Key Concepts

| Term | Definition |
|------|------------|
| **Handle** | Substring matching RHS of a production that can be reduced |
| **Reduce** | Replace handle with LHS non-terminal |
| **Shift** | Push input symbol onto stack |
| **Viable Prefix** | Prefix of a right sentential form (no symbols past handle) |

### The Rightmost Derivation (Reverse)

Bottom-up parsing traces **rightmost derivation in reverse**.

**Example:**
```
Grammar: E → E + T | T,  T → T * F | F,  F → (E) | id

Rightmost derivation of id + id:
E ⟹ E + T ⟹ E + F ⟹ E + id ⟹ T + id ⟹ F + id ⟹ id + id

Bottom-up (reverse):
id + id → F + id → T + id → E + id → E + F → E + T → E
```

---

## 📐 3.2 Shift-Reduce Parsing

### Parser Configuration

```
Stack          Input          Action
─────          ─────          ──────
$              id + id $      shift
$ id           + id $         reduce F → id
$ F            + id $         reduce T → F
$ T            + id $         reduce E → T
$ E            + id $         shift
$ E +          id $           shift
$ E + id       $              reduce F → id
$ E + F        $              reduce T → F
$ E + T        $              reduce E → E + T
$ E            $              accept
```

### Actions

| Action | Description |
|--------|-------------|
| **Shift** | Push current input onto stack |
| **Reduce** | Pop handle, push non-terminal |
| **Accept** | Input consumed, start symbol on stack |
| **Error** | No valid action |

### Conflicts

| Conflict | Description | Cause |
|----------|-------------|-------|
| **Shift-Reduce** | Can either shift or reduce | Ambiguity or grammar issue |
| **Reduce-Reduce** | Multiple reductions possible | Grammar not suitable for parser |

---

## ⚡ 3.3 LR Parsing | The Most Powerful

### LR Parsing Variants

```
[Image of LR Parser Hierarchy]
              Power
                ↑
              LR(1)     ← Most powerful, largest tables
                ↑
              LALR(1)   ← Best practical choice
                ↑
              SLR(1)    ← Simple, uses FOLLOW
                ↑
              LR(0)     ← Basic, many conflicts
```

| Parser | Lookahead | Table Size | Power |
|--------|-----------|------------|-------|
| LR(0) | 0 | Small | Low |
| SLR(1) | 1 (FOLLOW) | Small | Medium |
| LALR(1) | 1 (refined) | Small | High |
| LR(1) | 1 (full) | Large | Highest |

### LR Parser Structure

```
[Image of LR Parser]
       ┌─────────────────────────────────────────┐
       │              LR Parser                  │
       │  ┌───────────────────────────────────┐  │
       │  │           Stack                   │  │
       │  │  s₀ X₁ s₁ X₂ s₂ ... Xₘ sₘ        │  │
       │  └───────────────────────────────────┘  │
       │              ↑                          │
       │              │                          │
       │  ┌───────────┴───────────┐              │
       │  │    Parsing Table      │              │
       │  │  ┌────────┬────────┐  │              │
       │  │  │ ACTION │  GOTO  │  │              │
       │  │  └────────┴────────┘  │              │
       │  └───────────────────────┘              │
       └─────────────────────────────────────────┘
                        ↓
        aᵢ aᵢ₊₁ ... aₙ $    (Input)
```

### LR Parsing Algorithm

```
Initialize: stack = [0], input pointer at first symbol

while true:
    s = top state on stack
    a = current input symbol
    
    if ACTION[s, a] = shift s':
        push a, push s'
        advance input
    elif ACTION[s, a] = reduce A → β:
        pop 2*|β| symbols (|β| states and symbols)
        s' = new top state
        push A, push GOTO[s', A]
        output A → β
    elif ACTION[s, a] = accept:
        return success
    else:
        error()
```

---

## 🔢 3.4 LR(0) Items and Canonical Collection

### LR(0) Item

An LR(0) item is a production with a dot indicating parsing progress.

**For A → XYZ:**
- A → •XYZ (nothing parsed yet)
- A → X•YZ (X parsed)
- A → XY•Z (XY parsed)
- A → XYZ• (complete, ready to reduce)

### Closure Operation

```
Closure(I):
    J = I
    repeat:
        for each item A → α•Bβ in J:
            for each production B → γ:
                add B → •γ to J (if not present)
    until no new items added
    return J
```

### Goto Operation

```
Goto(I, X):
    J = {}
    for each item A → α•Xβ in I:
        add A → αX•β to J
    return Closure(J)
```

### Canonical LR(0) Collection

```
C = {Closure({S' → •S})}
repeat:
    for each state I in C:
        for each grammar symbol X:
            if Goto(I, X) ≠ ∅ and Goto(I, X) ∉ C:
                add Goto(I, X) to C
until no new states added
```

### Example: LR(0) Items

**Grammar (augmented):**
```
S' → S
S → CC
C → cC | d
```

**I₀ = Closure({S' → •S}):**
```
S' → •S
S → •CC
C → •cC
C → •d
```

**I₁ = Goto(I₀, S):**
```
S' → S•
```

**I₂ = Goto(I₀, C):**
```
S → C•C
C → •cC
C → •d
```

Continue for all symbols...

---

## 📊 3.5 SLR(1) Parsing

### SLR Parsing Table Construction

**ACTION Table:**
1. If A → α•aβ in Iᵢ and Goto(Iᵢ, a) = Iⱼ: ACTION[i, a] = shift j
2. If A → α• in Iᵢ (A ≠ S'): ACTION[i, a] = reduce A → α for all a ∈ FOLLOW(A)
3. If S' → S• in Iᵢ: ACTION[i, $] = accept

**GOTO Table:**
1. If Goto(Iᵢ, A) = Iⱼ: GOTO[i, A] = j

### SLR Conflicts

**SLR uses FOLLOW for reduce decisions:**
- Shift-reduce conflict: Shift symbol ∈ FOLLOW(A)
- Reduce-reduce conflict: Two reductions have overlapping FOLLOW sets

### ⚠️ SLR Limitation

**Grammar:**
```
S → L = R | R
L → *R | id
R → L
```

**Problem in SLR:**
- State with L → id• and S → L•=R
- FOLLOW(L) includes '='
- SLR says reduce on '=' AND shift on '='
- **Conflict!** (But grammar is unambiguous)

---

## 🎯 3.6 CLR(1) - Canonical LR

### LR(1) Item

An LR(1) item includes a lookahead:
```
[A → α•β, a]
```
where `a` is the lookahead terminal.

### LR(1) Closure

```
Closure(I):
    J = I
    repeat:
        for each item [A → α•Bβ, a] in J:
            for each production B → γ:
                for each b in FIRST(βa):
                    add [B → •γ, b] to J
    until no new items
    return J
```

### LR(1) Goto

Same as LR(0) but carries lookahead:
```
Goto(I, X):
    J = {}
    for each [A → α•Xβ, a] in I:
        add [A → αX•β, a] to J
    return Closure(J)
```

### CLR Parsing Table

**ACTION Table:**
1. Shift: Same as SLR
2. Reduce: If [A → α•, a] in Iᵢ: ACTION[i, a] = reduce A → α (**only for lookahead a!**)
3. Accept: Same as SLR

### CLR Power

- Uses precise lookahead instead of FOLLOW
- Resolves SLR conflicts
- **Drawback:** Many more states (can be exponentially more)

---

## ⚡ 3.7 LALR(1) - Lookahead LR

### LALR Construction

**Method 1: Merge LR(1) states with same core**
- Core = items without lookahead
- Merge lookahead sets

**Method 2: Compute from LR(0) with lookahead propagation**
- More efficient for tools

### LALR Properties

| Aspect | LALR |
|--------|------|
| States | Same as SLR (merged LR(1)) |
| Power | Between SLR and CLR |
| Conflicts | May introduce reduce-reduce (not shift-reduce) |
| Usage | Most practical parsers (yacc, bison) |

### LALR vs CLR

```
CLR States:        LALR (merged):
[A → α•, a]        [A → α•, a/b]  ← Merged
[A → α•, b]        (same core, combined lookahead)
```

**LALR can introduce reduce-reduce conflicts that CLR doesn't have!**
(But not shift-reduce conflicts)

---

## 📐 3.8 Operator Precedence Parsing

### Precedence Relations

| Relation | Meaning | When |
|----------|---------|------|
| a < b | a yields precedence to b | a is before handle |
| a = b | a has same precedence as b | Both in handle |
| a > b | a takes precedence over b | a ends handle |

### Operator Precedence Table

For expression grammar:

|   | id | + | * | ( | ) | $ |
|---|---|---|---|---|---|---|
| id | | > | > | | > | > |
| + | < | > | < | < | > | > |
| * | < | > | > | < | > | > |
| ( | < | < | < | < | = | |
| ) | | > | > | | > | > |
| $ | < | < | < | < | | accept |

### Limitations

- Only for operator grammars
- No ε productions
- No adjacent non-terminals in RHS

---

## 🎭 The Bizarre Mnemonic | "The Handle Factory"

*"LR parsing is a REDUCTION FACTORY:
- **Stack** is the assembly line with partially built products
- **Handle** is a complete sub-assembly ready to be boxed
- **Reduce** = box the sub-assembly, label it
- **Shift** = add more raw material to the line
- **Lookahead** = quality inspector checking the next piece
- **SLR** = inspector uses general guidelines (FOLLOW)
- **CLR** = inspector has specific checklist (lookahead)
- **LALR** = inspector with merged checklists"*

---

## 🏆 The 2026 Adversarial Vault

### Trap 1: The FOLLOW vs Lookahead
**Question Pattern:** "SLR has conflict, CLR doesn't. Why?"
**Anti-Solution:** Students think they're the same.
**Truth:** SLR uses FOLLOW(A) for all A → α• items. CLR uses context-specific lookahead computed for each LR(1) item, which is often more precise and can avoid conflicts that appear in SLR.

### Trap 2: The Reduce Action Entry
**Question Pattern:** "Which cells get reduce A → α in SLR table?"
**Anti-Solution:** Students put reduce in wrong columns.
**Truth:** Reduce A → α goes in ACTION[i, a] for ALL a ∈ FOLLOW(A).

### Trap 3: The State Counting
**Question Pattern:** "How many states in LR(0) canonical collection?"
**Anti-Solution:** Students forget closure adds items.
**Truth:** Count STATES (Closure sets), not items. Multiple items per state.

### Trap 4: The LALR Merge Effect
**Question Pattern:** "After merging LR(1) to LALR, what conflicts may appear?"
**Anti-Solution:** Students say shift-reduce.
**Truth:** Only **reduce-reduce** conflicts may be introduced. Never shift-reduce.

### Trap 5: The Handle Identification
**Question Pattern:** "Identify handle in stack: E + T * F"
**Anti-Solution:** Students pick wrong substring.
**Truth:** Handle is the rightmost substring matching a production RHS that should be reduced next.

### NAT Precision Lock
- State numbers: Exact integers
- Item counts: Count carefully (don't double-count)

### MSQ Logic Gate | Elimination Rules
1. LR(1) items include lookahead, LR(0) don't
2. SLR uses FOLLOW, CLR uses specific lookahead
3. LALR = merged CLR states
4. LALR can add reduce-reduce, not shift-reduce

---

## 📊 GATE PYQ Pattern Analysis

| Year | Topic | Marks | Trap Type |
|------|-------|-------|-----------|
| 2023 | LR Table Construction | 2 | Reduce action placement |
| 2022 | SLR vs LALR | 2 | Conflict type |
| 2021 | Handle Identification | 2 | Rightmost substring |
| 2020 | Canonical Collection | 2 | State count |

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| LR(0) item count | Production length + 1 |
| Reduce in SLR | FOLLOW columns only |
| CLR → LALR merge | Same core items |
| Handle position | Rightmost reducible |

---

## 🧮 Solved Examples

### Example 1: LR(0) Item Generation
**Production:** A → BCD

**Items:**
- A → •BCD
- A → B•CD
- A → BC•D
- A → BCD•

**Count:** 4 items

### Example 2: SLR Table Entry
**Given:** State I₃ contains: A → α• and FOLLOW(A) = {a, b, $}

**ACTION entries:**
- ACTION[3, a] = reduce A → α
- ACTION[3, b] = reduce A → α
- ACTION[3, $] = reduce A → α

### Example 3: Conflict Detection
**State with:**
- A → α•aβ (suggests shift on 'a')
- B → γ• and a ∈ FOLLOW(B) (suggests reduce on 'a')

**Result:** Shift-reduce conflict on 'a'. NOT SLR(1).

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Would you like to initiate a **'Multi-Variable Stress Test'** combining LR Parsing with Semantic Analysis for a Rank-1 simulation?*

---
[← Previous: Top-Down Parsing](./02-Syntax-Analysis-TopDown.md) | [Back to Index](./README.md) | [Next: Semantic Analysis & SDT →](./04-Semantic-Analysis-SDT.md)
