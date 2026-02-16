# Question Bank: Train-Test Split

## Q1 (MCQ)
**Problem:** Which of the following variables should NEVER be shown to the model during the `.fit()` (training) process?
A. `X_train`
B. `y_train`
C. `X_test` (and `y_test`)
D. `random_state`

## Q2 (Coding)
**Problem:** Write a Python snippet to split arrays `X` and `y` into training and testing sets. Use 25% for testing and set a random seed of 123.
**Input:** `X`, `y` arrays.
**Output:** Four arrays: `X_train`, `X_test`, `y_train`, `y_test`.

## Q3 (NAT)
**Problem:** You have a dataset with 500 rows. You perform a Train-Test split with `test_size=0.2`. How many rows will be in the `X_train` variable?

## Q4 (MSQ)
**Problem:** Which of the following statements about **Data Leakage** regarding Train-Test splits are true?
A. It occurs if you perform Feature Scaling (e.g., calculating Mean) on the *entire* dataset before splitting.
B. It occurs if you include the Test data in the `.fit()` command.
C. It results in a model that performs poorly on training data but well on test data.
D. It results in over-optimistic test scores that do not reflect reality.

## Q5 (Coding)
**Problem:** Implement a "Time-Based Split".
Given a DataFrame `df` with a 'Date' column, sort it by date, and split it such that the first 80% of rows are Train and the last 20% are Test. (Do not use `sklearn` randomness).

## Q6 (Subjective)
**Problem:** Explain why `random_state` is important for **Reproducibility**. If two engineers are working on the same model but use different (or no) random states, what problems might arise when they compare their results?
