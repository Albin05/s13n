# Editorials: Accessing Tuple Elements Using Indexing and Slicing

## Problem 1: Basic Indexing (Easy)

### Solution
```python
colors = ("red", "green", "blue", "yellow", "purple")

print(f"First: {colors[0]}")
print(f"Last: {colors[-1]}")
print(f"Middle: {colors[2]}")
```

**Output:**
```
First: red
Last: purple
Middle: blue
```

### Explanation
- `colors[0]` accesses first element (index 0)
- `colors[-1]` accesses last element using negative indexing
- `colors[2]` accesses third element (index 2)
- Negative indexing is more convenient for last element than `colors[len(colors)-1]`

---

## Problem 2: Negative Indexing Practice (Easy)

### Solution
```python
numbers = (10, 20, 30, 40, 50)

print(f"Last: {numbers[-1]}")
print(f"Second-to-last: {numbers[-2]}")
print(f"First (negative): {numbers[-5]}")
```

**Output:**
```
Last: 50
Second-to-last: 40
First (negative): 10
```

### Explanation
- `-1` always refers to last element
- `-2` refers to second-to-last
- `-5` refers to fifth-from-end, which is the first element in a 5-element tuple
- Negative indexing formula: `negative_index = length - positive_index`

---

## Problem 3: Basic Slicing (Easy)

### Solution
```python
data = (100, 200, 300, 400, 500, 600, 700)

first_three = data[:3]
last_three = data[-3:]
middle_slice = data[2:5]

print(f"First three: {first_three}")
print(f"Last three: {last_three}")
print(f"Middle slice: {middle_slice}")
```

**Output:**
```
First three: (100, 200, 300)
Last three: (500, 600, 700)
Middle slice: (300, 400, 500)
```

### Explanation
- `[:3]` means from start to index 3 (exclusive): indices 0, 1, 2
- `[-3:]` means from index -3 to end: last three elements
- `[2:5]` means from index 2 to 5 (exclusive): indices 2, 3, 4

---

## Problem 4: Reverse a Tuple (Easy)

### Solution
```python
original = (1, 2, 3, 4, 5)
reversed_tuple = original[::-1]

print(f"Original: {original}")
print(f"Reversed: {reversed_tuple}")
```

**Output:**
```
Original: (1, 2, 3, 4, 5)
Reversed: (5, 4, 3, 2, 1)
```

### Explanation
- `[::-1]` uses negative step to traverse backwards
- Creates a NEW tuple (original unchanged due to immutability)
- Most Pythonic way to reverse a sequence
- Equivalent to `tuple(reversed(original))`

---

## Problem 5: Every Other Element (Medium)

### Solution
```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

even_indices = numbers[::2]
odd_indices = numbers[1::2]
every_third = numbers[::3]

print(f"Even indices: {even_indices}")
print(f"Odd indices: {odd_indices}")
print(f"Every third: {every_third}")
```

**Output:**
```
Even indices: (0, 2, 4, 6, 8)
Odd indices: (1, 3, 5, 7, 9)
Every third: (0, 3, 6, 9)
```

### Explanation
- `[::2]` starts at index 0, step by 2: 0, 2, 4, 6, 8
- `[1::2]` starts at index 1, step by 2: 1, 3, 5, 7, 9
- `[::3]` starts at index 0, step by 3: 0, 3, 6, 9
- Step parameter controls which elements to select

---

## Problem 6: Extract RGB Components (Medium)

### Solution
```python
color = (255, 128, 64)

red = color[0]
green = color[1]
blue = color[2]

print(f"Red: {red}")
print(f"Green: {green}")
print(f"Blue: {blue}")
```

**Output:**
```
Red: 255
Green: 128
Blue: 64
```

### Explanation
- Tuples are perfect for fixed-size data like RGB colors
- Use indexing to extract each component
- Alternative: `red, green, blue = color` (tuple unpacking)
- Immutability ensures color values can't be accidentally changed

---

## Problem 7: Slice with Negative Indices (Medium)

### Solution
```python
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')

last_four = letters[-4:]
all_except_last_two = letters[:-2]
middle_section = letters[1:-1]

print(f"Last four: {last_four}")
print(f"All except last two: {all_except_last_two}")
print(f"Middle section: {middle_section}")
```

**Output:**
```
Last four: ('d', 'e', 'f', 'g')
All except last two: ('a', 'b', 'c', 'd', 'e')
Middle section: ('b', 'c', 'd', 'e', 'f')
```

### Explanation
- `[-4:]` from 4th-from-end to end
- `[:-2]` from start to 2nd-from-end (exclusive)
- `[1:-1]` from second element to second-to-last (exclusive)
- Negative indices useful when you don't know tuple length

---

## Problem 8: Nested Tuple Access (Medium)

### Solution
```python
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

second_row = matrix[1]
element = matrix[1][2]
last_of_first = matrix[0][-1]
first_of_last = matrix[-1][0]

print(f"Second row: {second_row}")
print(f"Element [1][2]: {element}")
print(f"Last of first row: {last_of_first}")
print(f"First of last row: {first_of_last}")
```

**Output:**
```
Second row: (4, 5, 6)
Element [1][2]: 6
Last of first row: 3
First of last row: 7
```

### Explanation
- First bracket selects row, second selects element in that row
- `matrix[1]` gets second row (index 1)
- `matrix[1][2]` gets third element (index 2) of second row (index 1)
- Can combine positive and negative indices: `matrix[0][-1]`

---

## Problem 9: Split Tuple at Index (Medium)

### Solution
```python
values = (10, 20, 30, 40, 50, 60)

split_index = 3
before = values[:split_index]
after = values[split_index:]

print(f"Before index 3: {before}")
print(f"From index 3 onwards: {after}")
```

**Output:**
```
Before index 3: (10, 20, 30)
From index 3 onwards: (40, 50, 60)
```

### Explanation
- `[:n]` and `[n:]` partition tuple at index n
- No overlap: `[:3]` ends at 3, `[3:]` starts at 3
- No gap: elements 0-2 and elements 3-5 cover all elements
- Useful for splitting data into head and tail

---

## Problem 10: Extract Date Components (Medium)

### Solution
```python
date = (2025, 12, 17, "Tuesday")

year = date[0]
month = date[1]
day = date[2]
weekday = date[3]

print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Weekday: {weekday}")
```

**Output:**
```
Year: 2025
Month: 12
Day: 17
Weekday: Tuesday
```

### Explanation
- Tuples good for structured data like dates
- Use indexing to extract each component
- Alternative: `year, month, day, weekday = date`
- Immutability prevents accidental date modification

---

## Problem 11: Get Middle Elements (Hard)

### Solution
```python
def get_middle(tup):
    return tup[1:-1]

data = (1, 2, 3, 4, 5, 6, 7)
middle = get_middle(data)

print(f"Middle elements: {middle}")
```

**Output:**
```
Middle elements: (2, 3, 4, 5, 6)
```

### Explanation
- `[1:-1]` excludes first (index 0) and last (index -1)
- Starts at second element (index 1)
- Stops before last element (index -1 is exclusive)
- Works for any tuple with at least 3 elements

---

## Problem 12: Alternate Extraction (Hard)

### Solution
```python
sequence = (10, 20, 30, 40, 50, 60, 70, 80, 90)

even_indices = sequence[::2]
odd_indices = sequence[1::2]

reversed_odds = odd_indices[::-1]
reversed_evens = even_indices[::-1]

combined = reversed_odds + reversed_evens

print(f"Even indices: {even_indices}")
print(f"Odd indices: {odd_indices}")
print(f"Combined reversed: {combined}")
```

**Output:**
```
Even indices: (10, 30, 50, 70, 90)
Odd indices: (20, 40, 60, 80)
Combined reversed: (80, 60, 40, 20, 90, 70, 50, 30, 10)
```

### Explanation
- Extract even/odd indices using step
- Reverse each using `[::-1]`
- Concatenate reversed tuples using `+`
- All operations create new tuples (immutability)

---

## Problem 13: Tic-Tac-Toe Board (Hard)

### Solution
```python
board = (
    ('X', 'O', 'X'),
    ('O', 'X', 'O'),
    ('X', 'O', 'X')
)

# Middle row
middle_row = board[1]

# First column
first_column = tuple(row[0] for row in board)

# Main diagonal
main_diagonal = tuple(board[i][i] for i in range(3))

# Center cell
center_is_x = board[1][1] == 'X'

print(f"Middle row: {middle_row}")
print(f"First column: {first_column}")
print(f"Main diagonal: {main_diagonal}")
print(f"Center is X: {center_is_x}")
```

**Output:**
```
Middle row: ('O', 'X', 'O')
First column: ('X', 'O', 'X')
Main diagonal: ('X', 'X', 'X')
Center is X: True
```

### Explanation
- Row access is direct: `board[1]`
- Column requires iteration: `row[0]` for each row
- Diagonal uses pattern `board[i][i]`
- Tuple comprehension creates new tuples from extracted data

---

## Problem 14: GPS Coordinate Processor (Hard)

### Solution
```python
coords = (40.7128, -74.0060, 10.5)

# Extract lat/long
lat_long = coords[:2]

# Convert altitude to feet
altitude_feet = coords[2] * 3.28084

print(f"2D Coordinates: {lat_long}")
print(f"Altitude in feet: {altitude_feet:.2f} feet")
```

**Output:**
```
2D Coordinates: (40.7128, -74.006)
Altitude in feet: 34.45 feet
```

### Explanation
- `[:2]` slices first two elements (lat, long)
- `[2]` indexes third element (altitude)
- Slicing creates new tuple with subset of data
- Useful for extracting relevant parts of structured data

---

## Problem 15: Slice Validation (Hard)

### Solution
```python
def safe_slice(tup, start, stop):
    result = tup[start:stop]
    if not result:
        print(f"Warning: Slice [{start}:{stop}] is out of range")
    print(f"Slice [{start}:{stop}]: {result}")
    return result

data = (1, 2, 3, 4, 5)
safe_slice(data, 1, 4)
safe_slice(data, 10, 20)
```

**Output:**
```
Slice [1:4]: (2, 3, 4)
Warning: Slice [10:20] is out of range
Slice [10:20]: ()
```

### Explanation
- Python slicing never raises IndexError
- Out-of-range slice returns empty tuple
- Check `if not result` to detect empty tuple
- Unlike indexing, slicing is forgiving

---

## Problem 16: Sliding Window (Very Hard)

### Solution
```python
def sliding_window(tup, window_size):
    windows = []
    for i in range(len(tup) - window_size + 1):
        window = tup[i:i+window_size]
        windows.append(window)
    return windows

result = sliding_window((1, 2, 3, 4, 5), 3)
print(f"Windows of size 3: {result}")
```

**Output:**
```
Windows of size 3: [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
```

### Explanation
- Loop from 0 to `len(tup) - window_size`
- Extract slice `[i:i+window_size]` at each position
- For length 5, window size 3: positions 0, 1, 2
- Each slice creates a new tuple of the specified size

---

## Problem 17: Matrix Row and Column (Very Hard)

### Solution
```python
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

def get_row(matrix, n):
    return matrix[n]

def get_column(matrix, n):
    return tuple(row[n] for row in matrix)

def get_diagonal(matrix):
    return tuple(matrix[i][i] for i in range(len(matrix)))

print(f"Row 1: {get_row(matrix, 1)}")
print(f"Column 1: {get_column(matrix, 1)}")
print(f"Diagonal: {get_diagonal(matrix)}")
```

**Output:**
```
Row 1: (4, 5, 6)
Column 1: (2, 5, 8)
Diagonal: (1, 5, 9)
```

### Explanation
- Row access is simple: direct indexing
- Column requires extracting same index from each row
- Diagonal follows pattern `matrix[i][i]`
- Tuple comprehension builds results

---

## Problem 18: Chunk Tuple (Very Hard)

### Solution
```python
def chunk_tuple(tup, chunk_size):
    chunks = []
    for i in range(0, len(tup), chunk_size):
        chunk = tup[i:i+chunk_size]
        chunks.append(chunk)
    return chunks

result = chunk_tuple((1, 2, 3, 4, 5, 6, 7), 3)
print(f"Chunks: {result}")
```

**Output:**
```
Chunks: [(1, 2, 3), (4, 5, 6), (7,)]
```

### Explanation
- Loop with step=chunk_size: `range(0, len(tup), chunk_size)`
- Extract slice `[i:i+chunk_size]` at each position
- Last chunk may be smaller if tuple length not evenly divisible
- Slicing handles end gracefully (no IndexError)

---

## Problem 19: Palindrome Check (Very Hard)

### Solution
```python
def is_palindrome_tuple(tup):
    return tup == tup[::-1]

test1 = (1, 2, 3, 2, 1)
test2 = (1, 2, 3, 4, 5)

print(f"{test1} is palindrome: {is_palindrome_tuple(test1)}")
print(f"{test2} is palindrome: {is_palindrome_tuple(test2)}")
```

**Output:**
```
(1, 2, 3, 2, 1) is palindrome: True
(1, 2, 3, 4, 5) is palindrome: False
```

### Explanation
- Compare tuple with its reverse
- `tup[::-1]` reverses the tuple
- If they're equal, it's a palindrome
- Simple and efficient one-liner

---

## Problem 20: Nested Tuple Flattening (Very Hard)

### Solution
```python
def flatten_once(nested_tuple):
    result = ()
    for inner_tuple in nested_tuple:
        result += inner_tuple
    return result

# Alternative using sum
def flatten_once_alt(nested_tuple):
    return sum(nested_tuple, ())

nested = ((1, 2), (3, 4), (5, 6))
flattened = flatten_once(nested)

print(f"Nested: {nested}")
print(f"Flattened: {flattened}")
```

**Output:**
```
Nested: ((1, 2), (3, 4), (5, 6))
Flattened: (1, 2, 3, 4, 5, 6)
```

### Explanation
- Iterate through outer tuple
- Concatenate each inner tuple using `+=`
- Alternative: `sum(nested_tuple, ())` concatenates all inner tuples
- `sum()` with empty tuple as start value concatenates tuples
- Only flattens one level (doesn't recursively flatten deeper nesting)
