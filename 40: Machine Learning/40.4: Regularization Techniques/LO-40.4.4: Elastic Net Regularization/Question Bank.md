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
