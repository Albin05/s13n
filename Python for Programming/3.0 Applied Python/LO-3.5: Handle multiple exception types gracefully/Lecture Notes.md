# Lecture Notes: Handle Multiple Exception Types

## Handle Multiple Exception Types

Catching and handling different exception types


---

<div align="center">

![Different data types representation](https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80)

*Python supports multiple data types: integers, floats, strings, and booleans*

</div>

---
### Key Concepts

**Core principle**: except (TypeError, ValueError): ...

### Syntax and Usage

```python
# Basic example will be shown in practical examples below
```

### Practical Examples

#### Example 1: Multiple Except Blocks

```python
try:
    value = int(input("Enter number: "))
    result = 10 / value
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Unexpected error: {e}")
```

#### Example 2: Tuple of Exceptions

```python
try:
    # Code that might raise multiple exceptions
    data = {"key": "value"}
    result = int(data["missing_key"])
except (KeyError, ValueError, TypeError) as e:
    print(f"Data processing error: {e}")
```

#### Example 3: Exception Hierarchy

```python
def read_config(filename):
    try:
        with open(filename) as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print("Config file not found")
    except json.JSONDecodeError:
        print("Invalid JSON in config")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return {}
```

### Best Practices

1. Write clear, readable code
2. Handle errors appropriately
3. Follow Python conventions
4. Document your code
5. Test thoroughly

### Common Mistakes

1. Not handling edge cases
2. Overcomplicating simple tasks
3. Not following naming conventions

### Key Takeaways

1. Understanding the core concept is essential
2. Practice with real examples
3. Apply best practices
4. Avoid common pitfalls
5. Write clean, maintainable code
