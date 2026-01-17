# Chapter 1: Introduction to Compilers

## 🎯 The Atomic Truth
> **"Compiler = Translator from Human to Machine"**

---

## 1.1 What is a Compiler?

### Definition
A **compiler** is a program that translates a program written in a **source language** (high-level) into an equivalent program in a **target language** (low-level/machine code).

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Source    │ ──────► │   COMPILER   │ ──────► │   Target    │
│   Program   │         │              │         │   Program   │
│  (C, Java)  │         │              │         │ (Assembly/  │
│             │         │              │         │  Machine)   │
└─────────────┘         └──────────────┘         └─────────────┘
                               │
                               ▼
                        ┌─────────────┐
                        │   Error     │
                        │  Messages   │
                        └─────────────┘
```

### 🧠 Analogy: The Universal Translator
Think of a compiler as a **human translator** at the UN:
- **Source Language:** French (what the speaker says)
- **Target Language:** English (what the listener hears)
- **Compiler:** The translator (converts French → English)
- **Error Messages:** "I didn't understand that idiom"

---

## 1.2 Compiler vs Interpreter vs Assembler

### The Big Picture

| Feature | Compiler | Interpreter | Assembler |
|---------|----------|-------------|-----------|
| **Input** | High-level language | High-level language | Assembly language |
| **Output** | Machine code | Executes directly | Machine code |
| **Translation** | Entire program at once | Line by line | One-to-one |
| **Speed** | Fast execution (after compilation) | Slow execution | Fast execution |
| **Error Detection** | All at once | One at a time | All at once |
| **Memory** | Needs more memory | Less memory | Less memory |
| **Examples** | C, C++, Go | Python, JavaScript, Ruby | MASM, NASM |

### 🎯 GATE Trap Alert!
**Q:** Which is faster - compiled code or interpreted code?
**A:** **Compiled code** is faster during execution, but interpretation is faster for quick testing/debugging.

### The Hybrid Approach (Java)
```
┌────────────┐      ┌──────────┐      ┌────────────┐      ┌─────────┐
│   Java     │ ──►  │  javac   │ ──►  │  Bytecode  │ ──►  │   JVM   │
│  Source    │      │(Compiler)│      │ (.class)   │      │ (Interp)|
└────────────┘      └──────────┘      └────────────┘      └─────────┘
```

---

## 1.3 Phases of a Compiler (THE MOST IMPORTANT TOPIC)

### The 6 Phases - Memory Trick: **"Lexical Syntax Semantic, Intermediate Optimize Generate"**
### Mnemonic: **"Lazy Students Study In Oral Games"**
- **L**exical Analysis
- **S**yntax Analysis
- **S**emantic Analysis
- **I**ntermediate Code Generation
- **O**ptimization
- **G**eneration (Code)

```
                            ┌─────────────────┐
                            │  Source Code    │
                            └────────┬────────┘
                                     │
┌────────────────────────────────────┼────────────────────────────────────┐
│                                    ▼                                    │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │          PHASE 1: LEXICAL ANALYZER (SCANNER)                     │  │
│  │  ────────────────────────────────────────────                    │  │
│  │  • Reads character stream                                        │  │
│  │  • Groups into lexemes                                           │  │
│  │  • Produces tokens: <token-name, attribute-value>                │  │
│  │  • Removes whitespace and comments                               │  │
│  │  • Error: "Unrecognized token"                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                    │                                    │
│                                    ▼                                    │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │          PHASE 2: SYNTAX ANALYZER (PARSER)                       │  │
│  │  ────────────────────────────────────────────                    │  │
│  │  • Takes token stream                                            │  │
│  │  • Creates Parse Tree (Syntax Tree)                              │  │
│  │  • Checks grammatical structure                                  │  │
│  │  • Uses: CFG, Parsing algorithms                                 │  │
│  │  • Error: "Syntax error at line X"                               │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                    │                                    │
│                                    ▼                                    │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │          PHASE 3: SEMANTIC ANALYZER                              │  │
│  │  ────────────────────────────────────────────                    │  │
│  │  • Type checking                                                 │  │
│  │  • Scope resolution                                              │  │
│  │  • Produces Annotated Parse Tree                                 │  │
│  │  • Error: "Type mismatch", "Undeclared variable"                 │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                    │                                    │
│  ═══════════════════════════════════════════════════════════════════   │
│              ▲  FRONT END (Analysis)  │  BACK END (Synthesis)  ▼       │
│  ═══════════════════════════════════════════════════════════════════   │
│                                    │                                    │
│                                    ▼                                    │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │          PHASE 4: INTERMEDIATE CODE GENERATOR                    │  │
│  │  ────────────────────────────────────────────                    │  │
│  │  • Produces machine-independent code                             │  │
│  │  • Three Address Code (TAC)                                      │  │
│  │  • Makes optimization easier                                     │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                    │                                    │
│                                    ▼                                    │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │          PHASE 5: CODE OPTIMIZER                                 │  │
│  │  ────────────────────────────────────────────                    │  │
│  │  • Improves intermediate code                                    │  │
│  │  • Removes redundancy                                            │  │
│  │  • Loop optimization                                             │  │
│  │  • Dead code elimination                                         │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                    │                                    │
│                                    ▼                                    │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │          PHASE 6: CODE GENERATOR                                 │  │
│  │  ────────────────────────────────────────────                    │  │
│  │  • Produces target machine code                                  │  │
│  │  • Register allocation                                           │  │
│  │  • Instruction selection                                         │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                    │                                    │
│      ┌─────────────────────────────┼─────────────────────────────┐     │
│      │                             │                             │     │
│      ▼                             │                             ▼     │
│ ┌──────────┐                       │                       ┌──────────┐│
│ │ SYMBOL   │◄──────────────────────┼───────────────────────│  ERROR   ││
│ │ TABLE    │  (Used by all phases) │ (Reports to all)      │ HANDLER  ││
│ │ MANAGER  │                       │                       │          ││
│ └──────────┘                       │                       └──────────┘│
└────────────────────────────────────┼────────────────────────────────────┘
                                     ▼
                            ┌─────────────────┐
                            │  Target Code    │
                            └─────────────────┘
```

---

## 1.4 Detailed Phase Example

### Input: `position = initial + rate * 60`

#### Phase 1: Lexical Analysis
```
Output: Token Stream
┌──────────────┬──────────────────────┐
│    Token     │   Attribute Value    │
├──────────────┼──────────────────────┤
│    id        │   pointer to "position" │
│    =         │   assignment operator│
│    id        │   pointer to "initial"  │
│    +         │   addition operator  │
│    id        │   pointer to "rate"     │
│    *         │   multiplication     │
│    num       │   60                 │
└──────────────┴──────────────────────┘

Token Stream: <id,1> <=> <id,2> <+> <id,3> <*> <num,60>
```

#### Phase 2: Syntax Analysis
```
                    =
                   / \
                  /   \
               id₁     +
             (position)/ \
                      /   \
                   id₂     *
                (initial) / \
                         /   \
                       id₃   60
                     (rate)
```

#### Phase 3: Semantic Analysis
```
                    =
                   / \
                  /   \
               id₁     +
             (position)/ \
                      /   \
                   id₂     *
                (initial) / \
                         /   \
                       id₃  inttofloat
                     (rate)    |
                              60
```
**Note:** `60` (int) → `inttofloat(60)` for type consistency

#### Phase 4: Intermediate Code Generation
```
t1 = inttofloat(60)
t2 = id3 * t1
t3 = id2 + t2
id1 = t3
```

#### Phase 5: Code Optimization
```
t1 = id3 * 60.0      // Converted at compile time
id1 = id2 + t1       // Reduced temporary variables
```

#### Phase 6: Code Generation
```assembly
LDF  R2, id3         ; Load rate into R2
MULF R2, R2, #60.0   ; R2 = rate * 60.0
LDF  R1, id2         ; Load initial into R1
ADDF R1, R1, R2      ; R1 = initial + (rate * 60.0)
STF  id1, R1         ; Store result in position
```

---

## 1.5 Front End vs Back End

```
┌─────────────────────────────────────────────────────────────────────┐
│                         FRONT END                                   │
│  ─────────────────────────────────────────────────────────────────  │
│  • Language Dependent                                               │
│  • Machine Independent                                              │
│  • Phases: Lexical, Syntax, Semantic, Intermediate                  │
│  • Focus: Analysis of source program                                │
└─────────────────────────────────────────────────────────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │   INTERMEDIATE CODE     │
                    │   (Bridge between)      │
                    └────────────┬────────────┘
                                 │
┌─────────────────────────────────────────────────────────────────────┐
│                         BACK END                                    │
│  ─────────────────────────────────────────────────────────────────  │
│  • Language Independent                                             │
│  • Machine Dependent                                                │
│  • Phases: Optimization, Code Generation                            │
│  • Focus: Synthesis of target program                               │
└─────────────────────────────────────────────────────────────────────┘
```

### Why This Division?
**Portability!**
- To support `n` languages and `m` machines:
  - Without division: Need `n × m` compilers
  - With division: Need `n` front-ends + `m` back-ends = `n + m` components

### 🎯 GATE Favorite Question
**Q:** How many compilers needed for 5 languages on 4 machines?
- **Without IR:** 5 × 4 = **20 compilers**
- **With IR:** 5 + 4 = **9 components** (5 front-ends + 4 back-ends)

---

## 1.6 Passes of a Compiler

### What is a Pass?
A **pass** is one complete scan of the source program or its representation.

### Single-Pass vs Multi-Pass Compiler

| Aspect | Single-Pass | Multi-Pass |
|--------|-------------|------------|
| **Memory** | Low (reads once) | High (stores intermediate) |
| **Speed** | Faster | Slower |
| **Optimization** | Limited | Extensive |
| **Forward Reference** | Problem | Handled |
| **Example** | Pascal compiler | C compiler |

### The Forward Reference Problem
```c
void main() {
    foo();      // Called before definition - FORWARD REFERENCE!
}

void foo() {
    printf("Hello");
}
```
- **Single-pass:** Cannot handle (doesn't know `foo` yet)
- **Multi-pass:** Pass 1 collects declarations, Pass 2 resolves references

---

## 1.7 Bootstrapping

### Definition
**Bootstrapping** is the technique of writing a compiler for a language using that language itself.

### The T-Diagram (Tombstone Diagram)
```
     ┌─────────────────┐
     │  Source    Target│
     │    S    →   T   │
     └────────┬────────┘
              │
       Implementation
         Language I
```

Meaning: Compiler written in language `I` that translates `S` to `T`

### The Bootstrapping Process

**Goal:** Create a compiler for language L in language L itself.

**Step 1:** Write a simple compiler for L in another language (say Assembly)
```
     ┌─────────────────┐
     │    L    →   M   │  (L to Machine code)
     └────────┬────────┘
              │
            ASM          (Written in Assembly)
```

**Step 2:** Write an improved compiler for L in L itself
```
     ┌─────────────────┐
     │    L    →   M   │
     └────────┬────────┘
              │
              L          (Written in L)
```

**Step 3:** Compile Step 2's compiler using Step 1's compiler
```
     ┌─────────────────┐          ┌─────────────────┐
     │    L    →   M   │          │    L    →   M   │
     └────────┬────────┘    =     └────────┬────────┘
              │                            │
              L                            M
              │
     ┌────────┴────────┐
     │    L    →   M   │
     └────────┬────────┘
              │
            ASM
```

### 🎯 GATE Question Pattern
**Given:** A compiler `C1` written in `A` that compiles `B` to `C`
**Question:** What happens when you run program `P` written in `B` through `C1`?

### Cross Compiler
A **cross compiler** runs on one machine but produces code for a different machine.
- **Use Case:** Compiling code for embedded systems on a desktop computer

```
     ┌─────────────────┐
     │    C    →  ARM  │
     └────────┬────────┘
              │
            x86          (Runs on x86, generates ARM code)
```

---

## 1.8 Compiler Construction Tools

| Tool | Purpose | Phase |
|------|---------|-------|
| **LEX / Flex** | Lexical Analyzer Generator | Lexical Analysis |
| **YACC / Bison** | Parser Generator | Syntax Analysis |
| **LLVM** | Complete Compiler Infrastructure | All phases |
| **GCC** | GNU Compiler Collection | All phases |

### LEX and YACC Workflow
```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│   ┌─────────┐        ┌─────────┐        ┌─────────────────────┐ │
│   │  RE     │        │   LEX   │        │   C code for        │ │
│   │ Patterns│  ───►  │         │  ───►  │   Lexical Analyzer  │ │
│   │ (.l)    │        │         │        │   (lex.yy.c)        │ │
│   └─────────┘        └─────────┘        └─────────────────────┘ │
│                                                                  │
│   ┌─────────┐        ┌─────────┐        ┌─────────────────────┐ │
│   │  CFG    │        │  YACC   │        │   C code for        │ │
│   │  Rules  │  ───►  │         │  ───►  │   Parser            │ │
│   │ (.y)    │        │         │        │   (y.tab.c)         │ │
│   └─────────┘        └─────────┘        └─────────────────────┘ │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 1.9 The Symbol Table

### What is it?
A **data structure** used by the compiler to store information about identifiers (variables, functions, classes).

### Information Stored

| Field | Description |
|-------|-------------|
| **Name** | Identifier name |
| **Type** | int, float, function, etc. |
| **Scope** | Local, global, block level |
| **Memory Location** | Address in memory |
| **Size** | Number of bytes |
| **Parameters** | For functions: parameter list |

### Symbol Table Operations
- `insert(name, info)` - Add new identifier
- `lookup(name)` - Search for identifier
- `delete(name)` - Remove identifier (for block exit)

### Implementation Methods
1. **Linear List:** O(n) search - Simple but slow
2. **Hash Table:** O(1) average search - **Most Common**
3. **Binary Search Tree:** O(log n) search

### 🎯 GATE Trap
**Q:** Which phase creates entries in the symbol table?
**A:** **Lexical Analyzer** creates entries, but **Semantic Analyzer** fills in the details (type, scope).

---

## 1.10 Cousins of the Compiler

### 1. Preprocessor
- Handles `#include`, `#define`, `#ifdef`
- Runs **before** compilation
- Macro expansion

### 2. Assembler
- Converts assembly language → machine code
- One-to-one translation
- Handles symbolic addresses

### 3. Linker
- Combines multiple object files into one executable
- Resolves external references
- Static linking

### 4. Loader
- Loads executable into memory
- Relocates addresses
- Starts execution

### Complete Flow
```
┌──────────┐    ┌──────────────┐    ┌──────────┐    ┌───────────┐
│  Source  │───►│ Preprocessor │───►│ Compiler │───►│ Assembler │
│  Code    │    │              │    │          │    │           │
└──────────┘    └──────────────┘    └──────────┘    └─────┬─────┘
                                                          │
                                                          ▼
┌──────────┐    ┌──────────────┐    ┌──────────────────────────┐
│ Running  │◄───│    Loader    │◄───│    Linker/Link Editor    │
│ Program  │    │              │    │   (with Library files)   │
└──────────┘    └──────────────┘    └──────────────────────────┘
```

---

## 🎯 GATE Previous Year Questions Pattern

### Type 1: Phase Identification
**Q:** "Syntax error at line 5" - Which phase reports this?
**A:** Syntax Analyzer (Parser)

### Type 2: Error Detection
**Q:** "Undeclared variable x" - Which phase detects this?
**A:** Semantic Analyzer

### Type 3: Bootstrapping
**Q:** Given T-diagrams, find the output language.
**Approach:** Follow the chain of compilation.

### Type 4: Front-End/Back-End
**Q:** Which phase is machine dependent?
**A:** Code Generator (Back-end)

---

## 📝 Key Points for Quick Revision

1. **6 Phases:** Lexical → Syntax → Semantic → Intermediate → Optimization → Code Gen
2. **Front End:** Language dependent, Machine independent
3. **Back End:** Language independent, Machine dependent
4. **Symbol Table:** Used by ALL phases (central database)
5. **Single Pass:** Fast but limited optimization
6. **Multi Pass:** Slow but better optimization
7. **LEX:** Generates Lexical Analyzer from RE
8. **YACC:** Generates Parser from CFG
9. **Bootstrapping:** Writing compiler in its own language
10. **Cross Compiler:** Runs on machine A, generates code for machine B

---

## 🧠 Mnemonic Summary

### The 6 Phases
> **"Lazy Students Study In Old Gardens"**
> - **L**exical Analysis
> - **S**yntax Analysis  
> - **S**emantic Analysis
> - **I**ntermediate Code Generation
> - **O**ptimization
> - Code **G**eneration

### Error Types by Phase
> **"Lex catches typos, Syn catches structure, Sem catches meaning"**

---

## ✅ Self-Assessment Questions

1. What is the difference between a compiler and an interpreter?
2. Draw the phase diagram of a compiler.
3. What is the purpose of intermediate code?
4. Explain bootstrapping with T-diagrams.
5. Why is the symbol table called the "central repository"?

---

**Next Chapter:** [Lexical Analysis →](02-Lexical-Analysis.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Foundation Established.*
