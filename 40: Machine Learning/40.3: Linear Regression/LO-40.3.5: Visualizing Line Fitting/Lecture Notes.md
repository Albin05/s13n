# Visualizing Line Fitting

## The Geometry of Error
* **Data Point:** $(x_i, y_i)$ (Blue Dot).
* **Predicted Point:** $(x_i, \hat{y}_i)$ (Point on Red Line).
* **Residual ($e_i$):** $y_i - \hat{y}_i$ (Green Dashed Line).

## Key Visual Indicators
1.  **Good Fit:**
    * Residuals are small.
    * Residuals are randomly scattered above and below the line (no pattern).
    * The sum of squares of the green lines is minimized.
2.  **Bad Fit:**
    * Residuals are large.
    * Residuals show a pattern (e.g., all points on the left are above, all points on the right are below). This suggests a curved relationship might be needed.

## Residual Sum of Squares (RSS)
Visually, imagine drawing a square with side length equal to the residual for every point.
* **RSS:** The total area of all these squares.
* **Goal:** Minimize this total area.

## Visual Summary
