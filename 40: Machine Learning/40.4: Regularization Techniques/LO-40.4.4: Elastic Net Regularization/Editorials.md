
# Question Bank: Elastic Net

## Q1 (MCQ)
**Problem:** Which geometric shape represents the constraint region of **Elastic Net** Regularization?
A. A perfect Circle.
B. A perfect Diamond (Square rotated 45 degrees).
C. A rounded Diamond (Diamond with curved edges).
D. A Triangle.

## Q2 (Coding)
**Problem:** Write a function `elastic_net_loss(w, error, alpha, l1_ratio)` that computes the cost.
*Cost = Error + alpha * (l1_ratio * |w| + 0.5 * (1 - l1_ratio) * w^2)*
**Input:** `w=[2]`, `error=10`, `alpha=1`, `l1_ratio=0.5`
**Output:** `12.0`

## Q3 (NAT)
**Problem:**
* MSE = 50.
* Weights = `[4]`.
* Alpha ($\alpha$) = 1.0.
* L1 Ratio ($\rho$) = 0.8.
Calculate the **Elastic Net Cost**. (Assume Scikit-Learn's formula structure: $a \cdot \rho \cdot |w| + \frac{a(1-\rho)}{2} w^2$).

## Q4 (MSQ)
**Problem:** When is Elastic Net preferred over Lasso?
A. When $n$ (samples) > $p$ (features).
B. When features are highly correlated.
C. When we want a sparse model (feature selection) but need stability.
D. When we want to eliminate the bias of the model completely.

## Q5 (Coding)
**Problem:** Use `sklearn` to tune an Elastic Net model.
1.  Create `X` (Random 10x5), `y` (Random 10).
2.  Define `ElasticNetCV` with `l1_ratio=[0.1, 0.5, 0.9]`.
3.  Fit the model.
4.  Print the best `l1_ratio_` found.

## Q6 (Subjective)
**Problem:** Explain the **"Grouping Effect"** of Elastic Net. If you have three identical features (Genes A, B, C that always activate together), how would Lasso treat them versus how Elastic Net would treat them? Why is the Elastic Net behavior often more biologically/physically meaningful?

```

---

### File 7: Editorials.md

```markdown
# Editorials

## Q1
### Title
Elastic Net Composition

### Problem Description
Identify the components of Elastic Net.

### Objective
Recall definitions.

### Hint
It's elastic because it stretches between L1 and L2.

### Short Explanation
**B:** Elastic Net = L1 (Lasso) + L2 (Ridge).

### Detailed Explanation
It adds both penalty terms to the loss function to gain benefits of both.

---

## Q2
### Title
L1 Ratio Extreme

### Problem Description
What happens when `l1_ratio = 0`?

### Objective
Understand the mixing parameter.

### Hint
L1 Ratio is the percentage of Lasso. 0% Lasso means...?

### Short Explanation
**B (Ridge):** If the ratio of L1 is 0, then 100% of the penalty comes from L2 (Ridge).

### Detailed Explanation
* `l1_ratio = 1.0` $\to$ Lasso.
* `l1_ratio = 0.0` $\to$ Ridge.
* `0 < l1_ratio < 1` $\to$ Elastic Net.

---

## Q3
### Title
Elastic Net Calculation

### Problem Description
Compute $50 + 1.0 \cdot (0.8 \cdot 4 + 0.5 \cdot 0.2 \cdot 16)$.

### Objective
Apply the specific combination formula.

### Hint
Calculate L1 and L2 terms separately.

### Short Explanation
L1 Term: $0.8 \times 4 = 3.2$.
L2 Term: $0.5 \times 0.2 \times 16 = 1.6$.
Total: $50 + 3.2 + 1.6 = 54.8$.

### Detailed Explanation
1.  **L1 Part:** $\alpha \cdot \rho \cdot |w| = 1 \cdot 0.8 \cdot 4 = 3.2$.
2.  **L2 Part:** $\frac{\alpha(1-\rho)}{2} w^2 = \frac{1(0.2)}{2} \cdot 16 = 0.1 \cdot 16 = 1.6$.
3.  **Total:** $50 + 3.2 + 1.6 = 54.8$.

---

## Q4
### Title
Elastic Net Use Cases

### Problem Description
Select scenarios favoring Elastic Net.

### Objective
Applied theory.

### Hint
Lasso fails with correlation.

### Short Explanation
B and C are true. A is usually handled fine by Lasso. D is false (Regularization *adds* bias).

### Detailed Explanation
* **B (True):** Ridge part handles correlation; Lasso part selects features.
* **C (True):** Best of both worlds.

---

## Q5
### Title
ElasticNetCV Implementation

### Problem Description
Tune hyperparameters automatically.

### Objective
Scikit-Learn pipeline usage.

### Hint
`ElasticNetCV(l1_ratio=...).fit(...)`.

### Short Explanation
Standard CV implementation.

### Detailed Explanation
```python
from sklearn.linear_model import ElasticNetCV
import numpy as np

X = np.random.rand(10, 5)
y = np.random.rand(10)

regr = ElasticNetCV(l1_ratio=[0.1, 0.5, 0.9], cv=3)
regr.fit(X, y)
print(regr.l1_ratio_)

```

---

## Q6

### Title

The Grouping Effect

### Problem Description

Compare Lasso vs Elastic Net on identical features.

### Objective

Understand stability and interpretability.

### Hint

Lasso is "greedy" and random.

### Short Explanation

* **Lasso:** Randomly picks ONE gene (e.g., Gene A) and sets coefficients for B and C to zero. This is misleading because B and C are also important.
* **Elastic Net:** Groups them. It will select A, B, and C and assign them equal (or similar) weights.
* **Benefit:** In biology/physics, if genes are correlated, they likely belong to the same pathway. Ignoring them loses information. Elastic Net preserves the "pathway" information.

```

```
