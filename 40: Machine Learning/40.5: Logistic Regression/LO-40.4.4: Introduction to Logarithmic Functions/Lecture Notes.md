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

### 4.6 In-class Quiz.md

```markdown
# In-class Quiz: Logarithm Fundamentals

## Question 1
What is the mathematical domain (valid inputs) for the natural logarithm function, $f(x) = \ln(x)$?
A. All real numbers
B. $x \ge 0$
C. $x > 0$
D. $x \neq 0$

## Question 2
Using the properties of logarithms, which of the following is equivalent to $\log(x^3)$?
A. $\log(x) + 3$
B. $3 \cdot \log(x)$
C. $\log(x) \cdot \log(x) \cdot \log(x)$
D. $\log(x / 3)$

## Question 3
As the input $x$ approaches $0$ from the positive side, what does the value of $-\log(x)$ approach?
A. $0$
B. $1$
C. $-\infty$
D. $+\infty$
4.7 Question Bank.md

Markdown
# Question Bank: Introduction to Logarithmic Functions

## Section A: Multiple Choice Questions (MCQs)

**Q1.** What is the value of the natural logarithm of 1, denoted as $\ln(1)$?
A. $e$
B. $1$
C. $0$
D. Undefined

**Q2.** What is the domain of the natural logarithmic function $f(x) = \ln(x)$?
A. All real numbers $(-\infty, \infty)$
B. All non-negative real numbers $[0, \infty)$
C. All positive real numbers $(0, \infty)$
D. All real numbers except zero

---

## Section B: Multiple Select Questions (MSQs)

**Q3.** Which of the following are valid properties of logarithms? (Select all that apply)
A. $\log(a \cdot b) = \log(a) + \log(b)$
B. $\log(a / b) = \log(a) - \log(b)$
C. $\log(a + b) = \log(a) \cdot \log(b)$
D. $\log(a^b) = b \cdot \log(a)$

---

## Section C: Short Answer Questions

**Q4.** In machine learning, why do we frequently use the natural logarithm ($\ln$) instead of the common logarithm ($\log_{10}$)?

---

## Section D: Long Answer / Application Questions

**Q5.** Explain the behavior of the function $f(x) = -\log(x)$ as $x$ approaches $0$ from the positive side, and briefly state why this property is useful in machine learning cost functions.
Would you like me to generate the files for the next Learning Objective?
