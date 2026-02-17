
# Editorials

## Q1
### Title
The Scale Trap

### Problem Description
Effect of unscaled data on Lasso weights.

### Objective
Apply scaling intuition.

### Hint
Small inputs require Large weights to produce the output. Large weights get punished.

### Short Explanation
**A:** "Age" has small values (0-100). To impact the prediction $y$, its weight $w_{age}$ needs to be relatively large. "Income" has huge values, so $w_{income}$ needs to be tiny.
Since Regularization minimizes weights, it will aggressively crush the **Large Weight** ($w_{age}$), effectively removing Age from the model purely because of its units.

### Detailed Explanation
* **Penalty:** $\lambda |w|$.
* **Scenario:** $w_{age} \approx 10$, $w_{inc} \approx 0.001$.
* **Result:** The algorithm sees $w_{age}$ as the "problem" and shrinks it, even if Age is the most important predictor.

---

## Q2
### Title
Pipeline Implementation

### Problem Description
Code a scaler + regressor pipeline.

### Objective
Best practice coding.

### Hint
`make_pipeline(StandardScaler(), Lasso(alpha=0.5))`.

### Short Explanation
Standard Scikit-Learn syntax.

### Detailed Explanation
```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso

model = make_pipeline(StandardScaler(), Lasso(alpha=0.5))
X = [[10], [100]]
y = [1, 2]
model.fit(X, y)
# To get coefs from a pipeline step:
print(model.named_steps['lasso'].coef_)

```

---

## Q3

### Title

Generalization Gap

### Problem Description

Calculate gap for .
Train MSE: 50. Test MSE: 20. (Note: It's unusual for Test < Train, but mathematically possible in small samples or specific distributions).

### Objective

Metric interpretation.

### Hint

Test - Train.

### Short Explanation

.
*Note:* Usually gap is positive (Test > Train). A large negative gap implies the test set was "easier" or regularization worked extremely well to simplify the model. If we take absolute magnitude, the gap is smaller than the unregularized case ().

### Detailed Explanation

* **Unregularized Gap:**  (Huge Overfitting).
* **Regularized Gap:**  (Ideally we want this close to 0, but Test < Train indicates strong regularization).

---

## Q4

### Title

RidgeCV Benefits

### Problem Description

Why use the specialized class?

### Objective

Library knowledge.

### Hint

Optimization tricks.

### Short Explanation

A and C are true. B is false (Scaling is never automatic). D is false (Use `RidgeClassifier` for that).

### Detailed Explanation

* **A (True):** `RidgeCV` uses Efficient Leave-One-Out CV which reuses computations, making it much faster than generic `GridSearchCV`.
* **C (True):** Built-in alphas list handling.

---

## Q5

### Title

Scaling Simulation

### Problem Description

Compare coefficients with and without scaling.

### Objective

Prove the necessity of scaling empirically.

### Hint

The unscaled model will have one tiny weight and one huge weight (or zero).

### Short Explanation

Code demonstration.

### Detailed Explanation

```python
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1, 1000], [2, 2000]])
y = np.array([2, 4])

# Unscaled
r1 = Ridge(alpha=1.0)
r1.fit(X, y)
print("Unscaled:", r1.coef_) 
# Weights will be unbalanced (one very small)

# Scaled
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
r2 = Ridge(alpha=1.0)
r2.fit(X_scaled, y)
print("Scaled:", r2.coef_) 
# Weights will be balanced

```

---

## Q6

### Title

Tuning Alpha

### Problem Description

Junior DS increases alpha to fix Underfitting.

### Objective

Hyperparameter dynamics.

### Hint

Does increasing alpha make the model more complex or simpler?

### Short Explanation

1. **Incorrect.** Increasing `alpha` increases the penalty. This simplifies the model further.
2. **Action:** Since the model is **Underfitting** (High Bias), it is already too simple. They should **decrease** `alpha` (towards 0) to allow the model more freedom to fit the training data. Or, switch to a more complex model (Polynomials).

```

```
