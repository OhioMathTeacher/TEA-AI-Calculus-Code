# PK-WAP Deep Research Memo — Master Template with Guardrails

---

### Introduction / Context

This analysis pertains to the case ID P22-GX-S6, focusing on a student–AI dialogue centered around the application of Taylor polynomials in real-world scenarios. The student is guided through a structured process to identify a suitable problem for Taylor approximation, construct the polynomial, and perform integration to approximate an area under a curve. Unlabeled student turns that answer AI prompts are treated as student turns.

---

## 1) Word counts & % student talk by page (estimated)

| Page | Student Words | AI Words | % Student Talk |
| ---: | ------------: | -------: | -------------: |
|    0 |             0 |       47 |              0 |
|    1 |             6 |       20 |             23 |
|    2 |             6 |       20 |             23 |
|    3 |            11 |       48 |             19 |
|    4 |            15 |       82 |             15 |
|    5 |            16 |       94 |             15 |
|    6 |            13 |       82 |             14 |
|    7 |            19 |       95 |             17 |
|    8 |            13 |       78 |             14 |
|    9 |             0 |       47 |              0 |
|   10 |            12 |       82 |             13 |
|   11 |             9 |       47 |             16 |
|   12 |             0 |       47 |              0 |
|   13 |            21 |       82 |             20 |
|   14 |            19 |       95 |             17 |
|   15 |             0 |       47 |              0 |
|   16 |            24 |       82 |             23 |
|   17 |            25 |       95 |             21 |
|   18 |             0 |       47 |              0 |
|   19 |             0 |       47 |              0 |

**Overall student talk:** 209 words (**15**).

---

## 2) Layer Progression Map

```
Primitive Knowing → Image-Making → Image-Having → Property-Noticing ↺ Image-Making (p. 5) → Property-Noticing → Formalising ↺ Image-Making (p. 10) → Formalising
```

---

## 3) Recursive / folding-back moments (narrative)

The first significant folding-back occurs on page 5, where the student initially proposes a scenario involving a simple pendulum. The AI corrects this by emphasizing the need for a problem where higher-order terms are essential. This prompts the student to revisit their understanding and propose a new scenario involving relativistic kinetic energy, demonstrating a transition from Image-Making back to Property-Noticing.

A second folding-back is observed on page 10, where the student attempts to construct a Taylor polynomial but makes errors in the factorial denominators. The AI provides corrective feedback, prompting the student to revisit their polynomial construction, moving from Formalising back to Image-Making before successfully reconstructing the polynomial.

---

## 4) PK layer coding (evidence-rich)

| Layer             | Evidence from transcript | Notes on classification |
| ----------------- | ------------------------ | ----------------------- |
| Primitive Knowing | Prefers direct instructions (p. 1) | Basic preferences for learning style |
| Image-Making      | Proposes pendulum scenario (p. 4) | Initial attempts to apply Taylor series concept |
| Image-Having      | Recognizes need for transcendental functions (p. 6) | Understanding of problem requirements |
| Property-Noticing | Identifies non-elementary integral (p. 8) | Notices specific mathematical properties |
| Formalising       | Constructs Taylor polynomial (p. 10) | Engages in formal mathematical procedures |
| Observing         | No evidence observed | No metacognitive reflection on system-level patterns |
| Structuring       | No evidence observed | No coherent theory-building across mathematical ideas |
| Inventising       | No evidence observed | No novel mathematical questions or extensions |

---

## 5) Page-by-page PK-WAP coding

| Page | Dominant layer(s) | Representative evidence | Notes |
| ---: | ----------------- | ----------------------- | ----- |
|    0 | Primitive Knowing | Prefers direct instructions | Establishes learning preferences |
|    1 | Primitive Knowing | Prefers no-nonsense fixes | Reinforces learning style |
|    2 | Primitive Knowing | Prefers no-nonsense fixes | Consistency in learning preference |
|    3 | Image-Making      | Proposes pendulum scenario | Initial problem formulation |
|    4 | Image-Making      | Proposes pendulum scenario | Attempts to apply Taylor series |
|    5 | Property-Noticing | Recognizes need for transcendental functions | Refines problem understanding |
|    6 | Property-Noticing | Identifies non-elementary integral | Notices mathematical properties |
|    7 | Image-Making      | Proposes relativistic scenario | Attempts new problem formulation |
|    8 | Property-Noticing | Identifies non-elementary integral | Correct problem identification |
|    9 | Formalising       | Constructs Taylor polynomial | Engages in formal procedures |
|   10 | Image-Making      | Corrects polynomial construction | Revisits polynomial formulation |
|   11 | Formalising       | Corrects polynomial construction | Achieves correct formulation |
|   12 | Formalising       | Integrates polynomial | Engages in integration |
|   13 | Formalising       | Integrates polynomial | Completes integration |
|   14 | Formalising       | Integrates polynomial | Completes integration |
|   15 | Formalising       | Integrates polynomial | Completes integration |
|   16 | Formalising       | Discusses accuracy | Reflects on approximation |
|   17 | Formalising       | Discusses accuracy | Reflects on approximation |
|   18 | Formalising       | Discusses accuracy | Reflects on approximation |
|   19 | Formalising       | Discusses accuracy | Reflects on approximation |

---

## 6) Representative quotes

**Student:**
1. "I prefer direct, bullet-pointed instructions." (p. 1) - Establishes learning preference.
2. "For the first step, I want to find the trace of a simple pendulum which moves in a small angle." (p. 4) - Initial problem proposal.
3. "How about finding the kinetic energy of an object that moves with speed near to the speed of light?" (p. 6) - Attempts new problem formulation.
4. "How about calculate the area of a ground whose boundary is surrounded by e^(-x^2) and y=0 0<=x<=1?" (p. 8) - Correct problem identification.
5. "Integral1=x+c, integral2=-x^3/3+c, integral3=x^5/10+c." (p. 14) - Attempts integration.
6. "For final reflection, I find that Taylor series can help us approximate some integral that we cannot easily find." (p. 17) - Reflects on learning.

**AI:**
1. "Got it— clear and structured." (p. 1) - Acknowledges student preference.
2. "Your example is too narrow. A simple pendulum’s motion (small angle) is already well-approximated by a linear ODE." (p. 5) - Provides corrective feedback.
3. "Close, but kinetic energy in special relativity uses the exact function." (p. 6) - Corrects student’s problem formulation.
4. "Yes— this works. The integral \(\int_{0}^{1} e^{-x^2} \,dx\) has no elementary closed-form solution." (p. 8) - Approves correct problem.
5. "Almost. Your coefficients are correct, but your factorial denominators are wrong." (p. 10) - Corrects polynomial construction.
6. "The true value of \(\int_{0}^{1} e^{-x^2} \,dx\) = 0.7468 (via numerical methods)." (p. 15) - Provides exact value for comparison.

---

## 7) Missed opportunities (elaborated)

1. **Deeper Conceptual Discussion:** The AI could have prompted the student to explore why transcendental functions are significant in mathematical modeling, deepening understanding of their real-world applications.
2. **Encouraging Observing:** The AI missed an opportunity to encourage the student to reflect on the broader implications of Taylor series beyond the immediate task, potentially fostering Observing.
3. **Connecting to Prior Knowledge:** The AI could have asked the student to relate Taylor series to previously learned mathematical concepts, reinforcing connections and aiding Structuring.
4. **Exploring Alternative Methods:** The AI could have encouraged the student to consider alternative approximation methods, such as Fourier series, to broaden their mathematical toolkit.
5. **Metacognitive Reflection:** The AI could have prompted the student to reflect on their problem-solving process, enhancing metacognitive skills and potentially leading to Observing.

---

## 8) Summary of Findings

The student engaged actively with the AI, demonstrating movement through several PK layers, primarily within Image-Making, Property-Noticing, and Formalising. The dialogue was characterized by a structured, no-nonsense tone, aligning with the student's preference for direct instruction. Key growth moments included the student's successful identification of a suitable problem for Taylor approximation and the correction of polynomial construction errors. Despite these achievements, opportunities for deeper conceptual understanding and metacognitive reflection were missed.

---

## 9) Final observations

The dialogue showcased the student's ability to navigate through Image-Making and Property-Noticing, with successful transitions to Formalising. The AI's direct and corrective approach facilitated this progression, though it could have further supported the student's development by encouraging reflection and connections to broader mathematical concepts. Enhancing these aspects could lead to richer learning experiences and potential movement into Observing.

---

## 10) Conclusion

This case highlights the importance of aligning instructional approaches with student preferences while also recognizing the value of fostering deeper conceptual understanding and metacognitive skills. The student's PK trajectory primarily involved Image-Making, Property-Noticing, and Formalising, with potential for growth into Observing. Encouraging reflection and connections to prior knowledge could enhance learning outcomes and support the development of a more comprehensive mathematical understanding.