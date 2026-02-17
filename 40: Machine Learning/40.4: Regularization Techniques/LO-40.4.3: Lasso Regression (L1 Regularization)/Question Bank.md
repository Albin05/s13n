# Question Bank: Lasso Regression

## Q1 (MCQ)
**Problem:** Geometrically, the constraint region for Lasso Regression (L1) in 2D space ($w_1, w_2$) is shaped like a:
A. Circle
B. Square / Diamond
C. Triangle
D. Parabola

## Q2 (Coding)
**Problem:** Write a function `lasso_loss(w, error, lambd)` that computes the total cost for Lasso.
*Cost = Error + Lambda * Sum(|w|)*
**Input:** `w=[2, -3]`, `error=10`, `lambd=0.5`
**Output:** `12.5`

## Q3 (NAT)
**Problem:**
* MSE = 50.
* Weights = `[3, -4]`.
* Lambda ($\lambda$) = 2.0.
Calculate the **Lasso Cost**.

## Q4 (MSQ)
**Problem:** Which of the following statements about Lasso are TRUE?
A. It yields sparse models.
B. It is differentiable everywhere (including at $w=0$).
C. It is useful when the number of features ($p$) is greater than the number of observations ($n$).
D. It penalizes large weights more severely than small weights (linear penalty).

## Q5 (Coding)
**Problem:** Use `sklearn` to select features using Lasso.
1.  Create `X` (Random, 10 columns). Make column 0 and 1 useful, others noise.
2.  Fit `Lasso(alpha=0.1)`.
3.  Print the indices of the features where `coef_ != 0`.

## Q6 (Subjective)
**Problem:** Explain the "Corner Solution" concept in Lasso Regression using the geometric interpretation. Why does the Diamond shape make it likely for the optimal solution to lie on an axis (where one coordinate is zero), whereas the Circle shape (Ridge) does not?
