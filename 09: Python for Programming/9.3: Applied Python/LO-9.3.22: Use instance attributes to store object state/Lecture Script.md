## Lecture Script: Use Instance Attributes

**Duration:** 12 minutes

---

### Hook (2 minutes)

Instance attributes store data unique to each object:

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.tricks = []

dog = Pet("Rex")
cat = Pet("Whiskers")
dog.tricks.append("shake")
print(cat.tricks)  # [] — each object has its own list
```

---

### Section 1: Setting and Accessing Attributes (3 minutes)

```python
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lives = 3

p = Player("Alice")
print(p.name)    # Alice
print(p.score)   # 0

# Modify attributes
p.score += 10
p.lives -= 1
print(p.score)   # 10
```

You can also add attributes after creation:

```python
p.nickname = "Ace"  # Works, but prefer __init__
print(p.nickname)
```

---

### Section 2: Common Pitfall — Mutable Defaults (3 minutes)

```python
# BUG: All instances share the same list!
class BadList:
    def __init__(self, items=[]):
        self.items = items

a = BadList()
b = BadList()
a.items.append(1)
print(b.items)  # [1] — shared!

# FIX: Use None as default
class GoodList:
    def __init__(self, items=None):
        self.items = items if items is not None else []
```

---

### Section 3: Inspecting Attributes (3 minutes)

```python
class Config:
    def __init__(self, host, port):
        self.host = host
        self.port = port

c = Config("localhost", 8080)

# Check if attribute exists
print(hasattr(c, "host"))    # True
print(hasattr(c, "debug"))   # False

# Get with default
print(getattr(c, "debug", False))  # False

# See all attributes
print(vars(c))  # {'host': 'localhost', 'port': 8080}
```

---

### Summary (1 minute)

1. Set attributes in `__init__` using `self.attr = value`
2. Each instance has its own independent attributes
3. Never use mutable defaults (`[]`, `{}`) — use `None` instead
4. Use `hasattr()`, `getattr()`, `vars()` to inspect attributes

