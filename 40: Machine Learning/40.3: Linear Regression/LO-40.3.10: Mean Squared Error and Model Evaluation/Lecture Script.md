# Mean Squared Error and Model Evaluation

## Topic Breakdown

### 1. Why do we need Evaluation Metrics?
* **Instructor Note:** Draw two different lines through the same scatter plot. Ask students "Which line is better?". Visually, it's hard to say. We need a number.
* **Why:** "You can't improve what you don't measure." To optimize our model (Gradient Descent), we need a single number that represents "Badness" (Loss).

### 2. What are the key metrics?
* **Residual ($e$):** The difference between Truth and Prediction ($y - \hat{y}$).
* **Mean Absolute Error (MAE):** The average of absolute errors.
    * $\frac{1}{n} \sum |y - \hat{y}|$
    * *Pros:* Easy to interpret (same unit as $y$).
    * *Cons:* Doesn't punish large errors enough.
* **Mean Squared Error (MSE):** The average of squared errors.
    * $\frac{1}{n} \sum (y - \hat{y})^2$
    * *Pros:* Heavily punishes outliers (due to squaring). Differentiable (good for math).
    * *Cons:* Unit is $y^2$ (hard to interpret).
* **Root Mean Squared Error (RMSE):** The square root of MSE.
    * $\sqrt{MSE}$
    * *Pros:* Interpretable unit (same as $y$). Punishes outliers.
* **R-Squared ($R^2$):** A relative score (0 to 1).
    * How much better is your model than just predicting the Mean for everyone?

### 3. How do we calculate them?
* **Method:** Use `sklearn.metrics`.
* **Code Example:**
    ```python
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    import numpy as np

    y_true = [10, 20, 30]
    y_pred = [12, 18, 33]

    # Calculate MSE
    mse = mean_squared_error(y_true, y_pred)
    print(f"MSE: {mse}") # ((2^2) + (-2^2) + (-3^2)) / 3 = (4+4+9)/3 = 5.66

    # Calculate RMSE
    rmse = np.sqrt(mse)
    print(f"RMSE: {rmse}")

    # Calculate R2
    r2 = r2_score(y_true, y_pred)
    print(f"R2 Score: {r2}")
    ```

* **Visual Aid:**
    [Image of visual comparison between MAE and MSE geometry]

* **Demo URL:**
    [Regression Metrics Playground](https://example.com/metrics-playground)
