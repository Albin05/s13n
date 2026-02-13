# Lecture Script: Overfitting vs Underfitting

## Topic Breakdown

### 1. Why does this matter?
* **Instructor Note:** Draw a scatter plot with a clear curve. Draw a straight line through it (bad) and a squiggly line connecting every dot (also bad).
* **Why:** A model that is 100% accurate on training data is often useless in the real world. We need to find the "Sweet Spot" where the model learns the *rule*, not the *examples*.

### 2. What are they?
* **Underfitting (High Bias):**
    * **Definition:** Model is too rigid.
    * **Symptoms:** High error on Training set, High error on Test set.
    * **Cause:** Using a linear model for non-linear data, too few features.
* **Overfitting (High Variance):**
    * **Definition:** Model is too flexible.
    * **Symptoms:** Low error on Training set, High error on Test set.
    * **Cause:** Too many features, training for too long, model too complex (e.g., deep decision tree).

### 3. How do we detect and fix them?
* **Method:** Compare Training Error vs. Testing Error.
    * $Train \approx Test \gg 0 \rightarrow$ Underfitting.
    * $Train \ll Test \rightarrow$ Overfitting.
* **Fixes:**
    * **Underfitting:** Add more features, make model more complex, train longer.
    * **Overfitting:** Get more data, simplify model, use Regularization (L1/L2), Early Stopping.

* **Code Example (Polynomial Fitting):**
    ```python
    import numpy as np
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import LinearRegression

    # Underfitting: Degree 1 (Straight line)
    model_under = LinearRegression()

    # Overfitting: Degree 15 (Wiggly curve passing through noise)
    model_over = make_pipeline(PolynomialFeatures(15), LinearRegression())
    
    # Good Fit: Degree 3 (Captures the curve)
    model_good = make_pipeline(PolynomialFeatures(3), LinearRegression())
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Interactive Overfitting Demo](https://example.com/overfitting-demo)
