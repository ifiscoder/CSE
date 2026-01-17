# Chapter 8: Code Generation

## 🎯 The Atomic Truth
> **"Code Generator = IR → Target Machine Code"**

---

## 8.1 What is Code Generation?

### Definition
**Code Generation** is the final phase of a compiler that transforms optimized intermediate representation into target machine code or assembly language.

```
┌────────────────────────────────────────────────────────────────────────┐
│                       CODE GENERATION                                  │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   ┌─────────────┐      ┌─────────────────┐      ┌─────────────────┐   │
│   │  Optimized  │      │     CODE        │      │    Target       │   │
│   │     IR      │ ──►  │   GENERATOR     │ ──►  │    Code         │   │
│   │    (TAC)    │      │                 │      │   (Assembly)    │   │
│   └─────────────┘      └─────────────────┘      └─────────────────┘   │
│                        • Register Allocation                          │
│                        • Instruction Selection                        │
│                        • Instruction Ordering                         │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### Main Tasks of Code Generator
1. **Instruction Selection:** Choose target instructions for IR operations
2. **Register Allocation:** Assign registers to variables
3. **Instruction Ordering:** Order instructions for efficiency

### 🧠 Analogy: The Blueprint to Building
IR is like architectural blueprints; code generator is the construction crew:
- **Instruction Selection:** Choose materials and methods
- **Register Allocation:** Assign workers to tasks
- **Instruction Ordering:** Schedule construction sequence

---

## 8.2 Issues in Code Generation

### 8.2.1 Input to Code Generator
- Intermediate representation (TAC, DAG)
- Symbol table information
- Target machine description

### 8.2.2 Target Programs
| Form | Description | Use Case |
|------|-------------|----------|
| **Absolute Machine Code** | Fixed memory addresses | Embedded systems |
| **Relocatable Machine Code** | Relative addresses | Linkable modules |
| **Assembly Code** | Symbolic instructions | Debugging, portability |

### 8.2.3 Memory Management
- Determine addresses for variables
- Handle stack, heap allocation
- Generate memory access instructions

### 8.2.4 Instruction Selection
- Map IR operations to machine instructions
- Consider instruction costs
- Handle special cases (addressing modes)

### 8.2.5 Register Allocation
- Map variables to registers
- Minimize memory accesses
- Handle register spilling

### 8.2.6 Evaluation Order
- Order operations to minimize registers needed
- Consider dependencies and parallelism

---

## 8.3 Target Machine Model

### Simple Target Machine
```
┌──────────────────────────────────────────────────────────────────────┐
│                        SIMPLE MACHINE MODEL                          │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   Registers: R0, R1, R2, ..., Rn (general purpose)                  │
│                                                                      │
│   Instruction Format:                                                │
│   ┌────────────┬────────────┬────────────┐                          │
│   │   OPCODE   │   Source   │    Dest    │                          │
│   └────────────┴────────────┴────────────┘                          │
│                                                                      │
│   Addressing Modes:                                                  │
│   • Register:      Ri                                                │
│   • Indexed:       c(Ri)  = M[c + contents(Ri)]                     │
│   • Direct:        M      = M[address]                               │
│   • Indirect:      *Ri    = M[contents(Ri)]                         │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### Common Instructions

| Instruction | Meaning | Example |
|-------------|---------|---------|
| **MOV src, dst** | dst = src | MOV R1, R2 |
| **ADD src, dst** | dst = dst + src | ADD R1, R2 |
| **SUB src, dst** | dst = dst - src | SUB R1, R2 |
| **MUL src, dst** | dst = dst * src | MUL R1, R2 |
| **LD addr, R** | R = M[addr] | LD x, R1 |
| **ST R, addr** | M[addr] = R | ST R1, x |

### Instruction Costs
```
Cost model (simplified):
- Register operations:     1 unit
- Memory operations:       2 units (additional for address)
- Indirect operations:     3 units
```

---

## 8.4 Simple Code Generator

### Algorithm
For each TAC instruction, generate target code using register descriptor and address descriptor.

### Descriptors

**Register Descriptor:** For each register, tracks what it currently holds
```
R1: {x}        // R1 contains value of x
R2: {t1}       // R2 contains value of t1
R3: {empty}    // R3 is available
```

**Address Descriptor:** For each variable, tracks where its value is stored
```
x: {R1, memory}    // x is in R1 and memory
y: {R2}            // y is only in R2
z: {memory}        // z is only in memory
```

### The getReg Function
Selects a register for an operation. Strategies:
1. If variable already in register, use that
2. If empty register available, use that
3. Otherwise, spill a register (save to memory, use it)

### Code Generation for TAC

#### For `x = y op z`:
```
1. Invoke getReg(x = y op z) to get register Rx
2. Find location Ly of y:
   - If y in register Ry, use Ry
   - Otherwise, generate LD y, Ry
3. Generate: op Rz, Ry (or op z, Ry if z in memory)
4. Update descriptors
```

#### Example
**TAC:** `t = a - b`
```
Assuming: a in R0, b in R1

Generated code:
MOV R0, R2      // Copy a to R2 (don't destroy a)
SUB R1, R2      // R2 = R2 - R1 = a - b

Descriptors after:
R2: {t}
t: {R2}
```

### Code Generation Example

**TAC:**
```
t1 = a - b
t2 = a - c
t3 = t1 + t2
d = t3 + t2
```

**Generated Code (2 registers):**
```
Statement          Generated Code              Register Contents
─────────────────────────────────────────────────────────────────
                                               R0       R1
t1 = a - b         LD a, R0                    a
                   LD b, R1                    a        b
                   SUB R1, R0                  t1       b

t2 = a - c         LD a, R1                    t1       a
                   LD c, R1    (need c, spill) t1       c
                   // Wait, we need to preserve t1!
                   
Better approach:
t1 = a - b         LD a, R0                    a
                   LD b, R1                    b
                   SUB R1, R0                  a-b=t1   b

t2 = a - c         ST R0, t1  (save t1)        t1       b
                   LD a, R0                    a        b
                   LD c, R1                    a        c
                   SUB R1, R0                  a-c=t2   c

t3 = t1 + t2       LD t1, R1                   t2       t1
                   ADD R1, R0                  t2+t1=t3 t1

d = t3 + t2        // t2 already in R0, but wait...
```

---

## 8.5 Register Allocation and Assignment

### The Problem
- Variables (unlimited) → Registers (limited)
- Goal: Minimize memory accesses (loads/stores)

### Local Register Allocation (Within Basic Block)
Use **usage counts** to prioritize which variables get registers.

### Global Register Allocation
Use **graph coloring** on interference graph.

### Spilling
When not enough registers:
1. Select a variable to spill (live range splitting)
2. Store it to memory
3. Load when needed

### 🎯 GATE Formula: Spill Cost
```
Spill cost = Σ (uses + defs) × 10^(loop_nesting_depth)
```
Spill variables with lowest cost.

---

## 8.6 Instruction Selection by Tree Rewriting

### Concept
Represent IR as trees, match subtrees to instruction patterns.

### Example Patterns
```
Pattern 1: Register + Constant
    +
   / \
  Ri  c
→ ADDI Ri, c, Rj

Pattern 2: Load from Memory
    load
      |
    addr
→ LD addr, Ri

Pattern 3: Indexed Load
    load
      |
      +
     / \
   Ri   c
→ LD c(Ri), Rj
```

### Tree for `a[i] = b`
```
        =
       / \
      []   b
     / \
    a   i
    
Generated:
    LD i, R0
    MUL #4, R0      // Assuming element size 4
    LD b, R1
    ST R1, a(R0)    // Indexed store
```

---

## 8.7 DAG-Based Code Generation

### Advantage of DAG
- Common subexpressions computed once
- Represents optimal evaluation order

### Labeling Algorithm (Sethi-Ullman)
Computes minimum registers needed for expression.

```
For leaf nodes:
    label = 1 if leftmost, 0 otherwise

For interior nodes with children L, R:
    if label(L) == label(R):
        label = label(L) + 1
    else:
        label = max(label(L), label(R))
```

### Code Generation from Labeled Tree
```
gencode(node):
    if node is leaf:
        generate: LD node.name, R
    else:
        if label(right) > label(left):
            gencode(right)
            gencode(left)
        else:
            gencode(left)
            gencode(right)
        generate: OP Rright, Rleft
```

### Example
```
Expression: (a + b) * (c + d)

Tree:
           *
          / \
         /   \
        +     +
       / \   / \
      a   b c   d

Labels:
           2
          / \
         /   \
        1     1
       / \   / \
      1   0 1   0

Minimum registers needed: 2

Code (2 registers):
LD a, R0
LD b, R1
ADD R1, R0      // R0 = a + b
LD c, R1
LD d, R2        // Need 3rd register! But...

Better order (evaluate right first when equal labels):
LD c, R0
LD d, R1
ADD R1, R0      // R0 = c + d
LD a, R1
LD b, R2        // Still need 3... 

Actually with 2 registers:
LD c, R0
LD d, R1
ADD R1, R0      // R0 = c + d
ST R0, temp     // Spill
LD a, R0
LD b, R1
ADD R1, R0      // R0 = a + b
LD temp, R1
MUL R1, R0      // R0 = (a+b) * (c+d)
```

---

## 8.8 Addressing Modes Code Generation

### Addressing Mode Selection
```
TAC: x = y           →  MOV y, R; MOV R, x  (if y in memory)
                        MOV Ry, Rx           (if y in register)

TAC: x = *p          →  MOV *Rp, Rx         (indirect)

TAC: x = a[i]        →  MOV i, R; MOV a(R), Rx  (indexed)

TAC: x = &a          →  LEA a, Rx           (load address)
```

---

## 8.9 Code Generation for Control Flow

### Conditional Jump
**TAC:** `if x < y goto L`
```
CMP x, y
JLT L
```

### If-Then-Else
**TAC:**
```
if x < y goto L1
goto L2
L1: z = 1
    goto L3
L2: z = 2
L3: ...
```

**Generated:**
```
    CMP x, y
    JLT L1
    MOV #2, z
    JMP L3
L1: MOV #1, z
L3: ...
```

### While Loop
**TAC:**
```
L1: if x < y goto L2
    goto L3
L2: x = x + 1
    goto L1
L3: ...
```

**Generated:**
```
L1: CMP x, y
    JGE L3       // Inverted condition
    ADD #1, x
    JMP L1
L3: ...
```

---

## 8.10 Code Generation for Function Calls

### Calling Convention (Standard)
```
Caller:
    1. Save caller-saved registers
    2. Push arguments (right to left)
    3. CALL function
    4. Pop arguments
    5. Restore caller-saved registers
    6. Use return value (usually in R0)

Callee:
    1. Push old FP
    2. FP = SP
    3. Allocate local space (SP -= size)
    4. Save callee-saved registers
    5. Execute function body
    6. Restore callee-saved registers
    7. SP = FP (deallocate locals)
    8. Pop old FP
    9. RET
```

### Example
**Source:**
```c
int add(int a, int b) {
    return a + b;
}
int x = add(3, 5);
```

**Generated:**
```
; Caller (main)
    PUSH #5         ; Push second arg
    PUSH #3         ; Push first arg
    CALL add
    ADD #8, SP      ; Pop arguments
    MOV R0, x       ; Save return value

; Callee (add)
add:
    PUSH FP         ; Save old FP
    MOV SP, FP      ; New FP
    ; No locals, no callee-saved regs needed
    MOV 8(FP), R0   ; Load a (first arg)
    ADD 12(FP), R0  ; Add b (second arg)
    POP FP          ; Restore FP
    RET
```

---

## 8.11 Peephole Optimization Revisited

### Common Patterns at Code Generation

#### Redundant Loads
```
Before:         After:
MOV R0, x       MOV R0, x
MOV x, R0       (removed - R0 already has x)
```

#### Redundant Jumps
```
Before:         After:
JMP L1          JMP L2
L1: JMP L2      (L1 eliminated)
```

#### Algebraic Simplification
```
Before:         After:
ADD #0, R0      (removed)
MUL #1, R0      (removed)
MUL #2, R0      SHL #1, R0  (cheaper)
```

#### Combine Operations
```
Before:         After:
MOV x, R0       ADD x, y, R0  (if machine supports)
ADD y, R0
MOV R0, z
```

---

## 8.12 GATE Previous Year Patterns

### Pattern 1: Minimum Registers
**Q:** How many registers needed for expression?
**Approach:** Use Sethi-Ullman labeling.

### Pattern 2: Code Generation
**Q:** Generate code for TAC with n registers.
**Approach:** Track descriptors, generate systematically.

### Pattern 3: Instruction Count
**Q:** How many instructions for expression?
**Approach:** Count LD, OP, ST operations.

### Pattern 4: Cost Calculation
**Q:** Total cost of generated code?
**Approach:** Sum instruction costs.

---

## 📝 Quick Revision Points

1. **Code Gen Tasks:** Instruction selection, register allocation, ordering
2. **Target Forms:** Absolute, relocatable, assembly
3. **Register Descriptor:** What each register holds
4. **Address Descriptor:** Where each variable is stored
5. **getReg:** Selects register for operation
6. **Spilling:** Save register to memory when needed
7. **Sethi-Ullman:** Minimum registers for expression
8. **Peephole:** Optimize small instruction windows
9. **Graph Coloring:** Global register allocation
10. **Calling Convention:** Standard function call sequence

---

## 🧠 Mnemonic Summary

### Code Generator Tasks
> **"RIOS"**
> - **R**egister allocation
> - **I**nstruction selection
> - **O**rdering
> - **S**cheduling

### Sethi-Ullman Rule
> **"Equal = Plus One, Unequal = Take Max"**

### Descriptor Types
> **"Register knows contents, Address knows locations"**

---

## 🔥 The Adversarial Vault

### Trap 1: Register Count
**Q:** 2 registers enough for `(a+b)*(c+d)`?
**A:** YES with spilling, NO without. Sethi-Ullman says 2 but needs temp store.

### Trap 2: Commutative Operations
**Q:** Does order matter for `a + b`?
**A:** For code gen, YES! Evaluate expensive side first to minimize registers.

### Trap 3: Addressing Modes
**Q:** Cost of `ADD R1, x(R2)` vs `LD x(R2), R3; ADD R1, R3`?
**A:** First is cheaper if machine supports indexed addressing.

---

## ✅ Self-Assessment Questions

1. Generate code for `t = a + b * c` with 2 registers.
2. Calculate minimum registers for `((a+b)+c)+d`.
3. Show register and address descriptors during code gen.
4. Optimize: `MOV R0, x; MOV x, R1; ADD R0, R1`.
5. Generate function call code for `foo(1, 2, 3)`.

---

**Next Chapter:** [Error Handling →](09-Error-Handling.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
