# Title: Deriving the Logistic Regression Equation - Editorials

## Problem Description (Q1)
Which of the following is the correct hypothesis equation $h_\theta(x)$ for Logistic Regression?
A. $h_\theta(x) = \theta^T x$
B. $h_\theta(x) = \frac{1}{1 + e^{\theta^T x}}$
C. $h_\theta(x) = \frac{1}{1 + e^{-\theta^T x}}$
D. $h_\theta(x) = 1 + e^{-\theta^T x}$

## Objective
Identify the correct mathematical composition of the linear model and the sigmoid function.

## Hint
Substitute $z = \theta^T x$ into the standard Sigmoid function $\sigma(z) = \frac{1}{1 + e^{-z}}$.

## Short Explanation
Option C is correct. The Logistic Regression hypothesis is formed by passing the linear equation $\theta^T x$ into the negative exponent of the Sigmoid function's denominator.

## Detailed Explanation
The derivation of the Logistic Regression equation involves two steps:
1.  Compute the linear combination of inputs and weights: $z = \theta_0 + \theta_1x_1 + \dots + \theta_nx_n = \theta^T x$.
2.  Pass this continuous, unbounded value $z$ through the Sigmoid activation function to map it to a valid probability range $(0, 1)$: $g(z) = \frac{1}{1 + e^{-z}}$.
Substituting $z$ gives the final hypothesis:
$$h_\theta(x) = \frac{1}{1 + e^{-\theta^T x}}$$

## Constraints / Edge Cases
N/A

---

## Problem Description (Q2)
What does the output of the Logistic Regression hypothesis, $h_\theta(x)$, strictly represent?
A. The exact class label ($0$ or $1$).
B. The estimated probability that $y = 1$ given input $x$.
C. The estimated probability that $y = 0$ given input $x$.
D. The margin of error in the prediction.

## Objective
Understand the probabilistic interpretation of the Logistic Regression model's output.

## Hint
By default, the model predicts the probability of the positive class.

## Short Explanation
Option B is correct. Mathematically, $h_\theta(x) = P(y=1 | x ; \theta)$.

## Detailed Explanation
The Logistic Regression hypothesis does not directly output a class like "Spam" or "Not Spam". Instead, it outputs a decimal value between $0$ and $1$. This value is interpreted as the estimated probability that the given observation belongs to the positive class ($y=1$), parameterized by the weights $\theta$. 
To find the probability of the negative class ($y=0$), you simply subtract this value from $1$: $P(y=0|x) = 1 - P(y=1|x)$.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q3)
Which of the following are necessary mathematical components to compute a prediction using standard Logistic Regression? (Select all that apply)
A. A linear combination of features and weights ($\theta^T x$).
B. The base of the natural logarithm ($e$).
C. A thresholding function (like outputting $1$ if $h_\theta(x) \ge 0.5$).
D. The Mean Squared Error function.

## Objective
Deconstruct the end-to-end prediction pipeline of a logistic model.

## Hint
Think about how you calculate the probability, and then how you convert that probability into a final discrete classification.

## Short Explanation
Options A, B, and C are correct. We need the linear equation, the exponential function (for the sigmoid), and a decision threshold to make a final categorical prediction. Option D is the cost function for linear regression, not a component of the logistic prediction equation.

## Detailed Explanation
To make a final prediction in Logistic Regression:
1.  Calculate $z = \theta^T x$ (Option A).
2.  Calculate $\sigma(z) = \frac{1}{1 + e^{-z}}$ (Requires Option B).
3.  Because the result is a probability, we must apply a threshold (usually $0.5$) to map the continuous probability back to a discrete class $0$ or $1$ (Option C).

## Constraints / Edge Cases
N/A

---

## Problem Description (Q4)
In the equation $h_\theta(x) = \frac{1}{1 + e^{-\theta^T x}}$, what is the mathematical dimension (shape) of $\theta^T x$ for a single data point, and what does it represent conceptually?

## Objective
Ensure clarity on the linear algebra and conceptual meaning of the inner term.

## Hint
What is the result of taking the dot product of a weight vector and a feature vector?

## Short Explanation
The term $\theta^T x$ is a single scalar value (a $1 \times 1$ number). Conceptually, it represents the unbounded "confidence score" or "log-odds" before it is compressed into a probability by the sigmoid function.

## Detailed Explanation
For a single observation with $n$ features, $x$ is an $(n+1) \times 1$ column vector (including the bias term), and $\theta$ is an $(n+1) \times 1$ column vector of weights. 
The operation $\theta^T x$ is a dot product, which multiplies corresponding elements and sums them up: $\theta_0(1) + \theta_1 x_1 + \dots + \theta_n x_n$. 
The result of a dot product between two vectors is a single scalar number. Conceptually, this number represents the raw, unbounded prediction of the linear boundary before the sigmoid function squishes it into the $(0, 1)$ interval.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q5)
Write a Python function `logistic_hypothesis(X, theta)` using NumPy that computes the logistic regression hypothesis for a given feature matrix $X$ and weight vector $\theta$.

## Objective
Translate the mathematical equation of Logistic Regression into vectorized Python code.

## Hint
Use `np.dot()` for the linear combination and `np.exp()` for the exponential.

## Short Explanation
Calculate the dot product of $X$ and $\theta$, then pass the result into the sigmoid formula $\frac{1}{1 + e^{-z}}$.

## Detailed Explanation
```python
import numpy as np

def logistic_hypothesis(X, theta):
    # Step 1: Compute the linear combination z = X * theta
    z = np.dot(X, theta)
    
    # Step 2: Apply the sigmoid function 1 / (1 + e^-z)
    hypothesis = 1 / (1 + np.exp(-z))
    
    return hypothesis

# Example usage:
# X is a 2x3 matrix (2 samples, 3 features including bias)
X_sample = np.array([[1, 2.5, 3.1], 
                     [1, 0.5, 1.2]])
# theta is a 3x1 vector
theta_sample = np.array([-1, 0.5, 0.2])

predictions = logistic_hypothesis(X_sample, theta_sample)
print(predictions)
