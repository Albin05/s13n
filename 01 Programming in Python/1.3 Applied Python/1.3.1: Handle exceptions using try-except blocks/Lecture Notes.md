# Lecture Notes: Handle Exceptions with Try-Except

## Exception Handling

Handle errors gracefully using try-except blocks.


---

<div align="center">

![Error handling and debugging](https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=800&q=80)

*Exception handling prevents your program from crashing on errors*

</div>

---
### Basic Syntax

```python
try:
    # Code that might cause an error
except ExceptionType:
    # Code to run if error occurs
```

## Common Examples

### Example 1: Handle ValueError

```python
try:
    age = int(input("Enter age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number!")
```

### Example 2: Division by Zero

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Example 3: File Not Found

```python
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
```

## Why Use Try-Except?

1. **Prevent crashes**: Program continues running
2. **User-friendly**: Show helpful error messages
3. **Robust**: Handle unexpected input
4. **Graceful degradation**: Provide alternatives

## Catching Multiple Exceptions

```python
try:
    num = int(input("Enter number: "))
    result = 100 / num
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Generic Exception Handler

```python
try:
    # Risky code
except Exception as e:
    print(f"An error occurred: {e}")
```

## Key Takeaways

1. **try-except**: Handle potential errors
2. **Specific exceptions**: Catch specific error types
3. **Prevents crashes**: Program continues
4. **User experience**: Better error messages
5. **Production code**: Essential for robust applications
