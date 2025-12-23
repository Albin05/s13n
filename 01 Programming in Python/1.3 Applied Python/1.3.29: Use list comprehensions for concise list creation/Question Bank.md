# Question Bank: Use List Comprehensions

## Problem 1 (Easy)

**Title:** Square Numbers

**Problem Statement:**
Write a program that creates a list of squares of numbers from 1 to 10 using list comprehension.

**Input Format:**
No input required.

**Output Format:**
Print the list of squares.

**Sample Output:**
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**Constraints:**
- Use list comprehension
- Numbers from 1 to 10 inclusive

---

## Problem 2 (Easy)

**Title:** Extract Even Numbers

**Problem Statement:**
Given a list of numbers, create a new list containing only the even numbers using list comprehension.

**Input Format:**
A list of integers is provided in the code.

**Output Format:**
Print the list of even numbers.

**Sample Input:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

**Sample Output:**
```
[2, 4, 6, 8, 10, 12]
```

**Constraints:**
- Use list comprehension with condition
- Preserve original order

---

## Problem 3 (Medium)

**Title:** Temperature Converter

**Problem Statement:**
You have a list of temperatures in Fahrenheit. Create a new list with temperatures converted to Celsius using list comprehension. Formula: C = (F - 32) * 5/9

**Input Format:**
A list of Fahrenheit temperatures is provided.

**Output Format:**
Print the list of Celsius temperatures rounded to 1 decimal place.

**Sample Input:**
```python
fahrenheit = [32, 68, 86, 104, 122, 140]
```

**Sample Output:**
```
[0.0, 20.0, 30.0, 40.0, 50.0, 60.0]
```

**Constraints:**
- Use list comprehension
- Round to 1 decimal place
- Use the conversion formula

---

## Problem 4 (Medium)

**Title:** Word Length Filter

**Problem Statement:**
Given a sentence, extract all words that have more than 4 letters using list comprehension. Remove any punctuation and convert to lowercase.

**Input Format:**
A string sentence is provided.

**Output Format:**
Print the list of filtered words.

**Sample Input:**
```python
sentence = "The quick brown fox jumps over the lazy dog!"
```

**Sample Output:**
```
['quick', 'brown', 'jumps']
```

**Constraints:**
- Use list comprehension
- Filter by length > 4
- Remove punctuation
- Convert to lowercase

---

## Problem 5 (Hard)

**Title:** Matrix Diagonal Sum

**Problem Statement:**
Create a 5x5 matrix where each element at position (i, j) equals i + j using nested list comprehension. Then calculate and print the sum of the main diagonal elements (where i == j).

**Input Format:**
No input required.

**Output Format:**
First print the matrix (each row on a new line), then print the diagonal sum.

**Sample Output:**
```
[0, 1, 2, 3, 4]
[1, 2, 3, 4, 5]
[2, 3, 4, 5, 6]
[3, 4, 5, 6, 7]
[4, 5, 6, 7, 8]
Diagonal sum: 20
```

**Constraints:**
- Use nested list comprehension to create matrix
- Matrix must be 5x5
- Calculate sum of diagonal where i == j
- Elements should be i + j

**Hint:**
The diagonal elements are at positions (0,0), (1,1), (2,2), (3,3), (4,4).
