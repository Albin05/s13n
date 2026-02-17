
# Editorials

## Q1
### Title
Convexity Definition

### Problem Description
Identify the geometric property of a convex function.

### Objective
Visualize the optimization landscape.

### Hint
Think of a bowl.

### Short Explanation
A convex function guarantees that any line segment connecting two points on the graph lies above or on the graph. This geometry ensures a single minimum.

### Detailed Explanation
* **A (False):** Convex functions have only ONE minimum (Global).
* **B (False):** Egg cartons are non-convex.
* **C (True):** This is the mathematical definition.
* **D (False):** GD works perfectly on convex functions.

---

## Q2
### Title
Huber Loss Implementation

### Problem Description
Implement a hybrid loss function that is quadratic for small errors and linear for large errors.

### Objective
Advanced cost function implementation.

### Hint
Use `np.where` or a simple loop to check the condition against `delta`.

### Short Explanation
Check the absolute error. Apply squared formula if small, linear formula if large.

### Detailed Explanation
```python
import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    error = y_true - y_pred
    is_small_error = np.abs(error) < delta
    
    squared_loss = 0.5 * error**2
    linear_loss = delta * (np.abs(error) - 0.5 * delta)
    
    return np.where(is_small_error, squared_loss, linear_loss).mean()

```

*Note: Huber Loss combines the best of MSE (differentiable at 0) and MAE (robust to outliers).*

---

## Q3

### Title

Minimizing Quadratics

### Problem Description

Find min of .

### Objective

Basic calculus/algebra optimization.

### Hint

When is  smallest?

### Short Explanation

The squared term  is always non-negative. Its smallest value is 0, which happens when .

### Detailed Explanation

1. **Vertex Form:** The equation is a parabola opening upwards with vertex at .
2. **Minimum:** The minimum value occurs at . The cost at this point is 5.
3. **Derivative:** . Set to 0: .

---

## Q4

### Title

Optimization Methods

### Problem Description

Select true statements about optimizers.

### Objective

Distinguish between Iterative vs Analytical methods.

### Hint

SGD is noisy; Batch is smooth.

### Short Explanation

A, B, and D are true. C is false.

### Detailed Explanation

* **A (True):** GD takes steps.
* **B (True):** Normal Equation () solves it instantly using algebra.
* **C (False):** SGD uses 1 sample, so it zig-zags wildly (high variance). Batch uses all samples, so it is smooth.
* **D (True):** Update rule is . If lr=0,  never changes.

---

## Q5

### Title

Vectorized Gradient Calculation

### Problem Description

Implement the gradient formula using matrix multiplication.

### Objective

Efficient Numpy implementation.

### Hint

Use `X.T.dot(error)`.

### Short Explanation

Calculate prediction, find error, multiply by transposed X.

### Detailed Explanation

```python
def compute_gradients(X, y, w):
    n = len(y)
    predictions = X.dot(w)
    error = predictions - y
    gradient = (2/n) * X.T.dot(error)
    return gradient

```

---

## Q6

### Title

MSE vs MAE Differentiability

### Problem Description

Why prefer MSE over MAE for optimization?

### Objective

Link Calculus concepts to ML implementation.

### Hint

What is the derivative of  at ?

### Short Explanation

MSE () is smooth and differentiable everywhere. MAE () has a sharp "kink" at 0, making its derivative undefined at the most important point (the bottom).

### Detailed Explanation

* **MSE ():** The derivative is . As we approach 0, the gradient becomes smaller (), naturally slowing down the descent (soft landing).
* **MAE ():** The derivative is constant (). As we approach 0, the gradient stays 1, causing the optimizer to bounce around the minimum unless we manually reduce the learning rate.
* **Conclusion:** MSE is mathematically "nicer" for Gradient Descent.

```

```
