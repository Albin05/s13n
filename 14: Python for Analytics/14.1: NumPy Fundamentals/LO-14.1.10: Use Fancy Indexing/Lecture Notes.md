## Use Fancy Indexing

### Basic Fancy Indexing with 1D Arrays

**Using arrays of indices:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# Select specific indices
result = arr[[0, 3, 5, 8]]
print(result)  # [10 40 60 90]

# Directly with list
result = arr[[1, 4, 7]]
print(result)  # [20 50 80]
```

**How it works:**
```
Array:    [10, 20, 30, 40, 50, 60, 70, 80, 90]
Indices:   0   1   2   3   4   5   6   7   8

arr[[0, 3, 5]] selects:
       [10,     40,     60]
```

**Repeated indices and reordering:**

```python
arr = np.array([10, 20, 30, 40, 50])

# Repeat indices
result = arr[[0, 2, 2, 1, 4]]
print(result)  # [10 30 30 20 50]

# Reverse using indices
result = arr[[4, 3, 2, 1, 0]]
print(result)  # [50 40 30 20 10]

# Custom order
result = arr[[2, 0, 4, 1, 3]]
print(result)  # [30 10 50 20 40]
```

---

### Fancy Indexing with Negative Indices

**Mixing positive and negative indices:**

```python
arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Mix positive and negative
result = arr[[0, -1, 2, -2]]
print(result)  # [10 70 30 60]
```

**Understanding:**
```
Array:       [10, 20, 30, 40, 50, 60, 70]
Positive:     0   1   2   3   4   5   6
Negative:    -7  -6  -5  -4  -3  -2  -1
```

---

### Fancy Indexing with 2D Arrays

**Selecting rows:**

```python
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90],
                   [100, 110, 120]])

# Select rows 0, 2, 3
rows = matrix[[0, 2, 3]]
# [[ 10  20  30]
#  [ 70  80  90]
#  [100 110 120]]
```

**Selecting specific elements:**

```python
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

# Elements at (0,0), (1,2), (2,1)
row_indices = [0, 1, 2]
col_indices = [0, 2, 1]
result = matrix[row_indices, col_indices]
print(result)  # [10 60 80]
```

**How 2D fancy indexing works:**
```
Matrix:
    Col 0  Col 1  Col 2
Row 0:  10     20     30
Row 1:  40     50     60
Row 2:  70     80     90

matrix[[0, 1, 2], [0, 2, 1]] selects:
       (0,0)  (1,2)  (2,1)
        10,    60,    80
```

---

### Combining Fancy Indexing with Slicing

**Fancy indexing for rows, slicing for columns:**

```python
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

# Rows 0 and 2, all columns
result = matrix[[0, 2], :]
# [[ 1  2  3  4]
#  [ 9 10 11 12]]

# Rows 1 and 3, columns 1-3
result = matrix[[1, 3], 1:4]
# [[ 6  7  8]
#  [14 15 16]]
```

**Slicing for rows, fancy indexing for columns:**

```python
# First 2 rows, columns 0 and 3
result = matrix[:2, [0, 3]]
# [[1 4]
#  [5 8]]
```

---

### Modifying Values with Fancy Indexing

**Update specific elements:**

```python
arr = np.array([10, 20, 30, 40, 50, 60])

# Modify elements at indices 1, 3, 5
arr[[1, 3, 5]] = 999
print(arr)  # [ 10 999  30 999  50 999]
```

**Set different values:**

```python
arr = np.array([10, 20, 30, 40, 50])

# Assign different values
arr[[0, 2, 4]] = [100, 200, 300]
print(arr)  # [100  20 200  40 300]
```

**Conditional updates:**

```python
arr = np.array([10, 20, 30, 40, 50, 60])

# Double values at specific indices
indices = [1, 3, 5]
arr[indices] = arr[indices] * 2
print(arr)  # [ 10  40  30  80  50 120]
```

---

### Practical Applications

**Select top performers:**

```python
import numpy as np

sales = np.array([1200, 1500, 800, 2000, 1100, 1800, 950])
names = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

# Get indices of top 3
top_3_indices = np.argsort(sales)[-3:][::-1]
print(f"Top 3 indices: {top_3_indices}")  # [3 5 1]

# Get top 3 sales and names
top_sales = sales[top_3_indices]
print(f"Top sales: {top_sales}")  # [2000 1800 1500]

top_names = names[top_3_indices]
print(f"Top performers: {top_names}")  # ['D' 'F' 'B']
```

**Rearrange rows in specific order:**

```python
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12]])

# Custom order for rows
new_order = [3, 0, 2, 1]
reordered = data[new_order]
# [[10 11 12]
#  [ 1  2  3]
#  [ 7  8  9]
#  [ 4  5  6]]
```

---

### Key Takeaways

1. **Basic fancy indexing:**
   - Use arrays/lists of indices: `arr[[0, 2, 5]]`
   - Select elements in any order
   - Can repeat indices

2. **2D fancy indexing:**
   - Select rows: `matrix[[0, 2]]`
   - Select specific elements: `matrix[[rows], [cols]]`
   - Combine with slicing

3. **Modification:**
   - `arr[[indices]] = new_values`
   - Update specific elements

4. **Advantages:**
   - Select non-contiguous elements
   - Reorder elements easily
   - Powerful for data manipulation

**Differences from slicing:**
- Slicing: Contiguous elements, creates views
- Fancy indexing: Any elements, creates copies

**Remember:**
- Fancy indexing uses arrays of indices
- Returns copies, not views
- Very flexible for custom selections
- Essential for advanced array manipulation
