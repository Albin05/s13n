
# Editorials

## Q1
### Title
RMSE Properties

### Problem Description
Identify true statements about RMSE.

### Objective
Understand the physical meaning of the metric.

### Hint
Square root brings the unit back to normal.

### Short Explanation
RMSE takes the square root of MSE, returning the unit to the original scale (e.g., Dollars).

### Detailed Explanation
* **A (False):** RMSE $\ge$ MAE always (due to inequality of arithmetic and quadratic means).
* **B (True):** $\sqrt{y^2} = y$. Unit is preserved.
* **C (False):** It is sensitive to outliers because it is based on Square.
* **D (False):** Squaring makes it positive; Root keeps it positive.

---

## Q2
### Title
Manual MSE Implementation

### Problem Description
Compute sum of squared diffs divided by $n$.

### Objective
Code the formula from scratch.

### Hint
`sum((t - p)**2 for t, p in zip(...)) / n`.

### Short Explanation
Iterate through pairs, square the difference, sum them, divide by count.

### Detailed Explanation
```python
def calculate_mse(y_true, y_pred):
    n = len(y_true)
    sum_squared_error = 0
    for t, p in zip(y_true, y_pred):
        sum_squared_error += (t - p) ** 2
    return sum_squared_error / n

```

---

## Q3

### Title

Calculating MSE

### Problem Description

Compute MSE for `[10, 20, 30]` vs `[12, 19, 29]`.

### Objective

Apply the formula.

### Hint

Diffs are: +2, -1, -1.

### Short Explanation

Squares: . Mean: .

### Detailed Explanation

1. **Diffs:**
* 
* 
* 


2. **Squared Diffs:**
* 
* 
* 


3. **Sum:** 
4. **Mean:** 

---

## Q4

### Title

MAE vs MSE Use Cases

### Problem Description

Select reasons to prefer MAE.

### Objective

Choose the right metric for the business problem.

### Hint

MAE is "linear" and robust. MSE is "quadratic" and sensitive.

### Short Explanation

A is true (Robustness). B is strictly true for MAE (though RMSE also satisfies this). C and D are reasons to use MSE.

### Detailed Explanation

* **A (True):** MAE treats outliers linearly. An error of 100 is just 100, not 10,000. Good if outliers are noisy.
* **B (True):** MAE is directly interpretable.
* **C (False):**  is not differentiable at 0. MSE () is smooth.
* **D (False):** MSE does this, not MAE.

---

## Q5

### Title

Sklearn Metrics

### Problem Description

Calculate metrics using library functions.

### Objective

Standard library usage.

### Hint

Import from `sklearn.metrics`.

### Short Explanation

Call the functions `mean_absolute_error`, `mean_squared_error`, `r2_score`.

### Detailed Explanation

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

print("MAE:", mean_absolute_error(y_true, y_pred))
print("MSE:", mean_squared_error(y_true, y_pred))
print("R2:", r2_score(y_true, y_pred))

```

---

## Q6

### Title

Negative R-Squared

### Problem Description

Explain how  can be negative.

### Objective

Deep understanding of the baseline model.

### Hint

The baseline is a horizontal line at .

### Short Explanation

 compares your model's error to the error of a simple horizontal line at the mean (). If your model is **worse** than just guessing the average for every input,  will be negative.

### Detailed Explanation

* **Formula:** .
* **Scenario:** If Model Error > Baseline Error, the fraction is . Then  is negative.
* **Meaning:** Your model is actively useless. It might be predicting the opposite trend or massive outliers.

```

```
