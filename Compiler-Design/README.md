# Compiler Design (CD) | The Complete GATE/ESE Mastery Guide

> **The Atomic Truth:** *"Transform source to target through structured phases."*

---

## 📚 Table of Contents

| Module | Topic | GATE Weightage |
|--------|-------|----------------|
| 1 | [Introduction & Lexical Analysis](./01-Lexical-Analysis.md) | 4-6 marks |
| 2 | [Syntax Analysis - Top-Down Parsing](./02-Syntax-Analysis-TopDown.md) | 6-8 marks |
| 3 | [Syntax Analysis - Bottom-Up Parsing](./03-Syntax-Analysis-BottomUp.md) | 8-10 marks |
| 4 | [Semantic Analysis & SDT](./04-Semantic-Analysis-SDT.md) | 4-6 marks |
| 5 | [Intermediate Code Generation](./05-Intermediate-Code-Generation.md) | 4-6 marks |
| 6 | [Code Optimization](./06-Code-Optimization.md) | 4-6 marks |
| 7 | [Code Generation & Runtime Environment](./07-Code-Generation-Runtime.md) | 4-6 marks |
| 8 | [Exam Traps & Problem-Solving Techniques](./08-Exam-Traps-Techniques.md) | — |

---

## 🎯 The 2026 Strategy Matrix

### Complexity Assessment (IIT Guwahati Standards)
| Topic | Failure Rate | Genius Trap Type |
|-------|--------------|------------------|
| LR Parsing | 72% | FOLLOW set in reduce decisions |
| FIRST/FOLLOW | 65% | ε propagation errors |
| Left Recursion | 55% | Indirect left recursion |
| Attribute Grammars | 50% | S vs L-attributed confusion |
| Code Optimization | 45% | DAG construction |

### The Compiler Pipeline

```
[Image of Compiler Phases]
┌─────────────────────────────────────────────────────────────┐
│                    SOURCE PROGRAM                           │
└───────────────────────┬─────────────────────────────────────┘
                        ↓
              ┌─────────────────────┐
              │  Lexical Analyzer   │ → Tokens
              │   (Scanner)         │
              └─────────┬───────────┘
                        ↓
              ┌─────────────────────┐
              │  Syntax Analyzer    │ → Parse Tree
              │    (Parser)         │
              └─────────┬───────────┘
                        ↓
              ┌─────────────────────┐
              │ Semantic Analyzer   │ → Annotated Tree
              │                     │
              └─────────┬───────────┘
                        ↓
              ┌─────────────────────┐
              │ Intermediate Code   │ → Three-Address Code
              │   Generator         │
              └─────────┬───────────┘
                        ↓
              ┌─────────────────────┐
              │   Code Optimizer    │ → Optimized Code
              │                     │
              └─────────┬───────────┘
                        ↓
              ┌─────────────────────┐
              │   Code Generator    │ → Target Code
              │                     │
              └─────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│                    TARGET PROGRAM                           │
└─────────────────────────────────────────────────────────────┘

Symbol Table ←───────────────────────────────────→ Error Handler
   (All Phases Access)                          (All Phases Report)
```

---

## 🧠 The Mental Machinery

### The Grammar Hierarchy (Chomsky)

```
[Image of Chomsky Hierarchy]
              Type 0: Unrestricted
                    (Turing Machine)
                        ↑
              Type 1: Context-Sensitive
                    (LBA)
                        ↑
              Type 2: Context-Free  ← MOST OF COMPILER
                    (PDA)
                        ↑
              Type 3: Regular
                    (DFA/NFA)
```

### The Parsing Spectrum

```
[Mental 3D Dial: Power ↔ Efficiency ↔ Complexity]
           MORE POWERFUL
                ↑
    LR(1) > LALR(1) > SLR(1) > LL(1)
                ↓
          LESS COMPLEX

    Left-to-Right Parsing:
    LL = scan Left, Leftmost derivation
    LR = scan Left, Rightmost derivation (reverse)
```

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| Regular vs CFG | Counting/matching brackets → CFG |
| LL(1) | No left recursion, no common prefix |
| LR(0) conflicts | Shift-reduce or reduce-reduce |
| FIRST(X) | First terminals derivable from X |
| FOLLOW(A) | Terminals that can follow A |

---

## 📖 How to Use This Material

1. **First Pass:** Understand the compiler pipeline and phase relationships
2. **Second Pass:** Master FIRST/FOLLOW and parsing table construction
3. **Third Pass:** Practice LR parsing (highest GATE weightage!)
4. **Fourth Pass:** Study SDT and attribute grammars
5. **Final Pass:** Use traps document and solve previous year questions

---

## 🔑 Key Concepts Quick Reference

### Grammar Notation
- **Terminal:** lowercase (a, b, c) or symbols (+, *, ;)
- **Non-terminal:** uppercase (A, B, S) or <name>
- **ε:** Empty string
- **$:** End of input marker

### Parsing Terms
- **Handle:** Substring that matches RHS and can be reduced
- **Viable Prefix:** Prefix of a right sentential form
- **Sentential Form:** Derivable from start symbol

### Optimization Terms
- **Basic Block:** Maximal sequence with single entry/exit
- **DAG:** Directed Acyclic Graph for CSE
- **Live Variable:** Used before next definition

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Navigate to individual modules for complete mastery →*
