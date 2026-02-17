# Question Bank: Regression Metrics

## Q1 (MCQ)
**Problem:** Which of the following statements is TRUE about RMSE (Root Mean Squared Error)?
A. RMSE is always smaller than MAE.
B. RMSE has the same unit as the target variable.
C. RMSE is robust to outliers (ignores them).
D. RMSE can be negative.

## Q2 (Coding)
**Problem:** Write a function `calculate_mse(y_true, y_pred)` from scratch (without using sklearn) that computes the Mean Squared Error between two lists of numbers.
**Input:** `y_true=[1, 2, 3]`, `y_pred=[1, 2, 3]`
**Output:** `0.0`

## Q3 (NAT)
**Problem:** You have three data points.
Actual: `[10, 20, 30]`
Predicted: `[12, 19, 29]`
Calculate the **Mean Squared Error (MSE)**. (Round to 2 decimal places).

## Q4 (MSQ)
**Problem:** Which of the following are valid reasons to choose **MAE** over **MSE**?
A. Your dataset has many outliers that are actually valid data points, and you don't want the model to over-focus on them.
B. You need the error metric to be in the same unit as the target variable for easy reporting to non-technical stakeholders.
C. You need the error function to be differentiable everywhere for Gradient Descent (Note: MAE is not differentiable at 0).
D. You want to penalize large errors more than small errors.

## Q5 (Coding)
**Problem:** Use `sklearn` to evaluate a regression model.
1.  Create `y_true = [3, -0.5, 2, 7]` and `y_pred = [2.5, 0.0, 2, 8]`.
2.  Calculate MAE, MSE, and R2 score.
3.  Print them.

## Q6 (Subjective)
**Problem:** Explain why a model can have a negative $R^2$ score. What does this physically mean about the model's predictions compared to a naive baseline?
