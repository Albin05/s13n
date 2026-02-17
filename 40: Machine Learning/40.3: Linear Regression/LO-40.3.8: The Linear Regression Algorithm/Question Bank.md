# Question Bank: Linear Regression Algorithm

## Q1 (MCQ)
**Problem:** In the update rule $w_{new} = w_{old} - \alpha \frac{\partial J}{\partial w}$, if the partial derivative $\frac{\partial J}{\partial w}$ is **positive**, what happens to the weight $w$?
A. It increases.
B. It decreases.
C. It stays the same.
D. It becomes zero.

## Q2 (Coding)
**Problem:** Write a function `predict(X, w, b)` that performs the "Forward Pass".
**Input:** `X` (array), `w` (scalar), `b` (scalar).
**Output:** Array of predictions.

## Q3 (NAT)
**Problem:** You run 1 epoch of training.
* $X = [2]$, $y = [10]$.
* Initial $w = 3, b = 0$.
* Learning Rate $\alpha = 0.1$.
* Gradient formula for $w$: $-2x(y - \hat{y})$ (ignoring $1/n$ for single sample).
What is the updated value of $w$?

## Q4 (MSQ)
**Problem:** Which of the following indicate that your Linear Regression algorithm has **Converged**?
A. The Cost Function $J$ is decreasing by very small amounts (e.g., $10^{-6}$) per epoch.
B. The gradient is close to zero.
C. The Learning Rate becomes zero.
D. The weights $w$ and $b$ stop changing significantly.

## Q5 (Coding)
**Problem:** Implement the **Normal Equation** using Numpy.
Formula: $\theta = (X^T X)^{-1} X^T y$.
Note: You must add a column of 1s to $X$ for the bias term.
**Input:** `X` (Feature Matrix), `y` (Target Vector).
**Output:** `theta` (Optimal weights).

## Q6 (Subjective)
**Problem:** Explain the concept of **Homoscedasticity** in Linear Regression. What would the residual plot look like if this assumption is violated (Heteroscedasticity), and why is that a problem for the model's reliability?
