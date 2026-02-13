# Model Complexity and Regularization

## The Problem of Complexity
* **Complex Models:** High flexibility (e.g., high-degree polynomials).
* **Risk:** High Variance $\to$ Overfitting.
* **Goal:** Keep error low but weights small (Simple).

## The Regularized Cost Function
$$J(\theta) = \text{MSE}(\theta) + \lambda \sum |\theta|^p$$
* **MSE:** Mean Squared Error (How well it fits data).
* **Penalty Term:** $\lambda \sum |\theta|^p$ (How complex it is).
* **$\lambda$ (Lambda/Alpha):** Hyperparameter controlling regularization strength.

## L1 vs L2 Regularization

| Feature | L1 (Lasso) | L2 (Ridge) |
| :--- | :--- | :--- |
| **Penalty** | Sum of Absolute Weights ($\sum |w_i|$) | Sum of Squared Weights ($\sum w_i^2$) |
| **Effect** | Can zero out coefficients. | Shrinks coefficients towards zero. |
| **Use Case** | Feature Selection (sparse models). | Handling Multicollinearity. |
| **Geometry** | Diamond shape constraint. | Circular shape constraint. |

## Effect of Lambda ($\lambda$)
* $\lambda = 0$: No regularization (Standard OLS).
* $\lambda \to \infty$: Weights $\to 0$ (High Bias / Underfitting).

## Visual Summary
