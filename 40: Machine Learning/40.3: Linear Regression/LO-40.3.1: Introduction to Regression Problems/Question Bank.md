# Question Bank: Regression Basics

## Q1 (MCQ)
**Problem:** Which of the following is **NOT** a Regression problem?
A. Predicting the time it takes for a pizza delivery.
B. Predicting the color of a flower based on petal size.
C. Predicting the lifetime of a lightbulb in hours.
D. Predicting the total revenue of a company for the next quarter.

## Q2 (Coding)
**Problem:** Write a Python function `is_regression(target_list)` that checks if a list of target values represents a regression problem.
* Logic: If the values are floating point numbers or have more than 10 unique values (high cardinality implying continuity), return `True`. Else return `False`.
**Input:** `[10.5, 20.1, 33.2]`
**Output:** `True`

## Q3 (NAT)
**Problem:** A simple regression model follows the rule $y = 3x + 5$. If the input $x$ is 4, what is the predicted value $\hat{y}$?

## Q4 (MSQ)
**Problem:** Select all correct statements about Regression.
A. The target variable must be numerical.
B. It tries to find a decision boundary to separate classes.
C. It minimizes the error distance between prediction and actual value.
D. Predicting "Customer Churn" (Yes/No) is a regression problem.

## Q5 (Coding)
**Problem:** You have a list of problem descriptions. Filter out only the ones that are Regression tasks.
`problems = ["Predict Price", "Predict Gender", "Predict Temperature", "Predict Spam"]`
**Input:** The list.
**Output:** `["Predict Price", "Predict Temperature"]`

## Q6 (Subjective)
**Problem:** Explain why converting a Regression problem (e.g., predicting exact age) into a Classification problem (e.g., predicting age groups 0-18, 19-35, 36+) results in a loss of information. When might this be useful despite the loss?
