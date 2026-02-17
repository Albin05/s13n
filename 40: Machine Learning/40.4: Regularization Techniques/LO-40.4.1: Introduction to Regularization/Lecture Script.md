# Lecture Script: Introduction to Regularization

## Topic Breakdown

### 1. The "Wiggly" Line Problem
* **Instructor Note:** Draw a scatter plot with 5 points.
    * *Model 1:* A straight line that misses a few points (Simple).
    * *Model 2:* A crazy squiggly line that touches every single point perfectly (Complex).
* **Ask:** "Which model has zero error?" (Model 2). "Which model would you trust to predict a new point?" (Model 1).
* **Why:** Model 2 has **Overfitted**. It learned the *noise* of the data, not the *signal*. It has high variance. We need a way to punish this wiggliness.

### 2. How do we punish complexity?
* **Concept:** In Linear Regression ($y = w_1x_1 + w_2x_2 + ...$), "Complexity" usually comes from having **large weights** ($w$).
    * If $w$ is huge, a tiny change in input causes a massive change in output (instability/wiggliness).
* **The Fix:** We change the game. Instead of just minimizing MSE, we minimize:
    $$Cost = MSE + \lambda \times (\text{Size of Weights})$$
    * **$\lambda$ (Lambda):** The "Strictness" of the penalty.
* **Mechanism:**
    * If the model sets $w=1,000,000$ to fit one outlier, the penalty becomes huge. The optimizer decides it's "too expensive" and lowers $w$, effectively smoothing out the line.

### 3. Code Demo: Visualizing the Penalty
* **Method:** We will simulate a cost calculation.
* **Code Example:**
    ```python
    import numpy as np

    # Weights for two models
    w_simple = np.array([0.5, 0.2])   # Small weights
    w_complex = np.array([100, -50])  # Huge weights (Overfitted)

    # Assume both have similar prediction error for now
    mse_error = 5.0 

    # Regularization Parameter
    lambda_val = 0.1

    def total_cost(w, error, lambd):
        # Penalty: Sum of absolute values of weights (L1 style)
        penalty = np.sum(np.abs(w))
        return error + (lambd * penalty)

    cost_simple = total_cost(w_simple, mse_error, lambda_val)
    cost_complex = total_cost(w_complex, mse_error, lambda_val)

    print(f"Simple Cost: {cost_simple}")   # 5 + 0.07 = 5.07
    print(f"Complex Cost: {cost_complex}") # 5 + 15.0 = 20.0
    ```
    *Observation:* Even though the MSE was the same, the algorithm now hates the complex model because of the penalty!

* **Visual Aid:**
    

* **Demo URL:**
    [Regularization Playground](https://developers.google.com/machine-learning/crash-course/regularization-for-simplicity/playground-exercise)
