# Lecture Script: Introduction to Logarithmic Functions

## Topic: Why Logarithms matter in Machine Learning

### Why (Importance)
As we transition from Linear Regression to Logistic Regression, we hit a mathematical roadblock. How do we calculate the "error" or "cost" when our predictions are probabilities between $0$ and $1$? If we use Mean Squared Error (MSE), the mathematics become non-convex—meaning gradient descent gets stuck. We need a mathematical function that severely penalizes the model when it is confidently wrong. The Logarithm is the mathematical tool that provides exactly this behavior.

### What (Concept)
A logarithm asks a simple question: "To what exponent must I raise the base to get this number?"
We focus on the **Natural Logarithm**, denoted as $\ln(x)$ or $\log_e(x)$, where the base is $e \approx 2.718$.

**Key Rules to Memorize:**
1.  $\log(1) = 0$
2.  $\log(e) = 1$
3.  $\log(a \cdot b) = \log(a) + \log(b)$
4.  $\log(a / b) = \log(a) - \log(b)$

Most importantly for us, consider the **domain and range**:
* You cannot input a negative number or zero into a logarithm.
* As $x$ approaches $0$, $\log(x)$ approaches $-\infty$. 
* If we multiply it by negative one, $-\log(x)$ approaches $+\infty$ as $x$ approaches $0$.

### How (Method / Example)
Let's see how $-\log(x)$ acts as a penalty function.
Imagine our model outputs a probability $p$ that an image is a dog. The image is indeed a dog (Class 1).

* **Scenario A:** Model predicts $p = 0.99$ (Highly confident and correct).
    Penalty = $-\log(0.99) \approx 0.01$. The penalty is near zero. Good!
* **Scenario B:** Model predicts $p = 0.5$ (Unsure).
    Penalty = $-\log(0.5) \approx 0.69$. Moderate penalty.
* **Scenario C:** Model predicts $p = 0.01$ (Highly confident but WRONG).
    Penalty = $-\log(0.01) \approx 4.60$. Large penalty!
* **Scenario D:** Model predicts $p = 0.0001$.
    Penalty = $-\log(0.0001) \approx 9.21$. Massive penalty!

As $p \to 0$, the error shoots to infinity. This is the exact behavior we need to train classification models effectively.

**Code Example:**
```python
import numpy as np

probabilities = np.array([0.99, 0.5, 0.01, 0.0001])
# Calculate the penalty for being wrong when the true class is 1
penalties = -np.log(probabilities)

for p, penalty in zip(probabilities, penalties):
    print(f"Prediction: {p:.4f} -> Penalty: {penalty:.4f}")
