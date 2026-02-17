# Lecture Script: Moving Lines

## Topic Breakdown

### 1. How does the machine "learn" the line?
* **Instructor Note:** Open an interactive graphing tool (like Desmos). Start with a line $y = 1x + 0$ that clearly misses the data points.
* **Step 1 (The Bias):** "Look, all our points are way above the line. We need to lift the line up." *Increase Intercept*. Now the line is in the middle of the cloud, but the angle is wrong.
* **Step 2 (The Weight):** "The line is too flat. For high X, our prediction is too low. For low X, it's too high. We need to tilt it." *Increase Slope*.
* **Conclusion:** Learning is just automating this wiggle process.

### 2. Independent Movements
* **Translation (Intercept):** Changing $c$ moves the line parallel to itself.
    * $y = 2x + 1$ and $y = 2x + 5$ are parallel.
* **Rotation (Slope):** Changing $m$ spins the line around the intercept point $(0, c)$.
    * $y = 1x + 0$ and $y = 5x + 0$ intersect at the origin.

### 3. Coding the Animation
* **Method:** We can create a loop that slightly updates $m$ and $c$ and plots the result to simulate "learning."
* **Code Example:**
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 5, 4, 5]) # True Data

    # Initial Guess
    m = 0.1
    c = 0.0

    # Simulation of "Learning" steps
    for i in range(5):
        y_pred = m * x + c
        print(f"Step {i}: Line is y = {m:.1f}x + {c:.1f}")
        
        # Manually adjusting to get closer (heuristic)
        m += 0.2  # Rotating up
        c += 0.5  # Shifting up
    ```

* **Visual Aid:**
    [Image of sequence of 3 graphs showing a line progressively getting closer to data points]

* **Demo URL:**
    [Desmos Slider Demo](https://www.desmos.com/calculator/epnzvpwzmw) - *Allow students to move sliders `m` and `b` to fit a set of points.*
