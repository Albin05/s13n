# Introduction to Logarithmic Functions

## Conceptual Explanation
In mathematics, a **logarithm** is the inverse operation to exponentiation. Just as division un-does multiplication, a logarithm un-does an exponent.
If you know that a base $b$ raised to a power $y$ equals $x$:
$$b^y = x$$
Then the logarithm of $x$ with base $b$ is $y$:
$$\log_b(x) = y$$

**The Natural Logarithm:**
In Machine Learning, we almost exclusively use the **natural logarithm**, where the base is Euler's number ($e \approx 2.718$). This is often written as $\ln(x)$ or simply $\log(x)$ in programming libraries like NumPy.

**Important Properties:**
1.  **Domain:** You can only take the logarithm of a strictly positive number ($x > 0$).
2.  **Roots:** $\ln(1) = 0$.
3.  **Growth:** The log function grows very slowly as $x$ increases, but plunges to negative infinity as $x$ gets close to zero.

## Short Examples
* If $10^2 = 100$, then $\log_{10}(100) = 2$.
* If $e^0 = 1$, then $\ln(1) = 0$.
* What is $\ln(e)$? Since $e^1 = e$, the answer is $1$.

## External Links
* [Khan Academy: Introduction to Logarithms](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs)
* [Numpy documentation for np.log()](https://numpy.org/doc/stable/reference/generated/numpy.log.html)

## Visuals
*(Refer to S3 bucket for the graph of $y = \ln(x)$, highlighting the asymptote at $x=0$ and the x-intercept at $x=1$)*
