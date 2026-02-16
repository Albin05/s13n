# Understanding Features and Feature Selection

## Key Concepts
* **Feature:** An input variable used in making predictions.
* **Target:** The output variable to be predicted.
* **Feature Selection:** Choosing the most relevant subset of features.

## Why Drop Features?
1.  **Improves Accuracy:** Removes misleading data (Noise).
2.  **Reduces Overfitting:** Fewer features mean less opportunity to learn random patterns.
3.  **Reduces Training Time:** Fewer columns to process.
4.  **Improves Interpretability:** Easier to explain a model with 5 inputs than 500.

## Types of Selection Methods

| Method | Description | Example | Speed | Accuracy |
| :--- | :--- | :--- | :--- | :--- |
| **Filter** | Uses statistical tests to score features. Independent of the model. | Correlation, Chi-Square, Variance Threshold | Fast | Low/Medium |
| **Wrapper** | Uses a predictive model to evaluate feature subsets. | Recursive Feature Elimination (RFE) | Slow | High |
| **Embedded** | Performs selection as part of the model construction process. | Lasso (L1), Decision Trees | Medium | High |

## Common Pitfalls
* **Multicollinearity:** Two features that are highly correlated (e.g., "Temperature in C" and "Temperature in F") provide redundant information. One should be removed.
* **Data Leakage:** Selecting features using the *entire* dataset (including Test set) instead of just the Training set.

## Visual Summary
!
