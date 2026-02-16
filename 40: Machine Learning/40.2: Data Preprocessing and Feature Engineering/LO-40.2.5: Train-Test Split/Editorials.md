
# Question Bank: Train-Test Split

## Q1 (MCQ)
**Problem:** Which of the following variables should NEVER be shown to the model during the `.fit()` (training) process?
A. `X_train`
B. `y_train`
C. `X_test` (and `y_test`)
D. `random_state`

## Q2 (Coding)
**Problem:** Write a Python snippet to split arrays `X` and `y` into training and testing sets. Use 25% for testing and set a random seed of 123.
**Input:** `X`, `y` arrays.
**Output:** Four arrays: `X_train`, `X_test`, `y_train`, `y_test`.

## Q3 (NAT)
**Problem:** You have a dataset with 500 rows. You perform a Train-Test split with `test_size=0.2`. How many rows will be in the `X_train` variable?

## Q4 (MSQ)
**Problem:** Which of the following statements about **Data Leakage** regarding Train-Test splits are true?
A. It occurs if you perform Feature Scaling (e.g., calculating Mean) on the *entire* dataset before splitting.
B. It occurs if you include the Test data in the `.fit()` command.
C. It results in a model that performs poorly on training data but well on test data.
D. It results in over-optimistic test scores that do not reflect reality.

## Q5 (Coding)
**Problem:** Implement a "Time-Based Split".
Given a DataFrame `df` with a 'Date' column, sort it by date, and split it such that the first 80% of rows are Train and the last 20% are Test. (Do not use `sklearn` randomness).

## Q6 (Subjective)
**Problem:** Explain why `random_state` is important for **Reproducibility**. If two engineers are working on the same model but use different (or no) random states, what problems might arise when they compare their results?

```

---

### File 7: Editorials.md

```markdown
# Editorials

## Q1
### Title
Data Leakage Prevention

### Problem Description
Identify the data to hide during training.

### Objective
Reinforce the golden rule of ML.

### Hint
If you study the exam questions (`Test`), you are cheating.

### Short Explanation
The Test set (`X_test`, `y_test`) simulates the future. The model must not see it during training.

### Detailed Explanation
* **Training:** Uses `X_train`, `y_train`.
* **Testing:** Uses `X_test` to predict, then compares with `y_test`.
* Showing `X_test` during training is Data Leakage.

---

## Q2
### Title
Sklearn Implementation

### Problem Description
Standard `train_test_split` syntax.

### Objective
Basic coding skill.

### Hint
Import `train_test_split` from `sklearn.model_selection`.

### Short Explanation
Pass `test_size=0.25` and `random_state=123`.

### Detailed Explanation
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=123
)

```

---

## Q3

### Title

Split Calculation

### Problem Description

Calculate row count for 80/20 split on 500 rows.

### Objective

Basic arithmetic of splitting.

### Hint

.

### Short Explanation

Train size is 80%. .

### Detailed Explanation

1. **Test Size:** 20% of 500 = 100 rows.
2. **Train Size:** Remaining 400 rows.

---

## Q4

### Title

Data Leakage Mechanics

### Problem Description

Select scenarios causing leakage.

### Objective

Understand subtle forms of cheating.

### Hint

Any information from Test leaking into Train is bad.

### Short Explanation

A, B, and D are true. C is false (Leakage usually makes Test performance look artificially *good*).

### Detailed Explanation

* **A (True):** If you calculate the Mean of the whole dataset, your Training data "knows" something about the Test data distribution.
* **B (True):** Direct leakage.
* **C (False):** Leakage usually causes high Test accuracy *offline*, but failure in *production*.
* **D (True):** It gives a false sense of confidence.

---

## Q5

### Title

Time-Series Splitting

### Problem Description

Split data chronologically (no shuffling).

### Objective

Handle temporal data where future cannot predict past.

### Hint

Sort by date, calculate index for 80%, slice using `iloc`.

### Short Explanation

Sort, find split index, slice.

### Detailed Explanation

```python
def time_split(df):
    df = df.sort_values('Date')
    split_idx = int(len(df) * 0.8)
    
    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]
    return train, test

```

*Note:* `train_test_split` shuffles by default, which is bad for time series (predicting yesterday using tomorrow's data).

---

## Q6

### Title

Reproducibility

### Problem Description

Why use `random_state`?

### Objective

Best practices for collaboration.

### Hint

If I get a lucky easy split and you get an unlucky hard split, can we compare models?

### Short Explanation

Without a fixed seed, the data is shuffled differently every time. Engineer A might get an "easy" test set and score 90%. Engineer B might get a "hard" test set and score 80%. They won't know if the model changed or just the data. `random_state` guarantees they use the exact same split.

### Detailed Explanation

* **Debugging:** If your code crashes on a specific row, you need to be able to recreate that split to fix it.
* **Benchmarking:** To prove Model A > Model B, the test data must be identical.

```

```
