## Lecture Script: Implement __init__ Constructor


---

### CS Theory Bite

> **Origin**: Constructors were invented by **Simula 67** (1967). Python's `__init__` is technically an **initializer** (not constructor) — `__new__` creates the object, `__init__` sets it up.
>
> **Analogy**: `__init__` is like a **birth certificate** — automatically records the essential details (attributes) the moment an object is born.
>
> **Why it matters**: Without `__init__`, objects start empty — guaranteed initialization prevents AttributeError bugs.



### Hook (2 minutes)

The `__init__` method is the first thing that runs when you create an object. It sets up everything the object needs:

```python
class Player:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.hp = level * 100

p = Player("Alice", 5)
print(p.hp)  # 500
```

---

### Section 1: How __init__ Works (3 minutes)

```python
class Dog:
    def __init__(self, name, breed):
        print(f"Creating dog: {name}")
        self.name = name
        self.breed = breed

d = Dog("Rex", "Lab")  # "Creating dog: Rex"
```

Key points:
- `__init__` is called automatically after the object is created
- `self` is the new object being initialized
- It should NOT return anything (only `None`)
- It sets up the object's initial state

---

### Section 2: Default Values and Validation (3 minutes)

```python
import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
        self.area = math.pi * radius ** 2

c = Circle(5)
print(f"Area: {c.area:.2f}")  # Area: 78.54

# Circle(-1)  # ValueError: Radius must be positive
```

Default values make arguments optional:

```python
class Connection:
    def __init__(self, host="localhost", port=5432, timeout=30):
        self.host = host
        self.port = port
        self.timeout = timeout

c1 = Connection()                        # All defaults
c2 = Connection("db.example.com", 3306)  # Custom host/port
```

---

### Section 3: Computed and Derived Attributes (3 minutes)

`__init__` can compute values from the inputs:

```python
class FullName:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.full = f"{first} {last}"
        self.initials = f"{first[0]}.{last[0]}."

n = FullName("Alice", "Smith")
print(n.full)      # Alice Smith
print(n.initials)  # A.S.

class Matrix:
    def __init__(self, rows):
        self.rows = rows
        self.num_rows = len(rows)
        self.num_cols = len(rows[0]) if rows else 0
```

---

### Summary (1 minute)

1. `__init__` initializes the object's state
2. Use default values for optional parameters
3. Validate inputs early — raise exceptions for bad data
4. Compute derived attributes during initialization
5. Never return a value from `__init__`

