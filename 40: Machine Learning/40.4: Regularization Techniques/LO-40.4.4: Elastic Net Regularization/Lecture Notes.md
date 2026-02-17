# Elastic Net Regularization

## The Hybrid Approach
Elastic Net linearly combines the L1 and L2 penalties.

## Parameters
1.  **Alpha ($\alpha$):** Total regularization penalty.
    * If $\alpha=0$, it becomes Linear Regression.
2.  **L1 Ratio ($\rho$):** Mixing parameter.
    * $0 \le \rho \le 1$.
    * If $\rho=1$, it is Lasso.
    * If $\rho=0$, it is Ridge.

## Use Cases
* **High-Dimensional Data:** When $p > n$ (more features than samples), Lasso behaves erratically. Elastic Net is preferred.
* **Grouped Variables:** If there is a group of highly correlated variables, Lasso tends to select one and ignore the rest. Elastic Net selects the whole group (Grouping Effect).

## Pros & Cons
* **Pros:**
    * Handles multicollinearity better than Lasso.
    * Performs feature selection better than Ridge.
* **Cons:**
    * Two hyperparameters to tune ($\alpha$ and $\rho$) instead of one, making Grid Search computationally more expensive.

## Visual Summary
