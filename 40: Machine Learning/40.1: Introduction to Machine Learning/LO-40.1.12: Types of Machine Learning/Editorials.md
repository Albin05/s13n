# Editorials

## Q1
### Title
Algorithm Input Requirements

### Problem Description
Identify the algorithm that trains without a target variable ($y$).

### Objective
Distinguish between Supervised and Unsupervised algorithms.

### Hint
Clustering algorithms look for patterns in $X$ alone.

### Short Explanation
Linear Regression, Logistic Regression, and Decision Trees are Supervised (require labels). K-Means is Unsupervised (no labels).

### Detailed Explanation
* **Linear Regression:** Predicts $y$ given $X$.
* **K-Means:** Groups $X$ into clusters. No $y$ needed.
* **Logistic Regression:** Classifies $X$ into $y$.
* Therefore, K-Means is the answer.

---

## Q2
### Title
Training Wrapper Logic

### Problem Description
Create a function that prints the training type based on the presence of labels.

### Objective
Implement simple logic to differentiate ML types programmatically.

### Hint
Use a standard `if/else` check on the `labels` argument.

### Short Explanation
Check if `labels is None`.

### Detailed Explanation
```python
def start_training(data, labels=None):
    if labels is not None:
        print("Starting Supervised Training")
        # train_model(data, labels)
    else:
        print("Starting Unsupervised Training")
        # train_model(data)
