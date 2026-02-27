# Lecture Notes: Use Range Function

## Introduction

The `range()` function represents a crucial innovation in how programming languages handle **numeric iteration**. It introduces the concept of **lazy generation** - producing values on-demand rather than creating them all at once in memory.

### Why Range Exists

**The memory problem**: If you need to count from 1 to 1 million, creating a list of 1 million numbers wastes memory and time.
**Range solution**: Generate numbers one at a time, as needed. Only the current number exists in memory.

**Historical note**: Python 2 had `range()` (created a list) and `xrange()` (lazy generation). Python 3 simplified this - `range()` now always uses lazy generation, making it memory-efficient by default.

### Real-World Analogy

Range is like a **ticket dispenser machine**:
- Doesn't print all tickets upfront (memory waste!)
- Prints next ticket only when you press the button (on-demand)
- Knows the sequence (1, 2, 3...) but generates incrementally
- Can handle billions of tickets without running out of space

You get numbers one at a time, exactly when you need them.

### The Power of Lazy Evaluation

```python
# This doesn't create 1 billion numbers in memory!
for i in range(1000000000):
    if i == 5:
        break  # Exit early - only 6 numbers ever created
```

Range saves memory by generating values **just in time**. This is called **lazy evaluation** - a fundamental concept in efficient programming.

---

<div align="center">

![Python range() Function with for Loop](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.23.jpg)

*The range() function generates numbers on demand, enabling efficient numeric iteration without storing the entire sequence in memory*

</div>

---

## The Range Function

`range()` generates a sequence of numbers, commonly used with for loops.


### Three Forms

```python
range(stop)              # 0 to stop-1
range(start, stop)       # start to stop-1
range(start, stop, step) # start to stop-1, by step
```

## Examples

### Form 1: range(stop)

```python
for i in range(5):
    print(i)

# Output: 0 1 2 3 4 (stops before 5!)
```

### Form 2: range(start, stop)

```python
for i in range(2, 7):
    print(i)

# Output: 2 3 4 5 6 (stops before 7!)
```

### Form 3: range(start, stop, step)

```python
for i in range(0, 10, 2):
    print(i)

# Output: 0 2 4 6 8 (even numbers)
```

### Counting Down

```python
for i in range(5, 0, -1):
    print(i)

# Output: 5 4 3 2 1 (countdown)
```

## Real-World Applications

### Multiplication Table

```python
num = 5

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

### Year Range

```python
for year in range(2020, 2025):
    print(f"Year: {year}")

# Output: 2020 2021 2022 2023 2024
```

### Skip Every Third

```python
for i in range(0, 20, 3):
    print(i)

# Output: 0 3 6 9 12 15 18
```

## Range with Lists

```python
fruits = ["apple", "banana", "cherry"]

# Access by index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
```

## Key Takeaways

1. **Generates numbers**: Not a list, but a range object
2. **Stops before end**: range(5) goes 0 to 4, not 5
3. **Default start**: 0 if not specified
4. **Default step**: 1 if not specified
5. **Can count down**: Use negative step
