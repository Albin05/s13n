# Question Bank: Practical Regularization

## Q1 (MCQ)
**Problem:** You train a Lasso model on a dataset containing "Age" (0-100) and "Income" (0-1,000,000) without scaling. Which feature is the model likely to punish (shrink) more aggressively, and why?
A. Age, because its values are small so its weight must be large.
B. Income, because its values are large.
C. Both equally.
D. Income, because money is more important.

## Q2 (Coding)
**Problem:** Create a robust regression pipeline.
1.  Import `make_pipeline`, `StandardScaler`, `Lasso`.
2.  Create a pipeline that scales data and then applies Lasso with `alpha=0.5`.
3.  Fit it on dummy data `X=[[10], [100]]`, `y=[1, 2]`.
4.  Print the model's coefficients.

## Q3 (NAT)
**Problem:** You are tuning `Ridge` regression.
* Training MSE with $\alpha=0$: 10.0
* Training MSE with $\alpha=100$: 50.0
* Test MSE with $\alpha=0$: 80.0
* Test MSE with $\alpha=100$: 20.0
What is the "Generalization Gap" (Test MSE - Train MSE) for the regularized model ($\alpha=100$)?

## Q4 (MSQ)
**Problem:** Which of the following are benefits of using `RidgeCV` over manually running `Ridge` inside a `GridSearchCV`?
A. `RidgeCV` often uses optimized linear algebra (Leave-One-Out Cross-Validation) which is faster than standard K-Fold.
B. `RidgeCV` automatically scales the data.
C. `RidgeCV` requires less code to write.
D. `RidgeCV` can handle classification problems.

## Q5 (Coding)
**Problem:** Simulate the failure of unscaled regularization.
1.  Create `X` where col 0 is `[1, 2]` and col 1 is `[1000, 2000]`. `y` is `[2, 4]`.
2.  Fit `Ridge(alpha=1.0)` directly. Print coefs.
3.  Fit `Ridge` after `StandardScaler`. Print coefs.
4.  Observe the massive difference in how weights are assigned.

## Q6 (Subjective)
**Problem:** You are reviewing a junior data scientist's code. They applied Ridge Regression to predict House Prices. They obtained a very high Training Error (Underfitting). They propose **increasing** the `alpha` parameter to fix this.
1.  Is this the correct decision? Why or why not?
2.  What should they do to the `alpha` instead?
