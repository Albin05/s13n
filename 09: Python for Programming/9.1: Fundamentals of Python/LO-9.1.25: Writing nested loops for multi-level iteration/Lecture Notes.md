# Lecture Notes: Write Nested Loops

## Introduction

Nested loops introduce **multi-dimensional iteration** - the ability to process data with multiple levels or dimensions. They represent a fundamental pattern in computing for handling **combinations**, **grids**, and **hierarchical data**.

### Why Nested Loops Exist

**The multi-level problem**: Real-world data isn't linear - think spreadsheets (rows AND columns), chess boards (8x8 grid), class schedules (students AND subjects).
**Nested loops solution**: One loop handles outer level (rows), inner loop handles inner level (columns).

**Computer graphics**: Every pixel on your screen was drawn using nested loops - one loop for rows, one for columns. Video games render millions of pixels per second using this pattern!

### Real-World Analogy

Nested loops are like **reading a book**:
- **Outer loop**: Iterate through each chapter (chapter 1, 2, 3...)
- **Inner loop**: Read each page in that chapter (page 1, 2, 3...)
- **Pattern**: For each chapter, you read ALL its pages before moving to next chapter

Or like **a teacher taking attendance**:
- **Outer loop**: Go through each row of seats
- **Inner loop**: Check each student in that row
- **Complete inner before advancing outer**: Check all students in row 1 before moving to row 2

### The Power of Combinations

Nested loops let you explore **all possible combinations**:
```python
# 3 outer × 4 inner = 12 total combinations
for i in [1, 2, 3]:
    for j in ['A', 'B', 'C', 'D']:
        print(f"{i}{j}")  # 1A, 1B, 1C, 1D, 2A, 2B...
```

This **Cartesian product** is fundamental in mathematics, databases (SQL joins), and algorithms.

## Nested Loops

A nested loop is a loop inside another loop.


### Basic Syntax

```python
for outer_var in outer_sequence:
    for inner_var in inner_sequence:
        # Inner loop body
        # Runs completely for each outer iteration
```

## Simple Example

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Output:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1
```

## Patterns

### Rectangle of Stars

```python
for row in range(3):
    for col in range(5):
        print("*", end="")
    print()  # New line after each row

# Output:
# *****
# *****
# *****
```

### Multiplication Table

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}x{j}={i*j}", end="\t")
    print()

# Output: 5x5 multiplication table
```

### Right Triangle

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Output:
# *
# **
# ***
# ****
# *****
```

## Nested Loops with Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

## Real-World: All Combinations

```python
sizes = ["S", "M", "L"]
colors = ["Red", "Blue", "Green"]

for size in sizes:
    for color in colors:
        print(f"{size}-{color}")

# Output: All 9 combinations
```

## Key Takeaways

1. **Loop in loop**: Inner loop completes for each outer iteration
2. **Multiply iterations**: Total = outer * inner
3. **Use for patterns**: Grids, tables, combinations
4. **Can nest multiple**: 3+ levels (but avoid too deep)
5. **break affects inner**: Only exits innermost loop
