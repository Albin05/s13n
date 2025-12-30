## Editorials: Reshape, Transpose, and Flatten Arrays

### Q1 Solution: Basic Reshaping

```python
import numpy as np

# Create array
arr = np.arange(1, 13)
print(f"Original: {arr}")
print(f"Shape: {arr.shape}")

# Reshape to (3, 4)
reshaped = arr.reshape(3, 4)
print("\nReshaped (3, 4):")
print(reshaped)

# Reshape to (4, 3)
reshaped = arr.reshape(4, 3)
print("\nReshaped (4, 3):")
print(reshaped)

# Reshape to (2, 6)
reshaped = arr.reshape(2, 6)
print("\nReshaped (2, 6):")
print(reshaped)

# Reshape to (2, 2, 3)
reshaped = arr.reshape(2, 2, 3)
print("\nReshaped (2, 2, 3):")
print(reshaped)
```

**Explanation:**
- `reshape()` changes array shape without modifying data
- Total elements must match: 12 = 3×4 = 4×3 = 2×6 = 2×2×3
- Elements filled in row-major (C) order by default
- Can reshape to any number of dimensions

---

### Q2 Solution: Transpose Operations

```python
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print(f"Original {matrix.shape}:")
print(matrix)

# Transpose
transposed = matrix.T
print(f"\nTransposed {transposed.shape}:")
print(transposed)

# Double transpose
double_trans = transposed.T
print(f"\nDouble transposed (back to {double_trans.shape}):")
print(double_trans)

# Square matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("\nSquare matrix A:")
print(A)

# Verify (A.T).T == A
result = np.array_equal((A.T).T, A)
print(f"\n(A.T).T equals A: {result}")
```

**Explanation:**
- `.T` swaps axes: rows become columns, columns become rows
- Transposing twice returns to original
- Works on any 2D array (doesn't need to be square)
- Transpose returns a view (shares memory)
- `np.array_equal()` compares arrays element-wise

---

### Q3 Solution: Flatten vs Ravel

```python
import numpy as np

# Create array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Original:")
print(arr)

# Test flatten() - creates copy
flat = arr.flatten()
print(f"\nFlattened (copy): {flat}")
flat[0] = 999
print("After modifying flattened[0] to 999:")
print("Original unchanged:")
print(arr)

# Reset
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Test ravel() - creates view
raveled = arr.ravel()
print(f"\nRaveled (view): {raveled}")
raveled[0] = 999
print("After modifying raveled[0] to 999:")
print("Original CHANGED:")
print(arr)

# Test reshape(-1) - creates view
reshaped = arr.reshape(-1)
print(f"\nReshape(-1) (view): {reshaped}")
reshaped[1] = 888
print("After modifying reshaped[1] to 888:")
print("Original CHANGED:")
print(arr)

print("\nSummary:")
print("- flatten() creates a COPY (safe, won't modify original)")
print("- ravel() creates a VIEW (modifies original)")
print("- reshape(-1) creates a VIEW (modifies original)")
```

**Explanation:**
- `flatten()` always creates independent copy
- `ravel()` returns view when possible (modifying affects original)
- `reshape(-1)` also returns view
- Use `flatten()` when you need independent copy
- Use `ravel()` or `reshape(-1)` for efficiency

---

### Q4 Solution: Reshape with -1 Parameter

```python
import numpy as np

# Create array
arr = np.arange(1, 25)
print(f"Original: {arr}  Shape: {arr.shape}")

# Reshape (-1, 6) - NumPy calculates first dimension
reshaped = arr.reshape(-1, 6)
print("\nReshape (-1, 6):")
print(reshaped)
print(f"Shape: {reshaped.shape}")

# Reshape (4, -1) - NumPy calculates second dimension
reshaped = arr.reshape(4, -1)
print("\nReshape (4, -1):")
print(reshaped)
print(f"Shape: {reshaped.shape}")

# Reshape (2, 3, -1)
reshaped = arr.reshape(2, 3, -1)
print("\nReshape (2, 3, -1):")
print(reshaped)
print(f"Shape: {reshaped.shape}")

# Reshape (-1, 2, 3)
reshaped = arr.reshape(-1, 2, 3)
print("\nReshape (-1, 2, 3):")
print(reshaped)
print(f"Shape: {reshaped.shape}")

# Try (-1, -1, 3) - will error
try:
    reshaped = arr.reshape(-1, -1, 3)
except ValueError as e:
    print("\nReshape (-1, -1, 3):")
    print(f"Error! Can only specify one unknown dimension (-1)")
```

**Explanation:**
- `-1` tells NumPy to calculate that dimension automatically
- Total elements must still match
- Can only use `-1` for one dimension at a time
- `-1` makes code more flexible and readable
- NumPy calculates: dimension = total_elements / (other dimensions)

---

### Q5 Solution: Image Data Manipulation

```python
import numpy as np

# Create image batch
images = np.arange(640).reshape(10, 8, 8)
print(f"Original batch shape: {images.shape}")
print(f"Total pixels: {images.size}")

# First image
first_image = images[0]
print(f"\nFirst image shape: {first_image.shape}")
print("First image:")
print(first_image)

# Flatten each image
flattened = images.reshape(10, -1)
print(f"\nFlattened images shape: {flattened.shape}")
print(f"First flattened image (first 10 elements): {flattened[0, :10]}")

# Transpose each image (swap last two axes)
transposed = images.transpose(0, 2, 1)
print(f"\nTransposed images shape: {transposed.shape}")

# Fully flatten
fully_flat = images.reshape(-1)
print(f"\nFully flattened shape: {fully_flat.shape}")
print(f"First 10 elements: {fully_flat[:10]}")

# Reshape back
back = fully_flat.reshape(10, 8, 8)
print(f"\nReshaped back to original: {back.shape}")
print(f"Shapes match: {np.array_equal(back, images)}")
```

**Explanation:**
- Batch of images has shape (num_images, height, width)
- `reshape(10, -1)` flattens each image: (10, 8, 8) → (10, 64)
- `transpose(0, 2, 1)` swaps height and width dimensions
- `reshape(-1)` fully flattens to 1D
- Can reshape back to original if total elements match
- `np.array_equal()` verifies arrays are identical

**Key Concepts Covered:**
1. Basic reshaping with different dimensions
2. Transpose operations and properties
3. Difference between flatten() (copy) and ravel()/reshape() (view)
4. Using -1 for automatic dimension calculation
5. Practical image data manipulation with multiple operations
