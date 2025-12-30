## Question Bank: Stack, Split, and Concatenate Arrays

### Q1: Basic Array Concatenation (3 minutes, Low Difficulty)

**Problem:**
Create three 1D arrays and concatenate them. Then create two 2D arrays and concatenate them both vertically and horizontally.

**Input:**
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
```

**Expected Output:**
```
1D concatenation: [1 2 3 4 5 6 7 8 9]
Vertical concat:
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
Horizontal concat:
[[1 2 5 6]
 [3 4 7 8]]
```

**Category:** Implementation  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q2: Array Stacking Operations (3 minutes, Low Difficulty)

**Problem:**
Create three 1D arrays representing daily temperatures for three cities. Stack them vertically and horizontally, then use np.stack() with different axis values.

**Input:**
```python
city1 = np.array([22, 25, 23])
city2 = np.array([18, 20, 19])
city3 = np.array([30, 32, 31])
```

**Expected Output:**
```
vstack (cities as rows):
[[22 25 23]
 [18 20 19]
 [30 32 31]]

hstack (all temps):
[22 25 23 18 20 19 30 32 31]

stack axis=0:
[[22 25 23]
 [18 20 19]
 [30 32 31]]

stack axis=1:
[[22 18 30]
 [25 20 32]
 [23 19 31]]
```

**Category:** Implementation  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q3: Array Splitting Operations (5 minutes, Medium Difficulty)

**Problem:**
Create an array of 15 numbers and split it into three equal parts. Then create a 6x4 matrix and split it both horizontally and vertically. Finally, split an array of 10 numbers into 3 unequal parts.

**Input:**
```python
arr = np.arange(1, 16)
matrix = np.arange(1, 25).reshape(6, 4)
uneven = np.arange(1, 11)
```

**Expected Output:**
```
Split into 3:
Part 1: [1 2 3 4 5]
Part 2: [ 6  7  8  9 10]
Part 3: [11 12 13 14 15]

Vertical split (3 parts):
[[ 1  2  3  4]
 [ 5  6  7  8]]
[[ 9 10 11 12]
 [13 14 15 16]]
[[17 18 19 20]
 [21 22 23 24]]

Horizontal split (2 parts):
[[ 1  2]
 [ 5  6]
 [ 9 10]
 [13 14]
 [17 18]
 [21 22]]

Unequal split:
[1 2 3 4]
[5 6 7]
[ 8  9 10]
```

**Category:** Implementation  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q4: Student Grades Analysis (5 minutes, Medium Difficulty)

**Problem:**
You have exam scores for three subjects from four students (each student's scores in a separate array). Combine all scores into a single 2D array, then:
1. Calculate average per subject (column means)
2. Calculate average per student (row means)
3. Split the combined array back into individual student arrays
4. Find the highest scoring student overall

**Input:**
```python
student1 = np.array([85, 90, 78])  # Math, Science, English
student2 = np.array([92, 88, 95])
student3 = np.array([76, 85, 80])
student4 = np.array([88, 92, 87])
```

**Expected Output:**
```
All scores:
[[85 90 78]
 [92 88 95]
 [76 85 80]
 [88 92 87]]

Subject averages: [85.25 88.75 85.  ]
Student averages: [84.33 91.67 80.33 89.  ]

Individual student scores after split:
Student 1: [85 90 78]
Student 2: [92 88 95]
Student 3: [76 85 80]
Student 4: [88 92 87]

Highest scoring student: Student 2 with average 91.67
```

**Category:** Application  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q5: Time Series Data Pipeline (5 minutes, Medium Difficulty)

**Problem:**
You have hourly temperature data for 24 hours from three weather stations. Combine the data, then:
1. Split into 4 six-hour periods
2. Calculate mean temperature for each period and station
3. Identify the warmest period for each station
4. Concatenate morning (0-12h) and evening (12-24h) data separately

**Input:**
```python
np.random.seed(42)
station1 = np.random.randint(15, 30, 24)
station2 = np.random.randint(12, 28, 24)
station3 = np.random.randint(18, 32, 24)
```

**Expected Output:**
```
Combined data shape: (3, 24)

Period averages (4 periods × 3 stations):
[[21.   20.67 24.83]
 [22.5  18.83 26.  ]
 [21.67 21.33 25.67]
 [22.33 19.   24.17]]

Warmest period per station:
Station 1: Period 2
Station 2: Period 3
Station 3: Period 2

Morning data (0-12h) shape: (3, 12)
Evening data (12-24h) shape: (3, 12)
```

**Category:** Application  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Additional Practice Problems

**Challenge 1: Image Channel Separation**
Given an RGB image array of shape (height, width, 3), split it into separate R, G, B channels and then recombine them in BGR order.

**Challenge 2: Batch Data Augmentation**
Create 5 sample vectors, stack them into a batch, then split the batch into mini-batches of size 2.

**Challenge 3: Cross-Validation Folds**
Given a dataset of 100 samples, create 5 train-test splits for 5-fold cross-validation using array splitting.
