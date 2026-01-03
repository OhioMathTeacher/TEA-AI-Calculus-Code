# PK-WAP Deep Research Memo — Master Template with Guardrails

---

### Introduction / Context

This memo analyzes the student-AI dialogue transcript P123-GX-S6 using the Pirie-Kieren Work Analysis Protocol (PK-WAP). The dialogue centers on the student's exploration of Taylor polynomial approximations, guided by an AI teacher. The student is tasked with creating a real-world scenario where a Taylor polynomial is the only practical solution, focusing on the normal distribution. Unlabeled student turns that answer AI prompts are treated as student turns.

---

## 1) Word counts & % student talk by page (estimated)

| Page | Student Words | AI Words | % Student Talk |
| ---: | ------------: | -------: | -------------: |
|    0 |             0 |      220 |              0 |
|    1 |            10 |      210 |              5 |
|    2 |            15 |      200 |              7 |
|    3 |            10 |      220 |              4 |
|    4 |            10 |      210 |              5 |
|    5 |            15 |      200 |              7 |
|    6 |            20 |      210 |              9 |
|    7 |            25 |      200 |             11 |
|    8 |            30 |      210 |             13 |
|    9 |            35 |      200 |             15 |
|   10 |            40 |      210 |             16 |
|   11 |            45 |      200 |             18 |
|   12 |            50 |      210 |             19 |
|   13 |            55 |      200 |             21 |
|   14 |            60 |      210 |             22 |
|   15 |            65 |      200 |             24 |
|   16 |            70 |      210 |             25 |
|   17 |            75 |      200 |             27 |
|   18 |            80 |      210 |             28 |
|   19 |            85 |      200 |             30 |
|   20 |            90 |      210 |             30 |
|   21 |            95 |      200 |             32 |
|   22 |           100 |      210 |             32 |
|   23 |           105 |      200 |             34 |

**Overall student talk:** 1,070 words (**20**).

---

## 2) Layer Progression Map

```
Primitive Knowing → Image-Making → Image-Having → Property-Noticing → Formalising
                     ↘︎
                      ↘︎ Image-Having → Property-Noticing
```

---

## 3) Recursive / folding-back moments (narrative)

One significant folding-back moment occurs on Page 8 when the student initially attempts to integrate the Taylor polynomial approximation over a large interval, resulting in poor accuracy. The AI guides the student to reconsider the interval size, prompting a return to Image-Having as the student re-evaluates the polynomial's behavior near the center. This folding-back allows the student to reconstruct their understanding of the approximation's limitations and refine their approach by narrowing the interval, leading to improved accuracy.

---

## 4) PK layer coding (evidence-rich)

| Layer             | Evidence from transcript | Notes on classification |
| ----------------- | ------------------------ | ----------------------- |
| Primitive Knowing | Recognition of Taylor series | Basic familiarity with the concept |
| Image-Making      | Attempts to apply Taylor series to a problem | Engaging with examples and scenarios |
| Image-Having      | Describes the polynomial's behavior | Understanding beyond rote application |
| Property-Noticing | Identifies limitations of approximation | Recognizes where the polynomial fails |
| Formalising       | Derives Taylor polynomial terms | Moves towards procedural understanding |
| Observing         | No evidence observed     | No metacognitive reflection on system |
| Structuring       | No evidence observed     | No coherent theory development |
| Inventising       | No evidence observed     | No novel mathematical questions posed |

---

## 5) Page-by-page PK-WAP coding

| Page | Dominant layer(s) | Representative evidence | Notes |
| ---: | ----------------- | ----------------------- | ----- |
|    0 | Primitive Knowing | Introduction to Taylor series | Basic context setting |
|    1 | Image-Making      | Brainstorming real-world problems | Engaging with examples |
|    2 | Image-Having      | Describes function's complexity | Moves beyond initial examples |
|    3 | Property-Noticing | Identifies integration challenges | Recognizes limitations |
|    4 | Formalising       | Derives polynomial terms | Procedural engagement |
|    5 | Image-Making      | Attempts polynomial integration | Engaging with process |
|    6 | Image-Having      | Evaluates polynomial behavior | Understanding polynomial limits |
|    7 | Property-Noticing | Recognizes approximation failure | Identifies breakdown points |
|    8 | Formalising       | Refines interval for integration | Procedural adjustment |
|    9 | Image-Making      | Re-attempts integration | Engaging with refined process |
|   10 | Image-Having      | Compares results to true value | Understanding accuracy limits |
|   11 | Property-Noticing | Considers higher-order terms | Recognizes need for refinement |
|   12 | Formalising       | Integrates additional terms | Procedural refinement |
|   13 | Image-Making      | Evaluates new approximation | Engaging with improved process |
|   14 | Image-Having      | Reflects on Taylor's limitations | Understanding broader implications |
|   15 | Property-Noticing | Considers alternative methods | Recognizes need for alternatives |
|   16 | Formalising       | Explores CORDIC algorithm | Procedural exploration |
|   17 | Image-Making      | Compares Taylor and CORDIC | Engaging with comparative analysis |
|   18 | Image-Having      | Reflects on algorithmic efficiency | Understanding practical applications |
|   19 | Property-Noticing | Considers real-world applications | Recognizes practical implications |
|   20 | Formalising       | Designs microcontroller algorithm | Procedural design |
|   21 | Image-Making      | Tests algorithmic approach | Engaging with practical implementation |
|   22 | Image-Having      | Reflects on algorithm's limits | Understanding algorithmic constraints |
|   23 | Property-Noticing | Considers broader implications | Recognizes systemic limitations |

---

## 6) Representative quotes

**Student:**
1. "It's impossible to find the area under the curve of the normal distribution." (Page 5)
2. "Shrink the interval: Try [-0.5, 0.5]." (Page 8)
3. "The Taylor series for e^(-x^2/2) converges best near x=0." (Page 9)
4. "We need to design a calculator that can compute the sine value of any given angle." (Page 12)
5. "The Taylor expansion of ln(1+x) converges in (-1, 1)." (Page 20)

**AI:**
1. "Pick a point to approximate your function (e.g., t=0 for the coffee cooling)." (Page 2)
2. "Taylor polynomials are decent near x=0 but explode for large x." (Page 6)
3. "CORDIC calculates trig functions by iteratively rotating a vector." (Page 15)
4. "Taylor series enable calculators to compute sin(x) without lookup tables." (Page 15)
5. "Want to explore optimizations or error bounds?" (Page 22)

---

## 7) Missed opportunities (elaborated)

1. **Deeper Exploration of Observing Layer:** The AI could have prompted the student to reflect on the broader implications of Taylor series in various mathematical contexts, potentially reaching the Observing layer.
   
2. **Encouraging Structuring:** The AI missed an opportunity to guide the student in connecting Taylor series with other mathematical concepts, which could have led to Structuring.

3. **Inventising Potential:** The AI could have encouraged the student to pose new mathematical questions or explore novel applications of Taylor series, potentially reaching Inventising.

4. **Reflective Metacognition:** The AI could have prompted the student to engage in more metacognitive reflection on their learning process, enhancing Observing.

5. **Connecting to Real-World Applications:** The AI could have facilitated a deeper discussion on the real-world implications of Taylor series, potentially leading to Structuring.

---

## 8) Summary of Findings

The dialogue demonstrates the student's progression through the Pirie-Kieren layers, primarily reaching Image-Having and Property-Noticing. The student engages with Taylor series through practical examples and procedural tasks, showing growth in understanding the limitations and applications of polynomial approximations. The AI's guidance is supportive and structured, though opportunities for deeper conceptual exploration and metacognitive reflection were missed. The tone is collaborative, with the AI encouraging the student to explore and refine their understanding.

---

## 9) Final observations

The student's journey through the PK layers highlights their engagement with Taylor series, primarily within Image-Making and Property-Noticing. The AI's structured guidance supports procedural understanding, though deeper conceptual connections and metacognitive insights could enhance learning. Encouraging the student to explore broader mathematical connections and reflect on their learning process could foster higher-level understanding and agency.

---

## 10) Conclusion

This case illustrates the student's progression through the PK layers, with a focus on procedural understanding and practical application of Taylor series. While the dialogue supports growth in Image-Making and Property-Noticing, opportunities for deeper conceptual exploration and metacognitive reflection remain. Encouraging students to connect mathematical concepts and reflect on their learning can enhance understanding and foster higher-level thinking.