# Lecture Script: Visualizing Line Fitting

## Topic Breakdown

### 1. What are we looking at?
* **Instructor Note:** Draw a scatter plot with 5 points. Draw a horizontal line. Draw a vertical line from each point to the horizontal line.
* **Why:** Students often think the error is the *perpendicular* distance to the line (shortest path). In standard Linear Regression, it is strictly the **Vertical Distance** ($y - \hat{y}$). We are predicting $y$, so we minimize error in $y$.

### 2. The concept of "Residuals"
* **Definition:** A residual is the error of a single point.
    * Positive Residual: Point is *above* the line.
    * Negative Residual: Point is *below* the line.
* **Visualizing the "Best" Line:**
    * If I tilt the line up, some residuals get smaller, some get larger.
    * The "Best" line is the one where the *squared* length of all these little vertical lines is minimized.

### 3. How do we code a visualizer?
* **Method:** Use `matplotlib` to plot the data, the line, and the error bars (residuals).
* **Code Example:**
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    # Data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1, 3, 2, 5, 4]) # Noisy data
    
    # Our Guess Line: y = 1x + 0.5
    y_pred = 1 * x + 0.5
    
    # Plot Data
    plt.scatter(x, y, color='blue', label='Data')
    
    # Plot Line
    plt.plot(x, y_pred, color='red', label='Prediction')
    
    # Plot Residuals (The vertical lines)
    for i in range(len(x)):
        plt.plot([x[i], x[i]], [y[i], y_pred[i]], color='green', linestyle='--')
        
    plt.legend()
    plt.show()
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Interactive Line Fitting](https://phet.colorado.edu/en/simulations/least-squares-regression) - *Let students move the line and watch the error squares grow/shrink.*
