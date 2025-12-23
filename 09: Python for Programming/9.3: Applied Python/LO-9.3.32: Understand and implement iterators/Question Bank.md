# Question Bank: Understand Iterators

## Problem 1 (Easy)

**Title:** Basic Counter Iterator

**Problem Statement:**
Create an iterator class called `CountUp` that counts from a starting number up to (and including) an ending number. The class should implement the iterator protocol with `__iter__()` and `__next__()` methods.

**Input Format:**
Two integers: start and end values.

**Output Format:**
Iterate through numbers from start to end (inclusive).

**Sample Usage:**
```python
counter = CountUp(1, 5)
for num in counter:
    print(num, end=" ")
```

**Sample Output:**
```
1 2 3 4 5
```

**Constraints:**
- Implement `__iter__()` and `__next__()` methods
- Raise StopIteration when done
- start <= end

---

## Problem 2 (Easy)

**Title:** String Character Iterator

**Problem Statement:**
Create an iterator class called `CharIterator` that iterates through each character in a string. The class should implement the iterator protocol.

**Input Format:**
A string.

**Output Format:**
Iterate through each character one at a time.

**Sample Usage:**
```python
char_iter = CharIterator("Hello")
for char in char_iter:
    print(char, end="-")
```

**Sample Output:**
```
H-e-l-l-o-
```

**Constraints:**
- Implement `__iter__()` and `__next__()` methods
- Raise StopIteration when all characters are processed

---

## Problem 3 (Medium)

**Title:** Skip Iterator

**Problem Statement:**
Create an iterator class called `SkipIterator` that takes a list and a skip value. It should yield every nth element where n is the skip value. For example, with skip=2, it yields elements at indices 0, 2, 4, 6, etc.

**Input Format:**
A list and an integer skip value.

**Output Format:**
Iterate through elements at positions 0, skip, 2*skip, 3*skip, etc.

**Sample Usage:**
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
skip_iter = SkipIterator(numbers, 3)
for num in skip_iter:
    print(num, end=" ")
```

**Sample Output:**
```
0 3 6 9
```

**Constraints:**
- Implement `__iter__()` and `__next__()` methods
- skip >= 1
- Handle cases where skip is larger than list length

---

## Problem 4 (Medium)

**Title:** Fibonacci Iterator

**Problem Statement:**
Create an iterator class called `FibonacciIterator` that generates Fibonacci numbers up to a maximum value. The iterator should stop when the next Fibonacci number would exceed the maximum.

**Input Format:**
An integer max_value.

**Output Format:**
Iterate through Fibonacci numbers not exceeding max_value.

**Sample Usage:**
```python
fib = FibonacciIterator(50)
for num in fib:
    print(num, end=" ")
```

**Sample Output:**
```
0 1 1 2 3 5 8 13 21 34
```

**Constraints:**
- Implement `__iter__()` and `__next__()` methods
- First two Fibonacci numbers are 0 and 1
- Stop before exceeding max_value

---

## Problem 5 (Hard)

**Title:** Matrix Row Iterator

**Problem Statement:**
Create an iterator class called `MatrixRowIterator` that takes a 2D list (matrix) and iterates through it row by row, but yields individual elements (not rows). Additionally, implement a method `get_position()` that returns the current (row, column) position.

**Input Format:**
A 2D list (list of lists).

**Output Format:**
Iterate through all elements row by row, left to right.

**Sample Usage:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mat_iter = MatrixRowIterator(matrix)
for value in mat_iter:
    print(f"{value}", end=" ")
```

**Sample Output:**
```
1 2 3 4 5 6 7 8 9
```

**Additional Requirement:**
Implement a `get_position()` method that returns the current (row, col) as a tuple after each iteration.

**Sample Usage with Position:**
```python
mat_iter = MatrixRowIterator([[1, 2], [3, 4]])
print(next(mat_iter), mat_iter.get_position())  # 1 (0, 0)
print(next(mat_iter), mat_iter.get_position())  # 2 (0, 1)
```

**Constraints:**
- Implement `__iter__()`, `__next__()`, and `get_position()` methods
- Handle empty matrices
- Matrix can have rows of different lengths
