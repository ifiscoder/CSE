# COA PART 1: QUICK REFERENCE CARD
## Digital Logic & Number Systems | The 5-Minute Refresh

---

## 🔢 NUMBER SYSTEMS CHEAT SHEET

### Conversion Formulas
| **From → To** | **Method** | **Example** |
|---------------|------------|-------------|
| Dec → Bin     | Divide by 2, collect remainders (↑) | $13 \to 1101$ |
| Bin → Dec     | Sum of $d_i \times 2^i$ | $1101 \to 13$ |
| Bin → Oct     | Group by 3 bits | $101110 \to 56_8$ |
| Bin → Hex     | Group by 4 bits | $10111010 \to \text{BA}_{16}$ |

### Fraction Termination Test
$$\text{Decimal fraction terminates in binary} \iff \text{denominator} = 2^k$$

**Examples:**
- $0.5 = \frac{1}{2}$ ✓ terminates
- $0.3 = \frac{3}{10}$ ✗ non-terminating

---

## ➖ SIGNED REPRESENTATIONS

### Range Formulas (n-bit)

| **Type** | **Range** | **Zero Count** |
|----------|-----------|----------------|
| Unsigned | $0$ to $2^n - 1$ | 1 |
| Sign-Magnitude | $-(2^{n-1}-1)$ to $+(2^{n-1}-1)$ | 2 (±0) |
| 1's Complement | $-(2^{n-1}-1)$ to $+(2^{n-1}-1)$ | 2 (±0) |
| **2's Complement** | $-2^{n-1}$ to $2^{n-1}-1$ | **1** ⭐ |

### 2's Complement Shortcuts
1. **Mental Conversion:** Keep bits from right until first 1, flip rest
2. **Quick Negative Check:** MSB = 1 → negative
3. **Decode Formula:** If MSB = 1: $\text{Value} = -2^{n-1} + \text{remaining bits}$

---

## ⚠️ OVERFLOW DETECTION

### The Golden Rule
$$\text{Overflow} = C_{\text{into MSB}} \oplus C_{\text{out of MSB}}$$

### Visual Check
- **Positive + Positive = Negative** → OVERFLOW
- **Negative + Negative = Positive** → OVERFLOW
- **Mixed signs** → NEVER overflow

### Carry vs Overflow

| **Context** | **Carry** | **Overflow** |
|-------------|-----------|--------------|
| Unsigned    | ✓ Matters | ✗ N/A |
| Signed (2C) | ✗ Ignore  | ✓ Matters |

---

## 🌊 IEEE 754 FLOATING POINT

### Format Layout
$$(-1)^S \times 1.M \times 2^{E - \text{Bias}}$$

| **Type** | **Bits** | **Exponent** | **Mantissa** | **Bias** |
|----------|----------|--------------|--------------|----------|
| Single   | 32       | 8            | 23           | 127      |
| Double   | 64       | 11           | 52           | 1023     |

### Special Values Quick Check

| **Exponent** | **Mantissa** | **Value** |
|--------------|--------------|-----------|
| All 0s       | All 0s       | **±0** |
| All 0s       | Non-zero     | Denormalized |
| All 1s       | All 0s       | **±Infinity** |
| All 1s       | Non-zero     | **NaN** |

---

## 🔀 BOOLEAN ALGEBRA ESSENTIALS

### De Morgan's Laws (MOST TESTED)
$$\overline{AB} = \bar{A} + \bar{B}$$
$$\overline{A + B} = \bar{A} \cdot \bar{B}$$

**Mnemonic:** "Break the bar, flip the operator"

### Universal Gates
- **NAND:** $\bar{A} = A \text{ NAND } A$
- **NOR:** $\bar{A} = A \text{ NOR } A$

### Key Identities
| **Law** | **Formula** |
|---------|-------------|
| Absorption | $A + AB = A$ |
| Consensus | $AB + A'C + BC = AB + A'C$ |
| Null | $A \cdot 0 = 0, \quad A + 1 = 1$ |

---

## 🔌 COMBINATIONAL CIRCUITS

### MUX Sizing Formula
$$n \text{ variables} \to 2^n\text{:1 MUX (or } 2^{n-1}\text{:1 with trick)}$$

### Adder Delays
| **Type** | **Delay** | **Hardware** |
|----------|-----------|--------------|
| RCA      | $O(n)$    | Minimal |
| CLA      | $O(\log n)$ | Heavy |

**CLA Formulas:**
$$G_i = A_i \cdot B_i \quad \text{(Generate)}$$
$$P_i = A_i \oplus B_i \quad \text{(Propagate)}$$
$$C_{i+1} = G_i + P_i \cdot C_i$$

---

## 🔄 SEQUENTIAL CIRCUITS

### Flip-Flop Characteristic Equations

| **Type** | **Equation** | **Toggle?** |
|----------|--------------|-------------|
| D        | $Q_{n+1} = D$ | ✗ |
| T        | $Q_{n+1} = T \oplus Q_n$ | ✓ (when $T=1$) |
| JK       | $Q_{n+1} = JQ_n' + K'Q_n$ | ✓ (when $J=K=1$) |
| SR       | $Q_{n+1} = S + R'Q_n$ | ✗ ($SR=11$ invalid) |

### Counter Formulas
$$\text{Mod-}N \text{ counter} \to \text{FFs needed} = \lceil \log_2 N \rceil$$
$$f_{\text{out}} = \frac{f_{\text{in}}}{N}$$

### Shift Register Mods
- **Ring Counter:** Mod = $n$
- **Johnson Counter:** Mod = $2n$

---

## 🗺️ K-MAP ESSENTIALS

### Grouping Rules
1. Groups must be powers of 2: $1, 2, 4, 8, 16$
2. Groups can **wrap around** edges
3. Larger groups = fewer literals

### Literal Count Formula
$$\text{Literals} = n - k \quad \text{(for } 2^k \text{ cell group in } n\text{-var K-map)}$$

**Example:** 4-var K-map, group of 8 cells ($2^3$):
$$\text{Literals} = 4 - 3 = 1$$

---

## 🎯 EXAM QUICK-FIRE CHECKS

### 5-Second Validation Tests

1. **Number System:** Does MSB match sign expectation?
2. **Overflow:** Do operand signs match but result differs?
3. **IEEE 754:** Is exponent 0 or 255? → Special case
4. **Boolean:** Can you simplify with absorption first?
5. **MUX:** Could you use one size smaller?
6. **Flip-Flop:** Does $J=K=1$ mean toggle?
7. **Counter:** Is $\log_2(N)$ rounded **up**?
8. **K-Map:** Did you check wrap-around corners?

---

## 📌 CRITICAL TRAPS TO AVOID

| **Topic** | **Trap** | **Fix** |
|-----------|----------|---------|
| Fractions | Assuming all decimals terminate in binary | Check denominator = $2^k$ |
| 2's Complement | Forgetting $-2^{n-1}$ has no positive pair | Range is asymmetric |
| Overflow | Confusing carry with overflow | Use XOR formula |
| IEEE 754 | Ignoring implicit leading 1 | Always $1.M$ for normalized |
| De Morgan | Applying to nested terms at once | One level at a time |
| MUX | Using full-size when reduced works | Try $2^{n-1}$:1 |
| JK FF | Thinking $J=K=1$ is invalid | It's **toggle** |
| K-Map | Missing corner groups | Corners wrap both ways |

---

## 🔥 RANK-1 MANTRAS

1. **"Radix Point = Power Pivot"** — Everything is weighted sum
2. **"2C = The Chosen One"** — Single zero, uniform arithmetic
3. **"XOR = Overflow Oracle"** — Carry mismatch = overflow
4. **"1.M = IEEE's Hidden Bit"** — Never forget implicit 1
5. **"Break Bar, Flip Op"** — De Morgan's visual rule
6. **"NAND & NOR = God Gates"** — Can build anything
7. **"JK = Smart SR"** — Toggle instead of invalid
8. **"Powers of 2 = Grouping Law"** — K-map gospel

---

## 📊 FORMULA REFERENCE CARD

### Must-Memorize Equations

$$\text{Bits needed} = \lceil \log_2(N) \rceil$$
$$\text{2C Range} = [-2^{n-1}, 2^{n-1}-1]$$
$$\text{Overflow} = C_{\text{in}} \oplus C_{\text{out}}$$
$$\text{IEEE 754} = (-1)^S \times 1.M \times 2^{E-\text{Bias}}$$
$$\text{XOR} = A'B + AB'$$
$$\text{Full Adder Sum} = A \oplus B \oplus C_{\text{in}}$$
$$\text{Full Adder Carry} = AB + C_{\text{in}}(A \oplus B)$$
$$\text{Mod-N Frequency} = \frac{f_{\text{in}}}{N}$$

---

**Status:** Quick Reference Active | Refresh Time: 5 minutes | Mastery Level: SOVEREIGN

**Last Updated:** 2026 GATE/ESE Cycle | IIT Guwahati Standards
