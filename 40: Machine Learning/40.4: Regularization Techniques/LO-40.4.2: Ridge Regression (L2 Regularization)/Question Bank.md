# Question Bank: Ridge Regression

## Q1 (MCQ)
**Problem:** Which of the following statements about the geometric interpretation of Ridge Regression is true?
A. The constraint region is a square (Diamond shape).
B. The constraint region is a circle (Hypersphere).
C. The optimal solution is always at the corners of the constraint region.
D. It performs feature selection by setting weights to zero.

## Q2 (Coding)
**Problem:** Write a function `ridge_loss(w, error, lambd)` that computes the total cost for Ridge.
*Cost = Error + Lambda * Sum(w^2)*
**Input:** `w=[2, 3]`, `error=10`, `lambd=0.5`
**Output:** `16.5`

## Q3 (NAT)
**Problem:**
* MSE = 50.
* Weights = `[3, 4]`.
* Lambda ($\lambda$) = 2.0.
Calculate the **Ridge Cost**.

## Q4 (MSQ)
**Problem:** What happens as you increase the regularization parameter $\lambda$ in Ridge Regression?
A. The training error likely increases.
B. The variance of the model decreases.
C. The model becomes more complex.
D. The coefficients (weights) approach zero.

## Q5 (Coding)
**Problem:** Use `sklearn` to find the best `alpha` for a Ridge model using `RidgeCV` (Cross-Validation).
1.  Create `X` (10x5 random), `y` (10 random).
2.  Define alphas `[0.1, 1.0, 10.0]`.
3.  Fit `RidgeCV`.
4.  Print the chosen alpha.

## Q6 (Subjective)
**Problem:** Explain why Ridge Regression does **not** perform Feature Selection (setting weights to 0), whereas Lasso (L1) does. Use the concept of the squared penalty shape ($w^2$) vs the absolute penalty shape ($|w|$).
