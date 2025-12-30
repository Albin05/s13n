## Use Boolean Indexing

### Creating Boolean Arrays

**Comparison operators create boolean arrays:**

```python
import numpy as np

arr = np.array([10, 25, 30, 15, 40, 5, 35])

# Comparisons return boolean arrays
mask = arr > 20
print(mask)  # [False  True  True False  True False  True]

# Different operators
print(arr >= 25)   # Greater than or equal
print(arr < 15)    # Less than
print(arr == 30)   # Equal to
print(arr != 10)   # Not equal to
```

---

### Basic Boolean Indexing

**Filter elements using boolean arrays:**

```python
arr = np.array([10, 25, 30, 15, 40, 5, 35])

# Create and use mask
mask = arr > 20
filtered = arr[mask]
print(filtered)  # [25 30 40 35]

# Direct (one-liner)
result = arr[arr > 20]
print(result)  # [25 30 40 35]
```

**How it works:**
```
Original:  [10, 25, 30, 15, 40,  5, 35]
Mask:      [ F,  T,  T,  F,  T,  F,  T]
Result:        [25, 30,     40,     35]
```

---

### Combining Conditions

**Logical operators:**

```python
arr = np.array([10, 25, 30, 15, 40, 5, 35])

# AND (&) - Both conditions True
result = arr[(arr >= 15) & (arr <= 35)]
print(result)  # [25 30 15 35]

# OR (|) - At least one condition True
result = arr[(arr < 15) | (arr > 35)]
print(result)  # [10  5 40]

# NOT (~) - Invert condition
result = arr[~((arr >= 20) & (arr <= 30))]
print(result)  # [10 15 40  5 35]
```

**Important:** Always use parentheses around each condition!

---

### Boolean Indexing with 2D Arrays

```python
matrix = np.array([[10, 25, 30],
                   [15, 40, 5],
                   [35, 20, 45]])

# Filter all values > 25
result = matrix[matrix > 25]
print(result)  # [30 40 35 45] (1D array)

# Filter rows by column condition
matrix = np.array([[1, 100, 3],
                   [4, 50, 6],
                   [7, 150, 9]])

# Rows where second column > 75
rows = matrix[matrix[:, 1] > 75]
# [[  1 100   3]
#  [  7 150   9]]
```

---

### Modifying with Boolean Indexing

**Update filtered elements:**

```python
arr = np.array([10, 25, 30, 15, 40, 5, 35])

# Cap values at 30
arr[arr > 30] = 30
print(arr)  # [10 25 30 15 30  5 30]

# Double values < 20
arr[arr < 20] = arr[arr < 20] * 2
print(arr)  # [20 25 30 30 30 10 30]
```

---

### Practical Examples

**Filter student scores:**

```python
scores = np.array([85, 92, 78, 65, 88, 91, 72, 95])

# Passed (>= 75)
passed = scores[scores >= 75]
print(f"Passed: {passed}")  # [85 92 78 88 91 72 95]

# A grades (>= 90)
a_grade = scores[scores >= 90]
print(f"A grades: {a_grade}")  # [92 91 95]
```

**Temperature analysis:**

```python
temps = np.array([32, 28, 35, 42, 38, 25, 30, 45])

# Comfortable range (30-38)
comfortable = temps[(temps >= 30) & (temps <= 38)]
print(f"Comfortable: {comfortable}")  # [32 35 38 30]
```

**Sales filtering:**

```python
sales = np.array([1200, 800, 1500, 600, 2000, 900, 1800])

# High performance (>= 1500)
high = sales[sales >= 1500]
avg = high.mean()
print(f"High performers avg: {avg}")  # 1775.0
```

---

### Key Takeaways

1. **Creating boolean arrays:**
   - Use: `>`, `<`, `>=`, `<=`, `==`, `!=`
   - Result: boolean array (True/False)

2. **Boolean indexing:**
   - Syntax: `arr[condition]`
   - Returns: elements where condition is True

3. **Combining conditions:**
   - AND: `(cond1) & (cond2)`
   - OR: `(cond1) | (cond2)`
   - NOT: `~(condition)`

4. **Modifying:**
   - `arr[condition] = new_value`
   - Updates filtered elements in-place

**Remember:**
- Boolean indexing filters based on conditions
- Very efficient (no loops needed)
- Always use parentheses for combined conditions
- Essential for data filtering and cleaning
