# Ridge Regression (L2 Regularization)

## The Objective Function
Minimize:
$$J(\theta) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} \theta_j^2$$

## Key Properties
1.  **Shrinkage:** Coefficients shrink towards zero but never reach exactly zero. All features are kept in the model.
2.  **Multicollinearity Handling:**
    * If features $A$ and $B$ are identical, standard regression might assign weights $w_A=100, w_B=-99$ (unstable).
    * Ridge will assign $w_A=0.5, w_B=0.5$ (stable).
3.  **Differentiability:** The penalty term $w^2$ is a smooth parabola. It is fully differentiable everywhere, making it easy to optimize with Gradient Descent.

## Hyperparameter $\lambda$ (Alpha)
* **$\lambda = 0$:** Same as Linear Regression (No penalty).
* **$\lambda \to \infty$:** All weights approach 0 (Underfitting / Horizontal Line).
* **Selection:** We must use Cross-Validation to find the optimal $\lambda$.

## When to use Ridge?
* When you have many features.
* When you suspect features are correlated (Multicollinearity).
* When you want to prevent overfitting but keep all features in the model.

## Visual Summary
