# Title: Why Linear Regression Fails for Classification - Editorials

## Problem Description (Q1)
Why is Linear Regression generally considered unsuitable for classification tasks where the target is binary ($y \in \{0, 1\}$)?
A. It cannot handle multiple features.
B. Its predictions can be less than 0 or greater than 1.
C. It requires the input data to be strictly categorical.
D. It always overfits binary data.

## Objective
Identify the fundamental output range limitation of applying Linear Regression to probability-based classification.

## Hint
Consider the domain and range of a linear function $h_\theta(x) = \theta^T x$.

## Short Explanation
Option B is correct. Linear Regression outputs a continuous unbounded value $(-\infty, \infty)$. For binary classification, we ideally want probabilities between $0$ and $1$.

## Detailed Explanation
Linear Regression fits a line (or hyperplane) to minimize the Mean Squared Error. The hypothesis is $h_\theta(x) = \theta^T x$. Because it is a linear function, the predicted values can easily exceed $1$ or fall below $0$ for large or small feature values. In classification, interpreting a prediction of $y = 1.5$ or $y = -0.3$ is meaningless when the target classes are exactly $0$ and $1$, and we are looking for a probability.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q2)
How does the presence of an outlier typically affect a Linear Regression model used for binary classification (using a threshold of 0.5)?
A. It has no effect on the decision boundary.
B. It skews the best-fit line, which can shift the decision boundary and cause misclassifications.
C. It forces the line to pass exactly through the threshold.
D. It immediately converts the model into a Logistic Regression model.

## Objective
Understand the sensitivity of Ordinary Least Squares (OLS) to outliers and its impact on classification boundaries.

## Hint
Think about how Mean Squared Error penalizes points that are far away from the line.

## Short Explanation
Option B is correct. OLS heavily penalizes large errors. An outlier pulls the regression line towards itself, which shifts the point where the line crosses the $0.5$ threshold, leading to previously correct points being misclassified.

## Detailed Explanation
If we use Linear Regression for classification, we typically set a threshold (e.g., if $h_\theta(x) \ge 0.5$, predict Class $1$). Mean Squared Error (MSE) is sensitive to outliers. An extreme positive point (an outlier in Class $1$) will pull the regression line up to minimize the squared error for that specific point. This decreases the slope of the line, shifting the $y=0.5$ intersection point further along the x-axis. As a result, standard data points that were previously correctly classified as Class $1$ might now fall below the $0.5$ threshold and be misclassified as Class $0$.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q3)
Select all valid reasons why Linear Regression is a poor choice for Classification.
A. The cost function (MSE) is sensitive to outliers.
B. The predicted values are not bounded between $[0, 1]$.
C. It cannot be regularized.
D. It assumes a linear relationship between features and continuous targets, rather than discrete classes.

## Objective
Summarize the multiple mathematical and conceptual reasons Linear Regression fails for categorical targets.

## Hint
Review the output range, the loss function's properties, and the underlying assumptions of the model.

## Short Explanation
Options A, B, and D are correct. Linear Regression is unbounded, highly sensitive to outliers changing the decision threshold, and structurally designed for continuous, not discrete, outputs.

## Detailed Explanation
* **A is true:** MSE squares the distance. An outlier generates a massive error, skewing the line.
* **B is true:** A line extends to infinity, making probability interpretations impossible.
* **D is true:** Regression assumes $y$ changes continuously with $X$, but classification implies a step-change or non-linear separation between distinct states.
* **C is false:** Linear Regression can absolutely be regularized (Lasso, Ridge).

## Constraints / Edge Cases
N/A

---

## Problem Description (Q
