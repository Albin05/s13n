## In-class Quiz: Create Identity and Diagonal Matrices

### Question 1
What will be the shape of the array created by `np.eye(4, 6)`?

A) `(4, 4)`
B) `(6, 6)`
C) `(4, 6)`
D) `(6, 4)`

**Correct Answer: C**
*Explanation: First parameter is rows (4), second is columns (6)*

---

### Question 2
What does `np.diag([1, 2, 3])` create?

A) A 1D array `[1, 2, 3]`
B) A 3×3 diagonal matrix with 1, 2, 3 on the diagonal
C) A 3×1 column vector
D) An error

**Correct Answer: B**

---

### Question 3
What is the main difference between `np.eye()` and `np.identity()`?

A) eye() is faster than identity()
B) identity() only creates square matrices, eye() can create rectangular
C) eye() only works with integers
D) There is no difference

**Correct Answer: B**

---

### Question 4
What does the k parameter in `np.eye(3, k=1)` do?

A) Sets the value on the diagonal to 1
B) Creates a 3×1 matrix
C) Shifts the diagonal up by 1 position
D) Creates k identity matrices

**Correct Answer: C**
*Explanation: k shifts the diagonal; k=1 moves it up, k=-1 moves it down*

---

### Question 5
What will `np.diag(np.array([[1, 2], [3, 4]]))` return?

A) `[[1, 0], [0, 4]]`
B) `[1, 4]`
C) `[2, 3]`
D) `[[1, 2], [3, 4]]`

**Correct Answer: B**
*Explanation: diag() with a 2D array extracts the main diagonal [1, 4]*
