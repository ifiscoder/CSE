# Machine Instructions & Addressing Modes | The ISA Singularity

> **The Atomic Truth:** *Instructions are hardware's command language.*

[Image of instruction bits flowing through decoder, splitting into opcode (what to do) and operands (what to act upon) - the fundamental syntax of computation]

---

## I. THE PATH OF ELEGANCE

### 1.1 Instruction Set Architecture (ISA) - The Contract

**The Golden Pivot:** The **instruction format** determines:
- What operations are possible (opcode space)
- How operands are specified (addressing modes)
- How fast instructions execute (complexity vs cycles)

**ISA Definition:** The boundary between hardware and software.

**Components of an Instruction:**
$$\text{Instruction} = \text{Opcode} \mid \text{Operand Specifiers}$$

Where:
- **Opcode** = Operation code (what to do)
- **Operand Specifiers** = Where to find data (addressing modes)

---

### 1.2 Instruction Formats (The Encoding Problem)

Hardware constraint: **Fixed-width instruction** vs **Variable-width instruction**

#### A. Fixed-Length Instructions (RISC Philosophy)
**Example:** MIPS, ARM (32-bit instructions)

**Advantage:** 
- Simple decode logic
- Easy pipelining
- Predictable fetch

**Disadvantage:**
- Wastes bits for simple operations
- Limited immediate field size

#### B. Variable-Length Instructions (CISC Philosophy)
**Example:** x86 (1-15 bytes)

**Advantage:**
- Compact code
- Complex operations in single instruction

**Disadvantage:**
- Complex decode
- Pipeline complications (Module 07)

---

### 1.3 Instruction Format Types

#### Type 1: Three-Address Format
$$\text{OP} \quad R_d, R_s, R_t$$

**Example:** `ADD R1, R2, R3` → $R_1 = R_2 + R_3$

**Bit Layout (32-bit):**
```
| Opcode (6) | Rs (5) | Rt (5) | Rd (5) | Shamt (5) | Funct (6) |
```

**Advantages:** 
- Maximum flexibility
- Operands preserved

**Disadvantages:**
- Uses 3 register fields (limits opcode space)

**Instruction Count for:**
$$Y = (A \times B) + (C \times D)$$

**Three-address:**
```
MUL T1, A, B    # T1 = A * B
MUL T2, C, D    # T2 = C * D  
ADD Y, T1, T2   # Y = T1 + T2
```
**Count:** 3 instructions

---

#### Type 2: Two-Address Format
$$\text{OP} \quad R_d, R_s$$

**Example:** `ADD R1, R2` → $R_1 = R_1 + R_2$

**Characteristic:** Destination is also source (destructive)

**Instruction Count for:**
$$Y = (A \times B) + (C \times D)$$

**Two-address:**
```
MOV T1, A       # T1 = A
MUL T1, B       # T1 = T1 * B
MOV T2, C       # T2 = C
MUL T2, D       # T2 = T2 * D
ADD T1, T2      # T1 = T1 + T2
MOV Y, T1       # Y = T1
```
**Count:** 6 instructions

---

#### Type 3: One-Address Format (Accumulator-based)
$$\text{OP} \quad \text{Address}$$

**Implicit:** Accumulator (AC) is always involved

**Example:** `ADD M` → $\text{AC} = \text{AC} + M[\text{Address}]$

**Instruction Count for:**
$$Y = (A \times B) + (C \times D)$$

**One-address:**
```
LOAD A          # AC = A
MUL B           # AC = AC * B
STORE T1        # T1 = AC
LOAD C          # AC = C
MUL D           # AC = AC * D
ADD T1          # AC = AC + T1
STORE Y         # Y = AC
```
**Count:** 7 instructions

---

#### Type 4: Zero-Address Format (Stack-based)
**Implicit:** Stack top and second element

**Example:** `ADD` → $\text{TOS} = \text{TOS} + \text{SOS}$ (pop 2, push 1)

**Instruction Count for:**
$$Y = (A \times B) + (C \times D)$$

**Zero-address:**
```
PUSH A          # Stack: [A]
PUSH B          # Stack: [A, B]
MUL             # Stack: [A*B]
PUSH C          # Stack: [A*B, C]
PUSH D          # Stack: [A*B, C, D]
MUL             # Stack: [A*B, C*D]
ADD             # Stack: [(A*B)+(C*D)]
POP Y           # Y = result
```
**Count:** 8 instructions

---

### 1.4 The Instruction Count Theorem

**For expression:** $Y = (A \times B) + (C \times D)$

| Format | Instruction Count |
|--------|-------------------|
| 3-address | 3 |
| 2-address | 6 |
| 1-address | 7 |
| 0-address | 8 |

**The Golden Trade-off:**
$$\text{Fewer addresses} \rightarrow \text{More instructions} \rightarrow \text{Longer execution time}$$

But:
$$\text{Fewer addresses} \rightarrow \text{Shorter instruction length} \rightarrow \text{Less memory bandwidth}$$

---

## II. ADDRESSING MODES (The Operand Singularity)

**The Master Variable:** How is the **effective address (EA)** computed?

$$\text{EA} = f(\text{Instruction Fields, Registers, PC})$$

---

### Mode 1: Immediate Addressing
**Definition:** Operand **is** part of instruction

$$\text{EA} = \text{Not applicable (data in instruction)}$$

**Example:** `ADD R1, #5` → $R_1 = R_1 + 5$

**Encoding:**
```
| Opcode | Rd | Immediate Value |
```

**Advantages:**
- No memory access for operand (fastest)
- Good for constants

**Disadvantages:**
- Limited range (immediate field size)
- Cannot modify operand value

**Use Cases:** Constants, small integers, loop counters initialization

**Cycles:** 1 (no memory access)

---

### Mode 2: Direct (Absolute) Addressing
**Definition:** Address **is** in instruction

$$\text{EA} = \text{Address field in instruction}$$

**Example:** `LOAD R1, 1000` → $R_1 = M[1000]$

**Encoding:**
```
| Opcode | Rd | Address |
```

**Memory Accesses:** 1 (to fetch operand)

**Advantages:**
- Simple
- Good for global variables

**Disadvantages:**
- Limited address space (address field size)
- Not relocatable (absolute addresses)

**Use Cases:** Static variables, fixed memory locations

**Cycles:** 2 (instruction fetch + operand fetch)

---

### Mode 3: Register Direct Addressing
**Definition:** Operand is in a register

$$\text{EA} = \text{Not applicable (data in register)}$$

**Example:** `ADD R1, R2` → $R_1 = R_1 + R_2$

**Memory Accesses:** 0 (register access)

**Advantages:**
- Fastest (registers are fast)
- Small encoding (few bits for register number)

**Disadvantages:**
- Limited number of registers
- Register allocation complexity

**Cycles:** 1 (no memory access)

---

### Mode 4: Register Indirect Addressing
**Definition:** Register **contains address** of operand

$$\text{EA} = [R_i]$$

Where $[R_i]$ means "contents of register $R_i$"

**Example:** `LOAD R1, (R2)` → $R_1 = M[[R_2]]$

If $R_2 = 1000$, then $R_1 = M[1000]$

**Memory Accesses:** 1 (using address from register)

**Advantages:**
- Pointer support
- Large address space (full register width)
- Relocatable code

**Disadvantages:**
- Extra indirection (slower than register direct)

**Use Cases:** Pointers, dynamic memory access, arrays

**Cycles:** 2 (instruction fetch + operand fetch via pointer)

---

### Mode 5: Indexed Addressing
**Definition:** EA = Base address + Index register

$$\text{EA} = \text{Base} + [R_{\text{index}}]$$

**Example:** `LOAD R1, 1000(R2)` → $R_1 = M[1000 + [R_2]]$

If $R_2 = 50$, then $R_1 = M[1050]$

**Memory Accesses:** 1

**Advantages:**
- Array access (base = array start, index = element offset)
- Table lookup

**Disadvantages:**
- Requires addition in address calculation

**Use Cases:** Arrays, tables, sequential data structures

**Cycles:** 2 (instruction fetch + indexed operand fetch)

**The Array Access Formula:**
$$\text{EA}_{\text{element}} = \text{Base} + (i \times \text{element\_size})$$

Where $i$ = array index (0-based)

---

### Mode 6: Base Register Addressing
**Definition:** EA = Base register + Offset

$$\text{EA} = [R_{\text{base}}] + \text{Offset}$$

**Example:** `LOAD R1, 100(R2)` → $R_1 = M[[R_2] + 100]$

If $R_2 = 2000$, then $R_1 = M[2100]$

**Difference from Indexed:**
- Base register: Large value (base address)
- Offset: Small value (displacement)

**Indexed mode:**
- Base: Small value (array start)
- Index register: Variable value (element index)

**Use Cases:** 
- Stack frames (base = frame pointer, offset = local variable)
- Structure member access (base = struct pointer, offset = member offset)

**Cycles:** 2

---

### Mode 7: Autoincrement / Autodecrement Addressing
**Definition:** Register indirect with automatic increment/decrement

**Autoincrement:**
$$\text{EA} = [R_i], \quad R_i \leftarrow R_i + \text{size}$$

**Autodecrement:**
$$\text{EA} = [R_i] - \text{size}, \quad R_i \leftarrow R_i - \text{size}$$

**Example (Autoincrement):** `LOAD R1, (R2)+`
```
R1 = M[[R2]]
R2 = R2 + 4  # (assuming 4-byte operand)
```

**Use Cases:**
- Stack operations (push/pop)
- Sequential memory access (loops)
- Array traversal

**The Stack Mapping:**
- **PUSH:** Autodecrement (decrement SP, then write)
- **POP:** Autoincrement (read, then increment SP)

**Cycles:** 2 (but efficient for loops)

---

### Mode 8: Relative Addressing (PC-Relative)
**Definition:** EA = PC + Offset

$$\text{EA} = \text{PC} + \text{Offset}$$

**Example:** `BRANCH +20` → Jump to $\text{PC} + 20$

**Critical:** PC value used is typically **PC of next instruction**

**Use Cases:**
- Branch instructions
- Position-independent code (PIC)
- Relocatable code

**Range:** Limited by offset field width
- 8-bit offset: $-128$ to $+127$ instructions
- 16-bit offset: $-32768$ to $+32767$ instructions

**The Branch Formula:**
$$\text{Target Address} = \text{PC}_{\text{next}} + (\text{Offset} \times \text{instruction\_size})$$

**Cycles:** 1 (for address calculation, may have branch penalty in pipeline)

---

### Mode 9: Memory Indirect Addressing
**Definition:** Address field points to memory location containing address

$$\text{EA} = M[\text{Address}]$$

**Example:** `LOAD R1, @1000` → $R_1 = M[M[1000]]$

If $M[1000] = 5000$, then $R_1 = M[5000]$

**Memory Accesses:** 2 (one for address, one for operand)

**Use Cases:**
- Pointer to pointer
- Dynamic dispatch (virtual functions)
- Function pointers

**Cycles:** 3 (instruction fetch + address fetch + operand fetch)

**The Double Indirection:**
- Rare in modern ISAs (too slow)
- Sometimes used for OS-level address translation

---

## III. THE 2026 ADVERSARIAL VAULT

### Trap #1: The Instruction Count Deception
**The Setup:** "How many instructions are needed to evaluate $X = (A - B) + (C \times D)$ using 2-address format?"

**Anti-Solution:** Student counts:
```
SUB T1, B      # T1 = A - B (assumes T1 = A first)
MUL T2, D      # T2 = C * D
ADD T1, T2     # T1 = T1 + T2
MOV X, T1      # X = T1
```
**Count:** 4 instructions

**The Trap:** Forgot the initial **MOV** instructions to load A and C!

**Correct Solution:**
```
MOV T1, A      # 1
SUB T1, B      # 2: T1 = T1 - B = A - B
MOV T2, C      # 3
MUL T2, D      # 4: T2 = T2 * D = C * D
ADD T1, T2     # 5: T1 = T1 + T2
MOV X, T1      # 6
```
**Count:** 6 instructions

**Mental Checkpoint:** In 2-address format, **always account for initial loads** of operands into working registers.

---

### Trap #2: The PC-Relative Branch Calculation
**The Setup:** 
```
Address | Instruction
1000    | LOAD R1, 2000
1004    | ADD R1, R2
1008    | BRANCH +8
1012    | SUB R1, R3
1016    | STORE R1, 2004
```
"Where does the branch at 1008 jump to?"

**Anti-Solution:** "$1008 + 8 = 1016$"

**The Trap:** PC value during branch execution!

**The Truth:** When branch is **decoded**, PC has already advanced to **next instruction** (1012).

**Correct Calculation:**
$$\text{Target} = \text{PC}_{\text{next}} + \text{Offset} = 1012 + 8 = 1020$$

**If instruction past the STORE doesn't exist, this is an error!**

**Alternative Interpretation:** Some ISAs use **word offset** instead of byte offset.

If offset is in **words** (4-byte instructions):
$$\text{Target} = 1012 + (8 \times 4) = 1044$$

**NAT Precision Lock:** Verify whether offset is in **bytes** or **words/instructions**.

---

### Trap #3: The Indexed Addressing Array Access
**The Setup:** Array of 32-bit integers starts at address 2000. Access element `A[5]` using indexed addressing with base register R2.

**Anti-Solution:** 
"$\text{EA} = 2000 + 5 = 2005$"

**The Trap:** Forgot element size!

**Correct Calculation:**
$$\text{EA} = \text{Base} + (i \times \text{size}) = 2000 + (5 \times 4) = 2020$$

Where $\text{size} = 4$ bytes (32-bit integer)

**Mental Checkpoint:** Always multiply index by element size.

**The Size Table:**
| Data Type | Size (bytes) |
|-----------|--------------|
| char | 1 |
| short | 2 |
| int, float | 4 |
| double, long long | 8 |
| pointer (64-bit) | 8 |

---

### Trap #4: The Autoincrement Post vs Pre
**The Setup:** Register R1 = 1000. Instruction: `LOAD R2, (R1)+` with 4-byte operands.

"What is R1 after execution?"

**Anti-Solution:** Some students think increment happens **before** memory access.

**The Truth:** 
- **Autoincrement (post-increment):** Memory access uses **old** R1 value, then R1 increments
  ```
  R2 = M[1000]
  R1 = 1000 + 4 = 1004
  ```

- **Autodecrement (pre-decrement):** R1 decrements **first**, then memory access uses new value
  ```
  R1 = 1000 - 4 = 996
  R2 = M[996]
  ```

**Mnemonic:** 
- "Post-increment: **Act first, then update**"
- "Pre-decrement: **Update first, then act**"

**Stack Conventions:**
- **PUSH (grows down):** Pre-decrement (decrement SP, then write)
- **POP:** Post-increment (read, then increment SP)

---

### Trap #5: The Effective Address vs. Operand Value
**The Setup:** Register R1 = 1000, Memory[1000] = 50. Instruction: `ADD R2, (R1)`

"What is the effective address?"

**Anti-Solution:** "50" (confusing EA with operand value)

**The Truth:**
- **Effective Address (EA):** 1000 (the memory location)
- **Operand Value:** 50 (the data at that location)

**Definition Precision:**
$$\text{EA} = \text{Memory address computed by addressing mode}$$
$$\text{Operand} = M[\text{EA}]$$

---

### Trap #6: The Immediate Mode Memory Access
**The Setup:** "How many memory accesses does `ADD R1, #100` require?"

**Anti-Solution:** "2: instruction fetch + operand fetch"

**The Trap:** Immediate mode has **no operand memory access**!

**Correct Answer:** 1 (only instruction fetch)

**The operand 100 is encoded in the instruction itself.**

**Memory Access Count Table:**
| Addressing Mode | Memory Accesses |
|----------------|-----------------|
| Immediate | 0 (data in instruction) |
| Register | 0 (data in register) |
| Direct | 1 (operand fetch) |
| Register Indirect | 1 (operand via pointer) |
| Indexed | 1 (operand at computed address) |
| Memory Indirect | 2 (address fetch + operand fetch) |

**Critical:** Always add 1 for instruction fetch itself (unless question specifies "operand access only")

---

### Trap #7: The RISC vs CISC Instruction Count
**The Setup:** "RISC always has higher instruction count than CISC for the same program."

**Anti-Solution:** "True, because RISC has simpler instructions."

**The Trap:** This is generally true, but **not always**.

**Counter-Example:**
RISC code:
```
LOAD R1, A
LOAD R2, B
ADD R1, R2
STORE R1, C
```
**Count:** 4 instructions

CISC code:
```
ADD [C], [A], [B]  # Memory-to-memory
```
**Count:** 1 instruction

**But:** CISC instruction may take **multiple cycles** (more than 4 RISC cycles combined).

**The Golden Rule:** Instruction count alone is meaningless. Must consider:
$$\text{Execution Time} = \text{Instructions} \times \text{CPI} \times \text{Cycle Time}$$

(Module 08: Performance)

---

### Trap #8: The Instruction Length Calculation
**The Setup:** "32-bit instruction format with 6-bit opcode, 3 register fields (5 bits each). How many bits remain for immediate value?"

**Anti-Solution:** $32 - 6 - 3 \times 5 = 11$ bits

**The Trap:** This assumes **all** fields are used simultaneously.

**The Truth:** Different instruction formats use different field layouts.

**For immediate instruction:**
```
| Opcode (6) | Rd (5) | Rs (5) | Immediate (16) |
```
Total: $6 + 5 + 5 + 16 = 32$ ✓

**For register instruction:**
```
| Opcode (6) | Rd (5) | Rs (5) | Rt (5) | Shamt (5) | Funct (6) |
```
Total: $6 + 5 + 5 + 5 + 5 + 6 = 32$ ✓

**Mental Checkpoint:** Different instruction types have different field allocations within the same fixed width.

---

## IV. PERMANENT RECALL (The Memory Machine)

### Mnemonic #1: Addressing Modes Hierarchy
**Phrase:** "I Directly Registered My Indexed Base Auto-Relative Memory"

- **I**mmediate
- **D**irect
- **R**egister (Direct/Indirect)
- **M**y = (placeholder)
- **I**ndexed
- **B**ase
- **Auto** (increment/decrement)
- **R**elative (PC-relative)
- **M**emory indirect

**Visual:** A ladder of indirection levels:
```
Level 0: Immediate (data in instruction)
Level 1: Register (data in register)
Level 2: Direct (data in memory, address in instruction)
Level 3: Indirect (data in memory, address in register/memory)
```

---

### Mnemonic #2: Instruction Format Trade-off
**"Three's Company, Zero's Crowded"**

- **3-address:** Few instructions, long format
- **0-address:** Many instructions, short format

**Mental Slider:** Turn the "address field count" dial down (3→2→1→0):
- Watch instruction length shrink
- Watch instruction count grow
- Code size may increase or decrease (depends on program)

---

### Mnemonic #3: PC-Relative Branch
**"PC Sees Tomorrow"**

When calculating branch target, PC has already moved to **next instruction** (tomorrow).

**Visual:** A car (PC) at a fork in the road. The sign says "+20 meters," but measured from where the car **will be** after reading the sign, not where it is now.

---

### Mnemonic #4: Autoincrement vs. Autodecrement
**"POPA Stack"**

- **PO**st-increment (POp): Use, then increment
- **PA**re-decrement (Push): Decrement, then use

**Visual:** A vending machine (stack):
- **PUSH (Pre-decrement):** Move shelf down, then place item
- **POP (Post-increment):** Take item, then move shelf up

---

### Mnemonic #5: Indexed vs. Base Register
**"Index Finger Counts, Thumb is Base"**

- **Index finger:** Points at different elements (variable)
- **Thumb:** Stable reference point (base address)

**Use case distinction:**
- **Indexed:** Base is constant (array start), index varies (element number)
- **Base Register:** Base varies (structure pointer), offset is constant (member offset)

---

## V. THE SOVEREIGNTY DRILLS

### Problem Set A: Instruction Count Calculations

**Problem 1:** Evaluate $W = (A + B) \times (C - D)$ using:
a) 3-address format
b) 2-address format
c) 1-address format (accumulator)

**Solution:**

**a) 3-address:**
```
ADD T1, A, B    # T1 = A + B
SUB T2, C, D    # T2 = C - D
MUL W, T1, T2   # W = T1 * T2
```
**Count:** 3

**b) 2-address:**
```
MOV T1, A       # T1 = A
ADD T1, B       # T1 = T1 + B = A + B
MOV T2, C       # T2 = C
SUB T2, D       # T2 = T2 - D = C - D
MOV W, T1       # W = T1
MUL W, T2       # W = W * T2
```
**Count:** 6

**c) 1-address:**
```
LOAD A          # AC = A
ADD B           # AC = AC + B
STORE T1        # T1 = AC
LOAD C          # AC = C
SUB D           # AC = AC - D
MUL T1          # AC = AC * T1
STORE W         # W = AC
```
**Count:** 7

---

**Problem 2 (GATE 2018):** A computer has 32-bit instruction format with 6-bit opcode. How many different 2-address instructions can be specified if there are 16 general-purpose registers?

**Solution:**

**2-address format:**
```
| Opcode (6) | Rd (4) | Rs (4) | Unused (18) |
```

Wait, this uses only $6 + 4 + 4 = 14$ bits out of 32.

**The question asks:** How many different 2-address instructions?

**Interpretation:** Each unique combination of (opcode, Rd, Rs) is a different instruction.

**Count:**
- Opcodes: $2^6 = 64$
- Rd choices: 16
- Rs choices: 16

**Total:** $64 \times 16 \times 16 = 16,384$

**But wait:** The question likely asks how many opcodes can be **allocated** to 2-address format, assuming other formats exist.

**Alternative Interpretation:** If we dedicate some opcodes to 2-address format:

With 6-bit opcode field, maximum opcodes = 64

If **all** are 2-address instructions: **64 different operations**, each with $16 \times 16$ register combinations.

**NAT Precision Lock:** Clarify whether question asks for:
- Number of opcode types (64 max)
- Number of unique instructions (64 × 16 × 16)

**Most likely answer:** $2^6 = 64$ (distinct operations in 2-address format)

---

**Problem 3:** Evaluate $X = ((A \times B) + C) \times D$ using stack (0-address) format.

**Solution:**
```
PUSH A          # Stack: [A]
PUSH B          # Stack: [A, B]
MUL             # Stack: [A*B]
PUSH C          # Stack: [A*B, C]
ADD             # Stack: [(A*B)+C]
PUSH D          # Stack: [(A*B)+C, D]
MUL             # Stack: [((A*B)+C)*D]
POP X           # X = result, Stack: []
```
**Count:** 8 instructions

**5-Second Snap-Check:** Expression has 3 operators → expect ~6-8 stack instructions (roughly 2× operator count).

---

### Problem Set B: Addressing Mode Identification

**Problem 4:** Identify addressing mode:
a) `MOV R1, #50`
b) `ADD R2, 1000`
c) `SUB R3, (R4)`
d) `LOAD R5, 100(R6)`
e) `STORE R7, (R8)+`

**Solution:**
a) **Immediate** (operand is constant 50)
b) **Direct/Absolute** (address 1000 in instruction)
c) **Register Indirect** (R4 contains address)
d) **Base Register** or **Indexed** (R6 + offset 100)
e) **Register Indirect with Autoincrement**

---

**Problem 5 (GATE 2017):** A computer has 32-bit addresses, 16-bit instructions, and byte-addressable memory. An instruction with 4-bit opcode and 1 register operand (4 bits) uses relative addressing. What is the maximum forward branch distance?

**Solution:**

**Instruction format:**
```
| Opcode (4) | Register (4) | Offset (8) |
```
Total: $4 + 4 + 8 = 16$ bits ✓

**Offset field:** 8 bits (signed)
- Range: $-128$ to $+127$

**Maximum forward branch:** $+127$

**But:** Is offset in bytes or instructions?

**Assuming byte offset:**
$$\text{Max distance} = 127 \text{ bytes}$$

**If offset is in instructions (16-bit = 2 bytes):**
$$\text{Max distance} = 127 \times 2 = 254 \text{ bytes}$$

**NAT Answer:** 
- If byte offset: **127**
- If word offset: **254**

**Critical:** Check problem statement for unit specification.

---

**Problem 6:** Register R1 = 2000, Memory[2000] = 3000, Memory[3000] = 50.

What is the effective address and operand value for:
a) `LOAD R2, (R1)`
b) `LOAD R2, @(R1)` (memory indirect via register)

**Solution:**

**a) Register Indirect `(R1)`:**
- EA = [R1] = 2000
- Operand = M[2000] = 3000
- **R2 = 3000**

**b) Memory Indirect `@(R1)`:**
- EA = M[[R1]] = M[2000] = 3000
- Operand = M[3000] = 50
- **R2 = 50**

**5-Second Snap-Check:** Each level of indirection adds one memory access.

---

### Problem Set C: Effective Address Calculations

**Problem 7:** Calculate EA for each instruction:

Given:
- R1 = 1000
- R2 = 20
- PC = 5000
- Memory[1000] = 2000

Instructions:
a) `LOAD R3, 500`
b) `LOAD R3, (R1)`
c) `LOAD R3, 100(R1)`
d) `LOAD R3, (R1, R2)`  [Base + Index]
e) `LOAD R3, @500`
f) `BRANCH -12`  [PC-relative]

**Solution:**

a) **Direct:** EA = 500

b) **Register Indirect:** EA = [R1] = 1000

c) **Base Register:** EA = [R1] + 100 = 1000 + 100 = 1100

d) **Indexed (Base + Index):** EA = [R1] + [R2] = 1000 + 20 = 1020

e) **Memory Indirect:** EA = M[500] (assume M[500] contains some address)

f) **PC-Relative:** 
   - Assuming PC has advanced to next instruction: PC_next = 5004 (if 4-byte instructions)
   - EA = 5004 + (-12) = 4992

---

**Problem 8 (Array Access):** Array A of 64-bit integers starts at address 4000. Compute EA for `A[10]` using indexed addressing.

**Solution:**

**Element size:** 64 bits = 8 bytes

**Index:** 10 (0-based)

**Formula:**
$$\text{EA} = \text{Base} + (i \times \text{size}) = 4000 + (10 \times 8) = 4000 + 80 = 4080$$

**NAT Answer:** 4080

**5-Second Snap-Check:** 10 elements × 8 bytes = 80 bytes offset ✓

---

**Problem 9 (Structure Access):** A structure starts at address stored in R5 (R5 = 2000). Member `field_x` is at offset 24 bytes. Write instruction using base register addressing.

**Solution:**

**Instruction:** `LOAD R1, 24(R5)`

**Effective Address:**
$$\text{EA} = [R5] + 24 = 2000 + 24 = 2024$$

**This is how compilers implement:** `struct_ptr->field_x`

---

### Problem Set D: Edge Cases and Traps

**Problem 10 (Autoincrement in Loop):** 

Register R1 points to array start (R1 = 1000). Array has 5 elements (4 bytes each). Load all elements using autoincrement.

**Code:**
```
MOV R1, #1000       # R1 = 1000
LOAD R2, (R1)+      # R2 = M[1000], R1 = 1004
LOAD R3, (R1)+      # R3 = M[1004], R1 = 1008
LOAD R4, (R1)+      # R4 = M[1008], R1 = 1012
LOAD R5, (R1)+      # R5 = M[1012], R1 = 1016
LOAD R6, (R1)+      # R6 = M[1016], R1 = 1020
```

**After all loads, R1 = 1020** (points past last element)

**Efficiency:** Autoincrement eliminates separate `ADD R1, #4` instructions.

---

**Problem 11 (PC-Relative Branch Target):**

```
Address | Instruction
2000    | LOAD R1, 100
2004    | ADD R1, R2
2008    | BRANCH +16
2012    | SUB R1, R3
2016    | MUL R1, R4
2020    | DIV R1, R5
2024    | STORE R1, 200
```

**Question:** Where does the branch at 2008 jump to?

**Solution:**

**PC during branch execution:** 2008
**PC of next instruction:** 2012

**Target:**
$$\text{EA} = \text{PC}_{\text{next}} + \text{Offset} = 2012 + 16 = 2028$$

**Result:** Branches to address 2028 (past the STORE instruction)

**If 2028 is beyond program code, this is a bug.**

---

**Problem 12 (Memory Indirect Double Access):**

Given:
- Memory[1000] = 2000
- Memory[2000] = 50

**Instruction:** `LOAD R1, @1000`

**Execution:**
1. Fetch address: M[1000] = 2000
2. Fetch operand: M[2000] = 50
3. R1 = 50

**Memory accesses:** 2 (for operand, not counting instruction fetch)

**Total cycles:** 3 (IF + address fetch + operand fetch)

---

**Problem 13 (The Instruction Format Opcode Space):**

32-bit instruction, 4 formats:
- Format A: 3-address (opcode 6 bits, 3 registers 5 bits each, funct 6 bits)
- Format B: 2-address with immediate (opcode 6 bits, 2 registers 5 bits each, immediate 16 bits)
- Format C: 1-address (opcode 6 bits, 1 register 5 bits, address 21 bits)
- Format D: Branch (opcode 6 bits, offset 26 bits)

**Question:** Is this encoding feasible?

**Analysis:**

All formats use **6-bit opcode** → 64 possible opcodes

**Answer:** Yes, feasible if:
- Each opcode uniquely identifies the format
- Example: Opcodes 0-15 for Format A, 16-31 for Format B, etc.

**This is how MIPS ISA is designed** (Module 09).

---

## VI. MSQ LOGIC GATES

### MSQ Strategy: Addressing Modes

**Question:** "Which addressing modes require ALU for EA calculation?"

**Options:**
A. Immediate
B. Register Indirect
C. Indexed
D. PC-Relative

**Logic Gate Process:**

1. **ALU Required for:**
   - Any mode that does **addition** for EA

2. **Analysis:**
   - A: No ALU (data in instruction)
   - B: No ALU (EA = register contents, direct transfer)
   - C: **Yes** (EA = Base + Index, requires adder)
   - D: **Yes** (EA = PC + Offset, requires adder)

**Answer:** C, D

**Edge Case Check:** Some argue B needs ALU to transfer register to address bus. **But** this is typically a direct connection, not an ALU operation.

**Examiner's Intent:** ALU for **computation** (addition), not just data transfer.

---

## VII. THE CROSS-TOPIC BRIDGES

### Bridge to Module 03 (ALU Design):
**Connection:** ALU must support address calculation for indexed, base, and PC-relative modes.
**Circuit:** Dedicated address adder vs. main ALU reuse.

### Bridge to Module 04 (Cache):
**Connection:** Effective address determines cache index/tag extraction.
**Example:** Indexed addressing may cause cache thrashing if index strides poorly.

### Bridge to Module 07 (Pipelining):
**Connection:** 
- Variable-length instructions complicate IF (Instruction Fetch) stage
- Memory indirect addressing causes pipeline stalls (multiple memory accesses)
- PC-relative branches cause control hazards

### Bridge to Module 09 (RISC/CISC):
**Connection:**
- RISC: Load/Store architecture (memory access only via LOAD/STORE)
- CISC: Memory operands in arithmetic instructions (e.g., `ADD R1, [1000]`)

---

## VIII. THE FINAL CHECKPOINT

### 5-Second Snap-Checks:

1. **Instruction Count Formula:** 3-addr < 2-addr < 1-addr < 0-addr
2. **Memory Access Count:** Immediate=0, Register=0, Direct=1, Indirect=1, Memory Indirect=2
3. **PC-Relative:** Target = PC_next + Offset
4. **Indexed Array:** EA = Base + (index × size)
5. **Autoincrement:** Use **then** increment (post)
6. **Autodecrement:** Decrement **then** use (pre)
7. **Stack PUSH:** Pre-decrement (decrement SP, then write)
8. **Stack POP:** Post-increment (read, then increment SP)
9. **Effective Address ≠ Operand Value**
10. **Instruction Length:** Fixed (RISC) vs. Variable (CISC)

---

**Logic Singularity verified for 2026 (IIT-G Standards).**

**Mastery Level: [Sovereign]**

**Would you like to initiate a "Multi-Variable Stress Test" combining this with [Module 07: Pipelining] for addressing mode hazards and branch prediction mastery?**

---

*"The instruction is the atom. The addressing mode is its quantum state."*
