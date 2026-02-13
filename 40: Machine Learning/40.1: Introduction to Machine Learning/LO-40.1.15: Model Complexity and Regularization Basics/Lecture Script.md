# Lecture Script: Model Complexity and Regularization

## Topic Breakdown

### 1. Why do we need Regularization?
* **Instructor Note:** Recall Overfitting. Show a graph with a polynomial of degree 100 passing through every single dot.
* **Why:** Complex models have "High Variance." They are unstable. To fix this, we could just remove features (simplify manually), but that might lose information. Instead, we use math to *automatically* keep the model simple.

### 2. What is Regularization?
* **Definition:** It is the process of adding a "penalty" for complexity to the model's cost function.
    $$Cost = Error(Data) + \lambda \times Complexity(Model)$$
* **The Penalty ($\lambda$):**
    * If $\lambda$ is zero, we get the standard complex model.
    * If $\lambda$ is very high, the model becomes too simple (Underfitting).
* **Types:**
    * **L1 (Lasso):** Penalizes the *absolute* value of weights ($|w|$). Can drive weights to exactly zero (Feature Selection).
    * **L2 (Ridge):** Penalizes the *squared* value of weights ($w^2$). Shrinks weights near zero but rarely *exactly* zero.

### 3. How do we implement it?
* **Method:** In libraries like Scikit-Learn, we simply switch from `LinearRegression` to `Ridge` or `Lasso`.
* **Code Example:**
    ```python
    from sklearn.linear_model import Ridge, Lasso

    # Standard Linear Regression (No Regularization)
    # model = LinearRegression()

    # Ridge Regression (L2 Regularization)
    # alpha is the parameter lambda
    ridge_model = Ridge(alpha=1.0) 
    ridge_model.fit(X_train, y_train)

    # Lasso Regression (L1 Regularization)
    lasso_model = Lasso(alpha=0.1)
    lasso_model.fit(X_train, y_train)
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Regularization Playground](https://example.com/regularization-playground)
