# Pre-Read: Using Range() Function for Numeric Iteration

## What You'll Learn
In this lesson, you'll learn how to use Python's `range()` function to generate sequences of numbers for use in for loops. This is essential for when you need to repeat code a specific number of times or iterate over numbers.

## Why This Matters
The `range()` function is one of the most commonly used tools in Python:
- Repeat an action N times ("do this 10 times")
- Count from 1 to 100
- Generate even/odd numbers
- Create countdowns
- Access list elements by index

---

## What is range()?

`range()` generates a sequence of numbers. It doesn't create a list in memory - it generates numbers on-demand, which is efficient.

### Three Ways to Use range()

**1. range(stop)** - Count from 0 to stop-1

```python
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4 (stops before 5!)
```

**2. range(start, stop)** - Count from start to stop-1

```python
for i in range(2, 6):
    print(i)
# Output: 2, 3, 4, 5 (stops before 6!)
```

**3. range(start, stop, step)** - Count with custom increment

```python
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8 (every 2nd number)
```

---

## Important: range() Stops BEFORE the End

The stop value is **exclusive** (not included):

```python
range(5)      # 0, 1, 2, 3, 4 (NOT 5!)
range(1, 4)   # 1, 2, 3 (NOT 4!)
range(0, 10, 2) # 0, 2, 4, 6, 8 (NOT 10!)
```

**Why?** This makes it easier to work with list indices, which start at 0.

---

## Common Patterns

### Pattern 1: Repeat N Times

```python
# Print "Hello" 5 times
for i in range(5):
    print("Hello")
```

### Pattern 2: Count from 1 to N

```python
# Count 1 to 10
for i in range(1, 11):  # Note: 11, not 10!
    print(i)
```

### Pattern 3: Even Numbers

```python
# Print even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)
# Output: 0, 2, 4, 6, 8, 10
```

### Pattern 4: Countdown

```python
# Countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)
print("Blast off!")
```

---

## Real-World Examples

### Example 1: Multiplication Table

```python
number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

### Example 2: Access List by Index

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(f"Item {i}: {fruits[i]}")
# Output:
# Item 0: apple
# Item 1: banana
# Item 2: cherry
```

### Example 3: Sum of First N Numbers

```python
n = 10
total = 0

for i in range(1, n + 1):
    total += i

print(f"Sum of first {n} numbers: {total}")
# Sum of first 10 numbers: 55
```

---

## Try It Yourself (Before Class)

Run this code:

```python
for i in range(1, 6):
    print("*" * i)
```

**Questions:**
1. What pattern does this create?
2. Try changing `range(1, 6)` to `range(5, 0, -1)` - what happens?
3. Change `"*" * i` to `str(i) * i` - what do you get?

---

## Key Takeaways

Before class, remember:
1. **range(n)** - 0 to n-1
2. **range(start, stop)** - start to stop-1
3. **range(start, stop, step)** - custom increment
4. **Stop is exclusive** - never includes the stop value
5. **Efficient** - doesn't create a list in memory

## What's Next?

In the live session, we'll:
- Practice all three forms of range()
- Use range() to solve real problems
- Combine range() with lists and other data structures
- Learn advanced range() techniques

See you in class!
