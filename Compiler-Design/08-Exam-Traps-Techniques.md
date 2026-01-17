# Module 8: Exam Traps & Problem-Solving Techniques | The Singularity

> **The Atomic Truth:** *"Master the traps, dominate the exam."*

---

## 🎯 The Meta-Strategy | GATE CD Mastery

### Complexity Assessment (IIT Guwahati Standards 2026)

| Topic | Weightage | Difficulty | Trap Density |
|-------|-----------|------------|--------------|
| LR Parsing | 8-10 marks | Very High | Very High |
| FIRST/FOLLOW | 6-8 marks | High | High |
| Lexical Analysis | 4-6 marks | Medium | Medium |
| SDT/Attributes | 4-6 marks | High | High |
| Code Optimization | 4-6 marks | Medium | Medium |
| Code Generation | 2-4 marks | Medium | Low |

---

## 🚨 The Master Trap Compendium

### Category 1: Grammar & Parsing Traps

#### Trap 1.1: The Left Recursion LL(1) Fallacy
**Pattern:** "Is this grammar LL(1)?"

**Anti-Solution:** Students compute FIRST/FOLLOW for left-recursive grammar.

**Truth:** Left recursion → IMMEDIATELY NOT LL(1). Save time!

**Snap-Check:** See A → Aα? Stop. NOT LL(1).

#### Trap 1.2: The Indirect Left Recursion
**Pattern:** A → Bα, B → Aβ

**Anti-Solution:** Students don't recognize indirect recursion.

**Truth:** Must eliminate systematically using ordering algorithm.

#### Trap 1.3: The FIRST(ε) Confusion
**Pattern:** What's FIRST(ε)?

**Answer:** FIRST(ε) = {ε}. Not empty set!

#### Trap 1.4: The FOLLOW Propagation
**Pattern:** A → αB where no β after B

**Anti-Solution:** Students forget to add FOLLOW(A) to FOLLOW(B).

**Truth:** When B is at production end, FOLLOW(A) ⊆ FOLLOW(B).

#### Trap 1.5: The LL(1) FOLLOW Condition
**Pattern:** A → α | ε, what condition?

**Anti-Solution:** Students only check FIRST(α).

**Truth:** If ε ∈ FIRST(α), must ensure FIRST(α) ∩ FOLLOW(A) = ∅.

---

### Category 2: LR Parsing Traps

#### Trap 2.1: The LR(0) vs LR(1) Item
**Pattern:** What's in an LR(1) item?

**Answer:** [A → α•β, a] - includes lookahead 'a'.

**LR(0):** A → α•β (no lookahead)

#### Trap 2.2: The SLR vs CLR Reduce
**Pattern:** "Where to place reduce in parsing table?"

**SLR:** Reduce A → α for ALL a ∈ FOLLOW(A)
**CLR:** Reduce A → α ONLY for specific lookahead a

This is why CLR resolves some SLR conflicts!

#### Trap 2.3: The LALR Merge Conflict
**Pattern:** "What conflicts can merging introduce?"

**Anti-Solution:** Students say shift-reduce.

**Truth:** ONLY reduce-reduce conflicts can be introduced by merging. Never shift-reduce.

#### Trap 2.4: The Handle Identification
**Pattern:** "Find handle in: E + T * F"

**Anti-Solution:** Students pick leftmost match.

**Truth:** Handle is the RIGHTMOST substring that should be reduced next (following rightmost derivation in reverse).

#### Trap 2.5: The State Count
**Pattern:** "How many LR(0) states?"

**Anti-Solution:** Counting items instead of states.

**Truth:** Count STATES (each is a closure set), not individual items.

---

### Category 3: Attribute Grammar Traps

#### Trap 3.1: The S-Attributed Definition
**Pattern:** "Is this S-attributed?"

**Definition:** S-attributed uses ONLY synthesized attributes.

**Test:** Any inherited attribute → NOT S-attributed.

#### Trap 3.2: The L-Attributed Right Sibling
**Pattern:** B.inh = f(C.syn) in A → BC

**Anti-Solution:** Students think this is valid.

**Truth:** NOT L-attributed! B depends on RIGHT sibling C. Violation!

#### Trap 3.3: The SDT Action Placement
**Pattern:** "Where to insert action for L.in = T.type in D → T L?"

**Anti-Solution:** Students put at end.

**Truth:** BETWEEN T and L: `D → T { L.in = T.type } L`

---

### Category 4: Lexical Analysis Traps

#### Trap 4.1: The NFA to DFA Start
**Pattern:** "DFA start state?"

**Anti-Solution:** Students say {start_NFA}.

**Truth:** ε-closure({start_NFA}) - must include ε-reachable states!

#### Trap 4.2: The RE Precedence
**Pattern:** "Language of ab|c*?"

**Anti-Solution:** Parsing as (ab|c)*.

**Truth:** Precedence: * > concat > |. Answer: (ab) | (c*)

#### Trap 4.3: The DFA Final States
**Pattern:** "Which DFA states are final?"

**Anti-Solution:** Only states containing ONLY NFA finals.

**Truth:** Any DFA state containing ANY NFA final state is final.

#### Trap 4.4: The Minimum DFA
**Pattern:** "Is this DFA minimal?"

**Test:** Apply partitioning algorithm. Check if states distinguish same strings.

---

### Category 5: Code Optimization Traps

#### Trap 5.1: The Data Flow Direction
**Pattern:** "Live variable analysis direction?"

**Answer:** BACKWARD (from use to definition)

**Reaching definitions:** FORWARD

#### Trap 5.2: The Meet Operation
**Pattern:** "Meet for available expressions?"

**Answer:** INTERSECTION (must be available on ALL paths)

**Reaching definitions:** UNION (may reach on ANY path)

#### Trap 5.3: The Loop Invariant Condition
**Pattern:** "When can we move code out of loop?"

**Conditions:**
1. No definitions of operands in loop
2. Single definition of result in loop
3. Definition dominates all uses

#### Trap 5.4: The Basic Block Leaders
**Pattern:** "Identify leaders."

**Leaders:**
1. First statement
2. Target of any jump
3. Statement after any jump

---

### Category 6: Code Generation Traps

#### Trap 6.1: The Stack Direction
**Pattern:** "Stack grows toward?"

**Answer:** LOWER addresses (SP decreases on push).

#### Trap 6.2: The Static vs Dynamic Scope
**Pattern:** "Which x does foo see?"

**Static (Lexical):** Declaration in textually enclosing scope.
**Dynamic:** Most recent active declaration on call stack.

#### Trap 6.3: The Call by Name
**Pattern:** "swap(i, a[i]) result?"

**Anti-Solution:** Same as call by reference.

**Truth:** Re-evaluates expression each access. If i changes, a[i] refers to different element!

---

## 📊 The Question Type Decoder

### Type 1: Construction Questions
**Keywords:** "Construct", "Build", "Generate"

**Strategy:**
- LR parsing table: Follow algorithm step-by-step
- FIRST/FOLLOW: Apply rules systematically
- NFA/DFA: Use Thompson's, subset construction

### Type 2: Identification Questions
**Keywords:** "Is this...", "Which type..."

**Strategy:**
- LL(1): Check left recursion first, then FIRST/FOLLOW
- S/L-attributed: Check attribute types
- Ambiguous: Find multiple parse trees

### Type 3: Calculation Questions
**Keywords:** "How many", "Count"

**Strategy:**
- States: Build canonical collection carefully
- Items: Count dot positions
- Temporaries: Count operations

### Type 4: Comparison Questions
**Keywords:** "Difference", "Compare", "Which is more powerful"

**Strategy:**
- Parser hierarchy: LR(0) < SLR < LALR < CLR
- Attribute types: S ⊂ L
- Analysis direction: Know forward vs backward

---

## ⚡ The 60-Second Topic Revision

### Lexical Analysis
- RE → NFA: Thompson's (2 states per symbol)
- NFA → DFA: Subset construction (ε-closure!)
- DFA minimization: Partition refinement
- Precedence: * > concatenation > |

### Syntax Analysis
- LL(1): No left recursion, no common prefix
- FIRST: First terminals derivable
- FOLLOW: Terminals that can follow
- LR: Reduce uses FOLLOW (SLR) or lookahead (CLR)

### Semantic Analysis
- Synthesized: From children (up)
- Inherited: From parent/left siblings (down)
- S-attributed: Only synthesized
- L-attributed: No right sibling dependency

### Intermediate Code
- TAC: At most 3 addresses
- Quadruple: (op, arg1, arg2, result)
- Triple: (op, arg1, arg2), result is index

### Optimization
- CSE: Eliminate redundant computation
- Dead code: Remove unused results
- Live variables: Backward analysis, union meet
- Available expressions: Forward analysis, intersection meet

### Code Generation
- Stack grows down
- Static scope: Textual enclosure
- Dynamic scope: Runtime stack
- Call by value: Copy, call by reference: Address

---

## 🎯 The NAT Answer Precision Guide

| Question Type | Precision |
|---------------|-----------|
| State count | Exact integer |
| FIRST/FOLLOW set size | Count elements |
| Parse table entries | One per cell for LL(1) |
| Temporary count | Exact integer |

### Common NAT Pitfalls
1. **ε in FIRST:** Count it if asked for cardinality
2. **$ in FOLLOW:** Always in FOLLOW(Start)
3. **States vs Items:** States contain multiple items
4. **Off-by-one:** Closure adds items

---

## 🎭 The Exam Day Protocol

### Before the Exam
1. Memorize: RE precedence, parsing hierarchy
2. Practice: FIRST/FOLLOW calculation
3. Review: LR parsing table construction

### During the Exam
1. Read TWICE
2. Identify question type
3. Check for quick eliminations (left recursion → not LL(1))
4. Apply algorithm systematically
5. Verify answer makes sense

### For MSQ (Multi-Select)
1. Evaluate EACH option
2. Don't assume patterns
3. Partial credit > wrong answer

### For NAT
1. Count carefully
2. Double-check ε and $
3. Verify algorithm application

---

## 📚 The Formula Quick Reference

### Regular Expressions
- (r)* = r* (parentheses don't affect closure)
- (r|s)* ≠ r*|s* in general
- ε* = ε
- ∅* = ε

### Parsing
- LL(1): FIRST(α) ∩ FIRST(β) = ∅ and ε → FOLLOW check
- States in DFA: ≤ 2^n (from n-state NFA)
- LR(1) items: LR(0) items × |FOLLOW + ε|

### Optimization
- Basic blocks: Single entry, single exit
- IN[B] = ∪/∩ OUT[predecessors] (depending on analysis)
- OUT[B] = GEN[B] ∪ (IN[B] - KILL[B])

### Code Generation
- Activation record: Parameters + Return addr + FP + Locals + Temps
- Stack offset: FP-relative addressing

---

## 🏆 The Final Checklist

### Before Answering Grammar Questions
- [ ] Is it left recursive? → Not LL(1)
- [ ] Common prefix? → Need left factoring
- [ ] Ambiguous? → Check carefully

### Before Answering Parsing Table Questions
- [ ] Which parser type? (LL/SLR/CLR/LALR)
- [ ] Correct algorithm applied?
- [ ] Reduce in right columns?

### Before Answering Attribute Questions
- [ ] Synthesized or inherited?
- [ ] Any right sibling dependency?
- [ ] Evaluation order valid?

### Before Answering Optimization Questions
- [ ] Forward or backward analysis?
- [ ] Union or intersection meet?
- [ ] Loop invariant conditions met?

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*You have completed the Compiler Design Mastery Guide. Would you like to proceed to a **'Full-Spectrum Mock Test'** simulating actual GATE conditions?*

---
[← Previous: Code Generation & Runtime](./07-Code-Generation-Runtime.md) | [Back to Index](./README.md)
