# Question Bank: Learning Rate

## Q1 (MCQ)
**Problem:** Which plot represents a "Good" Learning Rate behavior (Loss vs Epochs)?
A. A horizontal line.
B. A curve that goes down steeply and then flattens out (Hockey stick shape).
C. A curve that goes up.
D. A curve that zig-zags wildly up and down.

## Q2 (Coding)
**Problem:** Write a function `calculate_step(gradient, lr)` that returns the value to be subtracted from the weight.
**Input:** `grad=5.0`, `lr=0.1`
**Output:** `0.5`

## Q3 (NAT)
**Problem:**
* Current Weight $w = 2.0$.
* Gradient $\nabla = -4.0$.
* Learning Rate $\alpha = 0.5$.
What is the new weight $w_{new}$?

## Q4 (MSQ)
**Problem:** Which of the following are valid strategies to handle Learning Rate?
A. Learning Rate Decay (Start high, reduce gradually).
B. Grid Search (Try 0.1, 0.01, 0.001 and pick the best).
C. Negative Learning Rate (to go uphill).
D. Adaptive Learning Rates (Algorithms that change the rate automatically per parameter).

## Q5 (Coding)
**Problem:** Simulate "Overshooting".
1.  Define a cost function $J(w) = w^2$ (Min is at 0).
2.  Start at $w=10$.
3.  Set `lr = 1.1`.
4.  Run 3 steps of Gradient Descent.
5.  Print the weights to show they are getting farther from 0 (magnitude increasing).

## Q6 (Subjective)
**Problem:** Explain the concept of **Learning Rate Decay**. Why might we want a large learning rate at the beginning of training but a very small one at the end? Use the analogy of parking a car.
