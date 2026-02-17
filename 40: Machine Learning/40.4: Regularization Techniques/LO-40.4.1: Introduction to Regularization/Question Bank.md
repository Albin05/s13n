# Question Bank: Intro to Regularization

## Q1 (MCQ)
**Problem:** Which of the following scenarios indicates a need for Regularization?
A. Training Accuracy = 99%, Test Accuracy = 98%.
B. Training Accuracy = 60%, Test Accuracy = 55%.
C. Training Accuracy = 99%, Test Accuracy = 65%.
D. Training Accuracy = 80%, Test Accuracy = 82%.

## Q2 (Coding)
**Problem:** Write a function `regularized_cost(y_true, y_pred, weights, lambd)` that computes the cost using MSE plus an **L2 Penalty** (sum of squared weights).
Formula: $J = \frac{1}{n}\sum(y-\hat{y})^2 + \lambda \sum w^2$.
**Input:** `y=[1, 2]`, `pred=[1, 2]`, `w=[10, 5]`, `lambd=0.1`.
**Output:** `12.5`

## Q3 (NAT)
**Problem:**
* MSE Error = 50.
* Sum of Absolute Weights = 100.
* Lambda ($\lambda$) = 0.5.
Calculate the Total Cost using L1 Regularization ($Cost = MSE + \lambda \times |w|$).

## Q4 (MSQ)
**Problem:** Which of the following statements about Regularization are TRUE?
A. It adds a penalty term to the loss function.
B. It is used to solve the Underfitting problem.
C. It shrinks the magnitude of the model parameters (weights).
D. It helps when the dataset has high dimensionality (many features) compared to the number of samples.

## Q5 (Coding)
**Problem:** Simulate the effect of lambda.
1.  Define `w = 10`.
2.  Cost function $J(w) = (w-2)^2 + \lambda w^2$.
3.  For `lambda = [0, 1, 10]`, find the `w` that minimizes $J(w)$ using a simple loop or derivative logic ($w^* = 2 / (1+\lambda)$).
4.  Print how `w` shrinks as lambda increases.

## Q6 (Subjective)
**Problem:** Explain the concept of the **"Bias-Variance Tradeoff"** in the context of Regularization. Why does adding a penalty term (which intentionally makes the model perform slightly worse on the training data) actually help in the long run?
