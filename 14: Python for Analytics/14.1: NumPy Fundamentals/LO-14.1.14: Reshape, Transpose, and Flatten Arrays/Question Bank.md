## Question Bank: Reshape, Transpose, and Flatten Arrays

### Q1: Basic Reshaping (3 minutes, Low Difficulty)

**Problem:**
Create a 1D array with values from 1 to 12:
```python
arr = np.arange(1, 13)
```
1. Print the original shape
2. Reshape it to (3, 4)
3. Reshape it to (4, 3)
4. Reshape it to (2, 6)
5. Reshape it to (2, 2, 3) - a 3D array

**Expected Output:**
```
Original: [ 1  2  3  4  5  6  7  8  9 10 11 12]
Shape: (12,)

Reshaped (3, 4):
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

Reshaped (4, 3):
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

Reshaped (2, 6):
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]]

Reshaped (2, 2, 3):
[[[ 1  2  3]
  [ 4  5  6]]
 [[ 7  8  9]
  [10 11 12]]]
```

---

### Q2: Transpose Operations (3 minutes, Low Difficulty)

**Problem:**
Create a matrix:
```python
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
```
1. Print original matrix and its shape
2. Transpose the matrix and print result
3. Print transposed shape
4. Transpose it again (should get original back)
5. Create a square matrix and verify transpose property: (A.T).T == A

**Expected Output:**
```
Original (3, 4):
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

Transposed (4, 3):
[[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]

Double transposed (back to 3, 4):
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

Square matrix A:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

(A.T).T equals A: True
```

---

### Q3: Flatten vs Ravel (5 minutes, Medium Difficulty)

**Problem:**
Create a 2D array:
```python
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
```
1. Use `flatten()` to create a 1D array, modify first element, check if original changed
2. Use `ravel()` to create a 1D array, modify first element, check if original changed
3. Use `reshape(-1)` to flatten, modify first element, check if original changed
4. Compare all three methods and explain the difference

**Expected Output:**
```
Original:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Flattened (copy): [1 2 3 4 5 6 7 8 9]
After modifying flattened[0] to 999:
Original unchanged:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Raveled (view): [1 2 3 4 5 6 7 8 9]
After modifying raveled[0] to 999:
Original CHANGED:
[[999   2   3]
 [  4   5   6]
 [  7   8   9]]

Reshape(-1) (view): [999 2 3 4 5 6 7 8 9]
After modifying reshaped[1] to 888:
Original CHANGED:
[[999 888   3]
 [  4   5   6]
 [  7   8   9]]

Summary:
- flatten() creates a COPY (safe, won't modify original)
- ravel() creates a VIEW (modifies original)
- reshape(-1) creates a VIEW (modifies original)
```

---

### Q4: Reshape with -1 Parameter (5 minutes, Medium Difficulty)

**Problem:**
Create an array with 24 elements:
```python
arr = np.arange(1, 25)
```
1. Reshape to (-1, 6) and print shape
2. Reshape to (4, -1) and print shape
3. Reshape to (2, 3, -1) and print shape
4. Reshape to (-1, 2, 3) and print shape
5. Try reshape to (-1, -1, 3) and explain what happens

**Expected Output:**
```
Original: [ 1  2  3  4 ... 22 23 24]  Shape: (24,)

Reshape (-1, 6):
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]
 [13 14 15 16 17 18]
 [19 20 21 22 23 24]]
Shape: (4, 6)

Reshape (4, -1):
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]
 [13 14 15 16 17 18]
 [19 20 21 22 23 24]]
Shape: (4, 6)

Reshape (2, 3, -1):
[[[ 1  2  3  4]
  [ 5  6  7  8]
  [ 9 10 11 12]]
 [[13 14 15 16]
  [17 18 19 20]
  [21 22 23 24]]]
Shape: (2, 3, 4)

Reshape (-1, 2, 3):
[[[ 1  2  3]
  [ 4  5  6]]
 [[ 7  8  9]
  [10 11 12]]
 [[13 14 15]
  [16 17 18]]
 [[19 20 21]
  [22 23 24]]]
Shape: (4, 2, 3)

Reshape (-1, -1, 3):
Error! Can only specify one unknown dimension (-1)
```

---

### Q5: Image Data Manipulation (5 minutes, Medium Difficulty)

**Problem:**
Simulate a batch of grayscale images:
```python
# 10 images, each 8x8 pixels
images = np.arange(640).reshape(10, 8, 8)
```
1. Print the shape of the images
2. Extract the first image and print its shape
3. Flatten each image to 1D (shape should be 10, 64)
4. Transpose each image (swap height and width)
5. Convert to a single 1D array (all pixels from all images)
6. Reshape back to original (10, 8, 8)

**Expected Output:**
```
Original batch shape: (10, 8, 8)
Total pixels: 640

First image shape: (8, 8)
First image:
[[ 0  1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14 15]
 [16 17 18 19 20 21 22 23]
 [24 25 26 27 28 29 30 31]
 [32 33 34 35 36 37 38 39]
 [40 41 42 43 44 45 46 47]
 [48 49 50 51 52 53 54 55]
 [56 57 58 59 60 61 62 63]]

Flattened images shape: (10, 64)
First flattened image (first 10 elements): [ 0  1  2  3  4  5  6  7  8  9]

Transposed images shape: (10, 8, 8)

Fully flattened shape: (640,)
First 10 elements: [0 1 2 3 4 5 6 7 8 9]

Reshaped back to original: (10, 8, 8)
Shapes match: True
```
