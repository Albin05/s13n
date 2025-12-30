### Copy vs View Arrays

### Hook (2 minutes)

"Imagine you modify a NumPy array slice, and suddenly your original array changes too - unexpected! Or you think you're saving memory by reusing an array, but NumPy creates a full copy. Understanding the difference between copies and views is crucial for writing correct, efficient code. One small mistake can lead to hard-to-find bugs or memory issues. Let's master this fundamental concept!"

### Section 1: Introduction to Copy and View (3 minutes)

**What are copies and views?**

When you work with arrays, NumPy can create:
- **View**: A new array object that looks at the same data
- **Copy**: A new array object with its own separate data

**Why does this matter?**

1. **Memory efficiency**: Views share data, copies duplicate it
2. **Side effects**: Modifying a view changes the original array
3. **Performance**: Views are faster (no data copying)
4. **Correctness**: Understanding prevents unexpected bugs

**Key concept:**
```python
# View: Two variables point to same data
# Copy: Two variables have separate data
```

**Real-world analogy:**
- **View**: Two people sharing the same document (edit affects both)
- **Copy**: Two people with separate copies (edit affects only one)

### Section 2: Assignment Creates a View (3 minutes)

**Simple assignment does NOT create a copy:**

```python
import numpy as np

# Create original array
original = np.array([1, 2, 3, 4, 5])

# Assignment creates a view (alias)
view = original

# Modify through view
view[0] = 999

# Original is also changed!
print(original)  # [999   2   3   4   5]
print(view)      # [999   2   3   4   5]
```

**Why?**
- Assignment creates a new **reference** to the same object
- Both variables point to the same underlying data
- This is **not** specific to NumPy - it's Python behavior

**Checking if arrays share data:**

```python
import numpy as np

original = np.array([1, 2, 3, 4, 5])
view = original

# Check if they're the same object
print(view is original)  # True

# Check if they share data
print(np.shares_memory(view, original))  # True
```

**This applies to all Python objects:**
```python
# Same behavior with lists
list1 = [1, 2, 3]
list2 = list1  # Not a copy!
list2[0] = 999
print(list1)  # [999, 2, 3]
```

### Section 3: Slicing Creates a View (4 minutes)

**Array slicing returns a view:**

```python
import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50])

# Slice creates a view
slice_view = arr[1:4]  # [20, 30, 40]

# Modify the view
slice_view[0] = 999

# Original array is modified!
print(arr)        # [ 10 999  30  40  50]
print(slice_view) # [999  30  40]
```

**This is different from Python lists:**

```python
# Python list slicing creates a COPY
list1 = [10, 20, 30, 40, 50]
list2 = list1[1:4]  # Copy
list2[0] = 999
print(list1)  # [10, 20, 30, 40, 50] - unchanged!
```

**Why NumPy uses views:**
- **Memory efficiency**: Don't duplicate large arrays
- **Performance**: No need to copy data for operations
- **Flexibility**: Can work with subarrays efficiently

**2D array slicing also creates views:**

```python
import numpy as np

# 2D array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Extract row (view)
row = matrix[1]  # [4, 5, 6]
row[0] = 999

print(matrix)
# [[  1   2   3]
#  [999   5   6]
#  [  7   8   9]]
```

### Section 4: Using copy() to Create Independent Copy (3 minutes)

**Create a true copy with .copy():**

```python
import numpy as np

# Original array
original = np.array([1, 2, 3, 4, 5])

# Create independent copy
independent = original.copy()

# Modify the copy
independent[0] = 999

# Original is unchanged
print(original)    # [1 2 3 4 5]
print(independent) # [999 2 3 4 5]
```

**Check they don't share memory:**

```python
print(np.shares_memory(original, independent))  # False
```

**When to use .copy():**

1. **Need independent data**: Modifications shouldn't affect original
2. **Preserving original**: Keep backup before modifications
3. **Parallel processing**: Each process needs its own data
4. **Debugging**: Isolate changes to specific copies

**Copy with slicing:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Slice + copy for independence
slice_copy = arr[1:4].copy()

slice_copy[0] = 999

print(arr)        # [10 20 30 40 50] - unchanged!
print(slice_copy) # [999  30  40]
```

### Section 5: View vs Copy Detection (3 minutes)

**How to check if you have a view or copy:**

**Method 1: Use np.shares_memory()**

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# View
view = arr[1:3]
print(np.shares_memory(arr, view))  # True

# Copy
copy = arr[1:3].copy()
print(np.shares_memory(arr, copy))  # False
```

**Method 2: Check base attribute**

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# View has base attribute pointing to original
view = arr[1:3]
print(view.base is arr)  # True

# Copy has base = None
copy = arr[1:3].copy()
print(copy.base is None)  # True
```

**Quick reference:**

| Operation | Result |
|-----------|--------|
| `b = a` | View (same object) |
| `b = a[1:3]` | View |
| `b = a.copy()` | Copy |
| `b = a[1:3].copy()` | Copy |
| `b = np.array(a)` | Copy |

### Section 6: Practical Implications (2 minutes)

**Example 1: Unintended modification**

```python
import numpy as np

def normalize(arr):
    """Normalize array to 0-1 range"""
    min_val = arr.min()
    max_val = arr.max()
    # This modifies the original array!
    arr = (arr - min_val) / (max_val - min_val)
    return arr

data = np.array([10, 20, 30, 40, 50])
normalized = normalize(data)
print(data)  # Modified! [0.  0.25 0.5  0.75 1.  ]
```

**Solution: Use copy() in function**

```python
def normalize_safe(arr):
    """Normalize array without modifying original"""
    arr_copy = arr.copy()  # Work with copy
    min_val = arr_copy.min()
    max_val = arr_copy.max()
    return (arr_copy - min_val) / (max_val - min_val)

data = np.array([10, 20, 30, 40, 50])
normalized = normalize_safe(data)
print(data)  # Unchanged! [10 20 30 40 50]
```

**Example 2: Memory efficiency with views**

```python
import numpy as np

# Large array
large_array = np.arange(1000000)

# Process chunks using views (memory efficient)
for i in range(0, len(large_array), 1000):
    chunk = large_array[i:i+1000]  # View, not copy!
    # Process chunk...
```

### Summary (1 minute)

**Key Takeaways:**

1. **Assignment (=)**: Creates view/alias to same object
2. **Slicing (arr[1:3])**: Creates view in NumPy (unlike Python lists)
3. **.copy()**: Creates independent copy with separate data
4. **np.shares_memory()**: Check if arrays share data
5. **base attribute**: View has base pointing to original, copy has base=None

**Remember:**
- Views: Fast, memory efficient, but changes affect original
- Copies: Safe, independent, but use more memory
- Always use .copy() when you need to preserve the original
- Check with np.shares_memory() or .base when unsure

**Best practice:**
- Use views for reading data (efficiency)
- Use copies when modifying data (safety)
- Be explicit with .copy() to avoid bugs

**Next Steps:**
Now that you understand memory management, you'll learn array indexing and slicing techniques to access and manipulate array elements effectively!
