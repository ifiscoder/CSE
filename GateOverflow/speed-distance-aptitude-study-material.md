# Speed and Distance | Complete Aptitude Mastery Guide
### **For GATE · ESE · PSU · BANK Exams (2026 Edition)**

---

## Table of Contents

1. [The Atomic Foundation — What Is Speed?](#1-the-atomic-foundation)
2. [The Core Formula — Derivation from First Principles](#2-the-core-formula)
3. [Unit Conversions — The Silent Killer](#3-unit-conversions)
4. [Average Speed — The #1 Exam Trap](#4-average-speed)
5. [Relative Speed — Two Bodies in Motion](#5-relative-speed)
6. [Trains — The Classic Application](#6-trains)
7. [Boats and Streams — Speed in a Medium](#7-boats-and-streams)
8. [Races and Circular Tracks](#8-races-and-circular-tracks)
9. [Clocks — Hidden Speed-Distance](#9-clocks)
10. [Proportionality — The Golden Shortcut](#10-proportionality)
11. [Problems on Changing Speed](#11-problems-on-changing-speed)
12. [Meeting Point Problems](#12-meeting-point-problems)
13. [Escalators and Moving Walkways](#13-escalators-and-moving-walkways)
14. [Zig-Zag / Return Journey Problems](#14-zig-zag--return-journey-problems)
15. [Practice Problem Vault with Solutions](#15-practice-problem-vault)
16. [Permanent Recall — Mnemonics & Snap-Checks](#16-permanent-recall)

---

## 1. The Atomic Foundation

**The Atomic Truth:** *Distance equals speed multiplied by time.*

### Why Does This Formula Exist?

Imagine you're walking at a steady pace. Every second, you cover the same small stretch of ground. If you walk for twice as long, you cover twice the ground. If you walk twice as fast, you also cover twice the ground.

This intuition is the entire foundation:

$$\boxed{Distance = Speed \times Time}$$

This is not a "formula to memorize." It is a **definition**: speed is the rate at which distance is covered per unit time.

$$Speed = \frac{Distance}{Time}, \quad Time = \frac{Distance}{Speed}$$

**Analogy — The Water Tank:**
Think of a pipe filling a tank. The *flow rate* (liters/min) is like speed. The *total water* is distance. The *time* is how long the tap runs. If the tap flows at 5 L/min for 10 minutes, you get 50 L. Same logic: 5 km/hr for 10 hours = 50 km.

### The Triangle Trick (Visual Aid)

```
        [ D ]
       /     \
     [ S ] × [ T ]
```

Cover what you want to find:
- Cover **D** → what's left is **S × T**
- Cover **S** → what's left is **D ÷ T**
- Cover **T** → what's left is **D ÷ S**

---

## 2. The Core Formula

### Derivation from First Principles

Consider a body moving along a straight line. At time $t = 0$, position is $x_0$. At time $t$, position is $x$.

$$\text{Average Speed} = \frac{\text{Total Distance Covered}}{\text{Total Time Taken}} = \frac{|x - x_0|}{t - 0}$$

For **uniform motion** (constant speed $v$):

$$x = x_0 + v \cdot t$$

$$\Rightarrow v = \frac{x - x_0}{t} = \frac{d}{t}$$

$$\boxed{d = v \times t}$$

**Why this matters:** Every single problem in this chapter — trains, boats, races, clocks — is just this one equation dressed in different clothes.

---

## 3. Unit Conversions

### The Silent Killer in Exams

Most errors in Speed-Distance problems come not from logic, but from **mismatched units**.

### km/hr to m/s

$$1 \text{ km/hr} = \frac{1000 \text{ m}}{3600 \text{ s}} = \frac{5}{18} \text{ m/s}$$

**How the factor came:**
- 1 km = 1000 m
- 1 hr = 3600 s (60 min × 60 s)
- So: $\frac{1000}{3600} = \frac{5}{18}$

$$\boxed{\text{km/hr} \to \text{m/s}: \text{Multiply by } \frac{5}{18}}$$

$$\boxed{\text{m/s} \to \text{km/hr}: \text{Multiply by } \frac{18}{5}}$$

**The Mnemonic:** "**Five-Eighteen**" — *km/hr is the bigger unit name but the smaller number. Divide (multiply by 5/18) to go smaller.*

### Quick Reference Table

| From | To | Multiply by |
|------|----|-------------|
| km/hr | m/s | $\frac{5}{18}$ |
| m/s | km/hr | $\frac{18}{5}$ |
| km/hr | m/min | $\frac{50}{3}$ |
| miles/hr | ft/s | $\frac{22}{15}$ |

### Example

> Convert 72 km/hr to m/s.

$$72 \times \frac{5}{18} = \frac{360}{18} = 20 \text{ m/s}$$

**Edge Case:** When a problem gives speed in km/hr and length in meters, you **must** convert before computing. This is where 30% of exam errors occur.

---

## 4. Average Speed

### The #1 Trap in Competitive Exams

> **Trap Alert:** Average speed is **NOT** the arithmetic mean of speeds. It is the total distance divided by total time.

$$\boxed{\text{Average Speed} = \frac{\text{Total Distance}}{\text{Total Time}}}$$

### Case 1: Same Distance, Different Speeds

A person travels a distance $d$ at speed $a$ and returns the same distance at speed $b$.

- Time for first half: $t_1 = \frac{d}{a}$
- Time for second half: $t_2 = \frac{d}{b}$
- Total distance: $2d$
- Total time: $\frac{d}{a} + \frac{d}{b} = d \cdot \frac{a+b}{ab}$

$$\text{Average Speed} = \frac{2d}{d \cdot \frac{a+b}{ab}} = \frac{2ab}{a+b}$$

$$\boxed{\text{Same distance, two speeds:} \quad S_{avg} = \frac{2ab}{a+b} \quad \text{(Harmonic Mean)}}$$

**Why Harmonic Mean?** Because when the *distance* is constant, the time is inversely proportional to speed. The harmonic mean naturally weights by the *reciprocals* — which is exactly what "constant distance, varying speed" demands.

**Analogy:** If you eat half a pizza slowly and half quickly, the "average eating speed" is pulled toward the slower rate — because you spent *more time* eating slowly. That's the harmonic mean.

### Example

> A car travels from A to B at 40 km/hr and returns at 60 km/hr. Find the average speed.

$$S_{avg} = \frac{2 \times 40 \times 60}{40 + 60} = \frac{4800}{100} = 48 \text{ km/hr}$$

**Trap:** A student who averages $(40+60)/2 = 50$ km/hr gets the **wrong answer**. The correct answer is always **less than** the arithmetic mean when distances are equal.

### Case 2: Same Time, Different Speeds

$$\boxed{\text{Same time, two speeds:} \quad S_{avg} = \frac{a+b}{2} \quad \text{(Arithmetic Mean)}}$$

**Why Arithmetic Mean here?** When times are equal, each speed contributes equally to the total distance. No weighting is needed.

### Case 3: Three Speeds, Equal Distances

$$S_{avg} = \frac{3}{\frac{1}{a} + \frac{1}{b} + \frac{1}{c}} = \frac{3abc}{ab + bc + ca}$$

### The 5-Second Snap-Check

> The average speed for equal distances is **always less than** the arithmetic mean of the speeds (unless all speeds are equal). If your answer exceeds the arithmetic mean, it's **wrong**.

---

## 5. Relative Speed

### Two Bodies in Motion

**Core Idea:** When two objects move, what matters is how fast the gap between them changes.

### Same Direction

$$\boxed{S_{relative} = |S_1 - S_2|}$$

**Why?** Both objects eat into the same distance. The faster one only "gains" by the difference.

**Analogy:** Two runners on a track — the faster one laps the slower one. The gap closes at a rate equal to the *difference* in their speeds.

### Opposite Direction

$$\boxed{S_{relative} = S_1 + S_2}$$

**Why?** They approach each other. Both contribute to closing the gap.

**Analogy:** Two cars driving toward each other on a highway. If both go 60 km/hr, the gap shrinks at 120 km/hr.

### Example — The Classic Chase

> A thief starts running at 8 km/hr. A policeman starts chasing 15 minutes later at 10 km/hr. When will the policeman catch the thief?

**Step 1:** In 15 min, the thief covers $8 \times \frac{15}{60} = 2$ km (head start).

**Step 2:** Relative speed (same direction) = $10 - 8 = 2$ km/hr.

**Step 3:** Time to close the 2 km gap = $\frac{2}{2} = 1$ hr.

The policeman catches the thief **1 hour** after starting (i.e., 1 hr 15 min after the thief started).

---

## 6. Trains

### Why Trains Are Special

A train is not a point — it has **length**. When a train "crosses" something, it must cover **its own length** plus the length of the object.

### Case 1: Train Crossing a Pole / Standing Person

The train must cover **its own length**.

$$\boxed{Time = \frac{L_{train}}{S_{train}}}$$

**Why?** A pole is a point object (length ≈ 0). The front of the train reaches the pole, then the entire body must pass. Total distance = length of train.

### Case 2: Train Crossing a Platform / Bridge

The train must cover **its own length + platform length**.

$$\boxed{Time = \frac{L_{train} + L_{platform}}{S_{train}}}$$

**Why?** The front of the train starts at one end of the platform. Crossing is complete when the *tail* of the train clears the other end. So total distance = $L_{train} + L_{platform}$.

### Case 3: Two Trains Crossing Each Other

**Opposite directions:**

$$Time = \frac{L_1 + L_2}{S_1 + S_2}$$

**Same direction:**

$$Time = \frac{L_1 + L_2}{|S_1 - S_2|}$$

**Why?** For crossing to be complete, the combined length must be covered. The rate of coverage depends on relative speed.

### Example

> A train 150 m long crosses a platform 250 m long in 20 seconds. Find the speed of the train.

$$S = \frac{L_{train} + L_{platform}}{T} = \frac{150 + 250}{20} = \frac{400}{20} = 20 \text{ m/s}$$

Convert to km/hr: $20 \times \frac{18}{5} = 72$ km/hr.

### Example — Two Trains

> Two trains of lengths 100 m and 200 m run at 40 km/hr and 32 km/hr in opposite directions. How long do they take to cross each other?

**Step 1:** Convert speeds to m/s:
- $40 \times \frac{5}{18} = \frac{100}{9}$ m/s
- $32 \times \frac{5}{18} = \frac{160}{18} = \frac{80}{9}$ m/s

**Step 2:** Relative speed = $\frac{100}{9} + \frac{80}{9} = \frac{180}{9} = 20$ m/s

**Step 3:** Total distance = $100 + 200 = 300$ m

**Step 4:** Time = $\frac{300}{20} = 15$ seconds

### Edge Cases for Trains

| Scenario | Distance to Cover |
|----------|-------------------|
| Train passes a pole | $L_{train}$ |
| Train passes a person walking same direction | $L_{train}$, use relative speed $S_t - S_p$ |
| Train passes a person walking opposite direction | $L_{train}$, use relative speed $S_t + S_p$ |
| Train crosses a bridge | $L_{train} + L_{bridge}$ |
| Train enters a tunnel completely | $L_{tunnel} - L_{train}$ (train must fit inside) |
| Two trains cross each other | $L_1 + L_2$ |

### Train Passing a Man on Another Train

> A man sitting on a train sees another train pass him. The distance covered = length of the *other* train. Speed used = relative speed.

---

## 7. Boats and Streams

### Speed in a Medium

**Core Concept:** A boat has its own speed (in still water). The stream adds or subtracts from it.

- **Downstream** (with current): Effective speed = $B + S$
- **Upstream** (against current): Effective speed = $B - S$

Where:
- $B$ = speed of boat in still water
- $S$ = speed of stream/current

### Why?

**Analogy:** Imagine walking on a moving walkway at an airport.
- Walking *with* the walkway: your effective speed = your speed + walkway speed.
- Walking *against* it: your effective speed = your speed − walkway speed.

### Deriving B and S from Downstream/Upstream Speeds

Let downstream speed = $D$, upstream speed = $U$.

$$D = B + S, \quad U = B - S$$

Add: $D + U = 2B \Rightarrow B = \frac{D + U}{2}$

Subtract: $D - U = 2S \Rightarrow S = \frac{D - U}{2}$

$$\boxed{B = \frac{D + U}{2}, \quad S = \frac{D - U}{2}}$$

### Example

> A boat goes 24 km downstream in 2 hours and 24 km upstream in 3 hours. Find the speed of the boat in still water and the speed of the current.

- Downstream speed: $D = \frac{24}{2} = 12$ km/hr
- Upstream speed: $U = \frac{24}{3} = 8$ km/hr
- $B = \frac{12 + 8}{2} = 10$ km/hr
- $S = \frac{12 - 8}{2} = 2$ km/hr

### Round Trip in Streams

> Time for a round trip of distance $d$:

$$T = \frac{d}{B+S} + \frac{d}{B-S} = d \cdot \frac{(B-S) + (B+S)}{(B+S)(B-S)} = \frac{2dB}{B^2 - S^2}$$

$$\boxed{T_{round} = \frac{2dB}{B^2 - S^2}}$$

**Key Insight:** If $S \geq B$, the boat **cannot** go upstream. This is a common edge case tested in exams.

### Special Case — Still Water Speed Equals Stream Speed ($B = S$)

- Downstream speed = $2B$, upstream speed = $0$.
- The boat is effectively stranded upstream. Round trip is **impossible**.

---

## 8. Races and Circular Tracks

### Linear Races

**Terminology:**
- "A beats B by $x$ meters" → When A finishes, B is $x$ m behind the finish line.
- "A beats B by $t$ seconds" → B finishes $t$ seconds after A.
- "A gives B a head start of $x$ meters" → B starts $x$ m ahead of A.

### Example

> In a 1000 m race, A beats B by 50 m. In the same race, B beats C by 40 m. By how much does A beat C?

**Step 1:** When A covers 1000 m, B covers 950 m.

Speed ratio: $\frac{S_A}{S_B} = \frac{1000}{950} = \frac{20}{19}$

**Step 2:** When B covers 1000 m, C covers 960 m.

Speed ratio: $\frac{S_B}{S_C} = \frac{1000}{960} = \frac{25}{24}$

**Step 3:** $\frac{S_A}{S_C} = \frac{S_A}{S_B} \times \frac{S_B}{S_C} = \frac{20}{19} \times \frac{25}{24} = \frac{500}{456} = \frac{125}{114}$

When A covers 1000 m, C covers $\frac{114}{125} \times 1000 = 912$ m.

**A beats C by $1000 - 912 = 88$ m.**

**Trap:** The wrong approach is $50 + 40 = 90$ m. The correct answer (88 m) accounts for the compounding effect.

### Circular Tracks

**Two people start from the same point on a circular track of length $L$.**

**Same direction:**
- Relative speed = $|S_1 - S_2|$
- They meet when the faster one gains a full lap over the slower one.
- $\boxed{T_{meet} = \frac{L}{|S_1 - S_2|}}$

**Opposite directions:**
- Relative speed = $S_1 + S_2$
- $\boxed{T_{meet} = \frac{L}{S_1 + S_2}}$

### First Meeting at Starting Point

They meet at the starting point when both have completed an **integer** number of laps.

$$T = \text{LCM}\left(\frac{L}{S_1}, \frac{L}{S_2}\right)$$

### Example

> A and B run around a circular track of 600 m at speeds 10 m/s and 6 m/s.

**Opposite directions:** First meeting time = $\frac{600}{10+6} = \frac{600}{16} = 37.5$ s

**Same direction:** First meeting time = $\frac{600}{10-6} = \frac{600}{4} = 150$ s

**At starting point:**
- A's lap time = $\frac{600}{10} = 60$ s
- B's lap time = $\frac{600}{6} = 100$ s
- LCM(60, 100) = 300 s → They meet at the starting point after **300 seconds**.

---

## 9. Clocks

### Hidden Speed-Distance

A clock is a **circular track** problem where the minute hand and hour hand are two runners.

### Speeds of the Hands

- Minute hand: $360°$ in 60 min → speed = $6°$/min
- Hour hand: $360°$ in 12 hr (720 min) → speed = $0.5°$/min

**Relative speed** of minute hand over hour hand:

$$6 - 0.5 = 5.5°/\text{min}$$

### How the "Coincidence" Formula Works

The hands overlap when the minute hand gains $360°$ over the hour hand.

$$\text{Time between overlaps} = \frac{360°}{5.5°/\text{min}} = \frac{720}{11} \approx 65.45 \text{ min}$$

In 12 hours, the hands coincide **11 times** (not 12 — the overlap at 12:00 is shared between cycles).

### The Angle Formula

At $h$ hours and $m$ minutes:

$$\theta = \left| 30h - \frac{11m}{2} \right|$$

**Derivation:**
- Hour hand position from 12: each hour = $30°$, each minute = $0.5°$ → position = $30h + 0.5m$
- Minute hand position from 12: each minute = $6°$ → position = $6m$
- Angle between them: $|30h + 0.5m - 6m| = |30h - 5.5m|$

$$\boxed{\theta = \left|30h - \frac{11m}{2}\right|}$$

If $\theta > 180°$, use $360° - \theta$.

### Example

> Find the angle between the hands at 3:20.

$$\theta = \left|30(3) - \frac{11(20)}{2}\right| = |90 - 110| = 20°$$

### Gaining/Losing Clocks

A clock that gains $x$ minutes per hour runs at speed $\frac{60+x}{60}$ times normal.

A clock that loses $x$ minutes per hour runs at speed $\frac{60-x}{60}$ times normal.

### Example

> A clock gains 5 minutes every hour. What is the actual time when the clock shows 10:00 PM, if it was set right at 8:00 AM?

Clock shows 14 hours elapsed (8 AM to 10 PM).

In 1 real hour, clock shows 65 min.

So 14 clock-hours = $14 \times 60 = 840$ clock-minutes.

Real time = $\frac{840}{65} \times 60 = \frac{840 \times 60}{65} = \frac{50400}{65} \approx 775.38$ min $= 12$ hr $55.38$ min.

Actual time ≈ $8:00$ AM $+ 12$ hr $55$ min $\approx 8:55$ PM.

---

## 10. Proportionality

### The Golden Shortcut

This is the **most powerful technique** for solving speed-distance problems in competitive exams without lengthy calculations.

From $D = S \times T$:

### When Distance is Constant

$$S \times T = \text{constant} \Rightarrow S \propto \frac{1}{T}$$

$$\boxed{\frac{S_1}{S_2} = \frac{T_2}{T_1}}$$

**Speed and time are inversely proportional.**

If speed increases by $\frac{1}{4}$ (becomes $\frac{5}{4}$ of original), time decreases to $\frac{4}{5}$ of original.

### When Time is Constant

$$D \propto S$$

$$\boxed{\frac{D_1}{D_2} = \frac{S_1}{S_2}}$$

### When Speed is Constant

$$D \propto T$$

### Example — The Percentage Shortcut

> A man walks at $\frac{4}{5}$ of his usual speed. He reaches 15 minutes late. Find his usual time.

**Step 1:** Speed ratio = $\frac{4}{5}$ → Time ratio = $\frac{5}{4}$ (inverse).

**Step 2:** New time = $\frac{5}{4}$ of usual time. So extra time = $\frac{5}{4}T - T = \frac{T}{4}$.

**Step 3:** $\frac{T}{4} = 15$ min → $T = 60$ min.

### The General "Late/Early" Formula

If a person travels at speed $S_1$ and reaches $t_1$ late, and at speed $S_2$ and reaches $t_2$ early:

$$\boxed{D = \frac{S_1 \cdot S_2 \cdot (t_1 + t_2)}{S_2 - S_1}}$$

**Derivation:**

Let actual time = $T$. Distance $D$ is constant.

$$D = S_1(T + t_1) = S_2(T - t_2)$$

From both:
$$S_1 T + S_1 t_1 = S_2 T - S_2 t_2$$
$$T(S_2 - S_1) = S_1 t_1 + S_2 t_2$$
$$T = \frac{S_1 t_1 + S_2 t_2}{S_2 - S_1}$$

$$D = S_1(T + t_1) = S_1 \cdot \frac{S_1 t_1 + S_2 t_2 + S_1 t_1 + S_2 t_1 - S_1 t_1}{S_2 - S_1}$$

Simplifying more directly:

$$D = S_1 \cdot \frac{S_2(t_1 + t_2)}{S_2 - S_1} + S_1 t_1$$

The clean form when both late and early offsets are from the *same* scheduled arrival:

$$\boxed{D = \frac{S_1 \times S_2 \times (t_1 + t_2)}{S_2 - S_1}}$$

(Make sure $t_1$ and $t_2$ are in consistent units with speed.)

### Example

> Walking at 4 km/hr, a person reaches 10 min late. Walking at 6 km/hr, he reaches 10 min early. Find the distance.

$$D = \frac{4 \times 6 \times (10 + 10)}{6 - 4} = \frac{4 \times 6 \times 20}{2} = \frac{480}{2} = 240 \text{ (in min·km/hr)}$$

Convert: $240$ min·km/hr = $\frac{240}{60}$ km = **4 km**.

---

## 11. Problems on Changing Speed

### Concept

When a person changes speed partway through a journey, use the constraint that partial distances or partial times sum to the total.

### Case 1: Travels Part Distance at One Speed, Rest at Another

Total distance $D$, first part $d_1$ at speed $S_1$, remaining $d_2 = D - d_1$ at speed $S_2$.

$$T_{total} = \frac{d_1}{S_1} + \frac{D - d_1}{S_2}$$

### Case 2: Speed Changes After a Given Time

Travels at $S_1$ for time $t_1$, then at $S_2$ for time $t_2$.

$$D = S_1 t_1 + S_2 t_2$$

### Example

> A person covers half the distance at 40 km/hr and the remaining half at 60 km/hr. Find the average speed.

This is the "equal distance" case:

$$S_{avg} = \frac{2 \times 40 \times 60}{40 + 60} = \frac{4800}{100} = 48 \text{ km/hr}$$

### Example — Three-Part Journey

> A man travels 1/3 of the distance at 10 km/hr, next 1/3 at 20 km/hr, and the last 1/3 at 60 km/hr. Find the average speed.

$$S_{avg} = \frac{3}{\frac{1}{10} + \frac{1}{20} + \frac{1}{60}} = \frac{3}{\frac{6 + 3 + 1}{60}} = \frac{3}{\frac{10}{60}} = \frac{3 \times 60}{10} = 18 \text{ km/hr}$$

---

## 12. Meeting Point Problems

### Two People Start Simultaneously from Two Ends

$A$ starts from point P, $B$ starts from point Q. Distance PQ = $D$.

**First Meeting:**

$$\text{Time} = \frac{D}{S_A + S_B}$$

At the first meeting, $A$ covers $\frac{S_A}{S_A + S_B} \times D$ from P.

**The Distance Ratio Rule:**

$$\frac{\text{Distance by A}}{\text{Distance by B}} = \frac{S_A}{S_B}$$

(Because time is the same for both.)

### Multiple Meetings

**Key Insight:** Between two endpoints, the $n^{th}$ meeting occurs when the combined distance covered by both is $(2n-1) \times D$.

- 1st meeting: combined distance = $D$
- 2nd meeting: combined distance = $3D$
- 3rd meeting: combined distance = $5D$
- $n^{th}$ meeting: combined distance = $(2n-1) \times D$

**Why?** After the first meeting, both continue to the opposite ends, turn around, and meet again. Each "leg" between meetings requires them to collectively cover $2D$ more.

### Example

> A and B start from two ends of a 600 m track. A's speed = 5 m/s, B's speed = 7 m/s. Where do they meet for the 4th time?

Combined distance at 4th meeting = $(2 \times 4 - 1) \times 600 = 7 \times 600 = 4200$ m.

$A$ covers $\frac{5}{5+7} \times 4200 = \frac{5}{12} \times 4200 = 1750$ m from his starting point.

$1750 = 2 \times 600 + 550$. After 2 full trips (1200 m), A is going forward again from his start, $550$ m into the track.

**4th meeting point: 550 m from A's end.**

---

## 13. Escalators and Moving Walkways

### Concept

An escalator is exactly like a **boat and stream** problem, but for steps.

- Person's speed: $P$ steps/min
- Escalator's speed: $E$ steps/min
- Total steps visible (when escalator is stationary): $N$

**Going with the escalator (down on a down-escalator):**

$$\text{Time} = \frac{N}{P + E}, \quad \text{Steps taken by person} = P \times \frac{N}{P+E} = \frac{NP}{P+E}$$

**Going against the escalator:**

$$\text{Time} = \frac{N}{P - E} \quad (P > E), \quad \text{Steps taken by person} = \frac{NP}{P-E}$$

### Finding Total Steps $N$

If a person takes $a$ steps going with and $b$ steps going against:

$$\frac{a}{P} = \frac{N}{P+E} \Rightarrow N = a \cdot \frac{P+E}{P} = a + a\frac{E}{P}$$

$$\frac{b}{P} = \frac{N}{P-E} \Rightarrow N = b \cdot \frac{P-E}{P} = b - b\frac{E}{P}$$

Adding: $2N = a + b \Rightarrow N = \frac{a+b}{2}$... (only when step rates are equal)

More precisely, if the person's step rate is the same in both directions:

$$\boxed{N = \frac{a + b}{2}} \quad \text{(steps climbed with + steps climbed against, divided by 2)}$$

This is because:
- Going with: person covers $(P+E) \times t_1 = N$, person's steps = $P \times t_1 = a$
- Going against: $(P-E) \times t_2 = N$, person's steps = $P \times t_2 = b$
- From these: $N = a + E \cdot t_1 = a + E \cdot \frac{a}{P}$ and $N = b - E \cdot t_2 = b - E \cdot \frac{b}{P}$
- Adding: $2N = a + b$ → $N = \frac{a+b}{2}$ ✓

### Example

> A person walks up an escalator. Going with the escalator, he takes 20 steps. Going against, he takes 60 steps. Find the total visible steps.

$$N = \frac{20 + 60}{2} = 40 \text{ steps}$$

---

## 14. Zig-Zag / Return Journey Problems

### Concept

A person starts from A toward B, but changes direction at some point and returns, then goes again, and so on.

### The Dog-Between-Two-Trains Problem

> Two trains start toward each other from stations 100 km apart. Train A at 40 km/hr, Train B at 60 km/hr. A dog starts from Train A and runs back and forth between the two trains at 80 km/hr until the trains meet. What total distance does the dog cover?

**The Elegant Solution:**

Forget the zig-zag. The dog runs for the **same total time** as it takes for the trains to meet.

$$\text{Time for trains to meet} = \frac{100}{40 + 60} = 1 \text{ hr}$$

$$\text{Distance by dog} = 80 \times 1 = 80 \text{ km}$$

**Why this works:** The dog's total running time equals the time until the trains meet, regardless of how many times it turns. Speed × time = distance. Done.

**Trap:** Attempting to compute each leg of the dog's journey is an infinite geometric series. While mathematically valid, it's a waste of time in an exam. The elegant approach above takes 10 seconds.

### Return Journey with Changed Speed

> A person walks from A to B at 5 km/hr and immediately returns at 3 km/hr. If AB = 15 km, find total time and average speed.

- Time A→B: $\frac{15}{5} = 3$ hr
- Time B→A: $\frac{15}{3} = 5$ hr
- Total time: $8$ hr
- Total distance: $30$ km
- Average speed: $\frac{30}{8} = 3.75$ km/hr

Note: Average speed ($3.75$) < Arithmetic mean of speeds ($4$). This is always true for equal-distance scenarios.

---

## 15. Practice Problem Vault

### Problem 1 — NAT Type

> A man covers a distance of 24 km in 4.5 hours, partly on foot at 4 km/hr and partly on bicycle at 8 km/hr. Find the distance covered on foot.

**Solution:**

Let distance on foot = $x$ km. Then distance on bicycle = $(24 - x)$ km.

$$\frac{x}{4} + \frac{24 - x}{8} = 4.5$$

$$\frac{2x + 24 - x}{8} = 4.5$$

$$x + 24 = 36$$

$$x = 12 \text{ km}$$

**Answer:** $12$ km

---

### Problem 2 — MCQ Type

> Two trains of lengths 120 m and 80 m run in opposite directions at 42 km/hr and 30 km/hr. How long do they take to cross each other?

(a) 8 s &emsp; (b) 10 s &emsp; (c) 12 s &emsp; (d) 14 s

**Solution:**

Total distance = $120 + 80 = 200$ m

Relative speed = $42 + 30 = 72$ km/hr $= 72 \times \frac{5}{18} = 20$ m/s

Time = $\frac{200}{20} = 10$ s

**Answer: (b) 10 s**

---

### Problem 3 — MSQ Type (Multiple Select)

> Which of the following are true for a boat traveling upstream and downstream over the same distance?

(A) Average speed = Harmonic mean of upstream and downstream speeds  
(B) Average speed = Arithmetic mean of upstream and downstream speeds  
(C) Time taken upstream > Time taken downstream  
(D) Average speed < Arithmetic mean of the two speeds  

**Solution:**

- (A) ✅ For equal distances, average speed = harmonic mean.
- (B) ❌ Arithmetic mean applies only when times are equal, not distances.
- (C) ✅ Upstream speed is less, so more time is needed for the same distance.
- (D) ✅ Harmonic mean ≤ Arithmetic mean (AM-HM inequality), equality only when speeds are equal.

**Answer: (A), (C), (D)**

---

### Problem 4 — GATE/ESE Style

> A train traveling at 72 km/hr crosses a platform in 30 seconds and a man standing on the platform in 18 seconds. Find the length of the platform.

**Solution:**

Speed = $72 \times \frac{5}{18} = 20$ m/s.

Crossing the man: $L_{train} = 20 \times 18 = 360$ m.

Crossing the platform: $L_{train} + L_{platform} = 20 \times 30 = 600$ m.

$L_{platform} = 600 - 360 = 240$ m.

**Answer:** $240$ m

---

### Problem 5 — Circular Track

> Three people A, B, C start from the same point on a circular track of 240 m. Speeds: A = 6 m/s, B = 4 m/s, C = 3 m/s. All move in the same direction. After how many seconds will all three meet at the starting point for the first time?

**Solution:**

Lap times:
- A: $\frac{240}{6} = 40$ s
- B: $\frac{240}{4} = 60$ s
- C: $\frac{240}{3} = 80$ s

LCM(40, 60, 80) = ?

$40 = 2^3 \times 5$  
$60 = 2^2 \times 3 \times 5$  
$80 = 2^4 \times 5$

LCM = $2^4 \times 3 \times 5 = 240$ s

**Answer:** $240$ seconds

---

### Problem 6 — Clock Angle

> At what time between 4 and 5 o'clock are the hands of the clock at right angles?

**Solution:**

At 4:00, the hour hand is at $120°$, minute hand at $0°$. Angle = $120°$.

The minute hand gains at $5.5°$/min. We need the angle to be $90°$.

**Case 1:** Angle reduces from 120° to 90° → Minute hand gains $30°$.

$$t = \frac{30}{5.5} = \frac{60}{11} = 5\frac{5}{11} \text{ min}$$

Time: $4:05\frac{5}{11}$

**Case 2:** Angle goes past 0°, increases to 90° → Minute hand gains $120° + 90° = 210°$.

$$t = \frac{210}{5.5} = \frac{420}{11} = 38\frac{2}{11} \text{ min}$$

Time: $4:38\frac{2}{11}$

**Answer:** At $4:05\frac{5}{11}$ and $4:38\frac{2}{11}$

---

### Problem 7 — Escalator

> Ravi walks up an ascending escalator and takes 30 steps. He then walks down the same escalator (which is still going up) and takes 90 steps. Find the number of visible steps on the escalator.

$$N = \frac{30 + 90}{2} = 60 \text{ steps}$$

**Answer:** $60$ steps

---

### Problem 8 — Late/Early Formula

> Walking at 5 km/hr, a student reaches school 6 min late. Walking at 6 km/hr, he reaches 6 min early. Find the distance to school.

$$D = \frac{5 \times 6 \times (6 + 6)}{(6 - 5) \times 60} = \frac{5 \times 6 \times 12}{60} = \frac{360}{60} = 6 \text{ km}$$

(Note: Divided by 60 to convert minutes to hours for consistent units.)

**Answer:** $6$ km

---

### Problem 9 — Relative Speed Chase

> A is 30 km ahead of B. A travels at 20 km/hr and B at 25 km/hr in the same direction. After how many hours will B catch up with A?

$$T = \frac{30}{25 - 20} = \frac{30}{5} = 6 \text{ hours}$$

**Answer:** $6$ hours

---

### Problem 10 — Average Speed with Three Segments

> A car travels from P to Q at 20 km/hr, Q to R at 30 km/hr, and R to S at 60 km/hr. If PQ = QR = RS, find the average speed for the entire journey.

$$S_{avg} = \frac{3}{\frac{1}{20} + \frac{1}{30} + \frac{1}{60}} = \frac{3}{\frac{3 + 2 + 1}{60}} = \frac{3}{\frac{6}{60}} = \frac{3 \times 60}{6} = 30 \text{ km/hr}$$

**Answer:** $30$ km/hr

---

## 16. Permanent Recall

### Mnemonic 1 — "The DST Triangle"

Visualize a **traffic signal** in the shape of a triangle:
- **D**anger at the top (Distance)
- **S**low down on the left (Speed)
- **T**ake time on the right (Time)

Cover what you need → the remaining two give you the formula.

### Mnemonic 2 — "HARM for Harmonic Mean"

> **H**alf distance + **A**nd + **R**eturn at different speed = use har**M**onic mean.

Whenever the problem says "goes at speed $a$, returns at speed $b$" → **Harmonic Mean**: $\frac{2ab}{a+b}$

### Mnemonic 3 — "ROPES for Relative Speed"

- **R**unning **O**pposite → **P**lus (add speeds)
- **E**veryone **S**ame direction → Subtract (difference of speeds)

### Mnemonic 4 — "Train Length Chant"

> *"Pole me khud, bridge me jod"*  
> (At a pole, use self-length; at a bridge, add both)

### Mnemonic 5 — "Still Water = Average, Current = Half-Diff"

$$B = \frac{D+U}{2}, \quad S = \frac{D-U}{2}$$

"**Add for Boat, Diff for Stream, Divide by 2 in every dream.**"

### The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| Average speed sanity | Must lie **between** the two given speeds, closer to the slower one |
| Unit check | If speed is km/hr and distance is in meters, you **must** convert |
| Negative time | If your answer gives negative time, the scenario is physically impossible |
| Train crossing | Distance covered ≥ length of the train (never less) |
| Upstream speed | Must be positive; if $B < S$, the boat can't go upstream |
| Circular track meeting | Same direction meeting time > Opposite direction meeting time (always) |

---

## Quick Formula Reference Sheet

| Scenario | Formula |
|----------|---------|
| Basic | $D = S \times T$ |
| km/hr → m/s | $\times \frac{5}{18}$ |
| m/s → km/hr | $\times \frac{18}{5}$ |
| Avg speed (equal distance) | $\frac{2S_1 S_2}{S_1 + S_2}$ |
| Avg speed (equal time) | $\frac{S_1 + S_2}{2}$ |
| Relative speed (same dir) | $\|S_1 - S_2\|$ |
| Relative speed (opp dir) | $S_1 + S_2$ |
| Train crosses pole | $T = \frac{L}{S}$ |
| Train crosses platform | $T = \frac{L_{train} + L_{platform}}{S}$ |
| Two trains crossing | $T = \frac{L_1 + L_2}{S_{rel}}$ |
| Boat in still water | $B = \frac{D + U}{2}$ |
| Stream speed | $S = \frac{D - U}{2}$ |
| Round trip in stream | $T = \frac{2dB}{B^2 - S^2}$ |
| Circular track (opp) | $T = \frac{L}{S_1 + S_2}$ |
| Circular track (same) | $T = \frac{L}{S_1 - S_2}$ |
| Clock angle | $\theta = \|30h - \frac{11m}{2}\|$ |
| Clock overlaps per 12 hr | 11 times |
| Late/Early distance | $D = \frac{S_1 S_2 (t_1 + t_2)}{S_2 - S_1}$ |
| Escalator steps | $N = \frac{a + b}{2}$ |
| $n^{th}$ meeting (linear) | Combined distance = $(2n-1)D$ |
| Meeting at start (circular) | LCM of individual lap times |

---

## Summary of Exam Traps & How to Avoid Them

| Trap | Wrong Approach | Correct Approach |
|------|---------------|-----------------|
| Average speed | $(S_1 + S_2)/2$ | $2S_1S_2/(S_1+S_2)$ for equal distances |
| Unit mismatch | Mixing km/hr with meters | Always convert to consistent units first |
| Race "A beats B by x, B beats C by y" | A beats C by $x+y$ | Use speed ratios and multiply |
| Dog between trains | Sum infinite geometric series | Total time × dog's speed |
| Boat with $B = S$ | Attempt round trip | Impossible — upstream speed is zero |
| Clock coincidence in 12 hr | 12 times | 11 times |
| Train passing a walking person | Ignore person's speed | Use relative speed |
| "Head start" in chase | Forget the initial gap | Gap / relative speed = catch-up time |

---

*Study material prepared for GATE, ESE, PSU & Bank competitive examinations. Covers all standard and advanced problem types tested in these exams.*
