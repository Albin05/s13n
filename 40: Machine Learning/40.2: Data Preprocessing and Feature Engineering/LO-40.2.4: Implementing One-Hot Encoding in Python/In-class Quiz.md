Which parameter in `pd.get_dummies` allows you to automatically remove the first category to prevent the "Dummy Variable Trap"?
A. `remove_first=True`
B. `drop_first=True`
C. `trap_prevention=True`
D. `one_hot=True`

## Question 2
When using Scikit-Learn's `OneHotEncoder`, what happens if you call `.transform()` on data containing a category that was NOT present during `.fit()`?
A. It throws an error by default.
B. It automatically adds a new column for the new category.
C. It guesses the category based on similarity.
D. It retrains the encoder.

## Question 3
Why is `fit_transform` used on Training data, but only `transform` used on Testing data?
A. To save computation time.
B. To ensure the Test data is encoded using the *exact same* rules and columns as the Training data.
C. Because `fit` creates new data.
D. Because Testing data always has different columns.
