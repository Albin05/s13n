# Question Bank: Regression vs Classification

## Q1 (MCQ)
**Problem:** You are building a system to recommend clothing sizes (S, M, L, XL) based on user measurements. This is an example of:
A. Binary Classification
B. Linear Regression
C. Multi-Class Classification
D. Univariate Regression

## Q2 (Coding)
**Problem:** Write a function `check_task_type(target_array)` that returns `"Regression"` if the target array contains floats with many unique values, and `"Classification"` if it contains integers with few unique values (e.g., < 10).
**Input:** `[1.2, 3.4, 5.6]`
**Output:** `"Regression"`

## Q3 (NAT)
**Problem:** You have a dataset with a target variable $y$ taking values $\{0, 1\}$. You train a Linear Regression model on it and get a prediction of $0.8$. If you convert this to a Classification prediction using a threshold of $0.5$, what is the final class label?

## Q4 (MSQ)
**Problem:** Which of the following statements are **TRUE**?
A. Logistic Regression is a Regression algorithm used to predict continuous values.
B. A problem can often be converted from Regression to Classification by "binning" the target variable.
C. Classification models try to find a decision boundary separating classes.
D. Regression models try to fit a line minimizing the distance to data points.

## Q5 (Coding)
**Problem:** You have a list of predictions: `[12.5, 10.1, 14.8]` and a list of actual values: `[12, 10, 15]`.
1.  Calculate the Mean Absolute Error (Regression Metric).
2.  Now, convert both lists to binary Classification: Value > 11 is Class 1, else Class 0.
3.  Calculate the Accuracy (Classification Metric).

## Q6 (Subjective)
**Problem:** Explain why using **Mean Squared Error (MSE)** to evaluate a Classification model (e.g., Cat vs Dog) is generally a bad idea, even if you encode Cat=0 and Dog=1.
