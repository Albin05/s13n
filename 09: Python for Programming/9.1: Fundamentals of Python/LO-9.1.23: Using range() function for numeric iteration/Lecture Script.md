### LO-23 Use Range() Function (15 minutes)


### CS Theory Bite

> **Origin**: `range()` uses **lazy evaluation** — it doesn't create a list in memory but generates numbers on demand. `range(1000000)` uses almost no memory!
>
> **Analogy**: `range()` is like a **number dispenser at a deli counter** — it gives you the next number when asked, not all numbers at once.
>
> **Why it matters**: `range()` is the bridge between counting loops (C-style) and Python's for-each — efficient numeric iteration.


### Hook (2 minutes)

**Say**: "Need to count 1 to 100? You could type [1, 2, 3, ... 100]. Or use range() and do it automatically!"

```python
# Manual way (tedious!)
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(num)

# Range way (automatic!)
for num in range(1, 11):
    print(num)
```

### Range Basics (5 minutes)

**Say**: "range() generates numbers on the fly. Three ways to use it!"

```python
# range(stop) - starts at 0
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - custom start
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# range(start, stop, step) - custom increment
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

**Key Points**:
- Stop value is NOT included
- Default start is 0
- Default step is 1
- Can count backwards with negative step

```python
# Counting backwards
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

### Common Patterns (4 minutes)

**Say**: "Here are the patterns you'll use most!"

```python
# Count exactly n times
for i in range(10):
    print("Hello!")  # Prints 10 times

# 1 to n inclusive
n = 5
for i in range(1, n+1):
    print(i)  # 1, 2, 3, 4, 5

# Iterate through indices
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Odd numbers
for num in range(1, 21, 2):
    print(num)  # 1, 3, 5, ..., 19

# Even numbers
for num in range(0, 21, 2):
    print(num)  # 0, 2, 4, ..., 20
```

### Real-World Application (2 minutes)

**Multiplication table**:
```python
n = 7

print(f"Multiplication table for {n}:")
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")
```

### Practice (2 minutes)

Sum numbers 1 to 50:
```python
total = 0
for num in range(1, 51):
    total += num

print(f"Sum: {total}")  # 1275
```
