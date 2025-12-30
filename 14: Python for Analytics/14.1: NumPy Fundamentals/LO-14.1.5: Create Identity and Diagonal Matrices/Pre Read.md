## Pre-Read: Create Identity and Diagonal Matrices

### What You'll Learn

In this lesson, you'll learn how to create identity and diagonal matrices - fundamental structures in linear algebra, machine learning, and scientific computing.

### Prerequisites

Before starting this lesson, make sure you have:
- Completed LO-14.1.1 through LO-14.1.4
- Understanding of matrix concepts (rows, columns)
- Basic knowledge of linear algebra (helpful but not required)
- NumPy installed and ready to use

### Why Identity and Diagonal Matrices Matter

**Real-world applications:**

1. **Linear Algebra:**
   - Solving systems of equations
   - Matrix inversion
   - Eigenvalue computations

2. **Machine Learning:**
   - Ridge regression regularization: X^T X + λI
   - Neural network weight initialization
   - Batch normalization

3. **Computer Graphics:**
   - Scaling transformations
   - Coordinate system conversions
   - 3D rendering pipelines

4. **Physics & Engineering:**
   - Quantum mechanics (Pauli matrices)
   - Signal processing (filter design)
   - Control systems

**Benefits:**
1. **Identity matrices**: Act like "1" for matrices (A × I = A)
2. **Diagonal matrices**: Fast computation (only diagonal elements matter)
3. **Efficiency**: Easy to invert, multiply, and analyze
4. **Clarity**: Represent simple transformations clearly

### Key Concepts to Understand

**1. Identity Matrix**

The identity matrix is the matrix equivalent of the number 1:
- Square matrix with 1s on the diagonal
- 0s everywhere else
- Property: A × I = I × A = A

Example 3×3 identity:
```
[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]
```

**Why "identity"?**
- Preserves identity of any matrix when multiplied
- Like multiplying a number by 1

**2. Diagonal Matrix**

A matrix with values only on the diagonal:
- All off-diagonal elements are 0
- Can have any values on diagonal
- Fast to multiply and invert

Example diagonal matrix:
```
[[2, 0, 0],
 [0, 5, 0],
 [0, 0, 3]]
```

**Why useful?**
- Scaling: Each dimension scaled independently
- Fast computation: Only need diagonal values
- Easy inversion: Invert each diagonal element

**3. Diagonal Offset (k parameter)**

Diagonals can be offset from the main diagonal:
- **k = 0**: Main diagonal (default)
- **k = 1**: One position above main diagonal
- **k = -1**: One position below main diagonal

Visual example:
```
k=0:  [[1, 0, 0],      k=1:  [[0, 1, 0],      k=-1: [[0, 0, 0],
       [0, 1, 0],             [0, 0, 1],             [1, 0, 0],
       [0, 0, 1]]             [0, 0, 0]]             [0, 1, 0]]
```

### What to Expect

In this lesson, you will learn:

1. **np.eye()**: Create identity matrices
   - Square and rectangular
   - Offset diagonals
   - Different data types

2. **np.identity()**: Simple square identity matrices

3. **np.diag()**: Dual-purpose function
   - Create diagonal matrices from arrays
   - Extract diagonals from matrices

4. **Practical applications**: Real-world use cases

### Preparation Tasks

Before the lesson:
1. Review matrix multiplication basics
2. Understand what "diagonal" means in a matrix
3. Think about why multiplying by 1 preserves a number
4. Consider how scaling works in different dimensions

### Questions to Think About

As you prepare for this lesson, consider:
1. Why might an identity matrix be useful in solving equations?
2. How could diagonal matrices simplify computations?
3. What happens when you multiply any matrix by an identity matrix?
4. Why would you want to extract just the diagonal from a matrix?

### Preview Examples

**Create identity matrix:**
```python
np.eye(3)
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]
```

**Create diagonal matrix:**
```python
np.diag([2, 5, 3])
# [[2, 0, 0],
#  [0, 5, 0],
#  [0, 0, 3]]
```

**Extract diagonal:**
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
np.diag(matrix)  # [1, 5, 9]
```

**Scaling transformation:**
```python
S = np.diag([2, 3])  # Scale x by 2, y by 3
point = [10, 20]
S @ point  # [20, 60]
```

### Practical Applications

**Data Science:**
- Covariance matrix diagonal = variances
- Regularization: add λI to prevent overfitting
- Feature scaling with diagonal matrices

**Linear Algebra:**
- Identity for solving Ax = b
- Diagonal matrices for eigenvalue problems
- Fast matrix operations

**Computer Graphics:**
- Scaling objects: scale(sx, sy, sz)
- Projections onto axes
- Coordinate transformations

**Machine Learning:**
- Ridge regression: (X^T X + λI)^-1 X^T y
- Batch normalization
- Gradient descent with learning rate matrix

### Important Distinctions

**eye() vs identity():**
- `eye()`: More flexible (rectangular, offset)
- `identity()`: Simpler (square only)

**diag() dual behavior:**
- Input 1D array → Create diagonal matrix
- Input 2D matrix → Extract diagonal

**Diagonal vs Identity:**
- Identity: Special case where all diagonal values = 1
- Diagonal: Any values on diagonal

### Resources

If you want to read ahead:
- NumPy Linear Algebra: https://numpy.org/doc/stable/reference/routines.linalg.html
- Identity matrix explanation: https://en.wikipedia.org/wiki/Identity_matrix
- Diagonal matrix properties: https://en.wikipedia.org/wiki/Diagonal_matrix

### Coming Up Next

After mastering identity and diagonal matrices, you've completed the first 5 NumPy fundamentals! You'll continue learning:
- Array indexing and slicing
- Array reshaping and manipulation
- Mathematical operations on arrays
- Broadcasting and vectorization

These special matrices are building blocks for advanced numerical computing - you'll use them constantly in data science and scientific computing!
