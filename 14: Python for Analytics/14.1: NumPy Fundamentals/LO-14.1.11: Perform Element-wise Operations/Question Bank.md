## Question Bank: Perform Element-wise Operations

### Q1: Basic Arithmetic Operations (3 minutes, Low Difficulty)

**Problem:**
Create an array `arr = np.array([5, 10, 15, 20, 25])`.
1. Add 10 to all elements
2. Multiply all elements by 3
3. Divide all elements by 5
4. Calculate the square of all elements

**Expected Output:**
```
Original: [ 5 10 15 20 25]
After +10: [15 20 25 30 35]
After *3: [15 30 45 60 75]
After /5: [1. 2. 3. 4. 5.]
Squared: [  25  100  225  400  625]
```

---

### Q2: Array-to-Array Operations (3 minutes, Low Difficulty)

**Problem:**
Create two arrays:
```python
prices = np.array([100, 200, 150, 250, 300])
quantities = np.array([2, 1, 3, 2, 1])
```
1. Calculate total revenue (prices * quantities)
2. Create a new array with 10% increased prices
3. Calculate the difference between new and old prices
4. Find which items have price > 180

**Expected Output:**
```
Prices: [100 200 150 250 300]
Quantities: [2 1 3 2 1]
Revenue: [200 200 450 500 300]
New prices (10% increase): [110. 220. 165. 275. 330.]
Price difference: [10. 20. 15. 25. 30.]
Price > 180: [False  True False  True  True]
```

---

### Q3: In-Place Operations and Comparisons (5 minutes, Medium Difficulty)

**Problem:**
Create an array `scores = np.array([75, 88, 92, 65, 78, 95, 82, 70])`.
1. Print the original array
2. Use in-place operation to add 5 bonus points to all scores
3. Print the modified array
4. Create a boolean array showing which scores are >= 80
5. Count how many students scored >= 80
6. Create a new array and apply a grade curve: multiply all scores by 1.1, then use floor division to get integers

**Expected Output:**
```
Original scores: [75 88 92 65 78 95 82 70]
After adding 5 bonus points: [80 93 97 70 83 100 87 75]
Scores >= 80: [ True  True  True False  True  True  True False]
Number of students with >= 80: 5
Curved scores: [88 102 107 77 91 110 96 82]
```

---

### Q4: Temperature Analysis (5 minutes, Medium Difficulty)

**Problem:**
You have temperature data for a week in Celsius:
```python
celsius = np.array([22, 25, 28, 24, 20, 23, 26])
```
1. Convert all temperatures to Fahrenheit using: F = C * 9/5 + 32
2. Print both Celsius and Fahrenheit arrays
3. Find which days had temperature > 24°C
4. Calculate the average temperature in both Celsius and Fahrenheit
5. Find the temperature difference from the average for each day (in Celsius)

**Expected Output:**
```
Celsius: [22 25 28 24 20 23 26]
Fahrenheit: [71.6 77.  82.4 75.2 68.  73.4 78.8]
Days with temp > 24°C: [False  True  True False False False  True]
Average Celsius: 24.0°C
Average Fahrenheit: 75.2°F
Difference from average: [-2.  1.  4.  0. -4. -1.  2.]
```

---

### Q5: Financial Calculations (5 minutes, Medium Difficulty)

**Problem:**
You have monthly sales data for 6 months:
```python
sales = np.array([50000, 55000, 48000, 62000, 58000, 65000])
```
1. Calculate the monthly commission (7% of sales)
2. Calculate total commission for the 6 months
3. Find the percentage increase/decrease from first month for each month
4. Create a target array with 10% more than actual sales
5. Find which months met or exceeded 90% of the target
6. Calculate the average of months that exceeded $55,000 in sales

**Expected Output:**
```
Sales: [50000 55000 48000 62000 58000 65000]
Monthly commission (7%): [3500. 3850. 3360. 4340. 4060. 4550.]
Total commission: $23660.0
% Change from month 1: [  0.  10.  -4.  24.  16.  30.]
Target (10% above sales): [55000. 60500. 52800. 68200. 63800. 71500.]
90% of target: [49500. 54450. 47520. 61380. 57420. 64350.]
Met 90% of target: [ True  True  True  True  True  True]
Average of sales > 55000: $61666.67
```
