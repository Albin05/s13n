# Pre-Read: Bias-Variance Tradeoff

## Concept
In supervised machine learning, prediction error consists of three parts:
1.  **Bias Error:** The error introduced by approximating a real-world problem (which may be complex) by a much simpler model. High bias can cause an algorithm to miss the relevant relations between features and target outputs (**Underfitting**).
2.  **Variance Error:** The amount that the estimate of the target function will change if different training data was used. High variance can cause an algorithm to model the random noise in the training data rather than the intended outputs (**Overfitting**).
3.  **Irreducible Error:** The error that cannot be reduced regardless of the algorithm chosen (noise in the problem itself).

## The Tradeoff
The goal of any supervised machine learning algorithm is to achieve low bias and low variance. However, these are often at odds:
* **Low Bias** usually means a more complex model (flexible).
* **Low Variance** usually means a simpler model (rigid).
Increasing complexity decreases bias but increases variance. Decreasing complexity decreases variance but increases bias.

## Real-World Analogy: The Bullseye
Imagine throwing darts at a target:
* **High Bias, Low Variance:** All darts hit the same spot, but far from the center (Consistently wrong).
* **Low Bias, High Variance:** Darts are scattered all over the board, but the average is the center (Inconsistently right).
* **Low Bias, Low Variance:** All darts hit the bullseye (Accurate and Consistent).

## Visualization
![S3 Image: Four target boards showing combinations of High/Low Bias and Variance]

## External Resources
* [Article: The Bias-Variance Tradeoff in Data Science](https://example.com/bias-variance-ds)
* [Video: Visualizing Bias and Variance](https://example.com/bias-variance-viz)
