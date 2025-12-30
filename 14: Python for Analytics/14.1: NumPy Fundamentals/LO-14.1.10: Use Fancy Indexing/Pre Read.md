## Pre-Read: Use Fancy Indexing

### What You'll Learn

In this session, you'll master fancy indexing - an advanced NumPy technique that allows you to select, reorder, and manipulate array elements using arrays of indices. This powerful feature goes beyond basic slicing to give you complete control over element selection.

### Why It Matters

Fancy indexing is essential for:

1. **Non-contiguous selection**: Select specific elements scattered across an array
2. **Data reordering**: Rearrange elements in any custom order
3. **Advanced filtering**: Select elements based on sorted indices or rankings
4. **Multi-array operations**: Use same indices across multiple related arrays

Real-world examples:
- Select top N performers from ranked data
- Reorder rows/columns in specific patterns
- Extract elements at specific positions
- Sample random elements from datasets

### Key Concepts Preview

**Fancy Indexing:**
- Use arrays or lists of indices to select elements
- Indices can be in any order and can repeat
- Works with both 1D and 2D arrays
- Creates copies (not views)

**Basic syntax:**
```python
arr = np.array([10, 20, 30, 40, 50])

# Select specific indices
result = arr[[0, 2, 4]]  # [10, 30, 50]

# Reorder elements
result = arr[[4, 2, 0]]  # [50, 30, 10]

# Repeat indices
result = arr[[1, 1, 3]]  # [20, 20, 40]
```

**2D fancy indexing:**
```python
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

# Select rows
rows = matrix[[0, 2]]  # Rows 0 and 2

# Select specific elements
elements = matrix[[0, 1, 2], [0, 2, 1]]  # Elements at (0,0), (1,2), (2,1)
```

### What to Expect

You'll learn:
1. Basic fancy indexing with 1D arrays
2. Using negative indices
3. Fancy indexing with 2D arrays
4. Combining fancy indexing with slicing
5. Modifying values through fancy indexing
6. Practical applications like selecting top performers

### Prepare

Make sure you have:
- NumPy installed
- Understanding of basic indexing and slicing
- Completed previous indexing lessons (boolean indexing)
- Familiarity with `np.argsort()` is helpful but not required

### Quick Example

Try to predict the output:
```python
arr = np.array([100, 200, 300, 400, 500])

# What will these produce?
result1 = arr[[1, 3]]  # ?
result2 = arr[[4, 3, 2, 1, 0]]  # ?
result3 = arr[[0, 0, 1, 1]]  # ?

# 2D example
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

result4 = matrix[[0, 2]]  # ?
result5 = matrix[[0, 1, 2], [2, 1, 0]]  # ?
```

Answers:
- result1: [200, 400]
- result2: [500, 400, 300, 200, 100] (reversed)
- result3: [100, 100, 200, 200] (repeated)
- result4: [[1, 2, 3], [7, 8, 9]] (rows 0 and 2)
- result5: [3, 5, 7] (diagonal elements in reverse)

### Fancy Indexing vs Slicing

**Key difference:**
- **Slicing** (`arr[1:4]`): Creates views, contiguous elements only
- **Fancy indexing** (`arr[[1, 3, 5]]`): Creates copies, any elements in any order

Fancy indexing gives you complete flexibility for advanced array manipulation!
