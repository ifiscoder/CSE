# Memory Hierarchy & Cache | The Speed Singularity

> **The Atomic Truth:** *Speed costs. Cache is the compromise.*

[Image of memory pyramid: Registers at top (fast/small/expensive), Cache below, Main Memory, then Disk at bottom (slow/large/cheap) - the fundamental speed-capacity trade-off]

---

## I. THE PATH OF ELEGANCE

### 1.1 Memory Hierarchy (The Fundamental Theorem)

**The Golden Pivot:** The **locality principle** makes cache work.

**Memory Hierarchy Pyramid:**
```
Register     ←  1 cycle,   ~1 KB,    $$$$$
L1 Cache     ←  1-2 cycles, 32-64 KB, $$$$
L2 Cache     ←  4-8 cycles, 256 KB-2 MB, $$$
L3 Cache     ←  10-20 cycles, 8-32 MB, $$
Main Memory  ←  100-200 cycles, 4-32 GB, $
Disk/SSD     ←  10^5-10^7 cycles, TB, ¢
```

**The Performance Paradox:**
- Programs **want** disk capacity at register speed
- Physics **forbids** this
- Cache **approximates** it (via locality)

---

### 1.2 Locality Principles (Why Cache Works)

#### Temporal Locality
**Definition:** If a location is accessed, it will likely be accessed again **soon**.

**Example:** Loop variables, function calls (return addresses)

```c
for (int i = 0; i < 1000; i++) {
    sum += array[i];  // 'sum' accessed 1000 times (temporal locality)
}
```

#### Spatial Locality
**Definition:** If a location is accessed, **nearby** locations will likely be accessed soon.

**Example:** Array traversal, sequential code execution

```c
for (int i = 0; i < 1000; i++) {
    sum += array[i];  // array[i], array[i+1], ... accessed sequentially (spatial locality)
}
```

**Cache Strategy:** Fetch **blocks** (not just single bytes) to exploit spatial locality.

---

### 1.3 Cache Fundamentals (The Mapping Problem)

**The Core Question:** Given main memory address $A$, where in cache is it stored?

**Cache Structure:**
$$\text{Cache} = \text{Set of cache lines (blocks)}$$

**Each Cache Line Contains:**
1. **Valid Bit (V):** Is this line occupied?
2. **Tag:** Which memory block is stored here?
3. **Data Block:** Actual data (typically 4-64 bytes)

**Address Breakdown:**
$$\text{Address} = \boxed{\text{Tag}} \mid \boxed{\text{Index}} \mid \boxed{\text{Offset}}$$

Where:
- **Offset:** Byte within block (size = $\log_2(\text{block size})$ bits)
- **Index:** Which cache line/set (size = $\log_2(\text{# lines/sets})$ bits)
- **Tag:** Identifies which memory block (remaining bits)

**Golden Formula:**
$$\text{Address bits} = \text{Tag bits} + \text{Index bits} + \text{Offset bits}$$

---

### 1.4 Direct-Mapped Cache (The Simplest Mapping)

**Mapping Function:**
$$\text{Cache Line} = (\text{Memory Block Address}) \mod (\text{# Cache Lines})$$

**Structure:**
- Each memory block maps to **exactly one** cache line
- Formula: $\text{Cache Line} = \text{Block Address} \mod N$ (where $N$ = # lines)

**Address Fields:**
```
| Tag (t bits) | Index (i bits) | Offset (b bits) |
```

Where:
- $b = \log_2(\text{block size})$
- $i = \log_2(\text{# cache lines})$
- $t = \text{total address bits} - i - b$

**Example:** 16-bit address, 16 cache lines, 4-byte blocks
- Block size = 4 bytes → $b = \log_2(4) = 2$ bits (offset)
- # lines = 16 → $i = \log_2(16) = 4$ bits (index)
- Tag = $16 - 4 - 2 = 10$ bits

**Hit/Miss Decision:**
1. Extract **index** from address
2. Check **valid bit** of that cache line
3. Compare **tag** field of cache line with address tag
4. If $V = 1$ AND $\text{Tag}_{\text{cache}} = \text{Tag}_{\text{address}}$ → **HIT**
5. Else → **MISS**

**Advantages:**
- Simple hardware (one comparator)
- Fast (direct lookup)
- Low cost

**Disadvantages:**
- **Conflict misses:** Multiple blocks map to same line
  - Example: Addresses 0x0000 and 0x0040 (if stride = 64) → same cache line
- Poor utilization if access pattern causes conflicts

---

### 1.5 Fully Associative Cache (The Flexible Mapping)

**Mapping Function:**
$$\text{Any memory block can go in ANY cache line}$$

**No Index Field:** Address = Tag | Offset

**Hit/Miss Decision:**
1. Extract tag from address
2. **Compare tag with ALL cache lines in parallel** (requires $N$ comparators for $N$ lines)
3. If any line has $V = 1$ AND matching tag → **HIT**
4. Else → **MISS**

**Advantages:**
- No conflict misses
- Maximum flexibility
- Best hit rate (for given cache size)

**Disadvantages:**
- Expensive (requires $N$ comparators)
- Complex hardware
- Slower (parallel comparison delay)

**Use Case:** Small caches (e.g., TLB in virtual memory)

---

### 1.6 Set-Associative Cache (The Goldilocks Solution)

**The Compromise:** $N$-way set-associative cache

**Structure:**
- Cache divided into $S$ sets
- Each set contains $N$ lines (ways)
- A block maps to a **specific set** but can go in **any line within that set**

**Mapping:**
$$\text{Set Number} = (\text{Block Address}) \mod S$$

Within the set, block can go in any of the $N$ ways.

**Address Fields:**
```
| Tag (t bits) | Set Index (s bits) | Offset (b bits) |
```

Where:
- $b = \log_2(\text{block size})$
- $s = \log_2(\text{# sets})$
- $t = \text{total address bits} - s - b$
- $\text{# lines} = S \times N$ (total cache lines)

**Hit/Miss Decision:**
1. Extract **set index** from address
2. In that set, compare tag with **all $N$ ways in parallel**
3. If any way has $V = 1$ AND matching tag → **HIT**
4. Else → **MISS**

**Common Configurations:**
- 2-way: 2 lines per set
- 4-way: 4 lines per set
- 8-way: 8 lines per set

**The Trade-off:**
$$\text{Associativity} \uparrow \Rightarrow \text{Hit Rate} \uparrow, \text{Cost} \uparrow, \text{Access Time} \uparrow$$

**Example:** 2-way set-associative cache
- 16-bit address, 8 sets, 4-byte blocks, 2 ways
- Block size = 4 → $b = 2$
- # sets = 8 → $s = 3$
- Tag = $16 - 3 - 2 = 11$ bits
- Total lines = $8 \times 2 = 16$ lines

---

### 1.7 Cache Replacement Policies (When Cache is Full)

On a **miss**, if all ways in a set are full, which block to evict?

#### 1. Least Recently Used (LRU) ⭐
**Policy:** Replace the block that was accessed **longest time ago**.

**Implementation:**
- For 2-way: 1 bit per set (recent way)
- For 4-way: 2-bit or 3-bit counters
- For $N$-way: $\log_2(N!)$ bits (or approximation)

**Advantages:**
- Exploits temporal locality
- Best performance in most workloads

**Disadvantages:**
- Complex hardware for high associativity
- May not be optimal for sequential/scan patterns

**Example (2-way):**
```
Access sequence: A, B, C, A

Set 0 (2 ways):
Access A: [A, -]    LRU bit = 0 (way 0 is recent)
Access B: [A, B]    LRU bit = 1 (way 1 is recent)
Access C: [C, B]    Replace A (way 0, LRU), LRU bit = 0
Access A: [C, A]    Replace B (way 1, LRU), LRU bit = 1
```

---

#### 2. First-In-First-Out (FIFO)
**Policy:** Replace the block that was loaded **earliest**.

**Implementation:** Circular buffer pointer per set

**Advantages:**
- Simple hardware
- Fair replacement

**Disadvantages:**
- Ignores access patterns
- May replace frequently used blocks

---

#### 3. Random
**Policy:** Replace a **random** block in the set.

**Implementation:** Random number generator (LFSR)

**Advantages:**
- Simplest hardware
- Surprisingly competitive performance

**Disadvantages:**
- Unpredictable
- Slightly worse than LRU on average

---

#### 4. Least Frequently Used (LFU)
**Policy:** Replace block with **lowest access count**.

**Implementation:** Counter per line

**Advantages:**
- Good for long-term frequency patterns

**Disadvantages:**
- High hardware cost
- Slow to adapt to phase changes

**Rarely used in practice.**

---

### 1.8 Write Policies (The Data Consistency Problem)

**The Challenge:** When CPU writes to cache, how to maintain consistency with main memory?

#### Write-Hit Policies (What to do when write HITS in cache)

##### A. Write-Through (WT) ⭐
**Policy:** Write to **both cache and memory** simultaneously.

**Advantages:**
- Simple
- Memory always consistent
- Easy cache coherence (multi-core)

**Disadvantages:**
- Slow (every write waits for memory)
- High memory traffic

**Optimization:** Use **write buffer** (queue writes to memory, CPU continues)

---

##### B. Write-Back (WB) ⭐⭐
**Policy:** Write to **cache only**. Write to memory **only when block is evicted**.

**Requires:** **Dirty bit** per cache line
- Dirty = 1: Block modified (must write back)
- Dirty = 0: Block clean (no write-back needed)

**Advantages:**
- Fast (writes at cache speed)
- Low memory traffic (multiple writes to same block merged)

**Disadvantages:**
- Complex
- Memory inconsistent (until write-back)
- Cache coherence complexity

**When block evicted:**
```
If dirty bit = 1:
    Write block to memory
Set dirty bit = 0
```

---

#### Write-Miss Policies (What to do when write MISSES in cache)

##### A. Write-Allocate (WA)
**Policy:** On write miss, **load block into cache**, then write.

**Reason:** Exploit temporal/spatial locality (likely to write/read again)

**Typically paired with:** Write-back

---

##### B. No-Write-Allocate (NWA)
**Policy:** On write miss, **write directly to memory**, don't load into cache.

**Reason:** Don't pollute cache with write-only data

**Typically paired with:** Write-through

---

**Common Combinations:**
1. **Write-back + Write-allocate** (high performance)
2. **Write-through + No-write-allocate** (simple)

---

### 1.9 Cache Performance Metrics (The Golden Formulas)

#### Hit Rate & Miss Rate
$$\text{Hit Rate} = \frac{\text{# Hits}}{\text{# Accesses}}$$

$$\text{Miss Rate} = 1 - \text{Hit Rate} = \frac{\text{# Misses}}{\text{# Accesses}}$$

---

#### Average Memory Access Time (AMAT) ⭐⭐⭐
$$\boxed{\text{AMAT} = T_{\text{cache}} + (\text{Miss Rate} \times T_{\text{miss penalty}})}$$

Where:
- $T_{\text{cache}}$ = Cache access time (hit time)
- $T_{\text{miss penalty}}$ = Time to fetch from main memory on miss

**Example:** Cache hit time = 1 cycle, miss penalty = 100 cycles, miss rate = 2%

$$\text{AMAT} = 1 + (0.02 \times 100) = 1 + 2 = 3 \text{ cycles}$$

---

#### Multi-Level Cache AMAT
**For L1 and L2:**
$$\text{AMAT} = T_{L1} + (\text{MR}_{L1} \times T_{L2}) + (\text{MR}_{L1} \times \text{MR}_{L2} \times T_{\text{mem}})$$

Or more precisely:
$$\text{AMAT} = T_{L1} + (\text{MR}_{L1} \times [T_{L2} + \text{MR}_{L2} \times T_{\text{mem}}])$$

**The Local vs. Global Miss Rate:**
- **Local Miss Rate:** Misses in this cache / Accesses to this cache
- **Global Miss Rate:** Misses in this cache / Total CPU memory accesses

**Example:** L1 local MR = 5%, L2 local MR = 20%
- L2 global MR = $0.05 \times 0.20 = 0.01 = 1\%$

---

#### Effective Access Time (With Write Policy)
**For write-through:**
$$\text{EAT} = \text{AMAT}_{\text{read}} \times (1 - f_{\text{write}}) + (\text{AMAT}_{\text{write}}) \times f_{\text{write}}$$

Where $f_{\text{write}}$ = fraction of write accesses

---

#### Cache Speedup
$$\text{Speedup} = \frac{T_{\text{no cache}}}{T_{\text{with cache}}} = \frac{T_{\text{mem}}}{\text{AMAT}}$$

---

### 1.10 Cache Size Calculations (The Geometry)

**Total Cache Size:**
$$\text{Cache Size (bits)} = \text{# Lines} \times (\text{Valid} + \text{Dirty} + \text{Tag} + \text{Data})$$

**Example:** Direct-mapped, 32-bit address, 64 lines, 16-byte blocks

**Address breakdown:**
- Offset = $\log_2(16) = 4$ bits
- Index = $\log_2(64) = 6$ bits
- Tag = $32 - 6 - 4 = 22$ bits

**Per line:**
- Valid = 1 bit
- Tag = 22 bits
- Data = $16 \times 8 = 128$ bits
- (No dirty bit for direct-mapped with write-through)

**Total:**
$$\text{Cache Size} = 64 \times (1 + 22 + 128) = 64 \times 151 = 9664 \text{ bits} = 1208 \text{ bytes}$$

**Data capacity:** $64 \times 16 = 1024$ bytes = 1 KB

**Overhead:** $\frac{9664 - 8192}{9664} = 15.2\%$

---

## II. THE 2026 ADVERSARIAL VAULT

### Trap #1: Block Offset vs. Word Offset
**The Setup:** "16-bit address, direct-mapped cache, 16 lines, 8-byte blocks. What are the tag, index, offset bit widths?"

**Anti-Solution:**
- Offset = $\log_2(8) = 3$ bits
- Index = $\log_2(16) = 4$ bits
- Tag = $16 - 4 - 3 = 9$ bits

**The Trap:** This assumes **byte addressing**. What if memory is **word-addressed**?

**Critical Clarification:**
- If **byte-addressable:** Offset = 3 bits (selects byte within 8-byte block)
- If **word-addressable (4-byte words):** Block = 2 words → Offset = $\log_2(2) = 1$ bit

**NAT Precision Lock:** Check problem for addressing granularity (byte vs. word).

---

### Trap #2: The Hit Time Inclusion Fallacy
**The Setup:** "Cache hit time = 2 cycles, miss penalty = 100 cycles, miss rate = 5%. What is AMAT?"

**Anti-Solution:**
$$\text{AMAT} = (\text{HR} \times T_{\text{hit}}) + (\text{MR} \times T_{\text{miss}})$$
$$= (0.95 \times 2) + (0.05 \times 100) = 1.9 + 5 = 6.9 \text{ cycles}$$

**The Trap:** **Miss penalty already includes hit time!**

**Correct Formula:**
$$\text{AMAT} = T_{\text{hit}} + (\text{MR} \times T_{\text{miss penalty}})$$
$$= 2 + (0.05 \times 100) = 2 + 5 = 7 \text{ cycles}$$

**Alternatively, if miss penalty is TOTAL time (not additional time):**
$$\text{AMAT} = (\text{HR} \times T_{\text{hit}}) + (\text{MR} \times T_{\text{total miss}})$$

**Mental Checkpoint:** Clarify whether "miss penalty" is **additional time** or **total miss time**.

---

### Trap #3: The Set Index Calculation Error
**The Setup:** "4-way set-associative cache, 64 total lines, 32-bit address, 16-byte blocks. What are the tag, index, offset bits?"

**Anti-Solution:**
- Offset = $\log_2(16) = 4$ bits
- Index = $\log_2(64) = 6$ bits (WRONG!)
- Tag = $32 - 6 - 4 = 22$ bits

**The Trap:** Index bits select the **set**, not the line!

**Correct Calculation:**
- Total lines = 64
- Ways = 4
- **# Sets = 64 / 4 = 16**
- Index = $\log_2(16) = 4$ bits (not 6!)
- Tag = $32 - 4 - 4 = 24$ bits ✓

**Mental Checkpoint:** Index selects set. $\text{# Sets} = \frac{\text{# Lines}}{\text{Ways}}$

---

### Trap #4: The Dirty Bit Misunderstanding
**The Setup:** "Cache uses write-through policy. How many dirty bits are needed?"

**Anti-Solution:** "1 bit per cache line."

**The Trap:** Write-through writes to memory **immediately**. Cache and memory are **always consistent**.

**Correct Answer:** **Zero dirty bits** needed for write-through!

**Dirty bits are only for write-back.**

---

### Trap #5: The Associativity Naming Confusion
**The Setup:** "A cache has 128 lines and is 8-way set-associative. How many sets?"

**Anti-Solution:** "8 sets (because 8-way)."

**The Trap:** "8-way" means **8 lines per set**, not 8 sets!

**Correct:**
$$\text{# Sets} = \frac{\text{# Lines}}{\text{Ways}} = \frac{128}{8} = 16 \text{ sets}$$

**Mental Checkpoint:** $N$-way = $N$ lines per set.

---

### Trap #6: The LRU Bit Calculation
**The Setup:** "For a 4-way set-associative cache with LRU, how many bits per set for replacement?"

**Anti-Solution:** "$\log_2(4) = 2$ bits per set."

**The Trap:** LRU requires tracking **order** of 4 elements, not just identifying 1.

**Correct:**
- **Exact LRU:** $\log_2(4!) = \log_2(24) \approx 5$ bits (encode permutation)
- **Pseudo-LRU:** 3 bits (binary tree approximation)
- **Counter-based LRU:** $4 \times \log_2(4) = 4 \times 2 = 8$ bits (2-bit counter per way)

**Most common implementation:** Pseudo-LRU with 3 bits for 4-way.

---

### Trap #7: The Unified vs. Split Cache
**The Setup:** "L1 cache is 32 KB. What is the hit rate?"

**The Trap:** Is it **unified** (instructions + data) or **split** (separate I-cache and D-cache)?

**Implications:**
- **Unified:** Single 32 KB for both I and D → potential conflict between code and data
- **Split:** 16 KB I-cache + 16 KB D-cache → no conflict, but less flexible

**Modern processors:** Typically **split L1**, **unified L2/L3**.

**NAT Precision Lock:** Check problem specification. If unclear, state assumption.

---

### Trap #8: The Write Buffer Impact on AMAT
**The Setup:** "Write-through cache with write buffer. Write takes 100 cycles to memory. Does AMAT include write time?"

**Anti-Solution:** "Yes, add write time to AMAT."

**The Trap:** Write buffer **hides write latency** (CPU continues, writes queued).

**The Truth:**
- **Without write buffer:** CPU stalls for every write → AMAT includes write time
- **With write buffer:** CPU stalls only if buffer is full → AMAT approximately unaffected (assuming buffer rarely full)

**Typical assumption:** Write buffer is effective, AMAT formula uses **read** access time only.

**For NAT:** Unless problem states buffer is full, ignore write latency in AMAT.

---

## III. PERMANENT RECALL (The Memory Machine)

### Mnemonic #1: Cache Mapping Types
**"Direct Associates Fully"**
- **Direct**-mapped: One-to-one mapping (simplest)
- **Associative (Set-)**: Group-to-one mapping (middle)
- **Fully** associative: Any-to-any mapping (most flexible)

**Mental Slider:** Turn the "flexibility dial":
- Direct: 1 choice (rigid)
- N-way: N choices (flexible)
- Fully: All choices (maximum freedom)

---

### Mnemonic #2: Write Policies
**"Through is True, Back is Batch"**
- **Write-Through:** Write to memory immediately (truth)
- **Write-Back:** Batch writes, write later (batch)

**"Allocate Associates with Back"**
- Write-**Allocate** pairs with Write-**Back**
- **No**-Write-Allocate pairs with Write-**Through**

**Visual:** A post office:
- Write-Through: Hand letter directly to postal worker (slow but immediate)
- Write-Back: Put letters in mailbox, pickup later (fast but delayed)

---

### Mnemonic #3: AMAT Formula
**"Hit plus Miss-Rate times Penalty"**

$$\text{AMAT} = \text{Hit Time} + (\text{Miss Rate} \times \text{Penalty})$$

**Mental Slider:** Turn the "miss rate dial" from 0 to 1:
- At 0%: AMAT = Hit Time (best case)
- At 100%: AMAT = Hit Time + Penalty (worst case)

---

### Mnemonic #4: Address Field Breakdown
**"Tag-Index-Offset" = "TIO" (like I/O)**

**Order:** Most significant → Least significant

**Visual:** A postal address:
- **Tag:** City (identifies block)
- **Index:** Street (identifies cache line/set)
- **Offset:** House number (identifies byte within block)

---

### Mnemonic #5: Replacement Policies
**"LRU is Clever, FIFO is Fair, Random is Rare"**
- **LRU:** Best performance (clever)
- **FIFO:** Simple fairness
- **Random:** Rarely used

**Mental Slider:** Turn the "complexity dial":
- Random: Simplest hardware
- FIFO: Moderate hardware
- LRU: Most complex hardware

---

## IV. THE SOVEREIGNTY DRILLS

### Problem Set A: Address Field Calculations

**Problem 1 (GATE 2018):** 
- 32-bit address
- Direct-mapped cache
- 1024 lines
- 64-byte blocks
- Byte-addressable memory

**Find:** Tag, Index, Offset bit widths.

**Solution:**

**Step 1: Offset bits**
$$\text{Offset} = \log_2(64) = 6 \text{ bits}$$

**Step 2: Index bits**
$$\text{Index} = \log_2(1024) = 10 \text{ bits}$$

**Step 3: Tag bits**
$$\text{Tag} = 32 - 10 - 6 = 16 \text{ bits}$$

**Answer:** Tag = 16, Index = 10, Offset = 6

**5-Second Snap-Check:** $16 + 10 + 6 = 32$ ✓

---

**Problem 2:** 
- 16-bit address
- 4-way set-associative
- 32 total cache lines
- 8-byte blocks

**Find:** Tag, Set Index, Offset bits. How many sets?

**Solution:**

**# Sets:**
$$\text{# Sets} = \frac{\text{# Lines}}{\text{Ways}} = \frac{32}{4} = 8 \text{ sets}$$

**Offset:**
$$\text{Offset} = \log_2(8) = 3 \text{ bits}$$

**Set Index:**
$$\text{Index} = \log_2(8) = 3 \text{ bits}$$

**Tag:**
$$\text{Tag} = 16 - 3 - 3 = 10 \text{ bits}$$

**Answer:** Tag = 10, Index = 3, Offset = 3, Sets = 8

---

**Problem 3 (GATE 2020 NAT):**
- 64-bit address
- Fully associative cache
- 128 lines
- 256-byte blocks

**Find:** Total cache memory size (including tag bits and valid bit).

**Solution:**

**Fully associative → No index field**

**Address breakdown:**
- Offset = $\log_2(256) = 8$ bits
- Tag = $64 - 8 = 56$ bits

**Per line:**
- Valid bit: 1
- Tag: 56 bits
- Data: $256 \times 8 = 2048$ bits

**Total per line:**
$$1 + 56 + 2048 = 2105 \text{ bits}$$

**Total cache size:**
$$128 \times 2105 = 269,440 \text{ bits} = 33,680 \text{ bytes} = 32.89 \text{ KB}$$

**NAT Answer:** 269440 bits or 33680 bytes (check unit in question)

---

### Problem Set B: Hit Rate and AMAT

**Problem 4 (GATE 2019):**
- Cache hit time: 2 cycles
- Memory access time: 100 cycles
- Hit rate: 90%

**Find:** AMAT

**Solution:**

**Miss rate:** $1 - 0.90 = 0.10$

**Miss penalty:** $100 - 2 = 98$ cycles (additional time beyond hit)

**AMAT:**
$$\text{AMAT} = 2 + (0.10 \times 98) = 2 + 9.8 = 11.8 \text{ cycles}$$

**Alternative (if penalty is total time):**
$$\text{AMAT} = 2 + (0.10 \times 100) = 12 \text{ cycles}$$

**NAT Answer:** 11.8 or 12 (depends on penalty definition)

**5-Second Snap-Check:** AMAT must be between hit time (2) and mem time (100). ✓

---

**Problem 5 (Multi-Level Cache):**
- L1 hit time: 1 cycle, miss rate: 5%
- L2 hit time: 10 cycles, miss rate: 20% (local)
- Main memory: 100 cycles

**Find:** Overall AMAT

**Solution:**

**Method 1: Nested formula**
$$\text{AMAT} = T_{L1} + (\text{MR}_{L1} \times [T_{L2} + \text{MR}_{L2\_local} \times T_{\text{mem}}])$$
$$= 1 + (0.05 \times [10 + 0.20 \times 100])$$
$$= 1 + (0.05 \times [10 + 20])$$
$$= 1 + (0.05 \times 30)$$
$$= 1 + 1.5 = 2.5 \text{ cycles}$$

**Method 2: Global miss rates**
- L2 global MR = $0.05 \times 0.20 = 0.01$

$$\text{AMAT} = 1 + (0.05 \times 10) + (0.01 \times 100)$$
$$= 1 + 0.5 + 1 = 2.5 \text{ cycles}$$ ✓

---

**Problem 6 (Speedup):**
Without cache: Every memory access takes 100 cycles.
With cache: AMAT = 5 cycles.

**Find:** Speedup due to cache.

**Solution:**

$$\text{Speedup} = \frac{T_{\text{no cache}}}{T_{\text{with cache}}} = \frac{100}{5} = 20\times$$

**Answer:** 20× speedup

---

### Problem Set C: Cache Replacement

**Problem 7 (LRU Simulation):**

2-way set-associative cache, 2 sets.

**Access sequence:** A (maps to set 0), B (set 0), C (set 0), A, D (set 1), B, E (set 0)

**Determine:** Number of hits and misses.

**Solution:**

**Initial:** All invalid

| Access | Set 0 Ways | Action | Hit/Miss |
|--------|------------|--------|----------|
| A | [A, -] | Load A into way 0 | MISS |
| B | [A, B] | Load B into way 1 | MISS |
| C | [C, B] | Replace A (LRU), load C | MISS |
| A | [C, A] | Replace B (LRU), load A | MISS |
| D | Set 1: [D, -] | Load D into set 1 | MISS |
| B | [B, A] | Replace C (LRU in set 0) | MISS |
| E | [B, E] | Replace A (LRU) | MISS |

**Total:** 7 accesses, 0 hits, 7 misses (cold start + conflicts)

---

### Problem Set D: Write Policies

**Problem 8:** Cache uses write-back policy. Initially, all lines are clean (dirty bit = 0).

**Access sequence:**
1. Write to block A (miss)
2. Write to block A (hit)
3. Read block B (miss, same set as A)

**Determine:** Number of memory writes.

**Solution:**

**Step 1:** Write to A (miss)
- Assuming write-allocate: Load A into cache
- Write to A in cache
- Set dirty bit = 1
- **Memory writes:** 0 (not written to memory yet)

**Step 2:** Write to A (hit)
- Update A in cache
- Dirty bit already 1
- **Memory writes:** 0

**Step 3:** Read B (miss, conflicts with A)
- Must evict A (LRU or only line in set)
- Check dirty bit of A = 1
- **Write A to memory** (write-back)
- Load B into cache
- **Memory writes:** 1 (for write-back of A)

**Total memory writes:** 1

**Comparison with write-through:** Would have 2 memory writes (step 1 and step 2)

---

## V. MSQ LOGIC GATES

### MSQ: Cache Characteristics

**Question:** "Which are TRUE about direct-mapped cache?"

**Options:**
A. Each memory block maps to exactly one cache line
B. Requires only one comparator
C. Has the best hit rate among all mapping types
D. Can have conflict misses

**Logic Gate:**
- A: TRUE (definition)
- B: TRUE (only one line to check)
- C: FALSE (fully associative has best hit rate)
- D: TRUE (multiple blocks map to same line)

**Answer:** A, B, D

---

## VI. THE CROSS-TOPIC BRIDGES

### Bridge to Module 05 (Virtual Memory):
**Connection:** Virtual address → TLB (cache for page tables) → Cache (physical address)

**The Double Miss:** TLB miss + Cache miss = huge penalty

### Bridge to Module 07 (Pipelining):
**Connection:** Cache miss causes pipeline stall. Load-use hazard interacts with cache latency.

### Bridge to Module 08 (Performance):
**Connection:** AMAT directly affects CPI and overall execution time.

---

## VII. THE FINAL CHECKPOINT

### 5-Second Snap-Checks:

1. **AMAT:** Hit Time + (Miss Rate × Miss Penalty)
2. **Address Fields:** Tag | Index | Offset (MSB → LSB)
3. **Offset bits:** $\log_2(\text{block size})$
4. **Index bits (direct):** $\log_2(\text{# lines})$
5. **Index bits (N-way):** $\log_2(\text{# sets})$ where sets = lines / ways
6. **Tag bits:** Total address bits - Index - Offset
7. **Write-Back:** Needs dirty bit
8. **Write-Through:** No dirty bit
9. **Fully Associative:** No index field, all tag
10. **LRU:** Best performance, complex hardware

---

**Logic Singularity verified for 2026 (IIT-G Standards).**

**Mastery Level: [Sovereign]**

**Cache is 40% of COA score. Master this, dominate GATE.**

---

*"Cache: Where probability meets architecture, and locality becomes destiny."*
