
# Editorials

## Q1
### Title
Pandas Dummy Trap Parameter

### Problem Description
Identify the correct parameter to drop the first column.

### Objective
Syntax check for `get_dummies`.

### Hint
We want to **drop** the **first** column.

### Short Explanation
The parameter is `drop_first=True`.

### Detailed Explanation
`pd.get_dummies(df, drop_first=True)` removes the first category level to generate $N-1$ columns, avoiding perfect multicollinearity.

---

## Q2
### Title
Handling Unseen Categories

### Problem Description
Default behavior of `OneHotEncoder` on new data.

### Objective
Understand the robustness of Sklearn encoders.

### Hint
By default, Sklearn is strict.

### Short Explanation
It throws an error by default unless `handle_unknown='ignore'` is set.

### Detailed Explanation
* **Default:** Raises `ValueError: Found unknown categories`.
* **With `handle_unknown='ignore'`:** Encodes as a row of zeros.
* **With `handle_unknown='infrequent_if_exist'`:** Maps to an "infrequent" bin.
* **Answer:** A.

---

## Q3
### Title
Dropped Column Count

### Problem Description
Calculate columns for 5 categories with `drop='first'`.

### Objective
Calculate dimensions after encoding.

### Hint
$N - 1$.

### Short Explanation
$5 - 1 = 4$.

### Detailed Explanation
If a feature has $N$ unique values, standard OHE produces $N$ columns. Setting `drop='first'` removes 1 column (the reference category).
Result: $5 - 1 = 4$.

---

## Q4
### Title
Pipeline Advantages

### Problem Description
Why choose Sklearn over Pandas for ML?

### Objective
Understand best practices for production code.

### Hint
Think about consistency and error handling.

### Short Explanation
A, B, and D are valid reasons. C is not necessarily true (Pandas is very optimized for speed).

### Detailed Explanation
* **A (True):** Compatible with `sklearn.pipeline.Pipeline`.
* **B (True):** Can handle new data gracefully.
* **C (False):** Speed depends on data size/type; not the primary reason.
* **D (True):** It stores the "vocabulary" of categories.

---

## Q5
### Title
Sklearn Implementation

### Problem Description
Code a robust encoder for 'A', 'B' and test on 'C'.

### Objective
Demonstrate `handle_unknown`.

### Hint
Instantiate -> Fit -> Transform.

### Short Explanation
'C' will result in `[0, 0]` because it was not in fit data.

### Detailed Explanation
```python
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Instantiate
enc = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

# Fit
X_train = np.array([['A'], ['B']])
enc.fit(X_train)

# Transform
X_test = np.array([['A'], ['C']])
print(enc.transform(X_test))
# Output:
# [[1. 0.]   <- 'A' (Learned)
#  [0. 0.]]  <- 'C' (Unknown, ignored)

```

---

## Q6

### Title

Train-Test Skew with Pandas

### Problem Description

Explain column mismatch when using `get_dummies` twice.

### Objective

Highlight the danger of stateless encoding.

### Hint

Train has 'Apple', 'Banana'. Test has only 'Apple'.

### Short Explanation

`get_dummies` looks only at the data provided *at that moment*. It has no memory.

### Detailed Explanation

* **Scenario:**
* Train Data: `['Red', 'Blue']`. `get_dummies` creates 2 columns: `Is_Red`, `Is_Blue`.
* Test Data: `['Red', 'Red']` (No Blue present).


* **Result:** `get_dummies` on Test Data creates only 1 column: `Is_Red`.
* **Failure:** The model expects 2 columns (`Is_Red`, `Is_Blue`) but receives only 1. The code crashes or produces garbage predictions. Sklearn prevents this by enforcing the schema learned during `.fit()`.

```

```
