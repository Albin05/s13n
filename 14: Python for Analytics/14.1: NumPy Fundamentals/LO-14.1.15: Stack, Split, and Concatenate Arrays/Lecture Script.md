## Stack, Split, and Concatenate Arrays

### Hook (2 minutes)

**Scenario:**
You have monthly sales data from 12 different regions, each stored in separate arrays. How do you combine them into a single dataset for analysis?

Or you have a large dataset that you need to split into training, validation, and test sets. How do you divide the array efficiently?

These operations - stacking, splitting, and concatenating - are essential for data manipulation, model preparation, and batch processing in data science.

**What You'll Learn:**
1. Concatenate arrays along existing axes
2. Stack arrays to create new dimensions
3. Split arrays into multiple sub-arrays
4. Choose the right combination method
5. Apply these operations to real-world data tasks

---

### Section 1: Concatenating Arrays (4 minutes)

**Basic Concatenation:**

```python
import numpy as np

# 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.concatenate([arr1, arr2])
print(result)
# [1 2 3 4 5 6]
```

**Concatenating 2D Arrays:**

```python
# Vertical concatenation (axis=0)
mat1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

mat2 = np.array([[7, 8, 9],
                 [10, 11, 12]])

result = np.concatenate([mat1, mat2], axis=0)
print("Axis=0 (rows):")
print(result)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

print(f"Shape: {result.shape}")  # (4, 3)
```

```python
# Horizontal concatenation (axis=1)
result = np.concatenate([mat1, mat2], axis=1)
print("\nAxis=1 (columns):")
print(result)
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]

print(f"Shape: {result.shape}")  # (2, 6)
```

**Multiple Arrays:**

```python
# Concatenate 3+ arrays
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
arr3 = np.array([5, 6])
arr4 = np.array([7, 8])

result = np.concatenate([arr1, arr2, arr3, arr4])
print(result)
# [1 2 3 4 5 6 7 8]
```

**Key Points:**
- Arrays must have same shape except in concatenation axis
- axis=0: vertical (add rows)
- axis=1: horizontal (add columns)
- Use list of arrays as input

---

### Section 2: Vertical and Horizontal Stacking (4 minutes)

**vstack() - Vertical Stacking:**

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.vstack([arr1, arr2])
print("vstack:")
print(result)
# [[1 2 3]
#  [4 5 6]]

print(f"Shape: {result.shape}")  # (2, 3)
```

```python
# vstack with 2D arrays
mat1 = np.array([[1, 2, 3]])
mat2 = np.array([[4, 5, 6]])

result = np.vstack([mat1, mat2])
print(result)
# [[1 2 3]
#  [4 5 6]]
```

**hstack() - Horizontal Stacking:**

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.hstack([arr1, arr2])
print("hstack:")
print(result)
# [1 2 3 4 5 6]

print(f"Shape: {result.shape}")  # (6,)
```

```python
# hstack with 2D arrays
mat1 = np.array([[1, 2],
                 [3, 4]])

mat2 = np.array([[5, 6],
                 [7, 8]])

result = np.hstack([mat1, mat2])
print(result)
# [[1 2 5 6]
#  [3 4 7 8]]

print(f"Shape: {result.shape}")  # (2, 4)
```

**vstack vs concatenate:**

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# These are equivalent for 1D arrays
v1 = np.vstack([arr1, arr2])
v2 = np.concatenate([arr1.reshape(1, -1), arr2.reshape(1, -1)], axis=0)

print(np.array_equal(v1, v2))  # True
```

**When to use which:**
- vstack/hstack: More intuitive, automatic dimension handling
- concatenate: More explicit control over axis

---

### Section 3: General Stacking with stack() (3 minutes)

**Basic stack():**

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Stack along new axis 0
result = np.stack([arr1, arr2], axis=0)
print("Stack axis=0:")
print(result)
# [[1 2 3]
#  [4 5 6]]

print(f"Shape: {result.shape}")  # (2, 3)
```

```python
# Stack along new axis 1
result = np.stack([arr1, arr2], axis=1)
print("\nStack axis=1:")
print(result)
# [[1 4]
#  [2 5]
#  [3 6]]

print(f"Shape: {result.shape}")  # (3, 2)
```

**Difference from concatenate:**

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# stack creates new dimension
stacked = np.stack([arr1, arr2])
print(f"Stack: {stacked.shape}")  # (2, 3) - NEW dimension

# concatenate uses existing dimension
concat = np.concatenate([arr1, arr2])
print(f"Concatenate: {concat.shape}")  # (6,) - SAME dimension
```

**3D Stacking:**

```python
# Stack multiple 2D arrays into 3D
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
mat3 = np.array([[9, 10], [11, 12]])

result = np.stack([mat1, mat2, mat3], axis=0)
print(f"3D shape: {result.shape}")  # (3, 2, 2)

# Access first matrix
print("First matrix:\n", result[0])
# [[1 2]
#  [3 4]]
```

---

### Section 4: Splitting Arrays (4 minutes)

**split() - Equal Splits:**

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Split into 3 equal parts
parts = np.split(arr, 3)
print("Split into 3:")
for i, part in enumerate(parts):
    print(f"Part {i+1}: {part}")
# Part 1: [1 2 3]
# Part 2: [4 5 6]
# Part 3: [7 8 9]
```

**split() with Indices:**

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Split at indices 3 and 7
parts = np.split(arr, [3, 7])
print("Split at [3, 7]:")
for i, part in enumerate(parts):
    print(f"Part {i+1}: {part}")
# Part 1: [1 2 3]
# Part 2: [4 5 6 7]
# Part 3: [ 8  9 10]
```

**2D Array Splits:**

```python
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

# Split rows
row_parts = np.split(matrix, 2, axis=0)
print("Split rows:")
for i, part in enumerate(row_parts):
    print(f"Part {i+1}:\n{part}\n")
# Part 1:
# [[1 2 3 4]
#  [5 6 7 8]]
#
# Part 2:
# [[ 9 10 11 12]
#  [13 14 15 16]]
```

```python
# Split columns
col_parts = np.split(matrix, 2, axis=1)
print("Split columns:")
for i, part in enumerate(col_parts):
    print(f"Part {i+1}:\n{part}\n")
# Part 1:
# [[ 1  2]
#  [ 5  6]
#  [ 9 10]
#  [13 14]]
```

**vsplit() and hsplit():**

```python
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])

# Vertical split (rows)
v_parts = np.vsplit(matrix, 2)
print("vsplit:")
for part in v_parts:
    print(part)
# [[1 2 3 4]]
# [[5 6 7 8]]

# Horizontal split (columns)
h_parts = np.hsplit(matrix, 2)
print("\nhsplit:")
for part in h_parts:
    print(part)
# [[1 2]
#  [5 6]]
# 
# [[3 4]
#  [7 8]]
```

---

### Section 5: array_split() for Unequal Splits (2 minutes)

**When split() Fails:**

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# This fails - not evenly divisible
# np.split(arr, 3)  # ValueError

# Use array_split instead
parts = np.array_split(arr, 3)
print("Unequal split:")
for i, part in enumerate(parts):
    print(f"Part {i+1}: {part}")
# Part 1: [1 2 3 4]
# Part 2: [5 6 7]
# Part 3: [ 8  9 10]
```

**Difference:**

| Function | Requirement | Error on Unequal |
|----------|-------------|------------------|
| split() | Must divide evenly | Yes |
| array_split() | Can divide unevenly | No |

**Use Cases:**

```python
# Train-test split (80-20)
data = np.arange(100)

# Split at index 80
train, test = np.split(data, [80])
print(f"Train size: {len(train)}")  # 80
print(f"Test size: {len(test)}")    # 20
```

```python
# Train-val-test (70-15-15)
train, val, test = np.split(data, [70, 85])
print(f"Train: {len(train)}, Val: {len(val)}, Test: {len(test)}")
# Train: 70, Val: 15, Test: 15
```

---

### Section 6: Practical Applications (3 minutes)

**Application 1: Combining Data from Multiple Sources**

```python
import numpy as np

# Monthly sales from different regions
region1 = np.array([100, 150, 200])
region2 = np.array([120, 180, 220])
region3 = np.array([90, 140, 190])

# Stack into single dataset
all_regions = np.vstack([region1, region2, region3])
print("All regions:\n", all_regions)
# [[100 150 200]
#  [120 180 220]
#  [ 90 140 190]]

# Total sales per month
monthly_total = all_regions.sum(axis=0)
print(f"Monthly totals: {monthly_total}")
# [310 470 610]
```

**Application 2: Batch Processing**

```python
# Individual samples
sample1 = np.array([1, 2, 3, 4, 5])
sample2 = np.array([6, 7, 8, 9, 10])
sample3 = np.array([11, 12, 13, 14, 15])

# Create batch
batch = np.stack([sample1, sample2, sample3])
print(f"Batch shape: {batch.shape}")  # (3, 5)

# Process batch
normalized = (batch - batch.mean(axis=1, keepdims=True)) / batch.std(axis=1, keepdims=True)
print("Normalized batch:\n", normalized)
```

**Application 3: Train-Validation-Test Split**

```python
# Dataset with 100 samples
X = np.random.rand(100, 10)  # 100 samples, 10 features
y = np.random.randint(0, 2, 100)  # Binary labels

# Split into 70-15-15
X_train, X_val, X_test = np.split(X, [70, 85])
y_train, y_val, y_test = np.split(y, [70, 85])

print(f"Train: {X_train.shape}")  # (70, 10)
print(f"Val: {X_val.shape}")      # (15, 10)
print(f"Test: {X_test.shape}")    # (15, 10)
```

**Application 4: Time Series Windowing**

```python
# Daily data
daily_data = np.arange(1, 31)  # 30 days

# Split into weeks
weeks = np.array_split(daily_data, 4)
print("Weekly splits:")
for i, week in enumerate(weeks):
    print(f"Week {i+1}: {week}")
```

**Application 5: Feature Engineering**

```python
# Original features
features1 = np.array([[1, 2], [3, 4], [5, 6]])
features2 = np.array([[7, 8], [9, 10], [11, 12]])

# Combine features horizontally
combined = np.hstack([features1, features2])
print("Combined features:\n", combined)
# [[ 1  2  7  8]
#  [ 3  4  9 10]
#  [ 5  6 11 12]]
```

---

### Summary (1 minute)

**Key Concepts Covered:**

1. **Concatenating:**
   - `np.concatenate([arr1, arr2], axis=0)` - join along existing axis
   - axis=0: vertical (rows)
   - axis=1: horizontal (columns)

2. **Stacking:**
   - `np.vstack([arr1, arr2])` - stack vertically
   - `np.hstack([arr1, arr2])` - stack horizontally
   - `np.stack([arr1, arr2], axis=0)` - create new dimension

3. **Splitting:**
   - `np.split(arr, n)` - split into n equal parts
   - `np.split(arr, [i, j])` - split at indices
   - `np.vsplit(arr, n)` - split rows
   - `np.hsplit(arr, n)` - split columns
   - `np.array_split(arr, n)` - allow unequal splits

**Quick Reference:**

```python
# Combine
np.concatenate([a, b], axis=0)  # Along existing axis
np.vstack([a, b])               # Vertical
np.hstack([a, b])               # Horizontal
np.stack([a, b], axis=0)        # New dimension

# Split
np.split(arr, 3)                # Into 3 parts
np.split(arr, [2, 5])           # At indices
np.array_split(arr, 3)          # Unequal OK
```

**Remember:**
- concatenate: existing axis
- stack: new axis
- split: equal parts
- array_split: unequal OK
- Choose based on data structure and task

**Next Steps:**
- Practice with different array shapes
- Combine with reshaping operations
- Apply to real datasets
- Build data pipelines

These operations are fundamental for data preprocessing, feature engineering, and model preparation!
