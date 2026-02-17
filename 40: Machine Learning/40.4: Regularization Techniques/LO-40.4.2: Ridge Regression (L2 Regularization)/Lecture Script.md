# Lecture Script: Ridge Regression (L2 Regularization)

## Topic Breakdown

### 1. Why "Ridge"?
* **Instructor Note:** Draw a mountain ridge (long, narrow peak).
* **Why:** In statistics, if two features are highly correlated (multicollinearity), the "Loss Landscape" looks like a long, flat valley. The optimization algorithm (Gradient Descent) gets confused and drifts around, causing weights to explode.
* **The Fix:** Ridge Regression adds a penalty that turns this flat valley into a nice, deep bowl. It stabilizes the solution.

### 2. The Math of L2
* **Formula:**
    $$J(w) = \text{MSE} + \lambda ||w||_2^2$$
    * $||w||_2^2 = w_1^2 + w_2^2 + ... + w_n^2$
* **The Shrinkage:**
    * The penalty term pulls weights *towards* zero.
    * **Crucial:** It *rarely* makes them exactly zero. It just makes them very small (e.g., 0.0001). This is a key difference from Lasso (L1).

### 3. Coding Ridge in Python
* **Method:** `sklearn.linear_model.Ridge`
* **Code Example:**
    ```python
    from sklearn.linear_model import Ridge, LinearRegression
    import numpy as np

    # Data: 2 features, highly correlated
    X = np.array([[1, 1], [2, 2], [3, 3]])
    y = np.array([2, 4, 6])

    # Standard Linear Regression (Unstable weights)
    lin = LinearRegression()
    lin.fit(X, y)
    print(f"Linear Weights: {lin.coef_}") 
    # Might be [100, -98] -> Huge weights cancelling each other out!

    # Ridge Regression (Stable weights)
    ridge = Ridge(alpha=1.0) # alpha is lambda
    ridge.fit(X, y)
    print(f"Ridge Weights: {ridge.coef_}") 
    # Likely [1.0, 1.0] -> Distributed evenly
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Ridge Regression Simulator](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html)
