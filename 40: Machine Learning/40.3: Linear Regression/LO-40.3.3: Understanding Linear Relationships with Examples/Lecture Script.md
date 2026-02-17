# Lecture Script: Understanding Linear Relationships

## Topic Breakdown

### 1. Why do we start with "Lines"?
* **Instructor Note:** Draw a scatter plot that looks like a cloud (no pattern). Draw another that looks like a snake (curve). Draw one that looks like a line.
* **Why:** The straight line is the simplest possible pattern in the universe. "If I double X, Y doubles." It is the foundation of almost all physics and economics. Before we try complex curves (Neural Networks), we must master the line.

### 2. What defines a Linear Relationship?
* **Constant Rate of Change:**
    * If I study for 1 hour, my grade goes up by 5 points.
    * If I study for 2 hours, my grade goes up by 10 points.
    * The *rate* (5 points/hour) stays the same.
* **The Equation ($y = mx + c$):**
    * **$m$ (Slope):** The rate. Positive $m$ means they grow together (Height vs Weight). Negative $m$ means one goes up, the other goes down (Speed vs Time to Destination).
    * **$c$ (Intercept):** The starting point.

### 3. How do we visualize it?
* **Method:** We use Scatter Plots.
* **Code Example:**
    Generating and plotting linear data.

    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    # Generate X values (0 to 10)
    X = np.linspace(0, 10, 20)
    
    # Generate Y values with a formula: y = 3x + 7
    # We add some random 'noise' because real life isn't perfect
    noise = np.random.normal(0, 2, 20) 
    y = (3 * X + 7) + noise

    plt.scatter(X, y, label='Data')
    plt.plot(X, 3*X + 7, color='red', label='True Line')
    plt.legend()
    plt.show()
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Desmos Graphing Calculator](https://www.desmos.com/calculator/jwquvmikhr) - *Let students play with $m$ and $c$ sliders.*
