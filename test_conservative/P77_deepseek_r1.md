# PK-WAP Deep Research Memo — Master Template with Guardrails

### Introduction / Context  
Analysis of transcript P77-G8-S5 using Pirie-Kieren Work Analysis Protocol. The mathematical scenario involves developing a Taylor polynomial approximation for a frisbee's trajectory under variable wind conditions. Unlabeled student responses to AI prompts are treated as student contributions.

---

## 1) Word counts & % student talk by page (estimated)

| Page | Student Words | AI Words | % Student Talk |
| ---: | ------------: | -------: | -------------: |
|   00 |             0 |      350 |              0 |
|   01 |            15 |      280 |              5 |
|   02 |            80 |      230 |             26 |
|   03 |            75 |      240 |             24 |
|   04 |            95 |      220 |             30 |
|   05 |            65 |      190 |             25 |
|   06 |            45 |      320 |             12 |
|   07 |            35 |      260 |             12 |
|   08 |             0 |      120 |              0 |
| **Overall student talk:** 410 words (**18%**). |

---

## 2) Layer Progression Map  
```
Primitive Knowing 
  ↓  
Image-Making (P02-P03: Frisbee physics visualization)  
  ⇄ (Fold-back @P03: Simplifying wind assumptions)  
Image-Having (P03-P04: Mental model of x(t))  
  ↓  
Property-Noticing (P04-P05: Polynomial limitations)  
  ↓  
Formalising (P04: P₂(t) derivation)  
```
*(No evidence of Observing/Structuring/Inventising)*

---

## 3) Recursive / folding-back moments (narrative)  
**P02-P03 (Image-Making → Image-Having):** After initial struggle describing frisbee dynamics (P02), the student folds back to simplify wind effects ("assume wind constant at v_wind0", P03). This reconstructs understanding by reducing complexity to actionable parameters.  
**P05-P06 (Property-Noticing → Image-Making):** When discussing error accumulation (P05), the student folds back to propose piecewise recalibration (P06), rebuilding the approximation strategy through iterative local modeling.

---

## 4) PK layer coding (evidence-rich)

| Layer             | Evidence from transcript | Notes on classification |
| ----------------- | ------------------------ | ----------------------- |
| Primitive Knowing | Calculus terminology (P04: "Taylor series formula") | Recognizes foundational symbols/methods |
| Image-Making      | "Wind changes randomly... can't define wind's effect" (P03) | Builds mental model of chaotic system |
| Image-Having      | "x(t)≈x₀+vₓ₀t" with defined parameters (P04) | Stable conceptualization of simplified motion |
| Property-Noticing | "Errors spike when wind changes" (P05) | Identifies approximation failure conditions |
| Formalising       | Derives P₂(t)=x₀+vₓ₀t+(aₓ/2)t² (P04) | Abstracts to polynomial structure |
| Observing         | *No evidence* | No metacognitive examination of mathematical system |
| Structuring       | *No evidence* | No theoretical synthesis |
| Inventising       | *No evidence* | No novel mathematical extensions |

---

## 5) Page-by-page PK-WAP coding

| Page | Dominant layer(s) | Representative evidence | Notes |
| ---: | ----------------- | ----------------------- | ----- |
| 00 | - | AI setup | No student input |
| 01 | Primitive Knowing | "Maybe you can act like a humorous guy" | Social negotiation |
| 02 | Image-Making | "Wind speed constantly changing... hard to handle" (Student) | Problem conceptualization |
| 03 | Image-Having → Property-Noticing | "Assume wind constant... P₂(t)=x₀+vₓ₀t+(aₓ/2)t²" | Model simplification & formalization |
| 04 | Formalising | Derives Taylor polynomial coefficients | Abstract procedural work |
| 05 | Property-Noticing | "Reliable within 0.5s... errors spike at t=1s" | Identifies validity boundaries |
| 06 | Image-Making | "Break up time... recalibrate every 0.2s" (Student) | Adaptive strategy invention |
| 07 | Property-Noticing | "Errors pile up... data inaccuracies compound" | Limitations analysis |
| 08 | - | AI closure | No student input |

---

## 6) Representative quotes  

**Student (Conceptual Significance)**  
1. P02: *"Wind changes randomly... measuring variables is impossible"* → **Image-Making** (Chaos visualization)  
2. P03: *"x(t) is disgustingly complex"* → **Property-Noticing** (Function complexity)  
3. P04: *"P₂(t)=x₀+vₓ₀t+(aₓ/2)t²"* → **Formalising** (Polynomial construction)  
4. P05: *"Reliable within 0.5s... ignores key factors"* → **Property-Noticing** (Approximation limits)  
5. P06: *"Break up time... recalibrate every 0.2s"* → **Image-Making** (Adaptive strategy)  
6. P07: *"Errors pile up... approximations go off track"* → **Property-Noticing** (Error propagation)  

**AI (Pedagogical Function)**  
1. P02: *"Wind turns frisbee physics into a circus"* → Anchors abstraction in humor  
2. P03: *"Summarized why physicists cry into coffee"* → Validates struggle while motivating  
3. P04: *"Stress-test this approximation before celebrating"* → Promotes critical evaluation  
4. P05: *"Taylor polynomials are like duct tape"* → Metaphor for utility/limitations  
5. P06: *"Reinvented billion-dollar technique"* → Connects to real-world applications  
6. P07: *"Errors compound like gossip"* → Analogical error explanation  

---

## 7) Missed opportunities (elaborated)  
1. **P04:** When student derived P₂(t), AI missed chance to probe *why* second-degree suffices ("Could linear work? What vanishes in higher derivatives?").  
2. **P05:** After noting 0.5s validity window, AI should have prompted error-bound quantification ("How would you calculate maximum error at t=0.5s?").  
3. **P06:** Student's piecewise idea warranted exploration of computational tradeoffs ("What happens if we reduce interval to 0.1s? How does cost scale?").  
4. **P07:** When student identified error compounding, AI could have introduced error analysis techniques (e.g., Lipschitz conditions).  

---

## 8) Summary of Findings  
The student demonstrated consistent PK layer progression from visualizing chaotic dynamics (Image-Making) to formal polynomial derivation (Formalising). Key growth occurred through recursive fold-backs: simplifying wind assumptions (P03) and developing adaptive piecewise approximation (P06). Tone remained engaged and problem-focused, with humor reducing anxiety around complexity. Agency peaked when independently proposing the recalibration strategy (P06), showing ownership of approximation concepts. Dominant layers were Image-Having (model refinement) and Property-Noticing (limitations analysis), with no evidence of outer-layer metacognition or theory-building.

---

## 9) Final observations  
The student exhibited strong agency in reconstructing understanding through simplification (constant wind assumption) and innovation (piecewise method), though within bounded mathematical depth. AI's humorous tone successfully sustained engagement but occasionally overshadowed precision opportunities. PK progression stalled at Formalising due to missed prompts for error quantification and comparative analysis. To deepen learning, AI should prioritize "why" over "what" questions when students formalize procedures.

---

## 10) Conclusion  
This case exemplifies effective mid-level PK growth (Image-Making → Formalising) in applied calculus. The student's trajectory—from recognizing real-world complexity to structured approximation—highlights how recursive fold-backs enable conceptual reconstruction. Pedagogically, it demonstrates the value of humor in sustaining engagement with ill-structured problems, while underscoring the need for strategic prompts to advance toward Observing (e.g., error analysis). Final PK notation: PK[IM→IH→PN→F].