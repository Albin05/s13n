# Question Bank: Implementing Logistic Regression in Python

## Section A: Multiple Choice Questions (MCQs)

**Q1.** Which of the following `scikit-learn` modules contains the `LogisticRegression` class?
A. `sklearn.preprocessing`
B. `sklearn.ensemble`
C. `sklearn.linear_model`
D. `sklearn.classification`

**Q2.** When using a trained `LogisticRegression` model in `scikit-learn`, what is the primary difference between the `.predict(X)` and `.predict_proba(X)` methods?
A. `.predict(X)` returns probabilities, while `.predict_proba(X)` returns exact classes.
B. `.predict(X)` returns discrete class labels, while `.predict_proba(X)` returns continuous probabilities for each class.
C. `.predict(X)` trains the model, while `.predict_proba(X)` tests it.
D. There is no difference; they are aliases for the same function.

---

## Section B: Multiple Select Questions (MSQs)

**Q3.** Select all the mandatory steps required to train a `LogisticRegression` model and make predictions using `scikit-learn`.
A. Initialize the model: `model = LogisticRegression()`
B. Standardize the labels to be strictly between -1 and 1.
C. Train the model using the training data: `model.fit(X_train, y_train)`
D. Make predictions on new data: `predictions = model.predict(X_test)`

---

## Section C: Short Answer Questions

**Q4.** Explain why it is often recommended to use a standard scaler (like `StandardScaler`) on your feature matrix $X$ before fitting a `LogisticRegression` model in `scikit-learn`.

---

## Section D: Implementation Tasks

**Q5.** Write a complete Python script using `scikit-learn` and `numpy` to:
1. Create a synthetic dataset using `np.array` for $X$ (features) and $y$ (binary labels).
2. Initialize a Logistic Regression model.
3. Fit the model to the data.
4. Print the predicted classes and the probabilities for the training data.
