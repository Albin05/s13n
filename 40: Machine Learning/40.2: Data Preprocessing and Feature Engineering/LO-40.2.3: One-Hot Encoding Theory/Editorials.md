
# Editorials

## Q1
### Title
Label vs One-Hot Encoding

### Problem Description
Identify the downside of Label Encoding for Nominal data.

### Objective
Understand the mathematical implication of integer mapping.

### Hint
Is "Blue" (2) greater than "Red" (1)?

### Short Explanation
Label encoding imposes an arbitrary order (Rank) on data. A regression model might try to interpolate between 1 and 3 to get 2, which makes no sense for colors.

### Detailed Explanation
* **Label Encoding:** Maps Red $\to$ 1, Blue $\to$ 2, Green $\to$ 3. The model sees $3 > 1$.
* **Nominal Data:** There is no order.
* **Result:** The model learns a false relationship. OHE fixes this by orthogonalizing the categories.

---

## Q2
### Title
Pandas Implementation

### Problem Description
Apply `get_dummies` with prefix.

### Objective
Basic Pandas syntax for OHE.

### Hint
Use `pd.get_dummies(df, columns=['City'], prefix='City')`.

### Short Explanation
Standard pandas function handles the removal of original and prefixing automatically.

### Detailed Explanation
```python
import pandas as pd
def one_hot_encode_city(df):
    return pd.get_dummies(df, columns=['City'], prefix='City')

```

---

## Q3

### Title

Feature Expansion Calculation

### Problem Description

Calculate total columns after OHE.
Original: 1 Num, 1 Cat(4), 1 Cat(3).
Total rows: 10 (irrelevant for column count).

### Objective

Calculate dimensionality expansion.

### Hint

Sum the unique values plus the untouched numerical column.

### Short Explanation

.

### Detailed Explanation

1. **Numerical Col:** Stays as 1 column.
2. **Cat(4):** Becomes 4 binary columns.
3. **Cat(3):** Becomes 3 binary columns.
4. **Total:**  columns.
*(Note: If we dropped the first category, it would be . The question specified "without dropping").*

---

## Q4

### Title

OHE Pitfalls

### Problem Description

Identify when NOT to use OHE.

### Objective

Recognize High Cardinality and Ordinality issues.

### Hint

OHE explodes dimensions and destroys order.

### Short Explanation

A, C, and D are problematic. B is fine (low cardinality).

### Detailed Explanation

* **A (Problematic):** 40,000 new columns is too many (Curse of Dimensionality).
* **B (Fine):** 2 columns is negligible.
* **C (Problematic/Unnecessary):** Trees often prefer Label Encoding or native handling; OHE can actually make trees perform worse by splitting the data too sparsely.
* **D (Problematic):** OHE destroys the "Order" (1 < 5). Ordinal encoding is better.

---

## Q5

### Title

Avoiding Dummy Variable Trap

### Problem Description

Implement OHE with `drop_first=True`.

### Objective

Safe encoding practices.

### Hint

Pandas argument `drop_first=True`.

### Short Explanation

Pass the argument to the function.

### Detailed Explanation

```python
def encode_drop_first(df, col_name):
    return pd.get_dummies(df, columns=[col_name], drop_first=True)

```

---

## Q6

### Title

The Dummy Variable Trap

### Problem Description

Explain multicollinearity in OHE for "Season".

### Objective

Mathematical understanding of linear dependence.

### Hint

If Is_Spring=0, Is_Summer=0, and Is_Fall=0, what must Is_Winter be?

### Short Explanation

The columns sum to 1. If you know the state of  columns, the th column is perfectly predictable, causing multicollinearity which breaks linear regression models.

### Detailed Explanation

* **The Relationship:**  (Every row must be one season).
* **Redundancy:** .
* **Impact:** In Linear Regression (), if one variable is a linear combination of others, the matrix inversion fails (singular matrix) or weights become unstable. We drop one column to break this perfect correlation.

```

```
