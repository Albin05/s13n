# Lecture Notes: Control For Loops with Break and Continue

## Introduction

Break and continue introduce **flow interruption** to for loops - the ability to alter the normal sequential iteration based on conditions. These control statements make loops flexible and efficient by allowing **early exit** and **selective processing**.

### Why Flow Control Matters

**The efficiency problem**: Without break/continue, loops must run to completion even after finding what you need or encountering invalid data.
**Flow control solution**: Exit early (break) or skip items (continue), saving time and making logic cleaner.

**Real-world impact**: Google's search doesn't check all 50 billion web pages when you search - it uses break to stop once it finds enough good results. Your loop can do the same!

### Break vs Continue: Core Concepts

**Break**: "I found what I needed, stop the entire loop now"
- **Analogy**: Searching for keys in your house - once found, stop searching other rooms
- **Use case**: First match, error detection, early termination

**Continue**: "Skip this one item, but keep going through the rest"
- **Analogy**: Assembly line inspector - defective item? Skip it, inspect next one
- **Use case**: Filtering, ignoring special cases, validation

### The Power of Selective Iteration

Traditional approach requires processing everything:
```python
# Must check ALL items
for item in large_dataset:
    # Process even after finding what you need
```

With break/continue, you control flow intelligently:
```python
# Stop when done
for item in large_dataset:
    if found_target:
        break  # Save time!
```

This is **algorithmic efficiency** - doing less work to achieve the same goal.

## Break and Continue in For Loops

Both `break` and `continue` work in for loops just like while loops.


### Break in For Loop

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num == 6:
        break  # Stop at 6
    print(num)

# Output: 1 2 3 4 5
```

### Continue in For Loop

```python
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

# Output: 1 3 5 7 9
```

## Examples

### Find First Match

```python
names = ["Alice", "Bob", "Charlie", "David"]
target = "Charlie"

for i in range(len(names)):
    if names[i] == target:
        print(f"Found {target} at index {i}")
        break
```

### Filter While Iterating

```python
scores = [95, 45, 87, 32, 91, 68]

for score in scores:
    if score < 60:
        continue  # Skip failing scores
    print(f"Passing score: {score}")

# Output: Passing score: 95, 87, 91, 68
```

### Early Exit on Error

```python
data = [10, 20, 0, 40, 50]

for num in data:
    if num == 0:
        print("Error: Zero found!")
        break
    result = 100 / num
    print(f"100 / {num} = {result}")
```

## Nested Loops with Break

```python
# Break only exits innermost loop
for i in range(3):
    for j in range(3):
        if j == 2:
            break  # Exits inner loop only
        print(f"i={i}, j={j}")
```

## Key Takeaways

1. **break**: Exits for loop immediately
2. **continue**: Skips to next iteration
3. **Same as while**: Works identically
4. **Use break for**: Search, early exit
5. **Use continue for**: Filtering, skipping
