## Lecture Script: Create Objects from Class Definitions

**Duration:** 12 minutes

---

### Hook (2 minutes)

A class is just a blueprint — it does nothing until you create objects from it:

```python
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

# Creating objects (instances)
pet1 = Pet("Buddy", "Dog")
pet2 = Pet("Whiskers", "Cat")
print(pet1.name, pet2.name)  # Buddy Whiskers
```

---

### Section 1: Instantiation (3 minutes)

Calling a class creates a new object:

```python
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

red = Color(255, 0, 0)
blue = Color(0, 0, 255)

# Each object is independent
print(red.r)   # 255
print(blue.r)  # 0
print(type(red))           # <class '__main__.Color'>
print(isinstance(red, Color))  # True
```

---

### Section 2: Objects in Collections (3 minutes)

Objects work naturally in lists, dicts, and sets:

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

students = [
    Student("Alice", 92),
    Student("Bob", 85),
    Student("Carol", 95),
]

# Sort by grade
ranked = sorted(students, key=lambda s: s.grade, reverse=True)
for s in ranked:
    print(f"{s.name}: {s.grade}")
```

---

### Section 3: Object Identity vs Equality (3 minutes)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)  # False (different objects)
print(p1 is p2)  # False

# Add __eq__ to compare by value
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True
print(p1 is p2)  # False (still different objects)
```

---

### Summary (1 minute)

1. Call a class like a function to create an object
2. Each object has its own independent attributes
3. Objects work in lists, dicts, and other collections
4. `is` checks identity; `==` checks equality
5. Override `__eq__` for value-based comparison

