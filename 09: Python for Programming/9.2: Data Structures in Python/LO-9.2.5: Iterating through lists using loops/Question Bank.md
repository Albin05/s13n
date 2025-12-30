## Question Bank: Iterating Through Lists Using Loops

### Q1: Basic List Iteration (3 minutes, Low Difficulty)

**Problem:**
Given `numbers = [5, 10, 15, 20, 25, 30, 35, 40]`:

1. Print all numbers
2. Print only numbers greater than 20
3. Calculate and print the sum of all numbers
4. Count how many numbers are divisible by 10
5. Find and print the maximum number

**Expected Output:**
```
All numbers: 5 10 15 20 25 30 35 40
Numbers > 20: 25 30 35 40
Sum: 180
Count divisible by 10: 4
Maximum: 40
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3, 9.2.4

---

### Q2: Using enumerate() (3 minutes, Low Difficulty)

**Problem:**
Given `fruits = ['apple', 'banana', 'orange', 'mango', 'grape']`:

1. Print each fruit with its index (0-based)
2. Print each fruit with position number (1-based)
3. Find and print indices of all fruits with more than 5 letters
4. Print fruits at even indices only
5. Create a dictionary mapping index to fruit name

**Expected Output:**
```
With index:
0: apple
1: banana
2: orange
3: mango
4: grape

With position:
1. apple
2. banana
3. orange
4. mango
5. grape

Long fruits (>5 letters):
Index 1: banana (6 letters)
Index 2: orange (6 letters)

Fruits at even indices:
0: apple
2: orange
4: grape

Dictionary: {0: 'apple', 1: 'banana', 2: 'orange', 3: 'mango', 4: 'grape'}
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3, 9.2.4

---

### Q3: Parallel List Processing with zip() (5 minutes, Medium Difficulty)

**Problem:**
You have three parallel lists:
```python
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'USB Cable']
prices = [999.99, 29.99, 79.99, 299.99, 9.99]
quantities = [5, 50, 30, 10, 100]
```

Using zip(), create a program that:
1. Prints each product with its price and quantity
2. Calculates total value for each product (price × quantity)
3. Finds the product with highest total value
4. Calculates total inventory value (sum of all product values)
5. Creates a list of tuples: (product, price, quantity, total_value)

**Expected Output:**
```
Inventory:
Laptop: $999.99 × 5 = $4999.95
Mouse: $29.99 × 50 = $1499.50
Keyboard: $79.99 × 30 = $2399.70
Monitor: $299.99 × 10 = $2999.90
USB Cable: $9.99 × 100 = $999.00

Highest value product: Laptop ($4999.95)
Total inventory value: $12898.05

Product details:
[('Laptop', 999.99, 5, 4999.95),
 ('Mouse', 29.99, 50, 1499.50),
 ('Keyboard', 79.99, 30, 2399.70),
 ('Monitor', 299.99, 10, 2999.90),
 ('USB Cable', 9.99, 100, 999.00)]
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3, 9.2.4

---

### Q4: Temperature Analysis (5 minutes, Medium Difficulty)

**Problem:**
You have daily high temperatures for a week:
```python
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temps = [72, 68, 75, 80, 78, 82, 79]
```

Write a program that:
1. Prints each day with its temperature
2. Finds the hottest and coldest days
3. Calculates the average temperature
4. Counts how many days were above average
5. Creates a "comfort rating" for each day:
   - "Cold" if temp < 70
   - "Comfortable" if 70 ≤ temp ≤ 78
   - "Hot" if temp > 78

Print a formatted report.

**Expected Output:**
```
Weekly Temperatures:
Monday: 72°F
Tuesday: 68°F
Wednesday: 75°F
Thursday: 80°F
Friday: 78°F
Saturday: 82°F
Sunday: 79°F

Analysis:
Hottest: Saturday (82°F)
Coldest: Tuesday (68°F)
Average: 76.3°F
Days above average: 4

Comfort Ratings:
Monday: 72°F - Comfortable
Tuesday: 68°F - Cold
Wednesday: 75°F - Comfortable
Thursday: 80°F - Hot
Friday: 78°F - Comfortable
Saturday: 82°F - Hot
Sunday: 79°F - Hot
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3, 9.2.4

---

### Q5: Grade Book Manager (5 minutes, Medium Difficulty)

**Problem:**
You have a grade book with students and their scores in three subjects:
```python
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
math_scores = [85, 92, 78, 88, 95]
science_scores = [90, 88, 82, 91, 89]
english_scores = [88, 85, 90, 87, 92]
```

Create a program that:
1. Calculates each student's average score
2. Determines letter grade (A: ≥90, B: ≥80, C: ≥70, D: ≥60, F: <60)
3. Finds the student with highest overall average
4. Finds which subject has the highest class average
5. Creates a report card for each student

Print a comprehensive report.

**Expected Output:**
```
Student Averages:
Alice: 87.7 (B)
Bob: 88.3 (B)
Charlie: 83.3 (B)
Diana: 88.7 (B)
Eve: 92.0 (A)

Top student: Eve (92.0)

Subject Averages:
Math: 87.6
Science: 88.0
English: 88.4
Highest class average: English (88.4)

Report Cards:
===== Alice =====
Math: 85
Science: 90
English: 88
Average: 87.7
Grade: B

===== Bob =====
Math: 92
Science: 88
English: 85
Average: 88.3
Grade: B

[... and so on for each student]
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3, 9.2.4
