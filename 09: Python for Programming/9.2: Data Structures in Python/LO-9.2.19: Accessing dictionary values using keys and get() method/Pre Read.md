## Pre-Read: Accessing Dictionary Values

**Duration:** 5 minutes

---

## What's the Difference Between `[]` and `.get()`?

These are Python's **"crash vs. continue"** methods - one throws an error if key is missing (strict!), the other gives you a default value (friendly!).

### Simple Analogy

**Using `[]` like strict password system**:
- **Right password**: "Welcome!"
- **Wrong password**: "ERROR! Access denied!" 💥 (program crashes)
- **No second chances**: Must be exact
- **Use when**: Data MUST exist (critical settings)

**Using `.get()` like voice assistant**:
- **Ask for timer**: "Timer is 5 minutes!"
- **Ask for unknown**: "I don't have that. Want the default?"
- **Helpful**: Gives fallback automatically
- **Use when**: Data might be missing (user preferences)

### The "Missing Key" Problem

**Scenario**: User settings where some fields might not exist yet.

**Using `[]` (crashes!):**
```python
settings = {'theme': 'dark'}

# This works:
theme = settings['theme']  # 'dark'

# This crashes!
font_size = settings['font_size']  # KeyError! 💥
# Your program just died!
```

**Using `.get()` (safe!):**
```python
settings = {'theme': 'dark'}

# Both work:
theme = settings.get('theme', 'light')      # 'dark' (exists)
font_size = settings.get('font_size', 14)   # 14 (default!)
# No crashes! Program continues!
```

### When to Use Which?

**Use `[]` when**:
- Key is **guaranteed** to exist
- Missing key = **bug in your code** → crash is good!
- Example: `required_config['database_url']`

**Use `.get()` when**:
- Key **might not** exist
- Missing key = **normal** → use default instead
- Example: `user_prefs.get('language', 'en')`

**Golden rule**: If you'd write `if key in dict:` before accessing, just use `.get()` instead!

---

### Two Ways to Access Values

```python
student = {'name': 'Alice', 'age': 22}

# Way 1: Square brackets — errors if key missing
print(student['name'])  # Alice

# Way 2: .get() — returns None if key missing
print(student.get('name'))    # Alice
print(student.get('email'))   # None (no error!)
print(student.get('email', 'N/A'))  # N/A (custom default)
```

---

### The Problem with `[]`

```python
data = {'x': 10}
# print(data['y'])  # KeyError: 'y' — CRASH!
```

---

### The Solution: `.get()`

```python
data = {'x': 10}
print(data.get('y', 0))  # 0 — safe!
```

---

### Quick Exercise

```python
config = {'port': 8080}

# What does each print?
print(config.get('port', 3000))     # ?
print(config.get('host', 'localhost'))  # ?
```

**Answers:** `8080` (key exists, uses actual value), `localhost` (key missing, uses default)
