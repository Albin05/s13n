# Question Bank: Building Lists Efficiently with Comprehensions

## Problem 1: Square Numbers (Easy)
Create a list comprehension that generates squares of numbers from 1 to 10.

**Expected Output:**
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**Hint:** Use range(1, 11) and square each number.

---

## Problem 2: Filter Positive Numbers (Easy)
Given a list of numbers, create a list comprehension to extract only positive numbers.

**Input:**
```python
numbers = [-5, 3, -2, 8, -1, 10, -7, 4, 0]
```

**Expected Output:**
```
[3, 8, 10, 4]
```

**Hint:** Use an if condition to check if number > 0.

---

## Problem 3: Uppercase Words (Easy)
Convert all words in a list to uppercase using a list comprehension.

**Input:**
```python
words = ["hello", "world", "python", "programming"]
```

**Expected Output:**
```
['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']
```

**Hint:** Use the .upper() method on each word.

---

## Problem 4: Even or Odd Labels (Medium)
Create a list that labels each number as "even" or "odd".

**Input:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Expected Output:**
```
['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
```

**Hint:** Use if-else before the for: `[expr_if if condition else expr_else for x in list]`

---

## Problem 5: Filter and Transform (Medium)
Create a list of squares of only even numbers from 1 to 20.

**Expected Output:**
```
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
```

**Hint:** Combine filtering (if at end) with transformation (squaring).

---

## Problem 6: String Lengths (Medium)
Create a list of lengths of words that are longer than 4 characters.

**Input:**
```python
words = ["apple", "pie", "banana", "cat", "strawberry", "dog", "kiwi"]
```

**Expected Output:**
```
[5, 6, 10]
```

**Hint:** Filter words by length, then apply len() to each.

---

## Problem 7: Temperature Conversion (Medium)
Convert a list of Celsius temperatures to Fahrenheit. Only convert temperatures above 0°C.

**Input:**
```python
celsius = [-5, 0, 10, 20, -3, 30, 40]
```

**Expected Output:**
```
[50.0, 68.0, 86.0, 104.0]
```

**Formula:** F = (C × 9/5) + 32

**Hint:** Filter celsius > 0, then apply the formula.

---

## Problem 8: Extract Initials (Medium)
Extract the first letter of each name and create a string of initials.

**Input:**
```python
names = ["Alice", "Bob", "Charlie", "David"]
```

**Expected Output:**
```
"ABCD"
```

**Hint:** Get first letter of each name with [0], then join them.

---

## Problem 9: Nested List Flattening (Hard)
Flatten a 2D list into a 1D list using list comprehension.

**Input:**
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

**Expected Output:**
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Hint:** Use nested comprehension: `[item for sublist in matrix for item in sublist]`

---

## Problem 10: Cartesian Product (Hard)
Create all possible pairs (tuples) from two lists.

**Input:**
```python
colors = ["red", "blue", "green"]
sizes = ["S", "M", "L"]
```

**Expected Output:**
```
[('red', 'S'), ('red', 'M'), ('red', 'L'),
 ('blue', 'S'), ('blue', 'M'), ('blue', 'L'),
 ('green', 'S'), ('green', 'M'), ('green', 'L')]
```

**Hint:** Nested comprehension with two for loops.

---

## Problem 11: Conditional Replacement (Hard)
Replace all numbers greater than 100 with 100, keep others as-is.

**Input:**
```python
values = [45, 120, 80, 150, 95, 200, 110]
```

**Expected Output:**
```
[45, 100, 80, 100, 95, 100, 100]
```

**Hint:** Use if-else: `[value if condition else replacement for value in values]`

---

## Problem 12: Remove Vowels (Hard)
Remove all vowels from a string using list comprehension and join.

**Input:**
```python
text = "Hello World"
```

**Expected Output:**
```
"Hll Wrld"
```

**Hint:** Filter characters where char not in "aeiouAEIOU", then join.

---

## Problem 13: Prime Number Filter (Hard)
Create a list of prime numbers from 2 to 50.

**Expected Output:**
```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

**Hint:** Use a helper function or nested comprehension to check if number has no divisors.

---

## Problem 14: Dictionary Value Extraction (Hard)
Extract ages of people older than 25 from a list of dictionaries.

**Input:**
```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 28}
]
```

**Expected Output:**
```
[30, 35, 28]
```

**Hint:** Filter by age, then extract the age value.

---

## Problem 15: Create Multiplication Table Row (Hard)
Create a single row of a multiplication table for a given number.

**Input:**
```python
number = 7
```

**Expected Output:**
```
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
```

**Hint:** Multiply the number by each value in range(1, 11).
