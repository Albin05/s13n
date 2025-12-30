## Post-class Quiz: Perform Linear Algebra Operations

### Question 1
What is the result shape when multiplying matrices A(3×4) @ B(4×2)?

A) (3, 2)
B) (4, 4)
C) (3, 4)
D) Error - incompatible shapes

**Correct Answer: A**
*Explanation: Matrix multiplication (m×n) @ (n×p) produces shape (m×p). So (3×4) @ (4×2) = (3×2). Inner dimensions (4) must match*

---

### Question 2
Which condition must be true for a matrix to have an inverse?

A) Matrix must be rectangular
B) Determinant must be non-zero
C) Matrix must be symmetric
D) All elements must be positive

**Correct Answer: B**
*Explanation: A matrix has an inverse only if it's square AND its determinant is non-zero. If det(A) = 0, the matrix is singular and non-invertible*

---

### Question 3
What does `np.linalg.solve(A, b)` do?

A) Computes A × b
B) Solves the equation Ax = b for x
C) Computes the inverse of A
D) Calculates the determinant of A

**Correct Answer: B**
*Explanation: np.linalg.solve(A, b) solves the linear system Ax = b and returns the solution vector x. It's more efficient than manually computing A^(-1) @ b*

---

### Question 4
In the eigenvalue equation A @ v = λ * v, what is λ?

A) The eigenvector
B) The eigenvalue (scalar)
C) The identity matrix
D) The transpose of v

**Correct Answer: B**
*Explanation: λ (lambda) is the eigenvalue, a scalar that scales the eigenvector v when the matrix A is applied to it*

---

### Question 5
What's the difference between `@` and `*` operators for arrays?

A) They are the same
B) @ is matrix multiplication, * is element-wise
C) * is matrix multiplication, @ is element-wise
D) @ only works with 1D arrays

**Correct Answer: B**
*Explanation: @ performs matrix multiplication (dot product), while * performs element-wise multiplication. For matrices A and B, A @ B is matrix multiplication, A * B multiplies corresponding elements*
