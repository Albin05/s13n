# Lecture Notes: Control For Loops with Break and Continue

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
