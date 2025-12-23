# Editorials: Using Range() Function for Numeric Iteration

## Problem 1: Count to 10 (Easy)

### Solution
```python
for i in range(1, 11):
    print(i)
```

**Output:**
```
1
2
3
4
5
6
7
8
9
10
```

### Explanation
- `range(1, 11)` generates numbers from 1 to 10
- Stop value (11) is **exclusive** - not included
- Start value (1) is **inclusive** - included
- Default step is 1
- Cleaner than `while i <= 10` approach

---

## Problem 2: Count to 5 (Easy)

### Solution
```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

### Explanation
- Single argument: `range(5)` means start at 0, stop before 5
- Equivalent to `range(0, 5)`
- Default start is 0
- Generates 5 numbers: 0, 1, 2, 3, 4
- Common pattern for counting iterations

---

## Problem 3: Sum Numbers 1 to 100 (Easy)

### Solution
```python
total = 0
for num in range(1, 101):
    total += num

print(f"Sum: {total}")
```

**Output:**
```
Sum: 5050
```

### Explanation
- `range(1, 101)` generates 1 through 100
- Each number added to total
- 1+2+3+...+100 = 5050
- Range makes this cleaner than manual counting
- Accumulator pattern with range

---

## Problem 4: Even Numbers (Medium)

### Solution
```python
for num in range(0, 11, 2):
    print(num)
```

**Output:**
```
0
2
4
6
8
10
```

### Explanation
- `range(0, 11, 2)` - third argument is **step**
- Start at 0, stop before 11, increment by 2
- Generates: 0, 2, 4, 6, 8, 10
- Step of 2 creates even numbers
- More efficient than checking `if num % 2 == 0`

---

## Problem 5: Countdown from 10 (Medium)

### Solution
```python
for i in range(10, 0, -1):
    print(i)
print("Blast off!")
```

**Output:**
```
10
9
8
7
6
5
4
3
2
1
Blast off!
```

### Explanation
- Start at 10, stop before 0, step by -1
- **Negative step** counts backwards
- Stops at 1 (doesn't include 0)
- Perfect for countdown sequences
- Cleaner than manual decrementing

---

## Problem 6: Multiples of 5 (Medium)

### Solution
```python
for num in range(5, 51, 5):
    print(num)
```

**Output:**
```
5
10
15
20
25
30
35
40
45
50
```

### Explanation
- Start at 5, stop before 51, step by 5
- Generates multiples of 5
- 10 numbers total
- Step parameter creates the pattern
- Alternative: `range(1, 11)` with `i * 5`

---

## Problem 7: Create List of Squares (Medium)

### Solution
```python
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

print(f"Squares: {squares}")
```

**Output:**
```
Squares: [1, 4, 9, 16, 25]
```

### Explanation
- Range generates 1 through 5
- Each number squared and appended
- Builds list: [1², 2², 3², 4², 5²]
- Range controls iterations
- List comprehension alternative: `[i**2 for i in range(1, 6)]`

---

## Problem 8: Index with Range (Hard)

### Solution
```python
fruits = ["apple", "banana", "orange"]

for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
```

**Output:**
```
Index 0: apple
Index 1: banana
Index 2: orange
```

### Explanation
- `len(fruits)` is 3, so `range(3)` gives 0, 1, 2
- Use i to access list by index
- **Note**: `enumerate()` is more Pythonic
- Range useful when you need index arithmetic
- Classic C-style iteration pattern

---

## Problem 9: Nested Range Loops (Hard)

### Solution
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()  # New line after each row
```

**Output:**
```
(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)
```

### Explanation
- Outer range: i = 1, 2, 3
- Inner range: j = 1, 2, 3 for each i
- Creates 3×3 grid of coordinates
- Nested ranges for 2D iteration
- Total 9 combinations

---

## Problem 10: Skip Numbers (Hard)

### Solution
```python
for i in range(0, 20, 3):
    print(i)
```

**Output:**
```
0
3
6
9
12
15
18
```

### Explanation
- Start 0, stop before 20, step 3
- Generates every 3rd number
- Step controls spacing
- 7 numbers total
- Pattern: multiples of 3 less than 20

---

## Problem 11: Reverse Range (Hard)

### Solution
```python
for i in range(5, 0, -1):
    print(i)
```

**Output:**
```
5
4
3
2
1
```

### Explanation
- Start 5, stop before 0, step -1
- Counts down from 5 to 1
- Negative step required for reverse
- Doesn't include 0
- Equivalent to reversed counting

---

## Problem 12: Multiplication Table (Very Hard)

### Solution
```python
n = 7

for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")
```

**Output:**
```
7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
7 × 4 = 28
7 × 5 = 35
7 × 6 = 42
7 × 7 = 49
7 × 8 = 56
7 × 9 = 63
7 × 10 = 70
```

### Explanation
- Range 1 to 10 for multipliers
- Multiply 7 by each number
- Formatted output
- Classic use of range
- Easily adaptable for any number

---

## Problem 13: Generate Fibonacci (Very Hard)

### Solution
```python
n = 10
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()
```

**Output:**
```
0 1 1 2 3 5 8 13 21 34
```

### Explanation
- Range controls number of terms
- `range(10)` gives exactly 10 iterations
- Fibonacci logic independent of range
- Range just counts iterations
- Simpler than while with counter

---

## Problem 14: Factorial with Range (Very Hard)

### Solution
```python
n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")
```

**Output:**
```
5! = 120
```

### Explanation
- Range 1 to n (inclusive)
- Multiply: 1 × 1 × 2 × 3 × 4 × 5 = 120
- Range replaces manual counting
- Clean, readable code
- Standard factorial algorithm

---

## Problem 15: Pattern Printing (Very Hard)

### Solution
```python
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # New line
```

**Output:**
```
*
**
***
****
*****
```

### Explanation
- Outer range: rows 1 to 5
- Inner range: stars per row (0 to i-1)
- Row 1: range(1) = 1 star
- Row 2: range(2) = 2 stars
- Creates triangle pattern
- Inner range depends on outer variable

---

## Problem 16: Sum Odd Numbers (Very Hard)

### Solution
```python
# Method 1: Step by 2
total = 0
for num in range(1, 21, 2):
    total += num
print(f"Sum of odds 1-20: {total}")

# Method 2: Filter evens
total = 0
for num in range(1, 21):
    if num % 2 != 0:
        total += num
print(f"Sum of odds 1-20: {total}")
```

**Output:**
```
Sum of odds 1-20: 100
Sum of odds 1-20: 100
```

### Explanation
- **Method 1**: Step by 2 from 1 (1, 3, 5, ...)
- **Method 2**: Check each number
- Both get sum = 100
- Method 1 more efficient (half iterations)
- Step parameter powerful for patterns

---

## Problem 17: Power Table (Very Hard)

### Solution
```python
base = 2

for exp in range(0, 11):
    result = base ** exp
    print(f"{base}^{exp} = {result}")
```

**Output:**
```
2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64
2^7 = 128
2^8 = 256
2^9 = 512
2^10 = 1024
```

### Explanation
- Range 0 to 10 for exponents
- Calculate 2 to each power
- Shows exponential growth
- 2^10 = 1024 (kilobyte)
- Range makes pattern clear

---

## Problem 18: List Reversal with Range (Very Hard)

### Solution
```python
numbers = [10, 20, 30, 40, 50]
reversed_nums = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_nums.append(numbers[i])

print(f"Reversed: {reversed_nums}")
```

**Output:**
```
Reversed: [50, 40, 30, 20, 10]
```

### Explanation
- Start at last index (len-1 = 4)
- Stop before -1 (includes 0)
- Step by -1 (go backwards)
- Indices: 4, 3, 2, 1, 0
- Manual reversal using range
- **Note**: `reversed()` or slicing simpler

---

## Problem 19: Skip Pattern (Very Hard)

### Solution
```python
for i in range(0, 50, 7):
    print(i, end=" ")
print()
```

**Output:**
```
0 7 14 21 28 35 42 49
```

### Explanation
- Start 0, stop before 50, step 7
- Every 7th number
- Multiples of 7 less than 50
- 8 numbers total
- Custom step creates pattern

---

## Problem 20: Grid Coordinates (Very Hard)

### Solution
```python
for row in range(3):
    for col in range(4):
        print(f"({row},{col})", end=" ")
    print()
```

**Output:**
```
(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
```

### Explanation
- 3 rows (0, 1, 2)
- 4 columns per row (0, 1, 2, 3)
- Nested ranges for 2D grid
- Total 12 coordinates
- Common pattern for matrices

---

## Key Concepts Demonstrated

1. **Single argument**: `range(n)` → 0 to n-1
2. **Two arguments**: `range(start, stop)` → start to stop-1
3. **Three arguments**: `range(start, stop, step)` → custom increment
4. **Negative step**: Count backwards
5. **Exclusive stop**: Stop value not included
6. **Zero-based**: Default start is 0
7. **Iteration control**: Precise number of loops
8. **Index generation**: Create indices for lists
9. **Nested ranges**: Multi-dimensional iteration
10. **Pattern generation**: Steps create sequences

## Range Syntax Summary

```python
# Basic forms
range(5)           # 0, 1, 2, 3, 4
range(1, 6)        # 1, 2, 3, 4, 5
range(0, 10, 2)    # 0, 2, 4, 6, 8

# Backward counting
range(10, 0, -1)   # 10, 9, 8, ..., 1
range(5, -1, -1)   # 5, 4, 3, 2, 1, 0

# Empty ranges
range(0)           # Empty
range(5, 5)        # Empty
range(10, 1)       # Empty (need negative step)

# Common patterns
range(len(list))   # Indices of list
range(1, n+1)      # 1 to n inclusive
range(0, n, 2)     # Even numbers
range(1, n, 2)     # Odd numbers
```

## Best Practices

1. **Use range for counting**: Better than while with counter
2. **Remember exclusive stop**: `range(1, 11)` for 1-10
3. **Prefer enumerate**: Instead of `range(len(list))`
4. **Use step wisely**: For patterns like evens/odds
5. **Negative step for reverse**: Must have start > stop
6. **Single arg for iterations**: `range(n)` when just counting
7. **List when needed**: `list(range(5))` → [0, 1, 2, 3, 4]

## Common Mistakes

1. **Forgetting exclusive stop**: `range(10)` goes 0-9, not 0-10
2. **Wrong direction**: `range(10, 1)` is empty, need `range(10, 1, -1)`
3. **Float arguments**: range only accepts integers
4. **Modifying in loop**: Don't change range variable value
5. **Over-using with lists**: Use `for item in list` instead of indices
6. **Forgetting +1**: `range(n)` for n iterations, `range(1, n+1)` for 1 to n

## Range vs List

```python
# Range is memory efficient
r = range(1000000)      # Instant, little memory
l = list(range(1000000)) # Slow, lots of memory

# Range is lazy (generates on demand)
for i in range(1000000):
    if i == 10:
        break  # Only generated 0-10, not all million

# Convert to list when needed
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
```

## Advanced Patterns

```python
# Reverse with negative step
for i in range(10, 0, -1):  # 10 down to 1

# Every nth element
for i in range(0, len(list), n):
    process(list[i])

# Pairs of indices
for i in range(0, len(list)-1):
    compare(list[i], list[i+1])

# Chunks
for i in range(0, len(list), chunk_size):
    chunk = list[i:i+chunk_size]

# Skip first/last
for i in range(1, len(list)-1):
    process(list[i])
```
