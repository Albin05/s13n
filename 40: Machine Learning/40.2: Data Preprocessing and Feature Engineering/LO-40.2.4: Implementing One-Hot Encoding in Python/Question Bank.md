# Question Bank: Implementing OHE

## Q1 (MCQ)
**Problem:** You are using `OneHotEncoder(handle_unknown='ignore')`. Your training data has categories `['Cat', 'Dog']`. Your test data has `['Bird']`. What will be the vector output for `['Bird']`?
A. `[0, 0]` (All zeros)
B. `[0, 0, 1]` (New column added)
C. `[1, 0]` (Mapped to first category)
D. `NaN`

## Q2 (Coding)
**Problem:** Write a function `pandas_ohe(df, col)` that takes a DataFrame and a column name, performs One-Hot Encoding (dropping the first category), and returns the new DataFrame.
**Input:** `df` with `Color=['R', 'G', 'B']`.
**Output:** DataFrame with `Color_G`, `Color_R` (assuming B is dropped).

## Q3 (NAT)
**Problem:** You have a categorical feature with 5 unique values. You use `OneHotEncoder(drop='first')`. How many columns will the resulting array have?

## Q4 (MSQ)
**Problem:** Which of the following are valid reasons to prefer `OneHotEncoder` over `get_dummies` in a production pipeline?
A. `OneHotEncoder` can be part of a Scikit-Learn `Pipeline` object.
B. `OneHotEncoder` handles unknown categories in future data without crashing (if configured).
C. `OneHotEncoder` is always faster for small datasets.
D. `OneHotEncoder` remembers the column order and categories from training.

## Q5 (Coding)
**Problem:** Write a script using `sklearn` that:
1.  Fits a `OneHotEncoder` on `X_train = [['A'], ['B']]`.
2.  Transforms `X_test = [['A'], ['C']]`.
3.  Set `handle_unknown='ignore'` so it doesn't crash on 'C'.
4.  Print the result.

## Q6 (Subjective)
**Problem:** Explain the "Train-Test Skew" that can happen if you use `pd.get_dummies` separately on your Training dataset and your Test dataset. Give an example where the number of columns would mismatch.
