# Implementing Logistic Regression

## The Scikit-Learn API
`scikit-learn` uses a unified object-oriented API. All predictive models act as "Estimators" and follow the same basic lifecycle.

1.  **Import:** `from sklearn.linear_model import LogisticRegression`
2.  **Instantiate:** Create the estimator object. `model = LogisticRegression()`
3.  **Fit:** Train the model. `model.fit(X_train, y_train)`
4.  **Predict:** Generate new predictions. `model.predict(X_test)`

## Core Methods for Logistic Regression

### `.fit(X, y)`
* Executes the mathematical training process.
* $X$ must be a 2-dimensional structure (samples $\times$ features).
* $y$ must be a 1-dimensional structure (labels).

### `.predict(X)`
* Outputs the discrete class labels based on a default $0.5$ threshold.
* Returns an array like: `[0, 1, 0, 0, 1]`

### `.predict_proba(X)`
* Outputs the raw probability estimates.
* Returns a 2D array of shape `(n_samples, n_classes)`. 
* For binary classification, `column 0` is $P(y=0)$ and `column 1` is $P(y=1)$.

## Accessing the Learned Weights (Theta)
After `.fit()` is called, you can inspect the mathematical weights the model learned:
* `model.coef_`: The weights ($\theta_1, \dots, \theta_n$) associated with the features.
* `model.intercept_`: The bias term ($\theta_0$).

## Standard Implementation Example
```python
from sklearn.linear_model import LogisticRegression
import numpy as np

# Data Preparation
X_train = np.array([[2.0, 3.1], [1.1, 0.9], [5.5, 4.2], [6.1, 5.0]])
y_train = np.array([0, 0, 1, 1])

# Model Pipeline
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Evaluation
accuracy = clf.score(X_train, y_train)
print(f"Training Accuracy: {accuracy * 100}%")
