# Lecture Script: Lasso Regression (L1 Regularization)

## Topic Breakdown

### 1. Why "Lasso"?
* **Instructor Note:** Ask, "If you have 1,000 features but only 10 matter, do you want a model that uses all 1,000 slightly?"
* **Why:** We want **Sparsity**. We want a model that is interpretable. It's easier to say "House Price depends on Location and Size" (Lasso) than "House Price depends on Location, Size, and 0.001 times the paint color" (Ridge).
* **Name:** LASSO stands for "Least Absolute Shrinkage and Selection Operator".

### 2. The Math of L1
* **Formula:**
    $$J(w) = \text{MSE} + \lambda ||w||_1$$
    * $||w||_1 = |w_1| + |w_2| + ... + |w_n|$
* **The Geometry:**
    * The L1 penalty creates a "Diamond" shape constraint (squares rotated by 45 degrees).
    * When the error contours expand to hit this diamond, they are statistically likely to hit a **corner** (where one weight is 0) rather than a flat side. This forces coefficients to zero.

### 3. Coding Lasso in Python
* **Method:** `sklearn.linear_model.Lasso`
* **Code Example:**
    ```python
    from sklearn.linear_model import Lasso
    import numpy as np

    # Data: 3 features. Feature 3 is noise (random).
    X = np.array([[1, 1, 5], [2, 2, 2], [3, 3, 9]])
    y = np.array([2, 4, 6]) # y = 2 * Feature1 (Feature2 is redundant, Feature3 is noise)

    # Lasso Regression
    lasso = Lasso(alpha=0.1)
    lasso.fit(X, y)
    
    print(f"Lasso Weights: {lasso.coef_}")
    # Output might be: [1.95, 0.0, 0.0]
    # It realized Feature 2 and 3 are useless/redundant and set them to 0.
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Lasso Path Visualization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html)
