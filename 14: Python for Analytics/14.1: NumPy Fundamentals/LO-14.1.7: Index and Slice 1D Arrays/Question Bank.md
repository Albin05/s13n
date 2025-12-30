## Question Bank: Index and Slice 1D Arrays

### Q1: Access and Modify Elements (3 minutes, Low Difficulty)

**Problem:**
Create an array `arr = np.array([100, 200, 300, 400, 500])`.
1. Access and print the first element
2. Access and print the last element using negative indexing
3. Modify the third element (index 2) to 999
4. Print the entire array

**Expected Output:**
```
First element: 100
Last element: 500
Modified array: [100 200 999 400 500]
```

---

### Q2: Practice Negative Indexing (3 minutes, Low Difficulty)

**Problem:**
Create an array `numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])`.
1. Print the last 3 elements using negative indexing
2. Print the element at index -5
3. Modify the second-to-last element to 888
4. Print the final array

**Expected Output:**
```
Last 3 elements: [ 80  90 100]
Element at index -5: 60
Final array: [ 10  20  30  40  50  60  70  80 888 100]
```

---

### Q3: Basic Slicing Operations (5 minutes, Medium Difficulty)

**Problem:**
Create an array `data = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])`.
1. Extract elements from index 2 to 5 (exclusive) and print
2. Extract the first 4 elements and print
3. Extract elements from index 6 to the end and print
4. Extract all elements except the first and last and print
5. Extract the entire array using slicing and print

**Expected Output:**
```
Elements 2 to 5: [15 20 25]
First 4 elements: [ 5 10 15 20]
From index 6 to end: [35 40 45 50]
Except first and last: [10 15 20 25 30 35 40 45]
Entire array: [ 5 10 15 20 25 30 35 40 45 50]
```

---

### Q4: Slicing with Step Parameter (5 minutes, Medium Difficulty)

**Problem:**
Create an array `arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])`.
1. Extract every 2nd element (starting from index 0) and print
2. Extract every 3rd element and print
3. Extract elements from index 1 to 8 with step 2 and print
4. Reverse the entire array using slicing and print
5. Extract every 2nd element in reverse order and print

**Expected Output:**
```
Every 2nd element: [1 3 5 7 9]
Every 3rd element: [1 4 7 10]
Index 1 to 8, step 2: [2 4 6 8]
Reversed array: [10  9  8  7  6  5  4  3  2  1]
Every 2nd in reverse: [10  8  6  4  2]
```

---

### Q5: Analyze Temperature Data (5 minutes, Medium Difficulty)

**Problem:**
Given hourly temperature readings for a day (24 hours):
```python
temps = np.array([18, 18, 17, 17, 18, 19, 21, 23,
                  26, 28, 30, 31, 32, 32, 31, 30,
                  28, 26, 24, 22, 21, 20, 19, 18])
```

1. Extract and print temperatures for the first 6 hours (midnight to 6 AM)
2. Extract and print temperatures for hours 12-18 (noon to 6 PM)
3. Extract and print every 4th hour temperature reading
4. Extract and print the last 3 hours of the day
5. Calculate and print the average of the afternoon temperatures (hours 12-17)

**Expected Output:**
```
First 6 hours: [18 18 17 17 18 19]
Hours 12-18: [32 32 31 30 28 26]
Every 4th hour: [18 18 26 32 28 21]
Last 3 hours: [20 19 18]
Afternoon average: 30.5
```
