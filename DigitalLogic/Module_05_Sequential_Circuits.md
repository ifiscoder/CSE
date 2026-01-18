# Module 05: Sequential Circuits | The Memory Architects

> **The Singularity**: Output depends on present input AND past state (memory exists).

---

## [5.1] Latches | The Atomic Memory

### The Atomic Truth
**Latches are level-triggered. No clock needed. Set/Reset controls state.**

### The Path of Elegance

#### [5.1.1] SR Latch (Set-Reset) using NOR Gates

**Structure**: Cross-coupled NOR gates.

```
    ┌─ NOR ─┐
    │   Q   │
S ──┤       ├─── Q
    │       │
    └───────┘
    ┌───────┐
    │   Q'  │
R ──┤       ├─── Q'
    │       │
    └─ NOR ─┘
```

**Characteristic Table**:
| $S$ | $R$ | $Q(t)$ | $Q'(t)$ | Operation |
|-----|-----|--------|---------|-----------|
| 0 | 0 | Hold | Hold | No change (latch) |
| 0 | 1 | 0 | 1 | Reset |
| 1 | 0 | 1 | 0 | Set |
| 1 | 1 | X | X | Invalid (forbidden) |

**Boolean Equations**:
$$Q(t+1) = S + \overline{R \cdot Q(t)}$$
$$Q'(t+1) = R + \overline{S \cdot Q'(t)}$$

**The Golden Pivot**: When $S=R=0$, latch **holds state** (memory!).

**The Trap**: $S=R=1$ is **metastable**. Outputs undefined until one input goes low first.

#### [5.1.2] SR Latch using NAND Gates

**Structure**: Cross-coupled NAND gates.

**Characteristic Table**:
| $\overline{S}$ | $\overline{R}$ | $Q(t)$ | $Q'(t)$ | Operation |
|---|---|--------|---------|-----------|
| 0 | 0 | 1 | 1 | Invalid (forbidden) |
| 0 | 1 | 1 | 0 | Set |
| 1 | 0 | 0 | 1 | Reset |
| 1 | 1 | Hold | Hold | No change |

**Key Difference**: NAND latch has **active-low** inputs ($\overline{S}$, $\overline{R}$).

#### [5.1.3] SR Latch with Enable (Gated SR Latch)

**Function**: SR latch, but state changes only when enable = 1.

```
S ──┤ AND ├─┐
E ──┤     ├─ S' to SR latch
    └─────┘
    
R ──┤ AND ├─┐
E ──┤     ├─ R' to SR latch
    └─────┘
```

**Gate Count**: 2 AND gates + SR latch = ~6 gates total

#### [5.1.4] D Latch (Data Latch)

**Function**: Capture and hold 1-bit data. Single data input.

**Structure**: 
- D input → S (through NOT)
- D input → R (direct)
- When enable = 1: $Q = D$ (transparent)
- When enable = 0: $Q$ holds previous value

**Truth Table** (E=1):
| $D$ | $Q$ | Operation |
|-----|-----|-----------|
| 0 | 0 | Reset |
| 1 | 1 | Set |

(E=0) → Hold regardless of D

**Gate Count**: D latch = SR latch + 2 AND gates = ~8 gates total

**The Golden Pivot**: D latch eliminates undefined state (no invalid input combination).

### The 2026 Adversarial Vault

**Trap #1**: "S and R cannot both be 1"

**In NOR latch**: TRUE ✓ (forbidden state)
**In NAND latch**: TRUE ✓ (forbidden state, but different convention)

**But GATE asks**: "What happens if $S=R=1$ initially, then $S=0$?"
- Answer: Race condition! Output unpredictable (metastable state).

**Trap #2**: "D latch is a flip-flop"

**False** ❌: D latch is **level-triggered**; flip-flop is **edge-triggered**.
- Latch: Changes while enable = 1
- Flip-flop: Changes only on clock edge

**GATE Pattern**: "SR latch with $S=0, R=0, Q(t)=1$. After $S=1$ for 1ns, then $S=0$ again. $Q(t+?)$?"

**Answer**: Still 1 (set state persists due to memory).

**MSQ Logic Gate**: 
- "SR latch can be used as a debouncer" → **TRUE** ✓ (mechanical switches)
- "D latch is faster than SR latch" → **FALSE** (similar speed, same gates)
- "NOR latch is more stable than NAND latch" → **FALSE** (same metastability issue)

**NAT Precision Lock**: 
For "setup time violation in D latch":
- If D changes while enable = 1 close to disable edge
- Output may become metastable
- Recovery time = time to return to stable state

---

## [5.2] Flip-Flops | The Synchronous Memories

### The Atomic Truth
**Flip-flops are edge-triggered. Clock controls state transitions. Synchronous logic foundation.**

### The Path of Elegance

#### [5.2.1] SR Flip-Flop (Clocked SR Latch)

**Structure**: SR latch + AND gates controlled by clock.

```
S ──┤ AND ├─┐
CLK ┤     ├─ S' to SR latch
    └─────┘
```

**Truth Table** (on rising clock edge):
| $S$ | $R$ | $Q(t+1)$ | Operation |
|-----|-----|----------|-----------|
| 0 | 0 | $Q(t)$ | Hold |
| 0 | 1 | 0 | Reset |
| 1 | 0 | 1 | Set |
| 1 | 1 | X | Invalid |

**Gate Count**: 2 AND gates + SR latch = ~6 gates total

#### [5.2.2] JK Flip-Flop (Clocked SR Improved)

**Motivation**: Eliminate undefined state when J=K=1.

**Truth Table** (on rising clock edge):
| $J$ | $K$ | $Q(t+1)$ | Operation |
|-----|-----|----------|-----------|
| 0 | 0 | $Q(t)$ | Hold |
| 0 | 1 | 0 | Reset |
| 1 | 0 | 1 | Set |
| 1 | 1 | $\overline{Q(t)}$ | Toggle |

**The Golden Pivot**: JK flip-flop has **4 useful states** (no forbidden state).

**Boolean Equation** (characteristic equation):
$$Q(t+1) = J \overline{Q(t)} + \overline{K} Q(t)$$

**Structure**: Master-Slave configuration.

```
       Master            Slave
┌─────────┐          ┌─────────┐
│ JK Latch│ ─CLK'──→ │ SR FF   │
│  + Mux  │          │         │
└─────────┘          └─────────┘
    (On CLK=1)          (On CLK=0)
```

**Why Master-Slave?**
- Master latch captures when CLK=1
- Slave latch stores when CLK=0
- Prevents multiple transitions per clock cycle (essential for synchronous design)

**Gate Count**: 2 SR latches + control logic = ~20 gates total

#### [5.2.3] D Flip-Flop (Delayed Data)

**Simplest flip-flop. Captures data at clock edge, holds until next edge.**

**Truth Table**:
| $D$ | $Q(t+1)$ |
|-----|----------|
| 0 | 0 |
| 1 | 1 |

**Characteristic Equation**:
$$Q(t+1) = D$$

**Structure**: Master-slave D latches.

```
D ──┤ XOR ├──┐
    └─────┘  │
             ├─→ Master D-Latch ──┬──→ Slave D-Latch
             │                    │
          EN │                 NOT(EN)
             └────────────────────┘
```

**Setup and Hold Time** (critical timing parameters):

- **Setup time ($t_s$)**: Time D must be stable BEFORE clock edge
- **Hold time ($t_h$)**: Time D must remain stable AFTER clock edge
- **Propagation delay ($t_p$)**: Time for $Q$ to reflect $D$ after clock edge

```
D     ─────────┬────────────
              ts
              
CLK   ────┐
           └─────┐
                 └──
                 
Q      ─────────────┬─────────
                    tp
```

**Typical values** (modern CMOS):
- $t_s ≈ 100-200$ ps
- $t_h ≈ 50-100$ ps
- $t_p ≈ 150-300$ ps

**Gate Count**: 2 D latches + mux = ~16 gates

#### [5.2.4] T Flip-Flop (Toggle)

**Function**: Divides frequency by 2 (counter application).

**Truth Table**:
| $T$ | $Q(t+1)$ |
|-----|----------|
| 0 | $Q(t)$ |
| 1 | $\overline{Q(t)}$ |

**Characteristic Equation**:
$$Q(t+1) = T \overline{Q(t)} + \overline{T} Q(t) = T \oplus Q(t)$$

**Implementation**: JK flip-flop with $J=K=T$.

**Gate Count**: ~12 gates (using JK as base)

#### [5.2.5] T Flip-Flop from D Flip-Flop

**Circuit**:
```
    ┌──────────────────┐
    │                  │
D ──┤ XOR ├─→ D-FF     │
    └─ Q'─┘      │    │
                 Q ───┘
                
T ──→ (to D input, other side)
```

**Equation**: 
$$D = T \oplus Q = T \overline{Q} + \overline{T} Q$$

So next clock edge: $Q(t+1) = D = T \oplus Q(t)$ ✓

### The 2026 Adversarial Vault

**Trap #1**: "JK and SR flip-flops are equivalent"

**False** ❌: JK can toggle (J=K=1), SR cannot (forbidden).

**Trap #2**: "Setup time violation causes slow clock, hold time violation causes metastability"

**Partially true**:
- **Setup time violation**: Flip-flop might not capture $D$ correctly → wrong data
- **Hold time violation**: Metastable state → transition unpredictable

Both are bad!

**Trap #3**: "D flip-flop can be implemented from JK by tying J = D, K = D'"

**True!** ✓
$$Q(t+1) = J \overline{Q(t)} + \overline{K} Q(t) = D \overline{Q(t)} + D Q(t) = D$$

**GATE Pattern**: "2-bit synchronous counter using D flip-flops. Circuit?"

**Logic**:
- $D_0 = \overline{Q_0}$ (always toggle bit 0) → T flip-flop behavior
- $D_1 = Q_0 \oplus Q_1$ (toggle bit 1 only when bit 0 = 1)

**MSQ Logic Gate**: 
- "All flip-flops have same setup time" → **FALSE** (technology dependent)
- "Toggle flip-flop divides frequency exactly by 2" → **TRUE** ✓
- "Flip-flop is universal (can build any circuit)" → **FALSE** (needs gates too)

---

## [5.3] Flip-Flop Conversions | The Transformation Engine

### The Atomic Truth
**Any flip-flop type convertible to any other using combinational logic.**

### The Path of Elegance

#### [5.3.1] Conversion Framework

Given desired flip-flop type with **inputs** → need logic to drive available flip-flop.

**Target** → Available → **Required input logic**

#### [5.3.2] T → JK Conversion

**Given**: T flip-flop (available)
**Want**: JK flip-flop behavior

**Desired characteristic equation (JK)**:
$$Q(t+1) = J \overline{Q(t)} + \overline{K} Q(t)$$

**Available (T)**:
$$Q(t+1) = T \oplus Q(t)$$

**Solution**: Drive T flip-flop with $T = J \overline{Q(t)} + K Q(t)$

**Circuit**:
```
J ──┤ AND ├─┐
Q' ──┤    ├─ OR ──→ T input
K ──┤ AND ├─┐
Q ──┤    ├─ (to T FF)
     └────┘
```

**Gate Count**: 2 AND + 1 OR = 3 gates

#### [5.3.3] D → SR Conversion

**Given**: D flip-flop
**Want**: SR flip-flop behavior

**Target** (SR):
$$Q(t+1) = S + \overline{R} Q(t)$$

**Available** (D):
$$Q(t+1) = D$$

**Solution**: 
$$D = S + \overline{R} Q(t)$$

**Circuit**:
```
S ──┐
    ├─ OR ──→ D input
Q ──┤ AND ├─┐
R' ──────┘
```

**Gate Count**: 1 OR + 1 AND = 2 gates

#### [5.3.4] Conversion Matrix

| From ↓ To → | SR | JK | D | T |
|-------------|-----|-----|-----|-----|
| SR | - | + gate | + gate | + gates |
| JK | + gate | - | + gate | + gate |
| D | + gate | + gate | - | + gate |
| T | + gates | + gates | + gates | - |

**Gate count column** = complexity of conversion.

**Example**: SR → JK needs 3-4 gates
JK → SR needs 1-2 gates (simpler!)

### The 2026 Adversarial Vault

**Trap #1**: "Can convert any flip-flop to any other without loss"

**Mostly true**, but:
- Information loss possible if conversion adds complexity during transitions
- Timing constraints may force extra delay

**Trap #2**: "D from JK always simpler than JK from D"

**False** ❌: Depends on available inputs/outputs!

**GATE Pattern**: "Implement SR flip-flop using D flip-flop. Min gates?"

**Answer**: 
$$D = S + \overline{R} Q$$
- 1 OR gate + 1 AND gate = **2 gates** ✓

**MSQ Logic Gate**: 
- "All flip-flop conversions have same gate overhead" → **FALSE**
- "Conversion preserves synchronous timing" → **TRUE** (if done correctly)

---

## [5.4] Registers | The Multi-Bit Memory

### The Atomic Truth
**Register = n D flip-flops in parallel. Stores $n$-bit data.**

### The Path of Elegance

#### [5.4.1] Basic Register

**Structure**: $n$ D flip-flops, all clocked together.

```
D[0] → D-FF[0] → Q[0]
D[1] → D-FF[1] → Q[1]
...
D[n-1] → D-FF[n-1] → Q[n-1]
                 ↑
                CLK (common)
```

**Function**: On clock edge, $Q = D$ (parallel data capture).

**Gate Count**: $n \times 16$ gates (n D-FF @ ~16 gates each)

#### [5.4.2] Shift Register

**Function**: Serial data input, outputs shift right/left on each clock.

**Serial In - Parallel Out (SIPO)**:
```
S_in → D-FF[0] → D-FF[1] → D-FF[2] → D-FF[3]
                 Q[0]       Q[1]       Q[2]       Q[3]
```

On each clock:
- New bit enters at D-FF[0]
- Data shifts right: Q[0]←S_in, Q[1]←Q[0], Q[2]←Q[1], Q[3]←Q[2]

**Serial In - Serial Out (SISO)**:
Last Q is output: S_out = Q[n-1]

**Parallel In - Serial Out (PISO)**:
```
P[0] ──┤ MUX ├─ D-FF[0]
Shift ──┤    ├─ Q[0] → (to next)
Q[0] ────────┘
```

When Shift=1: Data shifts
When Shift=0: Parallel data loaded

**Gate Count** (SIPO 4-bit):
- 4 D-FF = 64 gates
- 4 MUX (for parallel load) = ~72 gates
- **Total**: ~140 gates

#### [5.4.3] Shift Register Applications

**App #1: Serial to Parallel Conversion**
- Receive serial data on UART → load into shift register → read parallel output

**App #2: Parallel to Serial Conversion**
- Load parallel data → shift out one bit per clock

**App #3: Data Distribution**
- 1 input → N stages → N outputs (delayed copies)

**App #4: Frequency Division**
- Tap any stage for frequency = $f_{clk} / (stage + 1)$

#### [5.4.4] Universal Shift Register

**Function**: Shift left, shift right, parallel load, hold.

**Truth Table**:
| Mode | Operation |
|------|-----------|
| 00 | Hold (no change) |
| 01 | Shift right (serial in → bit[n-1]) |
| 10 | Shift left (serial in → bit[0]) |
| 11 | Parallel load |

**Circuit**: 4:1 MUX per flip-flop input.

```
D[i] ──────┐
Q[i+1] ────┤ MUX ├─ D-FF[i]
Q[i-1] ────┤     ├─ Q[i]
Q[i] ──────┤     │
           └─────┘
           Mode: 2 bits
```

**Gate Count**: 4 MUX ($n \times 18$ gates) + n D-FF ($n \times 16$ gates) = ~34n gates

### The 2026 Adversarial Vault

**Trap #1**: "Shift register is just a counter"

**False** ❌: Counters INCREMENT; shift registers MOVE data.

**Trap #2**: "PISO universal shift register can implement SIPO"

**True** ✓: With mode=10 (shift left), acts like shift right if data fed right-to-left.

**GATE Pattern**: "8-bit shift register, initially 10101010. After 3 right shifts with 0 input?"

**Answer**: 01010101 (original shifted right 3 positions, 0s entered from left)
Wait, that's wrong: 00010101 (shifted right means bits move toward LSB, 0s enter from MSB)

Actually: $10101010 >> 3 = 00010101$ ✓

**MSQ Logic Gate**: 
- "Shift register frequency divider outputs same frequency on all taps" → **FALSE**
- "Universal shift register needs 2-bit mode" → **TRUE**

---

## [5.5] Counters | The Sequence Generators

### The Atomic Truth
**Counter = register with feedback logic. Sequences through states (usually 0→1→...→max→0).**

### The Path of Elegance

#### [5.5.1] Ripple Counter (Asynchronous)

**Structure**: T flip-flops cascaded. Output of one drives CLK of next.

```
CLK → T-FF[0] → Q[0]
        └─────── CLK[1] → T-FF[1] → Q[1]
                            └─────── CLK[2] → T-FF[2] → Q[2]
```

**Behavior** (4-bit binary counter):
```
CLK  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
Q[3] 0  0  0  0  0  0  0  0  1  1  1  1  1  1  1  1  0
Q[2] 0  0  0  0  1  1  1  1  0  0  0  0  1  1  1  1  0
Q[1] 0  0  1  1  0  0  1  1  0  0  1  1  0  0  1  1  0
Q[0] 0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0
```

**Delay**: $T_{delay} = n \times T_{FF}$ (serial propagation)

**Issue**: Glitches during carry propagation.

Example: Transition 7→8 (0111→1000)
- Intermediate states: 0110, 0100, 0000 (before settling to 1000)
- Causes short glitches on output

**Gate Count**: $n$ T-FF = $16n$ gates

#### [5.5.2] Synchronous (Binary) Counter

**Structure**: All flip-flops clocked together. Carry logic drives enable.

```
CLK ──────┬─→ T-FF[0] (always toggle)
          │       │
          ├─→ T-FF[1] ← enable = Q[0]
          │       │
          ├─→ T-FF[2] ← enable = Q[1]·Q[0]
          │       │
          └─→ T-FF[3] ← enable = Q[2]·Q[1]·Q[0]
```

**Truth Table** (4-bit):
```
Clock Q[3] Q[2] Q[1] Q[0]
0     0    0    0    0
1     0    0    0    1
2     0    0    1    0
3     0    0    1    1
4     0    1    0    0
...
15    1    1    1    1
16    0    0    0    0
```

**Delay**: $T_{delay} = T_{FF} + T_{AND}$ (parallel propagation)

**No glitches**: All transitions happen simultaneously.

**Gate Count**: $n$ T-FF + $(n-1)$ AND gates = $16n + 3(n-1)$ ≈ $19n$ gates

#### [5.5.3] Decade Counter (0-9)

**Type**: Counts 0-9, then resets.

**Implementation**: 4-bit synchronous counter with decode logic for reset.

**Reset logic** (when count=10):
$$\text{Reset} = Q[3] \cdot Q[1]$$

(When Q[3]=1 and Q[1]=1, count is 10, 11, 12, or 13; but ripple resets immediately to 0000)

**Gate Count**: ~40 gates

#### [5.5.4] Ring Counter

**Structure**: Single 1 bit, rotates around $n$ stages.

```
1000 → 0100 → 0010 → 0001 → 1000 → ...
```

**Implementation**: $n$-bit shift register with feedback: output of last → input of first.

**Behavior** (4-bit):
```
Clock Q[3] Q[2] Q[1] Q[0]
0     1    0    0    0
1     0    1    0    0
2     0    0    1    0
3     0    0    0    1
4     1    0    0    0
```

**Unique states**: Only 4 out of 16 possible states used.

**Gate Count**: 4 D-FF + 1 feedback path = ~65 gates

#### [5.5.5] Johnson Counter (Twisted Ring)

**Structure**: Like ring counter, but with inverted feedback.

```
1111 → 1110 → 1100 → 1000 → 0000 → 0001 → 0011 → 0111 → 1111 → ...
```

**Unique states**: 8 out of 16 (double ring counter).

**Gate Count**: $n$ D-FF + 1 NOT + feedback = ~65 gates

**Advantage**: Decodes cleanly with simple gates (each output is a 2-input AND).

### The 2026 Adversarial Vault

**Trap #1**: "Asynchronous counter is faster than synchronous"

**False** ❌: Synchronous is faster (no carry propagation delay)!
Asynchronous is simpler (fewer gates).

**Trap #2**: "Decade counter counts 0-10"

**Typically FALSE** ❌: Counts 0-9 (10 states), resets on 10.

**Trap #3**: "Ring counter state = position, Johnson state = position + inversion"

**Approximately true** ✓: Useful for decoding.

**GATE Pattern**: "Design a MOD-12 synchronous counter using 4-bit counter"

**Solution**: 4-bit counter naturally goes 0-15. Add decode logic for count=12 → reset.
$$\text{Reset} = Q[3] \cdot Q[2]$$

**MSQ Logic Gate**: 
- "Synchronous counter faster than ripple" → **TRUE**
- "Ring counter uses all 2^n states" → **FALSE** (uses only n states)
- "Johnson counter is self-clearing" → **FALSE** (needs external logic or specific init)

---

## [5.6] State Machines | The Control Logic

### The Atomic Truth
**State machine = FSM with states, transitions, inputs, outputs. Describes sequential behavior.**

### The Path of Elegance

#### [5.6.1] Mealy vs Moore Machines

**Moore Machine**:
- Output depends ONLY on current state
- Output = $f(\text{state})$
- Output changes only on state transition

**Mealy Machine**:
- Output depends on state AND input
- Output = $f(\text{state, input})$
- Output can change without state transition

**Comparison**:

| Aspect | Moore | Mealy |
|--------|-------|-------|
| Output timing | After state change | Same clock cycle (combinational) |
| States needed | Often more | Often fewer |
| Glitch risk | Lower | Higher (due to combinational output) |
| Decoder gates | Simple AND from state | MUX/AND (state + input) |
| Typical use | Safe, clean | Performance-critical |

#### [5.6.2] Example: Traffic Light (Moore)

**States**: 
- S0: Red (20 cycles)
- S1: Yellow (5 cycles)
- S2: Green (15 cycles)

**Outputs**: Light color (one-hot: R=1,0,0 for S0; Y=0,1,0 for S1; G=0,0,1 for S2)

**Transitions**: S0→S1→S2→S0 (triggered by timer)

**Implementation**:
- 2 flip-flops for 3 states
- Timer logic (counter)
- Output decoder

**State diagram**:
```
      ┌─ S0(Red) ←──┐
      │    ↓        │
      └→ S1(Yellow) │
           ↓        │
      S2(Green)─────┘
```

#### [5.6.3] Example: Sequence Detector (Mealy)

**Goal**: Detect sequence "101" in incoming data.

**States**:
- S0: No progress (initial)
- S1: Seen "1"
- S2: Seen "10"

**Transitions & Outputs**:
| Current | Input | Next | Output |
|---------|-------|------|--------|
| S0 | 0 | S0 | 0 |
| S0 | 1 | S1 | 0 |
| S1 | 0 | S2 | 0 |
| S1 | 1 | S1 | 0 |
| S2 | 0 | S0 | 0 |
| S2 | 1 | ? | **1** (detected!) |

Last row: When in S2 and input=1, we've seen "101". Output = 1. Next state = S1 (seen "1" for next seq).

**State diagram** (Mealy):
```
      0/0    1/0      0/0      1/0
S0 ─────→ S0   S0 ─────→ S1  S2 ─────→ S0   S1 ─────→ S1
            ↑     ↓ 0/0    ↓ 1/1    ↓       ↑
            └─────S2 ←─────S2 ─1/0─ S1
                  self-loop 0/0
```

**Implementation** (Moore-equivalent):
Add state S3 = "Seen '101'" (output=1), then reset.

#### [5.6.4] Excitation Tables

To implement FSM, convert state transitions to flip-flop inputs.

**Example**: 3-state (S0, S1, S2) Moore using 2 D-FF (state codes: S0=00, S1=01, S2=10)

**Next-state table**:
| State | Input | Next state | D[1] | D[0] |
|-------|-------|------------|------|------|
| S0(00) | 0 | S0(00) | 0 | 0 |
| S0(00) | 1 | S1(01) | 0 | 1 |
| S1(01) | 0 | S2(10) | 1 | 0 |
| S1(01) | 1 | S1(01) | 0 | 1 |
| S2(10) | 0 | S0(00) | 0 | 0 |
| S2(10) | 1 | S2(10) | 1 | 0 |

**Output table** (Moore):
| State | Color |
|-------|-------|
| S0(00) | Red (01) |
| S1(01) | Yellow (10) |
| S2(10) | Green (11) |

**K-map for $D[1]$**:
```
       Input
State  0   1
00     0   0
01     1   0
10     0   1
```
$$D[1] = \text{State}[1] \cdot \text{Input}' + \text{State}[0] \cdot \text{Input}$$

**Implementation**: 2 D-FF + output decoder + next-state logic.

**Gate count**: ~40 gates for this example.

### The 2026 Adversarial Vault

**Trap #1**: "Mealy machine is always faster than Moore"

**True for raw output**, but:
- Mealy outputs have glitches during transitions
- Moore outputs stable
- Timing depends on safety requirements

**Trap #2**: "FSM needs N flip-flops for N states"

**False** ❌: Needs $\lceil \log_2 N \rceil$ flip-flops!
- 3 states → 2 flip-flops
- 7 states → 3 flip-flops

**Trap #3**: "One-hot encoding wastes flip-flops"

**True**, but:
- One-hot is simpler to design (one FF per state)
- Decoder logic is trivial (AND gates)
- Trade-off: More FF, simpler logic vs fewer FF, complex logic

**GATE Pattern**: "Sequence detector for '110' using Mealy. Min gates?"

**States**: 3 (S0, S1, S2) → 2 FF
**Next-state logic**: ~10 gates
**Output logic**: ~5 gates
**Total**: ~30 gates

**MSQ Logic Gate**: 
- "Mealy machine output depends on input" → **TRUE**
- "Moore machine is always safer" → **TRUE** (stable outputs)
- "FSM with N states needs 2^N gates" → **FALSE** (depends on design)

---

## [5.7] Master Formula Sheet

### Counter Formulas

**Modulo-N counter**: $N = 2^n - 1$ if binary, needs decode for arbitrary N.

**Delay**:
- Ripple: $T = n \times T_{FF}$
- Synchronous: $T = T_{FF} + \log_2(n) \times T_{AND}$

**Gate count**:
- Ripple: $16n$
- Synchronous (MOD-2^n): $19n$
- MOD-N (arbitrary): $19n + \text{decode gates}$

### Register/Shift Register Formulas

**Storage capacity**: $n$ bits (n flip-flops)

**Propagation delay**:
- Parallel load: $T_{FF}$
- Serial shift: $n \times T_{FF}$

**Gate count**:
- Basic: $16n$
- Shift: $16n + 3(n-1)$
- Universal: $34n$

### FSM Formulas

**Minimum states**: Problem-dependent, but usually proportional to input pattern length.

**Minimum flip-flops**: $\lceil \log_2(\text{# states}) \rceil$

**Next-state logic gates**: Depends on transition complexity, ~O(# states × inputs).

**Output logic gates**: O(# states) for Moore, O(# states × inputs) for Mealy.

### Permanent Recall

**The Bizarre Mnemonic**: 
**"**LATCH** = **L**evel **A**ctivated, no Time-controlled, **CH**ange
**FLIP-FLOP** = **F**requency synchronizer, **LATCH** improved**P**erfect logic for **F**ast **L**ogic **O**perations **P**ropagation-controlled"

**Mental Slider**:
- Latch (gated SR): No clock, level-triggered
- FF (D/JK/T): Clock-triggered, synchronous
- Register: Multiple FF in parallel
- Counter: Register with feedback (increment)
- FSM: Counter with complex logic

**The 5-Second Snap-Check**:
- Latch: Two-state (bistable), no clock
- SR FF: 4-state (hold, set, reset, invalid)
- JK FF: 4-state (hold, set, reset, **toggle**)
- D FF: Maps D→Q directly
- T FF: Toggles if T=1
- Register stores N-bit data
- Ripple counter: Slow but simple
- Sync counter: Fast, needs enable logic
- FSM: Describes sequential behavior with states

---

## [5.8] Previous Year Patterns (GATE/ESE)

### GATE 2023-2024

**Q1 (Flip-flop conversion)**: "Design a JK flip-flop using D flip-flops. Min gates?"
- Answer: 1-2 gates (MUX or XOR for input logic)

**Q2 (Counter delay)**: "32-bit ripple counter vs 32-bit sync counter delay ratio?"
- Answer: ~32:3 or 10:1 (ripple much slower)

**Q3 (FSM states)**: "Sequence detector '1011': Min states (Mealy)?"
- Answer: 4 states (S0→S1→S2→S3→output=1)

### ESE 2023

**Q1 (Shift register)**: "8-bit shift register, parallel load, min gates?"
- Answer: ~200 gates (8 FF + 8 MUX + decode)

**Q2 (Ring vs Johnson)**: "Ring counter vs Johnson counter state efficiency?"
- Answer: Johnson uses half ring's states (8 vs 4 for MOD-8), double capacity

### Common Difficulty Levels

**Easy** (~20%): Flip-flop types, basic counter operation
**Medium** (~60%): FF conversion, counter design, FSM basics
**Hard** (~20%): Mealy/Moore optimization, complex FSM synthesis, glitch analysis

### Topic Weightage

- Latches: 5%
- Flip-flops: 20%
- FF Conversion: 10%
- Registers/Shift Registers: 15%
- Counters: 20%
- State Machines: 20%
- Applications: 10%

---

## [5.9] NAT Precision & MSQ Strategy

### NAT Examples

**Q**: "MOD-100 counter: Min FF needed?"
- $100 ≤ 2^n$ → $n = 7$ (since $2^6=64 < 100$, $2^7=128 ≥ 100$) ✓

**Q**: "Sequence detector '101' states using Gray code: Total gates?"
- States: 4 → 2 FF → Gray = 4 states (0, 1, 2, 3)
- Next-state logic + output = ~25 gates total

### MSQ Strategy

**Type 1: FF property MSQ**

Q: "Which are true for D flip-flop?"
- (A) Stores 1-bit ✓
- (B) Output changes only on clock edge ✓
- (C) Can toggle if T=1 ✗ (that's T flip-flop)
- (D) Setup/hold times apply ✓

**Type 2: FSM comparison MSQ**

Q: "Mealy vs Moore machines"
- Mealy faster to respond ✓
- Moore safer (no glitches) ✓
- Moore needs more states usually ✓
- Mealy uses fewer FF usually ✗ (not always true)

---

**END OF MODULE 05**
