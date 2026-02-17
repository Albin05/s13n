# Introduction to Regularization

## Definition
**Regularization** is any modification to a learning algorithm that is intended to reduce its generalization error (Test Error) but not its training error.

## The Bias-Variance Tradeoff
* **Overfitting (High Variance):** The model captures noise. It works perfectly on Train data but fails on Test data.
* **Underfitting (High Bias):** The model is too simple to capture the underlying pattern.
* **Regularization Goal:** Increase Bias slightly (simplify the model) to drastically reduce Variance (prevent overfitting).

## The Modified Cost Function
$$J_{reg}(\theta) = J_{orig}(\theta) + \lambda \Omega(\theta)$$
1.  **$J_{orig}$:** The original loss (e.g., MSE). Measures "Fit".
2.  **$\lambda$ (Lambda/Alpha):** The Regularization Strength.
    * $\lambda = 0$: No regularization (Standard Regression).
    * $\lambda \to \infty$: Penalty is infinite; all weights become 0 (Horizontal line).
3.  **$\Omega(\theta)$:** The Penalty Term. Usually a function of the weights.

## Occam's Razor
"Entities should not be multiplied beyond necessity."
In ML terms: Given two models with similar errors, the simpler one (smaller weights) is usually better.

## Visual Summary
