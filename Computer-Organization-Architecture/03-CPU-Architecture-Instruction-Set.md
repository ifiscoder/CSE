# Module 3: CPU Architecture & Instruction Set | The Singularity

> **The Atomic Truth:** *"Fetch-Decode-Execute: The eternal CPU heartbeat."*

---

## 🎯 The Path of Elegance (Root Derivation)

### 3.1 Basic CPU Organization

```
[Image of CPU Architecture]
┌─────────────────────────────────────────────────────────────┐
│                         CPU                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────────────────┐  │
│  │   CU     │    │   ALU    │    │     Registers        │  │
│  │ Control  │◄──►│Arithmetic│◄──►│ PC, IR, MAR, MBR,   │  │
│  │   Unit   │    │  Logic   │    │ ACC, GPRs, FLAGS    │  │
│  └────┬─────┘    └────┬─────┘    └──────────┬───────────┘  │
│       │               │                      │              │
│       └───────────────┴──────────────────────┘              │
│                         ↕                                   │
│              ┌──────────────────┐                           │
│              │   Internal Bus   │                           │
│              └────────┬─────────┘                           │
└───────────────────────┼─────────────────────────────────────┘
                        ↕
                 ┌──────────────┐
                 │ System Bus   │
                 │ (Address,    │
                 │  Data,       │
                 │  Control)    │
                 └──────┬───────┘
                        ↕
                 ┌──────────────┐
                 │    Memory    │
                 └──────────────┘
```

### The Register Set | The Golden Pivot

| Register | Full Name | Function |
|----------|-----------|----------|
| **PC** | Program Counter | Address of NEXT instruction |
| **IR** | Instruction Register | CURRENT instruction being executed |
| **MAR** | Memory Address Register | Address for memory access |
| **MBR/MDR** | Memory Buffer/Data Register | Data to/from memory |
| **ACC** | Accumulator | Primary operand/result storage |
| **SP** | Stack Pointer | Top of stack address |
| **FLAGS** | Status Register | Condition codes (Z, C, S, O) |

**⚠️ The Genius Trap:** PC points to NEXT instruction, not current!

---

## 📐 3.2 Instruction Cycle | The CPU Heartbeat

### The Basic Cycle

```
[Image of Instruction Cycle State Diagram]
        ┌──────────┐
        │  FETCH   │◄─────────────────────┐
        └────┬─────┘                      │
             ↓                            │
        ┌──────────┐                      │
        │  DECODE  │                      │
        └────┬─────┘                      │
             ↓                            │
    ┌────────┴────────┐                   │
    ↓                 ↓                   │
┌───────┐        ┌─────────┐              │
│OPERAND│        │ EXECUTE │              │
│ FETCH │        │(Direct) │              │
└───┬───┘        └────┬────┘              │
    ↓                 │                   │
┌───────┐             │                   │
│EXECUTE│             │                   │
└───┬───┘             │                   │
    ↓                 ↓                   │
    └────────┬────────┘                   │
             ↓                            │
        ┌──────────┐                      │
        │  STORE   │──────────────────────┘
        └──────────┘
```

### Micro-Operations | The Atomic Steps

**Fetch Cycle:**
```
T₀: MAR ← PC           // Send PC to MAR
T₁: MBR ← M[MAR]       // Read from memory
    PC ← PC + 1        // Increment PC (parallel)
T₂: IR ← MBR           // Transfer to IR
```

**Decode Cycle:**
```
T₃: Decode IR[opcode]  // Identify operation
    Calculate EA       // If needed
```

**Execute Cycle (ADD example):**
```
T₄: MAR ← IR[address]  // Address of operand
T₅: MBR ← M[MAR]       // Fetch operand
T₆: ACC ← ACC + MBR    // Perform addition
```

---

## 🎯 3.3 Instruction Format | The Anatomy

### General Format

```
[Image of Instruction Format]
┌────────────┬────────────┬────────────┬────────────┐
│   Opcode   │   Mode     │  Operand1  │  Operand2  │
└────────────┴────────────┴────────────┴────────────┘
```

### Classification by Operand Count

| Type | Format | Example | GATE Frequency |
|------|--------|---------|----------------|
| 3-Address | OP R1, R2, R3 | ADD R1, R2, R3 | High |
| 2-Address | OP R1, R2 | ADD R1, R2 (R1 ← R1+R2) | High |
| 1-Address | OP R1 | ADD R1 (ACC ← ACC+R1) | Medium |
| 0-Address | OP | ADD (Stack-based) | Medium |

### The Code Density Trade-off

$$\text{Code Size} = n \times (\text{Opcode bits} + \text{Address bits per operand})$$

**Example:** For 64 operations, 1024 memory locations:
- 3-Address: $6 + 3 \times 10 = 36$ bits/instruction
- 2-Address: $6 + 2 \times 10 = 26$ bits/instruction
- 1-Address: $6 + 1 \times 10 = 16$ bits/instruction
- 0-Address: $6 + 0 = 6$ bits (but needs PUSH/POP)

---

## 🔢 3.4 Addressing Modes | The Access Paths

### The Complete Addressing Mode Table

| Mode | Notation | Effective Address | Use Case |
|------|----------|-------------------|----------|
| **Immediate** | #X | Operand = X | Constants |
| **Direct** | X | EA = X | Simple variables |
| **Indirect** | (X) | EA = M[X] | Pointers |
| **Register** | R | EA = R | Fast operations |
| **Register Indirect** | (R) | EA = M[R] | Array access |
| **Displacement** | X(R) | EA = X + R | Structure fields |
| **Indexed** | (R1)(R2) | EA = R1 + R2 | 2D arrays |
| **Auto-increment** | (R)+ | EA = R; R ← R+d | Sequential access |
| **Auto-decrement** | -(R) | R ← R-d; EA = R | Stack operations |

### The Memory Access Count | The Golden Formula

$$\text{Total Memory Accesses} = \text{Fetch} + \text{EA Calculation} + \text{Operand Fetch}$$

| Mode | Memory Accesses (excluding fetch) |
|------|-----------------------------------|
| Immediate | 0 |
| Direct | 1 |
| Indirect | 2 |
| Register | 0 |
| Register Indirect | 1 |
| Double Indirect | 3 |

### ⚡ The GATE Shortcut: Indirection Levels

For $n$ levels of indirection: **Memory Accesses = $n + 1$**

---

## 🏗️ 3.5 CISC vs RISC | The Architecture Wars

```
[Image of CISC vs RISC Spectrum]
        CISC                              RISC
    (Complex)                           (Reduced)
        ◄─────────────────────────────────►
    
    Many addressing modes        │    Limited addressing modes
    Variable instruction length  │    Fixed instruction length
    Memory-to-memory operations  │    Load-store architecture
    Microprogrammed control      │    Hardwired control
    Complex instructions         │    Simple instructions
    Less registers              │    More registers
```

| Feature | CISC | RISC |
|---------|------|------|
| Instructions | 100-250 | 30-100 |
| Instruction Length | Variable (1-15 bytes) | Fixed (4 bytes) |
| Addressing Modes | 12-24 | 3-5 |
| Registers | 8-24 | 32-192 |
| CPI | 2-10 | ~1 (with pipelining) |
| Control | Microprogrammed | Hardwired |
| Examples | x86, VAX | ARM, MIPS, SPARC |

### The Performance Equation

$$\text{CPU Time} = \text{IC} \times \text{CPI} \times \text{Clock Cycle Time}$$

Where:
- IC = Instruction Count
- CPI = Cycles Per Instruction

**The RISC Advantage:**
$$\text{RISC: Lower CPI} \times \text{Higher IC} \approx \text{CISC: Higher CPI} \times \text{Lower IC}$$

---

## 🔄 3.6 Control Unit Design

### Hardwired Control | The Speed Demon

```
[Image of Hardwired Control]
┌─────────────┐
│   Opcode    │──┐
└─────────────┘  │    ┌────────────────┐
                 ├───►│ Combinational  │───► Control Signals
┌─────────────┐  │    │    Logic       │
│   Flags     │──┤    │  (PLA/ROM)     │
└─────────────┘  │    └────────────────┘
                 │
┌─────────────┐  │
│   Timing    │──┘
└─────────────┘
```

**Advantages:** Fast, efficient
**Disadvantages:** Complex, inflexible, hard to modify

### Microprogrammed Control | The Flexible Solution

```
[Image of Microprogrammed Control]
┌─────────────┐
│   Opcode    │───► ┌─────────────────┐
└─────────────┘     │ Control Memory  │
                    │ (Microprogram)  │
┌─────────────┐     │                 │───► Control Signals
│  μPC        │───► │ ┌───────────┐   │
└─────────────┘     │ │μInstruction│  │
                    │ └───────────┘   │
                    └─────────────────┘
```

**Microinstruction Format:**
```
┌────────────────────┬─────────────────┐
│  Control Signals   │  Next Address   │
└────────────────────┴─────────────────┘
```

### Horizontal vs Vertical Microprogramming

| Aspect | Horizontal | Vertical |
|--------|------------|----------|
| Control field | One bit per signal | Encoded |
| Width | Wide (50-100+ bits) | Narrow (16-32 bits) |
| Speed | Faster (no decode) | Slower (needs decode) |
| Memory | More | Less |
| Parallelism | High | Low |

---

## 🔗 3.7 Instruction Set Design

### Orthogonality Principle

*"Any addressing mode can be used with any instruction."*

**Benefit:** Simpler programming, regular instruction encoding
**Example:** MIPS is highly orthogonal; x86 is not

### Instruction Categories

| Category | Examples | Percentage (typical) |
|----------|----------|---------------------|
| Data Transfer | MOV, LOAD, STORE, PUSH, POP | 30-40% |
| Arithmetic | ADD, SUB, MUL, DIV | 15-20% |
| Logical | AND, OR, XOR, NOT | 10-15% |
| Control Transfer | JMP, CALL, RET, Bcc | 20-25% |
| I/O | IN, OUT | 5% |
| Special | NOP, HALT, INT | 5% |

---

## 🧮 3.8 Stack Architecture | Zero-Address Machines

### Postfix (Reverse Polish) Notation

**Infix:** $(A + B) \times (C - D)$
**Postfix:** $AB + CD - \times$

### Stack Execution

```
Expression: AB+CD-*
Stack Operations:
PUSH A    [A]
PUSH B    [A, B]
ADD       [A+B]
PUSH C    [A+B, C]
PUSH D    [A+B, C, D]
SUB       [A+B, C-D]
MUL       [(A+B)*(C-D)]
```

### Infix to Postfix Algorithm

1. Scan left to right
2. If operand, output it
3. If '(', push to stack
4. If ')', pop and output until '('
5. If operator:
   - Pop higher/equal precedence operators
   - Push current operator
6. At end, pop all remaining

---

## 🎭 The Bizarre Mnemonic | "The Restaurant CPU"

*"The PC is the WAITER who knows the next order. The IR is the CURRENT ORDER being prepared. The MAR is the TABLE NUMBER. The MBR is the FOOD TRAY. The Control Unit is the HEAD CHEF directing everyone!"*

---

## 🏆 The 2026 Adversarial Vault

### Trap 1: The PC Increment Timing
**Question Pattern:** "After executing a 4-byte instruction at address 1000, what is PC?"
**Anti-Solution:** Students say 1000 (current) or 1001 (+1 byte).
**Truth:** PC = 1004 (next instruction address). PC is incremented DURING fetch!

### Trap 2: The Addressing Mode Memory Access
**Question Pattern:** "How many memory accesses for indirect indexed mode?"
**Anti-Solution:** Students forget the instruction fetch.
**Truth:** Fetch (1) + Indirect (1) + Operand (1) = 3 minimum.

### Trap 3: The Register Indirect vs Indirect
**Question Pattern:** "Difference between (R) and (X)?"
**Anti-Solution:** Students confuse the two.
**Truth:** 
- (R): Address is IN register R (0 memory for EA)
- (X): Address is AT memory location X (1 memory for EA)

### Trap 4: The Stack Expression Evaluation
**Question Pattern:** "Minimum stack depth for $A+B*C-D/E*F$?"
**Anti-Solution:** Students trace incorrectly.
**Truth:** Postfix = $ABC*+DE/F*-$, Max depth = 3

### MSQ Logic Gate | Elimination Rules
1. PC always points to NEXT instruction
2. Immediate mode = 0 memory accesses for operand
3. Each indirection level = +1 memory access
4. RISC = fixed length, CISC = variable length

---

## 📊 GATE PYQ Pattern Analysis

| Year | Topic | Marks | Trap Type |
|------|-------|-------|-----------|
| 2023 | Addressing Modes | 2 | Memory access count |
| 2022 | Instruction Format | 1 | Bit allocation |
| 2021 | Stack Operations | 2 | Expression evaluation |
| 2020 | Control Unit | 2 | Microprogramming |

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| PC after fetch | PC = PC + instruction_size |
| Immediate mode | No memory access for operand |
| Indirect mode | +1 memory access per level |
| RISC instruction | Must be fixed length |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Would you like to initiate a **'Multi-Variable Stress Test'** combining CPU Architecture with Pipelining for a Rank-1 simulation?*

---
[← Previous: Digital Logic](./02-Digital-Logic-Boolean-Algebra.md) | [Back to Index](./README.md) | [Next: Pipelining & Hazards →](./04-Pipelining-Hazards.md)
