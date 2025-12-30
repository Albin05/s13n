## Editorials: Use Fancy Indexing

### Q1 Solution: Select Specific Elements

```python
import numpy as np

# Create array
arr = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

# Select indices 0, 3, 7
result1 = arr[[0, 3, 7]]
print(f"Indices 0, 3, 7: {result1}")

# Select indices 2, 5, 8, 9
result2 = arr[[2, 5, 8, 9]]
print(f"Indices 2, 5, 8, 9: {result2}")

# Select last, first, middle (index 5)
result3 = arr[[-1, 0, 5]]
print(f"Last, first, middle: {result3}")

# Select with repetition: 1, 1, 4, 4
result4 = arr[[1, 1, 4, 4]]
print(f"Repeated indices: {result4}")
```

**Explanation:**
- Fancy indexing uses arrays/lists of indices: `arr[[0, 3, 7]]`
- Indices can be in any order
- Negative indices work: `-1` is last element
- Indices can be repeated: `[1, 1, 4, 4]` gets same element multiple times
- Result is a new array (copy, not view)

---

### Q2 Solution: Reorder Array Elements

```python
import numpy as np

# Create array
arr = np.array([100, 200, 300, 400, 500])

# Reverse using fancy indexing
reversed_arr = arr[[4, 3, 2, 1, 0]]
print(f"Reversed: {reversed_arr}")

# Rearrange to [300, 100, 500, 200, 400]
# Indices:      [2,   0,    4,    1,    3]
custom = arr[[2, 0, 4, 1, 3]]
print(f"Custom order: {custom}")

# Index order [4, 2, 0, 1, 3]
index_order = arr[[4, 2, 0, 1, 3]]
print(f"Index order [4,2,0,1,3]: {index_order}")

# Duplicate first element 5 times
first_5 = arr[[0, 0, 0, 0, 0]]
print(f"First element 5 times: {first_5}")
```

**Explanation:**
- Reverse by listing indices backwards: `[4, 3, 2, 1, 0]`
- Custom ordering: rearrange indices to desired order
- Map desired output to original indices
- Duplicating: repeat same index multiple times
- Fancy indexing creates copies, so reordering doesn't affect original

---

### Q3 Solution: Fancy Indexing with 2D Arrays

```python
import numpy as np

# Create matrix
matrix = np.array([[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120],
                   [130, 140, 150, 160]])

# Select rows 0 and 3
rows_0_3 = matrix[[0, 3]]
print("Rows 0 and 3:")
print(rows_0_3)

# Select rows 1, 2, 3
rows_1_2_3 = matrix[[1, 2, 3]]
print("\nRows 1, 2, 3:")
print(rows_1_2_3)

# Select specific elements: (0,0), (1,3), (3,2)
elements = matrix[[0, 1, 3], [0, 3, 2]]
print(f"\nSpecific elements: {elements}")

# Select rows 0,2 and columns 1,3
rows_cols = matrix[[0, 2]][:, [1, 3]]
print("\nRows 0,2 cols 1,3:")
print(rows_cols)

# Row 1 all columns
row_1 = matrix[1, :]
print(f"\nRow 1: {row_1}")

# Row 3 columns 0 and 2
row_3_cols = matrix[3, [0, 2]]
print(f"Row 3 selected: {row_3_cols}")
```

**Explanation:**
- Row selection: `matrix[[0, 3]]` selects entire rows
- Element selection: `matrix[[rows], [cols]]` pairs row and column indices
- `matrix[[0, 1, 3], [0, 3, 2]]` selects (0,0), (1,3), (3,2)
- Combined: `matrix[[0, 2]][:, [1, 3]]` first selects rows, then columns
- Single row: `matrix[1, :]` uses slicing for all columns
- Single row, specific cols: `matrix[3, [0, 2]]`

---

### Q4 Solution: Modify Using Fancy Indexing

```python
import numpy as np

# Create array
data = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Print original
print(f"Original: {data}")

# Set indices 1, 4, 6 to 999
data[[1, 4, 6]] = 999
print(f"After setting to 999: {data}")

# Reset for next operation
data = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(f"Reset data: {data}")

# Set indices 0, 2, 4, 6 to [100, 200, 300, 400]
data[[0, 2, 4, 6]] = [100, 200, 300, 400]
print(f"After custom values: {data}")

# Triple values at indices 3, 5, 7
data[[3, 5, 7]] = data[[3, 5, 7]] * 3
print(f"After tripling: {data}")
```

**Explanation:**
- `data[[indices]] = value` sets all selected elements to same value
- `data[[indices]] = [values]` assigns different values (must match length)
- For operations: `data[[indices]] = data[[indices]] * 3`
  - Left side: selects elements to modify
  - Right side: gets current values and applies operation
- Fancy indexing modifies original array in-place
- Number of values must match number of indices

---

### Q5 Solution: Extract Top Performers

```python
import numpy as np

# Sales data
sales = np.array([1200, 1800, 950, 2200, 1500, 1100, 2000, 1300])
employees = np.array(['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace', 'Henry'])

# Find indices sorted in descending order
sorted_indices = np.argsort(sales)[::-1]
print(f"Sorted indices (desc): {sorted_indices}")

# Top 3 indices
top_3_indices = sorted_indices[:3]
print(f"Top 3 indices: {top_3_indices}")

# Top 3 sales
top_3_sales = sales[top_3_indices]
print(f"Top 3 sales: {top_3_sales}")

# Top 3 employees
top_3_employees = employees[top_3_indices]
print(f"Top 3 employees: {top_3_employees}")

# Bottom 2 performers
bottom_2_indices = sorted_indices[-2:][::-1]
bottom_2_employees = employees[bottom_2_indices]
bottom_2_sales = sales[bottom_2_indices]
print(f"Bottom 2 employees: {bottom_2_employees}")
print(f"Bottom 2 sales: {bottom_2_sales}")
```

**Explanation:**
- `np.argsort(sales)` returns indices that would sort array in ascending order
- `[::-1]` reverses to get descending order
- `sorted_indices[:3]` gets first 3 indices (top performers)
- Use these indices with fancy indexing: `sales[top_3_indices]`
- Works on any array with same indices: `employees[top_3_indices]`
- Bottom performers: `sorted_indices[-2:][::-1]` gets last 2 and reverses
- Fancy indexing essential for parallel arrays (sales & names)

**Key Concepts Covered:**
1. Basic fancy indexing for selecting specific elements
2. Reordering and duplicating elements
3. 2D array fancy indexing (rows, columns, specific elements)
4. Modifying values through fancy indexing
5. Practical applications with `np.argsort()` for ranking and selection
