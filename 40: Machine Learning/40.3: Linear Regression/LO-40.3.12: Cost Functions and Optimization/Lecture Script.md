# Lecture Script: Cost Functions and Optimization

## Topic Breakdown

### 1. Why do we need a "Function" for Cost?
* **Instructor Note:** Ask students, "Is it better to miss by 10 meters once, or by 1 meter ten times?"
* **Why:** We need a single metric to optimize. The choice of *how* we calculate this metric determines the behavior of the model.
    * If we use **MSE (L2 Cost)**, we tell the model: "Big errors are unacceptable."
    * If we use **MAE (L1 Cost)**, we tell the model: "All errors are equal."

### 2. What is the Landscape?
* **The Cost Surface:**
    * Imagine plotting the Cost ($J$) on the Z-axis against the Weights ($w$) on the X-axis.
    * For Linear Regression, this shape is a **Parabola** (in 2D) or a **Bowl** (in 3D). This property is called **Convexity**.
    * **Crucial Insight:** Because it is Convex, no matter where we start (random initialization), Gradient Descent will always roll down to the same Global Minimum. We cannot get "stuck."

### 3. How do we code a Cost Function?
* **Method:** Define a function that takes `y_true` and `y_pred` and returns a scalar.
* **Code Example:**
    Comparing L1 vs L2 Cost.

    ```python
    import numpy as np

    # Data
    y_true = np.array([10, 20, 30])
    y_pred = np.array([12, 18, 35]) # Last one is a big error

    def cost_l1(true, pred):
        # Mean Absolute Error
        return np.mean(np.abs(true - pred))

    def cost_l2(true, pred):
        # Mean Squared Error (Standard for LinReg)
        return np.mean((true - pred)**2)

    print(f"L1 Cost: {cost_l1(y_true, y_pred)}") # (2 + 2 + 5) / 3 = 3.0
    print(f"L2 Cost: {cost_l2(y_true, y_pred)}") # (4 + 4 + 25) / 3 = 11.0
    ```
    *Notice how L2 Cost is much higher because of that one big error (35 vs 30).*

* **Visual Aid:**
    !

* **Demo URL:**
    [Loss Function Landscape Explorer](https://losslandscape.com/)
