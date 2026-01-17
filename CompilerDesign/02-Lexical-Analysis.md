# Chapter 2: Lexical Analysis

## 🎯 The Atomic Truth
> **"Lexical Analyzer = Character Stream → Token Stream"**

---

## 2.1 What is Lexical Analysis?

### Definition
**Lexical Analysis** (also called **Scanning**) is the first phase of a compiler that reads the source program character by character and groups them into meaningful sequences called **lexemes**, producing **tokens** as output.

```
┌────────────────────────────────────────────────────────────────────────┐
│                          LEXICAL ANALYZER                              │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   ┌─────────────┐                              ┌─────────────────┐    │
│   │  Character  │                              │   Token Stream  │    │
│   │   Stream    │ ─────────────────────────►   │  <token, attr>  │    │
│   │ (Source)    │          SCANNER             │                 │    │
│   └─────────────┘                              └─────────────────┘    │
│          │                                              │             │
│          │         ┌─────────────────────┐              │             │
│          └────────►│   SYMBOL TABLE      │◄─────────────┘             │
│                    │  (Insert/Lookup)    │                            │
│                    └─────────────────────┘                            │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 🧠 Analogy: The Tokenizer Chef
Imagine you're a chef reading a recipe:
- **Character stream:** "A-D-D 2 C-U-P-S S-U-G-A-R"
- **Lexemes:** "ADD", "2", "CUPS", "SUGAR"
- **Tokens:** <VERB, ADD>, <NUMBER, 2>, <UNIT, CUPS>, <INGREDIENT, SUGAR>

---

## 2.2 Key Terminology

### 🔑 The Three Pillars

| Term | Definition | Example |
|------|------------|---------|
| **Token** | A pair of token-name and optional attribute-value | `<id, ptr_to_symbol_table>` |
| **Pattern** | A rule describing the set of lexemes for a token | `letter(letter\|digit)*` |
| **Lexeme** | Actual character sequence matching a pattern | `position`, `rate`, `initial` |

### Example
```c
int count = 100;
```

| Lexeme | Token | Pattern |
|--------|-------|---------|
| `int` | `<keyword, INT>` | "int" (exact match) |
| `count` | `<id, ptr>` | letter(letter\|digit)* |
| `=` | `<assign_op>` | "=" |
| `100` | `<num, 100>` | digit+ |
| `;` | `<semicolon>` | ";" |

---

## 2.3 Functions of Lexical Analyzer

### Primary Functions
1. **Read** source program character by character
2. **Group** characters into lexemes
3. **Produce** tokens for each lexeme
4. **Strip** whitespace and comments
5. **Keep track** of line numbers (for error reporting)
6. **Interact** with symbol table

### Secondary Functions
7. **Macro expansion** (in some compilers)
8. **Include file** processing

---

## 2.4 Token Types

### Standard Token Categories

| Token Type | Description | Examples |
|------------|-------------|----------|
| **Keywords** | Reserved words | `if`, `else`, `while`, `for` |
| **Identifiers** | User-defined names | `count`, `sum`, `main` |
| **Constants** | Literal values | `100`, `3.14`, `'a'` |
| **Operators** | Symbols for operations | `+`, `-`, `*`, `/`, `<=` |
| **Punctuation** | Separators | `;`, `,`, `(`, `)`, `{`, `}` |
| **Strings** | Character sequences | `"hello"`, `"world"` |

---

## 2.5 Regular Expressions (Foundation)

### Why Regular Expressions?
Regular Expressions (RE) are used to **specify patterns** for tokens.

### Basic Operations

| Operation | Symbol | Meaning | Example |
|-----------|--------|---------|---------|
| **Concatenation** | (implicit) | xy = x followed by y | `ab` matches "ab" |
| **Union/Alternation** | `\|` | x or y | `a\|b` matches "a" or "b" |
| **Kleene Closure** | `*` | Zero or more | `a*` matches "", "a", "aa", ... |
| **Positive Closure** | `+` | One or more | `a+` matches "a", "aa", "aaa", ... |
| **Optional** | `?` | Zero or one | `a?` matches "" or "a" |

### Precedence (Highest to Lowest)
1. `*` (Kleene star), `+`, `?`
2. Concatenation
3. `|` (Union)

### 🎯 GATE Trap Alert!
**Q:** What does `(a|b)*abb` match?
**A:** Any string of a's and b's that **ends with** "abb"
- Matches: "abb", "aabb", "babb", "aaabb", "ababb"
- Doesn't match: "ab", "aab", "abba"

### Common Token Patterns

| Token | Regular Expression |
|-------|-------------------|
| Identifier | `letter(letter\|digit)*` |
| Integer | `digit+` |
| Float | `digit+.digit+` |
| Signed Integer | `(+\|-)?digit+` |
| Whitespace | `( \|\t\|\n)+` |
| Comment (C-style) | `/\*[^*]*\*/` |

---

## 2.6 Regular Expression to NFA (Thompson's Construction)

### Thompson's Algorithm
Converts Regular Expression → NFA (Non-deterministic Finite Automaton)

### Basic Building Blocks

#### 1. For symbol `a`:
```
    ┌───┐  a   ┌───┐
───►│ i │─────►│ f │
    └───┘      └───┘
```

#### 2. For `ε` (epsilon):
```
    ┌───┐  ε   ┌───┐
───►│ i │─────►│ f │
    └───┘      └───┘
```

#### 3. For `r₁ | r₂` (Union):
```
              ┌───────────────┐
          ε   │     NFA(r₁)   │  ε
        ┌────►│  i₁ ──► f₁    │─────┐
        │     └───────────────┘     │
    ┌───┤                           ├───┐
───►│ i │                           │ f │
    └───┤                           ├───┘
        │     ┌───────────────┐     │
        └────►│     NFA(r₂)   │─────┘
          ε   │  i₂ ──► f₂    │  ε
              └───────────────┘
```

#### 4. For `r₁r₂` (Concatenation):
```
    ┌───────────────┐     ┌───────────────┐
───►│     NFA(r₁)   │────►│     NFA(r₂)   │
    │  i₁ ──► f₁    │  ε  │  i₂ ──► f₂    │
    └───────────────┘     └───────────────┘
```

#### 5. For `r*` (Kleene Closure):
```
                    ε
              ┌───────────────┐
              │  ┌─────────┐  │
              │  ▼         │  │
    ┌───┐  ε  │  ┌───────────────┐  ε  ┌───┐
───►│ i │────►│  │   NFA(r)      │────►│ f │
    └───┘     │  │   i₁ ──► f₁   │     └───┘
              │  └───────────────┘  │
              │                     │
              └───────────────────────┘
                         ε
```

### Example: NFA for `(a|b)*abb`

```
                    ε
         ┌──────────────────────────────────┐
         │                                  ▼
    ┌───►│◄──┐    ε     ┌───┐  a   ┌───┐    │    ┌───┐  a   ┌───┐  b   ┌───┐  b   ┌═══┐
───►│ 0 │    │─────────►│ 1 │─────►│ 2 │────┼───►│ 6 │─────►│ 7 │─────►│ 8 │─────►║ 9 ║
    └───┘    │    ε     └───┘      └───┘    │    └───┘      └───┘      └───┘      └═══┘
         │   │                    ε    │    │
         │   │   ε     ┌───┐  b   ┌───┘    │
         │   └────────►│ 3 │─────►│ 4 │◄────┘
         │             └───┘      └───┘
         │                          │
         │             ε            │
         └──────────────────────────┘
```

---

## 2.7 NFA to DFA (Subset Construction)

### The Algorithm
The **Subset Construction** (or **Powerset Construction**) converts NFA to DFA.

### Key Operations

| Operation | Symbol | Definition |
|-----------|--------|------------|
| **ε-closure(s)** | - | Set of states reachable from `s` using only ε-transitions |
| **ε-closure(T)** | - | Union of ε-closure(s) for all s in T |
| **move(T, a)** | - | Set of states reachable from T on input `a` |

### Algorithm Steps
```
1. Start state of DFA = ε-closure(start state of NFA)
2. For each unmarked state T in DFA:
   For each input symbol a:
     U = ε-closure(move(T, a))
     If U is new, add to DFA states
     Add transition T --a--> U
3. Mark T as processed
4. Repeat until no unmarked states
5. Final states = states containing NFA final state
```

### 🎯 GATE Critical Formula
**Maximum number of states in DFA derived from NFA with n states:**
$$\text{Max DFA states} = 2^n$$

**But in practice:** Usually much fewer!

### Example: Convert NFA to DFA for `(a|b)*abb`

Given NFA with states {0,1,2,3,4,5,6,7,8,9,10}:

**Step 1:** ε-closure({0}) = {0,1,2,4,7} = **State A**

**Step 2:** From A:
- move(A, a) → ε-closure = {1,2,3,4,6,7,8} = **State B**
- move(A, b) → ε-closure = {1,2,4,5,6,7} = **State C**

**Continue for all states...**

```
DFA:
         a
    ┌─────────┐
    ▼         │        a          a          b
┌═══════┐     │    ┌───────┐  ┌───────┐  ┌═══════┐
║   A   ║─────┴───►│   B   │─►│   C   │─►║   D   ║
└═══════┘          └───────┘  └───────┘  └═══════┘
    │  b              │ b         │ b        │ a,b
    ▼                 ▼           ▼          ▼
   ...               ...         ...        ...
```

---

## 2.8 DFA Minimization (Partition Algorithm)

### Why Minimize?
- Reduce number of states
- Reduce memory usage
- Faster execution

### Myhill-Nerode Theorem
Two states are **equivalent** if for every input string, they either both reach accepting states or both reach non-accepting states.

### Algorithm (Table-Filling Method)
1. **Initial Partition:**
   - P₀ = {Final states, Non-final states}
   
2. **Refinement:**
   - For each partition, check if states can be distinguished
   - Split if on any input, states go to different partitions
   
3. **Repeat** until no more splits possible

### 🎯 GATE Formula
For DFA with n states:
- **Minimum states** = Number of distinguishable states
- Use **Table Filling Method** or **Partition Refinement**

### Example
```
Given DFA:
States: {A, B, C, D, E}
Final: {C, D, E}
Non-final: {A, B}

Initial partition: P₀ = {{A,B}, {C,D,E}}

After checking transitions:
If A and B go to same partition on all inputs → keep together
If not → split

Final: P = {{A}, {B}, {C,D}, {E}}
Minimum states = 4
```

---

## 2.9 Lex: The Lexical Analyzer Generator

### Structure of Lex Program
```lex
%{
/* C declarations and includes */
#include <stdio.h>
%}

/* Definitions section */
DIGIT   [0-9]
LETTER  [a-zA-Z]

%%
/* Rules section */
{LETTER}({LETTER}|{DIGIT})*  { printf("ID: %s\n", yytext); }
{DIGIT}+                      { printf("NUM: %s\n", yytext); }
"if"                          { return IF; }
"else"                        { return ELSE; }
"+"                           { return PLUS; }
"-"                           { return MINUS; }
[ \t\n]                       { /* ignore whitespace */ }
.                             { printf("Unknown: %s\n", yytext); }
%%

/* User code section */
int main() {
    yylex();
    return 0;
}
```

### Important Lex Variables

| Variable | Purpose |
|----------|---------|
| `yytext` | Pointer to matched lexeme |
| `yyleng` | Length of matched lexeme |
| `yylval` | Value associated with token |
| `yylex()` | Main scanning function |

### Lex Conflict Resolution Rules
1. **Longest match wins** - Always prefer longer lexeme
2. **Earlier rule wins** - If same length, first rule in file

### 🎯 GATE Trap: Lex Matching
```lex
"if"    { return IF; }
[a-z]+  { return ID; }
```
**Input:** `ifelse`
**What matches?**
**A:** `ifelse` matches as ID (longest match), NOT `if` as keyword!

---

## 2.10 Finite Automata Variants

### DFA vs NFA Comparison

| Property | DFA | NFA |
|----------|-----|-----|
| **Transitions** | Exactly one per symbol | Zero, one, or more |
| **ε-transitions** | Not allowed | Allowed |
| **States at once** | Always one | Can be multiple |
| **Space** | Up to 2ⁿ states | n states |
| **Time** | O(n) per character | O(n²) per character |
| **Construction** | From NFA | From RE |

### ε-NFA (NFA with ε-transitions)
- Can move between states without reading input
- Useful for combining multiple NFAs

---

## 2.11 Important Algorithms & Complexities

### Conversion Algorithms

| Conversion | Algorithm | Time Complexity |
|------------|-----------|-----------------|
| RE → NFA | Thompson's | O(n) |
| NFA → DFA | Subset Construction | O(2ⁿ) worst case |
| DFA → Minimal DFA | Partition Algorithm | O(n² · |Σ|) |
| DFA → RE | State Elimination | O(n³ · 4ⁿ) |

### 🎯 GATE Formula: State Count

| Given | Maximum States |
|-------|----------------|
| NFA with n states | DFA ≤ 2ⁿ states |
| RE with n operators | NFA ≤ 2n states |
| DFA with n states | Minimal DFA ≤ n states |

---

## 2.12 Input Buffering Techniques

### Why Buffering?
Reading one character at a time from disk is **slow**. Buffering reads blocks at a time.

### Double Buffering Scheme
```
┌───────────────────────────────────────────────────────────────────┐
│                         BUFFER PAIRS                              │
├─────────────────────────────────┬─────────────────────────────────┤
│          Buffer 1               │          Buffer 2               │
│  ┌───┬───┬───┬───┬───┬───┬eof  │  ┌───┬───┬───┬───┬───┬───┬eof  │
│  │ i │ n │ t │   │ x │ = │     │  │ 1 │ 0 │ 0 │ ; │   │   │     │
│  └───┴───┴───┴───┴───┴───┴───┘ │  └───┴───┴───┴───┴───┴───┴───┘ │
│            ▲                    │                                 │
│            │                    │                                 │
│         lexeme_beginning        │                                 │
│                   ▲             │                                 │
│                   │             │                                 │
│                forward          │                                 │
└─────────────────────────────────┴─────────────────────────────────┘
```

### Sentinel Character
- Use special `eof` marker at buffer end
- Reduces comparisons needed

### Algorithm
```
1. Initialize: lexeme_beginning = forward = start of buffer
2. Advance forward to find token end
3. If forward reaches end:
   - If buffer not at EOF, reload other buffer
   - Switch to other buffer
4. When token found:
   - Return lexeme from lexeme_beginning to forward-1
   - Move lexeme_beginning to forward
```

---

## 2.13 Error Handling in Lexical Analysis

### Types of Lexical Errors
1. **Illegal characters:** Characters not in the alphabet
2. **Malformed tokens:** Invalid number format, unclosed strings
3. **Buffer overflow:** Identifier too long

### Error Recovery Strategies

| Strategy | Description | Example |
|----------|-------------|---------|
| **Panic Mode** | Delete characters until valid token found | Most common |
| **Delete** | Remove the erroneous character | Simple |
| **Insert** | Add missing character | Context-dependent |
| **Replace** | Substitute one character | Spelling correction |
| **Transpose** | Swap adjacent characters | "teh" → "the" |

---

## 2.14 Solved Examples

### Example 1: Token Recognition
**Input:** `int x = 10 + y;`

**Output:**
```
<keyword, int>
<id, x>
<assign, =>
<num, 10>
<plus, +>
<id, y>
<semicolon, ;>
```

### Example 2: RE to NFA
**RE:** `a*b+`

**NFA Construction:**
1. Build NFA for `a*`:
```
        ε
    ┌───────┐
    ▼       │
┌───┐ a ┌───┘
│ 1 │───│ 2 │
└───┘   └───┘
    └──ε──┘
```

2. Build NFA for `b+`:
```
    ┌───────┐
    │   b   │
    ▼       │
┌───┐   ┌───┘
│ 3 │───│ 4 │
└───┘   └───┘
```

3. Concatenate:
```
        ε
    ┌───────┐
    ▼       │        ε          ┌───────┐
┌───┐ a ┌───┘   ┌───┐   ┌───┐  │   b   │  ┌═══┐
│ 1 │───│ 2 │───│   │───│ 3 │──┴───│ 4 │──║ 5 ║
└───┘   └───┘   └───┘   └───┘      └───┘  └═══┘
    └──ε──┘              │         │
                         └────ε────┘
```

### Example 3: ε-closure Computation
**Given NFA:**
```
        ε       a       ε
    ┌───┐   ┌───┐   ┌───┐   ┌───┐
───►│ 1 │──►│ 2 │──►│ 3 │──►│ 4 │
    └───┘   └───┘   └───┘   └───┘
        └────ε────►
```

**ε-closure(1) = {1, 2, 3}** (all states reachable via ε from 1)
**ε-closure(2) = {2}** (no ε-transitions from 2)
**ε-closure(3) = {3, 4}** (3 and 4 via ε)

---

## 2.15 GATE Previous Year Patterns

### Pattern 1: NFA to DFA State Count
**Q:** An NFA has n states. What is the maximum number of states in equivalent DFA?
**A:** 2ⁿ (but usually much less in practice)

### Pattern 2: Minimum DFA States
**Q:** Find minimum DFA for language L = {w | w ends with "ab"}
**Approach:**
1. Draw NFA → Convert to DFA → Minimize
2. Or use Myhill-Nerode theorem directly

### Pattern 3: RE Interpretation
**Q:** Which strings are accepted by `(0|1)*01`?
**A:** All binary strings ending in "01"

### Pattern 4: Lex Precedence
**Q:** Given Lex rules, what token is returned for input X?
**Use rules:** Longest match first, then order in file

---

## 📝 Quick Revision Points

1. **Lexical Analyzer:** Characters → Tokens
2. **Token = <name, attribute>** 
3. **Lexeme:** Actual string matched
4. **Pattern:** Rule describing lexeme set (RE)
5. **Thompson's:** RE → NFA (O(n))
6. **Subset Construction:** NFA → DFA (O(2ⁿ))
7. **Minimization:** DFA → Minimal DFA
8. **Max DFA states from n-state NFA:** 2ⁿ
9. **Lex:** Longest match wins, then first rule
10. **Double buffering:** Efficient character reading

---

## 🧠 Mnemonic Summary

### Token vs Lexeme vs Pattern
> **"TLP: Token is Label, Lexeme is Literal, Pattern is Program"**

### NFA to DFA Steps
> **"Every Monkey Eats Coconuts"**
> - **E**psilon closure
> - **M**ove on symbol
> - **E**psilon closure again
> - **C**ontinue for all symbols

### DFA Minimization
> **"Partition Final from Non-Final, then Refine"**

---

## ✅ Self-Assessment Questions

1. What is the difference between token, lexeme, and pattern?
2. Convert RE `(a|b)*abb` to NFA using Thompson's construction.
3. Convert the NFA from Q2 to DFA using subset construction.
4. Minimize the DFA from Q3.
5. Write a Lex program to recognize integers and identifiers.

---

**Next Chapter:** [Syntax Analysis →](03-Syntax-Analysis.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
