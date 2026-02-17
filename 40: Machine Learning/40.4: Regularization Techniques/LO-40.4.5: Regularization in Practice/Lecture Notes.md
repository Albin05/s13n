# Regularization in Practice

## The Golden Rule
**NEVER** apply Regularization without **Feature Scaling** (Standardization).
* **Reason:** The penalty term ($\sum w^2$ or $\sum |w|$) is sensitive to the scale of the input features.
* **Consequence:** Unscaled features with small ranges (e.g., 0.0 to 0.1) will require large weights, which will be unfairly penalized. Features with large ranges (e.g., 0 to 1,000) will have tiny weights and escape penalization.

## Model Selection Guide
Which technique should I use?
1.  **Ridge (L2):** The safe default. Use it if you believe most features are useful or if features are correlated.
2.  **Lasso (L1):** Use it if you suspect many features are irrelevant noise (Feature Selection) or if you need a sparse, interpretable model.
3.  **Elastic Net:** Use it if you have millions of features, or if Lasso is behaving erratically (e.g., picking 1 out of 5 identical features).

## Finding the Best Lambda ($\alpha$)
We cannot know the best regularization strength in advance. We must tune it.
* **`RidgeCV` / `LassoCV`:** Efficient implementations that perform Cross-Validation automatically to find the best alpha from a list.
* **Range:** usually try powers of 10: `[0.001, 0.01, 0.1, 1, 10, 100]`.

## Implementation Pattern
Always wrap regularization in a Pipeline:
```python
model = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', RidgeCV(alphas=[0.1, 1.0, 10.0]))
])
