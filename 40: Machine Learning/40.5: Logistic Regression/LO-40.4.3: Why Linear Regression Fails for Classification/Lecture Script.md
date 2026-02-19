# Lecture Script: Why Linear Regression Fails for Classification

## Topic: The Breakdown of OLS on Discrete Targets

### Why (Importance)
Before we can appreciate Logistic Regression, we must understand why we can't just use Linear Regression. Why build a whole new mathematical framework? Because using the wrong tool for the job doesn't just give suboptimal results; it gives logically impossible results and creates fragile systems that break the moment an outlier appears.

### What (Concept)
Let's attempt to use Linear Regression $h_\theta(x) = \theta^T x$ for a binary classification problem where $y \in \{0, 1\}$. 
We apply a simple threshold:
* Predict $1$ if $h_\theta(x) \ge 0.5$
* Predict $0$ if $h_\theta(x) < 0.5$

**Failure Point 1: Outliers Destroy the Decision Boundary**
Because Linear Regression minimizes Mean Squared Error (MSE), it tries to keep the line as close to *all* points as possible. An extreme outlier in Class $1$ (say, an extremely large tumor that is definitively malignant) generates a huge squared error if the line stays steep. To minimize this error, the line flattens. 
When the line flattens, the point on the x-axis where $y = 0.5$ shifts to the right. This means data points that were correctly classified before the outlier was added are now misclassified. A model shouldn't get *worse* because it saw an overwhelmingly obvious example of Class $1$.

**Failure Point 2: Invalid Probabilities**
A straight line $y = mx + c$ goes from $-\infty$ to $\infty$. For very small or very large values of $x$, $h_\theta(x)$ will output values like $-2$ or $5$. You cannot tell a patient there is a $-200\%$ chance they have a disease. It breaks the fundamental axioms of probability.

### How (Method / Example)

Let's look at how the code proves this failure.

**Code Example:**
```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Scenario 1: Well-behaved data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([0, 0, 1, 1, 1])

model = LinearRegression()
model.fit(X, y)
print(f"Prediction for X=10: {model.predict([[10]])[0]:.2f}") 
# Output will be > 1. (Failure Point 2)

# Scenario 2: Adding an outlier
X_outlier = np.array([[1], [2], [3], [4], [5], [20]]) # 20 is a massive outlier
y_outlier = np.array([0, 0, 1, 1, 1, 1])

model_outlier = LinearRegression()
model_outlier.fit(X_outlier, y_outlier)

# Check the prediction for X=3 (which is definitely Class 1)
print(f"Prediction for X=3 (Without Outlier): {model.predict([[3]])[0]:.2f}")
print(f"Prediction for X=3 (With Outlier): {model_outlier.predict([[3]])[0]:.2f}")
# The prediction for X=3 drops significantly when the outlier is added, 
# potentially pushing it below the 0.5 threshold! (Failure Point 1)
