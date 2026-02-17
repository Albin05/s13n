
# Editorials

## Q1
### Title
Algorithm Steps

### Problem Description
Identify the unnecessary step.

### Objective
Understand the core loop.

### Hint
Does the order of data points matter for the line equation?

### Short Explanation
**Sorting** is not required. The line of best fit depends on the values, not their order in the array.

### Detailed Explanation
* **A, B, D:** Essential steps of Gradient Descent.
* **C:** Sorting $X$ or $y$ destroys the relationship between them (if you sort independently) or simply reorders rows (which doesn't change the sum of errors).

---

## Q2
### Title
Necessity of Scaling

### Problem Description
Why scale features for GD?

### Objective
Optimization theory.

### Hint
Think about the shape of the bowl.

### Short Explanation
If features have different scales (e.g., Age vs Salary), the cost function becomes a stretched ellipse (taco shape). Gradient descent zig-zags and takes a long time to reach the bottom. Scaling makes it a circle (bowl), allowing direct descent.

### Detailed Explanation
* **Unscaled:** Gradients are steep for one variable and flat for another.
* **Scaled:** Gradients are uniform.
* **Normal Equation:** Does not use gradients, so it handles unscaled data mathematically fine (though numerical stability issues can arise).

---

## Q3
### Title
Normal Equation Limitations

### Problem Description
Why avoid Normal Equation for Big Data?

### Objective
Complexity analysis.

### Hint
Matrix Inversion.

### Short Explanation
The Normal Equation involves calculating the inverse of $(X^T X)$. The computational complexity of inverting a matrix is roughly $O(n^3)$ (cubic). If you have 100,000 features, this becomes impossible to compute.

### Detailed Explanation
* **Gradient Descent:** $O(kn)$ where $k$ is number of steps. Linear scalability.
* **Normal Equation:** $O(n^3)$. Cubic scalability. explodes quickly.

---

## Q4
### Title
Signs of Convergence

### Problem Description
Select indicators that training is done.

### Objective
Monitoring training.

### Hint
When you reach the bottom of the valley, do you keep moving?

### Short Explanation
A, B, and D are signs of convergence. C is incorrect (LR is a fixed hyperparameter, usually).

### Detailed Explanation
* **A:** Cost plateauing means we can't improve much more.
* **B:** Zero gradient means we are at the minimum.
* **D:** Weights stabilizing means the update step is negligible.

---

## Q5
### Title
Normal Equation Implementation

### Problem Description
Compute $(X^T X)^{-1} X^T y$.

### Objective
Linear Algebra implementation.

### Hint
Use `np.linalg.inv`. Don't forget the bias column.

### Short Explanation
Add bias, transpose, multiply, invert.

### Detailed Explanation
```python
import numpy as np

def normal_equation(X, y):
    # Add bias column (1s)
    X_b = np.c_[np.ones((len(X), 1)), X]
    
    # Formula
    theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    
    return theta

```

---

## Q6

### Title

Homoscedasticity Assumption

### Problem Description

Explain constant variance of errors.

### Objective

Statistical assumptions of OLS.

### Hint

Does the error cloud look like a funnel?

### Short Explanation

**Homoscedasticity** means the "spread" or variance of the residuals is constant for all values of .

* **Visual:** The residuals look like a random cloud of constant width around the line.
* **Violation (Heteroscedasticity):** The residuals look like a **Funnel** (Fan shape). For example, prediction is accurate for low salaries, but wildly inaccurate for high salaries.
* **Problem:** The model's confidence intervals will be wrong (it will be overconfident in high-variance regions).

```

```
