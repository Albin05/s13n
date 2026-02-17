## Pre-Read: Create Objects from Class Definitions


---

### Creating Objects

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Each call creates a new, independent object
d1 = Dog("Rex", "Lab")
d2 = Dog("Max", "Poodle")
```

---

### Objects Are Independent

```python
d1.name = "Buddy"
print(d1.name)  # Buddy
print(d2.name)  # Max (unchanged)
```

---

### Type Checking

```python
print(type(d1))              # <class '__main__.Dog'>
print(isinstance(d1, Dog))   # True
```

---

### Try This

```python
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

items = [Item("Pen", 1.5), Item("Book", 12.0), Item("Bag", 25.0)]
for item in items:
    print(f"{item.name}: ${item.price}")
```

