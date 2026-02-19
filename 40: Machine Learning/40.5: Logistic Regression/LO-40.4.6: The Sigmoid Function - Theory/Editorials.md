# Title: The Sigmoid Function (Theory) - Editorials

## Problem Description (Q1)
Which of the following represents the correct mathematical formula for the Sigmoid function, denoted as $\sigma(z)$?
A. $\sigma(z) = \frac{1}{1 + e^z}$
B. $\sigma(z) = \frac{1}{1 + e^{-z}}$
C. $\sigma(z) = \frac{e^{-z}}{1 + e^{-z}}$
D. $\sigma(z) = \frac{z}{1 + e^{-z}}$

## Objective
Identify the standard mathematical definition of the logistic sigmoid function.

## Hint
Remember that the denominator must grow when $z$ becomes negative to make the output approach $0$. 

## Short Explanation
Option B is correct. The standard formula for the Sigmoid function is $\sigma(z) = \frac{1}{1 + e^{-z}}$.

## Detailed Explanation
The purpose of the Sigmoid function is to map any real-valued number $z$ into a value strictly between $0$ and $1$. 
* The equation is $\sigma(z) = \frac{1}{1 + e^{-z}}$.
* If we used $e^z$ in the denominator (Option A), large positive inputs would make the denominator huge, driving the output to $0$, which is the opposite of the desired behavior (large positive inputs should map to $1$). 

## Constraints / Edge Cases
N/A

---

## Problem Description (Q2)
What is the mathematical range of the Sigmoid function $\sigma(z)$?
A. $[-\infty, \infty]$
B. $[0, \infty]$
C. $(0, 1)$
D. $[-1, 1]$

## Objective
Establish the bounds of the Sigmoid function's output.

## Hint
Can the output of $\frac{1}{1 + e^{-z}}$ ever exactly equal $0$ or $1$ for a finite real number $z$?

## Short Explanation
Option C is correct. The output is strictly bounded between $0$ and $1$, never actually touching them.

## Detailed Explanation
Because $e^{-z}$ is always strictly positive for any real number $z$, the denominator $1 + e^{-z}$ is always strictly greater than $1$. 
* Therefore, the fraction $\frac{1}{1 + e^{-z}}$ must be strictly less than $1$. 
* Similarly, since the numerator is $1$ and the denominator is positive and finite, the fraction must be strictly greater than $0$. 
Thus, the range is the open interval $(0, 1)$.

## Constraints / Edge Cases
In practical programmatic implementations (like floating-point math in Python), very large inputs might round to exactly $1.0$ or $0.0$, but mathematically, it remains an open interval.

---

## Problem Description (Q3)
If the input to the Sigmoid function is $z = 0$, what is the output?
A. $0$
B. $1$
C. $0.5$
D. $e$

## Objective
Determine the critical midpoint (y-intercept) of the Sigmoid curve.

## Hint
Plug $z = 0$ into the equation $\sigma(z) = \frac{1}{1 + e^{-z}}$ and evaluate.

## Short Explanation
Option C is correct. $\sigma(0) = 0.5$.

## Detailed Explanation
Substitute $z = 0$ into the formula:
$$\sigma(0) = \frac{1}{1 + e^{-0}}$$
Since $e^0 = 1$:
$$\sigma(0) = \frac{1}{1 + 1} = \frac{1}{2} = 0.5$$
This is the inflection point of the curve, perfectly splitting the output range.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q4)
Describe the behavior of the Sigmoid function $\sigma(z)$ as $z$ approaches positive infinity ($z \to \infty$) and as $z$ approaches negative infinity ($z \to -\infty$).

## Objective
Analyze the asymptotic behavior of the Sigmoid function at its extremes.

## Hint
Think about what happens to $e^{-z}$ for very large positive and very large negative values of $z$.

## Short Explanation
As $z \to \infty$, $\sigma(z) \to 1$. As $z \to -\infty$, $\sigma(z) \to 0$.

## Detailed Explanation
1.  **As $z \to \infty$:** The term $e^{-z}$ becomes $e^{-\infty}$, which approaches $0$. The denominator $1 + e^{-z}$ approaches $1$. Therefore, $\frac{1}{1} = 1$.
2.  **As $z \to -\infty$:** The term $e^{-z}$ becomes $e^{-(-\infty)} = e^{\infty}$, which grows infinitely large. The denominator becomes infinitely large. A fraction with a constant numerator and an infinitely growing denominator approaches $0$. 
This "squishing" behavior ensures the output perfectly mimics a probability distribution.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q5)
Why is the Sigmoid function considered the essential link between Linear Regression and Logistic Regression?

## Objective
Connect the mathematical properties of Sigmoid to the architectural goal of classification.

## Hint
Consider the output range of Linear Regression ($z = \theta^T x$) and the required output range for a classification probability.

## Short Explanation
Linear regression outputs values from $-\infty$ to $\infty$. The Sigmoid function takes this unbounded output and mathematically maps it or "squishes" it strictly into the $(0, 1)$ range, making it valid for predicting probabilities.

## Detailed Explanation
In classification, we need a hypothesis function that outputs the probability $P(y=1 | x)$. Probabilities must be between $0$ and $1$. The linear equation $z = \theta^T x$ is unbounded. By feeding $z$ through the Sigmoid function $\sigma(z)$, we get $\hat{y} = \sigma(\theta^T x)$. 
* If the linear model outputs a huge positive number, Sigmoid maps it near $1$. 
* If it outputs a huge negative number, Sigmoid maps it near $0$. 
This transforms the linear regression line into the logistic regression S-curve.

## Constraints / Edge Cases
N/A
