# The Sigmoid Function (Theory)

## The Core Concept
The Sigmoid function is a mathematical "squishing" function. It takes any real-valued number and maps it into a strict range between $0$ and $1$. This S-shaped curve is the fundamental engine of Logistic Regression.

## Mathematical Definition
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$
Where:
* $z$ is the input (usually the linear hypothesis $z = \theta^T x$).
* $e$ is Euler's number ($\approx 2.718$).

## Key Properties & Asymptotes
1.  **Range:** The output is strictly bounded: $0 < \sigma(z) < 1$. It never actually touches $0$ or $1$.
2.  **y-intercept:** When $z = 0$, $\sigma(z) = 0.5$. This represents maximum uncertainty (a $50/50$ probability).
3.  **Positive Limit:** As $z \to \infty$, $e^{-z} \to 0$, so $\sigma(z) \to \frac{1}{1+0} = 1$.
4.  **Negative Limit:** As $z \to -\infty$, $e^{-z} \to \infty$, so $\sigma(z) \to \frac{1}{\infty} = 0$.

## The Logistic Regression Hypothesis
We combine Linear Regression with the Sigmoid function to create the Logistic Regression hypothesis:
$h_\theta(x) = \sigma(\theta^T x) = \frac{1}{1 + e^{-\theta^T x}}$

This equation translates directly to: "The probability that $y=1$, given input features $x$."
