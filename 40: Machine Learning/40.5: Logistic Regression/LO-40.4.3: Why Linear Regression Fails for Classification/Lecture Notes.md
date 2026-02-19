# Why Linear Regression Fails for Classification

## The Two Fatal Flaws

### 1. The Outlier Effect (Shifted Decision Boundary)
* **The Setup:** To use Linear Regression for classification, we set a threshold (usually $0.5$).
* **The Flaw:** Linear regression uses the Mean Squared Error (MSE) cost function. MSE heavily penalizes large errors.
* **The Result:** An extreme outlier will pull the regression line towards itself to minimize the squared distance. This flattens the slope of the line, shifting the $y=0.5$ intersection point. This causes the model to suddenly misclassify normal data points that it previously got right.

### 2. Unbounded Outputs (Nonsensical Probabilities)
* **The Setup:** In binary classification, we want the model's output to represent the probability $P(y=1|x)$.
* **The Flaw:** Probabilities are strictly bounded: $0 \le P \le 1$.
* **The Result:** The hypothesis function for linear regression is a straight line: $h_\theta(x) = \theta_0 + \theta_1 x$. This line extends to infinity in both directions. The model will frequently output values $< 0$ or $> 1$, which are impossible to interpret as probabilities.

## Conceptual Summary
Linear Regression asks "How much?" (Continuous).
Classification asks "Which one?" (Discrete).
Applying a "How much" algorithm to a "Which one" problem results in fragile boundaries and mathematical contradictions. We need an algorithm that inherently outputs values constrained between $0$ and $1$.

## Code Snippet: The Threshold Problem
```python
# If Linear Regression outputs 1.8 for a classification task...
prediction = 1.8

# We apply a threshold
predicted_class = 1 if prediction >= 0.5 else 0

# But what does 1.8 mean in probability? Nothing. 
# The model is conceptually mismatched.
