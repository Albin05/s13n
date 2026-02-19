# Deriving the Logistic Regression Equation

## The Composition of Functions
Logistic Regression is built by composing two mathematical functions:
1.  **Linear Function:** $z = \theta_0 + \theta_1 x_1 + \dots + \theta_n x_n = \theta^T x$
2.  **Sigmoid (Logistic) Function:** $g(z) = \frac{1}{1 + e^{-z}}$

## The Hypothesis Equation
By substituting the linear function into the Sigmoid function, we get the fundamental hypothesis for Logistic Regression:
$$h_\theta(x) = \frac{1}{1 + e^{-\theta^T x}}$$

## Probabilistic Interpretation
The output of $h_\theta(x)$ is not a direct class label. It is a conditional probability.
$$h_\theta(x) = P(y=1 | x ; \theta)$$
* "The probability that $y=1$, given $x$, parameterized by $\theta$."
* Since probabilities must sum to 1, the probability of the negative class is:
    $$P(y=0 | x ; \theta) = 1 - P(y=1 | x ; \theta)$$

## Making a Prediction
To output a final discrete class ($0$ or $1$), we apply a **Decision Threshold** (commonly $0.5$).
* Predict $y = 1$ if $h_\theta(x) \ge 0.5$
* Predict $y = 0$ if $h_\theta(x) < 0.5$

## Code Snippet: The Hypothesis in Python
```python
import numpy as np

def predict_proba(X, theta):
    z = np.dot(X, theta)
    return 1 / (1 + np.exp(-z))
