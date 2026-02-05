## Lecture Notes: Handle Exceptions Using try-except Blocks

**Duration:** 12 minutes

---

### What Are Exceptions?

An **exception** is an error that occurs during program execution. Without handling, it crashes the program.

```python
# This crashes!
number = int("hello")  # ValueError: invalid literal for int()
```

```python
result = 10 / 0  # ZeroDivisionError: division by zero
```

---

### The try-except Block

Wrap risky code in `try`, handle the error in `except`:

```python
try:
    number = int("hello")
except ValueError:
    print("That's not a valid number!")
# Program continues running
print("This still executes")
```

**Structure:**
```python
try:
    # Code that might fail
    risky_operation()
except SomeError:
    # Code that runs if that error occurs
    handle_error()
```

---

### Common Exception Types

```python
# ValueError — wrong type of value
int("abc")

# TypeError — wrong type for operation  
"hello" + 5

# ZeroDivisionError — dividing by zero
10 / 0

# IndexError — list index out of range
[1, 2, 3][10]

# KeyError — dictionary key not found
{'a': 1}['b']

# FileNotFoundError — file doesn't exist
open("nonexistent.txt")

# NameError — variable not defined
print(undefined_var)
```

---

### Catching Specific Exceptions

Always catch specific exceptions when possible:

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

### Catching Multiple Exceptions Together

```python
try:
    data = [1, 2, 3]
    index = int(input("Enter index: "))
    print(data[index])
except (ValueError, IndexError) as e:
    print(f"Error: {e}")
```

---

### The Generic except (Use Sparingly)

```python
try:
    result = risky_operation()
except Exception as e:
    print(f"Something went wrong: {e}")
```

**Warning:** Catching all exceptions hides bugs. Use specific exceptions when you know what to expect.

---

### The `as` Keyword — Getting Error Details

```python
try:
    number = int("abc")
except ValueError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
# Error type: ValueError
# Error message: invalid literal for int() with base 10: 'abc'
```

---

### The else Block

Runs only if **no exception** occurred:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Not a valid number")
else:
    print(f"You entered: {number}")
    print(f"Squared: {number ** 2}")
```

---

### Practical Examples

**1. Safe User Input:**
```python
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer")

age = get_integer("Enter your age: ")
```

**2. Safe Division:**
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None

print(safe_divide(10, 3))    # 3.333...
print(safe_divide(10, 0))    # None
print(safe_divide("a", 2))   # None
```

**3. Safe List Access:**
```python
def safe_get(lst, index, default=None):
    try:
        return lst[index]
    except (IndexError, TypeError):
        return default

data = [10, 20, 30]
print(safe_get(data, 1))     # 20
print(safe_get(data, 10))    # None
print(safe_get(data, "a"))   # None
```

**4. Safe Dictionary Access:**
```python
config = {'port': 8080}
try:
    host = config['host']
except KeyError:
    host = 'localhost'
print(host)  # localhost
```

---

### Key Takeaways

1. Use `try-except` to handle errors without crashing
2. Catch **specific** exception types — don't catch everything
3. Use `as e` to get error details
4. Use `else` for code that should run only when no error occurs
5. Common exceptions: `ValueError`, `TypeError`, `ZeroDivisionError`, `KeyError`, `IndexError`
