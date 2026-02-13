
# Editorials

## Q1
### Title
L2 Penalty Definition

### Problem Description
Identify the mathematical term for Ridge (L2) Regularization.

### Objective
Distinguish between L1 and L2 formulas.

### Hint
"Square" is the keyword for L2.

### Short Explanation
L2 (Ridge) uses the sum of squared weights ($\sum w^2$). L1 (Lasso) uses absolute values.

### Detailed Explanation
* **L1:** $\lambda \sum |w_i|$ (Absolute value)
* **L2:** $\lambda \sum w_i^2$ (Squared value)
* Therefore, C is the correct answer.

---

## Q2
### Title
Comparing Ridge and Linear Coefficients

### Problem Description
Train Linear vs Ridge models and compare coefficients.

### Objective
Observe how Regularization shrinks weights.

### Hint
Standard sklearn fit/predict workflow.

### Short Explanation
Instantiate `LinearRegression()` and `Ridge(alpha=10)`. Fit both. Print `model.coef_`.

### Detailed Explanation
```python
from sklearn.linear_model import LinearRegression, Ridge

# Assuming X, y are loaded
lin_reg = LinearRegression().fit(X, y)
ridge_reg = Ridge(alpha=10).fit(X, y)

print("Linear Coefs:", lin_reg.coef_)
print("Ridge Coefs:", ridge_reg.coef_)

```

*Expected Result:* The coefficients of the Ridge model should be smaller (closer to zero) than the Linear model.

---

## Q3

### Title

Calculating Cost with L2

### Problem Description

Calculate Total Cost given MSE, Weights, and Lambda.

### Objective

Apply the Regularized Cost Function formula.

### Hint

Cost = MSE + (Lambda * Penalty).

### Short Explanation

.

### Detailed Explanation

1. **MSE Term:** 50
2. **Penalty Term (L2):** 
3. **Total Cost:** .

---

## Q4

### Title

Properties of Regularization

### Problem Description

Select true statements about L1/L2 characteristics.

### Objective

Understand the theoretical implications of Regularization.

### Hint

Does adding a constraint make it harder to fit the training data perfectly? Yes.

### Short Explanation

A, B, and C are true. D is false (Regularization is *most* useful when data is scarce to prevent overfitting).

### Detailed Explanation

* **A (True):**  is a smooth curve, differentiable everywhere.  has a sharp corner at 0, making it harder to optimize.
* **B (True):** L1 creates sparsity (zeros out weights).
* **C (True):** By restricting the weights, we prevent the model from perfectly fitting the training noise, so Training Error usually goes up slightly (but Test Error should go down).
* **D (False):** It is crucial for small datasets.

---

## Q5

### Title

Manual L1 Calculation

### Problem Description

Calculate .

### Objective

Implement the math logic in code.

### Hint

Sum the absolute values, then multiply by lambda.

### Short Explanation

Sum: . Result: .

### Detailed Explanation

```python
def calculate_l1_penalty(weights, lambda_val):
    penalty = sum([abs(w) for w in weights])
    return penalty * lambda_val

```

---

## Q6

### Title

Lambda and Bias-Variance

### Problem Description

Trace the path of Bias and Variance as  increases.

### Objective

Connect Regularization strength to the Tradeoff.

### Hint

High Lambda = Simple Model. Low Lambda = Complex Model.

### Short Explanation

As : Bias increases (Underfitting), Variance decreases (More Stable).

### Detailed Explanation

* **Low  (near 0):** The model is free to be complex. It fits the training data perfectly. **Bias is Low**, **Variance is High** (Overfitting).
* **High :** The model is heavily constrained (weights forced near zero). It becomes too simple (like a flat line). **Bias is High** (Underfitting), **Variance is Low** (Stable).
* **Goal:** Find the intermediate  where Total Error is minimized.

```

```
