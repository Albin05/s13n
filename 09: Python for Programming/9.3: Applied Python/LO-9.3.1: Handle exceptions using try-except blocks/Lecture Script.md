## Lecture Script: Handle Exceptions Using try-except Blocks

**Duration:** 15 minutes

---

### Hook (2 minutes)

You build a calculator app. A user types "abc" instead of a number:

```python
num = int(input("Enter number: "))  # User types "abc"
# CRASH: ValueError: invalid literal for int() with base 10: 'abc'
```

Your entire app dies. Users hate this. The fix?

```python
try:
    num = int(input("Enter number: "))
except ValueError:
    print("That's not a number! Try again.")
```

No crash. Graceful message. Professional software. That's exception handling.

---

### Section 1: Why Exceptions Exist (2 minutes)

Things go wrong at runtime:
- Users enter bad input
- Files don't exist
- Networks fail
- Math goes wrong (divide by zero)

Python signals these with **exceptions** — objects that describe what went wrong.

```python
int("hello")      # ValueError
10 / 0            # ZeroDivisionError
[1,2,3][99]       # IndexError
{'a':1}['b']      # KeyError
open("nope.txt")  # FileNotFoundError
```

---

### Section 2: Basic try-except (3 minutes)

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
print("Program continues!")  # This runs!
```

Without try-except, the program would crash at `10/0`.

**Multiple except blocks:**
```python
try:
    val = int(input("Number: "))
    result = 100 / val
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print("Can't use zero!")
```

---

### Section 3: Getting Error Details (2 minutes)

```python
try:
    x = int("abc")
except ValueError as e:
    print(f"Error: {e}")
    print(f"Type: {type(e).__name__}")
```

The `as e` captures the exception object — useful for logging and debugging.

---

### Section 4: The else Block (2 minutes)

```python
try:
    num = int(input("Number: "))
except ValueError:
    print("Invalid!")
else:
    # Only runs if NO exception occurred
    print(f"Square: {num ** 2}")
```

`else` keeps the "happy path" code separate from error-prone code.

---

### Section 5: Practical Pattern (3 minutes)

**Retry loop:**
```python
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid. Try again.")

age = get_integer("Age: ")
```

**Safe dictionary access:**
```python
try:
    value = data[key]
except KeyError:
    value = default
# Equivalent to: value = data.get(key, default)
```

---

### Summary (1 minute)

1. `try` wraps code that might fail
2. `except SpecificError` handles that error
3. `as e` captures error details
4. `else` runs when no error occurs
5. Always catch specific exceptions, not bare `except`
