# Question Bank: Iterating Through Lists Using Loops

## Problem 1: Calculate Average (Easy)
Write a program that calculates the average of numbers in a list.

**Input:**
```python
scores = [85, 92, 78, 95, 88]
```

**Expected Output:**
```
Average score: 87.60
```

**Hint:** Sum all scores and divide by the count.

---

## Problem 2: Count Vowels in Names (Easy)
Given a list of names, count how many names start with a vowel (A, E, I, O, U).

**Input:**
```python
names = ["Alice", "Bob", "Emily", "David", "Oliver", "Sarah"]
```

**Expected Output:**
```
Names starting with vowels: 3
```

**Hint:** Use `.startswith()` or check the first character.

---

## Problem 3: Find Maximum and Its Position (Easy)
Find both the maximum value in a list and its index position.

**Input:**
```python
numbers = [45, 23, 67, 89, 12, 56]
```

**Expected Output:**
```
Maximum value: 89
Position: 3
```

**Hint:** Use enumerate() to track both index and value.

---

## Problem 4: Temperature Converter (Medium)
Convert a list of temperatures from Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32

**Input:**
```python
celsius = [0, 10, 20, 30, 40]
```

**Expected Output:**
```
0°C = 32.0°F
10°C = 50.0°F
20°C = 68.0°F
30°C = 86.0°F
40°C = 104.0°F
```

**Hint:** Create a new list for Fahrenheit values, then use zip() to print pairs.

---

## Problem 5: Filter by Length (Medium)
Create a new list containing only words that are longer than a given length.

**Input:**
```python
words = ["apple", "pie", "banana", "cat", "strawberry", "dog"]
min_length = 5
```

**Expected Output:**
```
Long words: ['apple', 'banana', 'strawberry']
```

**Hint:** Use a conditional inside the loop to filter.

---

## Problem 6: Parallel List Processing (Medium)
Given three lists (product names, prices, and quantities), calculate the total cost for each product and the grand total.

**Input:**
```python
products = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 25.50, 79.99]
quantities = [1, 2, 1]
```

**Expected Output:**
```
Laptop: $999.99 x 1 = $999.99
Mouse: $25.50 x 2 = $51.00
Keyboard: $79.99 x 1 = $79.99
Grand Total: $1130.98
```

**Hint:** Use zip() to iterate through all three lists together.

---

## Problem 7: Find All Occurrences (Medium)
Find all index positions where a specific value appears in a list.

**Input:**
```python
numbers = [5, 2, 8, 2, 9, 2, 1, 2]
target = 2
```

**Expected Output:**
```
Value 2 found at positions: [1, 3, 5, 7]
```

**Hint:** Use enumerate() and append indices when the value matches.

---

## Problem 8: Running Total (Medium)
Create a list where each element is the running sum up to that point.

**Input:**
```python
numbers = [1, 2, 3, 4, 5]
```

**Expected Output:**
```
Running totals: [1, 3, 6, 10, 15]
```

**Explanation:** [1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5]

**Hint:** Keep a running total and append it to a new list at each step.

---

## Problem 9: Pair Adjacent Elements (Hard)
Create a list of tuples where each tuple contains adjacent elements.

**Input:**
```python
numbers = [1, 2, 3, 4, 5]
```

**Expected Output:**
```
Pairs: [(1, 2), (2, 3), (3, 4), (4, 5)]
```

**Hint:** Use range(len(list)-1) and access list[i] and list[i+1].

---

## Problem 10: Student Grade Statistics (Hard)
Given a list of student records (name and scores), calculate each student's average and identify the top performer.

**Input:**
```python
students = [
    ["Alice", 85, 90, 88],
    ["Bob", 92, 88, 95],
    ["Charlie", 78, 85, 80],
    ["David", 95, 98, 97]
]
```

**Expected Output:**
```
Alice: Average = 87.67
Bob: Average = 91.67
Charlie: Average = 81.00
David: Average = 96.67

Top performer: David with 96.67
```

**Hint:** Use nested data access: first element is name, rest are scores.

---

## Problem 11: Remove Duplicates (Hard)
Create a new list with duplicates removed, preserving the original order.

**Input:**
```python
numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
```

**Expected Output:**
```
Unique numbers: [1, 2, 3, 4, 5, 6]
```

**Hint:** Create an empty list and only append items not already in it.

---

## Problem 12: Merge and Sort Parallel Lists (Hard)
Given separate lists for names and ages, create a combined list sorted by age.

**Input:**
```python
names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 22, 28]
```

**Expected Output:**
```
Sorted by age:
Charlie (22)
Alice (25)
David (28)
Bob (30)
```

**Hint:** Combine using zip(), convert to list, sort by age, then iterate to display.

---

## Problem 13: Matrix Row Sums (Hard)
Calculate the sum of each row in a 2D list (matrix).

**Input:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Expected Output:**
```
Row 0 sum: 6
Row 1 sum: 15
Row 2 sum: 24
```

**Hint:** Outer loop for rows, inner loop to sum elements in each row.

---

## Problem 14: Word Frequency Counter (Hard)
Count how many times each word appears in a list.

**Input:**
```python
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
```

**Expected Output:**
```
apple: 3
banana: 2
cherry: 1
```

**Hint:** Use nested loops or a dictionary (if learned). For each unique word, count occurrences.

---

## Problem 15: Longest Increasing Sequence (Very Hard)
Find the length of the longest consecutive increasing sequence in a list.

**Input:**
```python
numbers = [1, 3, 2, 4, 5, 6, 3, 7, 8]
```

**Expected Output:**
```
Longest increasing sequence length: 4
Sequence: [2, 4, 5, 6]
```

**Hint:** Track current sequence length and maximum length as you iterate. Reset when a number doesn't increase.
