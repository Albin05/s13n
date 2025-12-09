# Pre-Read: Handle Exceptions with Try-Except

## What are Exceptions?

Errors that occur during program execution.

```python
number = int("abc")  # ValueError!
```

## Try-Except Blocks

Handle errors gracefully:

```python
try:
    number = int("abc")
except ValueError:
    print("Invalid number!")
# Output: Invalid number!
```

## Why Use Try-Except?

1. **Prevent crashes**: Keep program running
2. **User-friendly**: Show helpful messages
3. **Robust code**: Handle unexpected input

## Basic Example

```python
try:
    age = int(input("Enter age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a number!")
```
