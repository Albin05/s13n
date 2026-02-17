# Gradient Descent Algorithm

## Definition
Gradient Descent is a first-order iterative optimization algorithm for finding a local minimum of a differentiable function.

## The Algorithm Steps
1.  **Initialize:** Start with random values for weights ($w$) and bias ($b$).
2.  **Calculate Gradient:** Compute the derivative of the Cost Function with respect to each parameter.
    * This tells us the direction of the steepest ascent.
3.  **Update Parameters:** Move in the *opposite* direction of the gradient by a factor of the Learning Rate ($\alpha$).
    * $w := w - \alpha \frac{\partial J}{\partial w}$
    * $b := b - \alpha \frac{\partial J}{\partial b}$
4.  **Repeat:** Continue until the cost stops decreasing (Convergence).

## Variants of Gradient Descent
1.  **Batch Gradient Descent:** Uses the *entire* dataset to calculate the gradient for one step.
    * *Pros:* Stable convergence.
    * *Cons:* Very slow for large datasets.
2.  **Stochastic Gradient Descent (SGD):** Uses *one* random sample to calculate the gradient.
    * *Pros:* Very fast.
    * *Cons:* Noisy, jumps around (high variance).
3.  **Mini-Batch Gradient Descent:** Uses a small batch (e.g., 32 samples).
    * *Pros:* Best balance of speed and stability. Standard in Deep Learning.

## The Learning Rate ($\alpha$)
* **Small $\alpha$:** Converges slowly but surely.
* **Large $\alpha$:** Can overshoot the minimum and fail to converge (diverge).

## Visual Summary
