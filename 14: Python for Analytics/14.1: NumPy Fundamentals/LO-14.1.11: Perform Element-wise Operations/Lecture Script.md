### Perform Element-wise Operations

### Hook (2 minutes)

"Imagine you have arrays of daily temperatures for two cities and want to find the difference, or you have product prices and need to apply a discount to all of them. In traditional Python, you'd need loops. But NumPy allows you to perform operations on entire arrays at once - element by element - with simple arithmetic operators! This is called element-wise operations, and it's one of NumPy's most powerful features that makes numerical computing both fast and intuitive."

### Section 1: Basic Arithmetic Operations (3 minutes)

**Addition with scalars:**

```python
import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50])

# Add scalar to all elements
result = arr + 5
print(result)  # [15 25 35 45 55]

# Original array unchanged
print(arr)  # [10 20 30 40 50]
```

**Subtraction, multiplication, division:**

```python
arr = np.array([10, 20, 30, 40, 50])

# Subtraction
result = arr - 5
print(result)  # [ 5 15 25 35 45]

# Multiplication
result = arr * 2
print(result)  # [ 20  40  60  80 100]

# Division
result = arr / 10
print(result)  # [1. 2. 3. 4. 5.]
```

**Power and modulo:**

```python
arr = np.array([2, 3, 4, 5])

# Exponentiation
result = arr ** 2
print(result)  # [ 4  9 16 25]

# Modulo
arr2 = np.array([10, 15, 20, 25])
result = arr2 % 3
print(result)  # [1 0 2 1]
```

### Section 2: Operations Between Arrays (4 minutes)

**Array-to-array operations:**

```python
import numpy as np

# Two arrays of same shape
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

# Addition
result = arr1 + arr2
print(result)  # [11 22 33 44]

# Subtraction
result = arr1 - arr2
print(result)  # [ 9 18 27 36]

# Multiplication (element-wise)
result = arr1 * arr2
print(result)  # [ 10  40  90 160]

# Division
result = arr1 / arr2
print(result)  # [10. 10. 10. 10.]
```

**How it works:**
```
arr1:     [10, 20, 30, 40]
arr2:     [ 1,  2,  3,  4]
         +-----------------
arr1+arr2:[11, 22, 33, 44]
         (10+1, 20+2, 30+3, 40+4)
```

**Multi-dimensional arrays:**

```python
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matrix2 = np.array([[10, 20, 30],
                    [40, 50, 60]])

# Element-wise multiplication
result = matrix1 * matrix2
print(result)
# [[ 10  40  90]
#  [160 250 360]]
```

### Section 3: Comparison Operations (3 minutes)

**Comparison operators:**

```python
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([15, 18, 30, 45, 48])

# Greater than
result = arr1 > arr2
print(result)  # [False  True False False  True]

# Less than or equal
result = arr1 <= arr2
print(result)  # [ True  False  True  True  False]

# Equal
result = arr1 == arr2
print(result)  # [False False  True False False]

# Not equal
result = arr1 != arr2
print(result)  # [ True  True False  True  True]
```

**Comparison with scalars:**

```python
arr = np.array([10, 25, 30, 15, 40])

# Elements greater than 20
result = arr > 20
print(result)  # [False  True  True False  True]

# Elements equal to 30
result = arr == 30
print(result)  # [False False  True False False]
```

### Section 4: In-Place Operations (2 minutes)

**Modifying arrays in-place:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(f"Original: {arr}")

# In-place addition
arr += 5
print(f"After += 5: {arr}")  # [15 25 35 45 55]

# In-place multiplication
arr *= 2
print(f"After *= 2: {arr}")  # [30 50 70 90 110]

# In-place subtraction
arr -= 10
print(f"After -= 10: {arr}")  # [20 40 60 80 100]
```

**Why use in-place operations:**

```python
# Without in-place (creates new array)
arr = np.array([1, 2, 3, 4, 5])
arr = arr + 10  # New array created

# With in-place (modifies existing array)
arr = np.array([1, 2, 3, 4, 5])
arr += 10  # Same array modified (memory efficient)
```

### Section 5: Floor Division and Absolute Value (2 minutes)

**Floor division:**

```python
import numpy as np

arr = np.array([10, 15, 20, 25, 30])

# Floor division
result = arr // 3
print(result)  # [ 3  5  6  8 10]

# Regular division for comparison
result = arr / 3
print(result)  # [ 3.33  5.    6.67  8.33 10.  ]
```

**Absolute value:**

```python
arr = np.array([-10, 20, -30, 40, -50])

# Absolute value
result = np.abs(arr)
print(result)  # [10 20 30 40 50]

# Also works as:
result = abs(arr)
print(result)  # [10 20 30 40 50]
```

### Section 6: Practical Applications (4 minutes)

**Example 1: Temperature conversion**

```python
import numpy as np

# Fahrenheit temperatures
fahrenheit = np.array([32, 68, 86, 104, 122])

# Convert to Celsius: (F - 32) * 5/9
celsius = (fahrenheit - 32) * 5 / 9
print(f"Fahrenheit: {fahrenheit}")
print(f"Celsius: {celsius}")
# [  0.  20.  30.  40.  50.]
```

**Example 2: Apply discount to prices**

```python
prices = np.array([100, 250, 75, 180, 320])

# Apply 20% discount
discount = 0.20
discounted_prices = prices * (1 - discount)
print(f"Original: {prices}")
print(f"After 20% discount: {discounted_prices}")
# [ 80. 200.  60. 144. 256.]

# Calculate savings
savings = prices - discounted_prices
print(f"You save: {savings}")
# [20. 50. 15. 36. 64.]
```

**Example 3: Calculate percentage change**

```python
old_sales = np.array([1000, 1500, 2000, 1200])
new_sales = np.array([1200, 1350, 2400, 1100])

# Percentage change: ((new - old) / old) * 100
change = ((new_sales - old_sales) / old_sales) * 100
print(f"Old sales: {old_sales}")
print(f"New sales: {new_sales}")
print(f"% Change: {change}")
# [ 20.  -10.   20.  -8.33]
```

**Example 4: Grade analysis**

```python
# Student scores
midterm = np.array([85, 90, 78, 92, 88])
final = np.array([88, 85, 82, 95, 90])

# Weighted average: 40% midterm, 60% final
weights = (0.4, 0.6)
overall = midterm * weights[0] + final * weights[1]
print(f"Midterm: {midterm}")
print(f"Final: {final}")
print(f"Overall: {overall}")
# [86.8 87.  80.4 93.8 89.2]

# Find who improved
improved = final > midterm
print(f"Improved from midterm: {improved}")
# [ True False  True  True  True]
```

### Summary (1 minute)

**Key Takeaways:**

1. **Element-wise operations:**
   - Apply operations to entire arrays at once
   - No loops needed
   - Fast and efficient

2. **Arithmetic operators:**
   - `+`, `-`, `*`, `/`, `**`, `%`, `//`
   - Work with scalars: `arr + 5`
   - Work between arrays: `arr1 + arr2`

3. **Comparison operators:**
   - `>`, `<`, `>=`, `<=`, `==`, `!=`
   - Return boolean arrays
   - Useful for filtering

4. **In-place operations:**
   - `+=`, `-=`, `*=`, `/=`
   - Modify array directly
   - Memory efficient

5. **Important rules:**
   - Arrays must have compatible shapes
   - Operations are element-wise
   - Original arrays unchanged (unless using in-place)

**Remember:**
- Element-wise means position by position
- Same shape required for array operations
- Scalars work with any array
- NumPy handles the iteration automatically

**Next Steps:**
You've learned element-wise operations! Next, you'll explore universal functions (ufuncs) which extend these capabilities even further.
