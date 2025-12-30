## Question Bank: Perform Linear Algebra Operations

### Q1: Matrix Multiplication and Dot Products (3 minutes, Low Difficulty)

**Problem:**
Create two matrices A (2×3) and B (3×2) with values of your choice. Perform:
1. Matrix multiplication A @ B
2. Matrix multiplication B @ A
3. Dot product of first row of A with first column of B
4. Verify dimensions work for multiplication

**Expected Output:**
```
Matrix A (2×3):
[[1 2 3]
 [4 5 6]]

Matrix B (3×2):
[[7 8]
 [9 10]
 [11 12]]

A @ B (2×2):
[[ 58  64]
 [139 154]]

B @ A (3×3):
[[ 39  54  69]
 [ 49  68  87]
 [ 59  82 105]]

Dot product of A[0] and B[:, 0]: 58
```

**Category:** Implementation  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q2: Matrix Inverse and Determinant (3 minutes, Low Difficulty)

**Problem:**
Create a 2×2 matrix and:
1. Calculate its determinant
2. Calculate its inverse
3. Verify that A @ A⁻¹ equals the identity matrix
4. Create a singular matrix and try to invert it (handle the error)

**Expected Output:**
```
Matrix A:
[[4 7]
 [2 6]]

Determinant: 10.0

Inverse:
[[ 0.6 -0.7]
 [-0.2  0.4]]

A @ A⁻¹:
[[1. 0.]
 [0. 1.]]

Singular matrix:
[[1 2]
 [2 4]]

Determinant: 0.0
Error: Matrix is singular and cannot be inverted!
```

**Category:** Implementation  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q3: Solving Linear Systems (5 minutes, Medium Difficulty)

**Problem:**
Solve the following system of equations using NumPy:

```
3x + 2y - z = 1
2x - 2y + 4z = -2
-x + 0.5y - z = 0
```

Then verify your solution by substituting back into the original equations.

**Expected Output:**
```
Coefficient matrix A:
[[ 3.   2.  -1. ]
 [ 2.  -2.   4. ]
 [-1.   0.5 -1. ]]

Constants vector b:
[ 1. -2.  0.]

Solution [x, y, z]:
[ 1. -2. -2.]

Verification:
Equation 1: 3(1) + 2(-2) - (-2) = 1 ✓
Equation 2: 2(1) - 2(-2) + 4(-2) = -2 ✓
Equation 3: -1(1) + 0.5(-2) - (-2) = 0 ✓

All equations satisfied: True
```

**Category:** Implementation  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q4: Eigenvalues and Principal Components (5 minutes, Medium Difficulty)

**Problem:**
Given a covariance matrix from a dataset, compute its eigenvalues and eigenvectors. Then:
1. Sort eigenvalues in descending order
2. Calculate the percentage of variance explained by each component
3. Identify the principal component (eigenvector with largest eigenvalue)
4. Verify that eigenvector equation holds: A @ v = λ * v

**Input:**
```python
cov_matrix = np.array([[4.0, 2.0, 0.5],
                       [2.0, 3.0, 1.0],
                       [0.5, 1.0, 2.0]])
```

**Expected Output:**
```
Covariance matrix:
[[4.  2.  0.5]
 [2.  3.  1. ]
 [0.5 1.  2. ]]

Eigenvalues (sorted):
[6.24 2.39 0.37]

Variance explained:
Component 1: 69.35%
Component 2: 26.52%
Component 3: 4.13%

Principal component (eigenvector):
[ 0.66  0.63  0.41]

Verification A @ v = λ * v: True
```

**Category:** Application  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q5: Portfolio Risk Analysis (5 minutes, Medium Difficulty)

**Problem:**
You manage a portfolio with 4 stocks. Given expected returns and a covariance matrix:
1. Calculate portfolio return for equal weights
2. Calculate portfolio risk (standard deviation)
3. Find minimum variance portfolio weights by solving optimization
4. Compare risk between equal-weight and minimum variance portfolios

**Input:**
```python
returns = np.array([0.08, 0.12, 0.10, 0.09])  # Expected returns

cov_matrix = np.array([
    [0.04, 0.01, 0.02, 0.005],
    [0.01, 0.09, 0.015, 0.01],
    [0.02, 0.015, 0.06, 0.008],
    [0.005, 0.01, 0.008, 0.05]
])
```

**Expected Output:**
```
Expected Returns: [8.0% 12.0% 10.0% 9.0%]

Covariance Matrix:
[[0.04  0.01  0.02  0.005]
 [0.01  0.09  0.015 0.01 ]
 [0.02  0.015 0.06  0.008]
 [0.005 0.01  0.008 0.05 ]]

Equal-weight Portfolio (25% each):
  Expected Return: 9.75%
  Risk (Std Dev): 16.25%
  Variance: 0.0264

Minimum Variance Portfolio:
  Weights: [58.3% 12.4% 18.2% 11.1%]
  Expected Return: 9.12%
  Risk (Std Dev): 14.87%
  Variance: 0.0221

Risk Reduction: 8.49%
```

**Category:** Application  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Additional Practice Problems

**Challenge 1: Rotation Matrices**
Create a rotation matrix to rotate points by any angle. Apply it to rotate a set of 2D points and visualize.

**Challenge 2: Linear Regression from Scratch**
Implement linear regression using matrix operations: β = (X^T X)^(-1) X^T y

**Challenge 3: Markov Chains**
Create a transition matrix and compute steady-state probabilities using eigenvalues.

**Challenge 4: SVD Decomposition**
Use np.linalg.svd() for image compression - compress a matrix by keeping only top k singular values.
