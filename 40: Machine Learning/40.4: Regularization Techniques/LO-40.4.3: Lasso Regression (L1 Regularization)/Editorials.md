
# Editorials

## Q1
### Title
Geometric Shape of Lasso

### Problem Description
Identify the shape of the L1 constraint.

### Objective
Visual intuition of sparsity.

### Hint
$|x| + |y| = 1$. Plot the points $(1,0), (0,1), (-1,0), (0,-1)$.

### Short Explanation
The equation $|w_1| + |w_2| \le t$ forms a **Diamond** (a square rotated by 45 degrees) centered at the origin.

### Detailed Explanation
* **Circle (Ridge):** Smooth curve.
* **Diamond (Lasso):** Sharp corners on the axes. These corners are where the "Zero Weight" solutions live.

---

## Q2
### Title
Lasso Loss Implementation

### Problem Description
Calculate cost: $E + \lambda \sum |w|$.

### Objective
Implement the mathematical formula.

### Hint
Absolute values.

### Short Explanation
$10 + 0.5 \times (|2| + |-3|) = 10 + 0.5 \times 5 = 12.5$.

### Detailed Explanation
```python
def lasso_loss(w, error, lambd):
    penalty = sum([abs(weight) for weight in w])
    return error + (lambd * penalty)

```

---

## Q3

### Title

Calculating Lasso Cost

### Problem Description

Compute .

### Objective

Apply the L1 penalty formula.

### Hint

Sum of absolute values is 7.

### Short Explanation

.

### Detailed Explanation

1. **L1 Norm:** .
2. **Penalty:** .
3. **Total:** .

---

## Q4

### Title

Lasso Properties

### Problem Description

Select true statements about L1 regularization.

### Objective

Verify theoretical understanding.

### Hint

Is  differentiable at 0?

### Short Explanation

A, C, and D are true. B is false (The absolute value function has a "kink" at 0 and is not differentiable there, requiring special optimization techniques like Coordinate Descent).

### Detailed Explanation

* **A (True):** Sparsity = Zeros.
* **B (False):** Not differentiable at 0.
* **C (True):** Classic use case ().
* **D (True):** Linear penalty.

---

## Q5

### Title

Feature Selection with Lasso

### Problem Description

Identify non-zero weights.

### Objective

Use Lasso as a filter.

### Hint

Check `model.coef_`.

### Short Explanation

Fit model, iterate `coef_`, print index if not 0.

### Detailed Explanation

```python
from sklearn.linear_model import Lasso
import numpy as np

X = np.random.rand(100, 10) # 10 Features
y = X[:, 0] * 2 + X[:, 1] * 3 # Only 0 and 1 matter

lasso = Lasso(alpha=0.1)
lasso.fit(X, y)

selected_features = [i for i, coef in enumerate(lasso.coef_) if coef != 0]
print("Selected Indices:", selected_features)

```

---

## Q6

### Title

The Corner Solution

### Problem Description

Why does Lasso produce zeros?

### Objective

Geometric intuition.

### Hint

Imagine inflating a balloon (loss contours) inside a box (constraint). Where does it touch first?

### Short Explanation

* **Geometry:** The L1 constraint is a Diamond with sharp corners on the axes (where ).
* **Probability:** When the elliptical contours of the Loss function expand to meet the constraint, they are geometrically much more likely to hit the "pointy" corner first than to hit the flat side of the diamond perfectly tangent.
* **Ridge:** The L2 constraint is a Circle. A circle has no corners. The contours will touch it at some random point on the curve, where  is small but non-zero.

```

```
