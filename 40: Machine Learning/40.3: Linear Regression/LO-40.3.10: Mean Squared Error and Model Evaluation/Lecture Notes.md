# Mean Squared Error and Model Evaluation

## The Residual
The difference between the actual value ($y$) and the predicted value ($\hat{y}$) for a single data point.
$$e_i = y_i - \hat{y}_i$$

## Comparison of Metrics

| Metric | Formula | Description | Unit | Sensitivity to Outliers |
| :--- | :--- | :--- | :--- | :--- |
| **MAE** (Mean Absolute Error) | $\frac{1}{n}\sum |y_i - \hat{y}_i|$ | Average magnitude of errors. | Same as $y$ | Low |
| **MSE** (Mean Squared Error) | $\frac{1}{n}\sum (y_i - \hat{y}_i)^2$ | Average of squared errors. | Unit Squared ($y^2$) | **High** |
| **RMSE** (Root Mean Sq. Error) | $\sqrt{MSE}$ | Root of MSE. Interpretable like MAE but penalizes large errors. | Same as $y$ | **High** |
| **$R^2$** (Coefficient of Determination) | $1 - \frac{SS_{res}}{SS_{tot}}$ | Proportion of variance explained by the model. | None (Percentage) | Medium |

## Interpreting $R^2$
* **$R^2 = 1$:** Perfect prediction.
* **$R^2 = 0$:** The model is as bad as just predicting the average $\bar{y}$.
* **$R^2 < 0$:** The model is *worse* than predicting the average (the predictions are completely wrong).

## Why Square the Errors?
1.  **Removes Negatives:** $(y - \hat{y})^2$ is always positive.
2.  **Penalizes Large Errors:** If error doubles (2x), the penalty quadruples (4x). This forces the model to focus on fixing the "worst" predictions.

## Visual Summary
