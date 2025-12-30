## Question Bank: Use Universal Functions (ufuncs)

### Q1: Basic Mathematical Ufuncs (3 minutes, Low Difficulty)

**Problem:**
Create an array `arr = np.array([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])`.
1. Calculate the square root of all elements
2. Calculate the square of all elements
3. Calculate the cube (power of 3) of all elements
4. Find the natural logarithm (log base e) of all elements
5. Round the logarithm values to 2 decimal places

**Expected Output:**
```
Original: [  1   4   9  16  25  36  49  64  81 100]
Square root: [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
Square: [    1    16    81   256   625  1296  2401  4096  6561 10000]
Cube: [      1      64     729    4096   15625   46656  117649  262144  531441 1000000]
Natural log: [0.   1.39 2.20 2.77 3.22 3.58 3.89 4.16 4.39 4.61]
Log rounded: [0.   1.39 2.2  2.77 3.22 3.58 3.89 4.16 4.39 4.61]
```

---

### Q2: Trigonometric Functions (3 minutes, Low Difficulty)

**Problem:**
Create an array with angles in degrees: `degrees = np.array([0, 30, 45, 60, 90, 180, 270, 360])`.
1. Convert degrees to radians
2. Calculate sine of all angles (use radians)
3. Calculate cosine of all angles (use radians)
4. Calculate tangent of angles 0°, 30°, 45°, 60° only
5. Round all results to 2 decimal places

**Expected Output:**
```
Degrees: [  0  30  45  60  90 180 270 360]
Radians: [0.   0.52 0.79 1.05 1.57 3.14 4.71 6.28]
Sine: [ 0.    0.5   0.71  0.87  1.    0.   -1.    0.  ]
Cosine: [ 1.    0.87  0.71  0.5   0.   -1.    0.    1.  ]
Tangent (0-60°): [0.   0.58 1.   1.73]
```

---

### Q3: Rounding and Comparison Functions (5 minutes, Medium Difficulty)

**Problem:**
Create two arrays:
```python
prices = np.array([23.456, 45.678, 12.345, 67.890, 34.567])
discounts = np.array([5.123, 10.789, 3.456, 15.234, 8.901])
```
1. Round prices to 2 decimal places
2. Use floor on discounts
3. Use ceiling on discounts
4. Calculate final prices: prices - discounts
5. Find element-wise maximum between prices and a fixed value of 30
6. Find element-wise minimum between final_prices and 50
7. Calculate absolute difference between prices and 40

**Expected Output:**
```
Prices: [23.456 45.678 12.345 67.89  34.567]
Discounts: [ 5.123 10.789  3.456 15.234  8.901]
Rounded prices: [23.46 45.68 12.35 67.89 34.57]
Floor discounts: [ 5. 10.  3. 15.  8.]
Ceiling discounts: [ 6. 11.  4. 16.  9.]
Final prices: [18.33 34.89  8.89 52.66 25.67]
Max with 30: [30.   45.68 30.   67.89 34.57]
Min final with 50: [18.33 34.89  8.89 50.   25.67]
Abs diff from 40: [16.54  5.68 27.66 27.89  5.43]
```

---

### Q4: Statistical Analysis with Ufuncs (5 minutes, Medium Difficulty)

**Problem:**
You have test scores for 5 students across 4 subjects:
```python
scores = np.array([[85, 90, 78, 92],
                   [88, 76, 95, 82],
                   [92, 88, 84, 89],
                   [78, 85, 88, 91],
                   [95, 89, 92, 87]])
```
1. Calculate the mean score for each student (across subjects)
2. Calculate the mean score for each subject (across students)
3. Find the maximum score for each student
4. Find the minimum score for each subject
5. Calculate the standard deviation for each student
6. Find which students have mean >= 87
7. Calculate the overall mean of all scores

**Expected Output:**
```
Scores:
[[85 90 78 92]
 [88 76 95 82]
 [92 88 84 89]
 [78 85 88 91]
 [95 89 92 87]]
Student means: [86.25 85.25 88.25 85.5  90.75]
Subject means: [87.6 85.6 87.4 88.2]
Student max: [92 95 92 91 95]
Subject min: [78 76 78 82]
Student std: [5.74 7.54 3.20 5.45 3.30]
Students with mean >= 87: [False False  True False  True]
Overall mean: 87.2
```

---

### Q5: Compound Interest Calculator (5 minutes, Medium Difficulty)

**Problem:**
You have investment data:
```python
principals = np.array([5000, 10000, 15000, 20000, 25000])  # Initial amounts
rate = 0.06  # 6% annual interest
years = np.array([5, 10, 15, 20, 25])  # Investment periods
```
1. Calculate final amounts using compound interest: A = P * (1 + r)^t
2. Calculate total interest earned for each investment
3. Find which investments will exceed $50,000
4. Calculate the percentage gain for each investment
5. Find the mean final amount across all investments
6. Calculate the square root of final amounts (hypothetical metric)
7. Round all final amounts to 2 decimal places

**Expected Output:**
```
Principals: [ 5000 10000 15000 20000 25000]
Years: [ 5 10 15 20 25]
Final amounts: [  6691.13  17908.48  35949.64  64142.71 107297.13]
Interest earned: [  1691.13   7908.48  20949.64  44142.71  82297.13]
Exceeds $50,000: [False False False  True  True]
Percentage gain: [ 33.82  79.08 139.66 220.71 329.19]
Mean final amount: $58397.82
Square root of finals: [ 81.80 133.82 189.60 253.26 327.56]
Final rounded: [  6691.13  17908.48  35949.64  64142.71 107297.13]
```
