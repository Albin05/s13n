## Pre-Read: Handle Multiple Exception Types

**Duration:** 5 minutes

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
