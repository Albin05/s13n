# Question Bank: Deriving the Logistic Regression Equation

## Section A: Multiple Choice Questions (MCQs)

**Q1.** Which of the following is the correct hypothesis equation $h_\theta(x)$ for Logistic Regression?
A. $h_\theta(x) = \theta^T x$
B. $h_\theta(x) = \frac{1}{1 + e^{\theta^T x}}$
C. $h_\theta(x) = \frac{1}{1 + e^{-\theta^T x}}$
D. $h_\theta(x) = 1 + e^{-\theta^T x}$

**Q2.** What does the output of the Logistic Regression hypothesis, $h_\theta(x)$, strictly represent?
A. The exact class label ($0$ or $1$).
B. The estimated probability that $y = 1$ given input $x$.
C. The estimated probability that $y = 0$ given input $x$.
D. The margin of error in the prediction.

---

## Section B: Multiple Select Questions (MSQs)

**Q3.** Which of the following are necessary mathematical components to compute a prediction using standard Logistic Regression? (Select all that apply)
A. A linear combination of features and weights ($\theta^T x$).
B. The base of the natural logarithm ($e$).
C. A thresholding function (like outputting $1$ if $h_\theta(x) \ge 0.5$).
D. The Mean Squared Error function.

---

## Section C: Short Answer Questions

**Q4.** In the equation $h_\theta(x) = \frac{1}{1 + e^{-\theta^T x}}$, what is the mathematical dimension (shape) of $\theta^T x$ for a single data point, and what does it represent conceptually?

---

## Section D: Implementation Tasks

**Q5.** Write a Python function `logistic_hypothesis(X, theta)` using NumPy that computes the logistic regression hypothesis for a given feature matrix $X$ and weight vector $\theta$.
