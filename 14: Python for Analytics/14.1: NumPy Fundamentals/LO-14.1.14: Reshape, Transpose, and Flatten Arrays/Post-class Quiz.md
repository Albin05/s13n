## Post-class Quiz: Reshape, Transpose, and Flatten Arrays

### Question 1
What happens when you reshape an array with 12 elements to shape (3, 5)?

A) Creates a 3x5 array with padding
B) Raises an error
C) Truncates to fit
D) Automatically adjusts to (3, 4)

**Correct Answer: B**
*Explanation: Total elements must match. 12 ≠ 3×5 (15), so it raises a ValueError*

---

### Question 2
What does the -1 parameter mean in `arr.reshape(-1, 4)`?

A) Reverses the array
B) NumPy automatically calculates that dimension
C) Creates a 1D array
D) Removes the dimension

**Correct Answer: B**
*Explanation: -1 tells NumPy to infer that dimension based on array size and other dimensions*

---

### Question 3
What is the main difference between `flatten()` and `ravel()`?

A) No difference
B) `flatten()` creates a copy, `ravel()` returns a view
C) `flatten()` is faster
D) `ravel()` only works on 2D arrays

**Correct Answer: B**
*Explanation: flatten() always creates a copy, while ravel() returns a view when possible (modifying ravel affects original)*

---

### Question 4
Given a matrix with shape (3, 4), what is the shape after transpose?

A) (3, 4)
B) (4, 3)
C) (12,)
D) (1, 12)

**Correct Answer: B**
*Explanation: Transpose swaps dimensions: rows become columns and vice versa, so (3, 4) becomes (4, 3)*

---

### Question 5
Which statement is TRUE about reshape()?

A) It always creates a copy of the data
B) It can change the total number of elements
C) It returns a view when possible
D) It only works on 1D arrays

**Correct Answer: C**
*Explanation: reshape() returns a view when possible (doesn't copy data). Total elements must remain the same*
