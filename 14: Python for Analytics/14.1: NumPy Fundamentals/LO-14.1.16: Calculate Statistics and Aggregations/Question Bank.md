## Question Bank: Calculate Statistics and Aggregations

### Q1: Basic Statistical Operations (3 minutes, Low Difficulty)

**Problem:**
Create an array of 10 random integers between 50 and 100. Calculate and display:
1. Mean
2. Median
3. Standard deviation
4. Variance
5. Minimum and maximum values
6. Range (max - min)

**Expected Output:**
```
Data: [87 72 95 63 78 89 91 68 74 82]
Mean: 79.90
Median: 80.00
Std Dev: 10.24
Variance: 104.89
Min: 63, Max: 95
Range: 32
```

**Category:** Implementation  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q2: Axis-based Aggregations (3 minutes, Low Difficulty)

**Problem:**
Create a 4×5 array of random integers between 1 and 100. Calculate:
1. Sum of each row
2. Mean of each column
3. Maximum value in each row
4. Minimum value in each column
5. Overall sum and mean

**Input:**
```python
np.random.seed(42)
data = np.random.randint(1, 101, (4, 5))
```

**Expected Output:**
```
Data:
[[52 93 15 72 61]
 [21 83 87 75 75]
 [88 24 3 22 88]
 [30 37 66 91 90]]

Row sums: [293 341 225 314]
Column means: [47.75 59.25 42.75 65.   78.5 ]
Row max: [93 87 88 91]
Column min: [21 24  3 22 61]
Overall sum: 1173
Overall mean: 58.65
```

**Category:** Implementation  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q3: Percentile and Quartile Analysis (5 minutes, Medium Difficulty)

**Problem:**
Create an array of 50 random integers between 20 and 100. Calculate:
1. Quartiles (Q1, Q2/median, Q3)
2. Interquartile range (IQR)
3. Outlier bounds (Q1 - 1.5*IQR, Q3 + 1.5*IQR)
4. Identify any outliers
5. Calculate percentiles: 10th, 25th, 50th, 75th, 90th

**Input:**
```python
np.random.seed(123)
data = np.random.randint(20, 101, 50)
```

**Expected Output:**
```
Q1: 45.75
Q2 (Median): 61.00
Q3: 77.25
IQR: 31.50

Outlier bounds: [-1.50, 124.50]
Outliers found: []

Percentiles [10, 25, 50, 75, 90]:
[32.1 45.75 61.  77.25 88.1]
```

**Category:** Implementation  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q4: Sales Performance Analysis (5 minutes, Medium Difficulty)

**Problem:**
You have monthly sales data for 6 salespersons over 12 months. Analyze:
1. Total sales per salesperson (annual performance)
2. Average monthly sales per salesperson
3. Best performing month for each salesperson
4. Overall monthly trends (total sales per month)
5. Top 3 salespersons by total annual sales
6. Most consistent salesperson (lowest std deviation)

**Input:**
```python
np.random.seed(456)
# 6 salespersons × 12 months
sales = np.random.randint(5000, 15000, (6, 12))
```

**Expected Output:**
```
Annual sales per salesperson:
[111000 108000 115000 106000 112000 109000]

Monthly averages per salesperson:
[9250.00 9000.00 9583.33 8833.33 9333.33 9083.33]

Best month for each salesperson:
Salesperson 1: Month 7
Salesperson 2: Month 11
Salesperson 3: Month 9
...

Monthly sales trends:
Month 1: $53000, Month 2: $58000, ...

Top 3 salespersons:
1. Salesperson 3: $115000
2. Salesperson 5: $112000
3. Salesperson 1: $111000

Most consistent: Salesperson 4 (Std: $2567.89)
```

**Category:** Application  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q5: Student Grade Analytics System (5 minutes, Medium Difficulty)

**Problem:**
Analyze exam scores for 20 students across 5 subjects. Create a comprehensive analytics report including:
1. Subject-wise statistics (mean, std, min, max)
2. Student rankings based on overall average
3. Grade distribution (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)
4. Identify students who need improvement (avg < 70)
5. Find the most challenging subject (lowest mean)
6. Calculate percentile rank for each student

**Input:**
```python
np.random.seed(789)
# 20 students × 5 subjects
scores = np.random.randint(55, 100, (20, 5))
subjects = ['Math', 'Science', 'English', 'History', 'Art']
```

**Expected Output:**
```
Subject Statistics:
Math: Mean=75.50, Std=12.34, Min=58, Max=99
Science: Mean=78.20, Std=11.56, Min=61, Max=97
English: Mean=76.80, Std=10.23, Min=59, Max=96
History: Mean=74.30, Std=13.45, Min=55, Max=98
Art: Mean=77.90, Std=11.78, Min=57, Max=99

Student Rankings:
Rank 1: Student 15 (Avg: 88.60)
Rank 2: Student 8 (Avg: 86.40)
Rank 3: Student 12 (Avg: 85.20)
...

Grade Distribution:
A (90+): 3 students
B (80-89): 6 students
C (70-79): 7 students
D (60-69): 3 students
F (<60): 1 student

Students needing improvement (avg < 70):
Student 3 (Avg: 67.80)
Student 17 (Avg: 65.40)

Most challenging subject: History (Mean: 74.30)

Percentile ranks calculated for all students.
```

**Category:** Application  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Additional Practice Problems

**Challenge 1: Rolling Statistics**
Calculate 7-day rolling mean and standard deviation for daily temperature data.

**Challenge 2: Correlation Analysis**
Find which product pairs have most similar sales patterns using correlation coefficients.

**Challenge 3: Seasonal Analysis**
Identify seasonal trends in quarterly sales data using aggregations by quarter.
