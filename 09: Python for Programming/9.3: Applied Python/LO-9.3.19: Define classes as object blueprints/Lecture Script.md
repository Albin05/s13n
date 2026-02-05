## Lecture Script: Define Classes as Object Blueprints

**Duration:** 12 minutes

---

### Hook (2 minutes)

Every Python value is an object. Strings have methods like `.upper()`, lists have `.append()`. Now you'll learn to create your own types:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

rex = Dog("Rex", "Labrador")
print(rex.bark())  # Rex says Woof!
```

---

### Section 1: What is a Class? (3 minutes)

A class is a blueprint. An object is an instance of that blueprint:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Create instances
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.make)   # Toyota
print(car2.model)  # Civic
print(type(car1))  # <class '__main__.Car'>
```

Key points:
- `class` keyword defines the blueprint
- `__init__` runs when creating an instance
- `self` refers to the current instance

---

### Section 2: Adding Methods (3 minutes)

Methods are functions that belong to a class:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def describe(self):
        return f"{self.width}x{self.height} rectangle"

r = Rectangle(5, 3)
print(r.area())        # 15
print(r.describe())    # 5x3 rectangle
```

---

### Section 3: Classes vs Dictionaries (3 minutes)

When should you use a class instead of a dict?

```python
# Dictionary approach - no structure enforcement
student = {"name": "Alice", "grades": [90, 85]}

# Class approach - structured with behavior
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

s = Student("Alice")
s.add_grade(90)
s.add_grade(85)
print(s.average())  # 87.5
```

Use classes when data has behavior or validation rules.

---

### Summary (1 minute)

1. `class` defines a blueprint for objects
2. `__init__` initializes instance attributes
3. `self` refers to the current instance
4. Methods define behavior for the class
5. Use classes when data needs structure and behavior

