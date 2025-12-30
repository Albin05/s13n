## Post-class Quiz: Use Fancy Indexing

### Question 1
What does `arr[[0, 2, 4]]` do?

A) Selects elements at positions 0 through 4
B) Selects elements at indices 0, 2, and 4
C) Creates a slice with step 2
D) Returns a boolean array

**Correct Answer: B**
*Explanation: Fancy indexing with a list/array of indices selects specific elements at those positions*

---

### Question 2
What is the result of `arr[[1, 1, 3]]` if `arr = np.array([10, 20, 30, 40])`?

A) [20, 20, 40]
B) [20, 30, 40]
C) [10, 20, 30]
D) An error occurs

**Correct Answer: A**
*Explanation: Fancy indexing allows repeated indices; index 1 appears twice, so element 20 is selected twice*

---

### Question 3
How do you select specific elements at coordinates (0,0), (1,2), (2,1) from a 2D array?

A) `matrix[[0, 1, 2], [0, 2, 1]]`
B) `matrix[0, 1, 2][0, 2, 1]`
C) `matrix[(0,0), (1,2), (2,1)]`
D) `matrix[0:2, 0:2]`

**Correct Answer: A**
*Explanation: Fancy indexing pairs row indices with column indices: rows [0,1,2] with cols [0,2,1]*

---

### Question 4
What is the difference between slicing and fancy indexing?

A) Slicing is faster but less flexible
B) Slicing creates views; fancy indexing creates copies
C) Slicing only works on 1D arrays
D) They are the same thing

**Correct Answer: B**
*Explanation: Slicing creates views that share memory; fancy indexing always creates copies of data*

---

### Question 5
How do you reverse an array using fancy indexing for `arr = np.array([10, 20, 30, 40, 50])`?

A) `arr[::-1]`
B) `arr[[5, 4, 3, 2, 1]]`
C) `arr[[4, 3, 2, 1, 0]]`
D) `arr.reverse()`

**Correct Answer: C**
*Explanation: Fancy indexing uses indices [4,3,2,1,0] to select elements in reverse order; note that indices are 0-based*
