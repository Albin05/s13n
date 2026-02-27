# Lecture Notes: Control While Loops with Break

## Introduction

The `break` statement provides an **emergency exit** from loops - a way to stop immediately when a special condition is met, regardless of the loop's normal condition.

---

<div align="center">

![Python break Statement Flowchart](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.20.png)

*The break statement exits the loop immediately — jumping straight past the loop body to the next statement*

</div>

---

### Why Break Exists

Sometimes you need to exit a loop for reasons other than the main condition:
- **Search**: Stop when item is found (don't check remaining items)
- **Validation**: Stop on first error (don't keep validating)
- **User quit**: Stop immediately when user says "quit"

Without break, you'd need complex condition logic. With break, it's simple and clear.

### Real-World Analogy

Break is like **"stop the search!"**:
- Looking for keys: Check pockets one by one. **Found them? BREAK - stop searching!**
- Reading a book: **Find the answer? BREAK - stop reading!**
- Fire alarm: **Alarm sounds? BREAK - stop everything, evacuate!**

It's an immediate exit when something important happens.

## The Break Statement

`break` immediately exits the current loop, regardless of the loop condition.


### Basic Syntax

```python
while condition:
    # Code
    if some_condition:
        break  # Exit loop immediately
    # More code
```

## Examples

### Example 1: Search and Stop

```python
numbers = [3, 7, 2, 9, 5]
target = 9
index = 0

while index < len(numbers):
    if numbers[index] == target:
        print(f"Found {target} at index {index}")
        break  # Stop searching
    index += 1
```

### Example 2: Exit on Command

```python
while True:
    command = input("Enter command (or 'quit'): ")
    if command == "quit":
        break
    print(f"Executing: {command}")

print("Program ended")
```

### Example 3: Limit Attempts

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == "secret":
        print("Access granted!")
        break
    attempts += 1
    print(f"Wrong! {max_attempts - attempts} attempts left")
else:
    print("Account locked")
```

## Break vs Condition

```python
# Using break
while True:
    x = int(input("Enter number (0 to stop): "))
    if x == 0:
        break
    print(f"You entered: {x}")

# Using condition
x = -1
while x != 0:
    x = int(input("Enter number (0 to stop): "))
    if x != 0:
        print(f"You entered: {x}")
```

## Key Takeaways

1. **Immediate exit**: break stops loop instantly
2. **Skips condition**: Doesn't check loop condition
3. **Use for early exit**: When you find what you need
4. **Works in while and for**: break works in both loop types
5. **One loop only**: Only exits innermost loop (in nested loops)
