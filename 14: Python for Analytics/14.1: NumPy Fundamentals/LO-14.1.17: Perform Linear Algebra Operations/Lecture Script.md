## Perform Linear Algebra Operations

### Hook (2 minutes)

**Scenario:**
You're building a recommendation system that needs to compute similarity between user preferences represented as vectors. Or you're solving a system of equations to optimize resource allocation in your business.

A data scientist transforms images using matrix operations. A machine learning engineer computes gradients using dot products. An economist solves simultaneous equations for market equilibrium.

These all use linear algebra - the mathematical foundation of data science, machine learning, computer graphics, and scientific computing. NumPy provides powerful tools to perform these operations efficiently.

**What You'll Learn:**
1. Perform matrix multiplication and dot products
2. Compute matrix transpose and inverse
3. Calculate determinants and rank
4. Find eigenvalues and eigenvectors
5. Solve systems of linear equations
6. Apply linear algebra to real problems

---

### Section 1: Dot Product and Matrix Multiplication (5 minutes)

**Dot Product (1D arrays):**

```python
import numpy as np

# Vector dot product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)
print(f"Dot product: {dot_product}")
# 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32

# Alternative: @ operator
result = a @ b
print(f"Using @: {result}")  # 32
```

**Matrix-Vector Multiplication:**

```python
# Matrix × Vector
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

vector = np.array([1, 2, 3])

result = np.dot(matrix, vector)
print("Matrix × Vector:")
print(result)
# [1*1 + 2*2 + 3*3,  = [14,
#  4*1 + 5*2 + 6*3]  =  32]
```

**Matrix-Matrix Multiplication:**

```python
# Matrix A (2×3) × Matrix B (3×2)
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

C = np.dot(A, B)
print("Matrix multiplication (2×3) × (3×2):")
print(C)
# Shape: (2, 2)
# [[1*7+2*9+3*11  1*8+2*10+3*12]   = [[58  64]
#  [4*7+5*9+6*11  4*8+5*10+6*12]]  =  [139 154]]
```

**Using @ Operator:**

```python
# @ is more readable for matrix operations
result1 = A @ B        # Same as np.dot(A, B)
result2 = matrix @ vector  # Same as np.dot(matrix, vector)

print(np.array_equal(result1, np.dot(A, B)))  # True
```

**matmul vs dot vs multiply:**

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
mat1 = np.matmul(a, b)
mat2 = a @ b
mat3 = np.dot(a, b)
print("All equal:", np.array_equal(mat1, mat2) and np.array_equal(mat2, mat3))
# True for 2D

# Element-wise multiplication (NOT matrix mult)
elem_mult = np.multiply(a, b)  # or a * b
print("\nElement-wise:")
print(elem_mult)
# [[1*5  2*6]  = [[ 5 12]
#  [3*7  4*8]]  =  [21 32]]
```

---

### Section 2: Transpose and Reshape for Linear Algebra (2 minutes)

**Transpose:**

```python
import numpy as np

# Matrix transpose
A = np.array([[1, 2, 3],
              [4, 5, 6]])

A_T = A.T
print("Original (2×3):")
print(A)
print("\nTranspose (3×2):")
print(A_T)
# [[1 4]
#  [2 5]
#  [3 6]]
```

**Practical Use:**

```python
# Column vector × Row vector = Outer product
col = np.array([[1], [2], [3]])  # (3, 1)
row = np.array([[4, 5, 6]])      # (1, 3)

outer = col @ row
print("Outer product (3×1) @ (1×3):")
print(outer)
# [[ 4  5  6]
#  [ 8 10 12]
#  [12 15 18]]

# Row vector × Column vector = Inner product (scalar)
inner = row @ col
print("\nInner product (1×3) @ (3×1):")
print(inner)  # [[32]]
```

---

### Section 3: Matrix Inverse and Determinant (4 minutes)

**Matrix Inverse:**

```python
import numpy as np

# Square matrix
A = np.array([[4, 7],
              [2, 6]])

# Calculate inverse
A_inv = np.linalg.inv(A)
print("Matrix A:")
print(A)
print("\nInverse A⁻¹:")
print(A_inv)

# Verify: A @ A⁻¹ = I (identity matrix)
I = A @ A_inv
print("\nA @ A⁻¹ (should be identity):")
print(np.round(I, 10))  # Round to remove floating point errors
# [[1. 0.]
#  [0. 1.]]
```

**Determinant:**

```python
# Determinant
det = np.linalg.det(A)
print(f"\nDeterminant: {det}")
# 4*6 - 7*2 = 24 - 14 = 10
```

**Singular Matrix (No Inverse):**

```python
# Singular matrix (det = 0)
singular = np.array([[1, 2],
                     [2, 4]])

det = np.linalg.det(singular)
print(f"Determinant: {det}")  # 0 (or very close)

try:
    inv = np.linalg.inv(singular)
except np.linalg.LinAlgError:
    print("Matrix is singular - no inverse exists!")
```

**3×3 Matrix:**

```python
# Larger matrix
B = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

det_B = np.linalg.det(B)
print(f"Determinant of B: {det_B}")

B_inv = np.linalg.inv(B)
print("Inverse of B:")
print(B_inv)

# Verify
identity = B @ B_inv
print("\nB @ B⁻¹:")
print(np.round(identity, 10))
```

---

### Section 4: Solving Linear Systems (4 minutes)

**System of Equations:**

Solve:
```
2x + 3y = 8
5x + 4y = 13
```

In matrix form: Ax = b

```python
import numpy as np

# Coefficient matrix A
A = np.array([[2, 3],
              [5, 4]])

# Constants vector b
b = np.array([8, 13])

# Solve for x
x = np.linalg.solve(A, b)
print("Solution:")
print(f"x = {x[0]}, y = {x[1]}")
# x = 1.0, y = 2.0

# Verify solution
verification = A @ x
print(f"\nVerification A @ x = {verification}")
print(f"Should equal b = {b}")
print(f"Match: {np.allclose(verification, b)}")
```

**Larger System:**

Solve:
```
x + 2y + 3z = 14
2x + 3y + 4z = 20
3x + 4y + 5z = 26
```

```python
A = np.array([[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5]])

b = np.array([14, 20, 26])

x = np.linalg.solve(A, b)
print("Solution [x, y, z]:")
print(x)

# Verify
print(f"Verification: {np.allclose(A @ x, b)}")
```

**Overdetermined System (Least Squares):**

```python
# More equations than unknowns
# Find best-fit solution
A = np.array([[1, 1],
              [1, 2],
              [1, 3],
              [1, 4]])

b = np.array([2, 3, 4, 5])

# Least squares solution
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
print("Least squares solution:")
print(x)
print(f"Residuals: {residuals}")
```

---

### Section 5: Eigenvalues and Eigenvectors (3 minutes)

**Basic Concept:**

For matrix A and vector v:
Av = λv (where λ is eigenvalue, v is eigenvector)

```python
import numpy as np

A = np.array([[4, 2],
              [1, 3]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
```

**Verification:**

```python
# Verify: A @ v = λ @ v
for i in range(len(eigenvalues)):
    λ = eigenvalues[i]
    v = eigenvectors[:, i]
    
    left = A @ v
    right = λ * v
    
    print(f"\nEigenvalue {i+1}: λ = {λ:.4f}")
    print(f"A @ v = {left}")
    print(f"λ * v = {right}")
    print(f"Match: {np.allclose(left, right)}")
```

**Symmetric Matrix:**

```python
# Symmetric matrices have real eigenvalues
S = np.array([[2, 1],
              [1, 2]])

eigenvalues, eigenvectors = np.linalg.eig(S)
print("Symmetric matrix eigenvalues:")
print(eigenvalues)  # Real values
```

**Applications:**

```python
# Principal Component Analysis (PCA) uses eigendecomposition
# Covariance matrix
cov = np.array([[2.0, 0.8],
                [0.8, 1.0]])

eigenvalues, eigenvectors = np.linalg.eig(cov)

# Sort by eigenvalue (descending)
idx = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("Principal components (eigenvectors):")
print(eigenvectors)
print(f"\nExplained variance (eigenvalues): {eigenvalues}")
```

---

### Section 6: Practical Applications (3 minutes)

**Application 1: Image Transformation**

```python
import numpy as np

# Simple 2D rotation matrix
theta = np.pi / 4  # 45 degrees

rotation = np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

# Point to rotate
point = np.array([1, 0])

# Rotate
rotated = rotation @ point
print(f"Original: {point}")
print(f"Rotated 45°: {np.round(rotated, 3)}")
# [0.707 0.707] - moved to diagonal
```

**Application 2: Portfolio Optimization**

```python
# Returns and covariance matrix
returns = np.array([0.10, 0.12, 0.08])  # Expected returns
cov_matrix = np.array([[0.04, 0.01, 0.02],
                       [0.01, 0.09, 0.01],
                       [0.02, 0.01, 0.16]])

# Equally weighted portfolio
weights = np.array([1/3, 1/3, 1/3])

# Portfolio return
portfolio_return = weights @ returns
print(f"Portfolio return: {portfolio_return:.2%}")

# Portfolio variance
portfolio_variance = weights @ cov_matrix @ weights
print(f"Portfolio variance: {portfolio_variance:.4f}")
print(f"Portfolio std dev: {np.sqrt(portfolio_variance):.4f}")
```

**Application 3: Network Analysis**

```python
# Adjacency matrix (graph connections)
adj_matrix = np.array([[0, 1, 1, 0],
                       [1, 0, 1, 1],
                       [1, 1, 0, 1],
                       [0, 1, 1, 0]])

# Degree centrality (connections per node)
degrees = np.sum(adj_matrix, axis=1)
print(f"Node degrees: {degrees}")

# Two-hop connections
two_hop = adj_matrix @ adj_matrix
print("\nTwo-hop connections:")
print(two_hop)
```

**Application 4: Linear Regression**

```python
# y = mx + b
# Find m and b given data points

# Data
X = np.array([[1, 1],   # [1, x1]
              [1, 2],   # [1, x2]
              [1, 3],   # [1, x3]
              [1, 4]])  # [1, x4]

y = np.array([2.1, 4.0, 5.9, 8.1])

# Solve: (X^T X) β = X^T y
beta = np.linalg.inv(X.T @ X) @ X.T @ y
print(f"Intercept: {beta[0]:.2f}")
print(f"Slope: {beta[1]:.2f}")

# Predictions
y_pred = X @ beta
print(f"\nPredictions: {np.round(y_pred, 2)}")
print(f"Actual: {y}")
```

---

### Summary (1 minute)

**Key Operations Covered:**

1. **Matrix Multiplication:**
   - `np.dot(A, B)` or `A @ B`
   - `np.matmul(A, B)` - same as @
   - Different from element-wise `*`

2. **Matrix Properties:**
   - `A.T` - transpose
   - `np.linalg.inv(A)` - inverse
   - `np.linalg.det(A)` - determinant
   - `np.linalg.matrix_rank(A)` - rank

3. **Solving Systems:**
   - `np.linalg.solve(A, b)` - exact solution
   - `np.linalg.lstsq(A, b)` - least squares

4. **Eigendecomposition:**
   - `np.linalg.eig(A)` - eigenvalues & eigenvectors
   - Used in PCA, stability analysis

**Quick Reference:**

```python
# Multiplication
A @ B              # Matrix multiplication
np.dot(a, b)       # Dot product

# Matrix operations
A.T                # Transpose
np.linalg.inv(A)   # Inverse
np.linalg.det(A)   # Determinant

# Solving
np.linalg.solve(A, b)     # Ax = b
np.linalg.lstsq(A, b)     # Least squares

# Eigendecomposition
np.linalg.eig(A)          # Eigenvalues/vectors
```

**Remember:**
- Matrix multiplication: (m×n) @ (n×p) = (m×p)
- Only square matrices have inverses
- Check determinant ≠ 0 for invertibility
- Use @ for clarity in matrix operations

**Next Steps:**
- Practice matrix operations
- Solve real linear systems
- Apply to machine learning
- Understand computational complexity

Linear algebra powers modern data science and ML!
