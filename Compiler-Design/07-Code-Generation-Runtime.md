# Module 7: Code Generation & Runtime Environment | The Singularity

> **The Atomic Truth:** *"Map IR to machine instructions, manage runtime state."*

---

## 🎯 The Path of Elegance (Root Derivation)

### 7.1 Code Generation Overview

```
[Image of Code Generator Position]
    Optimized IR → CODE GENERATOR → Target Code
                         ↓
                  ┌─────────────────────────┐
                  │ - Instruction Selection │
                  │ - Register Allocation   │
                  │ - Instruction Ordering  │
                  └─────────────────────────┘
```

### Code Generation Tasks

| Task | Description |
|------|-------------|
| **Instruction Selection** | Choose machine instructions |
| **Register Allocation** | Assign variables to registers |
| **Instruction Scheduling** | Order for pipeline efficiency |
| **Addressing Modes** | Select memory access methods |

---

## 📐 7.2 Target Machine Model

### Simple Machine Model

```
[Image of Simple Machine]
    Registers: R0, R1, R2, ..., Rn
    Memory: M[0], M[1], ...
    
    Instruction Format:
    OP dst, src1, src2
    
    Addressing Modes:
    - Register: R
    - Indexed: c(R)    // M[c + contents(R)]
    - Indirect: *R     // M[contents(R)]
    - Immediate: #c
```

### Instruction Costs

| Instruction | Example | Cost |
|-------------|---------|------|
| Register-Register | ADD R1, R2 | 1 |
| Register-Memory | ADD R1, M[x] | 2 |
| Memory-Memory | ADD M[x], M[y] | 3 |

---

## 🔄 7.3 Instruction Selection

### Tree Pattern Matching

**TAC:** t = a + b

**Possible Selections:**
1. `MOV R1, a; MOV R2, b; ADD R1, R2` (3 instructions)
2. `MOV R1, a; ADD R1, b` (2 instructions, if b in memory)
3. `ADD R1, a, b` (1 instruction, if 3-address available)

### Code Templates

**For x = y + z:**
```
Case 1: y and z in registers Ry, Rz
    ADD Rx, Ry, Rz

Case 2: y in register, z in memory
    MOV Rx, Ry
    ADD Rx, z

Case 3: Both in memory
    MOV Rx, y
    ADD Rx, z
```

---

## ⚡ 7.4 Register Allocation

### The Problem

- Registers: Fast but limited
- Memory: Slow but unlimited
- Goal: Maximize register usage, minimize spills

### Register Allocation Strategies

#### Local (Within Basic Block)

**Next-Use Information:**
- At each point, track when each variable is next used
- Prefer to spill variables with distant/no next use

**Algorithm for statement x = y op z:**
1. Get registers for y, z (load if needed)
2. Free register after last use
3. Get register for x (may reuse y or z's register)

#### Global (Across Basic Blocks)

**Graph Coloring:**
1. Build interference graph
   - Node = variable
   - Edge = variables live simultaneously
2. K-color the graph (K = registers)
3. If not K-colorable, spill and retry

### Register Descriptor and Address Descriptor

**Register Descriptor:** What variables are in each register?
```
R1: x, t
R2: y
R3: (empty)
```

**Address Descriptor:** Where is each variable?
```
x: R1, memory
y: R2
t: R1
z: memory only
```

### GetReg Algorithm

```
getReg(I: instruction, L: next-use info):
    // For x = y op z
    
    // Case 1: y is in register R, y not used after I, y ≠ x
    //         Return R (reuse y's register for x)
    
    // Case 2: Empty register available
    //         Return empty register
    
    // Case 3: Spill lowest-score register
    //         Score based on: next-use distance, dirty bit
    //         Save to memory if modified
    //         Return freed register
```

---

## 📊 7.5 Runtime Environment

### Memory Layout

```
[Image of Memory Layout]
High Address
┌─────────────────────────┐
│         Stack           │  ← Grows DOWN
│           ↓             │
├─────────────────────────┤
│                         │
│      Free Space         │
│                         │
├─────────────────────────┤
│           ↑             │
│         Heap            │  ← Grows UP
├─────────────────────────┤
│     Static/Global       │
│         Data            │
├─────────────────────────┤
│         Code            │
│       (Text)            │
└─────────────────────────┘
Low Address
```

### Activation Record (Stack Frame)

```
[Image of Activation Record]
High Addresses
┌─────────────────────────┐
│   Actual Parameters     │  (pushed by caller)
├─────────────────────────┤
│   Return Address        │
├─────────────────────────┤
│   Control Link (Old FP) │ ← Frame Pointer (FP)
├─────────────────────────┤
│   Access Link           │  (for nested scopes)
├─────────────────────────┤
│   Saved Registers       │
├─────────────────────────┤
│   Local Variables       │
├─────────────────────────┤
│   Temporaries           │ ← Stack Pointer (SP)
└─────────────────────────┘
Low Addresses
```

### Calling Convention

**Caller Responsibilities:**
1. Push actual parameters
2. Push return address
3. Jump to callee
4. Pop parameters after return

**Callee Responsibilities:**
1. Save old FP, set new FP
2. Allocate local variables
3. Save registers to be used
4. Execute function body
5. Put return value in designated location
6. Restore registers
7. Restore old FP
8. Return

---

## 🔗 7.6 Parameter Passing

### Call by Value

```
void foo(int x) {    // x is copy
    x = x + 1;       // doesn't affect actual
}

int a = 5;
foo(a);              // a still 5
```

**Implementation:** Copy value to activation record.

### Call by Reference

```
void foo(int &x) {   // x is alias
    x = x + 1;       // affects actual
}

int a = 5;
foo(a);              // a becomes 6
```

**Implementation:** Pass address, dereference in callee.

### Call by Value-Result (Copy-Restore)

1. Copy value in
2. Execute function
3. Copy value out

**Difference from reference:** When actual is aliased or overlapping.

### Call by Name

Textual substitution (lazy evaluation).

**Example:**
```
void swap(name a, name b) {
    int t = a;
    a = b;
    b = t;
}

swap(i, a[i]);  // Problematic!
```

If i=1, a[1]=5:
```
t = i;         // t = 1
i = a[i];      // i = a[1] = 5
a[i] = t;      // a[5] = 1 (NOT a[1]!)
```

---

## 📐 7.7 Scope and Access

### Static (Lexical) Scope

Variable refers to declaration in textually enclosing scope.

**Implementation:** Access links in activation records.

### Dynamic Scope

Variable refers to most recent active declaration.

**Implementation:** Search stack of activation records.

### Static Scoping Example

```
int x = 1;

void foo() {
    print(x);    // Prints 1 (lexically visible x)
}

void bar() {
    int x = 2;
    foo();
}

bar();           // Output: 1
```

### Dynamic Scoping Example

```
int x = 1;

void foo() {
    print(x);    // Prints 2 (dynamically visible x)
}

void bar() {
    int x = 2;
    foo();
}

bar();           // Output: 2 (dynamic scoping)
```

---

## 🏗️ 7.8 Heap Management

### Memory Allocation

**Explicit:** `malloc`/`free`, `new`/`delete`
**Implicit:** Garbage collection

### Allocation Strategies

| Strategy | Description |
|----------|-------------|
| First Fit | Use first block that fits |
| Best Fit | Use smallest block that fits |
| Worst Fit | Use largest block |
| Buddy System | Split/coalesce power-of-2 blocks |

### Garbage Collection

**Mark-and-Sweep:**
1. Mark all reachable objects
2. Sweep: free unmarked objects

**Reference Counting:**
- Track references to each object
- Free when count reaches 0
- Problem: Circular references

**Copying Collection:**
- Divide heap into from-space and to-space
- Copy live objects, flip spaces

---

## 🎭 The Bizarre Mnemonic | "The Function House Party"

*"Function calls are like a HOUSE PARTY:
- **Activation Record** = Guest's belongings bag
- **Stack** = Tower of bags (LIFO)
- **Parameters** = Items you bring to share
- **Local Variables** = Personal items you take out at the party
- **Return Address** = Your home address (where to go after)
- **Control Link** = Address of previous guest's bag (to restore)
- **Call by Value** = You bring a photocopy of your item
- **Call by Reference** = You give keys to your actual item"*

---

## 🏆 The 2026 Adversarial Vault

### Trap 1: The Stack Growth Direction
**Question Pattern:** "Stack pointer after allocating locals?"
**Anti-Solution:** Students forget stack grows down.
**Truth:** SP DECREASES when allocating (grows toward lower addresses).

### Trap 2: The Parameter Order
**Question Pattern:** "Order of parameters on stack for foo(a, b, c)?"
**Anti-Solution:** Students assume left-to-right push.
**Truth:** Depends on calling convention! C pushes right-to-left (c, b, a).

### Trap 3: The Static vs Dynamic Scope
**Question Pattern:** "What does foo print with nested functions?"
**Anti-Solution:** Students assume wrong scoping rule.
**Truth:** Must identify if language uses static or dynamic scoping.

### Trap 4: The Call by Name Trick
**Question Pattern:** "swap(i, a[i]) behavior?"
**Anti-Solution:** Students think it works like reference.
**Truth:** Call by name re-evaluates expression each use. Index changes!

### Trap 5: The Register Spill
**Question Pattern:** "When does spill occur?"
**Anti-Solution:** Students forget live variables.
**Truth:** Spill when all registers hold live variables and new register needed.

### NAT Precision Lock
- Activation record offset: Careful with direction
- Stack calculation: Account for all components

### MSQ Logic Gate | Elimination Rules
1. Stack grows toward lower addresses
2. Static scope = compile-time binding
3. Dynamic scope = runtime binding
4. Call by name ≠ Call by reference

---

## 📊 GATE PYQ Pattern Analysis

| Year | Topic | Marks | Trap Type |
|------|-------|-------|-----------|
| 2023 | Stack Layout | 2 | Offset calculation |
| 2022 | Static vs Dynamic | 2 | Scope identification |
| 2021 | Parameter Passing | 2 | Value-result vs reference |
| 2020 | Activation Records | 1 | Component ordering |

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| Stack direction | Down (to lower addresses) |
| Static scope | Lexical enclosure |
| Call by value | Copy of value |
| Call by reference | Alias to original |

---

## 🧮 Solved Examples

### Example 1: Stack Frame Calculation
**Given:** Function with 3 int parameters (4 bytes each), 2 int locals, return address 4 bytes.

**Activation Record Size:**
- Parameters: 3 × 4 = 12 bytes
- Return address: 4 bytes
- Saved FP: 4 bytes
- Locals: 2 × 4 = 8 bytes
- **Total: 28 bytes**

### Example 2: Static vs Dynamic Scoping
```
int x = 10;

int foo() { return x; }

int bar() {
    int x = 20;
    return foo();
}

print(bar());
```

**Static Scope:** foo sees x=10 → Output: 10
**Dynamic Scope:** foo sees x=20 (most recent) → Output: 20

### Example 3: Code Generation
**TAC:** t1 = a + b; x = t1 * c;

**Code (2 registers available):**
```
MOV R1, a       // R1 = a
ADD R1, b       // R1 = a + b (t1)
MUL R1, c       // R1 = t1 * c
MOV x, R1       // x = R1
```

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Would you like to initiate a **'Multi-Variable Stress Test'** combining Runtime Environment with Optimization for a Rank-1 simulation?*

---
[← Previous: Code Optimization](./06-Code-Optimization.md) | [Back to Index](./README.md) | [Next: Exam Traps & Techniques →](./08-Exam-Traps-Techniques.md)
