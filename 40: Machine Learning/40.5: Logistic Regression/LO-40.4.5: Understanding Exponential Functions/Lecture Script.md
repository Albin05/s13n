# Lecture Script: Understanding Exponential Functions

## Topic: The Mathematical Bridge to Probabilities

### Why (Importance)
Recall our problem with Linear Regression: the equation $z = \theta^T x$ draws a straight line that goes from negative infinity to positive infinity. We want to predict probabilities, which strictly live between $0$ and $1$. 
How do we take a line that shoots into negative numbers and mathematically force it to only produce positive numbers? We use the exponential function $e^x$. It acts as a mathematical filter that turns *any* real number into a strictly positive number.

### What (Concept)
The natural exponential function is $f(x) = e^x$. 
* $e$ is Euler's number $\approx 2.718$.
* $x$ is our input (which can be any number: positive, negative, or zero).

**The Three Behaviors to Memorize:**
1.  **When $x = 0$:** $e^0 = 1$.
2.  **When $x > 0$:** $e^x$ explodes upwards. $e^5$ is about $148$. $e^{10}$ is over $22,000$.
3.  **When $x < 0$:** This is the most crucial part for Logistic Regression. What is $e^{-5}$? The negative exponent means a fraction: $\frac{1}{e^5}$. Dividing $1$ by $148$ gives a tiny decimal ($0.0067$). It approaches zero, but it never crosses into negative territory.

### How (Method / Example)
Let's look at how we compute this and observe the outputs.

We use `np.exp()` in Python to compute $e^x$.

**Code Example:**
```python
import numpy as np

# Let's test negative, zero, and positive inputs
inputs = np.array([-10, -1, 0, 1, 10])
outputs = np.exp(inputs)

for x, y in zip(inputs, outputs):
    print(f"e^{x:3} = {y:.6f}")
