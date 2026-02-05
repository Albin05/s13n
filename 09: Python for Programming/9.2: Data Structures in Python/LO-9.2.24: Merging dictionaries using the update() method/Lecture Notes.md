## Lecture Notes: Merging Dictionaries Using the update() Method

**Duration:** 10 minutes

---

### The `update()` Method

Merges another dictionary (or key-value pairs) into the current dictionary:

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

d1.update(d2)
print(d1)  # {'a': 1, 'b': 3, 'c': 4}
```

**Behavior:**
- New keys are **added**
- Existing keys are **overwritten** (last value wins)
- `d1` is modified in place; `d2` is unchanged

---

### Different Ways to Call `update()`

**1. With another dictionary:**
```python
base = {'host': 'localhost', 'port': 3000}
base.update({'port': 8080, 'debug': True})
print(base)  # {'host': 'localhost', 'port': 8080, 'debug': True}
```

**2. With keyword arguments:**
```python
config = {'theme': 'light'}
config.update(font_size=14, language='en')
print(config)  # {'theme': 'light', 'font_size': 14, 'language': 'en'}
```

**3. With a list of tuples:**
```python
data = {}
data.update([('name', 'Alice'), ('age', 25)])
print(data)  # {'name': 'Alice', 'age': 25}
```

---

### Merging Without Modifying Originals

**Using `{**d1, **d2}` unpacking (Python 3.5+):**
```python
defaults = {'theme': 'light', 'lang': 'en', 'font': 14}
user_prefs = {'theme': 'dark', 'font': 18}

merged = {**defaults, **user_prefs}
print(merged)   # {'theme': 'dark', 'lang': 'en', 'font': 18}
print(defaults) # unchanged
print(user_prefs) # unchanged
```

**Using `|` operator (Python 3.9+):**
```python
merged = defaults | user_prefs
print(merged)  # {'theme': 'dark', 'lang': 'en', 'font': 18}
```

**Using `|=` for in-place merge (Python 3.9+):**
```python
defaults |= user_prefs  # modifies defaults
```

---

### Merge Priority (Who Wins?)

The **later** dictionary's values take priority:

```python
d1 = {'x': 1, 'y': 2}
d2 = {'y': 20, 'z': 30}

# d2 overrides d1 for shared keys
merged = {**d1, **d2}
print(merged)  # {'x': 1, 'y': 20, 'z': 30}

# d1 overrides d2 for shared keys
merged = {**d2, **d1}
print(merged)  # {'y': 2, 'z': 30, 'x': 1}
```

---

### Merging Multiple Dictionaries

```python
base = {'a': 1}
overrides1 = {'b': 2, 'a': 10}
overrides2 = {'c': 3, 'b': 20}

# Last one wins for overlapping keys
result = {**base, **overrides1, **overrides2}
print(result)  # {'a': 10, 'b': 20, 'c': 3}

# Or with update (sequential)
final = {}
final.update(base)
final.update(overrides1)
final.update(overrides2)
print(final)  # same result
```

---

### Practical Examples

**1. Configuration Layering:**
```python
# Default < Environment < Command Line
default_config = {'debug': False, 'port': 3000, 'host': 'localhost', 'log': 'info'}
env_config = {'port': 8080, 'log': 'debug'}
cli_config = {'debug': True}

final_config = {**default_config, **env_config, **cli_config}
print(final_config)
# {'debug': True, 'port': 8080, 'host': 'localhost', 'log': 'debug'}
```

**2. Combining API Responses:**
```python
user_basic = {'id': 42, 'name': 'Alice'}
user_profile = {'bio': 'Developer', 'avatar': 'alice.png'}
user_settings = {'theme': 'dark', 'notifications': True}

full_user = {**user_basic, **user_profile, **user_settings}
```

**3. Template with Overrides:**
```python
template = {'font': 'Arial', 'size': 12, 'color': 'black', 'bold': False}

heading_style = {**template, 'size': 24, 'bold': True}
subtitle_style = {**template, 'size': 18, 'color': 'gray'}

print(heading_style)
# {'font': 'Arial', 'size': 24, 'color': 'black', 'bold': True}
```

**4. Merging with Conditional Logic:**
```python
def merge_keep_higher(d1, d2):
    """Merge dicts, keeping the higher value for shared keys."""
    result = d1.copy()
    for key, val in d2.items():
        if key in result:
            result[key] = max(result[key], val)
        else:
            result[key] = val
    return result

scores_round1 = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
scores_round2 = {'Alice': 90, 'Bob': 88, 'Diana': 95}

best_scores = merge_keep_higher(scores_round1, scores_round2)
print(best_scores)
# {'Alice': 90, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
```

---

### Comparison Table

| Method | Modifies Original? | Python Version |
|--------|-------------------|----------------|
| `d1.update(d2)` | Yes | All |
| `{**d1, **d2}` | No (new dict) | 3.5+ |
| `d1 \| d2` | No (new dict) | 3.9+ |
| `d1 \|= d2` | Yes | 3.9+ |

---

### Key Takeaways

1. `update()` merges another dict into the current one (in place)
2. Later values overwrite earlier ones for shared keys
3. `{**d1, **d2}` creates a new merged dict without modifying originals
4. `|` and `|=` are clean syntax for merging (Python 3.9+)
5. Layered configs: defaults → environment → user → cli
6. For custom merge logic (keep max, combine lists), write a function
