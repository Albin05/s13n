
# Editorials

## Q1
### Title
Identifying Selection Methods

### Problem Description
Identify the iterative feature removal method.

### Objective
Distinguish between Filter, Wrapper, and Embedded types.

### Hint
"Recursive" implies repeating a process.

### Short Explanation
RFE (Recursive Feature Elimination) is a Wrapper method that repeatedly builds a model and removes the weakest feature.

### Detailed Explanation
* **Filter:** Looks at stats only (no training).
* **Wrapper (RFE):** Trains, checks weights, removes weakest, repeats.
* **Embedded:** Penalizes weights during one training run.
* **Answer:** B (RFE).

---

## Q2
### Title
Dropping Constant Columns

### Problem Description
Remove columns with 0 variance.

### Objective
Data cleaning / Basic Feature Selection.

### Hint
Use `df.nunique() == 1`.

### Short Explanation
Identify columns with only 1 unique value and drop them.

### Detailed Explanation
```python
def remove_constant_columns(df):
    return df.loc[:, df.nunique() > 1]

```

Alternatively, using VarianceThreshold from sklearn:

```python
from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold(threshold=0)
selector.fit(df)

```

---

## Q3

### Title

Combinatorial Explosion

### Problem Description

Calculate total subsets for 10 features.

### Objective

Understand why "Brute Force" feature selection is impossible for large datasets.

### Hint

.

### Short Explanation

.

### Detailed Explanation

The number of subsets of a set of size  is .
Since we exclude the empty set (training with 0 features), it is .

---

## Q4

### Title

Reasons to Drop Features

### Problem Description

Select valid criteria for removing columns.

### Objective

Apply heuristics for data cleaning.

### Hint

Does the feature help predict?

### Short Explanation

A, B, and D are valid reasons. C (High correlation with Target) is the *best* reason to KEEP a feature.

### Detailed Explanation

* **A (True):** 99% missing means mostly empty; usually dropped.
* **B (True):** Unique IDs (like "Row 1", "Row 2") have no predictive pattern.
* **C (False):** Correlation with Target = Signal. Keep it!
* **D (True):** Duplicates are redundant (Multicollinearity). Drop one.

---

## Q5

### Title

Correlation Filtering

### Problem Description

Select features based on correlation threshold > 0.5.

### Objective

Implement a Filter method.

### Hint

Calculate correlation matrix, select target column, filter by value.

### Short Explanation

Use `df.corr()[target]` and apply condition `abs(corr) > 0.5`.

### Detailed Explanation

```python
def select_features(df, target):
    correlations = df.corr()[target]
    # Filter where abs(correlation) > 0.5, exclude target itself
    selected = correlations[abs(correlations) > 0.5].index.tolist()
    if target in selected:
        selected.remove(target)
    return selected

```

---

## Q6

### Title

Filter vs Wrapper

### Problem Description

Compare the two main approaches to feature selection.

### Objective

Deep dive into the trade-off between speed and accuracy.

### Hint

Filter = General stats. Wrapper = Trial and error with the model.

### Short Explanation

Filter methods look at intrinsic properties (like variance) and are fast but ignore how features interact inside the model. Wrapper methods treat the model as a "black box" and test combinations (trial and error), which finds better feature subsets for that specific model but is very slow because it retrains the model many times.

### Detailed Explanation

1. **Filter:** Fast, Model-Agnostic. It asks: "Is this feature generally useful?" (e.g., Correlation). It might miss a feature that is only useful when combined with another feature.
2. **Wrapper:** Slow, Model-Specific. It asks: "Does adding this feature improve *this specific model's* accuracy?" It detects feature interactions but requires training  models, making it computationally expensive for large datasets.

```

```
