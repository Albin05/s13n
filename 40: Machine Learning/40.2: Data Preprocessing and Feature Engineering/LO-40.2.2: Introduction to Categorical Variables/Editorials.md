
# Editorials

## Q1
### Title
Encoding Techniques

### Problem Description
Identify the method that expands columns.

### Objective
Distinguish between Label and One-Hot encoding.

### Hint
"One-Hot" means one column is hot (active) for each category.

### Short Explanation
**One-Hot Encoding** creates a separate binary column for each unique category (e.g., `is_Red`, `is_Blue`).

### Detailed Explanation
* **Label Encoding:** Converts to 1, 2, 3 in a single column.
* **One-Hot Encoding:** Explodes the single column into $N$ binary columns.
* **Answer:** C.

---

## Q2
### Title
Manual Ordinal Mapping

### Problem Description
Map 'Low', 'Medium', 'High' to 1, 2, 3.

### Objective
Implement Label Encoding manually to preserve order.

### Hint
Use a dictionary `{'Low': 1, ...}` and a list comprehension.

### Short Explanation
Create a mapping dict and apply it to the list.

### Detailed Explanation
```python
def map_ordinal(categories):
    mapping = {'Low': 1, 'Medium': 2, 'High': 3}
    return [mapping[c] for c in categories]

```

---

## Q3

### Title

One-Hot Dimensionality

### Problem Description

Calculate new columns for 5 unique cities.

### Objective

Understand the impact of high cardinality on dataset width.

### Hint

One column per unique value.

### Short Explanation

5 unique values = 5 new columns.

### Detailed Explanation

One-Hot Encoding creates a binary vector of length , where  is the number of unique categories.
Unique Cities: 5  New Columns: 5.
(Note: Sometimes we drop one column to avoid multicollinearity, making it , but the standard definition implies  binary vectors).

---

## Q4

### Title

Identifying Nominal Data

### Problem Description

Select variables with no intrinsic order.

### Objective

Classify variable types correctly.

### Hint

Is a Poodle "greater than" a Beagle?

### Short Explanation

A and C are Nominal. B and D are Ordinal.

### Detailed Explanation

* **A (Nominal):** Zip codes are labels for regions. 90210 isn't "better" or "more" than 10001 mathematically.
* **B (Ordinal):** 5 stars > 1 star.
* **C (Nominal):** Breeds are just names.
* **D (Ordinal):** PhD > High School (in terms of education years).

---

## Q5

### Title

Checking Cardinality

### Problem Description

Count unique values in a Pandas column.

### Objective

Data exploration skills.

### Hint

`df['col'].nunique()`.

### Short Explanation

Use the built-in pandas function.

### Detailed Explanation

```python
def get_cardinality(df):
    return df['Category'].nunique()

```

---

## Q6

### Title

Numerical vs Categorical Ambiguity

### Problem Description

Explain why Zip Code is categorical.

### Objective

Prevent the common mistake of treating ID numbers as quantities.

### Hint

Does (Zip Code A + Zip Code B) / 2 mean anything?

### Short Explanation

Zip Codes are labels (Nominal). Numerical operations like average, sum, or multiplication are meaningless on Zip Codes.

### Detailed Explanation

* **Numerical Variables:** Quantities where math makes sense. (Average Age = Valid).
* **Categorical Variables:** Labels. (Average Zip Code = 54321... this corresponds to a place in Wisconsin, which is physically meaningless as an "average" of Beverly Hills and New York).
* Treating Zip Codes as numerical implies that a higher zip code is "more" than a lower one, which confuses the model. They should be treated as Nominal categories.

```

```
