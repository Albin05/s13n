
# Editorials

## Q1
### Title
Identifying the Target

### Problem Description
Identify the role of the "Spam/Not Spam" column.

### Objective
Distinguish Features from Labels.

### Hint
It's the answer the model is trying to learn.

### Short Explanation
The column containing the outcome we want to predict is the **Label** (or Target).

### Detailed Explanation
* **Features:** The email text, sender, time (Inputs).
* **Label:** The classification "Spam" (Output/Truth).

---

## Q2
### Title
Mean Absolute Error (MAE)

### Problem Description
Calculate the average of absolute differences.

### Objective
Implement a standard regression metric.

### Hint
Sum the absolute differences and divide by count.

### Short Explanation
$|10-12| + |20-18| = 2 + 2 = 4$. Average = $4 / 2 = 2.0$.

### Detailed Explanation
```python
def calculate_mae(y_true, y_pred):
    total_error = 0
    for t, p in zip(y_true, y_pred):
        total_error += abs(t - p)
    return total_error / len(y_true)

```

---

## Q3

### Title

Accuracy Calculation

### Problem Description

Calculate percentage of correct matches.
Correct: 80, Total: 100.

### Objective

Basic classification metric.

### Hint

(Correct / Total) * 100.

### Short Explanation

.

### Detailed Explanation

---

## Q4

### Title

Properties of Labels

### Problem Description

Select true statements about Labels.

### Objective

Understand the role of labels in different ML types.

### Hint

Do you need labels to group similar items (Clustering)? No.

### Short Explanation

A, B, and D are true. C is false (Labels can be categorical strings like "Cat").

### Detailed Explanation

* **A (True):** Supervised means "supervised by labels".
* **B (True):** Unsupervised means finding patterns without labels.
* **C (False):** Labels can be "Spam", "Benign", etc.
* **D (True):** Humans often have to manually label data (e.g., doctors labeling X-rays), which is costly.

---

## Q5

### Title

Accuracy Implementation

### Problem Description

Compare two lists and return accuracy percentage.

### Objective

Implement the logic behind the metric.

### Hint

Count where `preds[i] == labels[i]`.

### Short Explanation

Iterate, count matches, divide by length.

### Detailed Explanation

```python
def check_accuracy(predictions, labels):
    correct = 0
    for p, l in zip(predictions, labels):
        if p == l:
            correct += 1
    return (correct / len(labels)) * 100

```

Matches: 1st ('A'=='A'), 3rd ('A'=='A'). 2nd is mismatch. 2/3 = 66.6%.

---

## Q6

### Title

Training vs Test Accuracy

### Problem Description

Explain the discrepancy between performance on Training Labels vs Test Labels.

### Objective

Connect Labels/Predictions to Overfitting.

### Hint

If you memorize the answer key (Training Labels), you score high. If you take a new test (Test Labels), you might fail.

### Short Explanation

High Training Accuracy + Low Test Accuracy = **Overfitting**.

### Detailed Explanation

* **Training Accuracy:** How well the model's Predictions match the Labels it has *already seen*. The model can simply memorize these.
* **Test Accuracy:** How well the model's Predictions match Labels it has *never seen*. This measures **Generalization**.
* A large gap implies the model memorized the specific training labels (noise) instead of learning the underlying rule.

```

```
