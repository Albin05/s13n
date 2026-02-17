## Pre-Read: Handle Multiple Exception Types


---

## Introduction

**Multiple exception handling** lets you handle different error types differently - like a hospital triage system routing patients to appropriate specialists! One try block can have many except handlers, each catching specific error types. This is **polymorphic error handling**!

### Why Multiple Handlers Matter

**Problem**: Different errors need different responses:
```python
try:
    value = int(data[key][index])
# KeyError? IndexError? ValueError? Need different fixes!
```

**Solution**: Multiple except blocks catch different types:
```python
except KeyError:
    use_default_key()  # Fix missing key
except IndexError:
    use_default_index()  # Fix bad index
except ValueError:
    use_default_value()  # Fix type conversion
# Each error → appropriate handler!
```

**This is error polymorphism** - same try, different handlers!

### Critical Rule: Specific Before General

Python checks except blocks **top to bottom**, first match wins:
```python
# CORRECT - specific first
except FileNotFoundError:
    create_file()
except OSError:  # Catches other OS errors
    log_error()

# WRONG - general first
except OSError:  # Catches FileNotFoundError!
    log_error()
except FileNotFoundError:  # Never reached!
    create_file()
```

**Always specific → general!**

### Real-World Analogy

**Multiple exception handling like mail sorting**:
- **Local mail**: Local delivery (FileNotFoundError)
- **International**: Customs processing (PermissionError)
- **Undeliverable**: Return to sender (OSError catch-all)
**Different mail types → different handling!**

---

### Multiple Things Can Go Wrong

```python
data = {'scores': [85, 92, 0]}
value = data['grades'][5]  # Could fail with KeyError OR IndexError
```

---

### Handle Each Differently

```python
try:
    value = data[key][index]
except KeyError:
    print("Key not found")
except IndexError:
    print("Index out of range")
```

---

### Group Similar Errors

```python
try:
    result = process(data)
except (ValueError, TypeError):
    print("Input error")
```

---

### Full Structure

```python
try:
    result = compute()    # might fail
except SomeError:
    handle()              # if error
else:
    use(result)           # if success
finally:
    cleanup()             # always
```

---

### Key Rule

Put **specific** exceptions before **general** ones. Python checks top to bottom and stops at the first match.
