# Module 06: Logic Families | The Hardware Realities

> **The Singularity**: Voltage levels, current, timing, power matter. No circuit is ideal.

---

## [6.1] TTL (Transistor-Transistor Logic) | The Workhorse

### The Atomic Truth
**TTL uses **bipolar transistors**. Typical supply: +5V. Fast, power-hungry.**

### The Path of Elegance

#### [6.1.1] TTL Logic Levels

**Binary representation**:
- **Logic 0 (Low)**: 0V to 0.8V
- **Logic 1 (High)**: 2.0V to 5.0V
- **Undefined (Don't care)**: 0.8V to 2.0V (forbidden zone)

**Noise Margin**:
- **Low-side**: 0.8V (0 guaranteed up to 0.8V)
- **High-side**: 0.7V (5V to 2.0V is safe for 1)
- **Total**: 0.8V + 0.7V = 1.5V

$$\text{Noise Margin} = V_{IL} = 0.8V, \quad V_{IH} = 2.0V$$

**Output Levels**:
- **$V_{OL}$ (output low)**: ≤ 0.4V (guaranteed)
- **$V_{OH}$ (output high)**: ≥ 2.4V (guaranteed)

**Margin Definition**:
$$NM_{low} = V_{IL} - V_{OL} = 0.8 - 0.4 = 0.4V$$
$$NM_{high} = V_{OH} - V_{IH} = 2.4 - 2.0 = 0.4V$$

#### [6.1.2] TTL Gate Structure (NAND)

**Circuit**:
```
      +5V
       │
      ╱ R_C (≈1.6kΩ)
      │
      Q1
      │
      Q2 ─────── Output
      │
  Q3 ─┴─ Q4
  │      │
  A      B (inputs)
```

**Why multiple transistors?**
- **Q1**: Input stage (Schottky diode function, protects from negative voltage)
- **Q2**: Output stage (totem-pole configuration)
- **Q3, Q4**: Input diodes (for multiple inputs on AND/NAND)

#### [6.1.3] TTL Subfamilies

| Subfamily | Power | Speed | $t_p$ | $P_d$ | Use |
|-----------|-------|-------|-------|-------|-----|
| Standard (74) | High | Medium | 10 ns | 10 mW | General |
| **S** (Schottky) | Medium | Fast | 3 ns | 20 mW | Speed-critical |
| **LS** (Low-Power Schottky) | Very Low | Medium | 9 ns | 2 mW | **Most popular** |
| **ALS** (Advanced LS) | Very Low | Fast | 5 ns | 1.3 mW | Modern standard |
| **F** (FAST) | Medium | Very Fast | 4 ns | 6 mW | High-speed |

**Energy-Delay Product** (figure of merit):
$$EDP = P_d \times t_p$$

Lower is better!
- Standard: $10 \times 10 = 100$ (worst)
- LS: $2 \times 9 = 18$ (good balance)
- ALS: $1.3 \times 5 = 6.5$ (best)

#### [6.1.4] Fan-Out (TTL)

**Definition**: Max number of TTL inputs a gate can drive reliably.

**TTL Characteristics**:
- **Output current (sourcing)**: $I_{OH} ≈ -0.4 mA$ (negative = current leaves)
- **Input current (sinking)**: $I_{IH} ≈ 20 μA$ (each input draws this)
- **Fan-out** = $|I_{OH}| / I_{IH}$ = $0.4 mA / 20 μA$ = **20** (standard TTL)

**For LS-TTL**:
- $I_{OH} ≈ -0.4 mA$, $I_{IH} ≈ 20 μA$ → Fan-out ≈ **20** (same)
- But power dissipation much lower

**Practical Fan-out**: 10-15 for noise margin safety (don't push to absolute limit).

#### [6.1.5] Propagation Delay (TTL)

**Definition**: Time from input change to output change.

**For NAND gate**:
$$t_{pd} ≈ 10 \text{ ns (standard)}, 9 \text{ ns (LS)}$$

**Breakdown**:
- **$t_{PHL}$** (High→Low): ~5-6 ns (transistor turn-off)
- **$t_{PLH}$** (Low→High): ~8-10 ns (transistor turn-on, slower due to capacitive charging)

**Path delay in circuit**:
$$T_{circuit} = \sum_{all gates} t_{pd, gate} + \text{wire propagation}$$

For a 32-gate ripple path: $T ≈ 32 \times 10 \text{ ns} = 320 \text{ ns}$

#### [6.1.6] Power Dissipation (TTL)

**Static power** (at rest):
$$P_{static} = I_{cc} \times V_{cc}$$

**$I_{cc}$ depends on output state**:
- Low: ~10 mA (output sinking current to ground)
- High: ~5 mA (output capacitor charging)
- Average: ~7-8 mA per gate

**Dynamic power** (switching):
$$P_{dynamic} = f \times C \times V^2 + \text{short-circuit current}$$

For TTL:
- **Short-circuit current** dominates (totem-pole structure)
- Both upper and lower transistors briefly ON during transition

**Total for a chip** (74LS00 quad NAND):
$$P \approx 40 \text{ mW (at rest)} + 20 \times f \text{ mW (dynamic, f in MHz)}$$

### The 2026 Adversarial Vault

**Trap #1**: "TTL fan-out is unlimited"

**False** ❌: Limited by current (typically 20).
If you exceed fan-out: Output voltage drops, noise margin erodes, logic errors.

**Trap #2**: "TTL and CMOS voltage levels are identical"

**False** ❌:
- TTL: 0-0.8V (0), 2.0-5V (1)
- CMOS: 0-25% VDD (0), 75-100% VDD (1)
- **Interfacing needed!**

**GATE Pattern**: "3-stage TTL ripple chain. What's max frequency?"

**Calculation**:
- Each gate: ~10 ns
- 3 gates: ~30 ns propagation
- $f_{max} = 1/T = 1/30 \text{ ns} ≈ 33 \text{ MHz}$

**MSQ Logic Gate**: 
- "TTL faster than CMOS" → **TRUE** (but less power-efficient)
- "LS-TTL lowest power" → **FALSE** (CMOS lower)
- "TTL works at any voltage" → **FALSE** (designed for 5V ±10%)

**NAT Precision Lock**: 
For TTL gate count to power calculation:
$$P_{total} = n_{gates} \times (I_{cc} \times V_{cc})$$

Example: 100 gates, 8 mA each
$$P = 100 \times (0.008 A \times 5V) = 4W$$

---

## [6.2] CMOS (Complementary MOS) | The Efficiency King

### The Atomic Truth
**CMOS uses **complementary FETs** (NMOS + PMOS pairs). Supply: 3.3V, 5V, etc. Ultra-low static power.**

### The Path of Elegance

#### [6.2.1] CMOS Logic Levels

**Binary representation**:
- **Logic 0 (Low)**: 0V to 30% VDD (e.g., 1.5V for 5V supply)
- **Logic 1 (High)**: 70% VDD to VDD (e.g., 3.5V to 5V for 5V supply)
- **Undefined**: 30%-70% VDD (forbidden)

**For 5V CMOS**:
- $V_{IL} = 1.5V$, $V_{IH} = 3.5V$
- Noise margin: 1.5V (both sides) **- more than TTL!**

**Output levels**:
- $V_{OL}$ ≈ 0V (pulled to ground)
- $V_{OH}$ ≈ VDD (pulled to VDD)

#### [6.2.2] CMOS Inverter (Basic Building Block)

**Circuit**:
```
       VDD
        │
       PMOS (high on top)
        │
        ├──→ Output
        │
       NMOS (low on bottom)
        │
       GND
```

**Operation**:
- **Input Low (0V)**: PMOS ON, NMOS OFF → Output = VDD (High) ✓
- **Input High (VDD)**: PMOS OFF, NMOS ON → Output = GND (Low) ✓

**Key Insight**: Exact opposite of input (inverter). **Never both ON** (except during transition).

**Noise Margin**:

For symmetrical CMOS (matched device sizes):
- $V_{IL} = V_{IH} = VDD / 2 = 2.5V$ (for 5V)
- Noise margins: $\pm 1.25V$ (very robust)

#### [6.2.3] CMOS NAND Gate

**Structure** (2-input):
```
       VDD
        │
    P1 ┌─┴─┐ P2
       │   │
       ├─┬─┤
       │ │ │
       A B Output
       │ │ │
       ├─┴─┤
       │   │
    N1 └─┬─┘ N2
        │
       GND
```

**Network**:
- **Pull-up**: PMOS (P1, P2 in parallel) → drives output to VDD
- **Pull-down**: NMOS (N1, N2 in series) → drives output to GND

**Truth Table**:
| A | B | Output |
|---|---|--------|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Logic**: $\text{Output} = \overline{AB}$ (NAND) ✓

#### [6.2.4] CMOS Fan-Out & Propagation Delay

**Fan-out**: Theoretically **unlimited!** (CMOS draws almost zero static current)

**Practical limit**: Capacitive loading.

**Propagation delay**:
$$t_{pd} ≈ \frac{C_{load} \times V_{dd}}{I}$$

where $I$ is drive current.

**Typical**:
- Standalone gate: $t_{pd} ≈ 5-20 \text{ ns}$ (depends on VDD and load)
- As frequency increases → charge/discharge time reduces
- **CMOS gets faster at lower voltages** (less capacitive charge)

**Dynamic Power** (frequency-dependent):

For CMOS, **static power is negligible** (~pA leakage current).

**Dynamic power**:
$$P_{dynamic} = f \times C \times V_{dd}^2$$

**No short-circuit current** (PMOS and NMOS never both ON).

**Example**: 
- 1 MHz, 1pF capacitive load, 5V supply
- $P = 1 \times 10^6 \times 1 \times 10^{-12} \times 25 = 25 \text{ μW}$ (tiny!)

#### [6.2.5] CMOS Subfamilies

| Family | VDD | Speed | Power | Use |
|--------|-----|-------|-------|-----|
| 74HC (High-Speed CMOS) | 5V | ~8 ns | 1 mW | Modern TTL replacement |
| 74HCT | 5V | ~8 ns | 1 mW | TTL-compatible levels |
| 74AHC | 5V | ~5 ns | 0.5 mW | Faster, lower power |
| 74LVC (Low-Voltage CMOS) | 3.3V or 5V | ~5 ns | 0.2 mW | **Battery-powered** |
| 74LVCH | 3.3V/5V mixed | ~5 ns | 0.2 mW | **Mixed-voltage systems** |

#### [6.2.6] CMOS vs TTL Summary

| Parameter | TTL | CMOS |
|-----------|-----|------|
| Supply voltage | 5V ±10% | 3-15V (flexible) |
| Noise margin | 0.4V | 1.5V (40% VDD) |
| Fan-out (static) | 20 | ∞ |
| Propagation delay | 10 ns | 5-20 ns |
| Static power | ~8 mA | ~1 μA |
| Dynamic power | ~20 mW (10 MHz) | ~10 mW (10 MHz) |
| Noise immunity | Good | Excellent |

### The 2026 Adversarial Vault

**Trap #1**: "CMOS has unlimited fan-out, so can drive infinite loads"

**False** ❌: Fan-out unlimited in **static** sense, but **capacitive loading** limits frequency.

**Trap #2**: "CMOS consumes no power"

**False** ❌: Consumes significant **dynamic power** at high frequencies.
- Static: ~1 μA
- Dynamic at 1 GHz: ~100 mW (huge!)

**Trap #3**: "CMOS slower than TTL"

**Context-dependent**:
- Standalone gate: Similar (~5-10 ns each)
- At high load: CMOS slower (capacitive charging)
- At high frequency: TTL might fail (power dissipation), CMOS better

**GATE Pattern**: "Cascade 32 gates in TTL vs CMOS. Power at 10 MHz?"

**TTL**:
- Static: $32 \times 8 \text{ mA} = 256 \text{ mA} \times 5V = 1.28W$
- Dynamic: $32 \times 20 \text{ mW} = 640 \text{ mW}$
- **Total**: ~2W

**CMOS**:
- Static: negligible
- Dynamic: $f \times C_{load} \times V^2 = 10^7 \times 10^{-11} \times 25 ≈ 2.5 \text{ mW}$
- **Total**: ~2.5 mW (100× lower!)

**MSQ Logic Gate**: 
- "CMOS better for low-power" → **TRUE**
- "TTL better for high-speed" → **FALSE** (modern CMOS comparabl)
- "CMOS needs more complex design" → **FALSE** (simpler actually)

---

## [6.3] ECL (Emitter-Coupled Logic) | The Speed Demon

### The Atomic Truth
**ECL uses **current steering**. Non-saturating bipolar logic. Fastest but hottest.**

### The Path of Elegance

#### [6.3.1] ECL Basics

**Concept**: Instead of switching transistors on/off, steer current between parallel branches.

```
       V_cc
        │
     ┌──┴──┐
    R_c1  R_c2
     │      │
    Q1      Q2 ─────→ Output (or complement)
     │      │
     └──┬───┘
        │
      V_ref (reference voltage)
        │
       GND
```

**Operation**:
- **If input high**: Q1 conducts → Q2 off → Output low
- **If input low**: Q1 off → Q2 conducts → Output high

**Non-saturating transistors** (key advantage):
- Transistors never fully saturate → base charge builds up
- Reduces storage time
- **Much faster switching**: $t_{pd} ≈ 1-2 \text{ ns}$ (!!)

#### [6.3.2] ECL Logic Levels

**Binary representation**:
- **Logic 0 (Low)**: -1.7V
- **Logic 1 (High)**: -0.9V
- Supply: 0V and -5.2V (negative supply!)

**Noise Margin**: 0.8V (narrow, but voltage swing is large in practical circuits)

#### [6.3.3] ECL vs TTL vs CMOS

| Parameter | TTL | CMOS | ECL |
|-----------|-----|------|-----|
| $t_{pd}$ | 10 ns | 5-20 ns | **1-2 ns** |
| Power/gate | 10 mW | 0.1 mW (static) | **50 mW** |
| Noise margin | 0.4V | 1.5V | 0.8V |
| Temperature stability | Good | Excellent | **Poor** (VBE drift) |
| Cost | Low | Very Low | **High** |

#### [6.3.4] When to Use ECL

- **Supercomputers** (1980s-1990s, now obsolete for mainstream)
- **High-speed instrumentation** (real-time measurement)
- **Radar/military** (specialized applications)

**Modern equivalent**: **LVPECL** (Low-Voltage ECL) for differential signaling.

### The 2026 Adversarial Vault

**Trap #1**: "ECL is the fastest logic family"

**Historically TRUE** ✓, but:
- **Modern CMOS** (at lower node sizes) comparable
- **GaAs/InP** even faster (for specialty applications)

**Trap #2**: "ECL power consumption scales with frequency"

**True for CMOS**, but **ECL consumes constant power** (always current steering):
- Static AND dynamic power ≈ same (50 mW per gate, always)

---

## [6.4] Advanced Parameters | The Devil's Details

### [6.4.1] Noise and Immunity

**Noise sources**:
1. **Crosstalk**: Adjacent lines couple capacitively
2. **Ground bounce**: Supply voltage fluctuates due to switching current
3. **Electromagnetic interference** (EMI): External fields induce currents

**Noise margin calculation**:
$$NM = V_{OL}^{max} - V_{IL}^{max} \quad \text{or} \quad V_{OH}^{min} - V_{IH}^{min}$$

**Example (TTL)**:
$$NM_{low} = 0.4V - 0V = 0.4V$$
$$NM_{high} = 2.4V - 2.0V = 0.4V$$

**With noise** (worst case):
- Input must stay in valid range despite noise
- If noise > noise margin → logic error

**CMOS robustness**: Noise margin ≥ 1.5V (3-4× better than TTL)

### [6.4.2] Propagation Delay Variation

**Factors affecting delay**:
1. **Temperature**: -40°C to +85°C (military: -55 to +125°C)
   - TTL: ±5-10% variation
   - CMOS: ±10-15% variation
   
2. **Supply voltage**: VDD ±10% nominal
   - Lower VDD → slower (less current to charge capacitors)
   
3. **Capacitive load**: More load → longer delay
   - Proportional to $\tau = RC$

**Timing analysis** (critical path):

For a chain of gates:
$$T_{total} = \sum t_{pd} + \text{setup time} + \text{hold time}$$

**Worst case** (maximum delay):
- All gates at maximum delay
- Usually at high temperature, low supply

**Best case** (minimum delay):
- All gates at minimum delay
- Matters for **hold time violations**

### [6.4.3] Power Supply Decoupling

**Problem**: High-speed switching → large current spikes → supply voltage droops

**Solution**: Decoupling capacitors (bypass capacitors)

```
       VCC
        │
      ┌─┴──┐
      │ C_bypass (1-100 nF)
      └─┬──┘
        │
      Logic IC
        │
       GND
```

**Capacitor role**:
- **AC current source**: Supplies fast transient current during switching
- Prevents supply noise: $\Delta V = I \times \Delta t / C$

**Rule of thumb**: 1 decoupling cap per 5-10 logic gates.

### [6.4.4] Fanout and Fanin Effects

**Fanout**: Output drives multiple inputs → capacitive load increases → delay increases

**Delay vs fanout**:
$$t_{pd}(n) = t_{pd}(1) + \alpha \times n$$

where $\alpha$ is delay per loaded input (~1-2 ns per input for TTL).

**Fanin**: More gate inputs → more complex logic → possibly slower

**Example (CMOS)**:
- 2-input NAND: ~5 ns
- 4-input NAND: ~7 ns (28% slower)

---

## [6.5] Power Dissipation Analysis | The Energy Budget

### [6.5.1] Static vs Dynamic Power

**Total power**:
$$P_{total} = P_{static} + P_{dynamic}$$

**Static power** (at rest):
- TTL: $P_{static} ≈ I_{cc} \times V_{cc}$ (significant)
- CMOS: $P_{static} ≈ I_{leakage} \times V_{cc}$ (negligible at room temperature)

**Dynamic power** (during switching):
$$P_{dynamic} = f \times C \times V^2 + P_{short-circuit}$$

**$f$**: Clock frequency
**$C$**: Total capacitance switched per cycle
**$V$**: Supply voltage

**Short-circuit power** (brief interval when both transistors ON):
- TTL: ~50% of total dynamic power (totem-pole design)
- CMOS: ~10% of total dynamic power (minimal overlap)

### [6.5.2] Energy per Switching Event

**Energy per gate transition**:
$$E = \int P \, dt ≈ C \times V \times \Delta V$$

**For CMOS**:
$$E ≈ C \times V_{dd}^2 \quad (\text{per complete cycle})$$

**Example**: 
- C = 10 pF, VDD = 5V
- $E = 10^{-11} \times 25 = 250 \text{ fJ}$ (femtojoules)

**At 1 GHz**: $250 \text{ fJ} \times 10^9 = 250 \text{ mW}$ for single gate (scales with gate count!)

### [6.5.3] Power Optimization Techniques

**1. Voltage scaling** (most effective):
$$P \propto V^2 \quad \Rightarrow \quad \text{Halving V reduces P by 4×!}$$

Modern CPUs: 5V → 3.3V → 1.8V → 0.9V over decades

**2. Clock gating**:
Disable clock to unused functional units (ASIC design).

**3. Power gating**:
Cut supply to inactive blocks (advanced power management).

**4. Dynamic voltage/frequency scaling** (DVFS):
Adjust VDD and frequency based on workload.

### The 2026 Adversarial Vault

**Trap #1**: "Faster logic families always use more power"

**False** ❌:
- ECL: Always high power (current steering)
- CMOS at high frequency: High power (mainly dynamic)
- CMOS at low frequency: Low power
- TTL: Constant moderate power

**Trap #2**: "Power dissipation independent of design"

**False** ❌:
- Data patterns matter (switching activity)
- Fanout and routing affect capacitive load
- Clock frequency affects dynamic power

**GATE Pattern**: "32-bit register at 100 MHz. CMOS vs TTL power?"

**Assumptions**:
- 100 MHz clock → 100M transitions/sec per net
- ~1000 nets total → 100B transitions/sec
- CMOS (0.1 nJ/transition): $100B \times 0.1 \text{ nJ} = 10 \text{ W}$
- TTL (0.5 nJ/transition): $100B \times 0.5 \text{ nJ} = 50 \text{ W}$

**Conclusion**: CMOS wins by 5×

---

## [6.6] Master Formula Sheet

### Logic Levels & Margins

**TTL**:
- $V_{IL} = 0.8V, V_{IH} = 2.0V$
- $V_{OL} = 0.4V, V_{OH} = 2.4V$
- $NM = 0.4V$

**CMOS** (5V):
- $V_{IL} = 1.5V, V_{IH} = 3.5V$
- $V_{OL} ≈ 0V, V_{OH} ≈ 5V$
- $NM = 1.5V$

### Timing Formulas

**Propagation delay**:
$$t_{pd} = t_{0} + k \times C_{load}$$

**Fan-out effect**:
$$\Delta t_{pd} ≈ 1-2 \text{ ns/input}$$

**Cascade delay** (n stages):
$$T_{cascade} = n \times t_{pd} + setup/hold times$$

### Power Formulas

**CMOS Dynamic**:
$$P = f \times C \times V^2 \times \alpha$$

where $\alpha$ = switching activity (0-1)

**TTL Static**:
$$P ≈ n \times I_{cc} \times V_{cc}$$

**ECL Constant**:
$$P ≈ n \times 50 \text{ mW/gate}$$

---

## [6.7] Previous Year Patterns (GATE/ESE)

### GATE 2023-2024

**Q1 (Noise margin)**: "Which logic family has highest noise immunity?"
- Answer: CMOS (1.5V margin vs 0.4V for TTL)

**Q2 (Fanout)**: "TTL gate drives 25 inputs. What happens?"
- Answer: Output voltage drops below guaranteed high level → logic errors

**Q3 (Power comparison)**: "100 gates at 10 MHz: TTL vs CMOS power?"
- Answer: TTL ~800mW, CMOS ~10mW (80× difference)

### ESE 2023

**Q1 (ECL timing)**: "ECL propagation delay vs CMOS?"
- Answer: ECL 1-2 ns, CMOS 5-20 ns (ECL 10× faster, but higher power)

**Q2 (Supply decoupling)**: "Why use bypass capacitors?"
- Answer: Reduce power supply noise from switching current spikes

### Common Difficulty Levels

**Easy** (~20%): Logic levels, basic noise margin
**Medium** (~60%): Fanout calculations, delay analysis
**Hard** (~20%): Power dissipation optimization, complex timing paths

### Topic Weightage

- Logic Levels: 15%
- Noise Margin: 15%
- Propagation Delay: 20%
- Fan-in/Fan-out: 15%
- Power Dissipation: 20%
- Family Comparison: 15%

---

## [6.8] NAT Precision & MSQ Strategy

### NAT Examples

**Q**: "CMOS fanout: how many gates can single output drive?"
- **Technically**: Infinite (theoretically)
- **Practically**: Depends on frequency and load
- **Answer context**: Either "infinite" or "depends on frequency" (look for right answer format)

**Q**: "TTL gate drives N inputs. Max N before noise margin gone?"
- $NM = V_{OL}^{max} - V_{IL}^{max} = 0.4V - 0V = 0.4V$
- If capacitive load drops $V_{OH}$ by 0.4V → $V_{OH} = 2.4 - 0.4 = 2.0V = V_{IH}$
- So **N** depends on capacitive load per input and slew rate
- **Typical answer**: 10-15 (safety margin from absolute 20)

### MSQ Strategy

**Type 1: Family property MSQ**

Q: "TTL characteristics"
- (A) Lower power than CMOS ✗
- (B) Limited fanout ✓
- (C) Higher noise margin than CMOS ✗
- (D) Works at 5V ✓

**Type 2: Timing MSQ**

Q: "Propagation delay factors"
- (A) Gate type ✓
- (B) Frequency ✗ (delay ≈ constant for given load)
- (C) Capacitive load ✓
- (D) Temperature ✓

---

## [6.9] Permanent Recap

**All-in-one**: 
- **TTL** = Balanced, 5V, 0.4V margin, 10 ns, 10 mW/gate
- **CMOS** = Ultra-low static, flexible voltage, 1.5V margin, 5-20 ns, 0.1 mW/gate
- **ECL** = Blazing fast (1-2 ns), extreme power (50 mW), temperature-sensitive, rare

**Choose based on**:
- **Power-critical** → CMOS (battery, portable)
- **Speed-critical** → Modern CMOS (or ECL if cost no object)
- **Mixed-signal** → CMOS (noise immunity)
- **Legacy system** → TTL (compatibility)

---

**END OF MODULE 06**
