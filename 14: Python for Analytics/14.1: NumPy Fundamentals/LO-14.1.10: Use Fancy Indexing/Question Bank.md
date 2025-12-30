## Question Bank: Use Fancy Indexing

### Q1: Select Specific Elements (3 minutes, Low Difficulty)

**Problem:**
Create an array `arr = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])`.
1. Select elements at indices 0, 3, and 7
2. Select elements at indices 2, 5, 8, and 9
3. Select the last, first, and middle (index 5) elements
4. Select elements at indices 1, 1, 4, 4 (with repetition)

**Expected Output:**
```
Indices 0, 3, 7: [ 5 20 40]
Indices 2, 5, 8, 9: [15 30 45 50]
Last, first, middle: [50  5 30]
Repeated indices: [10 10 25 25]
```

---

### Q2: Reorder Array Elements (3 minutes, Low Difficulty)

**Problem:**
Create an array `arr = np.array([100, 200, 300, 400, 500])`.
1. Reverse the array using fancy indexing
2. Rearrange to [300, 100, 500, 200, 400]
3. Create a new array with elements in order [4, 2, 0, 1, 3] (using indices)
4. Duplicate the first element 5 times

**Expected Output:**
```
Reversed: [500 400 300 200 100]
Custom order: [300 100 500 200 400]
Index order [4,2,0,1,3]: [500 300 100 200 400]
First element 5 times: [100 100 100 100 100]
```

---

### Q3: Fancy Indexing with 2D Arrays (5 minutes, Medium Difficulty)

**Problem:**
Create a 2D array:
```python
matrix = np.array([[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120],
                   [130, 140, 150, 160]])
```
1. Select rows 0 and 3
2. Select rows 1, 2, and 3 in that order
3. Select specific elements: (0,0), (1,3), (3,2)
4. Select rows 0 and 2, columns 1 and 3
5. Select row 1 with all columns, then row 3 with columns 0 and 2

**Expected Output:**
```
Rows 0 and 3:
[[ 10  20  30  40]
 [130 140 150 160]]

Rows 1, 2, 3:
[[ 50  60  70  80]
 [ 90 100 110 120]
 [130 140 150 160]]

Specific elements: [ 10  80 150]

Rows 0,2 cols 1,3:
[[ 20  40]
 [100 120]]

Row 1 all, Row 3 cols 0,2:
Row 1: [50 60 70 80]
Row 3 selected: [130 150]
```

---

### Q4: Modify Using Fancy Indexing (5 minutes, Medium Difficulty)

**Problem:**
Create an array `data = np.array([10, 20, 30, 40, 50, 60, 70, 80])`.
1. Print original array
2. Set elements at indices 1, 4, and 6 to 999
3. Print modified array
4. Create a new array and set elements at indices 0, 2, 4, 6 to values [100, 200, 300, 400]
5. Print final array
6. Triple the values at indices 3, 5, and 7

**Expected Output:**
```
Original: [10 20 30 40 50 60 70 80]
After setting to 999: [ 10 999  30  40 999  60 999  80]
Reset data: [10 20 30 40 50 60 70 80]
After custom values: [100  20 200  40 300  60 400  80]
After tripling: [100  20 200 120 300 180 400 240]
```

---

### Q5: Extract Top Performers (5 minutes, Medium Difficulty)

**Problem:**
Given sales data and employee names:
```python
sales = np.array([1200, 1800, 950, 2200, 1500, 1100, 2000, 1300])
employees = np.array(['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace', 'Henry'])
```
1. Find indices of sales sorted in descending order
2. Print the top 3 indices
3. Extract sales amounts for top 3 performers
4. Extract names of top 3 performers
5. Extract bottom 2 performers (lowest sales) and their sales

**Expected Output:**
```
Sorted indices (desc): [3 6 1 4 7 0 5 2]
Top 3 indices: [3 6 1]
Top 3 sales: [2200 2000 1800]
Top 3 employees: ['David' 'Grace' 'Bob']
Bottom 2 employees: ['Carol' 'Frank']
Bottom 2 sales: [950 1100]
```
