# Lecture Notes: Control While Loops with Break

## The Break Statement

`break` immediately exits the current loop, regardless of the loop condition.


---

<div align="center">

![Circular pattern representing loops](https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800&q=80)

*Loops allow you to repeat operations efficiently*

</div>

---
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
