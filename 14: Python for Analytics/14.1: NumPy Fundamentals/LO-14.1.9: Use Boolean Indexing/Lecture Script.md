### Use Boolean Indexing

### Hook (2 minutes)

"Imagine filtering a dataset of thousands of records to find only those meeting specific criteria - sales above a threshold, temperatures below freezing, or students who passed. Boolean indexing makes this incredibly simple and efficient in NumPy. Instead of writing loops, you can select elements based on conditions with a single line of code. This powerful technique is fundamental to data filtering and analysis!"

### Section 1: Creating Boolean Arrays (3 minutes)

**Boolean arrays from comparisons:**

```python
import numpy as np

# Create array
arr = np.array([10, 25, 30, 15, 40, 5, 35])

# Create boolean array using comparison
mask = arr > 20
print(mask)
# [False  True  True False  True False  True]

# Different comparisons
print(arr >= 25)   # [False  True  True False  True False  True]
print(arr < 15)    # [False False False False False  True False]
print(arr == 30)   # [False False  True False False False False]
print(arr != 10)   # [False  True  True  True  True  True  True]
```

**How it works:**
- Comparison operators create boolean arrays
- Each element is compared individually
- Result is True/False for each position
- Same shape as original array

**Boolean array properties:**

```python
arr = np.array([10, 25, 30, 15, 40])
mask = arr > 20

print(type(mask))        # <class 'numpy.ndarray'>
print(mask.dtype)        # bool
print(mask.shape)        # (5,)
```

### Section 2: Basic Boolean Indexing (3 minutes)

**Using boolean arrays to filter:**

```python
import numpy as np

arr = np.array([10, 25, 30, 15, 40, 5, 35])

# Create mask
mask = arr > 20

# Use mask to filter
filtered = arr[mask]
print(filtered)  # [25 30 40 35]
```

**Direct boolean indexing (one-liner):**

```python
# Without storing mask
result = arr[arr > 20]
print(result)  # [25 30 40 35]
```

**How boolean indexing works:**
```
Original:  [10, 25, 30, 15, 40,  5, 35]
Mask:      [ F,  T,  T,  F,  T,  F,  T]
Result:        [25, 30,     40,     35]
```

**Different conditions:**

```python
arr = np.array([10, 25, 30, 15, 40, 5, 35])

# Less than
print(arr[arr < 20])      # [10 15  5]

# Equal to
print(arr[arr == 30])     # [30]

# Not equal
print(arr[arr != 25])     # [10 30 15 40  5 35]

# Greater than or equal
print(arr[arr >= 30])     # [30 40 35]
```

### Section 3: Combining Conditions (4 minutes)

**Logical operators for multiple conditions:**

**AND (`&`)** - Both conditions must be True:

```python
import numpy as np

arr = np.array([10, 25, 30, 15, 40, 5, 35])

# Values between 15 and 35 (inclusive)
result = arr[(arr >= 15) & (arr <= 35)]
print(result)  # [25 30 15 35]
```

**OR (`|`)** - At least one condition must be True:

```python
# Values less than 15 OR greater than 35
result = arr[(arr < 15) | (arr > 35)]
print(result)  # [10  5 40]
```

**NOT (`~`)** - Inverts the condition:

```python
# Values NOT between 20 and 30
result = arr[~((arr >= 20) & (arr <= 30))]
print(result)  # [10 15 40  5 35]
```

**Important: Use parentheses!**

```python
# CORRECT (with parentheses)
arr[(arr > 10) & (arr < 30)]

# WRONG (without parentheses) - will cause error
# arr[arr > 10 & arr < 30]
```

**Complex conditions:**

```python
arr = np.array([5, 10, 15, 20, 25, 30, 35, 40])

# Multiple conditions
result = arr[(arr > 10) & (arr < 30) & (arr != 20)]
print(result)  # [15 25]

# OR with multiple conditions
result = arr[(arr < 10) | (arr > 35)]
print(result)  # [ 5 40]
```

### Section 4: Boolean Indexing with 2D Arrays (3 minutes)

**Filtering 2D arrays:**

```python
import numpy as np

matrix = np.array([[10, 25, 30],
                   [15, 40, 5],
                   [35, 20, 45]])

# Get all values greater than 25
result = matrix[matrix > 25]
print(result)  # [30 40 35 45] (1D array)

# Filter and get original positions preserved
mask = matrix > 25
print(mask)
# [[False False  True]
#  [False  True False]
#  [ True False  True]]
```

**Row and column filtering:**

```python
# Filter entire rows based on condition in specific column
matrix = np.array([[1, 100, 3],
                   [4, 50, 6],
                   [7, 150, 9]])

# Get rows where second column > 75
rows = matrix[matrix[:, 1] > 75]
print(rows)
# [[  1 100   3]
#  [  7 150   9]]
```

### Section 5: Modifying Values with Boolean Indexing (2 minutes)

**Update filtered elements:**

```python
import numpy as np

arr = np.array([10, 25, 30, 15, 40, 5, 35])

# Set all values greater than 30 to 30 (cap values)
arr[arr > 30] = 30
print(arr)  # [10 25 30 15 30  5 30]
```

**Conditional updates:**

```python
arr = np.array([10, 25, 30, 15, 40, 5, 35])

# Double values less than 20
arr[arr < 20] = arr[arr < 20] * 2
print(arr)  # [20 25 30 30 40 10 35]
```

**Replace with different value:**

```python
arr = np.array([10, 25, 30, 15, 40, 5, 35])

# Replace negative or zero with 0 (data cleaning)
arr[arr <= 0] = 0
```

### Section 6: Practical Applications (3 minutes)

**Example 1: Filter student scores**

```python
import numpy as np

scores = np.array([85, 92, 78, 65, 88, 91, 72, 95])

# Students who passed (>= 75)
passed = scores[scores >= 75]
print(f"Passed: {passed}")
# [85 92 78 88 91 72 95]

# Count students who passed
print(f"Count: {len(passed)}")  # 7

# Students who got A grade (>= 90)
a_grade = scores[scores >= 90]
print(f"A grades: {a_grade}")
# [92 91 95]
```

**Example 2: Temperature analysis**

```python
temps = np.array([32, 28, 35, 42, 38, 25, 30, 45])

# Freezing temperatures (< 32)
freezing = temps[temps < 32]
print(f"Freezing: {freezing}")  # [28 25 30]

# Hot days (>= 40)
hot = temps[temps >= 40]
print(f"Hot days: {hot}")  # [42 45]

# Comfortable range (30-38)
comfortable = temps[(temps >= 30) & (temps <= 38)]
print(f"Comfortable: {comfortable}")  # [32 35 38 30]
```

**Example 3: Sales data filtering**

```python
sales = np.array([1200, 800, 1500, 600, 2000, 900, 1800])

# High performance (>= 1500)
high = sales[sales >= 1500]
avg_high = high.mean()
print(f"High performers avg: {avg_high}")  # 1775.0

# Below target (< 1000)
below = sales[sales < 1000]
print(f"Below target: {below}")  # [800 600 900]
```

### Summary (1 minute)

**Key Takeaways:**

1. **Creating boolean arrays:**
   - Use comparison operators: `>`, `<`, `>=`, `<=`, `==`, `!=`
   - Result is boolean array (True/False)

2. **Boolean indexing:**
   - Filter with `arr[condition]`
   - Returns only elements where condition is True

3. **Combining conditions:**
   - AND: `(cond1) & (cond2)`
   - OR: `(cond1) | (cond2)`
   - NOT: `~(condition)`
   - Always use parentheses!

4. **Modifying with boolean indexing:**
   - `arr[condition] = new_value`
   - Update filtered elements in place

**Remember:**
- Boolean indexing filters based on conditions
- Very efficient (no loops needed)
- Works with multi-dimensional arrays
- Essential for data filtering and cleaning

**Next Steps:**
You'll learn fancy indexing to select specific elements using arrays of indices!
