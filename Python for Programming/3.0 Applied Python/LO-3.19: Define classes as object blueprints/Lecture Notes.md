# Lecture Notes: Define Classes

## Classes in Python

A class is a blueprint for creating objects. It defines the structure and behavior of objects.


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

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
