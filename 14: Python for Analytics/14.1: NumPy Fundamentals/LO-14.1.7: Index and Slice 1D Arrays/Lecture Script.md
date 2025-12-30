### Index and Slice 1D Arrays

### Hook (2 minutes)

"Accessing specific elements and sections of arrays is one of the most fundamental operations in data analysis. Whether you need the first 10 records, the last value, every other element, or a reversed sequence, indexing and slicing provide powerful, efficient ways to extract exactly what you need. Unlike Python lists, NumPy's indexing returns views for efficiency. Mastering these operations unlocks your ability to manipulate large datasets with precision!"

### Section 1: Basic Indexing with Positive Indices (3 minutes)

**Accessing individual elements:**

NumPy arrays use zero-based indexing, just like Python lists.

```python
import numpy as np

# Create 1D array
arr = np.array([10, 20, 30, 40, 50])

# Access individual elements
print(arr[0])   # 10 (first element)
print(arr[1])   # 20 (second element)
print(arr[4])   # 50 (fifth element)
```

**Index positions:**
```
Array:  [10, 20, 30, 40, 50]
Index:   0   1   2   3   4
```

**Modifying elements through indexing:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Modify single element
arr[2] = 999

print(arr)  # [10 20 999 40 50]
```

**Index out of bounds error:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# This raises IndexError
print(arr[10])  # IndexError: index 10 is out of bounds
```

**Key points:**
- Indexing starts at 0
- Last element is at index `len(arr) - 1`
- Out of bounds access raises `IndexError`
- Indexing returns a single value (scalar), not an array

### Section 2: Negative Indexing (3 minutes)

**Accessing elements from the end:**

Negative indices count from the end of the array.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Negative indexing
print(arr[-1])   # 50 (last element)
print(arr[-2])   # 40 (second to last)
print(arr[-5])   # 10 (fifth from end = first element)
```

**Negative index positions:**
```
Array:       [10, 20, 30, 40, 50]
Positive:     0   1   2   3   4
Negative:    -5  -4  -3  -2  -1
```

**Why negative indexing is useful:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Get last element without knowing array length
last = arr[-1]
print(last)  # 50

# Compare with positive indexing
last = arr[len(arr) - 1]  # More verbose
print(last)  # 50
```

**Modifying with negative indices:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Modify last element
arr[-1] = 999

print(arr)  # [10 20 30 40 999]
```

**Key points:**
- `-1` is always the last element
- `-2` is second to last
- Negative indices wrap around from the end
- Very useful when you don't know the array length

### Section 3: Basic Slicing Syntax (4 minutes)

**Slicing extracts a portion of the array:**

**Syntax:** `arr[start:stop]`
- `start`: Index where slice begins (inclusive)
- `stop`: Index where slice ends (exclusive)

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Basic slicing
print(arr[1:4])   # [20 30 40] (indices 1, 2, 3)
print(arr[0:3])   # [10 20 30] (indices 0, 1, 2)
print(arr[2:5])   # [30 40 50] (indices 2, 3, 4)
```

**Understanding start and stop:**
```
Array:  [10, 20, 30, 40, 50, 60, 70]
Index:   0   1   2   3   4   5   6

arr[1:4] extracts:
         [ ↓   ↓   ↓ ]
         [20, 30, 40]
Start at 1 ───┘      │
Stop before 4 ───────┘
```

**Omitting start or stop:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Omit start (defaults to 0)
print(arr[:3])    # [10 20 30] (first 3 elements)

# Omit stop (defaults to end)
print(arr[4:])    # [50 60 70] (from index 4 to end)

# Omit both (full array)
print(arr[:])     # [10 20 30 40 50 60 70] (entire array)
```

**Negative indices in slicing:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Mix positive and negative
print(arr[1:-1])   # [20 30 40 50 60] (exclude first and last)
print(arr[-3:])    # [50 60 70] (last 3 elements)
print(arr[:-2])    # [10 20 30 40 50] (all except last 2)
```

**Slicing creates a view, not a copy:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Create slice
sub = arr[1:4]  # [20, 30, 40]

# Modify slice
sub[0] = 999

# Original is also modified!
print(arr)  # [10 999 30 40 50]
print(sub)  # [999  30  40]
```

### Section 4: Advanced Slicing with Step (4 minutes)

**Full slicing syntax:** `arr[start:stop:step]`

The `step` parameter controls the increment between indices.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# Every 2nd element
print(arr[::2])    # [10 30 50 70 90]

# Every 3rd element
print(arr[::3])    # [10 40 70]

# From index 1, every 2nd element
print(arr[1::2])   # [20 40 60 80]

# From index 2 to 7, every 2nd element
print(arr[2:7:2])  # [30 50 70]
```

**Understanding step:**
```
Array:  [10, 20, 30, 40, 50, 60, 70, 80, 90]
Index:   0   1   2   3   4   5   6   7   8

arr[::2] takes every 2nd element:
         ↓       ↓       ↓       ↓       ↓
        [10,    30,    50,    70,    90]
```

**Negative step (reverse):**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Reverse array
print(arr[::-1])   # [50 40 30 20 10]

# Reverse every 2nd element
print(arr[::-2])   # [50 30 10]
```

**Step patterns:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Positive step
print(arr[1:7:2])    # [20 40 60] (forward, skip 1)

# Negative step
print(arr[7:1:-2])   # [80 60 40] (backward, skip 1)

# Full reverse
print(arr[::-1])     # [80 70 60 50 40 30 20 10]
```

**Empty slices:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Invalid range (start >= stop with positive step)
print(arr[3:1])    # [] (empty array)

# Valid with negative step
print(arr[3:1:-1]) # [40 30]
```

### Section 5: Common Slicing Patterns (3 minutes)

**Useful slicing patterns:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# First n elements
first_3 = arr[:3]
print(first_3)  # [10 20 30]

# Last n elements
last_3 = arr[-3:]
print(last_3)   # [80 90 100]

# All except first n
except_first_2 = arr[2:]
print(except_first_2)  # [30 40 50 60 70 80 90 100]

# All except last n
except_last_2 = arr[:-2]
print(except_last_2)   # [10 20 30 40 50 60 70 80]

# Middle portion (exclude first and last)
middle = arr[1:-1]
print(middle)   # [20 30 40 50 60 70 80 90]

# Reverse
reversed_arr = arr[::-1]
print(reversed_arr)  # [100 90 80 70 60 50 40 30 20 10]

# Every nth element
every_3rd = arr[::3]
print(every_3rd)  # [10 40 70 100]

# Even indices
even_indices = arr[::2]
print(even_indices)  # [10 30 50 70 90]

# Odd indices
odd_indices = arr[1::2]
print(odd_indices)   # [20 40 60 80 100]
```

**Practical examples:**

```python
import numpy as np

# Temperature readings (hourly for 24 hours)
temps = np.array([20, 21, 22, 24, 26, 28, 30, 32,
                  33, 34, 33, 32, 30, 28, 26, 24,
                  22, 21, 20, 19, 18, 18, 19, 20])

# Get morning temps (6 AM to 12 PM)
morning = temps[6:12]
print(f"Morning temps: {morning}")

# Get every 3rd hour reading
every_3_hours = temps[::3]
print(f"Every 3 hours: {every_3_hours}")

# Get last 6 hours
last_6_hours = temps[-6:]
print(f"Last 6 hours: {last_6_hours}")
```

**Combining indexing and slicing:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Get slice, then index into it
sub = arr[1:5]      # [20, 30, 40, 50]
value = sub[2]      # 40
print(value)

# Equivalent to:
value = arr[1:5][2]  # 40
print(value)
```

### Section 6: Slicing vs Python Lists (2 minutes)

**Key difference: Views vs Copies**

```python
import numpy as np

# NumPy: Slicing creates VIEW
np_arr = np.array([1, 2, 3, 4, 5])
np_slice = np_arr[1:4]
np_slice[0] = 999
print(np_arr)  # [1 999 3 4 5] - Original modified!

# Python list: Slicing creates COPY
py_list = [1, 2, 3, 4, 5]
py_slice = py_list[1:4]
py_slice[0] = 999
print(py_list)  # [1, 2, 3, 4, 5] - Original unchanged!
```

**To get a copy in NumPy:**

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Use .copy() for independent copy
arr_copy = arr[1:4].copy()
arr_copy[0] = 999

print(arr)       # [1 2 3 4 5] - Unchanged!
print(arr_copy)  # [999 3 4]
```

### Summary (1 minute)

**Key Takeaways:**

1. **Indexing**: Access single elements using `arr[index]`
   - Positive indices: `0, 1, 2, ...`
   - Negative indices: `-1, -2, -3, ...` (from end)

2. **Slicing**: Extract portions using `arr[start:stop:step]`
   - `start`: inclusive
   - `stop`: exclusive
   - `step`: increment (default 1)

3. **Common patterns:**
   - First n: `arr[:n]`
   - Last n: `arr[-n:]`
   - Reverse: `arr[::-1]`
   - Every nth: `arr[::n]`

4. **Important:** NumPy slicing creates **views**, not copies
   - Modifications affect the original array
   - Use `.copy()` for independent data

**Remember:**
- Zero-based indexing
- Negative indices count from end
- Slicing is [inclusive:exclusive]
- Step parameter enables advanced patterns
- Slices are views, not copies

**Next Steps:**
Now that you can work with 1D arrays, you'll learn how to index and slice multi-dimensional arrays for more complex data manipulation!
