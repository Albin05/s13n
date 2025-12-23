# Pre-Read: Accessing Tuple Elements Using Indexing and Slicing

## What You'll Learn
In this lesson, you'll learn how to access individual tuple elements using indexing and how to extract portions of tuples using slicing - just like with lists, but remember they're immutable!

## Why This Matters
Accessing tuple elements is essential for:
- Extracting specific values from coordinates, colors, or records
- Working with function return values
- Processing structured data
- Navigating nested tuples
- Efficiently extracting subsets of data

Tuples use the same indexing and slicing syntax as lists, making it easy to work with both.

---

## What is Indexing?

**Indexing** means accessing a single element from a tuple using its position (index).

```python
coordinates = (10, 20, 30)

first = coordinates[0]    # 10
second = coordinates[1]   # 20
third = coordinates[2]    # 30
```

**Key characteristics:**
- **Zero-based**: First element is at index 0
- **Square brackets**: Use `[]` to access elements
- **Read-only**: Can read but cannot modify (immutability)
- **Negative indexing**: Access from the end using negative numbers

---

## Positive vs Negative Indexing

### Positive Indexing (from the start)

```python
colors = ("red", "green", "blue", "yellow")

# Index:    0       1        2        3
print(colors[0])  # red
print(colors[1])  # green
print(colors[3])  # yellow
```

### Negative Indexing (from the end)

```python
colors = ("red", "green", "blue", "yellow")

# Index:   -4      -3       -2       -1
print(colors[-1])  # yellow (last element)
print(colors[-2])  # blue   (second-to-last)
print(colors[-4])  # red    (first element)
```

**Why use negative indexing?**
- Easy access to last element: `my_tuple[-1]`
- No need to know tuple length
- More readable for accessing from end

---

## Index Out of Range Error

```python
numbers = (1, 2, 3)

# This will cause IndexError
value = numbers[5]  # IndexError: tuple index out of range

# Valid indices are 0, 1, 2 (or -3, -2, -1)
```

**Remember:** Index must be within valid range: `0` to `len(tuple) - 1`

---

## What is Slicing?

**Slicing** means extracting a portion (subset) of a tuple to create a new tuple.

```python
numbers = (10, 20, 30, 40, 50)

# Get elements from index 1 to 3 (excluding 3)
subset = numbers[1:3]
print(subset)  # (20, 30)
```

**Syntax:** `tuple[start:stop:step]`
- `start`: Starting index (inclusive)
- `stop`: Ending index (exclusive)
- `step`: Step size (optional, default is 1)

---

## Basic Slicing Examples

### Start and Stop

```python
fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Get elements from index 1 to 3 (excluding 3)
subset = fruits[1:3]
print(subset)  # ('banana', 'cherry')

# Get elements from index 0 to 2
first_two = fruits[0:2]
print(first_two)  # ('apple', 'banana')
```

### Omitting Start or Stop

```python
numbers = (1, 2, 3, 4, 5)

# From beginning to index 3
print(numbers[:3])    # (1, 2, 3)

# From index 2 to end
print(numbers[2:])    # (3, 4, 5)

# Entire tuple (copy)
print(numbers[:])     # (1, 2, 3, 4, 5)
```

### Using Step

```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Every second element
print(numbers[::2])   # (0, 2, 4, 6, 8)

# Every third element
print(numbers[::3])   # (0, 3, 6, 9)

# From index 1, every second element
print(numbers[1::2])  # (1, 3, 5, 7, 9)
```

---

## Reverse a Tuple with Slicing

```python
numbers = (1, 2, 3, 4, 5)

# Negative step reverses the tuple
reversed_numbers = numbers[::-1]
print(reversed_numbers)  # (5, 4, 3, 2, 1)
```

**How it works:** Step of `-1` means go backwards through the tuple.

---

## Slicing with Negative Indices

```python
letters = ('a', 'b', 'c', 'd', 'e')

# Last three elements
print(letters[-3:])     # ('c', 'd', 'e')

# All except last two
print(letters[:-2])     # ('a', 'b', 'c')

# From second-to-last to end
print(letters[-2:])     # ('d', 'e')
```

---

## Real-World Examples

### Example 1: Coordinates

```python
# 3D coordinate
point = (10, 20, 30)

x = point[0]
y = point[1]
z = point[2]

print(f"Position: X={x}, Y={y}, Z={z}")
# Position: X=10, Y=20, Z=30
```

### Example 2: RGB Color

```python
color = (255, 128, 64)

red = color[0]
green = color[1]
blue = color[2]

print(f"RGB({red}, {green}, {blue})")
# RGB(255, 128, 64)
```

### Example 3: Function Return Values

```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

stats = get_stats([10, 20, 30, 40, 50])

minimum = stats[0]
maximum = stats[1]
average = stats[2]

print(f"Min: {minimum}, Max: {maximum}, Avg: {average}")
# Min: 10, Max: 50, Avg: 30.0
```

### Example 4: Extract First and Last

```python
scores = (85, 90, 78, 92, 88)

first_score = scores[0]
last_score = scores[-1]

print(f"First: {first_score}, Last: {last_score}")
# First: 85, Last: 88
```

### Example 5: Get Middle Elements

```python
data = (10, 20, 30, 40, 50, 60, 70)

# Get elements from index 2 to 5
middle = data[2:5]
print(middle)  # (30, 40, 50)
```

---

## Nested Tuple Access

```python
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Access first row
first_row = matrix[0]
print(first_row)  # (1, 2, 3)

# Access element in first row, second column
element = matrix[0][1]
print(element)  # 2

# Access last element of last row
last_element = matrix[-1][-1]
print(last_element)  # 9
```

---

## Important Differences from Lists

### Tuples are Immutable

```python
numbers = (1, 2, 3, 4, 5)

# Can READ
print(numbers[0])  # 1

# CANNOT MODIFY
# numbers[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

### Slicing Creates New Tuple

```python
original = (1, 2, 3, 4, 5)
subset = original[1:4]

print(subset)    # (2, 3, 4) - new tuple
print(original)  # (1, 2, 3, 4, 5) - unchanged
```

---

## Common Indexing Patterns

### Get First Element
```python
first = my_tuple[0]
```

### Get Last Element
```python
last = my_tuple[-1]
```

### Get First Three Elements
```python
first_three = my_tuple[:3]
```

### Get Last Three Elements
```python
last_three = my_tuple[-3:]
```

### Get All Except First
```python
all_except_first = my_tuple[1:]
```

### Get All Except Last
```python
all_except_last = my_tuple[:-1]
```

### Reverse Tuple
```python
reversed_tuple = my_tuple[::-1]
```

### Every Other Element
```python
every_other = my_tuple[::2]
```

---

## Try It Yourself (Before Class)

Run this code:

```python
# Create a tuple
coordinates = (10, 20, 30, 40, 50)

# Indexing
print("First element:", coordinates[0])
print("Last element:", coordinates[-1])
print("Third element:", coordinates[2])

# Slicing
print("First three:", coordinates[:3])
print("Last two:", coordinates[-2:])
print("Middle elements:", coordinates[1:4])
print("Reversed:", coordinates[::-1])
print("Every other:", coordinates[::2])

# Nested tuples
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Second row:", matrix[1])
print("Element [1][2]:", matrix[1][2])
```

**Questions:**
1. What index would you use to get the last element of a tuple?
2. How do you get all elements except the first one?
3. What does `my_tuple[::-1]` do?
4. Why can't you modify tuple elements even though you can access them?

---

## Key Takeaways

Before class, remember:
1. **Zero-based indexing**: First element is at index 0
2. **Negative indexing**: Access from end using -1, -2, etc.
3. **Slicing syntax**: `tuple[start:stop:step]`
4. **Immutable**: Can read but cannot modify tuple elements
5. **Slicing creates new tuple**: Original tuple unchanged
6. **Stop is exclusive**: `tuple[1:3]` gets indices 1 and 2, not 3
7. **Nested access**: Use multiple brackets `tuple[i][j]`

## What's Next?

In the live session, we'll:
- Practice indexing and slicing extensively
- Work with nested tuples
- Understand edge cases and errors
- Solve real-world problems using tuple access
- Compare tuple and list indexing
- Master common slicing patterns

See you in class!
