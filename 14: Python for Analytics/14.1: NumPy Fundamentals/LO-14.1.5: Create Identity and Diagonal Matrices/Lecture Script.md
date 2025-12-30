### Create Identity and Diagonal Matrices

### Hook (2 minutes)

"In linear algebra and machine learning, certain special matrices appear everywhere: the identity matrix (like the number 1 for matrices) and diagonal matrices (where only the main diagonal has values). These matrices are fundamental for solving systems of equations, transforming data, and understanding linear transformations. NumPy makes creating these special matrices effortless. Let's explore!"

### Section 1: Introduction to Special Matrices (3 minutes)

**What are special matrices?**

Special matrices have specific patterns that make them useful in mathematics and data science:
- **Identity Matrix**: Diagonal of 1s, everything else 0
- **Diagonal Matrix**: Non-zero values only on the diagonal

**Why are they important?**

1. **Linear Algebra**: Fundamental for matrix operations
2. **Machine Learning**: Regularization, normalization
3. **Computer Graphics**: Transformations, scaling
4. **Numerical Methods**: Solving equations efficiently

**Key properties:**
- Identity matrix: Multiplying any matrix by I gives the same matrix (A × I = A)
- Diagonal matrices: Fast computation, easy to invert

### Section 2: Create Identity Matrix with np.eye() (4 minutes)

**What is an identity matrix?**

An identity matrix is a square matrix with:
- 1s on the main diagonal (top-left to bottom-right)
- 0s everywhere else

**Why "eye"?**

Named "eye" because it's denoted by the letter "I" in mathematics.

**Syntax:**
```python
np.eye(N, M=None, k=0, dtype=float)
```
- **N**: Number of rows
- **M**: Number of columns (default: same as N)
- **k**: Diagonal offset (default: 0 for main diagonal)
- **dtype**: Data type (default: float)

**Examples:**

```python
import numpy as np

# 3×3 identity matrix
I3 = np.eye(3)
print(I3)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 4×4 identity matrix
I4 = np.eye(4)
print(I4)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# Integer identity matrix
I_int = np.eye(3, dtype=int)
print(I_int)
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]
```

**Non-square identity matrices:**

```python
# 3 rows, 5 columns
I = np.eye(3, 5)
print(I)
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]]
```

**Offset diagonal with k parameter:**

```python
# Diagonal shifted up by 1
I_up = np.eye(3, k=1)
print(I_up)
# [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

# Diagonal shifted down by 1
I_down = np.eye(3, k=-1)
print(I_down)
# [[0. 0. 0.]
#  [1. 0. 0.]
#  [0. 1. 0.]]
```

### Section 3: Create Diagonal Matrix with np.diag() (4 minutes)

**What is a diagonal matrix?**

A diagonal matrix has:
- Specified values on the diagonal
- 0s everywhere else

**Syntax:**
```python
np.diag(v, k=0)
```
- **v**: Array of diagonal elements or a 2D matrix
- **k**: Diagonal offset (default: 0)

**Two modes of operation:**

1. **Array → Diagonal Matrix**: Create matrix from diagonal values
2. **Matrix → Diagonal**: Extract diagonal from matrix

**Mode 1: Create diagonal matrix from array:**

```python
import numpy as np

# Diagonal with values [1, 2, 3]
diag_values = [1, 2, 3]
D = np.diag(diag_values)
print(D)
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]

# Diagonal with different values
D2 = np.diag([10, 20, 30, 40])
print(D2)
# [[10  0  0  0]
#  [ 0 20  0  0]
#  [ 0  0 30  0]
#  [ 0  0  0 40]]
```

**With offset diagonal:**

```python
# Diagonal above main diagonal (k=1)
D_up = np.diag([5, 10, 15], k=1)
print(D_up)
# [[ 0  5  0  0]
#  [ 0  0 10  0]
#  [ 0  0  0 15]
#  [ 0  0  0  0]]

# Diagonal below main diagonal (k=-1)
D_down = np.diag([5, 10, 15], k=-1)
print(D_down)
# [[ 0  0  0  0]
#  [ 5  0  0  0]
#  [ 0 10  0  0]
#  [ 0  0 15  0]]
```

**Mode 2: Extract diagonal from matrix:**

```python
# Create a matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Extract main diagonal
main_diag = np.diag(matrix)
print(main_diag)  # [1 5 9]

# Extract diagonal above main (k=1)
upper_diag = np.diag(matrix, k=1)
print(upper_diag)  # [2 6]

# Extract diagonal below main (k=-1)
lower_diag = np.diag(matrix, k=-1)
print(lower_diag)  # [4 8]
```

### Section 4: Create Identity Matrix with np.identity() (2 minutes)

**Alternative: np.identity()**

`np.identity()` is simpler but only creates square identity matrices.

**Syntax:**
```python
np.identity(n, dtype=float)
```
- **n**: Size of the square matrix (n×n)

**Examples:**

```python
import numpy as np

# 3×3 identity
I = np.identity(3)
print(I)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Integer identity
I_int = np.identity(4, dtype=int)
print(I_int)
# [[1 0 0 0]
#  [0 1 0 0]
#  [0 0 1 0]
#  [0 0 0 1]]
```

**eye() vs identity():**

| Feature | np.eye() | np.identity() |
|---------|----------|---------------|
| Square only | No (can be rectangular) | Yes |
| Offset diagonal | Yes (k parameter) | No |
| Simplicity | More flexible | Simpler |

**When to use:**
- Use `identity()` for simple square identity matrices
- Use `eye()` for non-square or offset diagonals

### Section 5: Practical Applications (3 minutes)

**1. Matrix Operations:**

```python
import numpy as np

# Matrix multiplication with identity
A = np.array([[1, 2],
              [3, 4]])
I = np.eye(2)

# A × I = A
result = A @ I  # or np.dot(A, I)
print(result)
# [[1. 2.]
#  [3. 4.]]  - Same as A!
```

**2. Scaling Matrix:**

```python
# Create scaling matrix (scale by 2, 3, 4)
scale_factors = [2, 3, 4]
S = np.diag(scale_factors)
print(S)
# [[2 0 0]
#  [0 3 0]
#  [0 0 4]]
```

**3. Correlation/Covariance Matrices:**

```python
# Extract diagonal (variances) from covariance matrix
cov_matrix = np.array([[4, 1, 0],
                       [1, 9, 2],
                       [0, 2, 16]])
variances = np.diag(cov_matrix)
print(variances)  # [4 9 16]
```

**4. Regularization in Machine Learning:**

```python
# Add regularization to matrix (Ridge regression)
X = np.random.rand(3, 3)
lambda_val = 0.1
I = np.eye(3)

# Regularized matrix: X^T X + λI
regularized = X.T @ X + lambda_val * I
```

### Section 6: Comparison and Best Practices (2 minutes)

**Quick comparison:**

| Function | Purpose | Output |
|----------|---------|--------|
| `eye(3)` | 3×3 identity matrix | 1s on diagonal |
| `identity(3)` | 3×3 identity (simpler) | 1s on diagonal |
| `diag([1,2,3])` | Diagonal matrix from array | Values on diagonal |
| `diag(matrix)` | Extract diagonal from matrix | 1D array |

**Best practices:**

1. **Use eye() when:**
   - Need non-square matrices
   - Need offset diagonals
   - More flexibility required

2. **Use identity() when:**
   - Need simple square identity
   - Code readability is priority

3. **Use diag() for:**
   - Creating diagonal matrices with custom values
   - Extracting diagonals from existing matrices

**Common patterns:**
```python
# Initialize weights for regularization
I = np.eye(n_features)
weights = inv(X.T @ X + lambda_reg * I) @ X.T @ y

# Create scaling transformation
scale = np.diag([sx, sy, sz])

# Extract main diagonal of result matrix
variance = np.diag(covariance_matrix)
```

### Summary (2 minutes)

**Key Takeaways:**

1. **np.eye(N, M, k)**: Create identity matrix (flexible, can be non-square, supports offset)
2. **np.identity(n)**: Create square identity matrix (simpler alternative to eye)
3. **np.diag(v, k)**: Two modes:
   - Array → Diagonal matrix (create)
   - Matrix → Array (extract diagonal)
4. **k parameter**: Controls diagonal offset (0=main, 1=above, -1=below)

**Remember:**
- Identity matrix: I × A = A (acts like number 1)
- Diagonal matrices: Fast operations, easy inversion
- Use eye() for flexibility, identity() for simplicity
- diag() is bidirectional: create or extract

**Next Steps:**
You've completed the first 5 lessons on NumPy Fundamentals! Next, you'll learn array indexing, slicing, and advanced array manipulation techniques!
