## Editorials: Use Instance Attributes

---

### Q1 Solution

```python
class Profile:
    def __init__(self, username, email, bio):
        self.username = username
        self.email = email
        self.bio = bio

    def summary(self):
        return f"{self.username} ({self.email}): {self.bio}"

p = Profile("alice", "alice@mail.com", "Python developer")
print(p.summary())  # alice (alice@mail.com): Python developer
```

---

### Q2 Solution

```python
class ShoppingCart:
    def __init__(self):
        self.items = []  # Each instance gets its own list

    def add(self, item):
        self.items.append(item)

cart1 = ShoppingCart()
cart2 = ShoppingCart()
cart1.add("Apple")
print(cart1.items)  # ['Apple']
print(cart2.items)  # [] — independent

# Using items=[] as default parameter would make ALL instances
# share the same list object, which is a common Python bug.
```

---

### Q3 Solution

```python
class Counter:
    def __init__(self):
        self._count = 0
        self._total_increments = 0

    def increment(self):
        self._count += 1
        self._total_increments += 1

    def decrement(self):
        if self._count > 0:
            self._count -= 1

    def reset(self):
        self._count = 0

    def value(self):
        return self._count

c = Counter()
c.increment()
c.increment()
c.increment()
c.decrement()
print(c.value())              # 2
print(c._total_increments)    # 3
```

---

### Q4 Solution

```python
class Record:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def fields(self):
        return list(vars(self).keys())

r = Record(name="Alice", age=25, city="NYC")
print(r.name)      # Alice
print(r.fields())  # ['name', 'age', 'city']
```

---

### Q5 Solution

```python
class TrackedObject:
    def __init__(self, **kwargs):
        super().__setattr__("_history", [])
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __setattr__(self, name, value):
        if name != "_history":
            old = getattr(self, name, "<unset>")
            self._history.append({
                "attr": name,
                "old": old,
                "new": value,
            })
        super().__setattr__(name, value)

    def get_history(self):
        return self._history

t = TrackedObject(x=1, y=2)
t.x = 10
t.y = 20
for change in t.get_history():
    print(change)
```

