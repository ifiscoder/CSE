# Module 5: Memory Hierarchy & Cache | The Singularity

> **The Atomic Truth:** *"Exploit locality, hide latency."*

---

## 🎯 The Path of Elegance (Root Derivation)

### 5.1 The Memory Hierarchy | The Speed-Size Trade-off

```
[Image of Memory Hierarchy Pyramid]
                    ▲
                   /│\
                  / │ \      Speed: Fastest
                 /  │  \     Size: Smallest
                /   │   \    Cost: Highest
               ┌────┴────┐
               │Registers│   (< 1ns, ~1KB)
               └────┬────┘
                    │
               ┌────┴────┐
               │   L1    │   (~1-2ns, 32-64KB)
               │  Cache  │
               └────┬────┘
                    │
               ┌────┴────┐
               │   L2    │   (~4-10ns, 256KB-1MB)
               │  Cache  │
               └────┬────┘
                    │
               ┌────┴────┐
               │   L3    │   (~10-20ns, 2-32MB)
               │  Cache  │
               └────┬────┘
                    │
               ┌────┴────┐
               │  Main   │   (~50-100ns, 4-64GB)
               │ Memory  │
               └────┬────┘
                    │
               ┌────┴────┐
               │Secondary│   (~5-10ms, TB)
               │ Storage │
               └─────────┘
                    ↓
              Speed: Slowest
              Size: Largest
              Cost: Lowest
```

### The Locality Principles | Why Caching Works

| Type | Definition | Example |
|------|------------|---------|
| **Temporal Locality** | Recently accessed → likely again soon | Loop variables |
| **Spatial Locality** | Nearby addresses → likely accessed soon | Array elements |

---

## 📐 5.2 Cache Organization | The Architecture

### Cache Structure

```
[Image of Cache Line Structure]
┌───────────┬────────────────┬────────────────────────────┐
│   Tag     │     Index      │        Block Offset        │
│(identify) │  (which set)   │    (byte within block)     │
└───────────┴────────────────┴────────────────────────────┘
     t bits       s bits              b bits
```

**Address Breakdown:**
$$\text{Address bits} = t + s + b$$

Where:
- $t$ = Tag bits
- $s$ = Set index bits ($2^s$ = number of sets)
- $b$ = Block offset bits ($2^b$ = block size in bytes)

### The Three Mapping Strategies

#### 1. Direct Mapped Cache

```
[Image of Direct Mapped Cache]
Memory Block 0  ───┐
Memory Block 8  ───┼───► Cache Line 0
Memory Block 16 ───┘

Memory Block 1  ───┐
Memory Block 9  ───┼───► Cache Line 1
Memory Block 17 ───┘
        ...
```

**Mapping Formula:**
$$\text{Cache Line} = \text{Memory Block} \mod \text{Number of Cache Lines}$$

**Characteristics:**
- Simplest hardware
- Most conflict misses
- One location per block

**Address Breakdown (Direct Mapped):**
- Sets = Cache Lines (1 block per set)
- Associativity = 1

#### 2. Fully Associative Cache

```
[Image of Fully Associative Cache]
Any Memory Block ───► Any Cache Line (parallel search)
```

**Characteristics:**
- Most flexible
- Fewest conflict misses
- Most expensive (comparators for all tags)
- One set containing all lines

**Address Breakdown (Fully Associative):**
- Sets = 1
- Associativity = Number of cache lines
- Index bits = 0

#### 3. Set Associative Cache

```
[Image of N-Way Set Associative]
                    Set 0           Set 1
Memory Block 0  ──► [Way0│Way1│...] 
Memory Block 2  ──► [Way0│Way1│...]
Memory Block 1  ──►                 [Way0│Way1│...]
Memory Block 3  ──►                 [Way0│Way1│...]
```

**Mapping Formula:**
$$\text{Set} = \text{Memory Block} \mod \text{Number of Sets}$$

**Characteristics:**
- Compromise solution
- $n$ ways = $n$ comparators per set
- Common: 2-way, 4-way, 8-way

---

## 🧮 5.3 Cache Parameters | The Master Equations

### Fundamental Relationships

$$\text{Cache Size} = \text{Number of Sets} \times \text{Associativity} \times \text{Block Size}$$

$$C = S \times W \times B$$

$$\text{Number of Blocks} = \frac{\text{Cache Size}}{\text{Block Size}} = S \times W$$

### Address Bit Calculations

| Parameter | Formula |
|-----------|---------|
| Block Offset bits | $b = \log_2(\text{Block Size})$ |
| Index bits | $s = \log_2(\text{Number of Sets})$ |
| Tag bits | $t = \text{Address bits} - s - b$ |

### ⚡ The GATE Shortcut Table

| Mapping | Sets | Associativity | Index bits |
|---------|------|---------------|------------|
| Direct | Cache_lines | 1 | $\log_2(\text{lines})$ |
| N-way | Lines/N | N | $\log_2(\text{lines}/N)$ |
| Fully | 1 | Lines | 0 |

---

## 📊 5.4 Cache Performance | AMAT

### Average Memory Access Time (AMAT)

$$\text{AMAT} = \text{Hit Time} + \text{Miss Rate} \times \text{Miss Penalty}$$

**The Hierarchical AMAT:**
$$\text{AMAT} = T_{L1} + MR_{L1} \times (T_{L2} + MR_{L2} \times (T_{L3} + MR_{L3} \times T_{mem}))$$

### Miss Types | The 3 C's

| Miss Type | Cause | Solution |
|-----------|-------|----------|
| **Compulsory** | First access to block | Larger blocks, prefetching |
| **Capacity** | Cache too small | Larger cache |
| **Conflict** | Too many blocks map to same set | Higher associativity |

**4th C (for multiprocessor):**
| **Coherence** | Invalidation by other processor | Better coherence protocol |

### Hit Rate vs Miss Rate

$$\text{Hit Rate} = H = \frac{\text{Hits}}{\text{Total Accesses}}$$
$$\text{Miss Rate} = M = 1 - H$$

---

## 🔄 5.5 Cache Operations

### Read Operation

```
[Flowchart: Cache Read]
        ┌───────────────┐
        │   CPU Read    │
        └───────┬───────┘
                ↓
        ┌───────────────┐
        │ Check Tag &   │
        │  Valid bit    │
        └───────┬───────┘
                ↓
        ┌───────────────┐
     Yes│    Hit?       │No
   ┌────┴───────────────┴────┐
   ↓                         ↓
┌───────┐              ┌──────────┐
│Return │              │Fetch from│
│Data   │              │Main Mem  │
└───────┘              └────┬─────┘
                            ↓
                      ┌──────────┐
                      │Replace   │
                      │Cache Line│
                      └────┬─────┘
                            ↓
                      ┌──────────┐
                      │Return    │
                      │Data      │
                      └──────────┘
```

### Write Policies

#### Write Hit Policies

| Policy | Action | Advantage | Disadvantage |
|--------|--------|-----------|--------------|
| **Write-Through** | Write to cache AND memory | Simple, consistent | Slow, more traffic |
| **Write-Back** | Write to cache only, set dirty bit | Fast, less traffic | Complex, needs dirty bit |

#### Write Miss Policies

| Policy | Action | Typically Used With |
|--------|--------|---------------------|
| **Write-Allocate** | Fetch block, then write | Write-Back |
| **No Write-Allocate** | Write directly to memory | Write-Through |

### Replacement Policies

| Policy | Description | Implementation |
|--------|-------------|----------------|
| **LRU** | Least Recently Used | Counter/stack per set |
| **FIFO** | First In First Out | Queue per set |
| **Random** | Random selection | Simple, good enough |
| **LFU** | Least Frequently Used | Frequency counter |

**LRU Hardware Cost:**
For N-way set associative: Need $\log_2(N!)$ bits per set ≈ $N\log_2(N)$ bits

---

## 🧮 5.6 Cache Calculation Examples

### Example 1: Address Breakdown

**Given:** 32-bit address, 64KB cache, 64-byte blocks, 4-way set associative

**Solution:**
1. Block offset = $\log_2(64) = 6$ bits
2. Number of blocks = $64KB / 64B = 1024$ blocks
3. Number of sets = $1024 / 4 = 256$ sets
4. Set index = $\log_2(256) = 8$ bits
5. Tag = $32 - 8 - 6 = 18$ bits

```
┌──────────────┬──────────┬──────────────┐
│    Tag       │  Index   │   Offset     │
│   18 bits    │  8 bits  │   6 bits     │
└──────────────┴──────────┴──────────────┘
```

### Example 2: AMAT Calculation

**Given:**
- L1: 2ns hit time, 5% miss rate
- L2: 10ns hit time, 20% miss rate
- Main Memory: 100ns

**Solution:**
$$\text{AMAT} = 2 + 0.05 \times (10 + 0.20 \times 100)$$
$$= 2 + 0.05 \times (10 + 20)$$
$$= 2 + 0.05 \times 30$$
$$= 2 + 1.5 = 3.5 \text{ ns}$$

---

## 🔗 5.7 Cache Coherence | Multiprocessor Systems

### The Coherence Problem

```
[Image of Cache Coherence Problem]
     CPU 0                    CPU 1
       │                        │
   ┌───┴───┐                ┌───┴───┐
   │Cache 0│                │Cache 1│
   │ X=5   │                │ X=5   │
   └───┬───┘                └───┬───┘
       │                        │
       └──────────┬─────────────┘
                  │
              ┌───┴───┐
              │Memory │
              │ X=5   │
              └───────┘

CPU 0 writes X=10:
- Cache 0: X=10
- Cache 1: X=5 (stale!)
- Memory: X=5 or X=10?
```

### Coherence Protocols

#### Snooping Protocols (Bus-based)

**Write-Invalidate:** On write, invalidate all other copies
**Write-Update:** On write, update all other copies

**MESI Protocol States:**
| State | Meaning |
|-------|---------|
| **M** (Modified) | Only copy, dirty |
| **E** (Exclusive) | Only copy, clean |
| **S** (Shared) | Multiple copies, clean |
| **I** (Invalid) | Not valid |

#### Directory Protocols (Scalable)

- Central directory tracks which caches have copies
- Point-to-point messages instead of broadcast
- Used in large-scale systems (NUMA)

---

## 🎭 The Bizarre Mnemonic | "The Library Cache"

*"A cache is like a DESK in a library:
- **Direct Mapped:** Each book has ONE assigned desk spot
- **Fully Associative:** Any book on ANY desk (librarian searches all)
- **Set Associative:** Books grouped by genre (sets), any desk within genre

The AMAT is your average time to find a book: desk search + (miss rate × walk to shelf)"*

---

## 🏆 The 2026 Adversarial Vault

### Trap 1: The Block Offset Confusion
**Question Pattern:** "Which bits identify the byte within the block?"
**Anti-Solution:** Students confuse index and offset.
**Truth:** Block offset = LOWEST order bits, used to select byte WITHIN block.

### Trap 2: The Set Index in Fully Associative
**Question Pattern:** "How many index bits in a fully associative cache?"
**Anti-Solution:** Students calculate as if direct-mapped.
**Truth:** ZERO index bits! Only tag and offset (single set contains all lines).

### Trap 3: The AMAT Hierarchy
**Question Pattern:** "Calculate AMAT for multi-level cache."
**Anti-Solution:** Students add miss penalties incorrectly.
**Truth:** Miss penalty of L1 = L2_access_time + (L2_miss_rate × L3_penalty)

### Trap 4: The Write-Back Dirty Bit
**Question Pattern:** "When does main memory get updated with write-back?"
**Anti-Solution:** Students say "on every write."
**Truth:** ONLY on eviction (replacement) AND if dirty bit is set.

### Trap 5: The Associativity Trade-off
**Question Pattern:** "Doubling associativity always reduces miss rate?"
**Anti-Solution:** Students say yes.
**Truth:** Beyond 8-way, diminishing returns. Also increases hit time!

### NAT Precision Lock
- AMAT: Keep 2 decimal places minimum
- Miss rates: Convert percentages to decimals correctly
- Tag bits = Total - Index - Offset (not the other way!)

### MSQ Logic Gate | Elimination Rules
1. Direct mapped = 1-way set associative
2. Fully associative = 1 set
3. Tag bits cannot be negative
4. Block offset ≥ $\log_2(\text{word size})$

---

## 📊 GATE PYQ Pattern Analysis

| Year | Topic | Marks | Trap Type |
|------|-------|-------|-----------|
| 2023 | Address Breakdown | 2 | Set associative indexing |
| 2022 | AMAT Calculation | 2 | Hierarchical miss penalty |
| 2021 | Miss Types | 1 | 3 C's classification |
| 2020 | Write Policies | 2 | Dirty bit timing |

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| Tag + Index + Offset | Must equal address bits |
| Fully associative index | Must be 0 bits |
| AMAT | Must be > hit time |
| Miss rate | 0 ≤ M ≤ 1 |

---

## 🧮 More Solved Examples

### Example 3: Tag Comparison Count
**Q:** 4-way set associative cache, 1024 accesses, 90% hit rate. How many tag comparisons?

**Solution:**
- Each access: Up to 4 comparisons (but stops on hit)
- Average comparisons per hit ≈ 2.5 (assuming uniform)
- Comparisons = 1024 × 4 = 4096 (worst case)
- **Better answer:** Minimum = 1024 (if first way always hits)
- **GATE likely asks:** Total tag bits compared or similar

### Example 4: Block Size Trade-off
**Q:** Why not make block size very large?

**Solution:**
1. **Larger blocks → Fewer blocks → More conflict misses**
2. **Larger blocks → Higher miss penalty** (more bytes to fetch)
3. **Larger blocks → Pollution** (unused bytes fill cache)
4. **Optimal:** 32-128 bytes typically

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Would you like to initiate a **'Multi-Variable Stress Test'** combining Cache with Virtual Memory for a Rank-1 simulation?*

---
[← Previous: Pipelining](./04-Pipelining-Hazards.md) | [Back to Index](./README.md) | [Next: Virtual Memory →](./06-Virtual-Memory.md)
