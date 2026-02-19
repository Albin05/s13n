# Understanding Exponential Functions

## Euler's Number
* **Base $e$:** A mathematical constant approximately equal to $2.71828$.
* It is the base of the natural logarithm ($\ln$).

## The Function $f(x) = e^x$
This function maps any real number $x \in (-\infty, \infty)$ to a strictly positive number $y \in (0, \infty)$.

### Key Behaviors
1.  **y-intercept:** When $x = 0$, $e^0 = 1$.
2.  **Positive Inputs ($x > 0$):** Results in exponential growth. As $x \to \infty$, $e^x \to \infty$.
3.  **Negative Inputs ($x < 0$):** Results in exponential decay. A negative exponent creates a fraction ($e^{-x} = \frac{1}{e^x}$). As $x \to -\infty$, the value approaches $0$ but never becomes negative.

## The Function $f(x) = e^{-x}$
This specific form is highly relevant in machine learning (specifically in the denominator of the Sigmoid function).
* As $x$ grows large and positive, $e^{-x}$ shrinks to $0$.
* As $x$ grows large and negative, $e^{-x}$ explodes to $\infty$.

## Why it matters in Machine Learning
Linear models ($\theta^T x$) output unbound values including negative numbers. Since probability cannot be negative, applying $e^{\theta^T x}$ acts as a transformation that guarantees a strictly positive output, which is the first step in creating a probability model.

## Code Snippet
```python
import numpy as np

# Calculate e^x in Python
x = -5
result = np.exp(x)
print(result) # Output: 0.0067379...
