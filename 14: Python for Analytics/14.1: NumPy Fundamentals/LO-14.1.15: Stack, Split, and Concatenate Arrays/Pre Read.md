## Pre-Read: Stack, Split, and Concatenate Arrays

### What You'll Learn

In this session, you'll master the essential techniques for combining and dividing NumPy arrays - fundamental operations for data manipulation, feature engineering, and building data pipelines in data science.

### Why It Matters

Array combination and splitting are crucial for:

1. **Data Integration**: Combine data from multiple sources
2. **Batch Processing**: Group samples for efficient computation
3. **Train-Test Splits**: Divide datasets for machine learning
4. **Feature Engineering**: Merge and separate feature sets
5. **Memory Management**: Process large datasets in chunks

Real-world examples:
- Combining sales data from multiple regions
- Creating training batches for neural networks
- Splitting time series into train/validation/test sets
- Merging features from different data sources
- Processing image datasets in batches

### Key Concepts Preview

**Concatenation:**
- Joins arrays along existing dimensions
- Like adding rows or columns to a table

**Stacking:**
- Creates new dimensions
- Useful for batch creation

**Splitting:**
- Divides arrays into parts
- Essential for cross-validation

**Basic examples:**
```python
import numpy as np

# Concatenate
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.concatenate([arr1, arr2])
# [1 2 3 4 5 6]

# Stack
result = np.vstack([arr1, arr2])
# [[1 2 3]
#  [4 5 6]]

# Split
arr = np.array([1, 2, 3, 4, 5, 6])
parts = np.split(arr, 3)
# [array([1, 2]), array([3, 4]), array([5, 6])]
```

### What to Expect

You'll learn:
1. Concatenate arrays with `np.concatenate()`
2. Stack arrays vertically and horizontally
3. Use `np.vstack()`, `np.hstack()`, and `np.stack()`
4. Split arrays into equal parts
5. Use `np.split()`, `np.vsplit()`, and `np.hsplit()`
6. Handle unequal splits with `np.array_split()`
7. Build data processing pipelines

### Prepare

Make sure you have:
- NumPy installed
- Understanding of array shapes
- Knowledge of array indexing
- Familiarity with array dimensions

### Quick Examples

**Combining Data:**
```python
import numpy as np

# Three data sources
sales_q1 = np.array([100, 150, 200])
sales_q2 = np.array([120, 180, 220])
sales_q3 = np.array([110, 160, 210])

# Stack into single dataset
all_sales = np.vstack([sales_q1, sales_q2, sales_q3])
# [[100 150 200]
#  [120 180 220]
#  [110 160 210]]

# Total sales per product
totals = all_sales.sum(axis=0)
# [330 490 630]
```

**Splitting for Train-Test:**
```python
# Dataset
data = np.arange(100)

# 80-20 split
train, test = np.split(data, [80])
print(f"Train: {len(train)}, Test: {len(test)}")
# Train: 80, Test: 20
```

**Horizontal vs Vertical:**
```python
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])

# Vertical split (rows)
top, bottom = np.vsplit(matrix, 2)
# top: [[1 2 3 4]]
# bottom: [[5 6 7 8]]

# Horizontal split (columns)
left, right = np.hsplit(matrix, 2)
# left: [[1 2], [5 6]]
# right: [[3 4], [7 8]]
```

### Common Operations

**Concatenate:**
- `np.concatenate([a, b], axis=0)` - vertical
- `np.concatenate([a, b], axis=1)` - horizontal

**Stack:**
- `np.vstack([a, b])` - stack rows
- `np.hstack([a, b])` - stack columns
- `np.stack([a, b])` - create new dimension

**Split:**
- `np.split(arr, 3)` - into 3 parts
- `np.split(arr, [2, 5])` - at indices
- `np.vsplit(arr, 2)` - split rows
- `np.hsplit(arr, 2)` - split columns

### Try to Predict

```python
import numpy as np

# What will be the shapes?
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result1 = np.vstack([a, b])      # Shape?
result2 = np.hstack([a, b])      # Shape?
result3 = np.stack([a, b], axis=0)  # Shape?

# What will split produce?
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
parts = np.split(arr, 4)         # How many parts? Size of each?

# Will this work?
arr = np.array([1, 2, 3, 4, 5])
parts = np.split(arr, 2)         # Error or success?
```

Answers:
- result1 shape: (2, 3)
- result2 shape: (6,)
- result3 shape: (2, 3)
- split into 4: [2, 2, 2, 2]
- split by 2: Error! (5 not divisible by 2 - use array_split)

### When to Use What

**Use concatenate when:**
- Joining along existing dimension
- Need explicit axis control
- Working with multi-dimensional arrays

**Use vstack/hstack when:**
- Simple vertical/horizontal joins
- More readable code
- Working with 1D or 2D arrays

**Use stack when:**
- Creating batches
- Need new dimension
- Building 3D from 2D arrays

**Use split when:**
- Equal division needed
- Creating folds for cross-validation
- Processing in chunks

**Use array_split when:**
- Unequal division acceptable
- Array not evenly divisible
- Flexible chunking needed

These operations are the building blocks for data manipulation pipelines!
