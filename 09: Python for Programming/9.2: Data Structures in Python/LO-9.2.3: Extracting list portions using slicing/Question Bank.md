## Question Bank: Extracting List Portions Using Slicing

### Q1: Basic Slicing Operations (3 minutes, Low Difficulty)

**Problem:**
Given the list `numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`, use slicing to extract:
1. The first 4 elements
2. Elements from index 3 to 7
3. The last 3 elements
4. All elements except the first and last
5. Every element from index 5 to the end

**Expected Output:**
```
First 4: [10, 20, 30, 40]
Index 3 to 7: [40, 50, 60, 70]
Last 3: [80, 90, 100]
Except first and last: [20, 30, 40, 50, 60, 70, 80, 90]
From index 5: [60, 70, 80, 90, 100]
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.1, 9.2.2

---

### Q2: Using Step in Slicing (3 minutes, Low Difficulty)

**Problem:**
Given `data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]`, extract:
1. Every second element
2. Every third element
3. Every second element starting from index 1
4. The entire list reversed
5. Every second element in reverse

**Expected Output:**
```
Every 2nd: [0, 2, 4, 6, 8, 10, 12, 14]
Every 3rd: [0, 3, 6, 9, 12, 15]
Every 2nd from index 1: [1, 3, 5, 7, 9, 11, 13, 15]
Reversed: [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Every 2nd reversed: [15, 13, 11, 9, 7, 5, 3, 1]
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.1, 9.2.2

---

### Q3: Slice Assignment and Modification (5 minutes, Medium Difficulty)

**Problem:**
Start with `items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

Perform these operations in sequence (each modifies the list):
1. Replace elements at indices 2-5 with `[30, 40, 50]`
2. Delete elements at indices 5-7
3. Insert `[100, 200]` at index 3
4. Replace every second element (starting from index 0) with zeros
5. Show the final list

**Expected Output:**
```
After replacing 2-5 with [30,40,50]: [1, 2, 30, 40, 50, 6, 7, 8, 9, 10]
After deleting 5-7: [1, 2, 30, 40, 50, 8, 9, 10]
After inserting at 3: [1, 2, 30, 100, 200, 40, 50, 8, 9, 10]
After replacing evens with 0: [0, 2, 0, 100, 0, 40, 0, 8, 0, 10]
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.1, 9.2.2

---

### Q4: Temperature Data Analysis (5 minutes, Medium Difficulty)

**Problem:**
You have hourly temperature readings for 24 hours:
```python
temps = [65, 66, 64, 63, 62, 61, 62, 64, 68, 72, 75, 78,
         80, 82, 83, 81, 79, 76, 73, 70, 68, 67, 66, 65]
```

Using slicing, extract and calculate:
1. Morning temperatures (hours 6-12, indices 6-12)
2. Afternoon temperatures (hours 12-18, indices 12-18)
3. Evening temperatures (hours 18-24, indices 18-24)
4. Peak hours (temperatures above 75 degrees - you'll need to identify these first)
5. Every 3rd hour reading for a summary report

For each, print the slice and its average temperature (rounded to 1 decimal).

**Expected Output:**
```
Morning (6-12): [62, 64, 68, 72, 75, 78]
  Average: 69.8°F

Afternoon (12-18): [80, 82, 83, 81, 79, 76]
  Average: 80.2°F

Evening (18-24): [73, 70, 68, 67, 66, 65]
  Average: 68.2°F

Every 3rd hour: [65, 63, 62, 72, 80, 81, 73, 66]
  Average: 70.2°F
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2

---

### Q5: Sales Data Processing (5 minutes, Medium Difficulty)

**Problem:**
A store's daily sales for a month (30 days) are stored in a list:
```python
sales = [120, 135, 142, 128, 156, 189, 201, 145, 132, 128,
         167, 178, 192, 205, 198, 176, 188, 194, 203, 210,
         189, 176, 182, 195, 208, 215, 198, 187, 179, 165]
```

Using slicing:
1. Extract Week 1 (days 0-7) and Week 4 (days 21-28)
2. Get all weekend sales (assuming Sat-Sun are at positions 5-6, 12-13, 19-20, 26-27)
3. Create a weekly summary showing every 7th day
4. Find the second half of the month
5. Reverse the last 10 days to see recent trend backwards

For each, show the slice and calculate total sales.

**Expected Output:**
```
Week 1 sales: [120, 135, 142, 128, 156, 189, 201]
  Total: $1071

Week 4 sales: [176, 182, 195, 208, 215, 198, 187]
  Total: $1361

Weekend sales: [189, 201, 178, 192, 194, 203, 182, 195]
  Total: $1534

Weekly summary (every 7th): [120, 145, 188, 189]
  Total: $642

Second half: [176, 188, 194, 203, 210, 189, 176, 182, 195, 208, 215, 198, 187, 179, 165]
  Total: $2865

Last 10 days reversed: [165, 179, 187, 198, 215, 208, 195, 182, 176, 189]
  Total: $1894
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2
