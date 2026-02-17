# Lasso Regression (L1 Regularization)

## Concept
**Lasso Regression** (Least Absolute Shrinkage and Selection Operator) is similar to Ridge Regression, but with a crucial difference in the penalty term.
* **Ridge (L2):** Penalizes the *square* of the weights ($w^2$).
* **Lasso (L1):** Penalizes the *absolute value* of the weights ($|w|$).

$$Cost = \text{MSE} + \lambda \sum_{j=1}^{p} |w_j|$$

## The Superpower: Feature Selection
While Ridge shrinks coefficients to be *very small*, Lasso has the unique ability to shrink coefficients all the way to **exactly zero**.
* If a feature is irrelevant (e.g., "User's favorite color" for predicting "House Price"), Lasso will set its weight to 0, effectively removing it from the model.
* This makes Lasso an automatic **Feature Selection** tool.

## Real-World Analogy: The Budget Cut
Imagine a company needs to cut costs.
* **Ridge Approach:** Everyone takes a 10% salary cut. (Everyone stays, but costs are lower).
* **Lasso Approach:** We fire the 3 least productive employees completely. (Some people are removed entirely).

## Visualization


## External Resources
* [Article: Ridge vs Lasso Regression](https://example.com/ridge-vs-lasso)
* [Video: Why Lasso sets coefficients to zero](https://example.com/lasso-sparsity-video)
