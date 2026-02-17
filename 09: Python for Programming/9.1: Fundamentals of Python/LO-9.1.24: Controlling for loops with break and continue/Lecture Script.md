### LO-24 Control For Loops with Break and Continue (20 minutes)


### CS Theory Bite

> **Origin**: `break` and `continue` in for loops enable **early termination optimization** — stop searching once found. This turns O(n) worst-case into O(1) best-case.
>
> **Analogy**: Like **searching a phone book** — once you find the name (break), you stop flipping pages. Or skip entries that aren't relevant (continue).
>
> **Why it matters**: Efficient loops don't do unnecessary work — `break` and `continue` are optimization tools.


### Hook (3 minutes)

**Say**: "Imagine you're looking for your keys in a messy room. You check drawer after drawer. What happens when you find them? You BREAK - stop searching. What if a drawer is locked? You CONTINUE - skip it and check the next one!"

```python
drawers = ["socks", "locked", "books", "keys", "clothes"]

for drawer in drawers:
    if drawer == "locked":
        print(f"Skipping {drawer}")
        continue  # Skip this one
    if drawer == "keys":
        print("Found keys!")
        break  # Stop searching!
    print(f"Checking {drawer}...")

# Output:
# Checking socks...
# Skipping locked
# Checking books...
# Found keys!
```

### The Break Statement (5 minutes)

**Say**: "break exits the loop immediately."

```python
for item in collection:
    if condition:
        break  # Exit loop NOW
    # This code runs only if break doesn't execute
```

**Example - Find first even number**:
```python
numbers = [1, 3, 5, 8, 9, 11, 13]

for num in numbers:
    if num % 2 == 0:
        print(f"Found first even: {num}")
        break
    print(f"Checking {num}...")

# Output:
# Checking 1...
# Checking 3...
# Checking 5...
# Found first even: 8
```

### The Continue Statement (5 minutes)

**Say**: "continue skips the rest of this iteration and moves to the next."

```python
for item in collection:
    if condition:
        continue  # Skip rest, go to next
    # This code is skipped when continue executes
```

**Example - Print only positive numbers**:
```python
numbers = [5, -2, 10, -7, 3, 8]

for num in numbers:
    if num < 0:
        continue  # Skip negatives
    print(num)

# Output: 5 10 3 8
```

### Break vs Continue (3 minutes)

```python
# BREAK - Exits the entire loop
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0 1 2

# CONTINUE - Skips to next iteration
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0 1 2 4 (3 is skipped!)
```

### The For-Else Clause (4 minutes)

**Say**: "else after a loop runs ONLY if break was never called!"

```python
for item in collection:
    if condition:
        break
else:
    # Runs if NO break occurred
    print("Loop completed normally")
```

**Example - Search with feedback**:
```python
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not in list")

# Output: 4 not in list
```

**Real-World - Prime number check**:
```python
number = 17

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime")
        break
else:
    print(f"{number} is prime!")
```
