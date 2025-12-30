## Post-class Quiz: Calculate Statistics and Aggregations

### Question 1
What does `np.mean(arr, axis=0)` do on a 2D array?

A) Calculates mean of each row
B) Calculates mean of each column
C) Calculates overall mean
D) Returns the first column

**Correct Answer: B**
*Explanation: axis=0 operates down the columns (vertically), calculating the mean for each column across all rows. For a (4, 3) array, it returns (3,) array with column means*

---

### Question 2
What is the relationship between variance and standard deviation?

A) Variance = Standard Deviation + Mean
B) Variance = Standard Deviation²
C) Standard Deviation = Variance²
D) They are unrelated

**Correct Answer: B**
*Explanation: Variance is the square of standard deviation. If std=5, then var=25. Use np.var() and np.std() to calculate them*

---

### Question 3
Which function finds the 75th percentile (Q3)?

A) np.quantile(arr, 75)
B) np.percentile(arr, 0.75)
C) np.percentile(arr, 75)
D) np.quartile(arr, 3)

**Correct Answer: C**
*Explanation: np.percentile(arr, 75) calculates the 75th percentile. Alternatively, np.quantile(arr, 0.75) works (quantile uses 0-1 scale)*

---

### Question 4
What does `keepdims=True` do in aggregation functions?

A) Keeps all original dimensions unchanged
B) Preserves the reduced dimension as size 1
C) Prevents the operation from executing
D) Creates a deep copy of the array

**Correct Answer: B**
*Explanation: keepdims=True maintains the reduced dimension with size 1. For a (3, 4) array, np.mean(arr, axis=1, keepdims=True) returns (3, 1) instead of (3,), useful for broadcasting*

---

### Question 5
Given `arr = np.array([10, 20, 30, 40, 50])`, what does `np.argmax(arr)` return?

A) 50 (the maximum value)
B) 4 (the index of maximum)
C) 5 (the length of array)
D) [10, 20, 30, 40, 50]

**Correct Answer: B**
*Explanation: np.argmax() returns the INDEX of the maximum value, not the value itself. The max value 50 is at index 4. Use np.max() to get the value*
