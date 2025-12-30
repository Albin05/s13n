### Use Fancy Indexing

### Hook (2 minutes)

"What if you need to select specific elements from an array, but not in a continuous sequence? Maybe you need the 1st, 5th, and 9th elements, or you want to reorder array elements. Fancy indexing allows you to use arrays of indices to select exactly the elements you want, in any order you want. This powerful technique unlocks advanced array manipulation that goes beyond simple slicing!"

### Section 1: Basic Fancy Indexing with 1D Arrays (3 minutes)

**Using an array of indices:**

```python
import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# Select specific indices
indices = [0, 3, 5, 8]
result = arr[indices]
print(result)  # [10 40 60 90]
```

**Directly with list:**

```python
# Without storing indices
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

**Repeated indices:**

```python
arr = np.array([10, 20, 30, 40, 50])

# Can repeat indices
result = arr[[0, 2, 2, 1, 4]]
print(result)  # [10 30 30 20 50]
```

**Reordering elements:**

```python
arr = np.array([10, 20, 30, 40, 50])

# Reverse using indices
result = arr[[4, 3, 2, 1, 0]]
print(result)  # [50 40 30 20 10]

# Custom order
result = arr[[2, 0, 4, 1, 3]]
print(result)  # [30 10 50 20 40]
```

### Section 2: Fancy Indexing with Negative Indices (2 minutes)

**Mixing positive and negative indices:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Mix positive and negative
indices = [0, -1, 2, -2]
result = arr[indices]
print(result)  # [10 70 30 60]
```

**Understanding negative indices:**
```
Array:       [10, 20, 30, 40, 50, 60, 70]
Positive:     0   1   2   3   4   5   6
Negative:    -7  -6  -5  -4  -3  -2  -1

arr[[0, -1, 2]] selects:
        [10,         70, 30]
```

### Section 3: Fancy Indexing with 2D Arrays (4 minutes)

**Selecting specific rows:**

```python
import numpy as np

matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90],
                   [100, 110, 120]])

# Select rows 0, 2, 3
rows = matrix[[0, 2, 3]]
print(rows)
# [[ 10  20  30]
#  [ 70  80  90]
#  [100 110 120]]
```

**Selecting specific elements (rows and columns):**

```python
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

# Select elements at (0,0), (1,2), (2,1)
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

**Broadcasting with fancy indexing:**

```python
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

# Select multiple columns from specific rows
rows = [[0, 1]]
cols = [[0, 2]]
result = matrix[rows, cols]
print(result)  # [[10 60]]
```

### Section 4: Combining Fancy Indexing with Slicing (3 minutes)

**Fancy indexing for rows, slicing for columns:**

```python
import numpy as np

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

# Select rows 0 and 2, all columns
result = matrix[[0, 2], :]
print(result)
# [[ 1  2  3  4]
#  [ 9 10 11 12]]

# Select rows 1 and 3, columns 1-3
result = matrix[[1, 3], 1:4]
print(result)
# [[ 6  7  8]
#  [14 15 16]]
```

**Slicing for rows, fancy indexing for columns:**

```python
# Select first 2 rows, columns 0 and 3
result = matrix[:2, [0, 3]]
print(result)
# [[1 4]
#  [5 8]]
```

### Section 5: Modifying Values with Fancy Indexing (2 minutes)

**Update specific elements:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

# Modify elements at indices 1, 3, 5
arr[[1, 3, 5]] = 999
print(arr)  # [ 10 999  30 999  50 999]
```

**Set different values:**

```python
arr = np.array([10, 20, 30, 40, 50])

# Assign different values to each index
arr[[0, 2, 4]] = [100, 200, 300]
print(arr)  # [100  20 200  40 300]
```

**Conditional updates on specific indices:**

```python
arr = np.array([10, 20, 30, 40, 50, 60])

# Double values at specific indices
indices = [1, 3, 5]
arr[indices] = arr[indices] * 2
print(arr)  # [ 10  40  30  80  50 120]
```

### Section 6: Practical Applications (3 minutes)

**Example 1: Select top performers**

```python
import numpy as np

sales = np.array([1200, 1500, 800, 2000, 1100, 1800, 950])
names = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

# Get indices of top 3 performers
top_3_indices = np.argsort(sales)[-3:][::-1]
print(f"Top 3 indices: {top_3_indices}")  # [3 5 1]

# Get top 3 sales
top_sales = sales[top_3_indices]
print(f"Top sales: {top_sales}")  # [2000 1800 1500]

# Get top 3 names
top_names = names[top_3_indices]
print(f"Top performers: {top_names}")  # ['D' 'F' 'B']
```

**Example 2: Shuffle and sample data**

```python
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Random sample of 4 elements
random_indices = np.random.choice(len(arr), size=4, replace=False)
sample = arr[random_indices]
print(f"Random sample: {sample}")
```

**Example 3: Rearrange rows in specific order**

```python
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12]])

# Custom order for rows
new_order = [3, 0, 2, 1]
reordered = data[new_order]
print("Reordered:")
print(reordered)
# [[10 11 12]
#  [ 1  2  3]
#  [ 7  8  9]
#  [ 4  5  6]]
```

### Summary (1 minute)

**Key Takeaways:**

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

**Next Steps:**
You now have complete mastery of NumPy indexing techniques - from basic slicing to boolean and fancy indexing!
