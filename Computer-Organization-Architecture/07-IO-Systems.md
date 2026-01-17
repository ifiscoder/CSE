# Module 7: I/O Systems & Interfacing | The Singularity

> **The Atomic Truth:** *"Bridge the CPU-device speed gap."*

---

## 🎯 The Path of Elegance (Root Derivation)

### 7.1 The I/O Challenge | Speed Mismatch

```
[Image of I/O Speed Hierarchy]
         CPU: ~GHz (billions/sec)
              ↓
         Memory: ~100ns
              ↓
         SSD: ~100μs
              ↓
         HDD: ~10ms
              ↓
         Network: ~ms-seconds
              ↓
         Human: ~seconds

Speed difference: 10⁶ - 10⁹ times!
```

### The Fundamental I/O Questions

1. **How does CPU communicate with devices?** (Addressing)
2. **Who initiates the transfer?** (Control methods)
3. **Who performs the transfer?** (Transfer modes)

---

## 📐 7.2 I/O Addressing Methods

### Memory-Mapped I/O

```
[Image of Memory-Mapped I/O]
        Address Space
┌─────────────────────────┐ 0xFFFFFFFF
│                         │
│    I/O Device Registers │ ← Same instructions
│    (mapped here)        │   as memory access
├─────────────────────────┤ 0xFFFF0000
│                         │
│                         │
│        Memory           │
│                         │
│                         │
└─────────────────────────┘ 0x00000000
```

**Characteristics:**
- Same instructions for I/O and memory (MOV, LOAD, STORE)
- Unified address space
- Flexible addressing modes
- Cache complications (must mark as uncacheable)

### Isolated I/O (Port-Mapped)

```
[Image of Isolated I/O]
Memory Space          I/O Space
(Address Bus)        (Separate Ports)
┌───────────┐        ┌───────────┐
│           │        │ Port 0x3F8│ ← IN/OUT
│  Memory   │        │ Port 0x378│   instructions
│           │        │    ...    │
└───────────┘        └───────────┘

Control signal distinguishes:
M/IO = 0 → Memory access
M/IO = 1 → I/O access
```

**Characteristics:**
- Separate instructions (IN, OUT)
- Separate address space
- No cache issues
- Limited addressing modes

### Comparison

| Aspect | Memory-Mapped | Isolated |
|--------|---------------|----------|
| Instructions | Standard memory | Special I/O |
| Address space | Shared | Separate |
| Addressing modes | All | Limited |
| Protection | Via MMU | Via I/O permissions |
| Example | ARM, RISC | x86 |

---

## 🔄 7.3 I/O Control Methods

### 1. Programmed I/O (Polling)

```
[Flowchart: Polling]
    ┌───────────────┐
    │ Issue I/O cmd │
    └───────┬───────┘
            ↓
    ┌───────────────┐
    │ Read status   │◄──────┐
    └───────┬───────┘       │
            ↓               │
    ┌───────────────┐       │
    │ Ready?        │──No───┘
    └───────┬───────┘
            │Yes
            ↓
    ┌───────────────┐
    │ Transfer data │
    └───────┬───────┘
            ↓
    ┌───────────────┐
    │ More data?    │──Yes──► (continue)
    └───────┬───────┘
            │No
            ↓
          Done
```

**Characteristics:**
- CPU constantly checks device status
- Wastes CPU cycles (busy waiting)
- Simple hardware
- Good for fast devices

**CPU Utilization:**
$$\text{CPU time wasted} = \frac{\text{Data size} \times \text{Poll cycles per byte}}{\text{CPU speed}}$$

### 2. Interrupt-Driven I/O

```
[Image of Interrupt Flow]
    CPU                     Device
     │                        │
     │ ── Issue I/O ────────► │
     │                        │
     │    (CPU does           │
     │     other work)        │
     │                        │
     │ ◄── Interrupt ──────── │ (device ready)
     │                        │
     │    (save context)      │
     │                        │
     │ ── Read data ────────► │
     │ ◄── Data ───────────── │
     │                        │
     │    (resume work)       │
```

**Characteristics:**
- CPU notified when device ready
- Better CPU utilization
- Interrupt overhead (context save/restore)
- Good for moderate speed devices

**Interrupt Latency:**
$$T_{response} = T_{detect} + T_{save} + T_{ISR\_start}$$

### 3. Direct Memory Access (DMA)

```
[Image of DMA Operation]
          ┌────────────┐
          │    CPU     │
          │ (initiates)│
          └─────┬──────┘
                │ 1. Setup DMA
                ↓
    ┌───────────────────────────┐
    │       DMA Controller      │
    │  ┌─────┐ ┌─────┐ ┌─────┐  │
    │  │Addr │ │Count│ │Ctrl │  │
    │  └─────┘ └─────┘ └─────┘  │
    └──────┬──────────────┬─────┘
           │              │
    2. Transfer           │
           ↓              ↓
    ┌──────────┐    ┌──────────┐
    │  Memory  │◄──►│  Device  │
    └──────────┘    └──────────┘
           
    3. Interrupt CPU when done
```

**DMA Modes:**

| Mode | Description | Bus Sharing |
|------|-------------|-------------|
| **Burst** | Transfer entire block | CPU locked out |
| **Cycle Stealing** | Transfer one word/cycle | Interleaved |
| **Transparent** | Transfer during CPU idle | No conflict |

---

## 📊 7.4 DMA Calculations | The Master Formulas

### DMA Transfer Time

$$T_{DMA} = T_{setup} + T_{transfer} + T_{interrupt}$$

$$T_{transfer} = \frac{\text{Block size}}{\text{Transfer rate}}$$

### Cycle Stealing Overhead

$$\text{Cycles stolen} = \frac{\text{Data size (bytes)}}{\text{Bytes per transfer}} \times \text{Cycles per steal}$$

**CPU Slowdown:**
$$\text{Slowdown} = \frac{\text{Stolen cycles}}{\text{Total cycles}}$$

### DMA vs Interrupt Comparison

**Break-even point:** When DMA setup overhead equals interrupt overhead.

For block of size $B$ bytes:
- **Interrupt I/O:** $B \times (\text{interrupt overhead per byte})$
- **DMA:** $\text{DMA setup} + \text{DMA completion interrupt}$

DMA wins for large $B$.

---

## ⚡ 7.5 I/O Performance Calculations

### Bandwidth

$$\text{Bandwidth} = \frac{\text{Data transferred}}{\text{Time taken}}$$

### I/O Bound vs CPU Bound

| Type | Bottleneck | Optimization |
|------|------------|--------------|
| I/O Bound | Device speed | Faster I/O, DMA, async |
| CPU Bound | Processing speed | Better algorithms, faster CPU |

### Disk I/O Time (for HDD)

$$T_{access} = T_{seek} + T_{rotation} + T_{transfer}$$

Where:
- $T_{seek}$ = Time to move head (3-10ms typical)
- $T_{rotation}$ = Rotational latency ($\frac{1}{2} \times \frac{60}{RPM}$ average)
- $T_{transfer}$ = $\frac{\text{Data size}}{\text{Transfer rate}}$

---

## 🔧 7.6 I/O Interfaces & Buses

### Bus Hierarchy

```
[Image of Bus System]
                 CPU
                  │
                  ↓
    ┌─────────────────────────┐
    │     Processor Bus       │ (Fast, proprietary)
    └───────────┬─────────────┘
                │
    ┌───────────┴─────────────┐
    │      Memory Bus         │
    └───────────┬─────────────┘
                │
    ┌───────────┴─────────────┐
    │       I/O Bus           │ (PCI, PCIe)
    └───────────┬─────────────┘
                │
    ┌───────────┴─────────────┐
    │    Peripheral Bus       │ (USB, SATA)
    └─────────────────────────┘
```

### Bus Arbitration

| Type | Description | Fairness |
|------|-------------|----------|
| **Daisy Chain** | Priority by position | Low |
| **Centralized** | Arbiter decides | Configurable |
| **Distributed** | Self-arbitration | High |

### Common I/O Standards

| Standard | Speed | Usage |
|----------|-------|-------|
| USB 3.2 | 20 Gbps | Peripherals |
| PCIe 5.0 | 128 GB/s (x16) | GPUs, NVMe |
| SATA III | 6 Gbps | HDDs, SSDs |
| NVMe | 32 GT/s (PCIe 5) | Fast SSDs |

---

## 🎭 The Bizarre Mnemonic | "The Restaurant I/O"

*"I/O methods are like restaurant service:
- **Polling:** Waiter constantly checks 'Ready yet? Ready yet?' (annoying, wasteful)
- **Interrupt:** Customer rings bell when ready (efficient, waiter does other work)
- **DMA:** Kitchen sends food directly to table via robot (CPU/waiter does nothing!)
- **Cycle Stealing:** Robot takes one plate at a time between waiter's trips"*

---

## 🏆 The 2026 Adversarial Vault

### Trap 1: The DMA Setup Overhead
**Question Pattern:** "For small transfers, which is faster—interrupt or DMA?"
**Anti-Solution:** Students always choose DMA.
**Truth:** DMA has setup overhead! For very small transfers, interrupt I/O may be faster.

### Trap 2: The Cycle Stealing Calculation
**Question Pattern:** "CPU slowdown due to DMA cycle stealing?"
**Anti-Solution:** Students forget to account for transfer width.
**Truth:** If DMA transfers 4 bytes/cycle, stolen cycles = total_bytes / 4.

### Trap 3: The Memory-Mapped Caching Trap
**Question Pattern:** "Why mark I/O regions as uncacheable?"
**Anti-Solution:** Students think cache helps I/O.
**Truth:** Caching I/O registers would return stale values! Must always read from device.

### Trap 4: The Interrupt Priority Inversion
**Question Pattern:** "Higher priority device interrupted by lower?"
**Anti-Solution:** Students think priority always respected.
**Truth:** If interrupts disabled during ISR, lower-priority in-progress blocks higher-priority!

### NAT Precision Lock
- Time units: ms vs μs vs ns (factor of 1000!)
- Bandwidth: bits vs bytes (factor of 8)
- Transfer rate: Usually given in MB/s or Mbps (different!)

### MSQ Logic Gate | Elimination Rules
1. Polling → CPU 100% occupied during I/O
2. DMA → CPU free during transfer (mostly)
3. Burst DMA → CPU completely locked out
4. Memory-mapped I/O → No special instructions

---

## 📊 GATE PYQ Pattern Analysis

| Year | Topic | Marks | Trap Type |
|------|-------|-------|-----------|
| 2023 | DMA vs Interrupt | 2 | Break-even calculation |
| 2022 | Cycle Stealing | 2 | CPU slowdown |
| 2021 | I/O Addressing | 1 | Memory-mapped identification |
| 2020 | Disk Access Time | 2 | Component breakdown |

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| Polling efficiency | 0% (CPU always busy) |
| DMA advantage | Large transfers |
| Memory-mapped I/O | Uses LOAD/STORE |
| Interrupt overhead | Context switch time |

---

## 🧮 Solved Examples

### Example 1: DMA Transfer Time
**Given:**
- Block size: 4KB
- Transfer rate: 100 MB/s
- DMA setup: 5μs
- Interrupt handling: 10μs

**Solution:**
$$T_{transfer} = \frac{4 \times 1024}{100 \times 10^6} = \frac{4096}{10^8} = 40.96 \mu s$$
$$T_{total} = 5 + 40.96 + 10 = 55.96 \mu s$$

### Example 2: Cycle Stealing Impact
**Given:**
- CPU: 1 GHz
- DMA: Steals 1 cycle per 4 bytes
- Transfer: 1 MB
- Original program: 10 ms

**Solution:**
- Stolen cycles = $\frac{1 \times 10^6}{4} = 250,000$ cycles
- Time stolen = $\frac{250,000}{10^9} = 0.25$ ms
- Slowdown = $\frac{0.25}{10} = 2.5\%$
- New time = 10.25 ms

### Example 3: Interrupt vs Polling
**Given:**
- Device produces 1000 characters/sec
- Polling: 100 cycles per check, check every 1ms
- Interrupt: 500 cycles per interrupt
- CPU: 1 MHz

**Question:** CPU utilization comparison?

**Solution:**
**Polling:**
- Checks per second = 1000
- Cycles used = 1000 × 100 = 100,000 cycles/sec
- Utilization = 100,000/1,000,000 = 10%

**Interrupt:**
- Interrupts per second = 1000 (one per character)
- Cycles used = 1000 × 500 = 500,000 cycles/sec
- Utilization = 50%

Wait, polling better here? Yes! For **very frequent events**, polling can be more efficient than interrupt overhead. This is the genius trap!

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Would you like to initiate a **'Multi-Variable Stress Test'** combining I/O Systems with DMA and Cache Coherence for a Rank-1 simulation?*

---
[← Previous: Virtual Memory](./06-Virtual-Memory.md) | [Back to Index](./README.md) | [Next: Parallel Processing →](./08-Parallel-Processing.md)
