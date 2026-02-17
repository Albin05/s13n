# Lasso Regression (L1 Regularization)

## The Objective Function
Minimize:
$$J(\theta) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} |\theta_j|$$

## Key Properties
1.  **Sparsity:** Produces "Sparse Models" where many weights are exactly 0. This is useful for high-dimensional data (e.g., Genomics with 20,000 genes but only 50 patients).
2.  **Feature Selection:** Automatically identifies the most important features.
3.  **Correlation Handling:**
    * If two features are highly correlated, Lasso tends to arbitrarily select **one** and set the other to **zero**. (Ridge would shrink both together). This can be a downside if you want to know *all* relevant factors.

## Hyperparameter $\lambda$ (Alpha)
* **$\lambda = 0$:** Standard Linear Regression.
* **$\lambda$ increases:** More weights become 0. Model becomes simpler.
* **$\lambda$ too high:** All weights become 0 (Underfitting).

## Comparison with Ridge

| Feature | Lasso (L1) | Ridge (L2) |
| :--- | :--- | :--- |
| **Penalty** | Absolute Value $|w|$ | Squared Value $w^2$ |
| **Result** | Sparse coefficients (Zeros) | Small coefficients (Non-zeros) |
| **Use Case** | Feature Selection, Interpretability | Collinearity, Prediction Accuracy |
| **Solution** | No closed form (Iterative) | Closed form exists |

## Visual Summary
