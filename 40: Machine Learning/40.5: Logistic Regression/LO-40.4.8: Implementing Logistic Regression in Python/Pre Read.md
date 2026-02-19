# Implementing Logistic Regression in Python

## Conceptual Explanation
Writing the mathematical equations for gradient descent and the sigmoid function from scratch is excellent for building foundational knowledge. However, in an industry setting, writing custom implementations is inefficient and error-prone. 

Instead, data scientists rely on **`scikit-learn`**, the industry-standard machine learning library for Python. It provides highly optimized, production-ready algorithms.

The workflow for almost every model in `scikit-learn` follows a simple, consistent API:
1.  **Import:** Bring the model class into your script.
2.  **Instantiate:** Create an instance of the model (an object).
3.  **Fit:** Train the model using your feature matrix ($X$) and target labels ($y$).
4.  **Predict:** Use the trained model to make predictions on new data.

For Logistic Regression, `scikit-learn` provides two primary ways to output predictions:
* `predict()`: Outputs the final discrete class ($0$ or $1$).
* `predict_proba()`: Outputs the exact probability score before the threshold is applied.

## Short Examples
```python
from sklearn.linear_model import LogisticRegression

# 1. Instantiate
clf = LogisticRegression()

# 2. Fit (Train)
clf.fit(X_train, y_train)

# 3. Predict
predictions = clf.predict(X_test)
