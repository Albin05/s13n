## In-class Quiz: Understand Array Attributes (shape, dtype, ndim)

### Question 1
What will be the output of the following code?
```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)
```

A) `(3, 2)`
B) `(2, 3)`
C) `6`
D) `2`

**Correct Answer: B**

---

### Question 2
Which attribute returns the total number of elements in a NumPy array?

A) `length`
B) `count`
C) `size`
D) `total`

**Correct Answer: C**

---

### Question 3
What does the `ndim` attribute represent?

A) The total number of elements
B) The number of dimensions (axes)
C) The data type of the array
D) The memory size in bytes

**Correct Answer: B**

---

### Question 4
What will be the output of the following code?
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.ndim)
```

A) `1`
B) `5`
C) `(5,)`
D) `int64`

**Correct Answer: A**
*Explanation: ndim returns the number of dimensions, which is 1 for a 1D array*

---

### Question 5
If an array has `shape = (4, 3)` and `dtype = int64`, what is its total memory usage in bytes?

A) 12 bytes
B) 48 bytes
C) 96 bytes
D) 192 bytes

**Correct Answer: C**
*Explanation: 4 × 3 = 12 elements, each int64 element is 8 bytes, so 12 × 8 = 96 bytes*
