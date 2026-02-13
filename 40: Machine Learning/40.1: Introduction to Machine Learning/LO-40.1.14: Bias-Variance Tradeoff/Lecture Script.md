# Lecture Script: Bias-Variance Tradeoff

## Topic Breakdown

### 1. Why is this a "Tradeoff"?
* **Instructor Note:** Use the "Balloon" analogy. If you squeeze one side of a balloon (Bias), the air moves to the other side (Variance). You can't just eliminate error; you often just shift where it comes from.
* **Why:** We cannot simultaneously minimize both to zero in complex real-world scenarios. We must find the "sweet spot" that minimizes the **Total Error**.
    $$Total Error = Bias^2 + Variance + Irreducible Error$$

### 2. What are Bias and Variance?
* **Bias (Assumption Error):**
    * **Definition:** Simplifying assumptions made by a model to make the target function easier to learn.
    * **Example:** Linear Regression assumes data is a straight line. If data is curved, Bias is high.
* **Variance (Sensitivity Error):**
    * **Definition:** How much the model *changes* if we train it on a slightly different dataset.
    * **Example:** Decision Trees can change completely if you change just one data point. Variance is high.

### 3. How do we manage the Tradeoff?
* **Method:** We adjust Model Complexity.
    * **Increase Complexity (e.g., Deep Neural Net):** Bias $\downarrow$, Variance $\uparrow$.
    * **Decrease Complexity (e.g., Linear Regression):** Bias $\uparrow$, Variance $\downarrow$.
* **Code Example:**
    Visualizing the tradeoff using polynomial degrees.

    ```python
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures

    # Simple Model (High Bias)
    # Uses Degree 1: Assumes straight line.
    model_simple = LinearRegression()

    # Complex Model (High Variance)
    # Uses Degree 20: Tries to hit every single point.
    poly = PolynomialFeatures(degree=20)
    X_poly = poly.fit_transform(X)
    model_complex = LinearRegression().fit(X_poly, y)
    ```

* **Visual Aid:**
    ![S3 Image: Graph showing Total Error curve as the sum of Bias^2 and Variance curves]

* **Demo URL:**
    [Bias-Variance Interactive Simulator](https://example.com/bias-variance-sim)
