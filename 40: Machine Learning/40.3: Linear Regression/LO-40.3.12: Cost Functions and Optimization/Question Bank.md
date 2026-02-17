# Question Bank: Cost Functions

## Q1 (MCQ)
**Problem:** Which of the following is a property of a Convex Cost Function?
A. It has multiple local minima.
B. It looks like an egg carton.
C. A line drawn between any two points on the curve stays above the curve.
D. Gradient Descent is likely to get stuck.

## Q2 (Coding)
**Problem:** Implement the **Huber Loss** function.
* Formula:
    * If $|y - \hat{y}| < \delta$: Loss = $\frac{1}{2}(y - \hat{y})^2$
    * Else: Loss = $\delta(|y - \hat{y}| - \frac{1}{2}\delta)$
* Write a function `huber_loss(y_true, y_pred, delta=1.0)`.

## Q3 (NAT)
**Problem:** You have a Cost Function $J(w) = (w - 3)^2 + 5$. What is the value of $w$ that minimizes this cost?

## Q4 (MSQ)
**Problem:** Which of the following statements about **Optimization** are true?
A. Gradient Descent is an iterative optimization algorithm.
B. The "Normal Equation" is an analytical optimization method (solves in one step).
C. Stochastic Gradient Descent is generally smoother and more stable than Batch Gradient Descent.
D. A Learning Rate of 0 means the model will never learn (weights won't change).

## Q5 (Coding)
**Problem:** Write a function `compute_gradients(X, y, w)` for Linear Regression (MSE Cost).
* Formula: $\nabla w = \frac{2}{n} X^T (Xw - y)$
* Assume $X, y, w$ are numpy arrays. Return the gradient vector.

## Q6 (Subjective)
**Problem:** Compare **MSE** (L2) and **MAE** (L1) as cost functions. Why do we almost always use MSE for introductory Linear Regression instead of MAE, despite MAE being more robust to outliers? (Hint: Think about Calculus/Derivatives).
