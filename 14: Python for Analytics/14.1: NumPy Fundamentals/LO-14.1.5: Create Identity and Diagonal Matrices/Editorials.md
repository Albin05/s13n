## Editorials: Create Identity and Diagonal Matrices

### Q1 Solution: Create Identity Matrix

```python
import numpy as np

# Create 5x5 identity matrix
I = np.eye(5)
print(I)
print(f"Data type: {I.dtype}")
```

**Explanation:**
- `np.eye(5)` creates a 5×5 square identity matrix
- Default dtype is float64
- Identity matrix has 1s on diagonal, 0s elsewhere

---

### Q2 Solution: Create Diagonal Matrix

```python
import numpy as np

# Create diagonal matrix
diag_values = [5, 10, 15, 20]
D = np.diag(diag_values)
print(D)
```

**Explanation:**
- `np.diag()` with a 1D array creates a diagonal matrix
- Values appear on the main diagonal
- All other positions are filled with 0s
- Resulting matrix is 4×4 (size matches input array length)

---

### Q3 Solution: Extract Diagonals from Matrix

```python
import numpy as np

# Given matrix
matrix = np.array([[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120],
                   [130, 140, 150, 160]])

# Extract diagonals
main_diag = np.diag(matrix)
upper_diag = np.diag(matrix, k=1)
lower_diag = np.diag(matrix, k=-1)

# Print results
print(f"Main diagonal: {main_diag}")
print(f"Upper diagonal: {upper_diag}")
print(f"Lower diagonal: {lower_diag}")
```

**Explanation:**
- `np.diag(matrix)` extracts the main diagonal (default k=0)
  - Elements: matrix[0,0], matrix[1,1], matrix[2,2], matrix[3,3]
  - Result: [10, 60, 110, 160]
- `np.diag(matrix, k=1)` extracts diagonal above main
  - Elements: matrix[0,1], matrix[1,2], matrix[2,3]
  - Result: [20, 70, 120]
- `np.diag(matrix, k=-1)` extracts diagonal below main
  - Elements: matrix[1,0], matrix[2,1], matrix[3,2]
  - Result: [50, 100, 150]

**Key insight:** Same function, different modes based on input type (array vs matrix).

---

### Q4 Solution: Verify Identity Property

```python
import numpy as np

# Create a 3x3 matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("Original matrix:")
print(A)

# Create identity matrix
I = np.eye(3)

# Multiply matrix by identity
result = A @ I  # or np.dot(A, I)

print("\nResult after multiplying by identity:")
print(result)

# Verify equality
are_equal = np.allclose(result, A)  # Use allclose for float comparison
print(f"\nMatrices are equal: {are_equal}")
```

**Explanation:**
- Identity matrix property: A × I = A
- `@` operator performs matrix multiplication
- `np.allclose()` is better than `np.array_equal()` for floating-point comparison
  - Handles small rounding errors
  - More robust for numerical operations
- This demonstrates the fundamental identity property

**Alternative verification:**
```python
are_equal = np.array_equal(result, A.astype(float))
```

---

### Q5 Solution: Create Scaling Matrix

```python
import numpy as np

# Create scaling factors
scale_factors = [2, 3, 4]
S = np.diag(scale_factors)

print("Scaling matrix:")
print(S)

# Create point
point = np.array([10, 20, 30])
print(f"\nOriginal point: {point}")

# Apply scaling
scaled_point = S @ point  # or np.dot(S, point)
print(f"Scaled point: {scaled_point}")
```

**Explanation:**
- Diagonal scaling matrix multiplies each coordinate by its scale factor
- Matrix multiplication: S @ point
  - Row 0: [2, 0, 0] · [10, 20, 30] = 2×10 = 20
  - Row 1: [0, 3, 0] · [10, 20, 30] = 3×20 = 60
  - Row 2: [0, 0, 4] · [10, 20, 30] = 4×30 = 120
- Result: [20, 60, 120]

**Why diagonal matrices are useful:**
- Fast computation (only multiply diagonal elements)
- Easy to understand (each dimension scaled independently)
- Common in computer graphics, physics, machine learning

**Key Concepts Covered:**
1. Creating identity matrices with eye()
2. Creating diagonal matrices from arrays
3. Extracting diagonals from matrices (different offsets)
4. Verifying identity matrix property
5. Practical application: scaling transformations
6. Understanding bidirectional nature of diag()
