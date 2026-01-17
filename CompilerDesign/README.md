# 🔥 COMPILER DESIGN | GATE • ESE • PSU • BANK
## **The Sovereign Master Guide for Rank-1 Domination**

---

> **"A compiler transforms your high-level dreams into machine-level reality."**

This is the **ULTIMATE A-Z Compiler Design Study Material** - engineered for those who don't just want to pass, but want to **OWN** the exam.

---

## 📚 Table of Contents

| Chapter | Topic | GATE Weightage |
|---------|-------|----------------|
| 1 | [Introduction to Compilers](01-Introduction-to-Compilers.md) | 2-3 marks |
| 2 | [Lexical Analysis](02-Lexical-Analysis.md) | 4-6 marks |
| 3 | [Syntax Analysis - Parsing](03-Syntax-Analysis.md) | 8-12 marks |
| 4 | [Syntax Directed Translation](04-Syntax-Directed-Translation.md) | 4-6 marks |
| 5 | [Intermediate Code Generation](05-Intermediate-Code-Generation.md) | 3-5 marks |
| 6 | [Runtime Environment](06-Runtime-Environment.md) | 3-5 marks |
| 7 | [Code Optimization](07-Code-Optimization.md) | 3-5 marks |
| 8 | [Code Generation](08-Code-Generation.md) | 2-4 marks |
| 9 | [Error Handling](09-Error-Handling.md) | 1-2 marks |
| 10 | [Quick Revision & Formulas](10-Quick-Revision.md) | - |
| 11 | [Previous Year Questions](11-Previous-Year-Questions.md) | - |

---

## 🎯 GATE 2026 Strategy for Compiler Design

### Weightage Analysis
- **Total Expected Marks:** 10-15 marks
- **Number of Questions:** 4-6 questions
- **Difficulty:** Medium to High
- **Most Important Topics:**
  1. Parsing (LR, LL, FIRST/FOLLOW) - **MUST MASTER**
  2. Lexical Analysis (DFA/NFA, RE) - **HIGH FREQUENCY**
  3. SDT & Intermediate Code - **MODERATE**
  4. Runtime Environment - **TRICKY QUESTIONS**

### The 80/20 Rule for Compiler Design
Focus 80% of your energy on:
1. **Parsing Tables Construction** (SLR, CLR, LALR, LL(1))
2. **FIRST and FOLLOW Computation**
3. **Regular Expression ↔ Finite Automata**
4. **Activation Records & Parameter Passing**

---

## 🧠 The Compiler Pipeline (Mental Model)

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        SOURCE CODE (High-Level)                          │
└──────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  PHASE 1: LEXICAL ANALYSIS (Scanner)                                     │
│  ─────────────────────────────────────                                   │
│  • Input: Character Stream                                               │
│  • Output: Token Stream                                                  │
│  • Tool: LEX, Flex                                                       │
│  • Uses: Regular Expressions, DFA                                        │
└──────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  PHASE 2: SYNTAX ANALYSIS (Parser)                                       │
│  ─────────────────────────────────────                                   │
│  • Input: Token Stream                                                   │
│  • Output: Parse Tree / Syntax Tree                                      │
│  • Tool: YACC, Bison                                                     │
│  • Uses: CFG, Parsing Algorithms                                         │
└──────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  PHASE 3: SEMANTIC ANALYSIS                                              │
│  ─────────────────────────────────────                                   │
│  • Input: Parse Tree                                                     │
│  • Output: Annotated Parse Tree                                          │
│  • Checks: Type checking, Scope resolution                               │
│  • Uses: Symbol Table, SDT                                               │
└──────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  PHASE 4: INTERMEDIATE CODE GENERATION                                   │
│  ─────────────────────────────────────                                   │
│  • Input: Annotated Parse Tree                                           │
│  • Output: Three Address Code (TAC)                                      │
│  • Forms: Quadruples, Triples, Indirect Triples                         │
└──────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  PHASE 5: CODE OPTIMIZATION                                              │
│  ─────────────────────────────────────                                   │
│  • Input: Intermediate Code                                              │
│  • Output: Optimized Intermediate Code                                   │
│  • Types: Machine Independent Optimizations                              │
└──────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  PHASE 6: CODE GENERATION                                                │
│  ─────────────────────────────────────                                   │
│  • Input: Optimized Intermediate Code                                    │
│  • Output: Target Machine Code                                           │
│  • Tasks: Register Allocation, Instruction Selection                    │
└──────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                        TARGET CODE (Machine-Level)                       │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 🔑 Golden Rules of Compiler Design

### Rule 1: **The Phase Hierarchy**
```
Lexical < Syntax < Semantic < Intermediate < Optimization < Generation
(Simple)                                                      (Complex)
```

### Rule 2: **Error Detection Phases**
| Error Type | Detected By |
|------------|-------------|
| Spelling errors in identifiers | Lexical Analyzer |
| Missing semicolons, brackets | Syntax Analyzer |
| Type mismatches | Semantic Analyzer |
| Logical errors | Cannot be detected by compiler |

### Rule 3: **The Symbol Table Connection**
- Used by ALL phases except Lexical Analysis (though it populates it)
- It's the **central database** of the compiler

---

## ⚡ Quick Start: What You MUST Know Before Each Topic

1. **Before Lexical Analysis:** Finite Automata, Regular Expressions
2. **Before Syntax Analysis:** Context-Free Grammars, Derivations
3. **Before SDT:** Parse Trees, Attributes
4. **Before Code Optimization:** Basic Block identification
5. **Before Code Generation:** Assembly language basics

---

## 📖 How to Use This Material

1. **First Pass:** Read theory + understand "Why" behind each concept
2. **Second Pass:** Solve examples, understand "How"
3. **Third Pass:** Focus on tricks, edge cases, traps
4. **Fourth Pass:** Previous year questions
5. **Final Pass:** Quick revision notes only

---

**Start your journey:** [Chapter 1: Introduction to Compilers →](01-Introduction-to-Compilers.md)

---

*Created for GATE 2026 | ESE | PSU | BANK Aspirants*
*Version 1.0 | Last Updated: January 2026*
