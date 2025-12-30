## Apply Broadcasting Rules

### What is Broadcasting?

Broadcasting allows NumPy to perform operations on arrays of different shapes without creating copies.

```python
import numpy as np

# Scalar broadcasting
arr = np.array([1, 2, 3, 4, 5])
result = arr + 10  # [11 12 13 14 15]

# 2D array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
result = matrix * 5
# [[ 5 10 15]
#  [20 25 30]]
```

**Key point:** NumPy virtually stretches arrays without copying data.

---

### Broadcasting Rules

**Three rules:**
1. Pad shapes with 1s on the left if different dimensions
2. Arrays compatible if dimensions are equal or one is 1
3. Stretch size-1 dimensions to match larger array

**Compatible shapes:**
```
(3, 4) + (4,)   → ✓ (becomes (3, 4) + (1, 4))
(3, 4) + (3, 1) → ✓ 
(3, 4) + (3,)   → ✗ (incompatible)
```

---

### Scalar Broadcasting

```python
# Works with all operations
arr = np.array([10, 20, 30])

arr + 5    # [15 25 35]
arr * 2    # [20 40 60]
arr / 10   # [1. 2. 3.]
arr ** 2   # [ 100  400  900]
```

---

### 1D to 2D Broadcasting

**Row broadcasting:**

```python
matrix = np.array([[10, 20, 30],
                   [40, 50, 60]])

row_vec = np.array([1, 2, 3])

result = matrix + row_vec
# [[11 22 33]
#  [41 52 63]]
```

**Column broadcasting:**

```python
col_vec = np.array([[1], [2]])

result = matrix + col_vec
# [[11 21 31]
#  [42 52 62]]
```

**How it works:**
```
Matrix (2, 3):      Row vec (3,):
[[10, 20, 30],      [1, 2, 3]
 [40, 50, 60]]      
                    Broadcasts to (2, 3):
                    [[1, 2, 3],
                     [1, 2, 3]]
```

---

### Using np.newaxis

Add dimensions for broadcasting:

```python
arr = np.array([1, 2, 3])  # Shape: (3,)

# Add column dimension
col = arr[:, np.newaxis]   # Shape: (3, 1)
# [[1]
#  [2]
#  [3]]

# Add row dimension
row = arr[np.newaxis, :]   # Shape: (1, 3)
# [[1 2 3]]
```

**Outer product via broadcasting:**

```python
a = np.array([1, 2, 3])

col = a[:, np.newaxis]  # (3, 1)
row = a[np.newaxis, :]  # (1, 3)

result = col * row
# [[1 2 3]
#  [2 4 6]
#  [3 6 9]]
```

---

### Using keepdims for Broadcasting

```python
data = np.array([[10, 20, 30],
                 [40, 50, 60]])

# Without keepdims
mean1 = data.mean(axis=1)  # Shape: (2,)

# With keepdims
mean2 = data.mean(axis=1, keepdims=True)  # Shape: (2, 1)

# Now can broadcast easily
centered = data - mean2
# [[-10.   0.  10.]
#  [-10.   0.  10.]]
```

---

### Common Broadcasting Patterns

**Pattern 1: Normalize rows**

```python
data = np.array([[10, 20, 30],
                 [40, 50, 60]])

row_means = data.mean(axis=1, keepdims=True)
normalized = data - row_means
```

**Pattern 2: Normalize columns**

```python
col_means = data.mean(axis=0, keepdims=True)
normalized = data - col_means
```

**Pattern 3: Apply different operations per row**

```python
data = np.array([[100, 200],
                 [10, 20]])

multipliers = np.array([[2], [5]])
result = data * multipliers
# [[200 400]
#  [ 50 100]]
```

---

### Practical Applications

**Distance matrix:**

```python
points = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])

p1 = points[:, np.newaxis, :]  # (3, 1, 2)
p2 = points[np.newaxis, :, :]  # (1, 3, 2)

distances = np.sqrt(((p1 - p2) ** 2).sum(axis=2))
```

**Temperature conversion:**

```python
celsius = np.array([[20, 25, 30],
                    [15, 18, 22]])

fahrenheit = celsius * 9/5 + 32
```

---

### Key Takeaways

1. **Broadcasting rules:**
   - Pad shapes with 1s on left
   - Dimensions must match or be 1
   - Size-1 dimensions stretch

2. **Common patterns:**
   - Scalar to array: `arr + 5`
   - 1D to 2D: `matrix + vector`
   - Use `keepdims=True` for aggregations

3. **Tools:**
   - `np.newaxis` adds dimensions
   - `reshape()` controls shapes
   - `keepdims=True` preserves dimensions

4. **Compatible shapes:**
   - `(3, 4) + (4,)` ✓
   - `(3, 4) + (3, 1)` ✓
   - `(3, 4) + (3,)` ✗

**Remember:**
- Broadcasting avoids copying
- Check shapes with `.shape`
- Use `keepdims=True` for easy broadcasting
