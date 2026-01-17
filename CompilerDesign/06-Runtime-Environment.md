# Chapter 6: Runtime Environment

## 🎯 The Atomic Truth
> **"Runtime Environment = Memory Management During Execution"**

---

## 6.1 What is Runtime Environment?

### Definition
The **Runtime Environment** is the structure of memory and registers that supports the execution of a program, managing storage allocation, variable access, and function call mechanics.

```
┌────────────────────────────────────────────────────────────────────────┐
│                       MEMORY ORGANIZATION                              │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   High Address                                                         │
│   ┌──────────────────────────────────────────────────────────────┐    │
│   │                         STACK                                │    │
│   │              (Function calls, local variables)               │    │
│   │                            │                                 │    │
│   │                            ▼                                 │    │
│   │                          grows                               │    │
│   ├──────────────────────────────────────────────────────────────┤    │
│   │                            ▲                                 │    │
│   │                          grows                               │    │
│   │                            │                                 │    │
│   │                          HEAP                                │    │
│   │             (Dynamic allocation: malloc, new)                │    │
│   ├──────────────────────────────────────────────────────────────┤    │
│   │                    STATIC/GLOBAL DATA                        │    │
│   │                (Global variables, constants)                 │    │
│   ├──────────────────────────────────────────────────────────────┤    │
│   │                          CODE                                │    │
│   │                   (Program instructions)                     │    │
│   └──────────────────────────────────────────────────────────────┘    │
│   Low Address                                                          │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 🧠 Analogy: The Restaurant Kitchen
- **Code:** Recipe book (doesn't change)
- **Static Data:** Permanent ingredients storage
- **Heap:** Large flexible storage (walk-in fridge)
- **Stack:** Current orders being prepared (LIFO)

---

## 6.2 Storage Allocation Strategies

### 6.2.1 Static Allocation
**Definition:** Storage allocated at compile time, fixed for program lifetime.

**Used For:**
- Global variables
- Static local variables
- String literals
- Constants

**Properties:**
- Address known at compile time
- Size fixed at compile time
- Efficient access
- Cannot support recursion

### 6.2.2 Stack Allocation
**Definition:** Storage allocated at runtime in LIFO (Last-In-First-Out) order.

**Used For:**
- Local variables
- Function parameters
- Return addresses
- Temporary values

**Properties:**
- Allocated on function call
- Deallocated on function return
- Supports recursion
- Size must be known at call time

### 6.2.3 Heap Allocation
**Definition:** Dynamic storage allocated/deallocated explicitly at runtime.

**Used For:**
- Dynamic data structures
- Objects whose size is unknown at compile time
- Data that must outlive the creating function

**Properties:**
- Allocated by malloc/new
- Deallocated by free/delete
- Flexible size
- Requires garbage collection or manual management

### Comparison Table

| Property | Static | Stack | Heap |
|----------|--------|-------|------|
| **When Allocated** | Compile time | Function call | Explicit request |
| **When Freed** | Never (program end) | Function return | Explicit/GC |
| **Recursion** | No | Yes | Yes |
| **Speed** | Fastest | Fast | Slow |
| **Size** | Fixed | Fixed per call | Dynamic |
| **Fragmentation** | None | None | Possible |

---

## 6.3 Activation Records (Stack Frames)

### Definition
An **Activation Record** (or **Stack Frame**) is a block of memory on the stack that contains all information needed for a single execution of a function.

### Structure of Activation Record

```
┌───────────────────────────────────────────────────────────────┐
│                    ACTIVATION RECORD                          │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│   ┌─────────────────────────────────────────────────────┐    │
│   │            Return Value                              │    │
│   ├─────────────────────────────────────────────────────┤    │
│   │            Actual Parameters                         │    │
│   │            (Arguments)                               │    │
│   ├─────────────────────────────────────────────────────┤    │
│   │            Optional Control Link                     │    │
│   │            (Dynamic Link / Old FP)                   │    │
│   ├─────────────────────────────────────────────────────┤    │
│   │            Optional Access Link                      │    │
│   │            (Static Link)                             │    │
│   ├─────────────────────────────────────────────────────┤    │
│   │            Saved Machine Status                      │    │
│   │            (Return address, registers)               │    │
│   ├─────────────────────────────────────────────────────┤    │
│   │            Local Variables                           │    │
│   ├─────────────────────────────────────────────────────┤    │
│   │            Temporaries                               │    │
│   └─────────────────────────────────────────────────────┘    │
│                                                               │
│   FP (Frame Pointer) ──────────────────►                     │
│   SP (Stack Pointer) ──────────────────► (top of stack)      │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### Components Explained

| Component | Purpose |
|-----------|---------|
| **Return Value** | Space for function's return value |
| **Actual Parameters** | Arguments passed by caller |
| **Control Link** | Pointer to caller's activation record |
| **Access Link** | Pointer to enclosing scope (nested functions) |
| **Saved Status** | Return address, saved registers |
| **Local Variables** | Function's local data |
| **Temporaries** | Intermediate computation results |

### Frame Pointer vs Stack Pointer

| Pointer | Symbol | Points To | Used For |
|---------|--------|-----------|----------|
| **Frame Pointer** | FP | Fixed location in frame | Accessing locals/params |
| **Stack Pointer** | SP | Top of stack | Push/pop operations |

**Why FP?** 
- SP changes during execution (push/pop)
- FP is stable reference within a function

---

## 6.4 Function Call Sequence

### Calling Sequence (Before Call)

```
1. Caller evaluates actual parameters
2. Caller saves any registers it needs preserved
3. Caller pushes parameters (right to left usually)
4. Caller pushes return address
5. Caller jumps to callee
```

### Entry Sequence (Start of Callee)

```
6. Callee saves old FP (control link)
7. Callee sets new FP = SP
8. Callee allocates space for locals (SP -= size)
9. Callee saves callee-saved registers
```

### Exit Sequence (End of Callee)

```
10. Callee places return value
11. Callee restores callee-saved registers
12. Callee sets SP = FP (deallocate locals)
13. Callee restores old FP
14. Callee returns to caller
```

### Return Sequence (After Return)

```
15. Caller pops parameters
16. Caller retrieves return value
17. Caller restores its registers
```

### Visual Call Sequence Example

```
main() {
    int x = 5;
    int result = foo(x, 10);
}

foo(int a, int b) {
    int y = a + b;
    return y;
}
```

**Stack During foo Execution:**
```
        ┌────────────────────┐
        │   Temporaries      │ ◄── SP
        ├────────────────────┤
        │   y (local)        │
        ├────────────────────┤
        │   Saved registers  │
        ├────────────────────┤
        │   Return address   │
        ├────────────────────┤
        │   Old FP (main)    │ ◄── FP (points here)
        ├────────────────────┤
        │   b = 10 (param)   │
        ├────────────────────┤
        │   a = 5 (param)    │
        ╞════════════════════╡ ── main's frame
        │   result (local)   │
        ├────────────────────┤
        │   x = 5 (local)    │
        ├────────────────────┤
        │   main's saved regs│
        ├────────────────────┤
        │   ...              │
        └────────────────────┘
```

---

## 6.5 Parameter Passing Mechanisms

### 6.5.1 Call by Value
**Definition:** Actual parameter's VALUE is copied to formal parameter.

**Properties:**
- Changes to formal don't affect actual
- Simple and safe
- May be expensive for large data

```c
void swap(int a, int b) {    // Copies received
    int t = a; a = b; b = t;  // Only local copies swapped
}

int x = 1, y = 2;
swap(x, y);                   // x=1, y=2 (unchanged!)
```

### 6.5.2 Call by Reference
**Definition:** ADDRESS of actual parameter is passed.

**Properties:**
- Formal is alias for actual
- Changes to formal affect actual
- Efficient for large data

```c
void swap(int &a, int &b) {   // References received
    int t = a; a = b; b = t;   // Actual variables swapped
}

int x = 1, y = 2;
swap(x, y);                    // x=2, y=1 (swapped!)
```

### 6.5.3 Call by Copy-Restore (Call by Value-Result)
**Definition:** Value copied in, copied back out.

**Properties:**
- Copy value at call
- Copy value back at return
- Different from reference when aliasing occurs

```
void proc(int a, int b) {
    a = a + 1;
    b = b + 1;
}

int x = 0;
proc(x, x);    // Pass x twice

Call by Reference: x = 2 (both refs point to x)
Call by Copy-Restore: x = 1 (last copy-back wins)
```

### 6.5.4 Call by Name (Lazy Evaluation)
**Definition:** Actual parameter is substituted textually (like macro).

**Properties:**
- Evaluated each time accessed
- Can have unusual side effects
- Used in Algol 60

```
procedure swap(a, b);
    integer t;
    t := a; a := b; b := t;
end;

swap(i, A[i]);  // If i changes in body, A[i] refers to new index!
```

### 🎯 GATE Comparison Table

| Mechanism | What's Passed | Changes Visible? | Efficiency |
|-----------|--------------|------------------|------------|
| **Value** | Copy of value | No | O(n) copy |
| **Reference** | Address | Yes | O(1) |
| **Copy-Restore** | Copy in, copy out | Yes (at end) | O(n) copy ×2 |
| **Name** | Expression (thunk) | Yes | Evaluated each use |

---

## 6.6 Access Links (Static Links)

### Problem
How does a nested function access variables from enclosing functions?

### Solution: Access Links
Chain of pointers from inner function to each enclosing function's activation record.

### Example
```pascal
program main;
    var x: integer;
    
    procedure A;
        var y: integer;
        
        procedure B;
            var z: integer;
        begin
            z := x + y;  (* How does B access x and y? *)
        end;
        
    begin
        B();
    end;
    
begin
    A();
end;
```

### Stack with Access Links
```
┌──────────────────────────┐
│  B's Activation Record   │
│  Access Link ─────────┐  │ ◄── Points to A's frame
│  z, other locals      │  │
├──────────────────────────┤
│  A's Activation Record   │ ◄─┘
│  Access Link ─────────┐  │     Points to main's frame
│  y, other locals      │  │
├──────────────────────────┤
│  main's Activation Rec   │ ◄─┘
│  x, other locals         │
└──────────────────────────┘
```

### Accessing Variables (Using Nesting Depth)
To access variable at nesting level n from current level m:
1. Follow (m - n) access links
2. Use offset within that frame

---

## 6.7 Displays (Alternative to Access Links)

### Definition
A **Display** is an array where Display[i] points to the most recent activation record at nesting level i.

### Advantages
- O(1) access to any enclosing scope
- No chain following needed

### Disadvantages
- Extra maintenance on call/return
- Size limited to maximum nesting depth

### Display Management
```
On entering level n:
    saved_display[n] = Display[n]
    Display[n] = FP

On exiting level n:
    Display[n] = saved_display[n]
```

---

## 6.8 Heap Management

### 6.8.1 Heap Allocation

**First Fit:** Find first block that fits
**Best Fit:** Find smallest block that fits
**Worst Fit:** Find largest block (leaves bigger remainder)

### 6.8.2 Fragmentation

**External Fragmentation:** Free memory scattered in small pieces
**Internal Fragmentation:** Allocated block larger than needed

### 6.8.3 Garbage Collection

**Definition:** Automatic reclamation of unreachable memory.

#### Mark and Sweep
```
Phase 1 (Mark):
    - Start from roots (globals, stack)
    - Mark all reachable objects

Phase 2 (Sweep):
    - Scan all objects
    - Free unmarked objects
```

#### Reference Counting
```
- Each object has count of references to it
- When count becomes 0, free object
- Problem: Cannot detect cycles
```

#### Copying Collection
```
- Divide heap into two halves
- Copy live objects from one half to other
- Compacts memory
```

### 🎯 GATE Trap: Reference Counting Cycles
```
A.next = B
B.next = A
A = null
B = null
// A and B still have count = 1 (each other)
// Memory leaked! Reference counting can't detect.
```

---

## 6.9 Symbol Table Organization

### Hash Table Implementation
```
┌─────────────────────────────────────────────┐
│          SYMBOL TABLE (Hash)               │
├─────┬───────────────────────────────────────┤
│  0  │  → [x, int, global] → null           │
├─────┼───────────────────────────────────────┤
│  1  │  → [foo, func, ...] → null           │
├─────┼───────────────────────────────────────┤
│  2  │  → null                               │
├─────┼───────────────────────────────────────┤
│ ... │  ...                                  │
└─────┴───────────────────────────────────────┘
```

### Scope Management with Symbol Table
```
On entering scope:
    Push new table (or mark scope level)

On exiting scope:
    Pop table (or remove entries for this scope)

Lookup:
    Search from innermost scope outward
```

---

## 6.10 Activation Record Size Calculation

### 🎯 GATE Favorite Question

**Problem:** Calculate activation record size for a function.

**Components to Count:**
1. Return value (if needed): 4 bytes
2. Parameters: count × size
3. Control link (saved FP): 4-8 bytes
4. Access link (if needed): 4-8 bytes
5. Return address: 4-8 bytes
6. Local variables: sum of sizes
7. Saved registers: count × register size
8. Temporaries: as needed

### Example
```c
int foo(int a, double b, char c) {
    int x, y;
    double z;
    return x + y;
}
```

**Calculation (32-bit system):**
```
Return value:     4 bytes (int)
Parameters:       4 + 8 + 4 = 16 bytes (with padding)
Control link:     4 bytes
Return address:   4 bytes
Local variables:  4 + 4 + 8 = 16 bytes
Saved registers:  varies

Minimum size ≈ 44 bytes (plus alignment padding)
```

---

## 6.11 Recursion Support

### Why Stack Allocation Enables Recursion
Each recursive call gets its own activation record:

```
factorial(3) calls factorial(2) calls factorial(1)

Stack:
┌──────────────────────┐
│ factorial(1): n=1    │ ◄── Current
├──────────────────────┤
│ factorial(2): n=2    │
├──────────────────────┤
│ factorial(3): n=3    │
├──────────────────────┤
│ main()               │
└──────────────────────┘
```

### Static Allocation Cannot Support Recursion
With static allocation, there's only one copy of each function's variables:
- Second call overwrites first call's data
- Return to first call finds corrupted data

---

## 6.12 GATE Previous Year Patterns

### Pattern 1: Activation Record Contents
**Q:** What is stored in activation record?
**A:** Return value, parameters, links, saved status, locals, temporaries

### Pattern 2: Parameter Passing
**Q:** What is output with call by reference/value/name?
**Approach:** Trace execution with given mechanism

### Pattern 3: Stack Depth
**Q:** Maximum stack depth for recursive function?
**A:** Depth of recursion × activation record size

### Pattern 4: Access Links
**Q:** How many access links followed to access variable?
**A:** (Current nesting level) - (Variable's nesting level)

---

## 📝 Quick Revision Points

1. **Memory:** Code → Static → Heap (grows ↑) → Stack (grows ↓)
2. **Static Allocation:** Compile-time, no recursion
3. **Stack Allocation:** Runtime LIFO, supports recursion
4. **Heap Allocation:** Dynamic, explicit/GC management
5. **Activation Record:** Return value, params, links, status, locals, temps
6. **FP:** Fixed reference in frame; SP: Top of stack
7. **Call by Value:** Copy value, no changes visible
8. **Call by Reference:** Pass address, changes visible
9. **Access Link:** For nested function variable access
10. **Display:** Array for O(1) access to enclosing scopes

---

## 🧠 Mnemonic Summary

### Memory Layout (Bottom to Top)
> **"Code Sits High Stacking"**
> **C**ode → **S**tatic → **H**eap (↑) → **S**tack (↓)

### Parameter Passing
> **"Value Copies, Reference Refers, Name Delays"**

### Activation Record Contents
> **"Return Parameters Control Access Saved Local Temp"**
> (RPCASLT)

### Garbage Collection
> **"Mark the reachable, Sweep the unreachable"**

---

## 🔥 The Adversarial Vault

### Trap 1: Static vs Dynamic Scope
**Q:** What value does inner function see?
- **Static scope:** Variable from lexically enclosing scope
- **Dynamic scope:** Variable from most recent caller

### Trap 2: Copy-Restore with Aliasing
```c
void f(int a, int b) {
    a = 2; b = 3;
}
int x = 0;
f(x, x);  // a and b alias same x
```
- Call by Reference: x = 3 (both modify same location)
- Call by Copy-Restore: x = 3 or 2 (depends on order of copy-back)

### Trap 3: Heap vs Stack
**Q:** Where is array of unknown size stored?
**A:** If alloca/VLA on stack; if malloc on heap

---

## ✅ Self-Assessment Questions

1. Draw activation record for a function with 3 parameters and 2 locals.
2. Show stack state during recursive factorial(4) call.
3. Compare call by value vs call by reference with example.
4. Explain why static allocation cannot support recursion.
5. Draw access link chain for 3-level nested functions.

---

**Next Chapter:** [Code Optimization →](07-Code-Optimization.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
