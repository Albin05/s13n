## Pre-Read: Perform Linear Algebra Operations

### What You'll Learn

In this session, you'll master NumPy's linear algebra capabilities - the mathematical foundation powering machine learning, data science, computer graphics, optimization, and scientific computing.

### Why It Matters

Linear algebra is essential for:

1. **Machine Learning**: Neural networks, PCA, regression
2. **Data Science**: Dimensionality reduction, feature engineering
3. **Computer Graphics**: 3D transformations, rendering
4. **Optimization**: Solving systems, finding optimal solutions
5. **Scientific Computing**: Simulations, modeling

Real-world examples:
- Recommendation systems use matrix factorization
- Image compression uses singular value decomposition
- Portfolio optimization uses matrix operations
- Neural networks are matrix multiplications
- Computer graphics transforms use rotation matrices

### Key Concepts Preview

**Matrix Multiplication:**
- Combines two matrices
- Dimensions must be compatible
- Powers transformations and models

**Matrix Inverse:**
- "Undoes" a matrix transformation
- Used in solving equations
- Only exists for certain matrices

**Eigenvalues/Eigenvectors:**
- Special vectors that only scale under transformation
- Used in PCA, stability analysis
- Core to many algorithms

**Basic examples:**
```python
import numpy as np

# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = A @ B
# [[19 22]
#  [43 50]]

# Solve system: 2x + 3y = 8, 5x + 4y = 13
A = np.array([[2, 3], [5, 4]])
b = np.array([8, 13])
x = np.linalg.solve(A, b)
# [1. 2.]  means x=1, y=2
```

### What to Expect

You'll learn:
1. Matrix multiplication and dot products
2. Matrix transpose and inverse
3. Computing determinants
4. Solving linear systems
5. Finding eigenvalues and eigenvectors
6. Applying linear algebra to real problems

### Prepare

Make sure you have:
- NumPy installed
- Basic linear algebra concepts (matrices, vectors)
- Understanding of array operations
- Familiarity with mathematical notation

### Quick Examples

**Matrix Multiplication:**
```python
import numpy as np

# Two matrices
A = np.array([[1, 2], [3, 4]])  # 2×2
B = np.array([[5, 6], [7, 8]])  # 2×2

# Matrix multiplication (NOT element-wise!)
C = A @ B  # or np.dot(A, B)
print(C)
# [[1*5+2*7  1*6+2*8]  = [[19 22]
#  [3*5+4*7  3*6+4*8]]  =  [43 50]]

# Element-wise (different!)
D = A * B
# [[1*5  2*6]  = [[ 5 12]
#  [3*7  4*8]]  =  [21 32]]
```

**Solving Equations:**
```python
# System: 2x + y = 5
#         x + 3y = 6

A = np.array([[2, 1],
              [1, 3]])
b = np.array([5, 6])

solution = np.linalg.solve(A, b)
# [1.8 1.4]  means x=1.8, y=1.4
```

**Matrix Inverse:**
```python
A = np.array([[4, 7], [2, 6]])

A_inv = np.linalg.inv(A)

# Verify: A @ A_inv = I (identity)
I = A @ A_inv
# [[1. 0.]
#  [0. 1.]]
```

### Understanding Matrix Multiplication

**Rule:** (m×n) @ (n×p) = (m×p)

```
A (2×3)      B (3×2)      C (2×2)
[1 2 3]      [7  8]       [58  64]
[4 5 6]  @   [9  10]  =   [139 154]
             [11 12]
```

Inner dimensions (3) must match!

**Cannot multiply:**
- (2×3) @ (2×3) ✗ (inner dims 3≠2)
- (2×2) @ (3×2) ✗ (inner dims 2≠3)

**Can multiply:**
- (2×3) @ (3×2) ✓ = (2×2)
- (3×4) @ (4×1) ✓ = (3×1)
- (1×n) @ (n×1) ✓ = (1×1) scalar

### @ vs * Operators

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# @ is matrix multiplication
C = A @ B
# [[19 22]
#  [43 50]]

# * is element-wise
D = A * B
# [[ 5 12]
#  [21 32]]

# Always use @ for linear algebra!
```

### Linear Systems

**Problem:** Find x and y:
```
3x + 2y = 7
x - y = 1
```

**Matrix Form:** Ax = b
```
[3  2] [x]   [7]
[1 -1] [y] = [1]
```

**Solution:**
```python
A = np.array([[3, 2], [1, -1]])
b = np.array([7, 1])
x = np.linalg.solve(A, b)
# [2.2 0.6]
```

### Eigenvalues Intuition

**Question:** For which vectors v does matrix A only scale (not rotate)?

A @ v = λ * v

```python
A = np.array([[2, 0], [0, 3]])

eigenvals, eigenvecs = np.linalg.eig(A)
# eigenvals: [2, 3]
# eigenvecs: [[1, 0], [0, 1]]
```

This diagonal matrix scales [1,0] by 2 and [0,1] by 3!

### Common Functions

**Matrix Operations:**
- `A @ B` - matrix multiplication
- `A.T` - transpose
- `np.linalg.inv(A)` - inverse
- `np.linalg.det(A)` - determinant

**Solving:**
- `np.linalg.solve(A, b)` - solve Ax=b
- `np.linalg.lstsq(A, b)` - least squares

**Decomposition:**
- `np.linalg.eig(A)` - eigenvalues/vectors
- `np.linalg.svd(A)` - singular value decomposition

### Try to Predict

```python
A = np.array([[1, 2], [3, 4]])  # 2×2
B = np.array([[5], [6]])        # 2×1

# What shape is A @ B?
result = A @ B  # ?

# What is the determinant?
det = np.linalg.det(A)  # ?

# Can we multiply B @ A?
result2 = B @ A  # ?
```

Answers:
- A @ B: (2×2) @ (2×1) = (2×1) ✓
- det(A) = 1*4 - 2*3 = -2
- B @ A: (2×1) @ (2×2) = (2×2) ✓

### Real Applications

**Machine Learning:**
```python
# Neural network: output = weights @ input
W = np.array([[0.5, 0.3], [0.2, 0.8]])
x = np.array([1.0, 0.5])
y = W @ x  # Layer output
```

**Computer Graphics:**
```python
# Rotate point by 45 degrees
theta = np.pi / 4
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
point = np.array([1, 0])
rotated = R @ point
```

**Economics:**
```python
# Solve supply-demand equilibrium
# Supply: p = 2q + 3
# Demand: p = -q + 9
A = np.array([[1, -2], [1, 1]])
b = np.array([3, 9])
equilibrium = np.linalg.solve(A, b)
# [p, q] equilibrium point
```

Linear algebra is the language of modern data science!
