# Pre-Read: Writing Nested Loops for Multi-Level Iteration

## What You'll Learn
In this lesson, you'll learn how to write loops inside other loops (nested loops) to work with multi-dimensional data or create patterns. This is essential for working with grids, tables, and complex iterations.

## Why This Matters
Nested loops are used everywhere in programming:
- Creating multiplication tables
- Drawing patterns (stars, pyramids, grids)
- Processing 2D game boards (chess, tic-tac-toe)
- Working with rows and columns in spreadsheets
- Comparing every item with every other item

---

## What are Nested Loops?

A **nested loop** is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop.

```python
for outer in outer_sequence:
    for inner in inner_sequence:
        # This runs for every combination of outer and inner
```

---

## Simple Example: Multiplication Table

```python
for i in range(1, 4):    # Outer loop: rows
    for j in range(1, 4):  # Inner loop: columns
        print(f"{i} x {j} = {i*j}")
    print()  # Blank line after each row

# Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
#
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
#
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
```

**How it works:**
1. Outer loop: i = 1
   - Inner loop runs completely: j = 1, 2, 3
2. Outer loop: i = 2
   - Inner loop runs completely: j = 1, 2, 3
3. Outer loop: i = 3
   - Inner loop runs completely: j = 1, 2, 3

---

## Visual Example: Rectangle of Stars

```python
for row in range(3):     # 3 rows
    for col in range(5):   # 5 stars per row
        print("*", end="")
    print()  # New line after each row

# Output:
# *****
# *****
# *****
```

---

## Common Patterns

### Pattern 1: Right Triangle

```python
for row in range(1, 6):
    for col in range(row):
        print("*", end="")
    print()

# Output:
# *
# **
# ***
# ****
# *****
```

### Pattern 2: Number Grid

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}{j}", end=" ")
    print()

# Output:
# 11 12 13
# 21 22 23
# 31 32 33
```

---

## Real-World Example: Comparing Items

```python
students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "English"]

for student in students:
    for subject in subjects:
        print(f"{student} takes {subject}")
    print()

# Output:
# Alice takes Math
# Alice takes Science
# Alice takes English
#
# Bob takes Math
# Bob takes Science
# Bob takes English
#
# Charlie takes Math
# Charlie takes Science
# Charlie takes English
```

---

## How Many Times Does Inner Loop Run?

```python
for i in range(3):        # Runs 3 times
    for j in range(4):      # Runs 4 times for EACH i
        print(f"({i}, {j})")

# Inner loop runs: 3 × 4 = 12 times total!
```

**Formula:** Total iterations = (outer iterations) × (inner iterations)

---

## Try It Yourself (Before Class)

Run this code:

```python
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

**Questions:**
1. What pattern does this create?
2. Why does the inner range use `i + 1`?
3. Try changing `print(j, end="")` to `print("*", end="")` - what happens?

---

## Key Takeaways

Before class, remember:
1. **Nested loops = loop inside loop** - inner runs completely for each outer iteration
2. **Common use** - grids, patterns, tables, combinations
3. **Total iterations** - multiply outer count by inner count
4. **Indentation matters** - shows which loop contains which code
5. **Can nest many levels** - but usually 2-3 is maximum for readability

## What's Next?

In the live session, we'll:
- Create various patterns with nested loops
- Work with 2D data structures
- Use break and continue in nested loops
- Understand performance implications
- Practice debugging nested loops

See you in class!
