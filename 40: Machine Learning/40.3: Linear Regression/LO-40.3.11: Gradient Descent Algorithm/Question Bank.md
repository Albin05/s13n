# Question Bank: Gradient Descent

## Q1 (MCQ)
**Problem:** Which of the following statements about the Cost Function $J(w)$ for Linear Regression is true?
A. It is a convex function (bowl-shaped), ensuring only one global minimum.
B. It is non-convex, meaning Gradient Descent can get stuck in local minima.
C. It has multiple global minima.
D. Gradient Descent cannot be applied to it.

## Q2 (Coding)
**Problem:** Write a function `update_weight(w, gradient, learning_rate)` that performs a single step of Gradient Descent and returns the new weight.
**Input:** `w=10`, `gradient=2`, `lr=0.1`
**Output:** `9.8`

## Q3 (NAT)
**Problem:** You are minimizing a function $J(w) = w^2$.
* Current $w = 5$.
* Gradient at $w=5$ is $10$.
* Learning Rate $\alpha = 0.2$.
Calculate the value of $w$ after **one** update step.

## Q4 (MSQ)
**Problem:** Which of the following techniques can help if Gradient Descent is converging too slowly?
A. Increasing the Learning Rate (carefully).
B. Feature Scaling (Standardization).
C. Decreasing the Learning Rate significantly.
D. Using Stochastic Gradient Descent instead of Batch (for faster iterations).

## Q5 (Coding)
**Problem:** Implement a training loop for 100 epochs.
1.  Initialize `w = 0`.
2.  In each epoch, assume `gradient = (w - 5)`. (This assumes optimal w is 5).
3.  Update `w` with `lr = 0.1`.
4.  Print the final `w`.

## Q6 (Subjective)
**Problem:** Explain the difference between **Batch Gradient Descent** and **Stochastic Gradient Descent** in terms of:
1.  Computation time per step.
2.  Stability of the path towards the minimum.
