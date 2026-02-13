# Bias-Variance Tradeoff

## The Decomposition of Error
The expected prediction error of a model can be mathematically decomposed into:
$$E[(y - \hat{f}(x))^2] = (Bias[\hat{f}(x)])^2 + Var[\hat{f}(x)] + \sigma^2$$
* **Bias:** Error due to wrong assumptions (Underfitting).
* **Variance:** Error due to sensitivity to fluctuations (Overfitting).
* $\sigma^2$: Irreducible error (Noise).

## Characteristics
| Component | High Level | Low Level | Connection to Complexity |
| :--- | :--- | :--- | :--- |
| **Bias** | Model is too simple, misses trend. | Model captures trend well. | Decreases as complexity increases. |
| **Variance** | Model is unstable, captures noise. | Model is stable/robust. | Increases as complexity increases. |

## The Sweet Spot
The optimal model complexity is where the sum of $Bias^2$ and $Variance$ is minimized.
* **Left of Sweet Spot:** High Bias, Low Variance (Underfitting).
* **Right of Sweet Spot:** Low Bias, High Variance (Overfitting).

## Visual Summary
![S3 Image: Diagram showing U-shaped Total Error curve with decreasing Bias curve and increasing Variance curve overlapping]
