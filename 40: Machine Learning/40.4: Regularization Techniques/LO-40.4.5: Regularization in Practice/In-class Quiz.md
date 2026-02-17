# In-Class Quiz

## Question 1
Why is Feature Scaling (e.g., `StandardScaler`) considered mandatory before applying Ridge or Lasso Regression?
A. Because the algorithms cannot handle negative numbers.
B. Because the penalty term depends on the magnitude of the weights, which depends on the scale of the features.
C. Because it speeds up the matrix inversion.
D. It is not mandatory; it is optional.

## Question 2
Which Scikit-Learn class allows you to automatically find the best `alpha` (regularization strength) using efficient Cross-Validation?
A. `RidgeClassifier`
B. `LinearRegression`
C. `RidgeCV`
D. `GridSearch` (While true, C is the *specific efficient* class).

## Question 3
If you have a dataset with 100 features, and you suspect that only 5 of them are actually important for the prediction, which model should you start with?
A. Ridge Regression.
B. Lasso Regression.
C. Standard Linear Regression.
D. Polynomial Regression.
