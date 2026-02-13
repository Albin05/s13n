
# Editorials

## Q1
### Title
Choosing the Right Approach

### Problem Description
Diagnosing rare diseases with complex, unexplainable symptom interactions.

### Objective
Identify when ML is superior to Logic.

### Hint
If experts can't write the rules, you can't use Logic.

### Short Explanation
Since the rules are unknown or too complex to write down (implicit knowledge), we must rely on learning patterns from data (Experience/ML).

### Detailed Explanation
* **Logic-based:** Requires explicit rules (`If fever > 101...`). If doctors can't articulate these rules, this approach fails.
* **Experience-based:** The model looks at the history of patients and finds hidden correlations between symptoms and diseases that humans might miss.

---

## Q2
### Title
Logic Implementation

### Problem Description
Implement a grading scale using `if-else`.

### Objective
Demonstrate rigid, rule-based logic.

### Hint
Use `if`, `elif`, `else`.

### Short Explanation
Standard conditional checks.

### Detailed Explanation
```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

```

---

## Q3

### Title

Performance Calculation

### Problem Description

Compare execution time.
Logic: .
Experience: .

### Objective

Compare computational costs of search vs matrix multiplication.

### Hint

Calculate Logic total time and subtract Experience time.

### Short Explanation

Logic = 50ms. Experience = 35ms. Experience is faster by 15ms.

### Detailed Explanation

1. **Logic Time:** 5 rules  10ms/rule = 50ms.
2. **Experience Time:** Flat 35ms.
3. **Difference:** .
*Note:* As complexity grows (more rules), Logic becomes slower, while ML inference time often stays relatively constant (parallelized).

---

## Q4

### Title

Inductive Reasoning Properties

### Problem Description

Select true statements about Inductive Reasoning.

### Objective

Understand the philosophical basis of ML.

### Hint

Induction is "Bottom-Up" (Data to Rule). Deduction is "Top-Down" (Rule to Data).

### Short Explanation

B and C are true. A describes Deduction. D describes Deduction.

### Detailed Explanation

* **A (False):** Induction deals with *probability*, not guarantees. (Just because the sun rose every day doesn't guarantee it will tomorrow).
* **B (True):** It generalizes from data.
* **C (True):** If your data (observations) is biased, your generalization will be wrong.
* **D (False):** Top-down is Deduction. Induction is Bottom-up.

---

## Q5

### Title

Majority Vote Prediction

### Problem Description

Predict the next value based on the most frequent past value.

### Objective

Implement the simplest form of learning: "What usually happens?"

### Hint

Count occurrences of 0 and 1.

### Short Explanation

Use `max(set(data), key=data.count)`.

### Detailed Explanation

```python
def predict_next(history):
    count_1 = history.count(1)
    count_0 = history.count(0)
    return 1 if count_1 > count_0 else 0

```

This is a "Zero-Rule" baseline model.

---

## Q6

### Title

The Dangers of Experience

### Problem Description

Discuss Bias in ML vs Explicit Rules in hiring/loans.

### Objective

Highlight the ethical risks of Black Box models.

### Hint

If a bank never hired women in the past (History), what will an ML model learn to do?

### Short Explanation

Experience-based models learn *patterns from history*. If history contains human bias (racism, sexism), the model will learn and automate that bias.

### Detailed Explanation

* **Bias propagation:** An ML model trained on historical hiring data might learn that "Men get hired more often." It treats this as a valid rule and rejects women, determining that "Men are better candidates" based on experience.
* **Lack of Explainability:** With Logic, we can see `if gender == female: reject` and fix it. With ML, the bias is hidden in millions of numerical weights, making it hard to detect and remove ("Black Box").

```

```
