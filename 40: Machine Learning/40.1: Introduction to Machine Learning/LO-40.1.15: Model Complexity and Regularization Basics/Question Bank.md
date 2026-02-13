# Question Bank: Model Complexity and Regularization

## Q1 (MCQ)
**Problem:** In the context of Ridge Regression (L2), the penalty term added to the cost function is proportional to:
A. The sum of the weights.
B. The sum of the absolute values of the weights.
C. The sum of the square of the weights.
D. The square root of the weights.

## Q2 (Coding)
**Problem:** You have a dataset `X, y`. Train two models: a standard Linear Regression and a Ridge Regression with `alpha=10`. Print the coefficients (`coef_`) of both to compare them.
*Note: Use `sklearn.linear_model`.*

## Q3 (NAT)
**Problem:** A model has a training error (MSE) of 50. The sum of squared weights is 100. If we use L2 regularization with $\lambda = 0.5$, what is the total value of the Cost Function?

## Q4 (MSQ)
**Problem:** Which of the following statements are TRUE regarding L1 (Lasso) and L2 (Ridge) regularization?
A. L2 is differentiable everywhere, making it easier to optimize using Gradient Descent.
B. L1 produces "Sparse" models (many weights become zero).
C. Both L1 and L2 increase the Training Error compared to an unregularized model.
D. Regularization is only useful when you have huge amounts of data.

## Q5 (Coding)
**Problem:** Write a function `calculate_l1_penalty(weights, lambda_val)` that manually calculates the L1 penalty term.
**Input:** `weights = [2, -3, 0.5]`, `lambda_val = 0.1`
**Output:** Return the value.

## Q6 (Subjective)
**Problem:** Explain the concept of the "Bias-Variance Tradeoff" specifically in the context of the regularization parameter $\lambda$. As $\lambda$ increases from 0 to infinity, how do Bias and Variance change?
