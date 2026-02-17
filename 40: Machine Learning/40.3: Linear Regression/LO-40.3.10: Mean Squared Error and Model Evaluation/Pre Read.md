# Mean Squared Error and Model Evaluation

## Concept
In Linear Regression, we draw a line through data points. But how do we know if the line is "good"? We need a way to measure the **Error** (the distance between the line and the actual data points).

The most common metric is **Mean Squared Error (MSE)**. It calculates the average of the *squared* differences between the predicted values and the actual values.
$$MSE = \frac{1}{n} \sum (y_{actual} - y_{predicted})^2$$

## Real-World Analogy: The Dartboard
Imagine you throw 3 darts at a bullseye.
* **Throw 1:** Misses by 1 inch.
* **Throw 2:** Misses by 1 inch.
* **Throw 3:** Misses by 10 inches.

If we just average the distance (Mean Absolute Error), the average miss is $\frac{1+1+10}{3} = 4$ inches.
If we square the distances (Mean Squared Error), the "score" becomes $\frac{1^2+1^2+10^2}{3} = \frac{1+1+100}{3} = 34$.
**Notice:** The MSE punishes the big mistake (10 inches) much more severely than the small mistakes. This aligns with real life: a small error is okay, but a huge error can be catastrophic.

## Visualization
[Image of regression line showing residuals and squared residuals]

## External Resources
* [Article: MSE vs MAE vs RMSE](https://example.com/regression-metrics)
* [Video: Understanding R-Squared and MSE](https://example.com/r2-mse-video)
