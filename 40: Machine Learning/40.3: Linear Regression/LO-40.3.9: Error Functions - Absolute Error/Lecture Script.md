# Lecture Script: Error Functions - Absolute Error

## Topic Breakdown

### 1. Why do we need "Absolute" error?
* **Instructor Note:** Ask students, "If I miss the target by 5 meters to the left, and then by 5 meters to the right, is my average error zero?"
* **Why:** Mathematically, yes ($(-5 + 5)/2 = 0$). But practically, no! I missed twice.
* **The Fix:** We apply the absolute value function $|x|$. $|-5| + |5| = 10$. Average error = 5. This reflects reality.

### 2. The Definition: Mean Absolute Error (MAE)
* **Formula:**
    $$MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
* **Key Characteristic:** It is **Linear**.
    * If the error doubles, the penalty doubles.
    * This makes MAE very intuitive. "On average, my house price prediction is off by $5,000."
* **Robustness:** MAE is less sensitive to outliers than MSE (Mean Squared Error). If one data point is wildly wrong, MAE just adds that linear error. MSE squares it, causing the model to panic.

### 3. How do we compute it?
* **Method:** Calculate residuals, take absolute value, compute mean.
* **Code Example:**
    ```python
    import numpy as np
    
    y_true = np.array([10, 20, 30])
    y_pred = np.array([12, 15, 30]) # Errors: +2, -5, 0
    
    # Step 1: Raw Errors (Residuals)
    errors = y_true - y_pred # [-2, 5, 0]
    
    # Step 2: Absolute Errors
    abs_errors = np.abs(errors) # [2, 5, 0]
    
    # Step 3: Mean
    mae = np.mean(abs_errors) # (2+5+0)/3 = 2.33
    
    print(f"MAE: {mae:.2f}")
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Error Metric Calculator](https://www.calculatorsoup.com/calculators/statistics/mean-absolute-error-calculator.php)
