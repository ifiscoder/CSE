# Chapter 4: Process Synchronization | The Concurrency Singularity

## The Atomic Truth
**Synchronization = Ordering Concurrent Accesses to Shared State**

---

## 4.1 The Race Condition: First Principles

### The Path of Elegance

**Problem:** Multiple processes/threads accessing shared data concurrently.

**Example:**
```c
int counter = 0;  // Shared variable

// Thread 1        // Thread 2
counter++;         counter++;
```

**Expected:** `counter = 2`
**Actual:** `counter` might be 1 or 2

**Why?** `counter++` is **not atomic**:
```assembly
LOAD  counter, R1   ; R1 = counter
INC   R1            ; R1 = R1 + 1
STORE R1, counter   ; counter = R1
```

**The Race Condition:**
```
Thread 1: LOAD counter (0) → R1=0
Thread 2: LOAD counter (0) → R2=0
Thread 1: INC R1 → R1=1
Thread 2: INC R2 → R2=1
Thread 1: STORE R1 → counter=1
Thread 2: STORE R2 → counter=1  ← WRONG!
```

**The Golden Pivot:** The **critical section** (code accessing shared data) must be **mutually exclusive**.

---

## 4.2 The Critical Section Problem

### The Three Requirements

A solution must satisfy:

1. **Mutual Exclusion:** At most **one** process in critical section at a time.

$$\forall t: |\text{CS}(t)| \leq 1$$

2. **Progress:** If no process in CS, and some processes want to enter, **selection must happen** (no indefinite postponement).

3. **Bounded Waiting:** After a process requests entry, there exists a **bound** on the number of times other processes can enter CS before it.

**The 2026 Adversarial Vault:**

**Trap:** "Mutual exclusion alone solves the problem."
- **FALSE.** Need progress and bounded waiting too.

**Example of Mutual Exclusion without Progress:**
```c
// Lock variable never released → deadlock
lock = 1;  // Forever locked
```

**Example of Progress without Bounded Waiting:**
```c
// Two processes alternate, but process 2 might never enter
while (turn != myTurn);
```

---

## 4.3 Peterson's Solution (Two-Process)

### The Mechanism

```c
bool flag[2] = {false, false};  // Interest flags
int turn = 0;                   // Turn variable

// Process i (i ∈ {0, 1})
void enter_critical_section(int i) {
    int j = 1 - i;
    flag[i] = true;      // Show interest
    turn = j;            // Give priority to other
    while (flag[j] && turn == j);  // Wait
}

void exit_critical_section(int i) {
    flag[i] = false;     // Withdraw interest
}
```

**The Genius:** Two mechanisms:
1. **flag[i]:** Process i wants to enter
2. **turn:** Breaks tie when both want to enter

### Proof of Correctness

**Mutual Exclusion:**

Assume both P0 and P1 in CS simultaneously.

- P0 in CS → `flag[1] == false` OR `turn == 0`
- P1 in CS → `flag[0] == false` OR `turn == 1`

But `flag[0] == true` and `flag[1] == true` (they're in CS).

So `turn == 0` AND `turn == 1` → **Contradiction!**

**Progress:**

If P0 wants to enter and P1 doesn't (`flag[1] == false`), P0's while loop exits immediately.

**Bounded Waiting:**

After P0 sets `flag[0] = true` and `turn = 1`, P1 can enter at most once before P0 enters (because after P1 exits, `flag[1] = false`).

### The 2026 Adversarial Vault

**Trap 1:** "Peterson's solution works on modern hardware."
- **Partially FALSE.** Requires **sequential consistency** (no instruction reordering).
- Modern CPUs reorder instructions → needs **memory barriers**.

**Trap 2:** "Peterson's solution scales to N processes."
- **FALSE** (this version is for 2 processes only).
- **Extension exists** (Lamport's Bakery Algorithm).

**Trap 3:** "Peterson's solution is busy-waiting."
- **TRUE** (spin-lock, wastes CPU cycles).

---

## 4.4 Hardware Solutions

### 1. Disable Interrupts

```c
void enter_critical_section() {
    disable_interrupts();
}

void exit_critical_section() {
    enable_interrupts();
}
```

**How it works:** No context switch possible during CS.

**Problems:**
- **Only works on single-core** (other cores still run)
- **Dangerous** (malicious process can hang system)
- **Inefficient** (prevents all interrupts, not just context switches)

**The Trap:** "Disabling interrupts solves synchronization."
- **Only on uniprocessor systems.**

### 2. Test-and-Set (TAS)

**Hardware Instruction:**
```c
bool test_and_set(bool *target) {
    bool rv = *target;
    *target = true;
    return rv;       // Atomic operation
}
```

**Lock Implementation:**
```c
bool lock = false;

void enter_critical_section() {
    while (test_and_set(&lock));  // Spin until lock acquired
}

void exit_critical_section() {
    lock = false;
}
```

**Properties:**
- **Atomic** (hardware guarantee)
- **Busy-waiting** (spinlock)
- **No bounded waiting** (starvation possible)

### 3. Compare-and-Swap (CAS)

**Hardware Instruction:**
```c
int compare_and_swap(int *value, int expected, int new_value) {
    int temp = *value;
    if (*value == expected)
        *value = new_value;
    return temp;  // Atomic operation
}
```

**Lock Implementation:**
```c
int lock = 0;  // 0 = unlocked, 1 = locked

void enter_critical_section() {
    while (compare_and_swap(&lock, 0, 1) != 0);
}

void exit_critical_section() {
    lock = 0;
}
```

**The Golden Pivot:** CAS is more flexible than TAS (can check expected value before swap).

**Use Case:** Lock-free data structures, atomic counters.

### 4. Fetch-and-Add

**Hardware Instruction:**
```c
int fetch_and_add(int *value, int increment) {
    int temp = *value;
    *value = *value + increment;
    return temp;  // Atomic operation
}
```

**Ticket Lock Implementation:**
```c
int ticket = 0;
int turn = 0;

void enter_critical_section() {
    int my_ticket = fetch_and_add(&ticket, 1);
    while (turn != my_ticket);  // Wait for my turn
}

void exit_critical_section() {
    turn++;
}
```

**Properties:**
- **Guarantees bounded waiting** (FIFO order)
- **Fair** (no starvation)

**The 2026 Adversarial Vault:**

**Question:** "Which hardware primitive guarantees bounded waiting?"

**Answer:** **Fetch-and-Add** (used in ticket lock).
- TAS/CAS alone do **not** guarantee bounded waiting.

---

## 4.5 Semaphores: The Abstraction Layer

### The Atomic Truth
**Semaphore = Integer + Two Atomic Operations**

### Definition

```c
struct semaphore {
    int value;
    Queue waiting_processes;
};

void wait(semaphore *S) {  // Also called P() or down()
    S->value--;
    if (S->value < 0) {
        add_to_queue(S->waiting_processes, current_process);
        block();  // Sleep (no busy-waiting)
    }
}

void signal(semaphore *S) {  // Also called V() or up()
    S->value++;
    if (S->value <= 0) {
        process = remove_from_queue(S->waiting_processes);
        wakeup(process);
    }
}
```

**The Golden Pivot:** Semaphore **atomically** tests and modifies value, **blocking** instead of busy-waiting.

### Types of Semaphores

#### 1. Binary Semaphore (Mutex)

**Value:** 0 or 1

**Use:** Mutual exclusion

```c
semaphore mutex = 1;  // Initialized to 1

void enter_critical_section() {
    wait(mutex);
}

void exit_critical_section() {
    signal(mutex);
}
```

#### 2. Counting Semaphore

**Value:** 0 to N

**Use:** Resource counting (e.g., thread pool with N threads)

```c
semaphore resources = 5;  // 5 available resources

void acquire_resource() {
    wait(resources);
    // Use resource
}

void release_resource() {
    signal(resources);
}
```

### The Semantics

**Semaphore value:**
- **Positive:** Number of resources available
- **Negative:** Absolute value = number of waiting processes

**Example:**
- Initial: `S.value = 2`
- After 5 `wait()` calls: `S.value = -3` (3 processes blocked)

### The 2026 Adversarial Vault

**Trap 1:** "Binary semaphore = Mutex"
- **Mostly TRUE**, but:
  - **Mutex:** Same thread must lock and unlock
  - **Binary Semaphore:** Any thread can signal

**Trap 2:** "Semaphore avoids busy-waiting."
- **TRUE** (uses blocking queue).
- **But:** Implementation of `wait()` and `signal()` must be atomic (might use spinlock internally for short duration).

**Trap 3:** "Initial value of semaphore for mutual exclusion is 0."
- **FALSE.** Must be **1** (one process can enter initially).

---

## 4.6 Classical Synchronization Problems

### 1. Producer-Consumer Problem (Bounded Buffer)

**Scenario:**
- **Producer:** Adds items to buffer
- **Consumer:** Removes items from buffer
- **Buffer:** Fixed size N

**Solution:**

```c
semaphore empty = N;   // Number of empty slots
semaphore full = 0;    // Number of full slots
semaphore mutex = 1;   // Mutual exclusion for buffer access

// Producer
void produce(item) {
    wait(empty);       // Wait for empty slot
    wait(mutex);       // Lock buffer
    add_to_buffer(item);
    signal(mutex);     // Unlock buffer
    signal(full);      // Signal full slot
}

// Consumer
item consume() {
    wait(full);        // Wait for full slot
    wait(mutex);       // Lock buffer
    item = remove_from_buffer();
    signal(mutex);     // Unlock buffer
    signal(empty);     // Signal empty slot
    return item;
}
```

**The Golden Pivot:** Two types of synchronization:
1. **Resource counting:** `empty` and `full`
2. **Mutual exclusion:** `mutex`

**The 2026 Trap:**

**Wrong Order:**
```c
wait(mutex);   // Lock first ← WRONG!
wait(empty);   // Then wait for resource
```

**Why wrong:** If buffer is full, producer holds `mutex` and waits for `empty`, but consumer can't acquire `mutex` to free a slot → **Deadlock!**

**Correct Order:** Wait for resource first, then lock.

---

### 2. Readers-Writers Problem

**Scenario:**
- **Readers:** Read shared data (multiple allowed simultaneously)
- **Writers:** Write shared data (exclusive access required)

**Constraints:**
1. Multiple readers can read simultaneously
2. Writer needs exclusive access (no readers, no writers)

**Solution (Reader-Preference):**

```c
semaphore mutex = 1;       // Protects read_count
semaphore write_lock = 1;  // Protects data
int read_count = 0;        // Number of active readers

// Reader
void reader() {
    wait(mutex);
    read_count++;
    if (read_count == 1)
        wait(write_lock);  // First reader locks writers out
    signal(mutex);
    
    // Read data
    
    wait(mutex);
    read_count--;
    if (read_count == 0)
        signal(write_lock);  // Last reader unlocks
    signal(mutex);
}

// Writer
void writer() {
    wait(write_lock);
    
    // Write data
    
    signal(write_lock);
}
```

**The Problem:** **Writer starvation** (continuous readers prevent writer).

**Solution (Writer-Preference):**

Add another semaphore to prioritize writers:

```c
semaphore read_lock = 1;   // Controls reader entry
semaphore mutex = 1;
semaphore write_lock = 1;
int read_count = 0;
int write_count = 0;

// Reader
void reader() {
    wait(read_lock);
    wait(mutex);
    read_count++;
    if (read_count == 1)
        wait(write_lock);
    signal(mutex);
    signal(read_lock);
    
    // Read
    
    wait(mutex);
    read_count--;
    if (read_count == 0)
        signal(write_lock);
    signal(mutex);
}

// Writer
void writer() {
    wait(mutex);
    write_count++;
    if (write_count == 1)
        wait(read_lock);  // First writer blocks new readers
    signal(mutex);
    
    wait(write_lock);
    
    // Write
    
    signal(write_lock);
    
    wait(mutex);
    write_count--;
    if (write_count == 0)
        signal(read_lock);
    signal(mutex);
}
```

**The 2026 Adversarial Vault:**

**Question:** "In reader-preference solution, how many readers can enter simultaneously?"

**Answer:** **Unlimited** (no cap on `read_count`).

**Question:** "Can deadlock occur in readers-writers solution?"

**Answer:** **NO** (proper semaphore ordering prevents it).

---

### 3. Dining Philosophers Problem

**Scenario:**
- 5 philosophers around circular table
- 5 forks (one between each pair)
- Each philosopher: think → pick up two forks → eat → put down forks → repeat

**Naive Solution (WRONG):**

```c
semaphore fork[5] = {1, 1, 1, 1, 1};

void philosopher(int i) {
    while (true) {
        think();
        wait(fork[i]);           // Pick left fork
        wait(fork[(i+1) % 5]);   // Pick right fork
        eat();
        signal(fork[i]);         // Put down left fork
        signal(fork[(i+1) % 5]); // Put down right fork
    }
}
```

**Problem: Deadlock**

If all 5 philosophers pick up their left fork simultaneously, all wait for right fork forever.

**Solution 1: Asymmetric (Odd-Even)**

```c
void philosopher(int i) {
    while (true) {
        think();
        if (i % 2 == 0) {
            wait(fork[i]);
            wait(fork[(i+1) % 5]);
        } else {
            wait(fork[(i+1) % 5]);
            wait(fork[i]);
        }
        eat();
        signal(fork[i]);
        signal(fork[(i+1) % 5]);
    }
}
```

**Why it works:** Breaks circular wait (at least one philosopher picks up in different order).

**Solution 2: Limit Concurrency**

```c
semaphore room = 4;  // At most 4 philosophers can attempt to eat

void philosopher(int i) {
    while (true) {
        think();
        wait(room);  // Enter room
        wait(fork[i]);
        wait(fork[(i+1) % 5]);
        eat();
        signal(fork[i]);
        signal(fork[(i+1) % 5]);
        signal(room);  // Leave room
    }
}
```

**Why it works:** With only 4 philosophers attempting, at least one can get both forks.

**Solution 3: All-or-Nothing (Atomic)**

```c
semaphore mutex = 1;

void philosopher(int i) {
    while (true) {
        think();
        wait(mutex);  // Critical section for fork acquisition
        wait(fork[i]);
        wait(fork[(i+1) % 5]);
        signal(mutex);
        eat();
        signal(fork[i]);
        signal(fork[(i+1) % 5]);
    }
}
```

**Why it works:** Mutual exclusion ensures no interleaving during fork pickup.

**The 2026 Adversarial Vault:**

**Question:** "What is the minimum number of philosophers that can be simultaneously eating?"

**Answer:** **0** (all thinking).

**Question:** "What is the maximum number of philosophers that can be simultaneously eating?"

**Answer:** **2** (in a circle of 5, at most 2 non-adjacent philosophers can eat).

**Question:** "In Solution 2 (limit concurrency), why limit to 4, not 3?"

**Answer:** 4 is sufficient. With 5 philosophers and 5 forks, if 4 enter, at least one gets both forks. 3 would also work but is more restrictive.

---

## 4.7 Monitors: High-Level Synchronization

### The Atomic Truth
**Monitor = Class with Mutual Exclusion + Condition Variables**

### Structure

```c
monitor BoundedBuffer {
    int buffer[N];
    int count = 0;
    condition not_full, not_empty;
    
    void produce(item) {
        if (count == N)
            wait(not_full);  // Block if full
        buffer[count++] = item;
        signal(not_empty);
    }
    
    item consume() {
        if (count == 0)
            wait(not_empty);  // Block if empty
        item = buffer[--count];
        signal(not_full);
        return item;
    }
}
```

**Properties:**
1. **Automatic mutual exclusion:** Only one method executes at a time
2. **Condition variables:** `wait()` releases monitor lock, `signal()` wakes one waiting thread

**The Golden Pivot:** Monitors **hide** synchronization details from programmer.

### Condition Variables

**Operations:**
- `wait(condition)`: Release monitor lock, sleep
- `signal(condition)`: Wake one waiting thread
- `broadcast(condition)`: Wake all waiting threads

**Signaling Semantics:**

1. **Signal-and-Continue:** Signaler continues, signaled thread waits for monitor to be free
2. **Signal-and-Wait:** Signaler waits, signaled thread runs immediately

**The 2026 Trap:**

**Question:** "Can multiple threads execute monitor methods simultaneously?"

**Answer:** **NO** (mutual exclusion enforced automatically).

**Question:** "After `signal(condition)`, which thread runs next?"

**Answer:** **Depends on semantics** (signal-and-continue vs signal-and-wait).

---

## 4.8 Deadlock vs Starvation vs Race Condition

### The Distinctions

| **Problem** | **Definition** | **Cause** | **Solution** |
|-------------|----------------|-----------|--------------|
| **Race Condition** | Outcome depends on execution order | Unsynchronized shared access | Mutual exclusion |
| **Deadlock** | All processes blocked, waiting for each other | Circular wait | Resource ordering |
| **Starvation** | Process waits indefinitely (others keep running) | Unfair scheduling | Aging, fair queues |

**The Mental Machinery:**
- **Race Condition:** Incorrect result (bug)
- **Deadlock:** No progress (hang)
- **Starvation:** Unfairness (livelock for one process)

---

## 4.9 The Adversarial Vault: Synchronization Traps

### Trap 1: Semaphore Initialization

**Question:** For mutual exclusion, binary semaphore initialized to?

**Answer:** **1** (one process can initially enter).

**Not 0** (all processes would block immediately).

### Trap 2: Signal Before Wait

```c
signal(S);  // S.value = 2
wait(S);    // S.value = 1 (doesn't block)
```

**Effect:** Signal increments value, later wait decrements. **No deadlock**, but semantically wrong (signaling non-existent event).

### Trap 3: Forgetting to Signal

```c
wait(mutex);
// Critical section
// Oops, forgot signal(mutex)
```

**Result:** **Deadlock** (mutex never released).

### Trap 4: Wrong Semaphore Order

**Producer-Consumer deadlock:**
```c
wait(mutex);   // ← WRONG ORDER
wait(empty);
// Critical section
signal(mutex);
signal(full);
```

**Correct:** Wait for resource (`empty`) before locking (`mutex`).

---

## 4.10 Mental Machinery for Permanent Recall

### The Bizarre Mnemonic: "The Restaurant Synchronization"

Imagine a **restaurant**:

- **Critical Section:** Kitchen (only one chef at a time)
- **Semaphore:** Tokens (finite number for entry)
- **Mutex:** Single key to kitchen
- **Condition Variable:** Waiter announces "table ready!" (wait/signal)
- **Race Condition:** Two waiters grabbing same plate
- **Deadlock:** Two chefs, each holding one knife, waiting for the other's knife
- **Starvation:** One customer keeps getting skipped

**The Mental Slider:**
- Left (No sync): Chaos, multiple chefs collide
- Right (Over-sync): Only one chef ever, long waits

### The 5-Second Snap-Check

**Q:** How to synchronize?

| **Scenario** | **Solution** |
|--------------|--------------|
| Protect shared variable | Mutex/Binary semaphore |
| Coordinate producer-consumer | Counting semaphores + mutex |
| Multiple readers, exclusive writer | Readers-writers pattern |
| Resource pool (N resources) | Counting semaphore (init N) |

---

## 4.11 Practice Problems

### MCQ 1: Peterson's Solution

**Q:** In Peterson's solution, if both processes set their flag to true and turn = 0, which process enters CS?

(A) Process 0  
(B) Process 1  
(C) Both  
(D) Neither  

**Solution:**

Process 0: `while (flag[1] && turn == 1)` → `flag[1] = true` but `turn = 0` → exits loop → enters CS

Process 1: `while (flag[0] && turn == 0)` → both conditions true → blocks

**Answer: (A)**

---

### MCQ 2: Semaphore Semantics

**Q:** A counting semaphore is initialized to 3. After 5 `wait()` operations, the value is:

(A) -2  
(B) -5  
(C) 0  
(D) 2  

**Solution:**

Initial: 3
After 5 `wait()`: $3 - 5 = -2$

**Answer: (A)**

---

### MCQ 3: Producer-Consumer

**Q:** In bounded buffer with N=10, `empty=10`, `full=0`, `mutex=1`. After 3 produces and 2 consumes, what is the value of `empty`?

(A) 7  
(B) 8  
(C) 9  
(D) 10  

**Solution:**

Each produce: `wait(empty)` → `empty--`
Each consume: `signal(empty)` → `empty++`

$\text{empty} = 10 - 3 + 2 = 9$

**Answer: (C)**

---

### MCQ 4: Dining Philosophers

**Q:** In the dining philosophers problem with 5 philosophers, the maximum number that can be eating simultaneously is:

(A) 1  
(B) 2  
(C) 3  
(D) 5  

**Solution:**

In a circle of 5, eating requires 2 adjacent forks. Maximum non-overlapping = 2 philosophers (e.g., positions 0 and 2, or 1 and 3).

**Answer: (B)**

---

### NAT 1: Semaphore Calculation

**Q:** Semaphore S initialized to 5. The following operations occur:
- 8 `wait(S)`
- 3 `signal(S)`
- 2 `wait(S)`

How many processes are blocked?

**Solution:**

$S = 5 - 8 + 3 - 2 = -2$

Negative value means 2 processes blocked.

**Answer: 2**

---

### NAT 2: Critical Section Time

**Q:** 10 processes, each needs CS for 5 ms. If only one can be in CS at a time (using semaphore), what is the total time for all to complete their CS?

**Solution:**

Sequential execution: $10 \times 5 = 50$ ms

**Answer: 50**

---

### NAT 3: Reader-Writer

**Q:** In reader-preference readers-writers, 5 readers are reading. A writer arrives and waits. 3 more readers arrive. How many readers are active before writer can proceed?

**Solution:**

Reader-preference allows new readers even if writer is waiting.

$5 + 3 = 8$ readers active.

**Answer: 8**

---

### NAT 4: Binary Semaphore

**Q:** Two processes use a binary semaphore (init=1) for CS. Process 1 executes CS for 10 ms, Process 2 executes CS for 15 ms. If both arrive simultaneously, what is the minimum time for both to complete CS?

**Solution:**

Sequential (mutex): $10 + 15 = 25$ ms

**Answer: 25**

---

## 4.12 The Elite Formulas Summary

### 1. Semaphore Value After Operations

$$S_{\text{final}} = S_{\text{initial}} - N_{\text{wait}} + N_{\text{signal}}$$

If $S_{\text{final}} < 0$, blocked processes = $|S_{\text{final}}|$

### 2. Producer-Consumer Invariants

$$\text{empty} + \text{full} = N$$
$$\text{empty} = N - \text{items\_in\_buffer}$$

### 3. Critical Section Time (N processes, mutex)

$$T_{\text{total}} = \sum_{i=1}^{N} T_{\text{CS}_i}$$

---

## Logic Singularity Verified for 2026 (IIT-G Standards)

**Mastery Level:** Sovereign

**The Core Insight:**
- **Race Condition:** The problem
- **Critical Section:** The protected region
- **Synchronization Primitive:** The solution (locks, semaphores, monitors)

**The Universal Pattern:** All synchronization problems are variations of:
1. **Mutual Exclusion** (one at a time)
2. **Coordination** (ordering of events)
3. **Resource Management** (counting available units)

**Next:** Chapter 5 dissects **Deadlocks**—where you'll learn the four horsemen of the apocalypse (necessary conditions).

**Would you like to initiate a 'Multi-Variable Stress Test' combining synchronization with deadlock scenarios?**
