# Introduction to Classification

## Key Concepts
* **Supervised Learning:** Classification is a type of supervised learning where the target variable is categorical.
* **Discrete Output:** The output is a label, not a quantity.
* **Decision Boundary:** A hypersurface that partitions the underlying vector space into two or more sets, one for each class.

## Types of Classification
1.  **Binary Classification:**
    * Two possible outcomes.
    * Examples: Spam/Ham, Fraud/Legit, Pass/Fail.
    * Usually encoded as 0 (Negative class) and 1 (Positive class).
2.  **Multi-class Classification:**
    * More than two classes.
    * Example: Classifying types of flowers (Setosa, Versicolor, Virginica).

## Classification vs. Regression

| Feature | Regression | Classification |
| :--- | :--- | :--- |
| **Output Type** | Continuous (Numbers) | Discrete (Labels) |
| **Question Asked** | "How much?" or "How many?" | "Which category?" |
| **Example** | Predicting Temperature | Predicting if it will Rain (Yes/No) |

## Code Snippet: Loading a Classification Dataset
```python
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset (Classic classification problem)
data = load_iris()
X = data.data
y = data.target # Target is discrete: 0, 1, or 2

print(f"Target Labels: {set(y)}")
# Output: Target Labels: {0, 1, 2}
