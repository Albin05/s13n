# Question Bank: One-Hot Encoding

## Q1 (MCQ)
**Problem:** Which of the following statements explains why Label Encoding (mapping to 1, 2, 3...) is often bad for Nominal data like "Color"?
A. It takes up more memory than One-Hot Encoding.
B. It forces the model to treat the categories as having a mathematical order/rank ($3 > 1$), which doesn't exist.
C. It cannot handle missing values.
D. It converts the data into binary vectors.

## Q2 (Coding)
**Problem:** Using Pandas, write a snippet to apply One-Hot Encoding to the `City` column of a DataFrame `df`. Ensure that the original `City` column is removed and the new columns are prefixed with `City_`.
**Input:** `df` with column `City`.
**Output:** Transformed `df`.

## Q3 (NAT)
**Problem:** A dataset has 10 rows and 3 columns.
* Column 1: Numerical.
* Column 2: Categorical with 4 unique values.
* Column 3: Categorical with 3 unique values.
If we apply One-Hot Encoding to Columns 2 and 3 (without dropping the first category), how many columns will the final dataset have?

## Q4 (MSQ)
**Problem:** Select the scenarios where One-Hot Encoding might be **problematic**.
A. The feature is "Zip Code" with 40,000 unique values.
B. The feature is "Gender" with 2 unique values.
C. The dataset needs to be used with a Tree-based model (like Random Forest) which can handle raw categories well.
D. The feature is "Review Rating" (1 to 5 stars) where order matters significantly.

## Q5 (Coding)
**Problem:** Write a function `encode_drop_first(df, col_name)` that performs One-Hot Encoding on a specified column using Pandas, but drops the first category to avoid multicollinearity. Return the modified DataFrame.

## Q6 (Subjective)
**Problem:** Explain the "Dummy Variable Trap". If we have a categorical variable for "Season" (Spring, Summer, Fall, Winter), why is it mathematically redundant to have 4 binary columns? What is the mathematical relationship between the 4th column and the first 3?
