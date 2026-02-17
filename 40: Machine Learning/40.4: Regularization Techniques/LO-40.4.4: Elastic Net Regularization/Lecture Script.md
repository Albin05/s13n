# Lecture Script: Elastic Net Regularization

## Topic Breakdown

### 1. Why do we need a third option?
* **Instructor Note:** Draw a scenario with two identical features ($x_1 = x_2$).
    * **Lasso:** Will pick $x_1$ and drop $x_2$ (randomly). This is unstable.
    * **Ridge:** Will pick both $x_1$ and $x_2$ with equal weights. This is stable but doesn't remove useless features.
* **Why:** We want the sparsity of Lasso (remove noise) but the stability of Ridge (group correlated features). Elastic Net does exactly this.

### 2. The Math of Combination
* **Formula:**
    $$J(w) = \text{MSE} + \alpha \cdot \rho \cdot ||w||_1 + \frac{\alpha(1-\rho)}{2} \cdot ||w||_2^2$$
    * Note: Scikit-Learn uses `alpha` for total strength and `l1_ratio` ($\rho$) for the mix.
* **Geometry:**
    * Ridge = Circle.
    * Lasso = Diamond.
    * Elastic Net = A "rounded" diamond. It has corners (sparsity) but curved sides (stability).

### 3. Coding Elastic Net
* **Method:** `sklearn.linear_model.ElasticNet`
* **Code Example:**
    ```python
    from sklearn.linear_model import ElasticNet
    import numpy as np

    # Data: Correlated features
    X = np.array([[1, 1], [2, 2], [3, 3]])
    y = np.array([2, 4, 6])

    # Elastic Net
    # alpha=1.0 (Strength), l1_ratio=0.5 (50% Lasso, 50% Ridge)
    enet = ElasticNet(alpha=0.1, l1_ratio=0.5)
    enet.fit(X, y)
    
    print(f"Weights: {enet.coef_}")
    # Output: [0.98, 0.98] -> Keeps both (Ridge behavior) but shrinks them (Lasso behavior).
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Regularization Comparator](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)
