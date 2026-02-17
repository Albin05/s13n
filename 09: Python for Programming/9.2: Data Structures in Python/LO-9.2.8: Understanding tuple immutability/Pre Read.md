## Pre-Read: Understanding Tuple Immutability

## What Is Immutability?

Immutability means **"frozen forever"** - once created, cannot be changed. It's like writing in permanent ink vs. pencil!

### Simple Analogy

Think of immutability like **printed photos vs. digital photos**:
- **Digital** (list): Edit, crop, filter, delete anytime
- **Printed** (tuple): Once developed, permanent!
- **Why permanent**: Some moments should stay exactly as captured

Or like **tattoo vs. temporary tattoo**:
- **Temporary** (list): Washes off, can change
- **Permanent** (tuple): There forever!
- **Choose wisely**: Use permanent for data that shouldn't change

### The Safety Guarantee

Immutability is Python's way of saying **"I promise this won't change unexpectedly"**:
```python
config = ('production_server', 5432, 'maindb')
# Pass to 100 functions - stays safe!
# No function can accidentally break it
```

**Like a sealed time capsule** - contents protected from tampering!

### What You'll Learn

Immutability means "cannot be changed after creation." Tuples are immutable - their greatest strength.

### Why It Matters

**Problem with mutable data:**
```python
config = ['localhost', 5432, 'mydb']
# Later, someone accidentally changes it
config[0] = 'wrong_server'  # Oops! Bug introduced
```

**Safety with immutable data:**
```python
config = ('localhost', 5432, 'mydb')
# config[0] = 'wrong_server'  # TypeError - prevented!
```

### What Immutability Means

**Cannot Change:**
```python
point = (10, 20)

# These all fail:
# point[0] = 15      # TypeError
# point.append(30)   # AttributeError
# point.remove(20)   # AttributeError
```

**Can Create New:**
```python
point = (10, 20)

# Create new tuple
new_point = point + (30,)  # (10, 20, 30)
# Original unchanged: (10, 20)
```

### Key Benefits

**1. Safety:**
- Cannot accidentally modify
- Protected from bugs
- Clear intent

**2. Dictionary Keys:**
```python
# Tuples work as keys
locations = {(0, 0): 'home', (10, 20): 'work'}

# Lists don't work
# coords = {[0, 0]: 'home'}  # Error!
```

**3. Performance:**
- Faster than lists
- Use less memory
- Optimized by Python

### Shallow Immutability

**Important caveat:**
```python
data = (1, 2, [3, 4])

# Cannot change tuple
# data[0] = 999  # Error

# BUT can change list inside!
data[2].append(5)  # Works!
# Now: (1, 2, [3, 4, 5])
```

**Why:** The tuple structure is fixed, but the list inside can still change.

### Hashable = Dict Keys

**Works (all immutable):**
```python
point = (10, 20)
locations = {point: 'home'}  # ✓
```

**Fails (contains mutable):**
```python
bad = (1, [2, 3])
# locations = {bad: 'test'}  # Error!
```

### When to Use Tuples

**Use Tuple:**
- Data shouldn't change
- Coordinates: `(x, y)`
- Configuration: `(host, port, db)`
- Constants: `DAYS = ('Mon', 'Tue', ...)`
- Dictionary keys

**Use List:**
- Data will change
- Shopping cart
- To-do list
- Need add/remove

### Try to Predict

```python
config = (1, 2, 3)

# Will these work?
a = config[0]           # ?
b = config + (4,)       # ?
config[0] = 999         # ?
c = config.append(4)    # ?
```

Answers:
- `a = config[0]` ✓ Works (access is fine)
- `b = config + (4,)` ✓ Works (creates new tuple)
- `config[0] = 999` ✗ TypeError (cannot modify)
- `config.append(4)` ✗ AttributeError (no append method)

Immutability = safety + performance!
