# Cost Functions and Optimization

## Terminology
* **Loss Function:** Calculates error for a *single* training example.
    * $L(y, \hat{y}) = (y - \hat{y})^2$
* **Cost Function ($J$):** The average of the Loss Functions over the *entire* training set.
    * $J(w, b) = \frac{1}{n} \sum L(y_i, \hat{y}_i)$

## Common Cost Functions
1.  **Mean Squared Error (L2 Loss):**
    * Used for: Linear Regression.
    * Shape: Convex (Bowl).
    * Characteristic: Sensitive to outliers (squaring magnifies large errors).
2.  **Mean Absolute Error (L1 Loss):**
    * Used for: Robust Regression.
    * Shape: V-shape.
    * Characteristic: Robust to outliers (linear penalty).

## Optimization Challenges
1.  **Convergence:** Reaching the minimum.
2.  **Learning Rate:** Step size.
3.  **Local Minima:** Getting stuck in a shallow valley (not a problem for Linear Regression, but huge problem for Neural Networks).
4.  **Saddle Points:** Flat regions where gradient is zero but it's not a minimum.

## Convexity
* A function is **Convex** if a line segment between any two points on the graph lies *above* the graph.
* **Implication:** Any local minimum is also the global minimum. This guarantees that Linear Regression always has a unique, optimal solution (assuming no perfect multicollinearity).

## Visual Summary
!
