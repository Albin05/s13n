# Title: Understanding Exponential Functions - Editorials

## Problem Description (Q1)
What is the value of the exponential function $e^x$ when $x = 0$?
A. $e$
B. $1$
C. $0$
D. Undefined

## Objective
To establish the y-intercept of the natural exponential function.

## Hint
Any non-zero real number raised to the power of $0$ equals what?

## Short Explanation
Option B is correct. By the laws of exponents, any non-zero base raised to the power of $0$ is equal to $1$. Therefore, $e^0 = 1$.

## Detailed Explanation
The natural exponential function is $f(x) = e^x$, where $e$ is Euler's number (approximately $2.71828$). Just like $2^0 = 1$ and $10^0 = 1$, raising the mathematical constant $e$ to the power of $0$ results in exactly $1$. This means the graph of $y = e^x$ crosses the y-axis at the point $(0, 1)$.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q2)
What is the range of the natural exponential function $f(x) = e^x$ for any real number input $x$?
A. All real numbers $(-\infty, \infty)$
B. All non-negative real numbers $[0, \infty)$
C. All strictly positive real numbers $(0, \infty)$
D. Values between $0$ and $1$ $(0, 1)$

## Objective
To understand that exponential functions map any real number to a strictly positive number.

## Hint
Can multiplying a positive number ($2.718...$) by itself ever result in zero or a negative number?

## Short Explanation
Option C is correct. The output of $e^x$ is always strictly greater than $0$, no matter how negative the input $x$ becomes.

## Detailed Explanation
Euler's number $e$ is a positive constant.
* When $x > 0$, we are multiplying positive numbers, yielding a positive result.
* When $x = 0$, the result is $1$, which is positive.
* When $x < 0$, $e^{-x}$ is equivalent to $1 / e^{|x|}$. Dividing $1$ by a positive number always yields a strictly positive fraction.
Therefore, the function never touches $0$ and never becomes negative. The range is $(0, \infty)$.

## Constraints / Edge Cases
As $x$ approaches $-\infty$, $e^x$ approaches $0$ asymptotically, but it never actually reaches $0$.

---

## Problem Description (Q3)
Which of the following statements about $e^x$ and $e^{-x}$ are true? (Select all that apply)
A. As $x \to \infty$, $e^x$ grows towards $\infty$.
B. As $x \to \infty$, $e^{-x}$ approaches $0$.
C. $e^{-x}$ can output negative values for large positive inputs of $x$.
D. Both $e^x$ and $e^{-x}$ are always positive.

## Objective
To differentiate the behavior of exponential growth ($e^x$) and exponential decay ($e^{-x}$).

## Hint
Remember that $e^{-x} = \frac{1}{e^x}$.

## Short Explanation
Options A, B, and D are correct. Option C is false because exponential functions always output positive values.

## Detailed Explanation
* **A is true:** $e^x$ is exponential growth. As $x$ gets larger, $e^x$ grows extremely fast.
* **B is true:** $e^{-x} = \frac{1}{e^x}$. As $x$ grows large, the denominator becomes huge, making the fraction approach $0$.
* **D is true:** Both functions only produce positive outputs regardless of the input $x$.
* **C is false:** The negative sign is in the exponent, indicating a fraction, not a negative output value.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q4)
Explain the behavior of the function $f(x) = e^{-x}$ as $x$ becomes a very large positive number.

## Objective
To articulate the concept of an asymptote in the context of exponential decay.

## Hint
Write $e^{-x}$ as a fraction to visualize what happens as the input grows.

## Short Explanation
As $x$ becomes a very large positive number, $e^{-x}$ gets closer and closer to $0$.

## Detailed Explanation
The expression $e^{-x}$ is mathematically equivalent to $\frac{1}{e^x}$. When $x$ is a large positive number, the denominator $e^x$ becomes enormously large. Dividing $1$ by a massive number results in a very tiny fraction (e.g., $1 / 1,000,000 = 0.000001$). Therefore, as $x \to \infty$, $\frac{1}{e^x} \to 0$. The function has a horizontal asymptote at $y = 0$.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q5)
In the context of machine learning, if we have a linear equation $z = \theta^T x$ that can output any real number from $-\infty$ to $\infty$, why
