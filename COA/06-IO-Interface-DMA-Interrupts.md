# I/O Interface, DMA & Interrupts | The Communication Singularity

> **The Atomic Truth:** *CPU delegates I/O, regains control via interrupts.*

[Image of CPU, I/O devices, and DMA controller interconnected with interrupt lines and data buses - the I/O ecosystem]

---

## I. THE PATH OF ELEGANCE

### 1.1 I/O Interface Methods

**Three Techniques:**
1. **Programmed I/O:** CPU polls status, transfers data (wastes CPU cycles)
2. **Interrupt-Driven I/O:** Device signals CPU when ready (efficient)
3. **Direct Memory Access (DMA):** Device transfers data directly to/from memory (CPU-free)

---

### 1.2 Programmed I/O (Polling)

**Algorithm:**
```
while (device_status != READY):
    # CPU busy-waits (polling)
    pass
data = device_read()
```

**Disadvantage:** CPU wastes cycles checking status.

**Use Case:** Simple, low-latency devices.

---

### 1.3 Interrupt-Driven I/O ⭐

**Mechanism:**
1. CPU initiates I/O operation
2. CPU continues other work
3. Device sends **interrupt** when done
4. CPU saves state, executes **Interrupt Service Routine (ISR)**
5. CPU resumes original work

**Interrupt Handling:**
```
1. Save PC and processor state
2. Disable interrupts (optional)
3. Identify interrupt source (polling or vectored)
4. Execute ISR
5. Restore state, enable interrupts
6. Return from interrupt (RTI)
```

**Interrupt Priority:** Higher priority interrupts can preempt lower priority.

**Advantage:** CPU does useful work while waiting.

**Disadvantage:** Interrupt overhead for each byte/word.

---

### 1.4 Direct Memory Access (DMA) ⭐⭐

**The Problem:** Even with interrupts, CPU transfers data word-by-word (slow for large transfers).

**DMA Solution:** Hardware controller transfers data **directly** between device and memory without CPU.

**DMA Steps:**
1. **CPU initiates:** Set DMA registers (source, destination, count)
2. **DMA transfers:** Controller moves data block (CPU freed)
3. **DMA interrupts:** Signal CPU when transfer complete

**DMA Registers:**
- **Address Register:** Memory address for transfer
- **Count Register:** Number of bytes/words to transfer
- **Control Register:** Transfer direction (read/write), mode

**DMA Modes:**
- **Burst Mode:** DMA takes bus control, transfers entire block (fast, CPU blocked)
- **Cycle Stealing:** DMA steals cycles from CPU as needed (slower, less intrusive)
- **Transparent Mode:** DMA transfers when bus is idle (slowest, no CPU impact)

---

### 1.5 Memory-Mapped I/O vs. I/O-Mapped I/O

**Memory-Mapped I/O:**
- Devices assigned memory addresses
- Use same load/store instructions as memory
- **Example:** `LW R1, 0xFF00` reads from device at address 0xFF00

**I/O-Mapped I/O (Port-Mapped):**
- Separate address space for I/O
- Special instructions (`IN`, `OUT`)
- **Example:** `IN R1, PORT_5` reads from port 5

**Advantage of Memory-Mapped:**
- No special instructions needed
- Richer addressing modes available

**Advantage of I/O-Mapped:**
- Doesn't consume memory address space

---

## II. THE 2026 ADVERSARIAL VAULT

### Trap #1: DMA vs. Interrupt Confusion
**Setup:** "Does DMA eliminate interrupts?"

**Truth:** NO. DMA **reduces** interrupts (one per block instead of one per word), but final interrupt still needed.

---

### Trap #2: DMA Cycle Stealing Impact on CPU
**Setup:** "With DMA, CPU performance is unaffected."

**Truth:** Cycle stealing **does** impact CPU (bus contention), but much less than programmed I/O.

---

### Trap #3: Interrupt Latency
**Latency:** Time from interrupt signal to start of ISR.

**Components:**
1. Current instruction completion
2. Save state
3. Identify interrupt source
4. Load ISR address

**Typical: 5-50 cycles.**

---

## III. PERMANENT RECALL

### Mnemonic: "Programmed Polls, Interrupt Informs, DMA Delivers"
- **Programmed I/O:** CPU polls (wastes cycles)
- **Interrupt:** Device informs CPU (efficient)
- **DMA:** Direct delivery (CPU-free)

### Mental Slider: Turn "I/O autonomy" dial from 0 (programmed) → 1 (DMA):
- Watch CPU involvement decrease

---

## IV. THE SOVEREIGNTY DRILLS

### Problem 1 (GATE 2017): DMA Transfer Time
**Device speed:** 1 MB/s, **DMA block:** 4 KB, **DMA setup:** 500 cycles at 1 GHz.

**Transfer time:**
$$\frac{4 \text{ KB}}{1 \text{ MB/s}} = 4 \text{ ms}$$

**Setup overhead:** $\frac{500 \text{ cycles}}{10^9 \text{ Hz}} = 0.5 \mu\text{s}$ (negligible)

**Total:** ~4 ms

---

### Problem 2: Interrupt vs. Polling Efficiency
**Device transfer rate:** 100 bytes/sec, **CPU:** 1 GHz, **Polling loop:** 100 cycles, **Interrupt overhead:** 500 cycles.

**Polling CPU cycles/sec:**
$$100 \text{ bytes/s} \times 100 \text{ cycles} = 10,000 \text{ cycles/s}$$

**Interrupt cycles/sec:**
$$100 \text{ bytes/s} \times 500 \text{ cycles} = 50,000 \text{ cycles/s}$$

**Wait, polling seems better?**

**But:** Polling **continuously** checks, even when no data. Actual polling cost >> 10K.

**Interrupt:** Only costs when data arrives.

**For low data rates:** Interrupt wins.

---

**Logic Singularity verified for 2026 (IIT-G Standards).**

*"I/O: Where hardware learns to work without supervision."*
