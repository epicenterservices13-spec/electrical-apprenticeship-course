# 01-THEORY: Voltage, Current, Resistance, and Ohm's Law

| Field | Value |
| --- | --- |
| Topic | Electrical Theory |
| Level | First-year apprentice |
| Estimated time | 3 hours (2 h classroom, 1 h supervised bench) |
| Prerequisites | Basic algebra; workshop safety orientation |
| Jurisdiction | United States |
| Applicable code or standard | NFPA 70 (NEC) 2023; NFPA 70E 2024 (safety context only) |
| Author | TBD |
| Technical reviewer | TBD |
| Last reviewed | — |
| Status | Draft |

## Learning objectives

By the end of this lesson, the learner will be able to:

1. **Define** voltage, current, resistance, and power, and state their units and symbols.
2. **Calculate** any one of voltage, current, or resistance given the other two using Ohm's law.
3. **Calculate** power using P = E × I and its derived forms.
4. **Demonstrate** measuring resistance on a de-energized circuit with a digital multimeter (DMM).

## Safety and preparation

- **Activity setting:** Classroom, then supervised bench using a low-voltage DC trainer (≤ 12 V) and loose resistors.
- **Hazards:** Burns from overheated resistors; meter damage from wrong function selection; habits that become dangerous at line voltage.
- **Required controls:** Resistance measurements only on de-energized, isolated components. Trainer power off when changing connections.
- **Protective equipment:** Safety glasses.
- **Supervision:** Instructor approves each circuit before power is applied.
- **Stop conditions:** Smell of burning, hot components, meter display "OL" when unexpected, or any uncertainty.

This lesson does not authorize work on circuits above 12 V DC or any energized premises wiring.

## Tools and materials

| Item | Quantity | Specification or purpose |
| --- | --- | --- |
| Digital multimeter | 1 per learner | CAT III 600 V min. rated, with leads |
| DC trainer or bench supply | 1 per pair | 0–12 V, current-limited |
| Resistors | Assorted | 100 Ω, 470 Ω, 1 kΩ, 10 kΩ; ¼ W or ½ W |
| Calculator | 1 per learner | Basic scientific |

## Key terms

| Term | Definition | Units, if applicable |
| --- | --- | --- |
| Voltage (E or V) | Electrical pressure / potential difference that pushes charge | volt (V) |
| Current (I) | Rate of flow of electric charge | ampere (A) |
| Resistance (R) | Opposition to current flow | ohm (Ω) |
| Power (P) | Rate at which electrical energy is converted to work or heat | watt (W) |
| Conductor | Material with low resistance (copper, aluminum) | — |
| Insulator | Material with very high resistance (PVC, rubber, glass) | — |
| Open circuit | Break in the path; no current flows | — |
| Short circuit | Unintended low-resistance path; very high current | — |

## Lesson explanation

### What voltage, current, and resistance are

A useful (but imperfect) model is water in a pipe:

- **Voltage** is the pressure difference between two points. No difference, no flow. A voltage always exists *between two points* — you never measure it on one wire alone.
- **Current** is how much charge flows past a point each second. One ampere is about 6.24 × 10¹⁸ electrons per second.
- **Resistance** is how hard the path is to push through. Longer, thinner, or hotter conductors have more resistance.

On the job you will see these everywhere: a 120 V receptacle (voltage), a 20 A breaker (current limit), and the resistance of a motor winding or a long feeder that causes voltage drop.

### Ohm's law

In a resistive circuit, current is directly proportional to voltage and inversely proportional to resistance:

```
E = I × R        I = E ÷ R        R = E ÷ I
```

Double the voltage → double the current. Double the resistance → half the current.

**Limitation:** Ohm's law describes resistive loads well. Motors, transformers, and electronic loads behave differently under AC; those are covered in later THEORY and MOTOR modules.

### Power

Power is how fast energy is used:

```
P = E × I        P = I² × R        P = E² ÷ R
```

`P = I²R` explains why loose connections get hot: a small extra resistance at a terminal carrying high current produces significant heat.

### Diagram

```
   +  ┌──────[ R ]──────┐
 E ( )                  │      I flows from + through R and back to −
   −  └─────────────────┘
```

The circle is the source (E), the box is the load (R). Current is the same everywhere in this single loop.

## Worked example

**Problem:** A 120 V heater element draws 12.5 A. Find its resistance and power.

**Given:** E = 120 V, I = 12.5 A
**Find:** R (Ω), P (W)
**Assumptions:** Purely resistive load; nominal voltage.

1. R = E ÷ I = 120 V ÷ 12.5 A = **9.6 Ω**
2. P = E × I = 120 V × 12.5 A = **1,500 W**
3. Check with another formula: P = I²R = 12.5² × 9.6 = 156.25 × 9.6 = 1,500 W ✓
4. Reasonable — a 1,500 W heater is a common space heater rating.

**Reference:** Instructional example; not a code requirement.

## Guided practice

**Task:** Measure four resistors with a DMM and compare to their color-code value.

**Preparation:** Instructor confirms trainer is OFF and resistors are loose (not in circuit).

1. Set DMM to Ω. Touch leads together; note lead resistance (should be < 0.5 Ω).
2. Measure each resistor without touching both leads with your fingers (body resistance skews readings on high values).
3. Record measured value and calculate % difference from the marked value.

**Record:** Marked value, measured value, % difference.

**Completion criteria:** All four within the resistor's tolerance band (usually ±5%); correct meter function used throughout.

## Check your understanding

1. What are the units and symbols of voltage, current, resistance, and power?
2. A 24 V circuit has 8 Ω of resistance. What is the current?
3. Why must resistance be measured on a de-energized circuit?

## Common mistakes

| Mistake | Consequence | Prevention or correction |
| --- | --- | --- |
| Measuring resistance on an energized circuit | Wrong reading; blown meter fuse or meter damage | Isolate and verify de-energized first |
| Mixing kΩ and Ω | Answer off by 1,000× | Convert everything to base units before calculating |
| Leaving leads in the A jack, then measuring voltage | Blown meter fuse; at line voltage, a short through the meter and arc-flash risk | Return leads to V/Ω jack after every current reading |
| Using P = E × I on motors without power factor | Overstated power | Covered in later AC modules |

## Review

- E = I × R ties voltage, current, and resistance together.
- P = E × I; heat at bad connections follows P = I²R.
- Measure resistance only on isolated, de-energized parts.

## References

- NFPA 70, *National Electrical Code*, 2023 ed. — Article 100 (Definitions).
- NFPA 70E, *Standard for Electrical Safety in the Workplace*, 2024 ed. — Article 110 (meter use, general).
- Any standard first-year apprenticeship DC theory text.

## Related materials

- Exercises: [exercises.md](exercises.md)
- Assessment: [assessment.md](assessment.md)
- Instructor guidance and answer keys: `instructor-notes.md` (instructor distribution only)
