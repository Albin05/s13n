# Lecture Script: The Linear Equation

## Topic Breakdown

### 1. Why do we obsess over this one equation?
* **Instructor Note:** Write $y = mx + c$ and $y = \beta_0 + \beta_1 x$ on the board.
* **Why:** This simple equation is the building block of deep learning. A neuron in a neural network is essentially just a linear equation passed through an activation function. Understanding how $\theta_0$ shifts the line and $\theta_1$ rotates it is crucial for understanding how models "learn."

### 2. The Role of Slope ($\theta_1$)
* **Definition:** Rate of change ($\Delta y / \Delta x$).
* **Intuition:** "Sensitivity."
    * High Slope: A small change in input ($x$) causes a huge change in output ($y$). The output is very sensitive to the input.
    * Low Slope: A change in input barely affects output.
    * Zero Slope: Input is irrelevant to output.

### 3. The Role of Intercept ($\theta_0$)
* **Definition:** The value when $x=0$.
* **Intuition:** "Bias."
    * It allows the line to move up and down. Without an intercept, every line would be forced to pass through the origin $(0,0)$.
    * *Example:* Predicting Grade based on Hours Studied. Even with 0 hours, a student might get 20 marks just by guessing. That 20 is the Intercept.

### 4. Code Example: Visualizing Parameters
* **Method:** Plot multiple lines to see the effect.
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0, 10, 100)

    # 1. Changing Intercept (Shift Up/Down)
    plt.plot(x, 1*x + 0, label='Intercept=0')
    plt.plot(x, 1*x + 5, label='Intercept=5')

    # 2. Changing Slope (Rotate)
    plt.plot(x, 0.5*x, label='Slope=0.5 (Flat)')
    plt.plot(x, 2.0*x, label='Slope=2.0 (Steep)')

    plt.legend()
    plt.show()
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Desmos Linear Explorer](https://www.desmos.com/calculator/linear)
