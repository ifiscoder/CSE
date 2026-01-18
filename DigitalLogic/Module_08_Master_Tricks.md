# Module 08: Master Tricks & Quick Formulas | The Speedrun Playbook

> **The Singularity**: Excellence is 90% pattern recognition + 10% deep understanding.

---

## [8.1] Gate Count Formulas | The Quick Estimates

### The Atomic Truth
**Gate count determines speed, area, power. Estimate before calculating exact.**

### Combinational Circuits

| Circuit | Formula | Notes |
|---------|---------|-------|
| 2:1 MUX | $2+2+1 = 5$ gates | 1 NOT + 2 AND + 1 OR |
| 4:1 MUX | $4 \times 3 + 4 + 2 = 18$ | 4 AND(3-in) + 1 OR(4-in) + 2 NOT |
| 8:1 MUX | $8 \times 4 + 8 + 3 = 43$ | Rough: 40-45 gates |
| 16:1 MUX | ~100 gates | Use tree structure instead |
| $n$-input decoder | $2^n + n$ AND + NOT | $2^n$ AND(n-input) + $n$ inverters |
| $n$-input encoder | $n \times 2^{n-1}$ OR gates | Each output: OR of $2^{n-1}$ inputs |
| Full Adder (1-bit) | 2 XOR + 3 AND + 1 OR = 9 gates | OR as majority function |
| $n$-bit ripple adder | $9n + n-1$ AND + OR = ~10n | Rough: 10n gates |
| 1-bit comparator | ~5 gates | 1 XNOR + 2 AND + 1 OR |
| $n$-bit magnitude cmp | ~5n gates | n comparators + cascade logic |
| Parity generator (n-bit) | $n-1$ XOR gates | Serial XOR chain |
| Code converter (B↔G) | $n-1$ XOR gates | Binary to/from Gray |

### Practical Estimation

**Quick mental calculation**:
1. Count inputs: $n$ inputs → need $\log_2(n)$ gate levels minimum
2. Count outputs: $m$ outputs → need $m$ AND/OR terms
3. Total ≈ $(n + m) \times$ average gates per term

**Example**: 
- 4-input MUX = $2^4 = 16$ data combos
- Needs: 4 AND (4-input each) + 1 OR (16-input equivalent)
- Rough: 16 + 16 = 32? No, more efficient: ~18 gates

---

## [8.2] Flip-Flop Conversion Tricks | The Alchemy

### The Atomic Truth
**Any flip-flop → any other via combinational logic. Master these transformations.**

### Conversion Matrix

#### T from D

**Target T behavior**: Toggle on clock if T=1, hold if T=0.

**Logic needed**:
$$D = T \oplus Q$$

**Implementation**:
```
D-FF ← [XOR gate] ← T, Q feedback
```

**Gates**: 1 XOR = 3 gates

#### JK from D

**Target JK**: J = set, K = reset, J=K=1 toggles.

**Characteristic equation**:
$$Q(t+1) = J\overline{Q} + \overline{K}Q$$

**Logic needed**:
$$D = J\overline{Q} + \overline{K}Q$$

**Implementation**:
```
D ← [OR gate] ← J∧Q', K'∧Q
      ↓
   [AND]  [AND]
    ↙ ↘    ↙  ↘
   J  Q'  K'  Q
```

**Gates**: 2 AND + 1 OR = 3 gates

#### SR from D

**Target SR**: S sets, R resets (NOR latch logic).

**Characteristic equation**:
$$Q(t+1) = S + \overline{R}Q$$

**Logic needed**:
$$D = S + \overline{R}Q$$

**Implementation**:
```
D ← [OR gate] ← S, R'∧Q
      ↓
   [AND]
    ↙  ↘
   R'  Q
```

**Gates**: 1 AND + 1 OR = 2 gates

#### Full Conversion Table

| From ↓ To → | D | T | JK | SR | Notes |
|---|---|---|---|---|---|
| **D** | - | D⊕Q (1 XOR) | JQ'+K'Q (2AND+OR) | S+R'Q (AND+OR) | D simplest |
| **T** | T⊕Q (1 XOR) | - | J⊕K⊕Q? | Complex | T harder to convert |
| **JK** | J⊕K⊕Q? | ? | - | Complex | JK most flexible |
| **SR** | S+R'Q | ? | Complex | - | SR basic |

**Key insight**: Use D as intermediate:
- Source → D (via combinational) → D-FF → Target (if needed)

### Permanent Recall Mnemonic

**"**D is universal; T is toggle; JK is King; SR is Simple"**
- Start with D-FF (most flexible target)
- If need SR → 2 gates
- If need JK → 3 gates
- If need T → 1 gate (XOR)

---

## [8.3] Counter Tricks | The Sequencing Hacks

### Trick #1: MOD-N Counter using MOD-$2^n$

**Problem**: Design MOD-12 counter.

**Brute force**: 12 unique states → need 4 flip-flops (2^4=16 > 12)

**Implementation**:
1. Build MOD-16 counter (standard binary 4-bit)
2. Decode when count reaches 12 (0000 0001 1100)
3. Asynchronously reset to 0 when detected

**Decode logic**:
$$\text{Reset} = Q_3 \cdot Q_2 \cdot \overline{Q_1} \cdot \overline{Q_0} = \text{1 when count=12}$$

**Gates**: Standard 4-bit counter + 1 AND gate for decode

### Trick #2: Frequency Division

**Problem**: Divide 100 MHz by 16.

**Hack**: 4-bit ripple counter (each FF divides by 2)
- Input: 100 MHz
- Output Q[3]: 100 MHz / 16 = 6.25 MHz ✓

**Gates**: 4 T-FF = ~32 gates

### Trick #3: Counter with Preset

**Problem**: Start counting from N instead of 0.

**Method**: Parallel load capability.
```
Load ─┐
      ├─→ Mux ─→ FF input
Count ┤
      │
   Data[0] ─┘
```

**When Load=1**: Data[i] loaded into each FF
**When Load=0**: Counter increments normally

**Gates**: Add 2:1 MUX per FF = extra 2n gates

### Trick #4: UP/DOWN Counter

**Problem**: Count both directions.

**Method**: Alternate between incrementer and decrementer based on control.

**Control logic**:
- UP=1: Next state = current + 1
- DOWN=1: Next state = current - 1
- Both 0: Hold

**Implementation**: 2:1 MUX at each FF input selecting increment or decrement value.

**Gates**: 2n MUX gates + incrementer/decrementer logic

---

## [8.4] MUX Implementation Hacks | The Data Routing Shortcuts

### Trick #1: Implement Any Function with MUX

**Principle**: Any n-variable function can be realized with $2^{n-1}:1$ MUX + some gates.

**Example**: 4-variable function with 2:1 MUX

**Step 1**: Write function in terms of MSB

$$F(A,B,C,D) = \text{If } A=0: F_0(B,C,D) \text{ else } F_1(B,C,D)$$

**Step 2**: Recognize $F_0$ and $F_1$ (simpler functions)

**Step 3**: 2:1 MUX with A as select

**Gates**: Savings if $F_0$ or $F_1$ are simple (AND, OR, constant)

### Trick #2: Design Multiplexer with Shifter

**Problem**: Select 1 of 16 bits, then shift.

**Naive**: MUX to select, then separate shifter (~50 gates)

**Optimized**: Programmable shifter = MUX with rotation logic

**Implementation**: 16-bit word, MUX output as shifted result

### Trick #3: Bus Multiplexing

**Problem**: Multiple sources, multiple destinations (N×M matrix).

**Solution**: N:1 MUX per output line.

**Gates**: $M \times \log_2(N)$ select lines, $M$ MUX blocks

---

## [8.5] Parity & Error Detection Hacks | The Reliability Tricks

### Trick #1: Multi-bit Parity Generation

**Problem**: Generate parity for 32-bit word.

**Naive**: Chain 31 XOR gates (slow)

**Optimized (tree structure)**:
```
Level 1: 16 XOR pairs → 16 bits
Level 2: 8 XOR pairs → 8 bits
Level 3: 4 XOR pairs → 4 bits
Level 4: 2 XOR pairs → 2 bits
Level 5: 1 XOR → final parity
```

**Delay**: $\log_2(32) = 5$ XOR delays = ~15 ns (vs 31 XOR delays = ~90 ns)

**Speedup**: 6× faster!

### Trick #2: Distributed Parity

**Problem**: Single point of failure in parity.

**Solution**: Multiple parity checks (Hamming code).

For 4-bit data (7-bit codeword):
- $P_1$: checks bits 1,3,5,7
- $P_2$: checks bits 2,3,6,7
- $P_4$: checks bits 4,5,6,7

**Syndrome** ($S_1 S_2 S_4$) points directly to error bit!

**Gates**: 3 parity generators + (optional) error corrector

---

## [8.6] Adder Tricks | The Arithmetic Accelerators

### Trick #1: Carry Lookahead for Speed

**Ripple carry**: $T = n \times 10 \text{ ns} = 320 \text{ ns}$ (32-bit)

**Carry lookahead**: Compute all carries in parallel

$$C_i = G_i + P_i \cdot G_{i-1} + P_i P_{i-1} G_{i-2} + \ldots$$

**Speedup**: Constant time regardless of width (with sufficient gates)

**Cost**: Exponential gate growth for large n (limit to 4-bit blocks, cascade)

### Trick #2: Conditional Sum Adder

**Idea**: Pre-compute sum and carry for both C_in = 0 and C_in = 1.

At final stage: MUX selects correct result based on actual C_in.

**Advantage**: Logarithmic depth (tree structure)

**Gates**: ~2× ripple carry, but ~4× faster

### Trick #3: Subtract via Inversion

**A - B = A + (-B) = A + B' + 1** (2's complement)

**Hack**: Single adder + inverter on B + set carry-in = 1

**Cost**: 1 NOT gate per B bit + 1 control signal (rarely extra logic)

**Benefit**: Unified arithmetic unit (no separate subtractor)

---

## [8.7] Quick Reference Mnemonics | The Memory Palace

### The Trinity of Flip-Flops

**D = Direct** (Q = D after clock)
**T = Toggle** (Q ← ¬Q if T=1)
**JK = King** (All states covered)

**Remembering characteristics**:
- **D**: Simplest to use, stores input
- **T**: Divides frequency by 2 (counter building block)
- **JK**: Most flexible, universal

### Logic Family Speed Ranking

**ECL > CMOS ≈ TTL-LS > TTL > nothing** (in terms of speed)

**Power Ranking** (best to worst):
CMOS << CMOS-LS << TTL-LS < TTL << ECL

### Memory Type Pecking Order (Speed)

**Cache (SRAM) > Main (DRAM) > SSD (Flash) > HDD (magnetic)**

**Cost per GB** (best to worst):
**HDD << Flash < DRAM << SRAM**

---

## [8.8] Pattern Recognition | The Exam Speedrun

### GATE Exam Patterns

**Pattern #1: "Minimum gates" question**

**Approach**:
1. Draw truth table or K-map
2. Identify simplest form (minimal terms)
3. Count AND, OR, NOT gates
4. Don't forget inverters for complemented inputs!

**Trap**: Forgetting inverters = wrong answer

**Time**: 2-3 minutes per question

### Pattern #2: "Cascade/propagation delay" question

**Approach**:
1. Identify critical path (longest gate chain)
2. Count gates in that path
3. Multiply by gate delay (~10 ns for TTL, ~5 ns for CMOS)
4. Add setup/hold times if applicable

**Formula**: $T = n \times t_{gate} + t_{setup} + t_{hold}$

**Time**: 2-3 minutes

### Pattern #3: "FSM design" question

**Approach**:
1. Identify states needed (usually 3-5)
2. Draw state diagram
3. Create state table (encode states as binary)
4. Generate excitation table
5. Derive minimized logic

**Time**: 5-10 minutes (complex)

### Pattern #4: "Memory size" question

**Approach**:
1. Extract capacity: "1K × 8" = 1024 words, 8 bits/word
2. Calculate address bits: $\log_2(1024) = 10$
3. Calculate total bits: $1024 \times 8 = 8192$
4. Convert to bytes/KB: $8192 / 8 = 1 \text{ KB}$

**Time**: 1-2 minutes

### Pattern #5: "Comparison" question

**Approach**:
1. Create feature table (speed, power, density, cost)
2. Mark each family (TTL, CMOS, ECL, etc.)
3. Identify which is best for given constraint

**Time**: 3-5 minutes

---

## [8.9] Mental Math Speedups | The Calculator Bypass

### Quick Powers of 2

$$2^{10} = 1024 ≈ 1000 = 10^3$$

Use this to convert between binary and decimal:
- $2^{10}$ = 1K
- $2^{20}$ = 1M
- $2^{30}$ = 1G
- $2^{40}$ = 1T

**Application**: "32 Mbit DRAM = $2^{25}$ bits"?
- $32M = 32 \times 10^6 = 32 \times 2^{20} = 2^5 \times 2^{20} = 2^{25}$ ✓

### Quick Logarithms

$$\log_2(N) ≈ \text{# bits needed to represent N}$$

**Hack**: Count bits in binary representation.
- 8 = 1000₂ (4 bits) → $\log_2(8) = 3$ (one less)
- 16 = 10000₂ (5 bits) → $\log_2(16) = 4$

**Formula**: For $N ≤ 2^n$, we have $\log_2(N) ≤ n$.

### Quick Gate Count Estimation

**Rule of thumb**:
- Logic depth $d$ → minimum $d$ gate delays
- Logic width $w$ → minimum $\log_2(w)$ levels (binary tree)

**Combine**: Total minimum depth ≈ $\log_2(w) + \text{fanin constraints}$

---

## [8.10] Exam Strategy | The Game Plan

### Time Management

**Module breakdown** (for 3-hour exam):
- Easy (20%): 20 min (1 min each)
- Medium (60%): 100 min (2-3 min each)
- Hard (20%): 40 min (5-10 min each)

**Buffer time**: 20 min for review/corrections

### Question Prioritization

**If stuck on a question**:
1. Flag it (mark for later)
2. Move to next question
3. Return if time permits

**Reason**: Easy questions give same points, faster to solve.

### Common Mistakes to Avoid

1. **Forgetting inverters** in gate count
2. **Wrong K-map grouping** (not using Gray code)
3. **Confusing MUX select logic** (n bits → $2^n$ inputs)
4. **Off-by-one errors** in counter design (MOD-8 ≠ MOD-7)
5. **Propagation delay calculation** (forgetting all gate delays)

### Last-Minute Checks

- [ ] All inverters counted?
- [ ] K-map groups valid (powers of 2)?
- [ ] Address lines = $\log_2$ (# words)?
- [ ] Propagation delay = sum of ALL gate delays?
- [ ] Flip-flop setup/hold times included?

---

## [8.11] The Cheat Sheet | The Ultimate Reference

### All Gate Delays (approximate, in ns)

| Gate | TTL | CMOS | ECL |
|------|-----|------|-----|
| NOT | 3 | 2 | 1 |
| AND/NAND | 7 | 3 | 1 |
| OR/NOR | 7 | 3 | 1 |
| XOR | 10 | 5 | 2 |
| MUX (2:1) | 10 | 5 | 1 |
| FF (D) | 10 | 5 | 2 |

### Critical Logic Equations

| Function | Equation |
|----------|----------|
| XOR | $A \oplus B = A'B + AB'$ |
| XNOR | $A \odot B = AB + A'B'$ |
| Majority | $M = AB + AC + BC$ |
| Parity (3-bit) | $P = A \oplus B \oplus C$ |
| Gray (binary→Gray) | $G_i = B_i \oplus B_{i+1}$ |
| Adder Sum | $S = A \oplus B \oplus C_{in}$ |
| Adder Carry | $C_{out} = AB + C_{in}(A \oplus B)$ |

### State Machine Quick Guide

| Machine | Output depends on | States needed |
|---------|-------------------|---------------|
| Moore | State only | Usually more |
| Mealy | State + Input | Usually fewer |
| Combinational | Input only | 1 state (trivial) |

---

**END OF MODULE 08**
