# Lecture Script: Implementing Logistic Regression in Python

## Topic: Moving from Math to Code with Scikit-Learn

### Why (Importance)
You have learned the math behind the linear combination, the sigmoid squishing function, and probability thresholds. But building a recommendation system or a churn predictor from raw math arrays would take days. Libraries like `scikit-learn` bundle all of this complex calculus and linear algebra into three or four lines of Python code. Knowing how to interface with this API is what turns theoretical knowledge into tangible, deployable software. 

### What (Concept)
We are going to use the `LogisticRegression` class from `sklearn.linear_model`. 
This class expects two things to learn:
1.  $X$: The feature matrix. It must be a 2D array (e.g., a pandas DataFrame or a 2D NumPy array).
2.  $y$: The target array. It must be a 1D array of categorical labels.

Once trained, the model object holds the optimal weights ($\theta$) in its attributes (specifically `.coef_` for the weights and `.intercept_` for the bias). 

### How (Method / Example)
Let's build a mini classification pipeline.

**Step 1: The Setup**
We need data. Let's use NumPy to create a quick dataset representing study hours ($X$) and whether the student passed the exam ($y$).

```python
import numpy as np
from sklearn.linear_model import LogisticRegression

# Features: Hours studied (Must be a 2D array!)
X = np.array([[1.0], [1.5], [2.5], [5.0], [5.5], [7.0]])
# Target: 0 (Fail), 1 (Pass)
y = np.array([0, 0, 0, 1, 1, 1])

Step 2: Initialize and Train
We create the model object and call .fit(). Under the hood, this runs the optimization algorithms to find the best line to separate our classes.

Python
# Initialize
model = LogisticRegression()

# Train the model
model.fit(X, y)
Step 3: Make Predictions
Now let's see what the model thinks about a student who studied for 3.5 hours and one who studied for 6 hours.

Python
X_new = np.array([[3.5], [6.0]])

# Get hard class predictions (0 or 1)
hard_predictions = model.predict(X_new)
print(f"Predicted Classes: {hard_predictions}") 
# Output likely: [0, 1]

# Get the raw probabilities
probabilities = model.predict_proba(X_new)
print(f"Probabilities:\n{probabilities}")
Notice predict_proba() returns a 2D array. The first column is the probability of Class 0, and the second column is the probability of Class 1. For the 6-hour student, the Class 1 probability might be 0.85, meaning an 85% chance of passing.

URLs for Demos

Google Colab: Getting Started with Scikit-learn
