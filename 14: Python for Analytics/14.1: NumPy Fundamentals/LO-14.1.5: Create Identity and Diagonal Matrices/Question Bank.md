## Question Bank: Create Identity and Diagonal Matrices

### Q1: Create Identity Matrix (3 minutes, Low Difficulty)

**Problem:**
Create a 5×5 identity matrix using `np.eye()`. Print the matrix and its data type.

**Expected Output:**
```
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
Data type: float64
```

---

### Q2: Create Diagonal Matrix (3 minutes, Low Difficulty)

**Problem:**
Create a diagonal matrix from the array `[5, 10, 15, 20]` using `np.diag()`. Print the resulting matrix.

**Expected Output:**
```
[[ 5  0  0  0]
 [ 0 10  0  0]
 [ 0  0 15  0]
 [ 0  0  0 20]]
```

---

### Q3: Extract Diagonals from Matrix (5 minutes, Medium Difficulty)

**Problem:**
Given the matrix:
```python
matrix = np.array([[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120],
                   [130, 140, 150, 160]])
```

Extract and print:
1. The main diagonal
2. The diagonal above the main diagonal (k=1)
3. The diagonal below the main diagonal (k=-1)

**Expected Output:**
```
Main diagonal: [ 10  60 110 160]
Upper diagonal: [ 20  70 120]
Lower diagonal: [ 50 100 150]
```

---

### Q4: Verify Identity Property (5 minutes, Medium Difficulty)

**Problem:**
Create a 3×3 matrix with any values. Then:
1. Create a 3×3 identity matrix
2. Multiply your matrix by the identity matrix
3. Verify that the result equals the original matrix using `np.array_equal()`
4. Print a confirmation message

**Expected Output:**
```
Original matrix:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Result after multiplying by identity:
[[1. 2. 3.]
 [4. 5. 6.]
 [7. 8. 9.]]

Matrices are equal: True
```

---

### Q5: Create Scaling Matrix (5 minutes, Medium Difficulty)

**Problem:**
You need to scale a 3D point by different factors along each axis:
- X-axis: scale by 2
- Y-axis: scale by 3
- Z-axis: scale by 4

1. Create a diagonal scaling matrix using these factors
2. Create a point at position [10, 20, 30]
3. Multiply the scaling matrix by the point to get the scaled coordinates
4. Print both the scaling matrix and the scaled point

**Expected Output:**
```
Scaling matrix:
[[2 0 0]
 [0 3 0]
 [0 0 4]]

Original point: [10 20 30]
Scaled point: [ 20  60 120]
```
