
# Editorials

## Q1
### Title
Geometric Interpretation

### Problem Description
Identify the shape of the L2 constraint.

### Objective
Visualize the penalty region.

### Hint
$x^2 + y^2 = r^2$ is the equation of a circle.

### Short Explanation
The L2 norm ($\sum w^2 \le t$) defines a circular (or hyperspherical) constraint region. The solution is where the loss contours touch this circle.

### Detailed Explanation
* **L1 (Lasso):** $|w_1| + |w_2| \le t$ is a Diamond/Square. Corners touch axes (Zero weights).
* **L2 (Ridge):** $w_1^2 + w_2^2 \le t$ is a Circle. It touches the loss contours smoothly, shrinking weights but rarely hitting 0 exactly.

---

## Q2
### Title
Ridge Loss Implementation

### Problem Description
Calculate cost: $E + \lambda \sum w^2$.

### Objective
Implement the mathematical formula.

### Hint
Square the weights first.

### Short Explanation
$10 + 0.5 \times (2^2 + 3^2) = 10 + 0.5 \times 13 = 10 + 6.5 = 16.5$.

### Detailed Explanation
```python
def ridge_loss(w, error, lambd):
    penalty = sum([weight**2 for weight in w])
    return error + (lambd * penalty)

```

---

## Q3

### Title

Calculating Ridge Cost

### Problem Description

Compute .

### Objective

Apply the L2 penalty formula.

### Hint

.

### Short Explanation

.

### Detailed Explanation

1. **Sum of Squares:** .
2. **Penalty:** .
3. **Total:** .

---

## Q4

### Title

Effect of Lambda

### Problem Description

Select consequences of increasing Regularization.

### Objective

Understand the Bias-Variance tradeoff.

### Hint

Regularization simplifies the model.

### Short Explanation

A, B, and D are true. C is false (Model becomes simpler).

### Detailed Explanation

* **A (True):** Adding bias increases training error.
* **B (True):** Reducing flexibility reduces variance (overfitting).
* **C (False):** Simplicity increases.
* **D (True):** Weights shrink.

---

## Q5

### Title

RidgeCV Implementation

### Problem Description

Use built-in Cross-Validation for Ridge.

### Objective

Standard library usage for hyperparameter tuning.

### Hint

`RidgeCV(alphas=...).fit(...)`.

### Short Explanation

Import, instantiate, fit, print `.alpha_`.

### Detailed Explanation

```python
from sklearn.linear_model import RidgeCV
import numpy as np

X = np.random.rand(10, 5)
y = np.random.rand(10)
alphas = [0.1, 1.0, 10.0]

clf = RidgeCV(alphas=alphas).fit(X, y)
print(clf.alpha_)

```

---

## Q6

### Title

Why Ridge Doesn't Zero Out Weights

### Problem Description

Compare L2 (Parabola) vs L1 (V-shape) near zero.

### Objective

Calculus/Geometry intuition.

### Hint

What is the slope of  at 0? What is the slope of  at 0?

### Short Explanation

* **Ridge ():** As , the gradient  becomes tiny. The shrinking force ("pull") fades away, so the weight approaches 0 asymptotically but never quite reaches it.
* **Lasso ():** The gradient is constant (). The shrinking force stays strong all the way to 0, effectively snapping the weight to exactly 0.

```

```
