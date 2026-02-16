# Question Bank: Feature Selection

## Q1 (MCQ)
**Problem:** Which feature selection method involves training a model iteratively, removing the least important feature at each step?
A. Pearson Correlation
B. Recursive Feature Elimination (RFE)
C. L1 Regularization (Lasso)
D. Variance Threshold

## Q2 (Coding)
**Problem:** Write a function `remove_constant_columns(df)` using Pandas that drops any column where all values are identical.
**Input:** A DataFrame with columns A=[1, 2], B=[5, 5].
**Output:** A DataFrame with only column A.

## Q3 (NAT)
**Problem:** You have a dataset with 10 features. You want to test every possible combination of features to find the best subset. How many total combinations (subsets) would you have to train? (Hint: $2^n - 1$).

## Q4 (MSQ)
**Problem:** Which of the following are valid reasons to drop a feature?
A. The feature has 99% missing values.
B. The feature is a unique ID (e.g., `User_ID`) for each row.
C. The feature is highly correlated with the Target variable.
D. The feature is a duplicate of another feature (e.g., `height_cm` and `height_m`).

## Q5 (Coding)
**Problem:** Implement a simple Correlation Filter. Given a DataFrame `df` and a target column name `target`, return a list of feature names that have a correlation with the target greater than 0.5 (absolute value).
*Use `df.corr()`.*

## Q6 (Subjective)
**Problem:** Explain the difference between **Filter** and **Wrapper** methods. Why is a Wrapper method typically more accurate but computationally expensive?
