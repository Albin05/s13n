## Editorials: Create Arrays with arange, linspace, zeros, ones

### Q1 Solution: Create Array Using arange

```python
import numpy as np

# Create even numbers from 2 to 20
arr = np.arange(2, 21, 2)
print(arr)
```

**Explanation:**
- `start = 2`: Begin at 2
- `stop = 21`: End before 21 (so 20 is included)
- `step = 2`: Increment by 2 for even numbers
- Note: stop value 21 ensures 20 is included since stop is exclusive

---

### Q2 Solution: Create Array Using linspace

```python
import numpy as np

# Create 7 evenly-spaced values from 0 to 1
arr = np.linspace(0, 1, 7)
print(arr)
```

**Explanation:**
- `start = 0`: First value
- `stop = 1`: Last value (included by default)
- `num = 7`: Exactly 7 values
- linspace automatically calculates the spacing: 1/6 ≈ 0.16666667

---

### Q3 Solution: Create 2D Zero and One Arrays

```python
import numpy as np

# Create 4x5 zeros array
zeros_arr = np.zeros((4, 5))
print("Zeros array:")
print(zeros_arr)
print(f"Shape: {zeros_arr.shape}")

print()

# Create 3x3 ones array
ones_arr = np.ones((3, 3))
print("Ones array:")
print(ones_arr)
print(f"Shape: {ones_arr.shape}")
```

**Explanation:**
- `np.zeros((4, 5))` creates a 4-row, 5-column array of zeros
- `np.ones((3, 3))` creates a 3x3 array of ones
- Shape parameter must be a tuple: `(rows, cols)`
- Default dtype is float64, so values display as `0.` and `1.`

---

### Q4 Solution: Temperature Scale Conversion

```python
import numpy as np

# Create Celsius array from 0 to 100 with step of 10
celsius = np.arange(0, 101, 10)

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print results
print(f"Celsius:    {celsius}")
print(f"Fahrenheit: {fahrenheit}")
```

**Explanation:**
- `np.arange(0, 101, 10)` creates [0, 10, 20, ..., 100]
  - Stop = 101 ensures 100 is included
  - Step = 10 for increments of 10
- Vectorized operation: `(celsius * 9/5) + 32` applies to all elements at once
- No loops needed - NumPy handles element-wise operations automatically
- Formula applied: F = (C × 9/5) + 32

**Key insight:** This demonstrates NumPy's power in vectorized operations vs Python loops.

---

### Q5 Solution: Create Multiplication Table

```python
import numpy as np

# Create array from 1 to 10
nums = np.arange(1, 11)

# Method 1: Using outer product
table = np.outer(nums, nums)
print(table)

# Method 2: Using broadcasting (alternative)
# table = nums.reshape(10, 1) * nums
```

**Explanation:**
- `np.arange(1, 11)` creates [1, 2, 3, ..., 10]
- `np.outer(nums, nums)` computes outer product:
  - Takes each element from first array
  - Multiplies it by all elements in second array
  - Result is a 10x10 matrix
- Row i, Column j contains: i × j

**Alternative approach using broadcasting:**
```python
# Reshape to column vector (10, 1)
col = nums.reshape(10, 1)
# Multiply column by row
table = col * nums
```

**How it works:**
- `nums.reshape(10, 1)` creates a 10×1 column vector
- Multiplying by `nums` (shape 10,) uses broadcasting
- Each row is multiplied by the entire nums array

**Visual understanding:**
```
    1   2   3  ...  10
1 [ 1   2   3  ...  10]
2 [ 2   4   6  ...  20]
3 [ 3   6   9  ...  30]
...
10[10  20  30  ... 100]
```

**Key Concepts Covered:**
1. Using arange() with different start, stop, and step values
2. Using linspace() to create exact number of evenly-spaced values
3. Creating multi-dimensional arrays with zeros() and ones()
4. Vectorized operations for mathematical transformations
5. Array broadcasting and outer products for matrix creation
