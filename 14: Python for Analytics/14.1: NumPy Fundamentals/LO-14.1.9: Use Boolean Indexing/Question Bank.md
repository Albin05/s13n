## Question Bank: Use Boolean Indexing

### Q1: Filter Array with Simple Condition (3 minutes, Low Difficulty)

**Problem:**
Create an array `arr = np.array([12, 45, 23, 51, 34, 18, 67, 8, 92])`.
1. Use boolean indexing to find all values greater than 30
2. Find all values less than or equal to 20
3. Find all values equal to 45
4. Count how many values are greater than 50

**Expected Output:**
```
Values > 30: [45 51 34 67 92]
Values <= 20: [12 18  8]
Values == 45: [45]
Count > 50: 3
```

---

### Q2: Create and Use Boolean Masks (3 minutes, Low Difficulty)

**Problem:**
Create an array `temps = np.array([28, 32, 25, 35, 22, 38, 30, 19])`.
1. Create a boolean mask for temperatures below 30
2. Print the mask
3. Use the mask to extract cold temperatures
4. Create a mask for temperatures between 25 and 35 (inclusive)
5. Extract temperatures in that range

**Expected Output:**
```
Mask for temps < 30: [ True False  True False  True False False  True]
Cold temps: [28 25 22 19]
Mask for 25-35 range: [ True  True  True  True False False  True False]
Temps in range: [28 32 25 35 30]
```

---

### Q3: Combine Multiple Conditions (5 minutes, Medium Difficulty)

**Problem:**
Create an array `scores = np.array([85, 92, 67, 78, 95, 88, 73, 81, 90, 65])`.
1. Find scores between 70 and 85 (inclusive)
2. Find scores less than 70 OR greater than 90
3. Find scores NOT in the range 75-85
4. Find scores that are either exactly 85 or exactly 95
5. Count how many scores are between 80 and 90 (exclusive)

**Expected Output:**
```
Scores 70-85: [85 78 73 81]
Scores < 70 or > 90: [92 95 65]
Scores NOT 75-85: [92 67 95 88 73 90 65]
Scores == 85 or == 95: [85 95]
Count 80-90 (exclusive): 3
```

---

### Q4: Filter and Modify Values (5 minutes, Medium Difficulty)

**Problem:**
Create an array `prices = np.array([25, 150, 75, 200, 50, 180, 30, 120])`.
1. Print original prices
2. Apply a 10% discount to all prices above 100 (multiply by 0.9)
3. Print modified prices
4. Cap all prices at 150 (set any price > 150 to 150)
5. Print final prices
6. Set any price below 40 to 40 (floor price)
7. Print final adjusted prices

**Expected Output:**
```
Original: [ 25 150  75 200  50 180  30 120]
After 10% discount on >100: [ 25 135  75 180  50 162  30 108]
After cap at 150: [ 25 135  75 150  50 150  30 108]
After floor at 40: [ 40 135  75 150  50 150  40 108]
```

---

### Q5: Analyze Sales Data (5 minutes, Medium Difficulty)

**Problem:**
Given daily sales data:
```python
sales = np.array([1200, 1500, 800, 2000, 1800, 950, 1100, 2200, 1600, 1300])
```
1. Find and print high-performing days (sales >= 1500)
2. Calculate and print the average of high-performing days
3. Find and print low-performing days (sales < 1200)
4. Count how many days had sales between 1000 and 1500 (inclusive)
5. Identify days with exceptional performance (sales >= 2000)
6. Calculate what percentage of days were high-performing

**Expected Output:**
```
High-performing days: [1500 2000 1800 2200 1600]
Average high performance: 1820.0
Low-performing days: [ 800  950 1100]
Days with sales 1000-1500: 4
Exceptional days: [2000 2200]
High-performance percentage: 50.0%
```
