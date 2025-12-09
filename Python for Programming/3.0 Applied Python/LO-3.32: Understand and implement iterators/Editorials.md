# Editorials: Understand Iterators

## Problem 1: Basic Counter Iterator

```python
class CountUp:
    """Iterator that counts from start to end"""

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        """Return the iterator object"""
        return self

    def __next__(self):
        """Return the next value"""
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1
        return value

# Test
counter = CountUp(1, 5)
for num in counter:
    print(num, end=" ")
# Output: 1 2 3 4 5
```

### Explanation
1. `__init__()`: Initialize start, end, and current position
2. `__iter__()`: Return self to indicate this is an iterator
3. `__next__()`:
   - Check if current exceeds end, raise StopIteration if done
   - Store current value, increment current, return the stored value
   - This ensures we return the value before incrementing

**Time Complexity:** O(1) per iteration
**Space Complexity:** O(1)

---

## Problem 2: String Character Iterator

```python
class CharIterator:
    """Iterator for string characters"""

    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        """Return the iterator object"""
        return self

    def __next__(self):
        """Return the next character"""
        if self.index >= len(self.string):
            raise StopIteration

        char = self.string[self.index]
        self.index += 1
        return char

# Test
char_iter = CharIterator("Hello")
for char in char_iter:
    print(char, end="-")
# Output: H-e-l-l-o-
```

### Explanation
1. `__init__()`: Store the string and initialize index to 0
2. `__iter__()`: Return self
3. `__next__()`:
   - Check if index has reached the string length
   - If yes, raise StopIteration
   - Otherwise, get character at current index, increment index, return character

**Time Complexity:** O(1) per iteration
**Space Complexity:** O(1) - only stores index, not characters

---

## Problem 3: Skip Iterator

```python
class SkipIterator:
    """Iterator that skips elements"""

    def __init__(self, data, skip):
        self.data = data
        self.skip = skip
        self.index = 0

    def __iter__(self):
        """Return the iterator object"""
        return self

    def __next__(self):
        """Return the next element at skip interval"""
        if self.index >= len(self.data):
            raise StopIteration

        value = self.data[self.index]
        self.index += self.skip
        return value

# Test
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
skip_iter = SkipIterator(numbers, 3)
for num in skip_iter:
    print(num, end=" ")
# Output: 0 3 6 9
```

### Explanation
1. `__init__()`: Store data, skip value, and initialize index to 0
2. `__iter__()`: Return self
3. `__next__()`:
   - Check if index is beyond data length
   - Get value at current index
   - Increment index by skip amount (not just 1)
   - Return the value

For example, with skip=3:
- First call: index=0, return data[0], index becomes 3
- Second call: index=3, return data[3], index becomes 6
- Third call: index=6, return data[6], index becomes 9
- And so on...

**Time Complexity:** O(1) per iteration
**Space Complexity:** O(1)

---

## Problem 4: Fibonacci Iterator

```python
class FibonacciIterator:
    """Iterator for Fibonacci numbers up to max_value"""

    def __init__(self, max_value):
        self.max_value = max_value
        self.a = 0
        self.b = 1
        self.started = False

    def __iter__(self):
        """Return the iterator object"""
        return self

    def __next__(self):
        """Return the next Fibonacci number"""
        # Handle first number (0)
        if not self.started:
            self.started = True
            if self.a <= self.max_value:
                return self.a
            else:
                raise StopIteration

        # Check if current value exceeds max
        if self.b > self.max_value:
            raise StopIteration

        # Store current value
        current = self.b

        # Calculate next Fibonacci number
        self.a, self.b = self.b, self.a + self.b

        return current

# Test
fib = FibonacciIterator(50)
for num in fib:
    print(num, end=" ")
# Output: 0 1 1 2 3 5 8 13 21 34
```

### Explanation
1. `__init__()`: Initialize max_value, first two Fibonacci numbers (a=0, b=1), and a flag to track first iteration
2. `__iter__()`: Return self
3. `__next__()`:
   - First call: Return a (which is 0) if it doesn't exceed max
   - Subsequent calls: Check if b exceeds max, if yes raise StopIteration
   - Store current b value
   - Update a and b: a becomes b, b becomes a+b (next Fibonacci)
   - Return the stored value

**Sequence generation:**
- Initial: a=0, b=1
- Yield 0 (a), then a=1, b=1
- Yield 1 (b), then a=1, b=2
- Yield 1 (b), then a=2, b=3
- Yield 2 (b), then a=3, b=5
- And so on...

**Time Complexity:** O(1) per iteration
**Space Complexity:** O(1)

---

## Problem 5: Matrix Row Iterator

```python
class MatrixRowIterator:
    """Iterator for matrix elements row by row"""

    def __init__(self, matrix):
        self.matrix = matrix
        self.row = 0
        self.col = 0

    def __iter__(self):
        """Return the iterator object"""
        return self

    def __next__(self):
        """Return the next element"""
        # Check if we've exhausted all rows
        if self.row >= len(self.matrix):
            raise StopIteration

        # Handle empty rows
        while self.row < len(self.matrix) and self.col >= len(self.matrix[self.row]):
            self.row += 1
            self.col = 0

        # Check again after skipping empty rows
        if self.row >= len(self.matrix):
            raise StopIteration

        # Get current value
        value = self.matrix[self.row][self.col]

        # Move to next position
        self.col += 1

        # If we've reached end of current row, move to next row
        if self.col >= len(self.matrix[self.row]):
            self.row += 1
            self.col = 0

        return value

    def get_position(self):
        """Return current position as (row, col)"""
        # Return position of last yielded element
        if self.col == 0 and self.row > 0:
            # We just moved to next row, so last element was at end of previous row
            prev_row = self.row - 1
            prev_col = len(self.matrix[prev_row]) - 1
            return (prev_row, prev_col)
        else:
            # Current column was just incremented, so subtract 1
            return (self.row, self.col - 1)

# Test
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mat_iter = MatrixRowIterator(matrix)
for value in mat_iter:
    print(f"{value}", end=" ")
# Output: 1 2 3 4 5 6 7 8 9
print()

# Test with position
matrix2 = [[1, 2], [3, 4]]
mat_iter2 = MatrixRowIterator(matrix2)
print(next(mat_iter2), mat_iter2.get_position())  # 1 (0, 0)
print(next(mat_iter2), mat_iter2.get_position())  # 2 (0, 1)
print(next(mat_iter2), mat_iter2.get_position())  # 3 (1, 0)
print(next(mat_iter2), mat_iter2.get_position())  # 4 (1, 1)
```

### Explanation

**__next__() method:**
1. Check if we've exhausted all rows
2. Skip any empty rows by advancing row counter and resetting column
3. Get the value at current position (row, col)
4. Increment column
5. If we've reached the end of current row, move to next row and reset column to 0
6. Return the value

**get_position() method:**
1. Since col is incremented after getting the value, we need to adjust
2. If col is 0 and row > 0, we just moved to a new row, so the last element was at the end of the previous row
3. Otherwise, the last element was at current row and col-1

**How iteration works:**
```
Initial: row=0, col=0
1. Get matrix[0][0]=1, col becomes 1, return 1
2. Get matrix[0][1]=2, col becomes 2, return 2
3. Get matrix[0][2]=3, col becomes 3 (>= length), row becomes 1, col becomes 0, return 3
4. Get matrix[1][0]=4, col becomes 1, return 4
... and so on
```

**Time Complexity:** O(1) per iteration
**Space Complexity:** O(1) - only stores position indices
