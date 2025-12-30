## Pre-Read: Creating and Initializing Sets

Sets store unique values only. Duplicates automatically removed.

```python
numbers = {1, 2, 3, 2, 1}
print(numbers)  # {1, 2, 3}
```

**Create sets:**
- `{1, 2, 3}` - literal
- `set([1, 2, 3])` - from list
- `set()` - empty (NOT `{}`)

**Remove duplicates:**
```python
data = [1, 2, 2, 3]
unique = set(data)  # {1, 2, 3}
```
