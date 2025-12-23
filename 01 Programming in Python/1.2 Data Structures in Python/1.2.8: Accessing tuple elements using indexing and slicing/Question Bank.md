# Question Bank: Accessing Tuple Elements Using Indexing and Slicing

## Problem 1: Basic Indexing (Easy)
Given the tuple `colors = ("red", "green", "blue", "yellow", "purple")`, write code to:
1. Print the first color
2. Print the last color
3. Print the middle color (at index 2)

**Expected Output:**
```
First: red
Last: purple
Middle: blue
```

**Hint:** Use positive indexing for first and middle, negative indexing for last.

---

## Problem 2: Negative Indexing Practice (Easy)
Given `numbers = (10, 20, 30, 40, 50)`, access and print:
1. The last element using negative indexing
2. The second-to-last element
3. The first element using negative indexing

**Expected Output:**
```
Last: 50
Second-to-last: 40
First (negative): 10
```

**Hint:** -1 is last, -2 is second-to-last, -5 is first (for 5-element tuple).

---

## Problem 3: Basic Slicing (Easy)
Given `data = (100, 200, 300, 400, 500, 600, 700)`, create slices for:
1. First three elements
2. Last three elements
3. Elements from index 2 to 5 (exclusive)

**Expected Output:**
```
First three: (100, 200, 300)
Last three: (500, 600, 700)
Middle slice: (300, 400, 500)
```

**Hint:** Use `[:3]`, `[-3:]`, and `[2:5]`.

---

## Problem 4: Reverse a Tuple (Easy)
Given `original = (1, 2, 3, 4, 5)`, create a new reversed tuple and print both.

**Expected Output:**
```
Original: (1, 2, 3, 4, 5)
Reversed: (5, 4, 3, 2, 1)
```

**Hint:** Use slicing with step=-1: `[::-1]`.

---

## Problem 5: Every Other Element (Medium)
Given `numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)`, extract:
1. Every second element (even indices)
2. Every second element starting from index 1 (odd indices)
3. Every third element

**Expected Output:**
```
Even indices: (0, 2, 4, 6, 8)
Odd indices: (1, 3, 5, 7, 9)
Every third: (0, 3, 6, 9)
```

**Hint:** Use `[::2]`, `[1::2]`, and `[::3]`.

---

## Problem 6: Extract RGB Components (Medium)
Given a tuple representing an RGB color: `color = (255, 128, 64)`, extract and print each component with labels.

**Expected Output:**
```
Red: 255
Green: 128
Blue: 64
```

**Hint:** Use indexing `[0]`, `[1]`, `[2]`.

---

## Problem 7: Slice with Negative Indices (Medium)
Given `letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')`, create slices for:
1. Last four elements
2. All except the last two
3. From second to second-to-last (inclusive)

**Expected Output:**
```
Last four: ('d', 'e', 'f', 'g')
All except last two: ('a', 'b', 'c', 'd', 'e')
Middle section: ('b', 'c', 'd', 'e', 'f')
```

**Hint:** Use `[-4:]`, `[:-2]`, and `[1:-1]`.

---

## Problem 8: Nested Tuple Access (Medium)
Given a 2D matrix: `matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))`, access:
1. The entire second row
2. The element at row 1, column 2
3. The last element of the first row
4. The first element of the last row

**Expected Output:**
```
Second row: (4, 5, 6)
Element [1][2]: 6
Last of first row: 3
First of last row: 7
```

**Hint:** Use `matrix[1]`, `matrix[1][2]`, `matrix[0][-1]`, `matrix[-1][0]`.

---

## Problem 9: Split Tuple at Index (Medium)
Given `values = (10, 20, 30, 40, 50, 60)`, split it at index 3 into two tuples: before and after.

**Expected Output:**
```
Before index 3: (10, 20, 30)
From index 3 onwards: (40, 50, 60)
```

**Hint:** Use `[:3]` and `[3:]`.

---

## Problem 10: Extract Date Components (Medium)
Given a date tuple `date = (2025, 12, 17, "Tuesday")` representing (year, month, day, weekday), extract and print each component.

**Expected Output:**
```
Year: 2025
Month: 12
Day: 17
Weekday: Tuesday
```

**Hint:** Use indexing for each position.

---

## Problem 11: Get Middle Elements (Hard)
Write a function `get_middle(tup)` that returns a tuple containing all elements except the first and last.

Test with: `data = (1, 2, 3, 4, 5, 6, 7)`

**Expected Output:**
```
Middle elements: (2, 3, 4, 5, 6)
```

**Hint:** Use slicing `[1:-1]`.

---

## Problem 12: Alternate Extraction (Hard)
Given `sequence = (10, 20, 30, 40, 50, 60, 70, 80, 90)`, write code to:
1. Extract elements at even indices
2. Extract elements at odd indices
3. Combine them back in reverse order (odds first, then evens)

**Expected Output:**
```
Even indices: (10, 30, 50, 70, 90)
Odd indices: (20, 40, 60, 80)
Combined reversed: (80, 60, 40, 20, 90, 70, 50, 30, 10)
```

**Hint:** Use `[::2]`, `[1::2]`, then reverse each and concatenate.

---

## Problem 13: Tic-Tac-Toe Board (Hard)
Given a tic-tac-toe board:
```python
board = (
    ('X', 'O', 'X'),
    ('O', 'X', 'O'),
    ('X', 'O', 'X')
)
```

Write code to:
1. Get the entire middle row
2. Get the entire first column (as a tuple)
3. Get the main diagonal (top-left to bottom-right)
4. Check if the center cell is 'X'

**Expected Output:**
```
Middle row: ('O', 'X', 'O')
First column: ('X', 'O', 'X')
Main diagonal: ('X', 'X', 'X')
Center is X: True
```

**Hint:** Use nested indexing and tuple comprehension for column extraction.

---

## Problem 14: GPS Coordinate Processor (Hard)
Given a tuple of GPS coordinates: `coords = (40.7128, -74.0060, 10.5)` representing (latitude, longitude, altitude in meters).

Write a function that:
1. Extracts only lat/long (ignoring altitude)
2. Returns them as a 2-element tuple
3. Converts altitude to feet (1 meter = 3.28084 feet)

**Expected Output:**
```
2D Coordinates: (40.7128, -74.006)
Altitude in feet: 34.45 feet
```

**Hint:** Use slicing `[:2]` for lat/long, indexing `[2]` for altitude.

---

## Problem 15: Slice Validation (Hard)
Write a function `safe_slice(tup, start, stop)` that:
1. Takes a tuple and start/stop indices
2. Returns the slice if valid
3. Returns an empty tuple if indices are out of range
4. Prints a message if slicing would return empty

Test with:
```python
data = (1, 2, 3, 4, 5)
safe_slice(data, 1, 4)   # Should return (2, 3, 4)
safe_slice(data, 10, 20) # Should return () with message
```

**Expected Output:**
```
Slice [1:4]: (2, 3, 4)
Warning: Slice [10:20] is out of range
Slice [10:20]: ()
```

**Hint:** Python slicing doesn't raise errors, but check if result is empty.

---

## Problem 16: Sliding Window (Very Hard)
Write a function `sliding_window(tup, window_size)` that returns all possible windows of the given size.

For example: `sliding_window((1, 2, 3, 4, 5), 3)` should return:
```
[(1, 2, 3), (2, 3, 4), (3, 4, 5)]
```

**Expected Output:**
```
Windows of size 3: [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
```

**Hint:** Use a loop with slicing `[i:i+window_size]`.

---

## Problem 17: Matrix Row and Column (Very Hard)
Given a matrix: `matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))`, write functions to:
1. `get_row(matrix, n)` - returns nth row
2. `get_column(matrix, n)` - returns nth column as a tuple
3. `get_diagonal(matrix)` - returns main diagonal

**Expected Output:**
```
Row 1: (4, 5, 6)
Column 1: (2, 5, 8)
Diagonal: (1, 5, 9)
```

**Hint:** Use list comprehension with nested indexing for column.

---

## Problem 18: Chunk Tuple (Very Hard)
Write a function `chunk_tuple(tup, chunk_size)` that splits a tuple into chunks of the given size.

For example: `chunk_tuple((1, 2, 3, 4, 5, 6, 7), 3)` should return:
```
[(1, 2, 3), (4, 5, 6), (7,)]
```

**Expected Output:**
```
Chunks: [(1, 2, 3), (4, 5, 6), (7,)]
```

**Hint:** Use slicing in a loop: `tup[i:i+chunk_size]`.

---

## Problem 19: Palindrome Check (Very Hard)
Write a function `is_palindrome_tuple(tup)` that checks if a tuple reads the same forwards and backwards.

Test with:
- `(1, 2, 3, 2, 1)` - should return True
- `(1, 2, 3, 4, 5)` - should return False

**Expected Output:**
```
(1, 2, 3, 2, 1) is palindrome: True
(1, 2, 3, 4, 5) is palindrome: False
```

**Hint:** Compare `tup` with `tup[::-1]`.

---

## Problem 20: Nested Tuple Flattening (Very Hard)
Write a function `flatten_once(nested_tuple)` that flattens a tuple of tuples by one level.

For example:
```python
nested = ((1, 2), (3, 4), (5, 6))
```
Should return: `(1, 2, 3, 4, 5, 6)`

**Expected Output:**
```
Nested: ((1, 2), (3, 4), (5, 6))
Flattened: (1, 2, 3, 4, 5, 6)
```

**Hint:** Use tuple comprehension and sum or concatenation.
