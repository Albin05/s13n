# Pre-Read: Create Generator Functions

## Generator Functions

Generators create iterators using the `yield` keyword instead of `return`:

```python
# Regular function - returns a list
def get_numbers():
    return [1, 2, 3, 4, 5]

# Generator function - yields values one at a time
def generate_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# Using the generator
for num in generate_numbers():
    print(num)
# Output: 1, 2, 3, 4, 5 (one at a time)
```

## Memory Efficiency

Generators don't store all values in memory:

```python
# This creates a list in memory (inefficient for large ranges)
def get_range(n):
    result = []
    for i in range(n):
        result.append(i)
    return result

# This yields values one at a time (memory efficient)
def generate_range(n):
    for i in range(n):
        yield i

# Use the generator
for num in generate_range(1000000):
    # Process one number at a time
    pass
```

## Yield vs Return

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Create generator object
counter = countdown(5)
print(next(counter))  # 5
print(next(counter))  # 4
print(next(counter))  # 3
```
