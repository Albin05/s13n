# Lecture Notes: Apply Inheritance

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class.


---

<div align="center">

![Tree structure showing inheritance](https://images.unsplash.com/photo-1502101872923-d48509bff386?w=800&q=80)

*Inheritance allows classes to inherit properties from parent classes*

</div>

---

## Introduction

Inheritance implements **taxonomic hierarchies** - organizing classes by "is-a" relationships! This is **code reuse through specialization** - building specific classes from general ones. Inheritance is **hierarchical classification** - like biology's kingdom → phylum → class → species!

### Why Inheritance is Transformative

**Problem without inheritance**: Duplicate code everywhere:
```python
# REPETITIVE - same code copied!
class Dog:
    def eat(self): print("Eating")
    def sleep(self): print("Sleeping")
    def bark(self): print("Woof!")

class Cat:
    def eat(self): print("Eating")    # Duplicate!
    def sleep(self): print("Sleeping")  # Duplicate!
    def meow(self): print("Meow!")
# Copy-paste nightmare!
```

**Solution with inheritance**: Share common code:
```python
# DRY - Don't Repeat Yourself!
class Animal:
    def eat(self): print("Eating")
    def sleep(self): print("Sleeping")

class Dog(Animal):  # Inherits eat, sleep
    def bark(self): print("Woof!")

class Cat(Animal):  # Inherits eat, sleep
    def meow(self): print("Meow!")
# Common code written once!
```

**This is inheritance power** - write once, reuse everywhere!

### Historical Context

**Inheritance invented by Simula 67** (1967) for simulation - model real-world hierarchies! **"Class" from taxonomy** - biological classification inspired programming concept. **Smalltalk** (1972) popularized inheritance - made it central to OOP!

**Single vs multiple inheritance**: **C++** (1983) introduced **multiple inheritance** - inherit from multiple parents (complex!). **Java** (1995) chose **single inheritance only** - simpler but less flexible. **Python allows multiple inheritance** - power with complexity!

**Is-a relationship**: Inheritance models **Liskov Substitution Principle** (Barbara Liskov, 1987): "Objects of subclass should replace parent class objects without breaking program". **Dog IS-A Animal** - anywhere Animal works, Dog should work!

### Real-World Analogies

**Inheritance like biological taxonomy**:
- **Animal**: General category (parent class)
  - **Mammal**: More specific (child class)
    - **Dog**: Even more specific (grandchild class)
    - **Cat**: Another specialization
  - **Bird**: Different child
    - **Eagle**: Specialization
**Taxonomy == inheritance hierarchy!**

**Or like organizational structure**:
```python
class Employee:  # Base class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def work(self):
        print(f"{self.name} is working")

class Developer(Employee):  # Inherits Employee features
    def code(self):
        print(f"{self.name} is coding")

class Manager(Employee):  # Inherits Employee features
    def manage(self):
        print(f"{self.name} is managing")
# Developer IS-A Employee, Manager IS-A Employee!
```

**Or like vehicle classification**:
- **Vehicle**: Wheels, engine, drive() (base class)
  - **Car**: 4 wheels, trunk (specialized)
  - **Motorcycle**: 2 wheels, kickstand (specialized)
  - **Truck**: Cargo bed, heavy-duty (specialized)
**All vehicles, but with unique features!**

### Inheritance vs Composition

**Inheritance ("is-a")**: Dog IS-A Animal
```python
class Dog(Animal):  # Inherits
    pass
```

**Composition ("has-a")**: Dog HAS-A Owner
```python
class Dog:
    def __init__(self, owner):
        self.owner = owner  # Composition
```

**Favor composition over inheritance** - common design principle! Inheritance creates **tight coupling** (changes to parent affect all children). Composition more **flexible** - swap components easily!

---
### Syntax

```python
class ParentClass:
    # Parent class code
    pass

class ChildClass(ParentClass):
    # Child class code
    pass
```

### Example: Animal Hierarchy

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

# Create objects
dog = Dog("Buddy")
dog.eat()   # Inherited from Animal
dog.bark()  # Defined in Dog

cat = Cat("Whiskers")
cat.eat()   # Inherited from Animal
cat.meow()  # Defined in Cat
```

## Multiple Levels of Inheritance

```python
class Animal:
    def breathe(self):
        print("Breathing...")

class Mammal(Animal):
    def feed_young(self):
        print("Feeding young...")

class Dog(Mammal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.breathe()     # From Animal
dog.feed_young()  # From Mammal
dog.bark()        # From Dog
```

## Real-World Example: Employees

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        print(f"{self.name} is working")

class Developer(Employee):
    def code(self):
        print(f"{self.name} is coding")

class Manager(Employee):
    def manage(self):
        print(f"{self.name} is managing")

dev = Developer("Alice", 80000)
dev.work()  # From Employee
dev.code()  # From Developer

mgr = Manager("Bob", 90000)
mgr.work()    # From Employee
mgr.manage()  # From Manager
```

## Key Takeaways

1. **Inheritance syntax**: `class Child(Parent):`
2. **Code reuse**: Inherit parent functionality
3. **Specialization**: Add child-specific features
4. **Is-a relationship**: Dog IS-A Animal
5. **Multiple levels**: Grandparent → Parent → Child
