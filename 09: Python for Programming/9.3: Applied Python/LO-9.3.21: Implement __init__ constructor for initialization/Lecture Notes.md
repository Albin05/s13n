# Lecture Notes: Implement the __init__ Constructor

## The __init__ Method

`__init__` is a special method (constructor) that automatically runs when you create an object.


---

<div align="center">

![Python __init__ Constructor Method Object](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.21.png)

*The __init__ constructor acts as a function machine, transforming input parameters into initialized object state*

</div>

---

## Introduction

The `__init__` method implements **constructor functionality** - automatic initialization when objects are born! This is the **object birth certificate** - setting initial state before the object enters the world. Constructors are fundamental to **RAII** (Resource Acquisition Is Initialization) and **guaranteed initialization**!

### Why __init__ is Revolutionary

**Problem without constructors**: Uninitialized objects are dangerous:
```python
# DANGER - forgot to initialize!
dog = Dog()
print(dog.name)  # AttributeError - name doesn't exist!
# Broken object, runtime crashes!
```

**Solution with __init__**: Guaranteed initialization:
```python
# SAFE - always initialized!
class Dog:
    def __init__(self, name):
        self.name = name  # Must provide name
dog = Dog("Buddy")  # Cannot create without name!
print(dog.name)  # Always works!
```

**This is initialization safety** - objects born complete, never broken!

### Historical Context

**Constructors invented by Simula 67** (1967) - first OOP language. Originally called "**prefixing**" - code that runs before object use. **C++** (1979) formalized `ClassName()` syntax - function-like constructor calls!

**Python's __init__** differs from C++ constructors: Not technically a constructor (object already exists when `__init__` runs), but an **initializer**! Python's `__new__` creates object, `__init__` initializes it. This **two-phase construction** enables metaclasses and advanced patterns!

**Automatic invocation**: When you call `Dog("Buddy")`, Python automatically:
1. Calls `__new__` (creates empty object)
2. Calls `__init__` (fills object with data)
3. Returns initialized object
**This is constructor magic** - automatic setup!

### Real-World Analogies

**__init__ like birth certificate**:
- **Birth**: Object created by `__new__` (baby born)
- **Certificate**: `__init__` records initial data (name, date, parents)
- **Complete identity**: Object ready to use with all required info
**Your objects need birth certificates!**

**Or like assembling furniture**:
```python
class Table:
    def __init__(self, legs, surface_material):
        self.legs = legs          # Attach legs
        self.surface = surface_material  # Add tabletop
        self.assembled = True     # Mark complete
# Table arrives assembled, ready to use!
table = Table(4, "wood")
```

**Or like restaurant orders**:
- **Order placed**: Create object (call constructor)
- **Cook prepares**: `__init__` runs (set ingredients, cooking)
- **Served complete**: Object delivered with all parts ready
**Never serve half-cooked objects!**

### Constructor vs Regular Method

**Regular methods**: Called manually when needed:
```python
obj = MyClass()
obj.setup()  # Might forget to call!
```

**Constructor (__init__)**: Called automatically:
```python
obj = MyClass()  # setup() runs automatically!
# Cannot forget - guaranteed initialization!
```

**This is the constructor guarantee** - objects always initialized!

---
### Syntax

```python
class ClassName:
    def __init__(self, parameters):
        # Initialize attributes
        self.attribute = value
```

## Why Use __init__?

1. **Initialize attributes**: Set starting values for object
2. **Automatic execution**: Runs when object is created
3. **Required data**: Ensure objects start with necessary data

## Basic Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create person object
alice = Person("Alice", 25)
print(alice.name)  # Alice
print(alice.age)   # 25
```

## Without __init__

```python
class Dog:
    pass

# Must set attributes manually
dog = Dog()
dog.name = "Buddy"
dog.breed = "Labrador"
```

## With __init__

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Attributes set automatically
dog = Dog("Buddy", "Labrador")
print(dog.name)   # Buddy
print(dog.breed)  # Labrador
```

## The self Parameter

`self` refers to the object being created:

```python
class Car:
    def __init__(self, brand, year):
        self.brand = brand  # THIS object's brand
        self.year = year    # THIS object's year

car1 = Car("Toyota", 2020)
car2 = Car("Honda", 2021)

print(car1.brand)  # Toyota (car1's brand)
print(car2.brand)  # Honda (car2's brand)
```

## Real-World Examples

### Example 1: Bank Account

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []
        print(f"Account created for {owner} with balance ${balance}")

account = BankAccount("Alice", 1000)
# Output: Account created for Alice with balance $1000

print(account.owner)        # Alice
print(account.balance)      # 1000
print(account.transactions) # []
```

### Example 2: Book

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False
    
    def info(self):
        return f'"{self.title}" by {self.author} ({self.pages} pages)'

book = Book("1984", "George Orwell", 328)
print(book.info())  # "1984" by George Orwell (328 pages)
print(book.current_page)  # 1
print(book.is_open)       # False
```

### Example 3: Student with Default Values

```python
class Student:
    def __init__(self, name, grade, gpa=0.0):
        self.name = name
        self.grade = grade
        self.gpa = gpa
        self.courses = []
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"GPA: {self.gpa}")
        print(f"Courses: {len(self.courses)}")

# With default GPA
student1 = Student("Alice", 10)
student1.display()

# With custom GPA
student2 = Student("Bob", 11, 3.8)
student2.display()
```

### Example 4: Rectangle

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
        self.perimeter = 2 * (width + height)
    
    def display(self):
        print(f"Rectangle: {self.width}x{self.height}")
        print(f"Area: {self.area}")
        print(f"Perimeter: {self.perimeter}")

rect = Rectangle(5, 3)
rect.display()
# Rectangle: 5x3
# Area: 15
# Perimeter: 16
```

### Example 5: Shopping Cart with Initial Items

```python
class ShoppingCart:
    def __init__(self, customer_name):
        self.customer = customer_name
        self.items = []
        self.total = 0
        print(f"Shopping cart created for {customer_name}")
    
    def add_item(self, item, price):
        self.items.append(item)
        self.total += price
        print(f"Added {item} (${price})")

cart = ShoppingCart("Alice")
cart.add_item("Book", 15)
cart.add_item("Pen", 2)
print(f"Total: ${cart.total}")
```

## Validation in __init__

```python
class Person:
    def __init__(self, name, age):
        if age < 0:
            print("Age cannot be negative!")
            self.age = 0
        else:
            self.age = age
        
        if not name:
            print("Name cannot be empty!")
            self.name = "Unknown"
        else:
            self.name = name

# Valid person
person1 = Person("Alice", 25)
print(person1.name, person1.age)  # Alice 25

# Invalid age
person2 = Person("Bob", -5)
# Output: Age cannot be negative!
print(person2.name, person2.age)  # Bob 0
```

## Computing Values in __init__

```python
class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        # Computed attribute
        self.salary = hourly_rate * hours_worked
    
    def info(self):
        print(f"{self.name}: ${self.salary} ({self.hours_worked}hrs @ ${self.hourly_rate}/hr)")

emp = Employee("Alice", 25, 40)
emp.info()  # Alice: $1000 (40hrs @ $25/hr)
```

## __init__ with No Parameters

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def get_count(self):
        return self.count

counter = Counter()
counter.increment()
counter.increment()
print(counter.get_count())  # 2
```

## Common Mistakes

### 1. Forgetting self

```python
# Wrong
class Dog:
    def __init__(self, name):
        name = name  # Doesn't save to object!

dog = Dog("Buddy")
# print(dog.name)  # AttributeError!

# Correct
class Dog:
    def __init__(self, name):
        self.name = name  # Saves to object

dog = Dog("Buddy")
print(dog.name)  # Buddy
```

### 2. Forgetting self parameter

```python
# Wrong
class Cat:
    def __init__(name):  # Missing self!
        self.name = name

# Correct
class Cat:
    def __init__(self, name):
        self.name = name
```

### 3. Wrong indentation

```python
# Wrong
class Person:
def __init__(self, name):  # Not indented!
    self.name = name

# Correct
class Person:
    def __init__(self, name):
        self.name = name
```

## Key Takeaways

1. **__init__**: Constructor method, runs automatically
2. **self**: First parameter, refers to the object
3. **Initialize attributes**: Set starting values
4. **Automatic**: Called when creating object
5. **Required data**: Use parameters to require necessary data
6. **Default values**: Can provide default parameter values
7. **Validation**: Can validate data in __init__
