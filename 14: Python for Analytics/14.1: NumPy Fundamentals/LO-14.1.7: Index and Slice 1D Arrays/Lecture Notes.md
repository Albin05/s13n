## Index and Slice 1D Arrays

### Basic Indexing with Positive Indices

**Accessing individual elements:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Access elements
print(arr[0])   # 10 (first element)
print(arr[2])   # 30 (third element)
print(arr[4])   # 50 (last element)

# Modify element
arr[2] = 999
print(arr)  # [10 20 999 40 50]
```

**Key points:**
- Zero-based indexing (first element is index 0)
- Last element is at index `len(arr) - 1`
- Out of bounds raises `IndexError`

---

### Negative Indexing

**Accessing from the end:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Negative indices
print(arr[-1])   # 50 (last element)
print(arr[-2])   # 40 (second to last)
print(arr[-5])   # 10 (fifth from end)

# Modify last element
arr[-1] = 999
print(arr)  # [10 20 30 40 999]
```

**Index mapping:**
```
Array:       [10, 20, 30, 40, 50]
Positive:     0   1   2   3   4
Negative:    -5  -4  -3  -2  -1
```

---

### Basic Slicing Syntax

**Slicing extracts portions:** `arr[start:stop]`

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Basic slicing
print(arr[1:4])   # [20 30 40] (indices 1, 2, 3)
print(arr[:3])    # [10 20 30] (first 3)
print(arr[4:])    # [50 60 70] (from index 4 to end)
print(arr[:])     # [10 20 30 40 50 60 70] (entire array)

# Negative indices in slicing
print(arr[1:-1])  # [20 30 40 50 60] (exclude first and last)
print(arr[-3:])   # [50 60 70] (last 3 elements)
```

**Important:** Slicing is `[inclusive:exclusive]`
- Start index is included
- Stop index is excluded

**Slicing creates views:**

```python
arr = np.array([10, 20, 30, 40, 50])
sub = arr[1:4]  # View, not copy
sub[0] = 999
print(arr)  # [10 999 30 40 50] - Original modified!
```

---

### Advanced Slicing with Step

**Full syntax:** `arr[start:stop:step]`

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# Step parameter
print(arr[::2])    # [10 30 50 70 90] (every 2nd element)
print(arr[::3])    # [10 40 70] (every 3rd element)
print(arr[1::2])   # [20 40 60 80] (from index 1, every 2nd)
print(arr[2:7:2])  # [30 50 70] (from 2 to 7, every 2nd)

# Negative step (reverse)
print(arr[::-1])   # [90 80 70 60 50 40 30 20 10] (reversed)
print(arr[::-2])   # [90 70 50 30 10] (every 2nd in reverse)
```

---

### Common Slicing Patterns

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# First n elements
first_3 = arr[:3]         # [10 20 30]

# Last n elements
last_3 = arr[-3:]         # [80 90 100]

# All except first n
except_first = arr[2:]    # [30 40 50 60 70 80 90 100]

# All except last n
except_last = arr[:-2]    # [10 20 30 40 50 60 70 80]

# Middle (exclude first and last)
middle = arr[1:-1]        # [20 30 40 50 60 70 80 90]

# Reverse
reversed_arr = arr[::-1]  # [100 90 80 70 60 50 40 30 20 10]

# Every nth element
every_3rd = arr[::3]      # [10 40 70 100]

# Even indices
even_indices = arr[::2]   # [10 30 50 70 90]

# Odd indices
odd_indices = arr[1::2]   # [20 40 60 80 100]
```

---

### Practical Example

```python
import numpy as np

# Temperature readings (24 hours)
temps = np.array([20, 21, 22, 24, 26, 28, 30, 32,
                  33, 34, 33, 32, 30, 28, 26, 24,
                  22, 21, 20, 19, 18, 18, 19, 20])

# Morning temps (6 AM to 12 PM)
morning = temps[6:12]
print(f"Morning: {morning}")

# Every 3rd hour
every_3_hours = temps[::3]
print(f"Every 3 hours: {every_3_hours}")

# Last 6 hours
last_6 = temps[-6:]
print(f"Last 6 hours: {last_6}")

# Average of afternoon (hours 12-17)
afternoon_avg = temps[12:17].mean()
print(f"Afternoon average: {afternoon_avg}")
```

---

### NumPy vs Python Lists

**Key difference:**

```python
import numpy as np

# NumPy: Slicing creates VIEW
np_arr = np.array([1, 2, 3, 4, 5])
np_slice = np_arr[1:4]
np_slice[0] = 999
print(np_arr)  # [1 999 3 4 5] - Modified!

# Python list: Slicing creates COPY
py_list = [1, 2, 3, 4, 5]
py_slice = py_list[1:4]
py_slice[0] = 999
print(py_list)  # [1, 2, 3, 4, 5] - Unchanged!
```

**To get a copy in NumPy:**

```python
arr_copy = arr[1:4].copy()  # Independent copy
```

---

### Key Takeaways

1. **Indexing**: `arr[index]` for single elements
   - Positive: 0, 1, 2, ...
   - Negative: -1, -2, -3, ... (from end)

2. **Slicing**: `arr[start:stop:step]`
   - start: inclusive
   - stop: exclusive
   - step: increment (default 1)

3. **Common patterns:**
   - First n: `arr[:n]`
   - Last n: `arr[-n:]`
   - Reverse: `arr[::-1]`
   - Every nth: `arr[::n]`

4. **Important:** NumPy slicing creates views, not copies
   - Use `.copy()` for independent data
