## Question Bank: Apply Broadcasting Rules

### Q1: Basic Broadcasting Operations (3 minutes, Low Difficulty)

**Problem:**
Create a 2D array:
```python
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])
```
1. Add 5 to all elements using broadcasting
2. Multiply all elements by 3
3. Subtract 15 from all elements
4. Divide all elements by 10

**Expected Output:**
```
Original:
[[10 20 30]
 [40 50 60]
 [70 80 90]]
After +5:
[[15 25 35]
 [45 55 65]
 [75 85 95]]
After *3:
[[ 30  60  90]
 [120 150 180]
 [210 240 270]]
After -15:
[[-5   5  15]
 [25  35  45]
 [55  65  75]]
After /10:
[[1. 2. 3.]
 [4. 5. 6.]
 [7. 8. 9.]]
```

---

### Q2: Broadcasting with 1D Arrays (3 minutes, Low Difficulty)

**Problem:**
Create arrays:
```python
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
row_vec = np.array([10, 20, 30, 40])
```
1. Add row_vec to each row of matrix
2. Multiply matrix by row_vec
3. Create a column vector `col_vec = np.array([[100], [200], [300]])`
4. Add col_vec to each column of matrix

**Expected Output:**
```
Matrix:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
Row vector: [10 20 30 40]

After adding row_vec:
[[11 22 33 44]
 [15 26 37 48]
 [19 30 41 52]]

After multiplying by row_vec:
[[ 10  40  90 160]
 [ 50 120 210 320]
 [ 90 200 330 480]]

Column vector:
[[100]
 [200]
 [300]]

After adding col_vec:
[[101 102 103 104]
 [205 206 207 208]
 [309 310 311 312]]
```

---

### Q3: Normalize Data Using Broadcasting (5 minutes, Medium Difficulty)

**Problem:**
You have student scores:
```python
scores = np.array([[85, 90, 78],
                   [92, 88, 95],
                   [76, 85, 80],
                   [88, 92, 87]])
```
1. Calculate mean for each subject (column-wise mean)
2. Calculate standard deviation for each subject
3. Normalize each subject: (scores - mean) / std
4. Calculate mean for each student (row-wise mean)
5. Center each student's scores by subtracting their mean

**Expected Output:**
```
Scores:
[[85 90 78]
 [92 88 95]
 [76 85 80]
 [88 92 87]]

Subject means: [85.25 88.75 85.  ]
Subject std: [6.24 2.59 6.68]

Normalized scores (Z-score):
[[-0.04  0.48 -1.05]
 [ 1.08 -0.29  1.50]
 [-1.48 -1.45 -0.75]
 [ 0.44  1.26  0.30]]

Student means:
[[84.33]
 [91.67]
 [80.33]
 [89.  ]]

Centered by student:
[[ 0.67  5.67 -6.33]
 [ 0.33 -3.67  3.33]
 [-4.33  4.67 -0.33]
 [-1.   3.  -2.  ]]
```

---

### Q4: Temperature Conversion Matrix (5 minutes, Medium Difficulty)

**Problem:**
You have temperatures for 5 cities over 4 days (in Celsius):
```python
celsius = np.array([[22, 25, 23, 24],
                    [18, 20, 19, 21],
                    [30, 32, 31, 29],
                    [15, 17, 16, 18],
                    [28, 27, 29, 30]])
```
1. Convert all temperatures to Fahrenheit: F = C * 9/5 + 32
2. Find which temperatures are above 25°C (boolean array)
3. Calculate the average temperature for each city
4. Find the difference of each day's temp from city average
5. Calculate the overall mean temperature
6. Find how many readings are above the overall mean

**Expected Output:**
```
Celsius temperatures:
[[22 25 23 24]
 [18 20 19 21]
 [30 32 31 29]
 [15 17 16 18]
 [28 27 29 30]]

Fahrenheit:
[[71.6 77.  73.4 75.2]
 [64.4 68.  66.2 69.8]
 [86.  89.6 87.8 84.2]
 [59.  62.6 60.8 64.4]
 [82.4 80.6 84.2 86. ]]

Above 25°C:
[[False False False False]
 [False False False False]
 [ True  True  True  True]
 [False False False False]
 [ True  True  True  True]]

City averages: [23.5  19.5  30.5  16.5  28.5 ]

Difference from city avg:
[[-1.5   1.5  -0.5   0.5 ]
 [-1.5   0.5  -0.5   1.5 ]
 [-0.5   1.5   0.5  -1.5 ]
 [-1.5   0.5  -0.5   1.5 ]
 [-0.5  -1.5   0.5   1.5 ]]

Overall mean: 23.7°C
Readings above overall mean: 10
```

---

### Q5: Price Discount System (5 minutes, Medium Difficulty)

**Problem:**
You have product prices and category-specific discount rates:
```python
prices = np.array([[100, 200, 150],
                   [250, 180, 220],
                   [90, 160, 130],
                   [300, 270, 240]])

# Discount rates for each category (columns)
discounts = np.array([0.10, 0.15, 0.20])  # 10%, 15%, 20%

# Additional bulk discount for expensive items (rows)
bulk_discount = np.array([[0.05],
                          [0.10],
                          [0.00],
                          [0.15]])  # 5%, 10%, 0%, 15%
```
1. Apply category discounts to get discounted prices
2. Apply additional bulk discounts to already discounted prices
3. Calculate total savings per product
4. Find which products cost less than $150 after all discounts
5. Calculate average final price per category

**Expected Output:**
```
Original prices:
[[100 200 150]
 [250 180 220]
 [ 90 160 130]
 [300 270 240]]

After category discount:
[[ 90. 170. 120.]
 [225. 153. 176.]
 [ 81. 136. 104.]
 [270. 229.5 192.]]

After bulk discount:
[[ 85.5  161.5  114.  ]
 [202.5  137.7  158.4 ]
 [ 81.   136.   104.  ]
 [229.5  195.07 163.2 ]]

Total savings per product:
[[ 14.5   38.5   36.  ]
 [ 47.5   42.3   61.6 ]
 [  9.    24.    26.  ]
 [ 70.5   74.92  76.8 ]]

Products under $150:
[[ True False  True]
 [False  True False]
 [ True  True  True]
 [False False False]]

Average final price per category: [149.62 157.57 134.9 ]
```
