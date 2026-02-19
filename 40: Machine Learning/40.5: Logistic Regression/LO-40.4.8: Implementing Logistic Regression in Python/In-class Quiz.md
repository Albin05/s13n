# In-class Quiz: Python Implementation

## Question 1
From which `scikit-learn` module do you import `LogisticRegression`?
A. `sklearn.models`
B. `sklearn.linear_model`
C. `sklearn.classifier`
D. `sklearn.regression`

## Question 2
You pass a dataset of 10 new patients to `model.predict_proba(X_test)` on a trained binary classification model. What is the shape of the resulting output array?
A. $(10, 1)$
B. $(10, 2)$
C. $(2, 10)$
D. $(1, 10)$

## Question 3
What happens if you try to pass a 1-dimensional NumPy array (e.g., `shape (50,)`) as the feature matrix $X$ to the `.fit()` method?
A. The model trains normally.
B. The model assumes the data represents 50 features for 1 sample.
C. `scikit-learn` throws a `ValueError` demanding a 2D array.
D. The model converts the array into target labels.
