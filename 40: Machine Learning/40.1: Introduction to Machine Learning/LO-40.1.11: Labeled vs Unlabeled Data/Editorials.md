
# Editorials

## Q1
### Title
Identifying Labeled Data

### Problem Description
Identify the data type of a spam dataset with "Spam"/"Not Spam" marks.

### Objective
Recognize labeled data by the presence of a target variable.

### Hint
Does the data have an "answer key" (tags)?

### Short Explanation
Since every email has a specific tag ("Spam" or "Not Spam") defining its category, it is Labeled Data.

### Detailed Explanation
Labeled data consists of input data (the email content) and a label (the category). The label acts as the ground truth that the model tries to predict. Without the "Spam/Not Spam" tag, it would just be a collection of text (Unlabeled).

---

## Q2
### Title
Separating Features and Labels

### Problem Description
Split a list of `(features, label)` tuples into separate lists `X` and `y`.

### Objective
Data manipulation to prepare labeled data for training.

### Hint
Iterate through the list and append the first element to X and the second to y.

### Short Explanation
Unpack the tuples in a loop or list comprehension.

### Detailed Explanation
```python
def split_data(dataset):
    X = []
    y = []
    for features, label in dataset:
        X.append(features)
        y.append(label)
    return X, y

```

This separates the inputs (for the model to analyze) from the targets (for the model to learn to predict).

---

## Q3

### Title

Cleaning Labeled Data

### Problem Description

Calculate remaining rows after dropping missing labels.

### Objective

Understand that Supervised Learning requires complete labels.

### Hint

Total rows - Rows with missing labels.

### Short Explanation

.

### Detailed Explanation

In Supervised Learning, you cannot train on data that lacks a target (label).

1. Total rows: 100
2. Missing labels: 20
3. Usable Labeled Data: .

---

## Q4

### Title

Scenarios for Unlabeled Data

### Problem Description

Select scenarios that use Unlabeled Data.

### Objective

Differentiate between Supervised (Labeled) and Unsupervised (Unlabeled) tasks.

### Hint

Look for tasks where the "answer" is unknown or where we are just finding structure.

### Short Explanation

A and C involve finding patterns/structure without predefined answers. B and D use known history/tags (Labeled).

### Detailed Explanation

* **A (True):** Grouping (Clustering) is done on unlabeled data to find natural segments.
* **B (False):** "Known fraud cases" implies labels exist.
* **C (True):** PCA (Dimensionality Reduction) looks at the internal structure of features (Unlabeled).
* **D (False):** "Cat tags" explicitly mentions labels.

---

## Q5

### Title

Rule-Based Labeling

### Problem Description

Manually assign labels (0 or 1) based on a threshold rule.

### Objective

Demonstrate how unlabeled data can be converted to labeled data using simple logic (Weak Supervision).

### Hint

Loop through dictionary values and apply an `if-else` condition.

### Short Explanation

Apply logic: `label = 1 if value > 50 else 0`.

### Detailed Explanation

```python
def label_data(data_dict):
    labeled_list = []
    for key, val in data_dict.items():
        label = 1 if val > 50 else 0
        labeled_list.append({'val': val, 'label': label})
    return labeled_list

```

This simulates the process of "Annotating" data, turning raw numbers into a dataset ready for classification.

---

## Q6

### Title

The Cold Start Problem

### Problem Description

Startup has images (Unlabeled) but needs to detect defects (requires Labeled).

### Objective

Analyze the cost/benefit of data labeling.

### Hint

You cannot train a supervised detector without examples of defects.

### Short Explanation

The problem is they have Input () but no Output (). They cannot train a supervised model. Solution: Manual annotation or Active Learning.

### Detailed Explanation

* **The Problem:** The startup possesses **Unlabeled Data**. Standard defect detection is a Supervised Learning task (Classification), which requires **Labeled Data** (examples of "Defect" vs "Good").
* **The Solution:**
1. **Manual Labeling:** Hire humans to review a subset of images and tag them.
2. **Semi-Supervised Learning:** Label a small set and propagate labels to similar images.
3. **Anomaly Detection:** Treat the majority of images as "Normal" and look for outliers (Unsupervised approach), though this is less accurate than a trained classifier.



```

```
