# Question Bank: Why Linear Regression Fails for Classification

## Section A: Multiple Choice Questions (MCQs)

**Q1.** Why is Linear Regression generally considered unsuitable for classification tasks where the target is binary ($y \in \{0, 1\}$)?
A. It cannot handle multiple features.
B. Its predictions can be less than 0 or greater than 1.
C. It requires the input data to be strictly categorical.
D. It always overfits binary data.

**Q2.** How does the presence of an outlier typically affect a Linear Regression model used for binary classification (using a threshold of 0.5)?
A. It has no effect on the decision boundary.
B. It skews the best-fit line, which can shift the decision boundary and cause misclassifications.
C. It forces the line to pass exactly through the threshold.
D. It immediately converts the model into a Logistic Regression model.

---

## Section B: Multiple Select Questions (MSQs)

**Q3.** Select all valid reasons why Linear Regression is a poor choice for Classification.
A. The cost function (MSE) is sensitive to outliers.
B. The predicted values are not bounded between $[0, 1]$.
C. It cannot be regularized.
D. It assumes a linear relationship between features and continuous targets, rather than discrete classes.

---

## Section C: Short Answer Questions

**Q4.** Explain why interpreting the output of a Linear Regression model as a "probability" for classification is fundamentally flawed.

---

## Section D: Implementation Tasks

**Q5.** Write a Python snippet to fit a `sklearn.linear_model.LinearRegression` on binary data, and then predict a value that demonstrates the model outputting a value greater than 1.
