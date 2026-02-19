# Title: Introduction to Logarithmic Functions - Editorials

## Problem Description (Q1)
What is the value of the natural logarithm of 1, denoted as $\ln(1)$?
A. $e$
B. $1$
C. $0$
D. Undefined

## Objective
To recall the fundamental property of logarithms at $x = 1$.

## Hint
Any non-zero base raised to the power of $0$ equals what?

## Short Explanation
Option C is correct. The natural logarithm of $1$ is $0$, because $e^0 = 1$.

## Detailed Explanation
The logarithm function answers the question: "To what power must we raise the base to get $x$?" In the case of the natural logarithm, the base is Euler's number ($e \approx 2.718$). We want to find $y$ such that $e^y = 1$. According to the rules of exponents, any non-zero number raised to the power of $0$ is $1$. Therefore, $\ln(1) = 0$.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q2)
What is the domain of the natural logarithmic function $f(x) = \ln(x)$?
A. All real numbers $(-\infty, \infty)$
B. All non-negative real numbers $[0, \infty)$
C. All positive real numbers $(0, \infty)$
D. All real numbers except zero

## Objective
To identify the valid input range for a logarithmic function.

## Hint
Can you raise a positive base ($e$) to any real power and get a negative number or zero?

## Short Explanation
Option C is correct. Logarithms are only defined for strictly positive real numbers ($x > 0$).

## Detailed Explanation
For $y = \ln(x)$, we are looking for the exponent $y$ in the equation $e^y = x$. Since the base $e$ is positive ($2.718...$), raising it to any real power $y$ (whether positive, negative, or zero) will always result in a strictly positive number. There is no real power to which you can raise $e$ to get $0$ or a negative number. Thus, $x$ must be strictly greater than $0$.

## Constraints / Edge Cases
If $x \le 0$, $\ln(x)$ is undefined in the set of real numbers.

---

## Problem Description (Q3)
Which of the following are valid properties of logarithms? (Select all that apply)
A. $\log(a \cdot b) = \log(a) + \log(b)$
B. $\log(a / b) = \log(a) - \log(b)$
C. $\log(a + b) = \log(a) \cdot \log(b)$
D. $\log(a^b) = b \cdot \log(a)$

## Objective
To test knowledge of standard logarithmic algebraic rules.

## Hint
Logarithms are the inverses of exponents. How do you multiply terms with the same base? You add their exponents.

## Short Explanation
Options A, B, and D are correct. Option C is a common misconception; there is no simple rule for the logarithm of a sum.

## Detailed Explanation
* **A (Product Rule):** Log of a product is the sum of logs. Matches $e^x \cdot e^y = e^{x+y}$.
* **B (Quotient Rule):** Log of a quotient is the difference of logs. Matches $e^x / e^y = e^{x-y}$.
* **D (Power Rule):** The exponent inside the log can be pulled out as a multiplier. Matches $(e^x)^y = e^{x \cdot y}$.
* **C is incorrect:** $\log(a+b) \neq \log(a) \cdot \log(b)$.

## Constraints / Edge Cases
These rules assume $a > 0$ and $b > 0$.

---

## Problem Description (Q4)
In machine learning, why do we frequently use the natural logarithm ($\ln$) instead of the common logarithm ($\log_{10}$)?

## Objective
Understand the mathematical preference for Euler's number in calculus and optimization.

## Hint
Think about finding the derivative of $e^x$ versus $10^x$.

## Short Explanation
The natural logarithm has simpler, cleaner derivatives in calculus. Since machine learning relies heavily on gradient descent (which uses derivatives), base $e$ mathematically simplifies the optimization algorithms.

## Detailed Explanation
In machine learning optimization, we constantly compute gradients (derivatives). The derivative of $e^x$ is simply $e^x$, and the derivative of $\ln(x)$ is exactly $1/x$. If we used base 10, the derivative of $\log_{10}(x)$ would be $1 / (x \ln(10))$, introducing an extra constant factor that complicates the math. Using base $e$ keeps the derivative formulas as clean and efficient as possible.

## Constraints / Edge Cases
Changing the base of a logarithm only scales the function by a constant factor, so it does not change where the minimum or maximum of a cost function occurs, only the math to get there.

---

## Problem Description (Q5)
Explain the behavior of the function $f(x) = -\log(x)$ as $x$ approaches $0$ from the positive side, and briefly state why this property is useful in machine learning cost functions.

## Objective
Connect the mathematical asymptote of the logarithm to its application as a penalty function in algorithms like Logistic Regression.

## Hint
Plug in increasingly smaller numbers (like $0.1, 0.01, 0.0001$) into $-\log(x)$. What happens to the output?

## Short Explanation
As $x$ approaches $0$, $-\log(x)$ approaches positive infinity ($\infty$). This is highly useful in cost functions to heavily penalize a model when it confidently predicts the wrong class.

## Detailed Explanation
The logarithmic function $y = \log(x)$ has a vertical asymptote at $x = 0$, meaning $\lim_{x \to 0^+} \log(x) = -\infty$. When we negate this function to get $f(x) = -\log(x)$, the output grows infinitely large as $x$ gets closer to $0$.
In classification, if a model outputs a probability $p$ close to $0$ for an event that actually happened, we want to assign a massive error penalty. The function $-\log(p)$ naturally provides this massive penalty, forcing the model to correct its weights during gradient descent.

## Constraints / Edge Cases
Because $\log(0)$ is undefined, programmatic implementations of cost functions often add a tiny constant $\epsilon$ (e.g., $1e-15$) to $x$ to prevent math domain errors during computation.
