# Error Functions - Absolute Error

## Definition
The **Absolute Error** for a single prediction is the magnitude of the difference between the actual value ($y$) and the predicted value ($\hat{y}$).
$$e_i = |y_i - \hat{y}_i|$$

## Mean Absolute Error (MAE)
The average of all absolute errors in the dataset.
$$MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$

## Properties of MAE
1.  **Non-Negative:** MAE $\ge 0$.
2.  **Scale-Dependent:** The unit of MAE is the same as the unit of the target variable $y$ (e.g., Dollars, Degrees Celsius).
3.  **Robust to Outliers:** Unlike Mean Squared Error (MSE), MAE does not square the error terms.
    * *Scenario:* If most errors are small, but one is huge (1,000,000), MSE will be dominated by that one error ($10^{12}$). MAE will simply add 1,000,000 to the sum, affecting the average linearly.

## Optimization Challenges
* The derivative of $|x|$ is:
    * $-1$ if $x < 0$
    * $+1$ if $x > 0$
    * **Undefined** at $x = 0$ (The "kink" at the bottom of the V-shape).
* Because the gradient doesn't get smaller as we approach zero (it stays constant at 1), Gradient Descent using MAE can have trouble settling exactly at the minimum; it tends to bounce back and forth around 0 unless the learning rate is reduced.

## Visual Summary
