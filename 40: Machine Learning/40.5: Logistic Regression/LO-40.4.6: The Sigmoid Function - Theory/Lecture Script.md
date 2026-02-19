# Lecture Script: The Sigmoid Function (Theory)

## Topic: Squishing the Line into a Probability

### Why (Importance)
We have a massive problem from our linear regression module. We calculated $z = \theta^T x$, and $z$ can be $500$ or $-20$. We cannot present a probability of $-2000\%$. 
We need a mathematical mechanism that takes *any* real number and forces it into the $(0, 1)$ boundary without losing the information about how large or small the original number was. The Sigmoid function is the elegant mathematical solution that makes Logistic Regression possible.

### What (Concept)
The Sigmoid function, $\sigma(z)$, is defined as:
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

Let's dissect this equation:
1.  **The Numerator:** It is fixed at $1$. The overall fraction can never be larger than the numerator as long as the denominator is $> 1$.
2.  **The Denominator:** $1 + e^{-z}$. We already learned that exponential functions ($e^{-z}$) are always positive. So, $1 + (\text{positive number})$ is always greater than $1$.
3.  **The Result:** $1$ divided by something strictly greater than $1$ means the output is always strictly less than $1$ and greater than $0$.

### How (Method / Example)
Let's see how it behaves under three conditions: $z=0$, $z \to \infty$, and $z \to -\infty$.

**Case 1: The Boundary (z = 0)**
If our linear model predicts exactly $0$:
$\sigma(0) = \frac{1}{1 + e^0} = \frac{1}{1 + 1} = 0.5$
This is perfect. It means the model is $50\%$ sure. It's a coin toss.

**Case 2: Extreme Confidence (z = 10)**
Our linear model predicts a huge positive number.
$e^{-10} = \frac{1}{e^{10}} \approx 0.000045$
$\sigma(10) = \frac{1}{1 + 0.000045} = \frac{1}{1.000045} \approx 0.9999$
The model maps it to $99.99\%$ certainty.

**Case 3: Extreme Negative Confidence (z = -10)**
Our linear model predicts a huge negative number.
$e^{-(-10)} = e^{10} \approx 22026$
$\sigma(-10) = \frac{1}{1 + 22026} = \frac{1}{22027} \approx 0.000045$
The model maps it to near $0\%$ certainty.

By wrapping our linear model inside this function ($\hat{y} = \sigma(\theta^T x)$), we have successfully created a valid probability model.

### URLs for Demos
* [Desmos: Plot y = 1 / (1 + e^(-x))](https://www.desmos.com/calculator)
