# The Linear Equation

## ML Notation
$$h_\theta(x) = \theta_0 + \theta_1 x$$
* $h_\theta(x)$: Hypothesis function (Prediction).
* $\theta$ (Theta): The parameters (weights) the model learns.

## 1. The Slope ($\theta_1$)
Also known as the **Weight** ($w$).
* **$\theta_1 > 0$:** Positive correlation (Both go up).
* **$\theta_1 < 0$:** Negative correlation (One goes up, other goes down).
* **$\theta_1 = 0$:** No correlation (Horizontal line).
* **Magnitude:** Steeper line = Stronger relationship.

## 2. The Intercept ($\theta_0$)
Also known as the **Bias** ($b$).
* **Role:** Offsets the prediction.
* **Why it matters:** If we force the line through $(0,0)$, we introduce huge bias for datasets that naturally start elsewhere (e.g., Temperature in Kelvin never hits 0 in normal conditions).

## Calculating Slope manually
Given two points $(x_1, y_1)$ and $(x_2, y_2)$:
$$m = \frac{y_2 - y_1}{x_2 - x_1}$$

## Visual Summary
