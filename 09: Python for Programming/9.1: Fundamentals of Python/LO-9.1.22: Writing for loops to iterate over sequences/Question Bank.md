# Question Bank: Writing For Loops to Iterate Over Sequences

## Problem 1: Print List Items (Easy)

Write a for loop to print each item from a list of colors.

Given list: `["red", "green", "blue", "yellow"]`

**Expected Output:**
```
red
green
blue
yellow
```

**Hint:** Use `for color in colors:` and print each color.

---

## Problem 2: Sum Numbers (Easy)

Calculate the sum of all numbers in a list using a for loop.

Given list: `[10, 20, 30, 40, 50]`

**Expected Output:**
```
Sum: 150
```

**Hint:** Initialize `total = 0`, then add each number in the loop.

---

## Problem 3: Count Characters (Easy)

Count how many characters are in the word "programming" using a for loop.

**Expected Output:**
```
Character count: 11
```

**Hint:** Initialize counter, iterate through string, increment counter.

---

## Problem 4: Print Each Letter (Easy)

Print each letter of the word "Python" on a separate line.

**Expected Output:**
```
P
y
t
h
o
n
```

**Hint:** Iterate directly through the string with `for letter in word:`.

---

## Problem 5: Double Each Number (Medium)

Create a new list where each number from the original list is doubled.

Given list: `[1, 2, 3, 4, 5]`

**Expected Output:**
```
Doubled: [2, 4, 6, 8, 10]
```

**Hint:** Create empty list, iterate original, append doubled values.

---

## Problem 6: Count Vowels (Medium)

Count the number of vowels in the sentence "hello world".

**Expected Output:**
```
Vowels: 3
```

**Hint:** Iterate each character, check if `char in "aeiou"`, count matches.

---

## Problem 7: Print with Index (Medium)

Print each fruit with its position number (starting from 1).

Given list: `["apple", "banana", "orange", "grape"]`

**Expected Output:**
```
1. apple
2. banana
3. orange
4. grape
```

**Hint:** Use `enumerate(fruits, start=1)` to get index and value.

---

## Problem 8: Combine Two Lists (Medium)

Print names and ages together from two separate lists.

Given:
- Names: `["Alice", "Bob", "Charlie"]`
- Ages: `[25, 30, 35]`

**Expected Output:**
```
Alice is 25 years old
Bob is 30 years old
Charlie is 35 years old
```

**Hint:** Use `zip(names, ages)` to pair them together.

---

## Problem 9: Find Maximum (Hard)

Find the largest number in a list without using the max() function.

Given list: `[45, 12, 78, 34, 90, 23, 67]`

**Expected Output:**
```
Maximum: 90
```

**Hint:** Initialize max with first element, compare each number, update if larger.

---

## Problem 10: Build Uppercase List (Hard)

Create a new list with all strings converted to uppercase.

Given list: `["hello", "world", "python"]`

**Expected Output:**
```
Uppercase: ['HELLO', 'WORLD', 'PYTHON']
```

**Hint:** Create empty list, iterate original, append `word.upper()`.

---

## Problem 11: Display Dictionary (Hard)

Print all key-value pairs from a dictionary in a formatted way.

Given dictionary: `{"name": "Alice", "age": 25, "city": "NYC"}`

**Expected Output:**
```
name: Alice
age: 25
city: NYC
```

**Hint:** Use `for key, value in dict.items():` to iterate pairs.

---

## Problem 12: Nested List Iteration (Hard)

Print all numbers from a 2D list (list of lists).

Given matrix:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Expected Output:**
```
1 2 3
4 5 6
7 8 9
```

**Hint:** Outer loop for rows, inner loop for numbers in each row.

---

## Problem 13: Count Even Numbers (Hard)

Count how many even numbers are in a list.

Given list: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

**Expected Output:**
```
Even numbers: 5
```

**Hint:** Iterate list, check if `num % 2 == 0`, count matches.

---

## Problem 14: Filter Positive Numbers (Very Hard)

Create a new list containing only positive numbers from the original list.

Given list: `[10, -5, 20, -3, 15, -8, 5]`

**Expected Output:**
```
Positive numbers: [10, 20, 15, 5]
```

**Hint:** Create empty list, check if `num > 0`, append positive ones.

---

## Problem 15: Average Calculator (Very Hard)

Calculate the average of numbers in a list.

Given list: `[85, 92, 78, 90, 88]`

**Expected Output:**
```
Average: 86.6
```

**Hint:** Sum all numbers using for loop, divide by count (use `len()`).

---

## Problem 16: Reverse String (Very Hard)

Build a reversed version of a string using a for loop.

Given string: "python"

**Expected Output:**
```
Reversed: nohtyp
```

**Hint:** Create empty string, iterate original, build result. Or use `reversed()`.

---

## Problem 17: Count Word Occurrences (Very Hard)

Count how many times each word appears in a list.

Given list: `["apple", "banana", "apple", "orange", "banana", "apple"]`

**Expected Output:**
```
apple: 3
banana: 2
orange: 1
```

**Hint:** Use dictionary to track counts, iterate list, increment counts.

---

## Problem 18: Flatten Nested List (Very Hard)

Convert a nested list into a single flat list.

Given nested list: `[[1, 2], [3, 4, 5], [6, 7, 8]]`

**Expected Output:**
```
Flattened: [1, 2, 3, 4, 5, 6, 7, 8]
```

**Hint:** Nested loops - outer for sublists, inner for numbers in each sublist.

---

## Problem 19: Multiplication Table (Very Hard)

Generate a 5x5 multiplication table.

**Expected Output:**
```
1   2   3   4   5
2   4   6   8  10
3   6   9  12  15
4   8  12  16  20
5  10  15  20  25
```

**Hint:** Nested loops, outer loop for rows (i), inner for columns (j), print i*j.

---

## Problem 20: Student Grades Average (Very Hard)

Calculate average grade for each student from a dictionary of lists.

Given grades:
```python
grades = {
    "Alice": [85, 90, 88],
    "Bob": [92, 87, 95],
    "Charlie": [78, 82, 80]
}
```

**Expected Output:**
```
Alice: 87.7
Bob: 91.3
Charlie: 80.0
```

**Hint:** Iterate dictionary items, calculate sum/len for each student's list.

---

## Problem 21: Find Common Elements (Very Hard)

Find elements that appear in both lists.

Given lists:
- List 1: `[1, 2, 3, 4, 5]`
- List 2: `[4, 5, 6, 7, 8]`

**Expected Output:**
```
Common elements: [4, 5]
```

**Hint:** Iterate one list, check if item `in` other list, collect matches.

---

## Problem 22: Sum Each Row (Very Hard)

Calculate the sum of each row in a 2D matrix.

Given matrix:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Expected Output:**
```
Row 1 sum: 6
Row 2 sum: 15
Row 3 sum: 24
```

**Hint:** Outer loop for rows, inner loop to sum each row's numbers.

---

## Problem 23: Create Index Dictionary (Very Hard)

Create a dictionary mapping each item to its index.

Given list: `["apple", "banana", "orange"]`

**Expected Output:**
```
{'apple': 0, 'banana': 1, 'orange': 2}
```

**Hint:** Use enumerate(), build dictionary with fruit as key, index as value.

---

## Problem 24: Print Pyramid Pattern (Very Hard)

Print a number pyramid using nested loops.

**Expected Output:**
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

**Hint:** Outer loop controls rows, inner loop prints numbers 1 to current row number.

---

## Problem 25: Calculate Product (Very Hard)

Calculate the product of all numbers in a list (multiply them all together).

Given list: `[2, 3, 4, 5]`

**Expected Output:**
```
Product: 120
```

**Hint:** Initialize product = 1, iterate list, multiply each number.

---

## Additional Practice Problems

### Problem 26: Enumerate from 1 (Medium)

Print each color with its position starting from 1 (not 0).

Given list: `["red", "green", "blue"]`

**Expected Output:**
```
1: red
2: green
3: blue
```

**Hint:** Use `enumerate(colors, start=1)`.

---

### Problem 27: Zip Three Lists (Hard)

Combine three lists and print them together.

Given:
- Names: `["Alice", "Bob"]`
- Ages: `[25, 30]`
- Cities: `["NYC", "LA"]`

**Expected Output:**
```
Alice, 25, NYC
Bob, 30, LA
```

**Hint:** `zip(names, ages, cities)` works with 3+ lists.

---

### Problem 28: Dictionary Keys Only (Easy)

Print only the keys from a dictionary.

Given dict: `{"a": 1, "b": 2, "c": 3}`

**Expected Output:**
```
a
b
c
```

**Hint:** Use `for key in dict.keys():` or just `for key in dict:`.

---

### Problem 29: Dictionary Values Only (Easy)

Print only the values from a dictionary.

Given dict: `{"a": 10, "b": 20, "c": 30}`

**Expected Output:**
```
10
20
30
```

**Hint:** Use `for value in dict.values():`.

---

### Problem 30: Reversed List Iteration (Medium)

Print a list in reverse order without modifying it.

Given list: `[1, 2, 3, 4, 5]`

**Expected Output:**
```
5
4
3
2
1
```

**Hint:** Use `for item in reversed(list):`.

---

## Key Patterns to Practice

1. **Basic iteration**: Process each item in sequence
2. **Accumulator**: Build sum, product, count
3. **Transform**: Create new list from original
4. **Filter**: Collect items matching condition
5. **Enumerate**: Get index and value together
6. **Zip**: Parallel iteration of multiple lists
7. **Dictionary iteration**: Keys, values, or pairs
8. **Nested loops**: Process 2D data
9. **Find min/max**: Track extremes while iterating
10. **Build dictionary**: Create dict from lists

## Common Mistakes to Avoid

1. Trying to use index variable without enumerate
2. Modifying list while iterating over it
3. Forgetting colon after for statement
4. Wrong indentation for loop body
5. Not initializing accumulator before loop
6. Using while when for is more appropriate
7. Confusing `.items()`, `.keys()`, and `.values()`
