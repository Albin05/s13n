# Question Bank: Absolute Error

## Q1 (MCQ)
**Problem:** Which of the following is the correct formula for Mean Absolute Error (MAE)?
A. $\frac{1}{n} \sum (y_i - \hat{y}_i)^2$
B. $\frac{1}{n} \sum |y_i - \hat{y}_i|$
C. $\sqrt{\frac{1}{n} \sum (y_i - \hat{y}_i)^2}$
D. $\sum (y_i - \hat{y}_i)$

## Q2 (Coding)
**Problem:** Write a function `calculate_mae(y_true, y_pred)` that takes two lists and returns the Mean Absolute Error. Do not use any external libraries like sklearn.
**Input:** `[10, 20]`, `[12, 18]`
**Output:** `2.0`

## Q3 (NAT)
**Problem:** A model makes three predictions.
* True Values: `[100, 200, 300]`
* Predictions: `[110, 190, 330]`
Calculate the MAE.

## Q4 (MSQ)
**Problem:** Select all statements that are **TRUE** about the L1 Loss function (Absolute Error).
A. Its graph looks like a "V".
B. It is differentiable everywhere, including at 0.
C. It is more robust to outliers than L2 Loss (Squared Error).
D. Its gradient is constant (either 1 or -1) everywhere except 0.

## Q5 (Coding)
**Problem:** You have a dataset with an outlier.
`y_true = [10, 10, 10, 1000]` (1000 is an outlier)
`y_pred = [10, 10, 10, 10]` (Model ignores outlier)
Calculate and print both MAE and MSE to demonstrate how much more MSE penalizes the outlier.

## Q6 (Subjective)
**Problem:** Why is the gradient of the Mean Absolute Error (MAE) considered "unstable" for optimization near the minimum compared to Mean Squared Error (MSE)? Think about the slope of the "V" shape versus the slope of the "U" shape as you get closer to 0.
