# Lecture Notes: Write For Loops

## Introduction

For loops introduce **iteration over collections** - the ability to process each item in a sequence automatically. This is one of Python's most elegant features, making data processing intuitive and concise.

### Why For Loops Are Revolutionary

**The problem with while loops**: Need manual counter management, index tracking, condition checking.
**For loops solution**: "For each item in this collection, do something" - natural, readable, Pythonic.

**Historical note**: Early languages (FORTRAN, 1957) had basic for loops. Python's for loop (1991) improved on this by iterating directly over collections, not just numbers - a game-changer for readability.

### Real-World Analogy

For loops are like **"for each" instructions**:
- "For each student in the class, mark attendance"
- "For each email in inbox, check if spam"
- "For each item in cart, calculate price"

You process the entire collection, one item at a time, automatically.

## For Loops

A for loop iterates over a sequence (list, string, range, etc.).


### Basic Syntax

```python
for item in sequence:
    # Code using item
```

## Examples

### Example 1: Iterate String

```python
name = "Alice"

for letter in name:
    print(letter)

# Output: A l i c e (each on new line)
```

### Example 2: Iterate List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

### Example 3: Count Using Range

```python
for i in range(5):
    print(i)

# Output: 0 1 2 3 4
```

### Example 4: Sum Numbers

```python
numbers = [10, 20, 30, 40]
total = 0

for num in numbers:
    total += num

print(f"Total: {total}")  # 100
```

## For Loop vs While Loop

```python
# For loop - when you know iterations
for i in range(5):
    print(i)

# While loop - when condition-based
count = 0
while count < 5:
    print(count)
    count += 1
```

## Real-World Applications

### Validate All Inputs

```python
scores = [85, 92, 78, 95, 88]
all_passing = True

for score in scores:
    if score < 60:
        all_passing = False
        break

if all_passing:
    print("Everyone passed!")
```

### Process Each Item

```python
prices = [19.99, 29.99, 39.99]
tax_rate = 0.08

for price in prices:
    final_price = price * (1 + tax_rate)
    print(f"${price} -> ${final_price:.2f}")
```

## Key Takeaways

1. **Iterates sequences**: Works with lists, strings, ranges
2. **Automatic**: No manual counter needed
3. **Cleaner than while**: For known iterations
4. **item variable**: Automatically gets next value
5. **Use when**: You know what to iterate over
