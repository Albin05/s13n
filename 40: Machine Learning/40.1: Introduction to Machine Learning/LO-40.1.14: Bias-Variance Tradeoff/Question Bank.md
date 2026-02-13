# Question Bank: Bias-Variance Tradeoff

## Q1 (MCQ)
**Problem:** A K-Nearest Neighbors (KNN) model with $K=1$ (considering only the single closest neighbor) typically has:
A. High Bias, Low Variance
B. Low Bias, High Variance
C. Low Bias, Low Variance
D. High Bias, High Variance

## Q2 (Coding)
**Problem:** You are given two error values: `bias_squared = 0.04` and `variance = 0.02`. If the irreducible error is `0.01`, write a function to return the `total_expected_error`.

## Q3 (NAT)
**Problem:** A model has a Bias of 4 units and a Variance of 3 units. If we increase the model complexity, the Bias drops to 2 units, but the Variance increases to $V_{new}$. If the Total Error remains exactly the same (ignoring irreducible error), what is $V_{new}$? (Note: Error = Bias$^2$ + Variance).

## Q4 (MSQ)
**Problem:** Which of the following statements are TRUE about the Bias-Variance Tradeoff?
A. High variance often leads to Overfitting.
B. High bias often leads to Underfitting.
C. The goal is to maximize bias and minimize variance.
D. Gathering more training data is a way to reduce Variance without necessarily increasing Bias.

## Q5 (Coding)
**Problem:** Implement a function `evaluate_tradeoff(bias, variance)`:
* If $bias > 0.5$ and $variance < 0.1$, return "High Bias"
* If $bias < 0.1$ and $variance > 0.5$, return "High Variance"
* Else return "Balanced"

## Q6 (Subjective)
**Problem:** Explain why "Ensemble Methods" like Random Forests (which average many Decision Trees) are effective at managing the Bias-Variance Tradeoff. Which component (Bias or Variance) do they primarily reduce compared to a single Decision Tree?
