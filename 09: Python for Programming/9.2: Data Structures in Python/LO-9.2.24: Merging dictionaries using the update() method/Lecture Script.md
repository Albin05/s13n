## Lecture Script: Merging Dictionaries Using update()


---

### CS Theory Bite

> **Origin**: `update()` merges dicts — later values overwrite earlier ones. **Python 3.9+** added the `|` merge operator: `merged = dict1 | dict2` — cleaner syntax inspired by set union.
>
> **Analogy**: `update()` is like **merging two address books** — if both have "Alice", the newer entry wins.
>
> **Why it matters**: Dict merging is essential for combining configuration, API responses, and default + custom settings.



### Hook (2 minutes)

Your app has a layered configuration:

```python
defaults = {'debug': False, 'port': 3000, 'host': 'localhost'}
# User says: "I want port 8080 and debug on"
user = {'port': 8080, 'debug': True}
```

How do you combine them, with user preferences overriding defaults?

```python
config = {**defaults, **user}
print(config)  # {'debug': True, 'port': 8080, 'host': 'localhost'}
```

One line. User preferences win. Defaults fill in the gaps. This is dictionary merging.

---

### Section 1: update() Basics (3 minutes)

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 30}

d1.update(d2)
print(d1)  # {'a': 1, 'b': 20, 'c': 30}
# d2 values override d1 for shared keys
# d2 is unchanged
```

`update()` can also take keyword args:
```python
d1.update(x=100, y=200)
```

Or tuples:
```python
d1.update([('m', 10), ('n', 20)])
```

---

### Section 2: Creating New Merged Dicts (3 minutes)

`update()` modifies in place. To create a new dict:

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 30}

# Unpacking
merged = {**d1, **d2}
print(merged)  # {'a': 1, 'b': 20, 'c': 30}
print(d1)      # {'a': 1, 'b': 2} — unchanged!

# | operator (Python 3.9+)
merged = d1 | d2  # same result
```

---

### Section 3: Merge Priority (2 minutes)

Later dicts override earlier ones:

```python
layer1 = {'x': 1, 'y': 2}
layer2 = {'y': 20, 'z': 30}
layer3 = {'z': 300}

result = {**layer1, **layer2, **layer3}
print(result)  # {'x': 1, 'y': 20, 'z': 300}
```

To reverse priority, reverse the order:
```python
result = {**layer3, **layer2, **layer1}
# layer1 wins for shared keys
```

---

### Section 4: Practical Applications (3 minutes)

**Config layering:**
```python
final = {**defaults, **env_config, **cli_args}
```

**Template system:**
```python
base_style = {'font': 'Arial', 'size': 12, 'color': 'black'}
heading = {**base_style, 'size': 24, 'bold': True}
```

**Custom merge logic:**
```python
def merge_sum(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result
```

---

### Section 5: Pitfalls (1 minute)

**Shallow merge only:**
```python
d1 = {'settings': {'theme': 'dark', 'lang': 'en'}}
d2 = {'settings': {'theme': 'light'}}

merged = {**d1, **d2}
print(merged)  # {'settings': {'theme': 'light'}}
# 'lang' is LOST! Nested dicts are replaced, not merged
```

For deep merging, you need a custom function or a library.

---

### Summary (1 minute)

1. `d1.update(d2)` — merge in place, d2 wins for shared keys
2. `{**d1, **d2}` — new dict, d2 wins
3. Order determines priority — last one wins
4. Merging is **shallow** — nested dicts are replaced, not merged
5. For custom logic (sum, max, lists), write a merge function
