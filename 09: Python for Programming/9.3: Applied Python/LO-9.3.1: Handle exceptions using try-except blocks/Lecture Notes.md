## Lecture Notes: Handle Exceptions Using try-except Blocks


---

<div align="center">

![Python try-except-else-finally Block Diagram](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.1.png)

*Try-except follows an if-then-else pattern: if an error occurs, branch to the except handler*

</div>

---

## Introduction

Exception handling represents **structured error recovery** - one of the most important advances in programming language design! Before exceptions, programs used **error codes** (return values like -1 or NULL) which developers often forgot to check, leading to silent failures and cascading bugs. Exceptions implement **fail-fast principles**: errors are impossible to ignore, forcing explicit handling.

### Why Exception Handling is Revolutionary

**Before exceptions** (error codes): Silent failures, bugs propagate far from source:
```c
// C-style error handling - fragile!
int result = divide(10, 0);  // Returns -1 on error
// Forgot to check! Bug propagates...
int x = result + 5;  // Now x = 4, wrong answer!
```

**With exceptions** (Python): Errors crash loudly at the source:
```python
# Python exceptions - safe!
result = 10 / 0  # Crashes IMMEDIATELY at error site
# Cannot forget to handle - program stops!
```

**This is "fail-fast"** - errors detected early, not allowed to propagate. Better to crash than silently produce wrong results!

### Historical Context

**Exception mechanisms** invented by **PL/I** (IBM, 1964), formalized by **CLU** (Barbara Liskov, MIT, 1975). Python's try-except based on **Modula-3** (1980s) and **Java** (1995) which popularized checked exceptions.

**Python's EAFP philosophy**: "**Easier to Ask Forgiveness than Permission**" - try first, handle errors later. Contrasts with **LBYL** ("Look Before You Leap" - check first, act later). EAFP is more Pythonic!

**Evolution**: Python 2 had old-style exception syntax (`except ValueError, e`). Python 3 standardized on `except ValueError as e` - cleaner and less ambiguous.

### Real-World Analogies

**Exception handling like parachute**:
- **Try block**: Jump from plane (risky operation)
- **Except block**: Parachute opens if something goes wrong
- **No parachute**: Crash! (program termination)
- **With parachute**: Safe landing (graceful error recovery)

**Or like try-on at a store**:
- **Try**: Attempt to wear clothes
- **Fits**: Keep going (no exception)
- **Doesn't fit**: Return it (exception caught)
- **Store policy**: "Try before you buy" - EAFP philosophy!

**Or like medical diagnosis**:
```python
try:
    perform_surgery()  # Risky operation
except Complication as error:
    emergency_procedure(error)  # Have a backup plan
```
**Doctors don't assume surgery succeeds** - they prepare for complications!

### The Exception Hierarchy

**Python exceptions inherit from BaseException**:
```
BaseException
  ├── SystemExit (interpreter exit)
  ├── KeyboardInterrupt (Ctrl+C)
  └── Exception (this is what you catch!)
      ├── ValueError
      ├── TypeError
      ├── ZeroDivisionError
      ├── KeyError
      └── ... (60+ built-in types)
```

**Why hierarchy?** Catch specific errors or broader categories! Flexibility through inheritance.

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
