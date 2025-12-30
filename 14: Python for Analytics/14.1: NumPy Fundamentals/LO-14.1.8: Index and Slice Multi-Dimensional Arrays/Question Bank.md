## Question Bank: Index and Slice Multi-Dimensional Arrays

### Q1: Access 2D Array Elements (3 minutes, Low Difficulty)

**Problem:**
Create a 2D array:
```python
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
```
1. Access and print the element at row 1, column 2
2. Access and print the element at the last row, first column using negative indexing
3. Modify the element at row 0, column 1 to 999
4. Print the entire matrix

**Expected Output:**
```
Element at (1, 2): 30
Element at last row, first column: 35
Modified matrix:
[[  5 999  15]
 [ 20  25  30]
 [ 35  40  45]]
```

---

### Q2: Extract Rows and Columns (3 minutes, Low Difficulty)

**Problem:**
Create a 2D array:
```python
data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
```
1. Extract and print the second row (index 1)
2. Extract and print the third column (index 2)
3. Extract and print the last row using negative indexing
4. Extract and print the first column

**Expected Output:**
```
Second row: [5 6 7 8]
Third column: [ 3  7 11]
Last row: [ 9 10 11 12]
First column: [1 5 9]
```

---

### Q3: Slice Sub-Matrices (5 minutes, Medium Difficulty)

**Problem:**
Create a 4x5 matrix:
```python
matrix = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]])
```
1. Extract the first 2 rows and first 3 columns
2. Extract the last 2 rows and last 2 columns
3. Extract all middle elements (exclude first and last row/column)
4. Extract every other row
5. Extract every other column

**Expected Output:**
```
First 2 rows, first 3 cols:
[[1 2 3]
 [6 7 8]]

Last 2 rows, last 2 cols:
[[14 15]
 [19 20]]

Middle elements:
[[ 7  8  9]
 [12 13 14]]

Every other row:
[[ 1  2  3  4  5]
 [11 12 13 14 15]]

Every other column:
[[ 1  3  5]
 [ 6  8 10]
 [11 13 15]
 [16 18 20]]
```

---

### Q4: Manipulate 3D Arrays (5 minutes, Medium Difficulty)

**Problem:**
Create a 3D array (2 layers, 3 rows, 3 columns):
```python
arr_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                   [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
```
1. Print the shape of the array
2. Extract and print the first layer (layer 0)
3. Extract and print the second row from the second layer
4. Extract and print the third column from the first layer
5. Access and print the element at layer 1, row 2, column 1

**Expected Output:**
```
Shape: (2, 3, 3)
First layer:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
Second row from second layer: [13 14 15]
Third column from first layer: [3 6 9]
Element at (1, 2, 1): 17
```

---

### Q5: Analyze Student Grades (5 minutes, Medium Difficulty)

**Problem:**
Given a 2D array where rows are students and columns are test scores:
```python
grades = np.array([[85, 92, 78, 90],
                   [88, 76, 95, 82],
                   [92, 88, 84, 89],
                   [78, 85, 88, 91],
                   [95, 89, 92, 87]])
```
1. Extract and print all scores for student 3 (index 2)
2. Extract and print all scores for test 2 (index 1)
3. Extract scores for the first 3 students on the last 2 tests
4. Calculate and print the average score for student 1 (index 0)
5. Calculate and print the average score for test 4 (index 3)

**Expected Output:**
```
Student 3 scores: [92 88 84 89]
Test 2 scores: [92 76 88 85 89]
First 3 students, last 2 tests:
[[78 90]
 [95 82]
 [84 89]]
Student 1 average: 86.25
Test 4 average: 87.8
```
