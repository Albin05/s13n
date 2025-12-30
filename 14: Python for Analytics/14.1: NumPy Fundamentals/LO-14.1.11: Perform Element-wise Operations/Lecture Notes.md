## Perform Element-wise Operations

### Basic Arithmetic Operations

**Operations with scalars:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Addition
result = arr + 5  # [15 25 35 45 55]

# Subtraction
result = arr - 5  # [ 5 15 25 35 45]

# Multiplication
result = arr * 2  # [ 20  40  60  80 100]

# Division
result = arr / 10  # [1. 2. 3. 4. 5.]

# Power
result = arr ** 2  # [ 100  400  900 1600 2500]

# Modulo
result = arr % 3  # [1 2 0 1 2]

# Floor division
result = arr // 3  # [ 3  6 10 13 16]
```

---

### Operations Between Arrays

**Array-to-array operations:**

```python
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

# Addition
result = arr1 + arr2  # [11 22 33 44]

# Subtraction
result = arr1 - arr2  # [ 9 18 27 36]

# Multiplication (element-wise)
result = arr1 * arr2  # [ 10  40  90 160]

# Division
result = arr1 / arr2  # [10. 10. 10. 10.]
```

**How it works:**
```
arr1:     [10, 20, 30, 40]
arr2:     [ 1,  2,  3,  4]
         +-----------------
arr1+arr2:[11, 22, 33, 44]
```

**Multi-dimensional arrays:**

```python
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])
matrix2 = np.array([[10, 20, 30],
                    [40, 50, 60]])

result = matrix1 * matrix2
# [[ 10  40  90]
#  [160 250 360]]
```

---

### Comparison Operations

**Comparison operators:**

```python
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([15, 18, 30, 45, 48])

# Greater than
result = arr1 > arr2  # [False  True False False  True]

# Less than or equal
result = arr1 <= arr2  # [ True  False  True  True  False]

# Equal
result = arr1 == arr2  # [False False  True False False]

# Not equal
result = arr1 != arr2  # [ True  True False  True  True]
```

**Comparison with scalars:**

```python
arr = np.array([10, 25, 30, 15, 40])

result = arr > 20  # [False  True  True False  True]
result = arr == 30  # [False False  True False False]
```

---

### In-Place Operations

**Modifying arrays in-place:**

```python
arr = np.array([10, 20, 30, 40, 50])

# In-place addition
arr += 5  # [15 25 35 45 55]

# In-place multiplication
arr *= 2  # [30 50 70 90 110]

# In-place subtraction
arr -= 10  # [20 40 60 80 100]
```

**Benefits:**
- Memory efficient
- Modifies existing array
- No new array created

---

### Absolute Value and Floor Division

**Absolute value:**

```python
arr = np.array([-10, 20, -30, 40, -50])

result = np.abs(arr)  # [10 20 30 40 50]
# or
result = abs(arr)  # [10 20 30 40 50]
```

**Floor division:**

```python
arr = np.array([10, 15, 20, 25, 30])

result = arr // 3  # [ 3  5  6  8 10]
result = arr / 3   # [ 3.33  5.    6.67  8.33 10.  ]
```

---

### Practical Applications

**Temperature conversion:**

```python
fahrenheit = np.array([32, 68, 86, 104, 122])
celsius = (fahrenheit - 32) * 5 / 9
# [  0.  20.  30.  40.  50.]
```

**Apply discount:**

```python
prices = np.array([100, 250, 75, 180, 320])
discount = 0.20
discounted = prices * (1 - discount)
# [ 80. 200.  60. 144. 256.]
```

**Percentage change:**

```python
old_sales = np.array([1000, 1500, 2000, 1200])
new_sales = np.array([1200, 1350, 2400, 1100])

change = ((new_sales - old_sales) / old_sales) * 100
# [ 20.  -10.   20.  -8.33]
```

**Weighted average:**

```python
midterm = np.array([85, 90, 78, 92, 88])
final = np.array([88, 85, 82, 95, 90])

overall = midterm * 0.4 + final * 0.6
# [86.8 87.  80.4 93.8 89.2]
```

---

### Key Takeaways

1. **Element-wise operations:**
   - Apply to entire arrays at once
   - No loops needed
   - Fast and efficient

2. **Arithmetic operators:**
   - `+`, `-`, `*`, `/`, `**`, `%`, `//`
   - Work with scalars or arrays
   - Arrays must have compatible shapes

3. **Comparison operators:**
   - `>`, `<`, `>=`, `<=`, `==`, `!=`
   - Return boolean arrays
   - Useful for filtering

4. **In-place operations:**
   - `+=`, `-=`, `*=`, `/=`
   - Modify array directly
   - Memory efficient

**Remember:**
- Element-wise means position by position
- Scalars broadcast to all elements
- Operations preserve array shape
- Original arrays unchanged (unless in-place)
