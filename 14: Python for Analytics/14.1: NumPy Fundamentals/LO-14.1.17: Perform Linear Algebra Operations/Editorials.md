## Editorials: Perform Linear Algebra Operations

### Q1 Solution: Matrix Multiplication and Dot Products

```python
import numpy as np

# Create matrices
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("Matrix A (2×3):")
print(A)

print("\nMatrix B (3×2):")
print(B)

# A @ B
result_AB = A @ B
print("\nA @ B (2×2):")
print(result_AB)

# B @ A
result_BA = B @ A
print("\nB @ A (3×3):")
print(result_BA)

# Dot product of first row of A with first column of B
dot_prod = np.dot(A[0], B[:, 0])
print(f"\nDot product of A[0] and B[:, 0]: {dot_prod}")

# Verify dimensions
print(f"\nDimension check:")
print(f"A shape: {A.shape}, B shape: {B.shape}")
print(f"A @ B works: (2,3) @ (3,2) = (2,2) ✓")
print(f"B @ A works: (3,2) @ (2,3) = (3,3) ✓")
```

**Explanation:**
- Matrix multiplication: (m×n) @ (n×p) → (m×p)
- Inner dimensions must match (n)
- Result has outer dimensions (m×p)
- A @ B ≠ B @ A (different shapes and values)
- Dot product: element-wise multiply and sum
- @ operator is cleaner than np.dot() for matrices

---

### Q2 Solution: Matrix Inverse and Determinant

```python
import numpy as np

# Regular matrix
A = np.array([[4, 7],
              [2, 6]])

print("Matrix A:")
print(A)

# Determinant
det = np.linalg.det(A)
print(f"\nDeterminant: {det}")

# Inverse
A_inv = np.linalg.inv(A)
print("\nInverse:")
print(A_inv)

# Verify A @ A^(-1) = I
identity = A @ A_inv
print("\nA @ A⁻¹:")
print(np.round(identity, 10))  # Round to remove floating point errors

# Singular matrix
singular = np.array([[1, 2],
                     [2, 4]])

print("\nSingular matrix:")
print(singular)

det_singular = np.linalg.det(singular)
print(f"Determinant: {det_singular}")

# Try to invert
try:
    inv_singular = np.linalg.inv(singular)
    print("Inverse:")
    print(inv_singular)
except np.linalg.LinAlgError as e:
    print(f"Error: Matrix is singular and cannot be inverted!")
```

**Explanation:**
- Determinant measures "volume scaling" of transformation
- det = 0 means matrix is singular (not invertible)
- For 2×2: det = ad - bc
- Inverse: A @ A^(-1) = I (identity matrix)
- np.linalg.inv() raises LinAlgError for singular matrices
- Always check determinant before inverting
- Use np.round() to clean up floating point errors

---

### Q3 Solution: Solving Linear Systems

```python
import numpy as np

# Coefficient matrix
A = np.array([[3.0, 2.0, -1.0],
              [2.0, -2.0, 4.0],
              [-1.0, 0.5, -1.0]])

# Constants
b = np.array([1.0, -2.0, 0.0])

print("Coefficient matrix A:")
print(A)

print("\nConstants vector b:")
print(b)

# Solve Ax = b
x = np.linalg.solve(A, b)
print("\nSolution [x, y, z]:")
print(x)

# Verify by substitution
print("\nVerification:")
eq1 = 3*x[0] + 2*x[1] - x[2]
eq2 = 2*x[0] - 2*x[1] + 4*x[2]
eq3 = -x[0] + 0.5*x[1] - x[2]

print(f"Equation 1: 3({x[0]:.1f}) + 2({x[1]:.1f}) - ({x[2]:.1f}) = {eq1:.1f} ✓")
print(f"Equation 2: 2({x[0]:.1f}) - 2({x[1]:.1f}) + 4({x[2]:.1f}) = {eq2:.1f} ✓")
print(f"Equation 3: -({x[0]:.1f}) + 0.5({x[1]:.1f}) - ({x[2]:.1f}) = {eq3:.1f} ✓")

# Alternative verification using matrix multiplication
verification = A @ x
print(f"\nMatrix verification A @ x:")
print(verification)
print(f"Should equal b: {b}")
print(f"All equations satisfied: {np.allclose(verification, b)}")
```

**Explanation:**
- System of linear equations: Ax = b
- np.linalg.solve() finds exact solution
- More efficient than computing inverse manually
- Internally uses LU decomposition
- Verification: A @ x should equal b
- Use np.allclose() to check equality with tolerance
- Only works for square, non-singular matrices

---

### Q4 Solution: Eigenvalues and Principal Components

```python
import numpy as np

# Covariance matrix
cov_matrix = np.array([[4.0, 2.0, 0.5],
                       [2.0, 3.0, 1.0],
                       [0.5, 1.0, 2.0]])

print("Covariance matrix:")
print(cov_matrix)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort by eigenvalue (descending)
idx = eigenvalues.argsort()[::-1]
eigenvalues_sorted = eigenvalues[idx]
eigenvectors_sorted = eigenvectors[:, idx]

print("\nEigenvalues (sorted):")
print(np.round(eigenvalues_sorted, 2))

# Variance explained
total_variance = np.sum(eigenvalues_sorted)
variance_explained = (eigenvalues_sorted / total_variance) * 100

print("\nVariance explained:")
for i, var in enumerate(variance_explained, 1):
    print(f"Component {i}: {var:.2f}%")

# Principal component
principal_component = eigenvectors_sorted[:, 0]
print("\nPrincipal component (eigenvector):")
print(np.round(principal_component, 2))

# Verify eigenvector equation: A @ v = λ * v
print("\nVerification A @ v = λ * v:")
for i in range(len(eigenvalues_sorted)):
    λ = eigenvalues_sorted[i]
    v = eigenvectors_sorted[:, i]
    
    left = cov_matrix @ v
    right = λ * v
    
    match = np.allclose(left, right)
    print(f"Component {i+1}: {match}")

print(f"\nAll verifications passed: {np.allclose(cov_matrix @ principal_component, eigenvalues_sorted[0] * principal_component)}")
```

**Explanation:**
- Eigenvalue equation: A @ v = λ * v
- λ (lambda): eigenvalue (scalar)
- v: eigenvector (direction)
- np.linalg.eig() returns both
- Eigenvalues show variance in each direction
- Sort by eigenvalue to find principal components
- First eigenvector = direction of maximum variance
- Used in PCA for dimensionality reduction
- Variance explained = eigenvalue / sum(eigenvalues)
- Eigenvectors are orthogonal for symmetric matrices

---

### Q5 Solution: Portfolio Risk Analysis

```python
import numpy as np

# Expected returns
returns = np.array([0.08, 0.12, 0.10, 0.09])

# Covariance matrix
cov_matrix = np.array([
    [0.04, 0.01, 0.02, 0.005],
    [0.01, 0.09, 0.015, 0.01],
    [0.02, 0.015, 0.06, 0.008],
    [0.005, 0.01, 0.008, 0.05]
])

print("Expected Returns:", [f"{r:.1%}" for r in returns])
print("\nCovariance Matrix:")
print(cov_matrix)

# Equal-weight portfolio
equal_weights = np.array([0.25, 0.25, 0.25, 0.25])

# Portfolio return
equal_return = equal_weights @ returns
print(f"\nEqual-weight Portfolio (25% each):")
print(f"  Expected Return: {equal_return:.2%}")

# Portfolio variance and risk
equal_variance = equal_weights @ cov_matrix @ equal_weights
equal_risk = np.sqrt(equal_variance)
print(f"  Risk (Std Dev): {equal_risk:.2%}")
print(f"  Variance: {equal_variance:.4f}")

# Minimum variance portfolio
# Solve: minimize w^T Σ w subject to sum(w) = 1
# Solution: w = Σ^(-1) 1 / (1^T Σ^(-1) 1)

ones = np.ones(len(returns))
cov_inv = np.linalg.inv(cov_matrix)

# Minimum variance weights
min_var_weights = cov_inv @ ones / (ones @ cov_inv @ ones)

# Ensure weights sum to 1
min_var_weights = min_var_weights / np.sum(min_var_weights)

print(f"\nMinimum Variance Portfolio:")
print(f"  Weights: {[f'{w:.1%}' for w in min_var_weights]}")

# Minimum variance return and risk
min_var_return = min_var_weights @ returns
min_var_variance = min_var_weights @ cov_matrix @ min_var_weights
min_var_risk = np.sqrt(min_var_variance)

print(f"  Expected Return: {min_var_return:.2%}")
print(f"  Risk (Std Dev): {min_var_risk:.2%}")
print(f"  Variance: {min_var_variance:.4f}")

# Risk reduction
risk_reduction = ((equal_risk - min_var_risk) / equal_risk) * 100
print(f"\nRisk Reduction: {risk_reduction:.2f}%")
```

**Explanation:**
- Portfolio return: w^T r (weights × returns)
- Portfolio variance: w^T Σ w (quadratic form)
- Portfolio risk: √variance (standard deviation)
- Minimum variance portfolio minimizes risk
- Formula: w = Σ^(-1) 1 / (1^T Σ^(-1) 1)
- Requires matrix inverse of covariance
- Weights must sum to 1 (fully invested)
- Trade-off: lower risk often means lower return
- Linear algebra enables optimal portfolio construction

---

### Key Concepts Demonstrated:

1. **Matrix Multiplication:**
   - Dimensions must be compatible
   - @ operator for clarity
   - Not commutative (A @ B ≠ B @ A)

2. **Matrix Inverse:**
   - Only for square, non-singular matrices
   - Check determinant first
   - A @ A^(-1) = I

3. **Linear Systems:**
   - np.linalg.solve() for exact solutions
   - More efficient than manual inverse
   - Verify solutions

4. **Eigendecomposition:**
   - A @ v = λ * v
   - Used in PCA, stability analysis
   - Sort by eigenvalue for importance

5. **Applications:**
   - Finance: portfolio optimization
   - ML: principal components
   - Physics: system dynamics
   - Graphics: transformations
