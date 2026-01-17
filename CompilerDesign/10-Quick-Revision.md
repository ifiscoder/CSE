# Chapter 10: Quick Revision & Formulas

## 🎯 The Ultimate Cheat Sheet for GATE/ESE/PSU

---

## 📊 The 6 Phases at a Glance

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        COMPILER PHASES                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ Phase 1: LEXICAL ANALYZER                                              │
│ Input:  Character Stream                                                │
│ Output: Token Stream                                                    │
│ Tool:   LEX, Flex                                                       │
│ Uses:   RE, DFA                                                         │
│ Error:  "Illegal character"                                            │
│                                                                         │
│ Phase 2: SYNTAX ANALYZER                                               │
│ Input:  Token Stream                                                    │
│ Output: Parse Tree                                                      │
│ Tool:   YACC, Bison                                                     │
│ Uses:   CFG, LL/LR Parsing                                             │
│ Error:  "Syntax error"                                                 │
│                                                                         │
│ Phase 3: SEMANTIC ANALYZER                                             │
│ Input:  Parse Tree                                                      │
│ Output: Annotated Parse Tree                                           │
│ Uses:   SDT, Symbol Table                                              │
│ Error:  "Type mismatch", "Undeclared"                                 │
│                                                                         │
│ Phase 4: INTERMEDIATE CODE GEN                                         │
│ Input:  Annotated Parse Tree                                           │
│ Output: TAC, Quadruples, Triples                                       │
│ Uses:   DAG for optimization                                           │
│                                                                         │
│ Phase 5: CODE OPTIMIZER                                                │
│ Input:  IR                                                              │
│ Output: Optimized IR                                                    │
│ Uses:   Data Flow Analysis                                             │
│                                                                         │
│ Phase 6: CODE GENERATOR                                                │
│ Input:  Optimized IR                                                    │
│ Output: Target Code                                                     │
│ Uses:   Register Allocation                                            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 📐 Critical Formulas

### Regular Expressions & Finite Automata

| Formula | Description |
|---------|-------------|
| Max DFA states from n-state NFA | $2^n$ (worst case) |
| NFA states for RE with n operators | $\leq 2n$ (Thompson's) |
| RE to NFA | Thompson's Construction: O(n) |
| NFA to DFA | Subset Construction: O($2^n$) |
| DFA Minimization | O($n^2 \cdot |\Sigma|$) |

### Parsing Formulas

| Formula | Description |
|---------|-------------|
| LL(1) Condition | FIRST(α) ∩ FIRST(β) = ∅ AND if ε ∈ FIRST(α), FIRST(β) ∩ FOLLOW(A) = ∅ |
| LR(0) Items for A → XYZ | 4 items: A→•XYZ, A→X•YZ, A→XY•Z, A→XYZ• |
| SLR Reduce Condition | Reduce A→α if input ∈ FOLLOW(A) |
| Parse Tree Leaves | = Number of terminals in derived string |

### Grammar Power Hierarchy
$$\text{LL}(1) \subset \text{SLR}(1) \subset \text{LALR}(1) \subset \text{CLR}(1)$$

### FIRST and FOLLOW Quick Rules

```
FIRST(X):
├── X is terminal → {X}
├── X → ε → ε ∈ FIRST(X)
└── X → Y₁Y₂...Yₖ → Add FIRST(Y₁) - {ε}
                    → If ε ∈ FIRST(Y₁), add FIRST(Y₂) - {ε}
                    → Continue...

FOLLOW(A):
├── A is start → $ ∈ FOLLOW(A)
├── B → αAβ → FIRST(β) - {ε} ⊆ FOLLOW(A)
└── B → αA or ε ∈ FIRST(β) → FOLLOW(B) ⊆ FOLLOW(A)
```

### Code Generation Formulas

| Formula | Description |
|---------|-------------|
| Ershov Numbers (equal) | n = left + 1 |
| Ershov Numbers (unequal) | n = max(left, right) |
| Minimum Registers | Label at root of expression tree |
| Spill Cost | $\sum (\text{uses} + \text{defs}) \times 10^{\text{loop depth}}$ |

### Array Address Calculation

| Array Type | Formula (0-indexed, width w) |
|------------|------------------------------|
| 1D: A[i] | base + i × w |
| 2D Row-Major: A[i][j] | base + (i × cols + j) × w |
| 2D Column-Major: A[i][j] | base + (j × rows + i) × w |

### Activation Record Size
$$\text{Size} = \text{Return Value} + \text{Parameters} + \text{Links} + \text{Saved Regs} + \text{Locals} + \text{Temps}$$

---

## 📋 Comparison Tables

### Parser Comparison

| Feature | LL(1) | SLR(1) | LALR(1) | CLR(1) |
|---------|-------|--------|---------|--------|
| Direction | Top-down | Bottom-up | Bottom-up | Bottom-up |
| Left Recursion | ❌ Cannot handle | ✅ Handles | ✅ Handles | ✅ Handles |
| Power | Weakest | Weak | Medium | Strongest |
| Table Size | Small | Small | Small | Large |
| Lookahead | FIRST | FOLLOW | Per-item | Per-item |
| Tool | Recursive Descent | Simple LR | YACC/Bison | Full LR |

### IR Representations

| Representation | Fields | Size | Reordering |
|----------------|--------|------|------------|
| Quadruple | (op, arg1, arg2, result) | 4 | Easy |
| Triple | (op, arg1, arg2) | 3 | Hard |
| Indirect Triple | Pointer + Triple | 1 + 3 | Easy |

### Parameter Passing

| Method | Passed | Changes Visible? | Aliasing Issue |
|--------|--------|------------------|----------------|
| Value | Copy | No | None |
| Reference | Address | Yes | Yes |
| Copy-Restore | Copy→Copy | Yes (at end) | Order matters |
| Name | Thunk | Yes | Substitution |

### Optimization Types

| Optimization | Scope | Example |
|--------------|-------|---------|
| Constant Folding | Local | 2+3 → 5 |
| CSE | Local/Global | Reuse a+b |
| Dead Code | Local/Global | Remove unused |
| Loop Invariant | Loop | Move invariant out |
| Strength Reduction | Loop | i*4 → i<<2 |
| Inlining | Interprocedural | Replace call with body |

### Memory Regions

| Region | Allocation | Deallocation | Contents |
|--------|------------|--------------|----------|
| Code | Compile-time | Never | Instructions |
| Static | Compile-time | Program end | Globals, constants |
| Stack | Function call | Function return | Locals, params |
| Heap | malloc/new | free/delete/GC | Dynamic data |

---

## 🎯 One-Liner Concepts

### Lexical Analysis
- **Token:** `<name, attribute>` pair
- **Lexeme:** Actual string matched
- **Pattern:** Rule (RE) for token
- **LEX conflict:** Longest match wins; if tie, first rule

### Parsing
- **Ambiguous:** Multiple parse trees for same string
- **Left Recursion:** A → Aα | β (eliminate for LL)
- **Left Factoring:** A → αβ₁ | αβ₂ → A → αA', A' → β₁ | β₂
- **Handle:** String to reduce in shift-reduce parsing

### SDT
- **Synthesized:** Computed from children (bottom-up)
- **Inherited:** Computed from parent/siblings (top-down)
- **S-attributed ⊂ L-attributed:** Every S is also L

### Intermediate Code
- **TAC:** x = y op z (max 3 addresses)
- **DAG:** Compact tree with shared CSE nodes
- **Backpatching:** Fill jump targets later

### Runtime
- **Activation Record:** Frame for function call
- **Control Link:** Pointer to caller's frame (dynamic)
- **Access Link:** Pointer to enclosing scope (static)

### Optimization
- **Basic Block:** Single entry, single exit, no jumps
- **Live Variable:** Used later without redefinition
- **Available Expression:** Computed on all paths, not invalidated

---

## 🔢 Quick Number Reference

| Concept | Value/Count |
|---------|-------------|
| Compiler phases | 6 |
| Max DFA states (n-state NFA) | 2ⁿ |
| Items for production with k RHS symbols | k + 1 |
| LL(1) lookahead | 1 |
| LR(k) typical k | 0 or 1 |
| Ershov: equal children | label + 1 |
| Ershov: unequal children | max of labels |

---

## 📝 Common GATE Question Types

### Type 1: FIRST/FOLLOW Computation
1. Start with terminals: FIRST(a) = {a}
2. Apply rules iteratively
3. Remember $ in FOLLOW(Start)

### Type 2: LL(1) Table Construction
1. Compute FIRST and FOLLOW
2. For A → α: Put in M[A, a] for a ∈ FIRST(α)
3. If ε ∈ FIRST(α): Put in M[A, b] for b ∈ FOLLOW(A)

### Type 3: SLR Table Construction
1. Compute LR(0) items and item sets
2. Build DFA of item sets
3. SHIFT: A → α•aβ, goto exists
4. REDUCE: A → α• for all a ∈ FOLLOW(A)

### Type 4: Generate TAC
1. Use temporaries for subexpressions
2. One operation per line
3. Handle operators left to right (or by precedence)

### Type 5: Count Registers
1. Label leaves with 1 (leftmost) or 0
2. Apply Ershov rules at each interior node
3. Root label = minimum registers

---

## 🎓 Last-Minute Tips

### Before Exam
1. **Memorize:** FIRST/FOLLOW rules, Ershov formula, Parser hierarchy
2. **Practice:** Table construction (LL1, SLR), TAC generation
3. **Review:** Error types by phase, Optimization classifications

### During Exam
1. **Read carefully:** Many questions have subtle traps
2. **Eliminate:** Use hierarchy rules (LL ⊂ SLR ⊂ LALR ⊂ CLR)
3. **Verify:** Check parse table entries, trace derivations
4. **Time management:** Skip long computations, return later

### Common Mistakes to Avoid
1. Forgetting $ in FOLLOW(Start)
2. Confusing NFA→DFA states count (2ⁿ, not n²)
3. Left recursion removal changes grammar's parsed structure
4. SLR uses FOLLOW, not item-specific lookahead

---

## 🏆 The Golden Rules

1. **Phases:** "Lazy Students Study In Old Gardens"
2. **Parser Power:** SLR < LALR < CLR
3. **Attributes:** S goes UP, L goes LEFT
4. **Memory:** Code→Static→Heap↑→Stack↓
5. **Recovery:** Panic mode is most common
6. **Optimization:** Focus on loops (90% time)
7. **Registers:** Ershov for min count, graph coloring for allocation

---

## 📖 Topic-wise Weightage (GATE)

| Topic | Expected Marks | Priority |
|-------|----------------|----------|
| Parsing (LL, LR) | 4-6 | ⭐⭐⭐⭐⭐ |
| Lexical (RE, FA) | 2-4 | ⭐⭐⭐⭐ |
| FIRST/FOLLOW | 2-4 | ⭐⭐⭐⭐⭐ |
| SDT | 1-2 | ⭐⭐⭐ |
| Intermediate Code | 1-2 | ⭐⭐⭐ |
| Runtime | 1-2 | ⭐⭐⭐ |
| Optimization | 1-2 | ⭐⭐ |
| Code Gen | 0-2 | ⭐⭐ |

---

**Next Chapter:** [Previous Year Questions →](11-Previous-Year-Questions.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Quick Revision Complete.*
