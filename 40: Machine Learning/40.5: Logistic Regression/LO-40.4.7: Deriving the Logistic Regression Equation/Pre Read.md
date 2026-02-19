# Deriving the Logistic Regression Equation

## Conceptual Explanation
We have established two core building blocks:
1.  **The Linear Boundary:** $z = \theta^T x$. This calculates a continuous score based on features and weights.
2.  **The Sigmoid Function:** $g(z) = \frac{1}{1 + e^{-z}}$. This squishes any number into a probability between $0$ and $1$.

Deriving the Logistic Regression model is simply the act of composing these two functions. We take the output of the linear model ($z$) and feed it directly into the input of the Sigmoid function. 

This results in the **Logistic Regression Hypothesis**. This hypothesis doesn't just output an arbitrary score; it outputs a specific mathematical probability: the probability that a data point belongs to the positive class (Class 1).

## The Equation
$$h_\theta(x) = \frac{1}{1 + e^{-\theta^T x}}$$

## Short Examples
* If $\theta^T x = 0$, then $h_\theta(x) = 0.5$ (50% probability).
* If $\theta^T x$ is a large positive number, $h_\theta(x)$ is close to $1$ (e.g., 99% probability).
* If $\theta^T x$ is a large negative number, $h_\theta(x)$ is close to $0$ (e.g., 1% probability).

## External Links
* [Stanford CS229: Logistic Regression](https://cs229.stanford.edu/notes2022-fall/main_notes.pdf)

## Visuals
*(Refer to S3 bucket for diagram showing the composition: Linear Model Box -> Output 'z' -> Sigmoid Box -> Output Probability)*
