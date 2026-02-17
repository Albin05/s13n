
# Editorials

## Q1
### Title
MAE Formula Identification

### Problem Description
Identify the math formula for MAE.

### Objective
Recall definitions.

### Hint
"Mean" = Average ($1/n$), "Absolute" = Bars ($||$).

### Short Explanation
**B** matches the definition: Average ($\frac{1}{n}$) of Absolute Differences ($|...|$).
* A is MSE.
* C is RMSE.
* D is Sum of Residuals (usually close to 0).

---

## Q2
### Title
Manual MAE Implementation

### Problem Description
Calculate MAE without libraries.

### Objective
Understand the algorithmic steps.

### Hint
Sum $|a-b|$, divide by count.

### Short Explanation
$|10-12| + |20-18| = 2 + 2 = 4$. Mean = $4/2 = 2.0$.

### Detailed Explanation
```python
def calculate_mae(y_true, y_pred):
    total_error = 0
    n = len(y_true)
    for t, p in zip(y_true, y_pred):
        total_error += abs(t - p)
    return total_error / n

```

---

## Q3

### Title

MAE Calculation

### Problem Description

Calculate MAE for 3 points.

### Objective

Arithmetic practice.

### Hint

Find differences: 10, 10, 30.

### Short Explanation

. . .
Sum = 50. Mean = .

### Detailed Explanation

1. **Diffs:** .
2. **Sum:** .
3. **Mean:** 

---

## Q4

### Title

Properties of L1 Loss

### Problem Description

Characteristics of Absolute Error.

### Objective

Deep understanding of loss landscapes.

### Hint

Is a V-shape smooth at the bottom?

### Short Explanation

A, C, and D are true. B is false (Not differentiable at the tip of the V).

### Detailed Explanation

* **A (True):** Graph of  is a V.
* **B (False):** At , the slope jumps from -1 to +1 instantly. The derivative is undefined.
* **C (True):** Linear penalty is robust.
* **D (True):** Slope is constant, unlike MSE where slope shrinks.

---

## Q5

### Title

MAE vs MSE Outlier Sensitivity

### Problem Description

Compare metrics on outlier data.

### Objective

Demonstrate robustness.

### Hint

Square the error for MSE.

### Short Explanation

* **MAE:** Error is 990. Avg = .
* **MSE:** Error is . Avg = .
* MSE is ~1000x larger due to squaring.

### Detailed Explanation

```python
import numpy as np
y_true = np.array([10, 10, 10, 1000])
y_pred = np.array([10, 10, 10, 10])

# MAE
# Errors: 0, 0, 0, 990
# Mean: 247.5
print("MAE:", np.mean(np.abs(y_true - y_pred)))

# MSE
# Squared Errors: 0, 0, 0, 980100
# Mean: 245025.0
print("MSE:", np.mean((y_true - y_pred)**2))

```

---

## Q6

### Title

Optimization Stability

### Problem Description

Why is MAE harder to optimize near 0?

### Objective

Calculus/Gradient Descent intuition.

### Hint

What happens to the step size if the gradient is always 1?

### Short Explanation

* **MSE (U-shape):** As you approach the bottom (), the slope () gets smaller naturally. This acts like an automatic brake, slowing down the updates so you land softly at the minimum.
* **MAE (V-shape):** The slope is constant (). Even when you are 0.0001 units away from the bottom, the gradient is still 1. If your learning rate isn't tiny, you will overshoot and bounce back and forth forever.

```

```
