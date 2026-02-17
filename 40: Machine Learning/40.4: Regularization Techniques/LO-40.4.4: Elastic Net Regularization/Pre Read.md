# Elastic Net Regularization

## Concept
We have learned two powerful regularization techniques:
1.  **Ridge (L2):** Good for handling multicollinearity (correlated features) and keeping all features.
2.  **Lasso (L1):** Good for feature selection (setting coefficients to zero) but struggles with correlated features (picks one randomly).

**Elastic Net** is the "best of both worlds." It combines the penalties of both Ridge and Lasso.
$$Cost = \text{MSE} + r \cdot \lambda \sum |w| + \frac{1-r}{2} \cdot \lambda \sum w^2$$

* **$\lambda$ (Alpha):** Overall regularization strength.
* **$r$ (L1 Ratio):** The balance between Lasso and Ridge.
    * $r=1$: Pure Lasso.
    * $r=0$: Pure Ridge.
    * $r=0.5$: Equal mix.

## Real-World Analogy: The Investment Portfolio
* **Ridge:** You invest a little bit in every stock to minimize risk (Diversification).
* **Lasso:** You pick the single best performing stock and dump the rest (High Risk/High Reward).
* **Elastic Net:** You pick the top 5 performing stocks and invest in them equally. You get the benefit of selection (Lasso) and the stability of diversification (Ridge).

## Visualization


## External Resources
* [Article: Elastic Net Regression](https://example.com/elastic-net)
* [Video: Regularization Part 3: Elastic Net](https://example.com/elastic-net-video)
