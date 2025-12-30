## Post-class Quiz: Use Universal Functions (ufuncs)

### Question 1
What is the result of `np.sqrt(np.array([4, 9, 16, 25]))`?

A) [2, 3, 4, 5]
B) [2., 3., 4., 5.]
C) [16, 81, 256, 625]
D) An error occurs

**Correct Answer: B**
*Explanation: `np.sqrt()` calculates the square root of each element, returning a float array: [2., 3., 4., 5.]*

---

### Question 2
What does `np.maximum(arr1, arr2)` do?

A) Returns the largest value from either array
B) Returns element-wise maximum between two arrays
C) Returns the sum of both arrays
D) Returns the maximum value of arr1

**Correct Answer: B**
*Explanation: `np.maximum()` compares arrays element-wise and returns the larger value at each position*

---

### Question 3
Which function is used to convert degrees to radians?

A) `np.deg2rad()` or `np.radians()`
B) `np.to_radians()`
C) `np.convert_degrees()`
D) `np.angle()`

**Correct Answer: A**
*Explanation: Both `np.radians()` and `np.deg2rad()` convert degrees to radians*

---

### Question 4
What is the difference between `np.floor()` and `np.ceil()`?

A) No difference
B) `floor()` rounds down, `ceil()` rounds up
C) `floor()` rounds to nearest, `ceil()` rounds up
D) `floor()` only works with positive numbers

**Correct Answer: B**
*Explanation: `np.floor()` rounds down to the nearest integer, while `np.ceil()` rounds up to the nearest integer*

---

### Question 5
What does `np.mean(arr, axis=1)` calculate for a 2D array?

A) Mean of entire array
B) Mean across rows (for each column)
C) Mean across columns (for each row)
D) Median of the array

**Correct Answer: C**
*Explanation: `axis=1` calculates mean across columns horizontally, giving the mean for each row*
