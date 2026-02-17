# Lecture Script: Gradient Descent Algorithm

## Topic Breakdown

### 1. Why do we need an algorithm?
* **Instructor Note:** Draw a U-shaped curve (Cost Function). Place a dot (Current Weight) high up on the curve.
* **Why:** For simple Linear Regression, we *can* solve it directly using algebra (Normal Equation). But as soon as we have millions of data points or move to complex models (like Neural Networks), algebra becomes too slow or impossible. Gradient Descent is the universal solver.

### 2. What is the Math?
* **The Goal:** Minimize $J(w, b)$ (The Cost Function).
* **The Gradient:** $\frac{\partial J}{\partial w}$. This is the "slope" of the cost curve at our current point.
    * If slope is positive ($+$), we need to go left (decrease $w$).
    * If slope is negative ($-$), we need to go right (increase $w$).
* **The Update Rule:**
    $$w_{new} = w_{old} - \alpha \times \frac{\partial J}{\partial w}$$
    * $\alpha$ (Alpha) is the **Learning Rate**.
    * The minus sign ensures we always go *opposite* to the slope (downhill).

### 3. How do we implement it?
* **Method:** A simple `for` loop updating weights.
* **Code Example:**
    ```python
    # Simple Gradient Descent for y = (w * x) (assuming b=0 for simplicity)
    
    w = 0.0          # Initial guess
    learning_rate = 0.01
    
    # Data: x=1, y=2 (Target is w=2)
    x = 1
    y_true = 2
    
    for i in range(50):
        y_pred = w * x
        loss = (y_pred - y_true)**2
        
        # Derivative of Loss w.r.t w: 2 * (pred - true) * x
        gradient = 2 * (y_pred - y_true) * x
        
        # Update Step
        w = w - (learning_rate * gradient)
        
        print(f"Step {i}: w={w:.2f}, Gradient={gradient:.2f}")
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Gradient Descent Simulator](https://u.aryabhat.com/gd-sim)
