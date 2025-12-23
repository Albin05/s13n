### LO-25 Write Nested Loops (20 minutes)

### Hook (3 minutes)

**Say**: "Imagine seating guests at a wedding with 5 tables, each with 6 chairs. How do you assign seat numbers? Table 1: seats 1-6. Table 2: seats 1-6. That's nested loops - a loop inside a loop!"

```python
for table in range(1, 6):      # 5 tables
    for seat in range(1, 7):    # 6 seats per table
        print(f"Table {table}, Seat {seat}")
```

### What are Nested Loops (4 minutes)

**Say**: "A nested loop is a loop inside another loop. The inner loop runs COMPLETELY for EACH iteration of the outer loop."

```python
for outer in range(3):      # Runs 3 times
    print(f"Outer: {outer}")
    for inner in range(2):  # Runs 2 times FOR EACH outer
        print(f"  Inner: {inner}")

# Output:
# Outer: 0
#   Inner: 0
#   Inner: 1
# Outer: 1
#   Inner: 0
#   Inner: 1
# Outer: 2
#   Inner: 0
#   Inner: 1
```

**Key Points**:
- Inner loop completes all iterations before outer moves forward
- Total iterations = outer × inner (3 × 2 = 6 in example above)
- Can have multiple levels (but keep it simple!)

### Simple Patterns (5 minutes)

**Rectangle pattern**:
```python
# 4 rows, 6 columns
for row in range(4):
    for col in range(6):
        print('*', end=' ')
    print()  # New line after each row

# Output:
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
```

**Multiplication table**:
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}×{j}={i*j:2}", end="  ")
    print()

# Output:
# 1×1= 1  1×2= 2  1×3= 3  1×4= 4  1×5= 5
# 2×1= 2  2×2= 4  2×3= 6  2×4= 8  2×5=10
# ...
```

### Working with 2D Lists (4 minutes)

**Say**: "Nested loops are perfect for 2D lists (lists of lists)!"

```python
# Create a 3x3 matrix of zeros
matrix = []

for row in range(3):
    current_row = []
    for col in range(3):
        current_row.append(0)
    matrix.append(current_row)

# Result: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

**Iterate through 2D list**:
```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    for item in row:
        print(item, end=' ')
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

### Advanced Patterns (2 minutes)

**Triangle pattern**:
```python
for i in range(1, 6):
    for j in range(i):
        print('*', end=' ')
    print()

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
```

### Practice (2 minutes)

Print all pairs from two lists:
```python
colors = ["red", "blue"]
sizes = ["S", "M", "L"]

for color in colors:
    for size in sizes:
        print(f"{color}-{size}")

# Output:
# red-S
# red-M
# red-L
# blue-S
# blue-M
# blue-L
```
