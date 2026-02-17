# Adjusting Slope and Intercept

## The Geometry of Adjustment

### 1. Vertical Shift (Intercept $\theta_0$)
* **Mathematical Operation:** $y_{new} = y_{old} + \delta$
* **Geometric Effect:** Translation along the Y-axis.
* **When to adjust:** If the **Mean Error** is non-zero (e.g., the line is consistently below the data cloud).

### 2. Rotation (Slope $\theta_1$)
* **Mathematical Operation:** $y_{new} = y_{old} + \delta \cdot x$
* **Geometric Effect:** Rotation around the Y-intercept $(0, \theta_0)$.
* **When to adjust:** If the error varies systematically with $x$ (e.g., error is positive for small $x$ but negative for large $x$). This indicates the "trend" is wrong.

## The Interaction
* Often, adjusting one requires adjusting the other.
* *Example:* If you rotate the line (Slope) to match the trend, the left side of the line might dip too low. You then need to raise the line (Intercept) to fix the position.
* **Gradient Descent** adjusts both simultaneously to find the optimal combination.

## Visual Summary
