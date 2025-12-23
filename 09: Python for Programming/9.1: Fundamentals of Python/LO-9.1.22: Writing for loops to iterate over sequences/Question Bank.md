### **1. Print List Items**

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

---

### **2. Sum Numbers**

Calculate the sum of all numbers in a list using a for loop.

Given list: `[10, 20, 30, 40, 50]`

**Expected Output:**
```
Sum: 150
```

**Hint:** Initialize `total = 0`, then add each number in the loop.

---

---

### **3. Count Characters**

Count how many characters are in the word "programming" using a for loop.

**Expected Output:**
```
Character count: 11
```

**Hint:** Initialize counter, iterate through string, increment counter.

---

---

### **4. Print Each Letter**

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

---

### **5. Double Each Number**

Create a new list where each number from the original list is doubled.

Given list: `[1, 2, 3, 4, 5]`

**Expected Output:**
```
Doubled: [2, 4, 6, 8, 10]
```

**Hint:** Create empty list, iterate original, append doubled values.

---

---

### **6. Count Vowels**

Count the number of vowels in the sentence "hello world".

**Expected Output:**
```
Vowels: 3
```

**Hint:** Iterate each character, check if `char in "aeiou"`, count matches.

---

---

### **7. Print with Index**

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

---

### **8. Combine Two Lists**

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

---

### **9. Find Maximum**

Find the largest number in a list without using the max() function.

Given list: `[45, 12, 78, 34, 90, 23, 67]`

**Expected Output:**
```
Maximum: 90
```

**Hint:** Initialize max with first element, compare each number, update if larger.

---

---

### **10. Build Uppercase List**

Create a new list with all strings converted to uppercase.

Given list: `["hello", "world", "python"]`

**Expected Output:**
```
Uppercase: ['HELLO', 'WORLD', 'PYTHON']
```

**Hint:** Create empty list, iterate original, append `word.upper()`.

---

---

### **11. Display Dictionary**

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

---

### **12. Nested List Iteration**

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

---

### **13. Count Even Numbers**

Count how many even numbers are in a list.

Given list: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

**Expected Output:**
```
Even numbers: 5
```

**Hint:** Iterate list, check if `num % 2 == 0`, count matches.

---

---

### **14. Filter Positive Numbers**

Create a new list containing only positive numbers from the original list.

Given list: `[10, -5, 20, -3, 15, -8, 5]`

**Expected Output:**
```
Positive numbers: [10, 20, 15, 5]
```

**Hint:** Create empty list, check if `num > 0`, append positive ones.

---

---

### **15. Average Calculator**

Calculate the average of numbers in a list.

Given list: `[85, 92, 78, 90, 88]`

**Expected Output:**
```
Average: 86.6
```

**Hint:** Sum all numbers using for loop, divide by count (use `len()`).

---

---

### **16. Reverse String**

Build a reversed version of a string using a for loop.

Given string: "python"

**Expected Output:**
```
Reversed: nohtyp
```

**Hint:** Create empty string, iterate original, build result. Or use `reversed()`.

---

---

### **17. Count Word Occurrences**

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

---

### **18. Flatten Nested List**

Convert a nested list into a single flat list.

Given nested list: `[[1, 2], [3, 4, 5], [6, 7, 8]]`

**Expected Output:**
```
Flattened: [1, 2, 3, 4, 5, 6, 7, 8]
```

**Hint:** Nested loops - outer for sublists, inner for numbers in each sublist.

---

---

### **19. Multiplication Table**

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

---

### **20. Student Grades Average**

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

---

### **21. Find Common Elements**

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

---

### **22. Sum Each Row**

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

---

### **23. Create Index Dictionary**

Create a dictionary mapping each item to its index.

Given list: `["apple", "banana", "orange"]`

**Expected Output:**
```
{'apple': 0, 'banana': 1, 'orange': 2}
```

**Hint:** Use enumerate(), build dictionary with fruit as key, index as value.

---

---

### **24. Print Pyramid Pattern**

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

---

### **25. Calculate Product**

Calculate the product of all numbers in a list (multiply them all together).

Given list: `[2, 3, 4, 5]`

**Expected Output:**
```
Product: 120
```

**Hint:** Initialize product = 1, iterate list, multiply each number.

---

## Additional Practice Problems

#

---

### **26. Enumerate from 1**

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

#

---

### **27. Zip Three Lists**

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

#

---

### **28. Dictionary Keys Only**

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

#

---

### **29. Dictionary Values Only**

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

#

---

### **30. Reversed List Iteration**

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

---

