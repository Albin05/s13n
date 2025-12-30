## Perform Linear Algebra Operations

### Matrix Multiplication

```python
import numpy as np

# Dot product (1D)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot = np.dot(a, b)  # or a @ b
# 1*4 + 2*5 + 3*6 = 32

# Matrix multiplication
A = np.array([[1, 2, 3],
              [4, 5, 6]])  # (2, 3)

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])   # (3, 2)

C = A @ B  # (2, 2)
# [[58  64]
#  [139 154]]
```

**Key Points:**
- Dimensions: (m×n) @ (n×p) → (m×p)
- Inner dimensions must match
- Use @ operator (cleaner than np.dot)
- @ ≠ * (matrix mult vs element-wise)

---

### Matrix Inverse and Determinant

```python
A = np.array([[4, 7],
              [2, 6]])

# Determinant
det = np.linalg.det(A)  # 10.0

# Inverse
A_inv = np.linalg.inv(A)

# Verify: A @ A^(-1) = I
identity = A @ A_inv
# [[1. 0.]
#  [0. 1.]]
```

**Key Points:**
- Only square matrices can have inverse
- det ≠ 0 required for invertibility
- A @ A^(-1) = I (identity matrix)
- For 2×2: det = ad - bc

---

### Solving Linear Systems

**System:**
```
2x + 3y = 8
5x + 4y = 13
```

**Solution:**
```python
A = np.array([[2, 3],
              [5, 4]])
b = np.array([8, 13])

x = np.linalg.solve(A, b)
# x = [1., 2.]
```

**Verification:**
```python
verification = A @ x
# Should equal b
```

**Key Points:**
- np.linalg.solve(A, b) solves Ax = b
- More efficient than A_inv @ b
- Only for square systems
- Use lstsq for overdetermined systems

---

### Eigenvalues and Eigenvectors

**Equation:** A @ v = λ * v

```python
A = np.array([[4, 2],
              [1, 3]])

eigenvalues, eigenvectors = np.linalg.eig(A)

# eigenvalues: λ values (scalars)
# eigenvectors: v vectors (columns)
```

**Verification:**
```python
λ = eigenvalues[0]
v = eigenvectors[:, 0]

left = A @ v
right = λ * v
# left ≈ right
```

**Applications:**
- PCA (Principal Component Analysis)
- Stability analysis
- Dimensionality reduction
- System dynamics

---

### Common Operations

**Transpose:**
```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])
A_T = A.T
# [[1 4]
#  [2 5]
#  [3 6]]
```

**Matrix Rank:**
```python
rank = np.linalg.matrix_rank(A)
```

**Trace (sum of diagonal):**
```python
trace = np.trace(A)
```

**Matrix Norm:**
```python
norm = np.linalg.norm(A)
```

---

### Practical Example: Linear Regression

```python
# y = mx + b
# Data points
X = np.array([[1, 1],   # [1, x]
              [1, 2],
              [1, 3],
              [1, 4]])

y = np.array([2, 4, 6, 8])

# Solve: X^T X β = X^T y
beta = np.linalg.inv(X.T @ X) @ X.T @ y
# beta[0] = intercept, beta[1] = slope
```

Or using solve:
```python
beta = np.linalg.solve(X.T @ X, X.T @ y)
```

---

### Practical Example: Portfolio Risk

```python
returns = np.array([0.10, 0.12, 0.08])
cov_matrix = np.array([[0.04, 0.01, 0.02],
                       [0.01, 0.09, 0.01],
                       [0.02, 0.01, 0.16]])

weights = np.array([1/3, 1/3, 1/3])

# Portfolio return
port_return = weights @ returns

# Portfolio variance
port_variance = weights @ cov_matrix @ weights

# Portfolio risk
port_risk = np.sqrt(port_variance)
```

---

### Quick Reference

**Multiplication:**
```python
A @ B              # Matrix multiplication
np.dot(A, B)       # Same as @
A * B              # Element-wise (NOT matrix mult)
```

**Matrix Properties:**
```python
A.T                # Transpose
np.linalg.inv(A)   # Inverse
np.linalg.det(A)   # Determinant
np.linalg.matrix_rank(A)  # Rank
np.trace(A)        # Trace
```

**Solving:**
```python
np.linalg.solve(A, b)     # Exact solution Ax=b
np.linalg.lstsq(A, b)     # Least squares
```

**Eigendecomposition:**
```python
eigenvals, eigenvecs = np.linalg.eig(A)
```

---

### Key Takeaways

1. **Matrix Multiplication:**
   - Check dimension compatibility
   - Use @ not *
   - (m×n) @ (n×p) = (m×p)

2. **Inverse:**
   - Square matrices only
   - det ≠ 0 required
   - Check before inverting

3. **Linear Systems:**
   - Use solve() not inv()
   - More efficient and stable
   - Verify solutions

4. **Eigendecomposition:**
   - A @ v = λ * v
   - Sort by eigenvalue
   - Critical for PCA, dynamics

5. **Applications:**
   - Machine learning
   - Finance/economics
   - Computer graphics
   - Scientific computing
