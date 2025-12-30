## Editorials: Copy vs View Arrays

### Q1 Solution: Test Assignment Behavior

```python
import numpy as np

# Create array
arr1 = np.array([10, 20, 30, 40, 50])

# Assignment creates alias/view
arr2 = arr1

# Modify arr2
arr2[0] = 999

# Print both
print(f"arr1: {arr1}")
print(f"arr2: {arr2}")

# Check if they share memory
print(f"Shares memory: {np.shares_memory(arr1, arr2)}")
```

**Explanation:**
- Assignment with `=` does NOT create a copy
- `arr2 = arr1` makes both variables point to the same data
- Modifying `arr2` also modifies `arr1`
- `np.shares_memory()` returns True because they reference the same memory

---

### Q2 Solution: Test Slicing Behavior

```python
import numpy as np

# Create array
arr = np.array([5, 10, 15, 20, 25, 30])

# Create slice (view)
sub = arr[1:4]

# Modify slice
sub[0] = 999

# Print both
print(f"Original array: {arr}")
print(f"Slice: {sub}")
```

**Explanation:**
- Slicing `arr[1:4]` creates a **view**, not a copy
- The view shares memory with the original array
- Modifying `sub[0]` modifies `arr[1]` (same memory location)
- This is different from Python lists where slicing creates a copy!

**Key difference from lists:**
```python
# NumPy: slicing creates VIEW
arr[1:4] → modifies original

# Python lists: slicing creates COPY
list[1:4] → does NOT modify original
```

---

### Q3 Solution: Create Independent Copy

```python
import numpy as np

# Create original array
original = np.array([1, 2, 3, 4, 5])

# Create independent copy
independent = original.copy()

# Modify copy
independent[2] = 100

# Print both
print(f"Original: {original}")
print(f"Independent: {independent}")

# Verify they don't share memory
print(f"Shares memory: {np.shares_memory(original, independent)}")
```

**Explanation:**
- `.copy()` creates a true independent copy with separate memory
- Modifying `independent` does NOT affect `original`
- `np.shares_memory()` returns False
- Use `.copy()` whenever you need to preserve the original array

---

### Q4 Solution: Fix Unintended Modification

```python
import numpy as np

# Unsafe function (modifies original)
def double_values(arr):
    arr = arr * 2
    return arr

# Safe function (uses copy)
def double_values_safe(arr):
    arr_copy = arr.copy()
    arr_copy = arr_copy * 2
    return arr_copy

# Test unsafe function
print("Using unsafe function:")
data = np.array([10, 20, 30])
result = double_values(data)
print(f"Original data after: {data}")
print(f"Result: {result}")

print("\nUsing safe function:")
data = np.array([10, 20, 30])
result = double_values_safe(data)
print(f"Original data after: {data}")
print(f"Result: {result}")
```

**Explanation:**
- **Unsafe version**: `arr = arr * 2` creates a new array but the operation modifies original
- **Safe version**: Uses `.copy()` to work with independent data
- The multiplication operation `arr * 2` itself creates a new array, but without `.copy()` it can still modify the original in some cases
- **Best practice**: Always use `.copy()` in functions when you don't want to modify the input

---

### Q5 Solution: Detect View vs Copy

```python
import numpy as np

def check_relationship(arr1, arr2):
    """Determine relationship between two arrays"""
    if arr1 is arr2:
        return "Same object"
    elif np.shares_memory(arr1, arr2):
        return "View"
    else:
        return "Independent copy"

# Test 1: Same object
a = np.array([1, 2, 3])
b = a
print(f"Test 1: {check_relationship(a, b)}")

# Test 2: View (slice)
a = np.array([1, 2, 3])
b = a[:]
print(f"Test 2: {check_relationship(a, b)}")

# Test 3: Independent copy
a = np.array([1, 2, 3])
b = a.copy()
print(f"Test 3: {check_relationship(a, b)}")
```

**Explanation:**
- **Same object**: `arr1 is arr2` checks if they're the exact same object
- **View**: Different objects but share memory (`np.shares_memory()` returns True)
- **Independent copy**: Different objects, separate memory

**Logic flow:**
1. First check `is` for same object (strongest relationship)
2. Then check `shares_memory()` for views
3. Otherwise, it's an independent copy

**Key insights:**
- `b = a` → Same object
- `b = a[:]` → View (NumPy slicing)
- `b = a.copy()` → Independent copy

**Key Concepts Covered:**
1. Understanding assignment creates aliases, not copies
2. Slicing creates views in NumPy (unlike Python lists)
3. Using `.copy()` to create independent data
4. Fixing functions that unintentionally modify inputs
5. Detecting relationships using `is` and `np.shares_memory()`
6. Importance of preserving original data in functions
