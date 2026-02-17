
# Editorials

## Q1
### Title
Identifying Multi-Class Tasks

### Problem Description
Classify the task of predicting S, M, L, XL sizes.

### Objective
Distinguish between binary and multi-class classification.

### Hint
Are the outputs numbers or distinct categories? How many are there?

### Short Explanation
The output is a category (Size), not a continuous number. Since there are more than 2 categories (S, M, L, XL), it is **Multi-Class Classification**.

### Detailed Explanation
* **Regression:** Would predict exact measurements (e.g., 42cm shoulder width).
* **Binary Classification:** Would predict just two classes (e.g., Fits / Doesn't Fit).
* **Multi-Class:** Predicts one of several discrete options.

---

## Q2
### Title
Heuristic Type Checking

### Problem Description
Automate the detection of problem types based on the target array.

### Objective
Understand the data properties of targets.

### Hint
Floats usually imply continuous data. Integers with low cardinality imply classes.

### Short Explanation
Check data type and count unique values.

### Detailed Explanation
```python
def check_task_type(target_array):
    unique_vals = len(set(target_array))
    is_float = any(isinstance(x, float) for x in target_array)
    
    if is_float or unique_vals > 10:
        return "Regression"
    else:
        return "Classification"

```

---

## Q3

### Title

Thresholding Regression for Classification

### Problem Description

Convert a regression output (0.8) to a class label using threshold 0.5.

### Objective

Understand the link between probability estimation and classification.

### Hint

Is ?

### Short Explanation

, so the class is 1.

### Detailed Explanation

In binary classification, models often output a probability score. We apply a threshold (usually 0.5) to decide the hard label.

* If Score  Threshold  Class 1.
* If Score < Threshold  Class 0.
*  Class 1.

---

## Q4

### Title

Core Concepts

### Problem Description

Select true statements about the two types.

### Objective

Clarify common misconceptions.

### Hint

Logistic Regression is named confusingly.

### Short Explanation

B, C, and D are true. A is false.

### Detailed Explanation

* **A (False):** Logistic Regression is a *Classification* algorithm (despite the name).
* **B (True):** Binning Age (0-100) into Groups (Kid, Adult) converts Regression to Classification.
* **C (True):** Classification = Separation.
* **D (True):** Regression = Fitting/Approximation.

---

## Q5

### Title

Metric Conversion

### Problem Description

Calculate MAE (Regression) and Accuracy (Classification) on the same data.

### Objective

Contrast evaluation metrics.

### Hint

MAE = Avg(|diff|). Accuracy = Correct/Total.

### Short Explanation

MAE  0.3. Accuracy = 100%.

### Detailed Explanation

1. **MAE:** . Average = .
2. **Classification:**
* Preds: [12.5(>11), 10.1(<=11), 14.8(>11)]  [1, 0, 1]
* Actuals: [12(>11), 10(<=11), 15(>11)]  [1, 0, 1]
* Matches: 3/3.
* Accuracy: 100%.



---

## Q6

### Title

MSE for Classification

### Problem Description

Why is MSE bad for discrete classes?

### Objective

Theoretical understanding of loss functions.

### Hint

Does it make sense to say "Cat" is 0.5 units away from "Dog"?

### Short Explanation

MSE treats the output as a continuous quantity.

1. **Meaningless Distance:** It implies that Class 2 is "twice as much" as Class 1, which is false for Nominal data (e.g., Cat, Dog, Bird).
2. **Probability:** We want to penalize *wrong classes*, not geometric distance. Cross-Entropy Loss (Log Loss) is much better for classification because it penalizes confident wrong answers exponentially.

```

```
