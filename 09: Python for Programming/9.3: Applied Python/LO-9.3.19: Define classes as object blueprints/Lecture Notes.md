# Lecture Notes: Define Classes

## Classes in Python

A class is a blueprint for creating objects. It defines the structure and behavior of objects.


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---

## Introduction

Classes implement **object-oriented programming** (OOP) - organizing code around objects that combine data and behavior! Classes are **blueprints** or **templates** - they define what objects will look like and do. This is **abstraction** - modeling real-world concepts in code!

### Why Classes are Revolutionary

**Before OOP** (procedural): Data and functions separate:
```python
# Procedural - data and behavior disconnected
dog_name = "Buddy"
dog_age = 3

def bark(name):
    print(f"{name} says Woof!")

bark(dog_name)  # Loose coupling!
```

**With OOP** (classes): Data and behavior bundled together:
```python
# OOP - data and behavior unified!
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

buddy = Dog("Buddy", 3)
buddy.bark()  # Tight coupling!
```

**This is encapsulation** - data and functions that operate on data bundled together!

### Historical Context

**OOP invented by Simula 67** (1967, Norway) for simulations. **Smalltalk** (1972, Xerox PARC) made "everything is an object". **Python classes** (1991) influenced by **Modula-3** and **C++**.

**Why "class"?** From **taxonomy** - biological classification. Class → Species → Individual. In code: Class → Type → Instance. **Object = instance of a class**!

**The OOP paradigm**: **Alan Kay** (Smalltalk creator) defined OOP as message passing between objects. Python uses dot notation: `obj.method()` = sending message to object!

### Real-World Analogies

**Classes like cookie cutters**:
- **Class**: Cookie cutter shape (blueprint)
- **Objects**: Actual cookies (instances)
- **Same shape**: All cookies follow cutter's shape
- **Different dough**: Each cookie can have unique decorations
**One blueprint, many instances!**

**Or like building blueprints**:
```python
class House:  # Blueprint
    def __init__(self, address):
        self.address = address

house1 = House("123 Main St")  # Built from blueprint
house2 = House("456 Oak Ave")  # Another instance
# Same blueprint, different houses!
```

**Or like car manufacturing**:
- **Class Car**: Design specs (blueprint)
- **car1, car2**: Actual cars off assembly line (instances)
- **Same design**: All follow class definition
- **Different**: Each has unique VIN, color, owner
**Classes = manufacturing templates!**

---
### Basic Syntax

```python
class ClassName:
    # Class body
    pass
```

### Naming Convention

- Use **PascalCase** (capitalize first letter of each word)
- Descriptive names

```python
# Good
class Dog:
    pass

class BankAccount:
    pass

class StudentRecord:
    pass

# Avoid
class dog:  # Should be capitalized
    pass

class d:    # Not descriptive
    pass
```

## Creating a Simple Class

```python
class Dog:
    pass

# Create an object
my_dog = Dog()
print(my_dog)  # <__main__.Dog object at 0x...>
```

## Adding Methods

```python
class Dog:
    def bark(self):
        print("Woof!")
    
    def sit(self):
        print("Sitting")

my_dog = Dog()
my_dog.bark()  # Woof!
my_dog.sit()   # Sitting
```

## Real-World Examples

### Example 1: Book Class

```python
class Book:
    def open(self):
        print("Opening book...")
    
    def close(self):
        print("Closing book...")
    
    def read_page(self, page_num):
        print(f"Reading page {page_num}")

book = Book()
book.open()
book.read_page(1)
book.close()
```

### Example 2: Calculator Class

```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Cannot divide by zero"

calc = Calculator()
print(calc.add(5, 3))       # 8
print(calc.multiply(4, 2))  # 8
```

## Key Takeaways

1. **class keyword**: Define classes
2. **PascalCase**: Naming convention
3. **Blueprint**: Class is template, object is instance
4. **Methods**: Functions inside classes
5. **self**: First parameter of methods
