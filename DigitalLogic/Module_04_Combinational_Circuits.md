# Module 04: Combinational Circuits | The Functional Builders

> **The Singularity**: Output at any instant depends ONLY on present input (no memory).

---

## [4.1] Multiplexer (MUX) | The Data Highway

### The Atomic Truth
**$2^n$ inputs, $n$ select lines, 1 output. Each select code routes one input to output.**

### The Path of Elegance

A multiplexer is a **data selector** device. With $n$ select lines, it can choose from $2^n$ input lines.

$$\text{Output} = \sum_{i=0}^{2^n-1} I_i \cdot S_i$$

where $S_i$ is the **minterm** corresponding to select code $i$.

#### [4.1.1] 2:1 MUX (Simplest)

**Truth Table**:
| $S_0$ | Output |
|-------|--------|
| 0 | $I_0$ |
| 1 | $I_1$ |

**Boolean Expression**:
$$Y = \overline{S_0} \cdot I_0 + S_0 \cdot I_1$$

**Gate Count**: 3 gates (1 NOT, 2 AND, 1 OR) = **4 two-input gates**

#### [4.1.2] 4:1 MUX (Common)

**Select lines**: $S_1 S_0$ (2 bits)

**Boolean Expression**:
$$Y = \overline{S_1}\,\overline{S_0} \cdot I_0 + \overline{S_1}\,S_0 \cdot I_1 + S_1\,\overline{S_0} \cdot I_2 + S_1\,S_0 \cdot I_3$$

**Compact form**: 
$$Y = \sum_{i=0}^{3} I_i \cdot m_i(S_1, S_0)$$

**Gate Count**: 
- 4 AND gates (3-input each)
- 1 4-input OR gate
- 2 inverters
- **Total**: $4 \times 3 + 4 + 2 = 18$ two-input gate equivalents

#### [4.1.3] 8:1 MUX (Extended)

**Select lines**: $S_2 S_1 S_0$ (3 bits)

**Gate Count**: 
- 8 AND gates (4-input each) = $8 \times 4 = 32$ two-input equivalents
- 1 8-input OR = 7 two-input equivalents
- 3 inverters
- **Total**: ~40 two-input gate equivalents

**The Golden Pivot**: Larger MUXes can be implemented using **tree structure**:
- 8:1 MUX from four 2:1 MUXes (tree stage 1) + one 4:1 MUX (tree stage 2)

$$\text{8:1} = \text{Tree of 2:1s} = (2:1 \times 4) \to \text{4:1}$$

#### [4.1.4] MUX Implementation Tricks

**Trick #1: Using MUX as Function Inverter**

To invert any Boolean function $F(A,B,C)$:
1. Implement $F$ using a MUX with A, B, C as select lines
2. Apply $\overline{F}$ to each output by complementing inputs selectively

**Trick #2: One MUX Can Implement Any Function**

An $n$-variable function $F(x_1, x_2, \ldots, x_n)$ can be implemented as a **single $2^n:1$ MUX**:
- Connect $x_1, \ldots, x_n$ to select lines
- Connect minterms $(F(0,0,\ldots), F(0,0,\ldots,1), \ldots)$ to data inputs

$$\text{Gate count} = 2^n - 1 \text{ AND gates} + (2^n-1) \text{ OR gates}$$

**Trick #3: Tree Implementation (Preferred for Large Functions)**

For an $n$-variable function using $(n-k)$-variable select lines:
- Reduce to a $2^{n-k}:1$ MUX fed by $2^k$ terms built from remaining $k$ variables
- **Example**: 4-variable function using 2:1 MUXes

$$F(A,B,C,D) = \text{MUX}(A, F(0,B,C,D), F(1,B,C,D))$$

where $F(0,\cdot,\cdot,\cdot)$ and $F(1,\cdot,\cdot,\cdot)$ are simpler 3-variable functions.

**Trick #4: MUX for Arithmetic (Conditional Selection)**

- **Max circuit**: $(A > B) ? A : B$ = 2:1 MUX with $A > B$ as select
- **Absolute value**: $|A-B|$ = Combine MUX with subtractor
- **Sign extension**: Use MUX to replicate sign bit

### The 2026 Adversarial Vault

**Trap #1**: "How many 2:1 MUXes to build an 8:1 MUX?"

**Wrong Answer**: 8 ❌
**Correct Answer**: 7 ✓ (Tree structure: 4 MUXes in stage 1 → feed into 1 MUX → feed into 1 MUX = $4 + 2 + 1 = 7$)

**Trap #2**: "Minimum gates to implement arbitrary 3-variable function?"

**Wrong reasoning**: "Use K-map, get ~5 gates" ❌ (only true for some functions)
**Correct reasoning**: "Worst case needs 3:1 MUX ($2^3-1=7$ gates min) OR worst-case SOP/POS (~8 gates)" ✓

**Trap #3**: K-map gate count vs MUX for same function

**GATE Pattern**: "Implement $F(A,B,C) = \sum m(0,2,3,5)$ using minimal gates"

**K-map approach**: 
```
    BC
    00 01 11 10
A 0 | 1  0  0  1
  1 | 0  1  1  0
```
Grouping: $\overline{A}\,\overline{B}\,\overline{C} + \overline{A}\,B\,C + A\,B\,\overline{C} + A\,B\,C$
Gates: 4 AND + 1 OR = 5 gates

**MUX approach**: 4:1 MUX = ~4 gates

**MSQ Logic Gate**: 
- "MUX is universal" → **FALSE** (needs external gates for some functions)
- "Every combinational function needs at most one $2^n:1$ MUX for $n$ variables" → **TRUE**
- "Cascade of 2:1 MUXes always more efficient than single large MUX" → **FALSE** (depends on gate technology)

**NAT Precision Lock**: 
When asked "minimum gate count for $n$-input MUX":
$$\text{Gate count} = 2^n - 1 \text{ (AND gates)} + 2^n - 1 \text{ (OR gates)} - \text{optimization}$$

Typical: $2^{n+1} - 2$ for basic implementation.

### Permanent Recall

**The Bizarre Mnemonic**: 
Imagine a **PHONE SWITCHBOARD**. The SELECT lines are like fingers dialing (each combo dials a unique line). The DATA inputs are like phone lines. Your brain instantly sees the selected phone line routed to output.

**The Mental Slider**: 
For any MUX, think: "$2^n$ DATA lines, $n$ SELECT lines, 1 OUTPUT". Always $2^n:1$.
- 4 data → 2 selects (4:1)
- 8 data → 3 selects (8:1)
- 16 data → 4 selects (16:1)

**The 5-Second Snap-Check**:
- Total inputs = data lines + select lines = $2^n + n$
- Each data input used exactly once in output expression
- For tree MUX, level $i$ has $2^i$ select line uses
- MUX count in balanced tree = $\frac{2^n - 1}{2^k - 1}$ for $2^k:1$ building blocks

---

## [4.2] Demultiplexer (DEMUX) | The Data Router

### The Atomic Truth
**1 input, $n$ select lines, $2^n$ outputs. Select code routes input to exactly one output.**

### The Path of Elegance

DEMUX is the **inverse** of MUX:
- **MUX**: Many data inputs → 1 output (routing based on select)
- **DEMUX**: 1 data input → Many outputs (activated by select)

#### [4.2.1] 1:2 DEMUX (Simplest)

**Truth Table**:
| $S_0$ | $O_0$ | $O_1$ |
|-------|-------|-------|
| 0 | $I$ | 0 |
| 1 | 0 | $I$ |

**Boolean Expressions**:
$$O_0 = \overline{S_0} \cdot I$$
$$O_1 = S_0 \cdot I$$

#### [4.2.2] 1:4 DEMUX

**Select lines**: $S_1 S_0$

**Boolean Expressions**:
$$O_0 = \overline{S_1}\,\overline{S_0} \cdot I$$
$$O_1 = \overline{S_1}\,S_0 \cdot I$$
$$O_2 = S_1\,\overline{S_0} \cdot I$$
$$O_3 = S_1\,S_0 \cdot I$$

**Gate Count**: 4 AND gates (2-input each) + 1 decoder/truth table

**The Golden Pivot**: DEMUX is essentially a **decoder** with an enable input. 

**Connection**: 
$$\text{Decoder with enable} = \text{DEMUX}$$
where the enable signal is the data input.

#### [4.2.3] DEMUX Applications

**App #1: Memory address decoding**
- 1 memory write signal → selects which address gets written

**App #2: Interrupt routing**
- 1 interrupt signal → routed to specific I/O device

**App #3: Cascaded DEMUX for larger arrays**
- 1:4 DEMUX with select → feeds into multiple 1:4 DEMUXes → creates 1:16

### The 2026 Adversarial Vault

**Trap #1**: "MUX and DEMUX are the same thing"

**False**: They're inverses!
- MUX: $2^n:1$ combiner
- DEMUX: $1:2^n$ splitter

**Trap #2**: DEMUX output selection formula

**Wrong**: "Output $k$ is active if $k = \text{select}$ address" ❌ (incomplete)
**Correct**: "Output $k$ is active if $k = \text{select}$ address AND $I = 1$" ✓

**GATE Pattern**: "Design a 1:8 DEMUX using 1:2 DEMUXes. Gate count?"

**Solution**:
- Need 7 cascaded 1:2 DEMUXes (binary tree structure)
- Input → 1:2 DEMUX (stage 1) → 2 signals to 2× 1:2 DEMUXes (stage 2) → 4 signals to 4× 1:2 DEMUXes (stage 3) = 8 outputs
- Total DEMUXes: $1 + 2 + 4 = 7$
- Each 1:2 DEMUX uses 2 AND gates + 2 inverters (reusable)
- **Total gates**: ~14 AND gates

---

## [4.3] Encoders & Decoders | The Code Converters

### The Atomic Truth
**Encoder**: $2^n$ inputs → $n$ outputs (priority determines which input)
**Decoder**: $n$ inputs → $2^n$ outputs (one-hot output)

### The Path of Elegance

#### [4.3.1] Binary Encoder (Priority Encoder)

**Function**: Converts one-hot input to binary address.

**Example: 4:2 Encoder**

**Truth Table** (highest priority = input 3):
| $I_3$ | $I_2$ | $I_1$ | $I_0$ | $Y_1$ | $Y_0$ |
|-------|-------|-------|-------|-------|-------|
| 0 | 0 | 0 | 0 | X | X |
| 0 | 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | X | 0 | 1 |
| 0 | 1 | X | X | 1 | 0 |
| 1 | X | X | X | 1 | 1 |

(X = don't care due to priority)

**Boolean Expressions**:
$$Y_1 = I_3 + I_2$$
$$Y_0 = I_3 + I_1$$

**Gate Count**: 2 OR gates

#### [4.3.2] Binary Decoder (1-of-$2^n$ decoder)

**Function**: Converts binary address to one-hot output.

**Example: 2:4 Decoder**

**Truth Table**:
| $A_1$ | $A_0$ | $O_0$ | $O_1$ | $O_2$ | $O_3$ |
|-------|-------|-------|-------|-------|-------|
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 |

**Boolean Expressions**:
$$O_0 = \overline{A_1}\,\overline{A_0}$$
$$O_1 = \overline{A_1}\,A_0$$
$$O_2 = A_1\,\overline{A_0}$$
$$O_3 = A_1\,A_0$$

**General Formula**: $O_i = m_i(A_1, A_0)$ (minterm generator)

**Gate Count**: 4 AND gates (2-input each)

#### [4.3.3] Decoder Generalization

For $n$-input, $2^n$-output decoder:
- Each output is a **minterm**
- $O_i = m_i(A_{n-1}, \ldots, A_0)$
- Gate count: $2^n$ AND gates + $n$ inverters

#### [4.3.4] Encoder-Decoder Relationship

$$\text{If cascaded} \to (\text{Encoder output}) \to (\text{Decoder input})$$
$$\text{Result} = \text{Original input (one-hot)}$$

**Exception**: If multiple inputs active in encoder → decoder gets the address of **highest priority** only.

### The 2026 Adversarial Vault

**Trap #1**: "Encoder and decoder are inverses"

**Technically FALSE** ❌: Multiple inputs can be active in encoder, but decoder produces single output.
**Correct understanding**: Ideal encoder (one-hot input) and decoder are inverses. ✓

**Trap #2**: "8:3 Encoder gate count"

**Wrong**: "Need 8 AND gates" ❌ (confusing with decoder)
**Correct**: "Need 3 OR gates maximum" ✓
$$Y_2 = I_7 + I_6 + I_5 + I_4$$
$$Y_1 = I_7 + I_6 + I_3 + I_2$$
$$Y_0 = I_7 + I_5 + I_3 + I_1$$

**Trap #3**: "Address decoder for $2^n$ locations uses $n$ bits"

**This is correct** ✓ but students forget **why**: $\log_2(2^n) = n$ addresses need $n$ bits.

**MSQ Logic Gate**: 
- "Decoder output is always exactly one 1" → **TRUE** (for valid input)
- "Encoder needs priority logic" → **TRUE** (multiple inputs need arbitration)
- "Gray code decoder" → **Possible** (special case where outputs represent Gray code minterms)

**NAT Precision Lock**: 
For "design a $(2^n):n$ priority encoder":
- Gate count = $n \times 2^{n-1}$ (rough estimate)
- Each output needs OR of $2^{n-1}$ inputs

### Permanent Recall

**The Bizarre Mnemonic**: 
**ENCODER** = "Encode into address" → Multiple switches → Select one → Output address (0-indexed)
**DECODER** = "Decode address" → Address input → Light up specific output lamp

Think: Post office with 8 mailboxes → Encoder (read which mailbox) → Address → Decoder (activate that mailbox light)

**The Mental Slider**: 
- Encoder: $2^n$ in, $n$ out (compression)
- Decoder: $n$ in, $2^n$ out (expansion)
- Both reversible only in ideal one-hot case

**The 5-Second Snap-Check**:
- Total gates in $n:2^n$ decoder ≈ $n \times 2^n$ two-input equivalents
- Total gates in $2^n:n$ encoder ≈ $n \times 2^{n-1}$ two-input equivalents
- Encoder gates < Decoder gates for same $n$ (due to OR simplification)

---

## [4.4] Adders & Subtractors | The Arithmetic Engines

### The Atomic Truth
**Adder**: $A + B = \text{Sum and Carry}$
**Subtractor**: $A - B = \text{Difference and Borrow}$

### The Path of Elegance

#### [4.4.1] Half Adder (Single Bit, No Carry-in)

**Function**: Add two single bits without considering carry-in.

**Truth Table**:
| $A$ | $B$ | Sum | Carry |
|-----|-----|-----|-------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

**Boolean Expressions**:
$$\text{Sum} = A \oplus B$$
$$\text{Carry} = A \cdot B$$

**Gate Count**: 
- 1 XOR (= 3 two-input gates: $AB' + A'B$)
- 1 AND
- **Total**: 4 two-input gates

#### [4.4.2] Full Adder (Single Bit with Carry-in)

**Function**: Add two bits plus a carry-in.

**Truth Table**:
| $A$ | $B$ | $C_{in}$ | Sum | $C_{out}$ |
|-----|-----|----------|-----|-----------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

**Boolean Expressions** (from K-map):
$$\text{Sum} = A \oplus B \oplus C_{in}$$
$$C_{out} = AB + (A \oplus B) \cdot C_{in} = AB + AC_{in} + BC_{in}$$

**Alternative $C_{out}$ form**:
$$C_{out} = AB + C_{in}(A + B) \text{ (majority gate)}$$

This form is elegant because:
- $AB$: both inputs are 1
- $C_{in}(A+B)$: if at least 2 of {A, B, $C_{in}$} are 1

**Gate Count**:
- 2 XOR gates (one for $A \oplus B$, one for Sum)
- 3 AND gates (for $AB$, $AC_{in}$, $BC_{in}$)
- 1 OR gate (to combine ANDs)
- **Total**: ~9 two-input gates

**Optimized form**:
$$C_{out} = M(A, B, C_{in})$$
where $M$ is the **majority function** (3-input).

#### [4.4.3] N-bit Adder (Ripple Carry)

**Structure**: Cascade $n$ full adders, each with carry-in from previous stage.

$$A_n \ldots A_1 + B_n \ldots B_1 = \text{Sum}_n \ldots \text{Sum}_1, C_{out}$$

**Block Diagram**:
```
A[n] B[n]           A[1] B[1]
  |   |               |   |
  FA n ← C_n    ...   FA 1 ← C_1
  |                   |
Sum[n]             Sum[1]
       ↖ Carry propagates left
```

**Carry Propagation Time** (critical for speed):

$$t_{delay} = n \times t_{FA}$$

where $t_{FA}$ is delay through one full adder (~9-12 gate delays in CMOS).

For 32-bit adder: $32 \times 10 = 320$ ns (typically).

**The Golden Pivot - Carry Look-Ahead (CLA)**:

To speed up addition, we compute carries in parallel rather than waiting for ripple:

$$C_1 = AB + C_0(A \oplus B)$$
$$C_2 = AB + (A \oplus B)C_0 + (A \oplus B)(A' B'C_0 + AB)$$

This becomes complex, but **generate and propagate signals** simplify:
- **Generate**: $G = AB$ (generates carry regardless of $C_{in}$)
- **Propagate**: $P = A \oplus B$ (propagates carry if $C_{in} = 1$)

Then:
$$C_{out} = G + P \cdot C_{in}$$

**4-bit CLA equations**:
$$C_1 = G_0 + P_0 C_0$$
$$C_2 = G_1 + P_1 C_1 = G_1 + P_1(G_0 + P_0 C_0) = G_1 + P_1 G_0 + P_1 P_0 C_0$$
$$C_3 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0$$
$$C_4 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0$$

**Delay reduction**: From $O(n)$ to $O(\log n)$ for large $n$.

#### [4.4.4] Half Subtractor

**Function**: Subtract $B$ from $A$ (single bit).

**Truth Table**:
| $A$ | $B$ | Diff | Borrow |
|-----|-----|------|--------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

**Boolean Expressions**:
$$\text{Difference} = A \oplus B$$
$$\text{Borrow} = \overline{A} \cdot B$$

#### [4.4.5] Full Subtractor

**Truth Table**:
| $A$ | $B$ | $B_{in}$ | Diff | $B_{out}$ |
|-----|-----|----------|------|-----------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 |

**Boolean Expressions**:
$$\text{Difference} = A \oplus B \oplus B_{in}$$
$$B_{out} = \overline{A}B + \overline{A}B_{in} + B \cdot B_{in}$$
$$B_{out} = \overline{A}(B + B_{in}) + B \cdot B_{in}$$

**Connection to Adder**: 
$$A - B = A + (-B) = A + \overline{B} + 1 \text{ (in 2's complement)}$$

So subtraction uses the **same adder** with inverted $B$ bits + carry-in = 1.

### The 2026 Adversarial Vault

**Trap #1**: "Full adder sum is majority gate"

**Wrong**: Sum IS XOR, not majority ❌
**Correct**: Carry IS majority ✓
$$\text{Sum} = A \oplus B \oplus C$$
$$C_{out} = M(A, B, C)$$

**Trap #2**: "Full subtractor same as full adder"

**Wrong if you think**: "Use full adder for subtraction by just inverting" ❌ (missing +1 for 2's complement)
**Correct**: "Full subtractor circuit is similar in structure but carries are borrows" ✓

**Trap #3**: "Ripple carry adder is always slower than CLA"

**Context-dependent**:
- Small $n$ (4-bit): Ripple OK due to gate count (ripple = fewer gates)
- Medium $n$ (8-bit): CLA faster if logic implemented efficiently
- Large $n$ (32+ bit): CLA much faster

**Typical trade-off**: CLA uses ~1.5× more gates but runs at ~2-3× speed.

**GATE Pattern**: "Design a 1-bit full adder using only NAND gates. Gate count?"

**Solution**: 
$$\text{Sum} = A \oplus B \oplus C = (A \oplus B) \oplus C$$
Each XOR needs 4 NAND gates (from Lecture 02)
One XOR with another input = 4 more NANDs
**Total**: ~12 NAND gates (worst case)

**MSQ Logic Gate**: 
- "Full adder can be built from 2 half adders" → **TRUE** ✓
- "Carry-lookahead works for subtraction" → **FALSE** (borrow propagation is different)
- "Sum function uses all 3 inputs symmetrically" → **TRUE** (XOR is symmetric)

**NAT Precision Lock**: 
For $n$-bit addition time:
- Ripple carry: $T = n \times T_{FA}$ (linear)
- CLA (4-bit groups): $T = \frac{n}{4} \times T_{CLA}$ (approximate)
- Tree adder: $T = \log_2(n) \times T_{stage}$ (logarithmic)

### Permanent Recall

**The Bizarre Mnemonic**: 
Imagine adding apples:
- **Half Adder**: You add 2 apples. If sum > 1, carry overflow to next basket.
- **Full Adder**: You add 2 apples + overflow from previous basket (3-way add).
- **Carry**: Each basket holds max 1 apple; overflow goes to next basket.
- **CLA**: Instead of passing apples one by one, you count all apples together and directly determine which baskets overflow.

**The Mental Slider**: 
For any adder:
- 1-bit basic → Half Adder
- 1-bit with carry-in → Full Adder
- $n$-bit simple → Ripple Carry Adder ($O(n)$ time)
- $n$-bit fast → CLA ($O(\log n)$ time, more gates)

**The 5-Second Snap-Check**:
- Full Adder has 5 outputs in K-map: 1 Sum (3-input XOR), 1 Carry (3-input Majority)
- Majority gate appears in many arithmetic circuits
- Subtract using adder: complement B, add, add 1 (or use full subtractor circuit)

---

## [4.5] Comparators | The Equality Detectors

### The Atomic Truth
**Output high if inputs satisfy relation ($A < B$, $A = B$, $A > B$, etc.)**

### The Path of Elegance

#### [4.5.1] 1-Bit Equality Comparator

**Function**: Check if two 1-bit inputs are equal.

**Truth Table**:
| $A$ | $B$ | $A = B$ |
|-----|-----|---------|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Boolean Expression**:
$$A = B \Rightarrow A \odot B = \overline{A \oplus B} = AB + \overline{A}\,\overline{B}$$

**Gate Count**: 1 XNOR gate = 4 two-input gates

#### [4.5.2] 1-Bit Magnitude Comparator

**Function**: Compare magnitudes (A < B, A = B, A > B).

**Truth Table**:
| $A$ | $B$ | $A<B$ | $A=B$ | $A>B$ |
|-----|-----|-------|-------|-------|
| 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 0 |

**Boolean Expressions**:
$$A < B: A < B = \overline{A} \cdot B$$
$$A = B: A = B = \overline{A \oplus B}$$
$$A > B: A > B = A \cdot \overline{B}$$

**Gate Count**: 3 terms = ~5 gates total

#### [4.5.3] N-Bit Magnitude Comparator

**Cascading Logic**:

Compare from MSB down. If $A[n-1] \neq B[n-1]$, result is determined immediately. Otherwise, continue to lower bits.

**Algorithm**:
1. If $A[n-1] > B[n-1]$, then $A > B$ (stop)
2. If $A[n-1] < B[n-1]$, then $A < B$ (stop)
3. If $A[n-1] = B[n-1]$, compare $A[n-2]$ and $B[n-2]$, and so on

**Recursive Logic**:

Define:
- $L_{n-1}$: Result of comparing lower $(n-1)$ bits
  - $L_{n-1}$ can be: $A<B$, $A=B$, or $A>B$

Then $n$-bit comparison:
$$A > B \text{ (n-bit)} = \begin{cases}
1 & \text{if } A[n-1] > B[n-1] \\
L_{n-1} > B & \text{if } A[n-1] = B[n-1]
\end{cases}$$

**Gate Count for $n$-bit**:
- 1-bit comparators: $n$ (one per bit)
- Cascading logic: ~$O(n)$ gates
- **Total**: $O(n)$ gates

**Block Diagram (4-bit)**:
```
A[3] B[3]    A[2] B[2]    A[1] B[1]    A[0] B[0]
  ↓ Comp ↓      ↓ Comp ↓     ↓ Comp ↓      ↓ Comp ↓
  └─────→ Cascade Logic ←──────────────────┘
            outputs A>B, A=B, A<B
```

### The 2026 Adversarial Vault

**Trap #1**: "Gate count for $n$-bit comparator"

**Wrong**: "$2^n$ gates needed" ❌ (confusing with truth table size)
**Correct**: "$O(n)$ gates sufficient" ✓ (cascading bit comparisons)

**Trap #2**: "XNOR is better for equality than XOR"

**In circuits context** ✓: XNOR directly gives equality signal (1 = equal)
**In cost**: Same gate count (4 two-input gates either way)

**GATE Pattern**: "Design a 2-bit magnitude comparator. Gates?"

**Solution**:
- Compare bit 1 (MSB): 2-input magnitude comparator = 5 gates
- If equal, feed to compare bit 0: another 5 gates + mux to select
- **Total**: ~10-12 gates

**MSQ Logic Gate**: 
- "Equality requires XNOR logic" → **FALSE** (XOR + NOT also works)
- "Magnitude comparison is associative" → **FALSE** (MSB has higher priority)
- "Cascaded comparator always O(n)" → **TRUE** for sequential design

---

## [4.6] Parity Generators & Checkers | The Error Detection Circuits

### The Atomic Truth
**Even Parity**: Count of 1s is even. Parity bit = 1 if odd number of 1s in data.
**Odd Parity**: Count of 1s is odd. Parity bit = 1 if even number of 1s in data.

### The Path of Elegance

#### [4.6.1] Parity Generator (Writer)

**Function**: Append a parity bit to data such that total 1s count matches parity rule.

**Example (Even Parity, 3-bit data)**:

| $D_2$ | $D_1$ | $D_0$ | # ones | Parity Bit |
|-------|-------|-------|--------|------------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 2 | 0 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 2 | 0 |
| 1 | 1 | 0 | 2 | 0 |
| 1 | 1 | 1 | 3 | 1 |

**Pattern**: Parity bit = 1 if odd number of 1s in data.

$$P = D_2 \oplus D_1 \oplus D_0$$

This is an $n$-input XOR = **parity function**.

**Key Insight**: XOR of all bits gives parity!

**Gate Count for $n$-bit parity generator**:
- $(n-1)$ cascaded XOR gates
- Each XOR = ~3 gates
- **Total**: ~$3(n-1)$ gates

#### [4.6.2] Parity Checker (Reader)

**Function**: Check if received data (including parity bit) maintains parity rule.

**Logic**:
$$P_{check} = D_{n-1} \oplus D_{n-2} \oplus \cdots \oplus D_0 \oplus P$$

If $P_{check} = 0$ (even parity) → No error detected
If $P_{check} = 1$ (even parity) → Error detected

**Gate Count**: Same as generator, ~$3n$ gates.

#### [4.6.3] Single-Bit Error Detection & Correction (Hamming Code Basics)

For $n$ data bits, use $\log_2(n)$ parity bits strategically placed:

**Example: 4-bit data (4 bits) → 3 parity bits**

- Parity bit $P_1$ checks positions 1, 3, 5, 7 (binary: bit 0 = 1)
- Parity bit $P_2$ checks positions 2, 3, 6, 7 (binary: bit 1 = 1)
- Parity bit $P_4$ checks positions 4, 5, 6, 7 (binary: bit 2 = 1)

Error correction: If syndrome is non-zero, its value points to error position.

$$\text{Error position} = S_2 S_1 S_0 \text{ (syndrome bits)}$$

**Gate Count (7-bit codeword)**:
- 3 syndrome generators: ~9 gates
- Error corrector logic: ~7 gates
- **Total**: ~16 gates

### The 2026 Adversarial Vault

**Trap #1**: "Parity bit prevents errors"

**False** ❌: Parity DETECTS single-bit errors, not corrects them.
**To correct**: Use Hamming code (more parity bits needed).

**Trap #2**: "Even vs Odd parity difference"

**Wrong**: "Odd parity uses more gates" ❌
**Correct**: "Identical gate count, different parity bit logic" ✓

Even: $P = D_{n-1} \oplus \cdots \oplus D_0$
Odd: $P = \overline{D_{n-1} \oplus \cdots \oplus D_0}$

**GATE Pattern**: "4-bit Hamming code: Error in position 3. Correct it?"

**Syndrome = 011₂ = 3 (decimal) → Error in position 3** ✓
Flip bit 3 to correct.

**MSQ Logic Gate**: 
- "XOR is parity function" → **TRUE**
- "XNOR is parity function" → **FALSE** (opposite)
- "Hamming code corrects 2-bit errors" → **FALSE** (corrects 1, detects 2)

---

## [4.7] Code Converters | The Format Transformers

### The Atomic Truth
**Convert between different codes: Binary ↔ Gray, BCD ↔ Binary, Gray ↔ Excess-3, etc.**

### The Path of Elegance

#### [4.7.1] Binary to Gray Converter

**Gray Code Property**: Adjacent codewords differ in exactly one bit.

**Conversion Formula**:
$$G_i = B_i \oplus B_{i+1}$$

where $B_i$ is $i$-th bit of binary, $G_i$ is $i$-th bit of gray.

**Example (4-bit)**:

| Binary | Gray |
|--------|------|
| 0000 | 0000 |
| 0001 | 0001 |
| 0010 | 0011 |
| 0011 | 0010 |
| 0100 | 0110 |
| 0101 | 0111 |
| 0110 | 0101 |
| 0111 | 0100 |
| 1000 | 1100 |
| ... | ... |

**Gate Implementation**:
$$G_3 = B_3$$
$$G_2 = B_3 \oplus B_2$$
$$G_1 = B_2 \oplus B_1$$
$$G_0 = B_1 \oplus B_0$$

**Gate Count**: $(n-1)$ XOR gates for $n$-bit binary.

#### [4.7.2] Gray to Binary Converter

**Reverse Formula**:
$$B_i = B_{i+1} \oplus G_i$$

or equivalently (from MSB):
$$B_i = G_i \oplus G_{i+1} \oplus G_{i+2} \oplus \cdots \oplus G_{n-1}$$

**Gate Implementation**:
$$B_3 = G_3$$
$$B_2 = B_3 \oplus G_2 = G_3 \oplus G_2$$
$$B_1 = B_2 \oplus G_1 = G_3 \oplus G_2 \oplus G_1$$
$$B_0 = B_1 \oplus G_0 = G_3 \oplus G_2 \oplus G_1 \oplus G_0$$

**Gate Count**: 
- 3 XOR gates for MSB computation
- 3 XOR for next bit (cascaded)
- **Total**: ~6 XORs for 4-bit (inefficient)

**Optimized approach** (using parallel XOR):
$$B_i = \bigoplus_{j \geq i} G_j$$

**Gate Count**: $O(n \log n)$ with parallel computation.

#### [4.7.3] BCD to Gray Converter

BCD (4-bit, 0-9) → Gray code (4-bit, single-bit adjacent change)

**Process**:
1. Convert BCD to binary (if needed, but BCD in many systems IS the decimal representation)
2. Binary to Gray
3. BUT: Gray code doesn't have natural BCD meaning

**Practical**: BCD rarely converts to Gray directly; instead use intermediate binary.

#### [4.7.4] Excess-3 to Gray Converter

Excess-3: Encoded as (binary value + 3) in 4 bits.

**Example**:
- 0 → 0011
- 1 → 0100
- 2 → 0101
- ...
- 9 → 1100

**Conversion**:
1. Excess-3 → Binary (subtract 3)
2. Binary → Gray (standard XOR)

**Gate Implementation**: Subtract logic (adder with inverted +1) + Gray converter.

### The 2026 Adversarial Vault

**Trap #1**: "Gray code uses more/fewer gates than binary"

**Context-dependent**: 
- For representing numbers: Same space (both 4-bit)
- For changing between: Binary→Gray (~n XORs) vs Gray→Binary (~n² in naive implementation)

**Trap #2**: "Gray code is useful for arithmetic"

**Wrong**: "Use Gray code for addition" ❌ (arithmetic on Gray code is complex)
**Correct**: "Use Gray for state transitions (rotary encoders, async counters)" ✓

**GATE Pattern**: "4-bit Gray to binary converter using minimal gates?"

**Naive**: Cascade 4 XORs for each output = 6 XORs
**Optimized**: Parallel XOR structure = 4 XORs (each computing binary bit independently)

**MSQ Logic Gate**: 
- "Gray code is self-complementing" → **FALSE** (only for certain codes like Excess-3)
- "Gray code minimizes switching in counters" → **TRUE** (single-bit change)
- "Binary to Gray is reversible" → **TRUE**

---

## [4.8] Master Formula Sheet & Tricks

### Quick Reference

| Circuit | Inputs | Outputs | Gate Count |
|---------|--------|---------|-----------|
| 4:1 MUX | 6 | 1 | ~18 gates |
| 1:4 DEMUX | 3 | 4 | ~8 gates |
| 2:4 Decoder | 2 | 4 | 4 AND + 2 NOT |
| 4:2 Encoder | 4 | 2 | 2 OR |
| 1-bit Full Adder | 3 | 2 | ~9 gates |
| 4-bit Ripple Adder | 9 | 5 | ~36 gates |
| 1-bit Comparator | 2 | 3 | ~5 gates |
| Parity Generator (4-bit) | 4 | 1 | ~3 XORs |

### Implementation Tricks

**Trick #1: Function Realization with MUX**

Any $n$-variable function = one $2^n:1$ MUX (data inputs = minterms, select = variables)

**Trick #2: Arithmetic Fast Path**

For addition speed: Use CLA for 4-bit chunks, cascade 4-bit CLAs.
Gate cost ≈ $1.5 \times$ ripple carry, but speed ≈ $3 \times$ faster.

**Trick #3: Gray Code Advantage**

Use Gray code for async counter / rotary encoder to avoid glitches (multiple bit transitions at once).

**Trick #4: Parity Reduction**

Parity function is XOR of all bits. For fast parity:
- Use parallel prefix XOR (tree structure)
- Reduces delay from $O(n)$ to $O(\log n)$

**Trick #5: Comparator Cascade Optimization**

For equality only: Use single cascaded XNOR (faster than magnitude).
For magnitude: Use hierarchical MSB-first check (stop early if MSB differs).

---

## [4.9] Previous Year Patterns (GATE/ESE)

### GATE 2023-2024

**Q1 (MUX-based logic)**: "Implement $F(A,B,C) = \sum m(0,2,3,5)$ using minimum gates. Best choice?"
- Options: K-map SOP, 4:1 MUX, ROM
- **Trap**: K-map looks better but MUX single gate count may be lower for specific technology

**Q2 (Adder delay)**: "32-bit CLA vs Ripple carry delay ratio?"
- Answer: ~3-4× faster (CLA logarithmic, ripple linear)

**Q3 (Gray code)**: "Binary 1010 to Gray?"
- Answer: 1111 ($B_3=G_3=1$, $G_2=1\oplus0=1$, $G_1=0\oplus1=1$, $G_0=1\oplus0=1$)

### ESE 2023

**Q1 (Decoder application)**: "8:256 memory decoder needs how many 2:4 decoders?"
- Answer: 8 for first stage (decode upper 3 bits) + 64 for second stage = 72 (approx)

**Q2 (Comparator cascade)**: "Design 8-bit comparator using 1-bit comparators?"
- Answer: 8 1-bit comparators + cascade logic, ~40 gates total

### Common Difficulty Levels

**Easy** (~20%): Basic MUX/DEMUX definition, simple gate count
**Medium** (~60%): Cascade design, mixed arithmetic operations, optimization
**Hard** (~20%): Combined optimization (speed vs area), novel applications

### Topic Weightage

- MUX/DEMUX: 15%
- Encoders/Decoders: 10%
- Adders/Subtractors: 25%
- Comparators: 10%
- Parity/Error correction: 15%
- Code converters: 10%
- Combined circuits: 15%

---

## [4.10] NAT Precision & MSQ Strategy

### NAT (Numerical Answer Type) Precision

**Example**: "Minimum gates for 8:1 MUX = ?"

**Process**:
1. Count data AND gates: 8 (each 3-input) = $8 \times 3 = 24$ two-input equivalents
2. Count select OR gate: 1 (8-input) = 7 two-input equivalents
3. Count inverters: 3 = 3 two-input equivalents
4. **Total**: $24 + 7 + 3 = 34$ ✓

**Common NAT Mistakes**:
- Forget to convert multi-input gates to 2-input equivalents
- Forget inverters for select lines
- Count gates differently than expected (ask "2-input or any-input gates?")

### MSQ (Multiple Select Questions) Logic

**Type 1: Function Property MSQ**

Q: "Which statements are true for MUX?"
- (A) Universal gate ✗
- (B) Can implement any combinational function ✓
- (C) Gate count = $2^n + n$ ✗
- (D) Data inputs = $2^n$ ✓

**Type 2: Implementation Trade-off MSQ**

Q: "Compare MUX vs Gate-level implementation for arbitrary 4-bit function"
- MUX: 1 block, straightforward
- Gates: Depends on function (K-map might be simpler)

**Strategy**: Avoid absolute statements; context matters.

---

## [4.11] Permanent Recap

**All-in-one mnemonic**: 
"**CODEC** = **C**ombinational circuits **ODE**c"
- **Routing** (MUX/DEMUX)
- **Decoding** (Encoder/Decoder)
- **Arithmetic** (Adder/Subtractor)
- **Comparison** (Comparators)
- **Protection** (Parity)
- **Translation** (Code converters)

The entire module is ONE cohesive ecosystem for data manipulation without memory!

---

**END OF MODULE 04**
