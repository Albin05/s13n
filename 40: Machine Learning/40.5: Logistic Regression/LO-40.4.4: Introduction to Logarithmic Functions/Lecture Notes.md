# Introduction to Logarithmic Functions

## The Basics of Logarithms
* The logarithm is the inverse function of exponentiation.
* Equation: If $b^y = x$, then $\log_b(x) = y$.
* **Natural Logarithm ($\ln$):** The logarithm with base $e$ ($2.71828...$). In machine learning math, $\log(x)$ almost always implies $\ln(x)$.

## Properties of Logarithms
* **Product Rule:** $\log(xy) = \log(x) + \log(y)$
* **Quotient Rule:** $\log(x/y) = \log(x) - \log(y)$
* **Power Rule:** $\log(x^y) = y\log(x)$
* **Log of 1:** $\log(1) = 0$
* **Log of Base:** $\log_e(e) = 1$

## The Domain and Asymptote
* **Domain:** $x > 0$. You cannot compute the log of $0$ or a negative number.
* **Vertical Asymptote:** As $x$ approaches $0$ from the right, the function output dives to negative infinity.
  $$\lim_{x \to 0^+} \log(x) = -\infty$$

## Why ML uses $-\log(x)$
In classification, we predict probabilities ($0 \le p \le 1$). 
The function $f(p) = -\log(p)$ is heavily used in the **Cross-Entropy Cost Function** because:
1.  If the prediction $p$ is $1$ (100% accurate), the cost is $-\log(1) = 0$.
2.  If the prediction $p$ approaches $0$ (completely wrong), the cost approaches $+\infty$, heavily penalizing the model.

## NumPy Implementation
```python
import numpy as np

# Calculating natural log in Python
val = np.log(1) 
print(val) # Outputs 0.0

