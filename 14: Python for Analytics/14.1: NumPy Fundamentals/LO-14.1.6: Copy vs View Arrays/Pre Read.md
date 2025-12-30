## Pre-Read: Copy vs View Arrays

### What You'll Learn

In this session, you'll understand the crucial difference between **copies** and **views** in NumPy arrays. This concept is fundamental to writing correct, efficient code and avoiding unexpected bugs.

### Why It Matters

When working with NumPy arrays, some operations create a **view** (sharing the same data) while others create a **copy** (independent data). Understanding this difference helps you:

1. **Avoid bugs**: Prevent unintended modifications to original arrays
2. **Optimize memory**: Use views when possible to save memory
3. **Write safer functions**: Ensure functions don't have unexpected side effects
4. **Debug effectively**: Understand why array values change unexpectedly

### Key Concepts Preview

**View vs Copy:**
- **View**: A new array object that looks at the same underlying data
- **Copy**: A new array object with its own separate data

**Common operations:**
- `arr2 = arr1` → Creates an alias (same object)
- `arr2 = arr1[1:3]` → Creates a view (shares memory)
- `arr2 = arr1.copy()` → Creates a copy (independent)

**Real-world analogy:**
Think of a view like two people editing the same shared Google Doc - changes by one person affect what the other sees. A copy is like two people with separate Word documents - changes are independent.

### What to Expect

You'll learn:
1. How assignment creates aliases, not copies
2. Why slicing creates views (different from Python lists!)
3. When and how to use `.copy()` for independent data
4. How to detect if arrays share memory
5. Best practices for safe array manipulation

### Prepare

Make sure you have:
- NumPy installed (`pip install numpy`)
- Basic understanding of NumPy arrays
- Python environment ready for practice

### Quick Example

```python
import numpy as np

# Assignment creates alias
arr1 = np.array([1, 2, 3])
arr2 = arr1
arr2[0] = 999
print(arr1)  # [999 2 3] - Original changed!

# .copy() creates independent copy
arr1 = np.array([1, 2, 3])
arr2 = arr1.copy()
arr2[0] = 999
print(arr1)  # [1 2 3] - Original unchanged!
```

This fundamental concept will appear throughout your NumPy work, so understanding it well is essential!
