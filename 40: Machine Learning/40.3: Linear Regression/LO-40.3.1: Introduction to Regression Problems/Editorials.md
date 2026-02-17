

# Editorials

## Q1
### Title
Identifying Classification vs Regression

### Problem Description
Identify the non-regression task.

### Objective
Distinguish between categorical and continuous outputs.

### Hint
Which one predicts a category/name instead of a number?

### Short Explanation
Predicting the **color** (Red, Blue, Yellow) is predicting a category. This is Classification. Time, Lifetime, and Revenue are all continuous quantities (Regression).

### Detailed Explanation
* **A (Time):** Continuous number (e.g., 30.5 mins). Regression.
* **B (Color):** Discrete category (Label). Classification.
* **C (Lifetime):** Continuous number. Regression.
* **D (Revenue):** Continuous currency. Regression.

---

## Q2
### Title
Heuristic for Regression Check

### Problem Description
Check if a target vector looks like regression data.

### Objective
Programmatic type checking.

### Hint
Check types or count unique values.

### Short Explanation
If data is float, it's likely regression. If it's integer with many unique values, it's likely regression (count). If few unique values, likely classification.

### Detailed Explanation
```python
def is_regression(target_list):
    # Check if floats
    if any(isinstance(x, float) for x in target_list):
        return True
    # Check cardinality (heuristic)
    if len(set(target_list)) > 10:
        return True
    return False

```

---

## Q3

### Title

Simple Linear Calculation

### Problem Description

Predict  using  for .

### Objective

Basic function evaluation.

### Hint

Substitute x.

### Short Explanation

.

### Detailed Explanation

---

## Q4

### Title

Regression Properties

### Problem Description

Select true statements about Regression.

### Objective

Concept verification.

### Hint

Regression = Numbers, Classification = Boundaries.

### Short Explanation

A and C are true. B describes Classification. D describes Classification (Binary).

### Detailed Explanation

* **A (True):** You cannot perform regression on text strings directly; targets must be numbers.
* **B (False):** Decision boundaries are for separating classes.
* **C (True):** Regression minimizes error (e.g., MSE).
* **D (False):** Churn is Yes/No (Binary Classification).

---

## Q5

### Title

Filtering Tasks

### Problem Description

Select regression strings from a list.

### Objective

Apply definitions to text descriptions.

### Hint

Look for continuous quantities.

### Short Explanation

Price and Temperature are numbers. Gender and Spam are categories.

### Detailed Explanation

```python
def filter_regression(problems):
    # This requires logic or a predefined set of keywords
    keywords = ["Price", "Temperature", "Age", "Count"]
    return [p for p in problems if any(k in p for k in keywords)]

```

*(Note: In the context of the question, this logic is conceptual)*.

---

## Q6

### Title

Discretization Trade-off

### Problem Description

Regression vs Binning (Classification).

### Objective

Discuss information loss.

### Hint

"19 years old" vs "Adult".

### Short Explanation

**Loss of Information:** "Age 19" and "Age 35" are very different, but in the "19-35" bucket, the model treats them as identical. You lose the nuance of the specific number.
**Why do it?** Sometimes specific numbers are noisy or irrelevant. If you are selling alcohol, you only care if Age  21. The exact age (45 vs 46) doesn't change the outcome, so classification simplifies the problem.

```

```
