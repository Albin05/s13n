# Lecture Script: Multi-class Classification Strategies

## Topic: Extending Logistic Regression beyond Binary Choices

### Why (Importance)
The real world rarely fits into neat "Yes or No" boxes. When you build a recommendation engine, you aren't just deciding between "Action" or "Comedy"—you have dozens of genres. When building self-driving car vision systems, the car must classify traffic signs into "Stop", "Yield", "Speed Limit 50", etc. Understanding how to scale a binary algorithm to handle $K$ classes is essential for solving these complex, real-world mapping problems.

### What (Concept)
Since standard Logistic Regression only knows how to separate data into two groups, we have two paths to scale it up:

**Path 1: The Meta-Strategy (One-vs-Rest / OvR)**
We don't change the algorithm; we change how we use it. If we have $K$ classes, we train $K$ separate binary logistic regression models.
* Model $1$ learns to separate Class $1$ from everything else.
* Model $2$ learns to separate Class $2$ from everything else.
When predicting, the model that screams the loudest (has the highest probability output) wins.

**Path 2: The Mathematical Upgrade (Multinomial / Softmax)**
We change the algorithm itself. Instead of Sigmoid, we use **Softmax**.
Softmax takes the raw linear scores ($z$) for all classes and normalizes them together. 
$$P(y=k | x) = \frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}$$
Because every score is divided by the sum of all scores, the resulting probabilities will always sum to exactly $1.0$.

### How (Method / Example)

Let's look at how seamless this is in Python. `scikit-learn` handles the heavy lifting for us.

**Code Example:**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Generate a synthetic dataset with 3 classes
X, y = make_classification(n_samples=100, n_features=4, n_classes=3, n_informative=3)

# Strategy 1: One-vs-Rest (OvR)
model_ovr = LogisticRegression(multi_class='ovr')
model_ovr.fit(X, y)
print("OvR Prediction:", model_ovr.predict([X[0]]))

# Strategy 2: Multinomial (Softmax)
model_multi = LogisticRegression(multi_class='multinomial')
model_multi.fit(X, y)
probs = model_multi.predict_proba([X[0]])
print("Softmax Probabilities:", probs)
print("Sum of Softmax Probabilities:", sum(probs[0])) # This will be exactly 1.0
