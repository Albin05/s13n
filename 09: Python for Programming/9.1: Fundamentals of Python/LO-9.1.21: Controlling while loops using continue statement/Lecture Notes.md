# Lecture Notes: Control While Loops with Continue

## Introduction

The `continue` statement provides a way to **skip the rest of the current iteration** and jump to the next one. Unlike `break` which exits entirely, `continue` says "skip this one, move to the next."

---

<div align="center">

![Python continue Statement Flow Diagram](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.21.png)

*The continue statement skips the remaining loop body and jumps back to the condition check for the next iteration*

</div>

---

### Why Continue Exists

Sometimes you want to process most items but skip certain ones:
- **Filter while processing**: Skip invalid entries but continue with others
- **Conditional skipping**: Ignore specific cases without stopping entirely
- **Cleaner logic**: Avoid deeply nested if statements

**Without continue**: Complex nested ifs. **With continue**: Clear, linear flow.

### Real-World Analogy

Continue is like **"skip this, next!"**:
- **Assembly line**: Defective item detected? Skip it, continue with next item (don't stop the whole line!)
- **Reading list**: Boring chapter? Skip it, continue reading
- **Playlist**: Don't like this song? Skip to next (don't stop playback)

It's selective skipping, not stopping.

## The Continue Statement

`continue` skips the rest of the current iteration and goes to the next one.


### Basic Syntax

```python
while condition:
    # Code
    if some_condition:
        continue  # Skip to next iteration
    # This code is skipped if continue runs
```

## Examples

### Example 1: Skip Even Numbers

```python
count = 0

while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)  # Only prints odd numbers

# Output: 1 3 5 7 9
```

### Example 2: Input Validation

```python
attempts = 0

while attempts < 5:
    age = int(input("Enter age: "))
    attempts += 1
    
    if age < 0:
        print("Invalid age!")
        continue  # Skip to next attempt
    
    print(f"Valid age: {age}")
    break
```

### Example 3: Filter Data

```python
count = 0
total = 0
num_count = 0

while count < 10:
    num = int(input("Enter number (negative to skip): "))
    count += 1
    
    if num < 0:
        continue  # Skip negative numbers
    
    total += num
    num_count += 1

average = total / num_count if num_count > 0 else 0
print(f"Average: {average}")
```

## Continue vs Break

```python
# continue - skips iteration
while count < 10:
    count += 1
    if count == 5:
        continue  # Skips printing 5
    print(count)

# break - exits loop
while count < 10:
    count += 1
    if count == 5:
        break  # Stops at 5
    print(count)
```

## Key Takeaways

1. **Skips to next**: continue jumps to next iteration
2. **Doesn't exit**: Loop continues running
3. **Use for filtering**: Skip unwanted items
4. **Update before continue**: Make sure loop variable updates
5. **Common with validation**: Skip invalid input
