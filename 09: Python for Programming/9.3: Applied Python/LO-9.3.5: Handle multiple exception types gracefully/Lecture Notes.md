## Lecture Notes: Handle Multiple Exception Types Gracefully


---

<div align="center">

![Python Multiple except Clauses Handling](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.5.png)

*Handling multiple exception types creates multiple conditional branches, each catching a specific error*

</div>

---

## Introduction

Handling multiple exceptions implements **exception polymorphism** - different error types handled differently based on inheritance hierarchies. This solves the **error granularity problem**: catch specific errors for specific handling, or catch broad categories for generic handling. **Exception hierarchies** enable this flexibility!

### Why Multiple Exception Handling Matters

**Before exception hierarchies** (single catch): All errors handled the same:
```c
// C-style - all errors treated equally!
if (error_occurred) {
    handle_error();  // Same handler for everything!
}
```

**With exception hierarchies** (polymorphic): Each error type handled appropriately:
```python
# Python - specific handlers for specific errors!
try:
    operation()
except ValueError:
    fix_value_error()  # Specific handler
except TypeError:
    fix_type_error()  # Different handler
except Exception:
    log_unexpected()  # Catch-all
```

**This is "polymorphic error handling"** - one try block, many handlers!

### Historical Context

**Multiple exception handlers** from **CLU** (Barbara Liskov, 1975) which allowed multiple `except` clauses. Refined by **Modula-3** (1980s) and **Java** (1995) which formalized exception hierarchies.

**Python's exception hierarchy** inherited from **object-oriented design**: exceptions are classes, catching uses isinstance() checks, inheritance enables catching parent classes. **Liskov Substitution Principle** applies to exceptions!

**Design evolution**: Python 2 allowed `except ValueError, TypeError:` (ambiguous). Python 3 requires `except (ValueError, TypeError):` (explicit tuple) - prevents bugs from comma confusion!

### Real-World Analogies

**Multiple exception handling like hospital triage**:
- **Minor injury**: First aid (ValueError handler)
- **Major injury**: Surgery (TypeError handler)
- **Unknown condition**: General care (Exception handler)
- **Triage**: Route patients to appropriate care!
**Different problems → different specialists!**

**Or like emergency services dispatcher**:
```python
try:
    emergency_call()
except FireEmergency:
    dispatch_fire_truck()
except MedicalEmergency:
    dispatch_ambulance()
except PoliceEmergency:
    dispatch_police()
except Emergency:
    dispatch_general_response()
# Route each emergency to right service!
```

**Or like mail sorting facility**:
- **Local mail**: Local delivery (specific exception)
- **Express mail**: Express service (specific exception)
- **International**: International processing (specific exception)
- **Unknown**: Dead letter office (catch-all)
**Sort by specificity, handle appropriately!**

### The Specificity-to-Generality Gradient

**Critical rule**: Specific exceptions BEFORE general ones!
```python
# CORRECT - specific to general
try:
    file = open("data.txt")
except FileNotFoundError:
    # Most specific
    create_default_file()
except PermissionError:
    # Still specific
    request_permission()
except OSError:
    # General (catches all OS errors)
    log_os_error()
except Exception:
    # Most general
    log_unexpected()
```

**Why?** Python checks top-to-bottom, first match wins! If general exception first, specific ones never reached - **unreachable code**!

---

### Multiple except Blocks

Handle each exception type differently:

```python
def process_input(data, index):
    try:
        value = int(data[index])
        result = 100 / value
        return result
    except IndexError:
        print(f"Index {index} out of range")
    except ValueError:
        print(f"Cannot convert '{data[index]}' to integer")
    except ZeroDivisionError:
        print("Cannot divide by zero")
```

Python checks each `except` in order. The first matching one runs.

---

### Catching Multiple Types Together

When you want the same handler for several exceptions:

```python
try:
    result = process(data)
except (ValueError, TypeError, KeyError) as e:
    print(f"Input error: {e}")
except (IOError, OSError) as e:
    print(f"System error: {e}")
```

---

### Exception Hierarchy Matters

Python exceptions form a hierarchy. Catching a parent catches all children:

```python
# OSError is parent of FileNotFoundError, PermissionError, etc.
try:
    f = open("secret.txt")
except FileNotFoundError:
    print("File doesn't exist")
except PermissionError:
    print("No permission")
except OSError:
    print("Other OS error")  # catches remaining OSError subtypes
```

**Order matters:** specific exceptions first, general ones last.

```python
# WRONG — OSError catches everything, others never run
try:
    f = open("file.txt")
except OSError:
    print("OS error")        # Catches FileNotFoundError too!
except FileNotFoundError:
    print("Not found")       # NEVER reached
```

---

### The Exception Base Class

`Exception` catches almost everything:

```python
try:
    risky_operation()
except ValueError:
    handle_value_error()
except TypeError:
    handle_type_error()
except Exception as e:
    # Catches any remaining exception
    print(f"Unexpected error: {type(e).__name__}: {e}")
```

---

### try-except-else-finally

The complete structure:

```python
try:
    result = operation()      # Might fail
except SpecificError:
    handle_error()            # Runs if that error occurs
else:
    use_result(result)        # Runs only if NO error
finally:
    cleanup()                 # ALWAYS runs
```

Example:
```python
def read_config(filename):
    try:
        f = open(filename)
    except FileNotFoundError:
        print(f"Config not found, using defaults")
        return {}
    else:
        import json
        config = json.load(f)
        return config
    finally:
        print("Config loading complete")
```

---

### Practical Examples

**1. Robust Data Processor:**
```python
def safe_process(records):
    results = []
    errors = []
    for i, record in enumerate(records):
        try:
            name = record['name']
            score = float(record['score'])
            results.append((name, score))
        except KeyError as e:
            errors.append(f"Record {i}: missing key {e}")
        except (ValueError, TypeError) as e:
            errors.append(f"Record {i}: {e}")
    return results, errors
```

**2. Multi-Source Data Loader:**
```python
def load_data(sources):
    for source in sources:
        try:
            if source.endswith('.json'):
                return load_json(source)
            elif source.endswith('.csv'):
                return load_csv(source)
        except FileNotFoundError:
            continue
        except (json.JSONDecodeError, csv.Error) as e:
            print(f"Error in {source}: {e}")
            continue
    raise FileNotFoundError("No valid data source found")
```

---

### Key Takeaways

1. List specific exceptions before general ones
2. Group related exceptions with `(ExcA, ExcB)`
3. Use `as e` to access error details
4. `else` runs when no exception occurs
5. `finally` always runs — for cleanup
6. Catch `Exception` as a last resort, not as a first choice
