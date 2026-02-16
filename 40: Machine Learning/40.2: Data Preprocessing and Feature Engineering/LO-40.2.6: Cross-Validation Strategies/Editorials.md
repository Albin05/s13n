
# Editorials

## Q1
### Title
LOOCV Training Size

### Problem Description
Identify the training set size for LOOCV.

### Objective
Understand the extreme limit of K-Fold.

### Hint
We leave ONE out.

### Short Explanation
In LOOCV, we hold out 1 sample for testing. Therefore, the remaining $N-1$ samples are used for training.

### Detailed Explanation
* **Test Set:** Size 1.
* **Train Set:** Size $N - 1$.
* **Iterations:** $N$ times.

---

## Q2
### Title
Stratified K-Fold Iterator

### Problem Description
Iterate through stratified folds and print indices.

### Objective
Visualize how indices are selected.

### Hint
Use `skf.split(X, y)`.

### Short Explanation
Instantiate `StratifiedKFold`, loop through split.

### Detailed Explanation
```python
from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=3)
for train_index, test_index in skf.split(X, y):
    print("TRAIN:", train_index, "TEST:", test_index)

```

---

## Q3

### Title

Mean CV Score

### Problem Description

Calculate average of 10 scores.

### Objective

Basic metric aggregation.

### Hint

Sum / 10.

### Short Explanation

Sum is 8.06. Average is 0.806.

### Detailed Explanation

---

## Q4

### Title

Benefits of CV

### Problem Description

Select advantages of CV.

### Objective

Justify the extra computation time.

### Hint

More tests = More reliability.

### Short Explanation

A, B, and D are true. C is false (It is  times slower).

### Detailed Explanation

* **A (True):** Averaging reduces the luck factor.
* **B (True):** Reduces variance in the estimate.
* **C (False):** It requires training the model  times, making it slower.
* **D (True):** Every point gets a chance to be in the test set.

---

## Q5

### Title

Manual LOOCV

### Problem Description

Simulate LOOCV logic.

### Objective

Understand the underlying indexing.

### Hint

Use list slicing or exclusion.

### Short Explanation

Loop index `i`. Test is `data[i]`. Train is `data[:i] + data[i+1:]`.

### Detailed Explanation

```python
data = [10, 20, 30]
for i in range(len(data)):
    test = [data[i]]
    train = data[:i] + data[i+1:]
    print(f"Train: {train}, Test: {test}")

```

---

## Q6

### Title

Computational Cost

### Problem Description

Assess feasibility of 10-Fold CV for slow models.

### Objective

Practical engineering constraints.

### Hint

.

### Short Explanation

It will take 10 hours. This is often not feasible for large Deep Learning models.

### Detailed Explanation

* **Trade-off:** We gain a statistically robust performance estimate, but we pay with time.
* **Calculation:** 1 hour/run  10 runs = 10 hours.
* **Real-world:** For massive models (like GPT or ResNet training on ImageNet), we usually stick to a single Train-Test-Validation split because 10-Fold CV would take weeks or months.

```

```
