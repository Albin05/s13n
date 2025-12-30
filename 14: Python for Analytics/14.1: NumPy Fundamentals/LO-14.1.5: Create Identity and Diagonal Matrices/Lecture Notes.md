## Create Identity and Diagonal Matrices

### Introduction to Special Matrices

**What are special matrices?**
- **Identity Matrix**: 1s on diagonal, 0s elsewhere
- **Diagonal Matrix**: Values on diagonal, 0s elsewhere

**Why important?**
- Linear algebra operations
- Machine learning (regularization)
- Computer graphics (transformations)
- Numerical methods

**Key properties:**
- Identity: A × I = A (like multiplying by 1)
- Diagonal: Fast computation, easy inversion

### Create Identity Matrix: np.eye()

**Purpose:**
Creates identity matrix (1s on diagonal, 0s elsewhere)

**Syntax:**
```python
np.eye(N, M=None, k=0, dtype=float)
```
- **N**: Number of rows
- **M**: Number of columns (default: N)
- **k**: Diagonal offset (default: 0)
- **dtype**: Data type (default: float)

**Examples:**
```python
import numpy as np

# 3×3 identity
I = np.eye(3)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 3×5 identity (rectangular)
I = np.eye(3, 5)
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]]

# Offset diagonal (k=1)
I = np.eye(3, k=1)
# [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

# Integer identity
I = np.eye(3, dtype=int)
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]
```

### Create Diagonal Matrix: np.diag()

**Purpose:**
Two modes - create diagonal matrix or extract diagonal

**Syntax:**
```python
np.diag(v, k=0)
```
- **v**: 1D array (create matrix) or 2D matrix (extract diagonal)
- **k**: Diagonal offset

**Mode 1: Create diagonal matrix from array:**
```python
import numpy as np

# Diagonal matrix
D = np.diag([1, 2, 3])
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]

# Offset diagonal
D = np.diag([5, 10], k=1)
# [[0  5  0]
#  [0  0 10]
#  [0  0  0]]
```

**Mode 2: Extract diagonal from matrix:**
```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Main diagonal
main = np.diag(matrix)  # [1, 5, 9]

# Upper diagonal
upper = np.diag(matrix, k=1)  # [2, 6]

# Lower diagonal
lower = np.diag(matrix, k=-1)  # [4, 8]
```

### Create Identity: np.identity()

**Purpose:**
Simpler alternative for square identity matrices only

**Syntax:**
```python
np.identity(n, dtype=float)
```

**Examples:**
```python
import numpy as np

# 3×3 identity
I = np.identity(3)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Integer identity
I = np.identity(4, dtype=int)
```

**eye() vs identity():**

| Feature | np.eye() | np.identity() |
|---------|----------|---------------|
| Square only | No | Yes |
| Offset diagonal | Yes (k parameter) | No |
| Rectangular | Yes | No |

### Practical Applications

**1. Matrix multiplication with identity:**
```python
A = np.array([[1, 2], [3, 4]])
I = np.eye(2)
result = A @ I  # Same as A
```

**2. Scaling transformation:**
```python
# Scale by [2, 3, 4]
S = np.diag([2, 3, 4])
point = np.array([10, 20, 30])
scaled = S @ point  # [20, 60, 120]
```

**3. Extract variances from covariance matrix:**
```python
cov = np.array([[4, 1], [1, 9]])
variances = np.diag(cov)  # [4, 9]
```

**4. Regularization in machine learning:**
```python
# Ridge regression: X^T X + λI
I = np.eye(n_features)
regularized = X.T @ X + lambda_val * I
```

### Function Comparison

| Function | Purpose | Output |
|----------|---------|--------|
| `eye(3)` | 3×3 identity | 1s on diagonal |
| `identity(3)` | 3×3 identity (simpler) | 1s on diagonal |
| `diag([1,2,3])` | Create diagonal matrix | Values on diagonal |
| `diag(matrix)` | Extract diagonal | 1D array |

### Key Takeaways

1. **eye(N, M, k)**: Flexible identity matrix creation
   - Can be rectangular
   - Supports diagonal offset
2. **identity(n)**: Simple square identity only
3. **diag(v, k)**: Bidirectional function
   - 1D array → Diagonal matrix
   - 2D matrix → Extract diagonal
4. **k parameter**: Diagonal offset (0=main, 1=above, -1=below)
5. **Identity property**: A × I = A
6. Use for: linear algebra, transformations, regularization
