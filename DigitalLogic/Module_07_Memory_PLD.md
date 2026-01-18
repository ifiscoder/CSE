# Module 07: Memory & PLD | The Storage & Programmability Revolution

> **The Singularity**: Memory is everywhere. Programmable logic democratizes design.

---

## [7.1] Memory Organization | The Addressing Architecture

### The Atomic Truth
**Memory = array of storage cells. Address selects which cell(s). Data reads/written.**

### The Path of Elegance

#### [7.1.1] Memory Basics

**Capacity formula**:
$$\text{Total bits} = \text{# of words} \times \text{bits/word}$$

**Example**: 1K × 8 memory
- 1K words = $2^{10} = 1024$ words
- 8 bits/word
- **Total**: $1024 \times 8 = 8192$ bits = 1 Kilobyte (KB)

**Address lines needed**:
$$\text{# address lines} = \log_2(\text{# words})$$

For 1K words: $\log_2(1024) = 10$ address lines

**Data lines**:
$$\text{# data lines} = \text{bits/word}$$

For 8-bit word: 8 data lines

**Total pins** (rough estimate):
$$\text{Pins} ≈ \text{address lines} + \text{data lines} + \text{control} + \text{power}$$

For 1K × 8: $10 + 8 + 4 + 2 = 24$ pins (typical DIP package)

#### [7.1.2] Memory Organization Types

**1D array**:
- Single row of cells
- Simple but requires many decoder lines for large memories
- Used for small caches

**2D array** (most common):
```
┌─────────────────┐
│  Column Decoder │
└─────────────────┘
       │
  ┌────┴────┐
  │ Memory  │
  │ Array   │
  └────┬────┘
       │
  ┌─────────────────┐
  │   Row Decoder   │
  └─────────────────┘
```

- Reduces decoder complexity: $m$ rows + $n$ columns < $(m \times n)$ cells
- Example: 1K × 8 memory
  - Alternative 1: 1024-to-1 decoder (huge!)
  - Better: 32×32 array with 5-bit row + 5-bit column decoder (manageable)

**3D array** (advanced):
- Used in modern DRAM for stacking
- Multiple layers (e.g., 3D NAND flash)

#### [7.1.3] Access Time & Cycle Time

**Access Time** ($t_{access}$):
- Time from address stable to data available
- Typical: 100-500 ns for RAM, 1-10 ns for cache

**Cycle Time** ($t_{cycle}$):
- Time between consecutive independent accesses
- $t_{cycle} ≥ t_{access}$ (may be longer due to precharge phase)

**Bandwidth**:
$$\text{BW} = \frac{\text{bits accessed}}{t_{cycle}}$$

Example: 1K × 8 memory, $t_{cycle} = 500 \text{ ns}$
$$\text{BW} = \frac{8 \text{ bits}}{500 \text{ ns}} = 16 \text{ Mbit/s}$$

### The 2026 Adversarial Vault

**Trap #1**: "Access time = cycle time"

**False** ❌: Access time ≤ cycle time.
- Access time: "How long to read?"
- Cycle time: "How long until next read?"

---

## [7.2] RAM Types | The Volatile Memories

### The Atomic Truth
**RAM loses data when powered off. Fast but temporary.**

### The Path of Elegance

#### [7.2.1] Static RAM (SRAM)

**Cell Structure**: Cross-coupled latches (flip-flop).

```
     VDD
      │
     ├──→ Q
     │
    [Latch]
     │
     └──→ Q'
```

**Characteristics**:
- **Access time**: 2-5 ns (fast!)
- **Cycle time**: 2-5 ns (same as access)
- **Density**: Low (6-8 transistors/bit)
- **Power**: High (leakage current even in standby)
- **Cost**: Expensive per bit
- **Application**: CPU cache, registers

**Density formula**:
$$\text{Cell area} ≈ 100-200 \text{ nm}^2 \text{ (modern tech)}$$

For 1 Mbit SRAM: Area ≈ 100-200 mm² (compared to 1-10 mm² for DRAM!)

**Gate count per cell**:
- 6 transistors (6T SRAM standard)
- 8 transistors (8T SRAM for low-power)

#### [7.2.2] Dynamic RAM (DRAM)

**Cell Structure**: Single transistor + capacitor.

```
      Gate
       │
    Word Line (address)
       │
    ┌──Transistor─┐
    │             │
    ├─Bit Line    │
    │             │
    └─Capacitor───┘
       │
      GND
```

**Operation**:
1. **Read**: 
   - Activate word line → transistor ON
   - Bit line capacitor charges/discharges (1-0 depending on cell value)
   - Sense amplifier detects small voltage change
   - **Destructive read**: Must restore data (refresh)

2. **Write**:
   - Activate word line
   - Drive bit line to desired level
   - Capacitor charges to that level
   - Deactivate word line (transistor OFF, charge stored)

**Characteristics**:
- **Access time**: 30-100 ns (slower than SRAM)
- **Cycle time**: 30-100 ns
- **Density**: Very high (1 transistor/bit)
- **Power**: Lower than SRAM (minimal leakage, but refresh overhead)
- **Cost**: Cheap per bit
- **Application**: Main memory (RAM in laptops/servers)

**Refresh requirement**:
- Capacitor leaks charge over time
- Must periodically read and restore all cells
- **Refresh period**: 64 ms (DRAM standard)
- **Refresh overhead**: ~2-3% of memory bandwidth

**Capacity calculation** (1Gb DRAM):
- 1 Gb = $10^9$ bits = 1024 Mb
- Typical organization: 256M × 4 or 512M × 2 (high fanout)
- Or: 1024M × 1 (many word lines)

#### [7.2.3] SRAM vs DRAM

| Parameter | SRAM | DRAM |
|-----------|------|------|
| Cell transistors | 6-8 | 1 |
| Density | Low | High |
| Access time | 2-5 ns | 30-100 ns |
| Power (active) | High | Low |
| Power (standby) | High (leakage) | Medium (refresh) |
| Cost/bit | High | Low |
| Use | Cache | Main memory |

**Energy per access** (critical metric):
- SRAM: ~10-100 pJ (higher transistor count, but lower swing)
- DRAM: ~1-10 pJ (lower, but refresh adds up at scale)

### The 2026 Adversarial Vault

**Trap #1**: "DRAM is always slower than SRAM"

**True for access time**, but:
- Careful DRAM design can approach SRAM speed (burst mode, prefetch)
- Multiple banks can provide parallel access

**Trap #2**: "DRAM must refresh constantly"

**Not quite**: Refresh every 64 ms (not real-time).
- 10 ms between rows refreshed = manageable
- But adds complexity and power

---

## [7.3] ROM Types | The Non-Volatile Memories

### The Atomic Truth
**ROM retains data without power. Slow but permanent.**

### The Path of Elegance

#### [7.3.1] Masked ROM (Mask Programmable ROM)

**Structure**: Diodes/transistors wired in specific pattern during manufacturing.

**Characteristics**:
- **Programmable**: Only at fabrication (mask design)
- **Cost**: High NRE (non-recurring engineering), low per-unit
- **Density**: Very high (minimal extra logic)
- **Access time**: 100-500 ns
- **Use**: Consumer products (firmware, bootloaders)

**Capacity example**:
- 64K × 8 masked ROM in single IC
- Cost per unit: $1-5 (amortized across millions)

#### [7.3.2] PROM (Programmable ROM, One-Time Programmable)

**Structure**: All cells have fuses or antifuses.

**Fuse-based**:
- Default: Connected (usually 1)
- Programmed: Blow fuse (disconnect) to get 0
- One-time only (irreversible)

**Antifuse-based**:
- Default: Disconnected (usually 0)
- Programmed: Zap antifuse (connect) to get 1
- Harder to manufacture, but avalanche breakdown is reliable

**Characteristics**:
- **Programmable**: By user (special equipment needed)
- **Cost**: Moderate per unit
- **Access time**: 100-500 ns
- **Use**: Specialized applications, low-volume production

#### [7.3.3] EPROM (Erasable PROM)

**Structure**: Floating-gate transistor (capacitor gate isolated by oxide).

```
       ┌─────┐
       │ FG  │ (Floating Gate - high impedance isolated)
       └─┬───┘
         │
    ┌────┴────┐
    │ Control  │
    │  Gate    │
    └────┬────┘
         │
    Source─Drain (transistor)
```

**Operation**:
- **Erase**: UV light (photons) knock electrons out of floating gate
- **Program**: Hot-electron injection through oxide onto floating gate
- **Read**: Floating gate charge affects threshold voltage

**Characteristics**:
- **Erasable**: UV exposure (~15-20 minutes)
- **Reprogrammable**: Many times (>1000 cycles)
- **Cost**: Moderate per unit
- **Access time**: 100-500 ns
- **Use**: Development, prototyping

**Limitations**:
- Requires UV eraser (special equipment)
- Slow erase (minutes)
- Window required (quartz top for UV)

#### [7.3.4] EEPROM (Electrically Erasable PROM)

**Structure**: Similar to EPROM but different erase mechanism.

**Key difference**: Erase via electrical pulse (not UV).

**Characteristics**:
- **Erasable**: Electrically (fast, ~1-10 ms)
- **Reprogrammable**: Many times (>10,000 cycles)
- **Cost**: Moderate to high per unit
- **Access time**: 1-100 ns (depending on circuit)
- **Use**: Consumer electronics, microcontroller firmware

**Advantages over EPROM**:
- No special equipment needed
- Much faster erase
- Byte-level erase (selective)

**Disadvantages**:
- More complex circuit
- Higher cost
- Lower density (compared to EPROM)

#### [7.3.5] Flash Memory (Modern Standard)

**Structure**: Floating-gate like EEPROM, but block-based erase.

**Key features**:
- **Block erase**: Erase multiple cells simultaneously (not byte-by-byte)
- **NOR Flash**: Random access within block
- **NAND Flash**: Sequential access (cheaper, denser)

**NAND Flash structure** (strings):
```
Bit Line 0  Bit Line 1  ...
   │           │
 [Cell]       [Cell]    <- Row 0
   │           │
 [Cell]       [Cell]    <- Row 1
   │           │
 [Cell]       [Cell]    <- Row 2
   │           │
  GND         GND

All cells in series = bit line string
```

**Advantages**:
- **Density**: Highest (3D NAND stacks 64+ layers)
- **Cost**: Lowest per GB
- **Speed**: Fast read (100+ ns), fast erase (1+ ms per block)
- **Endurance**: 10,000-1,000,000 cycles (depending on type)

**Disadvantages**:
- Block erase leads to **write amplification** (erase extra data to write 1 byte)
- Wear leveling required
- Limited lifetime (cycles)

**Modern variants**:
- **SLC** (Single-Level Cell): 1 bit/cell, best endurance (~100k cycles)
- **MLC** (Multi-Level Cell): 2 bits/cell (~10k cycles)
- **TLC** (Triple-Level Cell): 3 bits/cell (~1k cycles)
- **QLC** (Quad-Level Cell): 4 bits/cell (~100 cycles, but higher density)

#### [7.3.6] ROM Comparison

| Type | Programmable | Erasable | Speed | Density | Cost |
|------|---|---|---|---|---|
| Masked | No | - | Fast | Very High | Very Low (volume) |
| PROM | Once | No | Fast | High | Low |
| EPROM | Many | UV | Fast | High | Moderate |
| EEPROM | Many | Electrical | Fast | Moderate | Moderate-High |
| Flash (NOR) | Many | Block | Very Fast | Moderate | Moderate |
| Flash (NAND) | Many | Block | Fast | Very High | Very Low |

### The 2026 Adversarial Vault

**Trap #1**: "All ROM is non-volatile"

**True** ✓, but Flash can lose data if:
- Power failure during programming
- Cell degradation (leakage increases with age)

**Trap #2**: "NAND Flash faster than NOR Flash"

**False** ❌: NOR is faster (random access). NAND is cheaper/denser.

---

## [7.4] PLA & PAL | The Programmable Logic

### The Atomic Truth
**Programmable logic = AND array + OR array. Implement any Boolean function.**

### The Path of Elegance

#### [7.4.1] PLA (Programmable Logic Array)

**Structure**:
```
Inputs (16)
   │
 [AND array] ← programmable (each AND has connections to each input)
   │
   ├─→ Product term 0
   ├─→ Product term 1
   ├─→ Product term 2
   ...
   │
 [OR array] ← programmable (each OR sums specific product terms)
   │
Outputs (8)
```

**Example (4-input, 2-output)**:

```
Inputs: A, B, C, D
Outputs: F1, F2

F1 = ABC + A'BD + CD
F2 = AB + A'C' + BCD

PLA Programming:
AND Array (each row = one AND gate):
    A B C D → Product Term
    1 1 1 0 → ABC (F1)
    0 1 0 1 → A'BD (F1)
    0 0 1 1 → CD (both)
    1 1 0 0 → AB (F2)
    0 0 1 1 → A'C' (F2)
    1 0 1 1 → BCD (F2)

OR Array:
    P0 P1 P2 P3 P4 P5 → Output
    1  1  1  0  0  0  → F1
    0  0  1  1  1  1  → F2
```

**Characteristics**:
- **Programmable**: AND array AND OR array (flexible)
- **Capacity**: m AND terms × n OR terms
- **Speed**: $t_{pd} = t_{AND} + t_{OR}$ (2 gate delays)
- **Density**: Good (all AND terms and OR terms used)
- **Cost**: Moderate

**Typical PLA**:
- 16-input, 8-output, 48 product terms
- Can implement most practical 4-8 variable functions

#### [7.4.2] PAL (Programmable Array Logic)

**Structure** (improvement over PLA):
```
Inputs (16)
   │
 [AND array] ← PROGRAMMABLE (flexible connections)
   │
   ├─→ Fixed OR array 0 ← each output tied to specific set of AND terms
   ├─→ Fixed OR array 1
   ├─→ Fixed OR array 2
   ...
   │
Outputs (8)
```

**Key difference**: OR array is **fixed**, only AND array is programmable.

**Advantages over PLA**:
- Simpler to manufacture (fixed OR reduces complexity)
- Faster (no delay from programmable OR)
- Cheaper
- "Write once" (fuse-based) easier to implement

**Disadvantage**:
- Less flexible (can't share product terms between outputs)
- May need more product terms for same function

**Example**:
- 16-input PAL
- 8 outputs, each tied to 3 AND terms (3-input OR)
- 32 AND terms total

**vs PLA**:
- PLA: 48 AND terms, fully flexible OR
- PAL: 32 AND terms, dedicated OR
- PAL cheaper and simpler, but may need more terms

#### [7.4.3] Fuse-based Programming (Classical)

**Mechanism**:
- Default: All connections exist (fuses intact)
- Program: Blow specific fuses to disconnect

**Example**:
```
Intact fuse: ─╱╱╱─ (conducts)
Blown fuse:  ────  (open)
```

**Process**:
1. Load fuse pattern into programmer
2. Apply higher voltage/current to blow selected fuses
3. Verify by reading back

**Modern alternative** (Flash-based PAL):
- Use EEPROM/Flash cells instead of fuses
- Reprogrammable
- In-circuit programmable (ICP)

### The 2026 Adversarial Vault

**Trap #1**: "PAL is simpler than PLA"

**True** ✓ (fixed OR array), but:
- PAL may need more AND terms
- Trade-off: Simplicity vs flexibility

**Trap #2**: "PLA can implement ANY function with unlimited inputs"

**False** ❌:
- Limited by # of AND terms (product terms)
- Each AND term can implement only one monomial (product)
- If function needs more monomials than AND terms available → can't implement

**Example**: 
- ABCD + A'B'C'D' + ... (many disjoint terms)
- If only 8 AND terms available → can implement only 8 monomials

---

## [7.5] FPGA Basics | The Reconfigurable Logic

### The Atomic Truth
**FPGA = thousands of logic blocks + programmable interconnect. Reconfigurable hardware.**

### The Path of Elegance

#### [7.5.1] FPGA Architecture

**Components**:

1. **Logic Blocks (LBs)** or **Configurable Logic Blocks (CLBs)**:
   - 4-input LUT (Look-Up Table) → implements any 4-variable function
   - Or 6-input LUT (modern)
   - Flip-flops for sequential logic

2. **Programmable Interconnect**:
   - Routing matrix between blocks
   - Allows any block to connect to any other

3. **I/O Blocks**:
   - Interface with external signals
   - Include pull-ups, configurable voltage levels

4. **Memory Blocks**:
   - Embedded RAM (configurable as FIFO, cache, etc.)

5. **Special Blocks** (modern FPGAs):
   - Multiply-accumulate (MAC) units
   - DSP cores
   - High-speed I/O (SERDES)

**Example FPGA**:
```
┌────────────────────────────────┐
│  ┌──────────────────────────┐  │
│  │   CLB Grid (e.g., 40×40) │  │
│  │ ┌──┐ ┌──┐ ┌──┐ ┌──┐     │  │
│  │ │  │ │  │ │  │ │  │ ...  │  │
│  │ └──┘ └──┘ └──┘ └──┘     │  │
│  │ ┌──┐ ┌──┐ ┌──┐ ┌──┐     │  │
│  │ │  │ │  │ │  │ │  │ ...  │  │
│  │ └──┘ └──┘ └──┘ └──┘     │  │
│  │ ...                       │  │
│  └──────────────────────────┘  │
│  ┌─ I/O Blocks (around edge)   │
│  ┌─ Memory Blocks              │
└────────────────────────────────┘
```

#### [7.5.2] LUT (Look-Up Table)

**Principle**: 4-input LUT = 16-bit memory (one row for each input combo).

```
Inputs: A, B, C, D (4 bits)
Output: F = any function of A,B,C,D

Truth table (16 rows):
Address (ABCD) | Content (F)
000            | 1
001            | 0
010            | 1
...
111            | 0

LUT is 16×1 ROM!
```

**Implementation**:
- 4:16 decoder
- 16 × 1-bit memory (16 SRAM cells or fuses)
- 16:1 MUX to select output

**Total gates**: ~50-100 equivalent gates per LUT

**Versatility**: Can implement:
- Boolean functions: AND, OR, XOR, majority, etc.
- Arithmetic: Half adder, multiplexer
- Storage (if you add FF): Counter, shift register

#### [7.5.3] CLB (Configurable Logic Block)

**Modern CLB structure**:
- Two LUTs (6-input each)
- Two flip-flops
- Combinational and registered outputs
- Carry chain (for arithmetic)

**Capacity**: Single CLB can implement:
- 2 independent 4-variable functions
- 1 function + state bit (with FF)
- Small counter

#### [7.5.4] FPGA Gate Capacity

**Typical modern FPGA**:
- **Xilinx Artix-7** (small): 215K LUTs
- **Xilinx Kintex-7** (medium): 478K LUTs
- **Xilinx Virtex-7** (large): 1.4M LUTs

**Equivalent gates**:
$$\text{Gate count} ≈ (\text{# LUTs}) \times 50-100$$

Example: 100K LUTs ≈ 5-10 million gates (equivalent to large ASIC!)

**Practical capacity** (after routing overhead):
- Typically 60-70% of theoretical (rest consumed by routing)

#### [7.5.5] FPGA vs ASIC

| Aspect | FPGA | ASIC |
|--------|------|------|
| NRE cost | Low (software) | High (masks, fabrication) |
| Unit cost | High ($50-5000) | Low ($1-50 at volume) |
| Design time | Weeks | Months-years |
| Reconfigurable | Yes | No |
| Speed | Moderate (100 MHz - 1 GHz) | High (1-10 GHz) |
| Power | Moderate-high | Very low |
| Break-even volume | ~10k units | >1M units |

**Decision**:
- **FPGA**: Prototyping, low-volume, need flexibility
- **ASIC**: High-volume, performance-critical, cost-sensitive

### The 2026 Adversarial Vault

**Trap #1**: "FPGA always slower than ASIC"

**Usually true**, but:
- Modern FPGA ~500 MHz - 1 GHz (fast!)
- ASIC ~1-10 GHz (faster, but design complexity)
- For some applications, FPGA speed sufficient

**Trap #2**: "FPGA can implement ANY circuit"

**True logically**, but:
- Limited by LUT count
- Large circuits may not fit
- Routing congestion may prevent logic placement

---

## [7.6] Master Formula Sheet

### Memory Capacity

$$\text{Total bits} = 2^{\text{# address lines}} \times \text{bits/word}$$

$$\text{Address lines} = \log_2(\text{# words})$$

### Access & Cycle Time

$$\text{Bandwidth} = \frac{\text{bits/word}}{t_{cycle}}$$

### ROM Types Comparison

- **Masked ROM**: Permanent, fast, inflexible
- **PROM**: One-time, fast, user programmable
- **EPROM**: Reusable (UV), moderate cost
- **EEPROM**: Reusable (electrical), flexible
- **Flash**: Modern, cheap, dense

### PLA/PAL Design

**PLA product terms needed**:
$$P ≤ 2^n \quad (\text{for n-variable function, worst case})$$

Typically: $P = $ number of 1s in truth table (or fewer with optimization)

### FPGA Capacity

$$\text{Approx. gates} = (\text{# LUTs}) \times 50-100$$

**Routable fraction** ≈ 60-70%

---

## [7.7] Previous Year Patterns (GATE/ESE)

### GATE 2023-2024

**Q1 (Memory size)**: "32K × 16 RAM. Address lines needed?"
- Answer: $\log_2(32K) = \log_2(2^{15}) = 15$

**Q2 (SRAM vs DRAM)**: "Which is faster?"
- Answer: SRAM (2-5 ns vs 30-100 ns)

**Q3 (FPGA LUT)**: "6-input LUT memory size?"
- Answer: $2^6 = 64$ bits (one row for each input combo)

### ESE 2023

**Q1 (ROM types)**: "Which can erase electrically?"
- Answer: EEPROM, Flash (not PROM, EPROM requires UV)

**Q2 (PLA capacity)**: "4-input, 2-output, how many AND terms min?"
- Depends on specific function (worst case: all 2^4 minterms = 16)

### Common Difficulty Levels

**Easy** (~20%): Memory capacity calculation, ROM type definitions
**Medium** (~60%): PLA synthesis, FPGA architecture understanding
**Hard** (~20%): PLA minimization, complex memory organization

### Topic Weightage

- Memory types: 20%
- Capacity calculations: 15%
- ROM types: 20%
- PLA/PAL design: 20%
- FPGA basics: 15%
- Interfacing: 10%

---

## [7.8] NAT Precision & MSQ Strategy

### NAT Examples

**Q**: "64M × 32 bit DRAM. Address lines?"
- $64M = 64 \times 10^6 = 2^{26}$ (approx, actually $2^{26}$ = 67M)
- More precise: Find $n$ such that $2^n$ ≈ 64M
- $2^{25} = 33.5M, 2^{26} = 67M$ → Use 26 (or be more precise with $\log_2$)

**Q**: "16 product terms in PLA. Max 4-variable functions?"
- One function: $2^4 = 16$ minterms max → fits exactly
- Two functions: Depends on overlap (could need more than 16 terms)
- Conservative answer: **1 maximum**

---

**END OF MODULE 07**
