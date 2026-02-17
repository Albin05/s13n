# Lecture Notes: Create Objects

## Creating Objects (Instances)

An object is a specific instance of a class. You can create multiple objects from the same class.


---

<div align="center">

![Class blueprint and objects](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Classes are blueprints for creating objects*

</div>

---

## Introduction

Object creation implements **instantiation** - creating concrete instances from abstract blueprints! A class is the template, objects are the actual things built from that template. This is the **class-instance relationship** - fundamental to OOP!

### Why Instances Matter

**The blueprint-product relationship**:
```python
# Class = blueprint (abstract)
class Car:
    def drive(self):
        print("Driving!")

# Objects = actual cars (concrete)
car1 = Car()  # First car
car2 = Car()  # Second car
# Same blueprint, different instances!
```

**Each object has**:
- **Unique identity**: Different memory address
- **Own state**: Independent data/attributes
- **Shared behavior**: Methods from class definition
**This is instance independence!**

### Historical Context

**Instantiation from Simula 67** (1967) - first OOP language. Coined "**new**" keyword for creating objects. **Python uses function-call syntax** - `ClassName()` - cleaner than `new ClassName()`.

**Memory allocation**: Object creation allocates heap memory. Python's **garbage collector** (reference counting + cycle detection) automatically frees unused objects. Invented for **LISP** (1960), adopted by Python!

**The factory pattern**: `ClassName()` is like calling a factory - returns new product (object) each time. Same blueprint → different products!

### Real-World Analogies

**Objects like baking cookies**:
- **Class Cookie**: Recipe/cutter (blueprint)
- **cookie1, cookie2**: Actual cookies (instances)
- **Same recipe**: All follow class definition
- **Different**: Each can have unique decorations, toppings
**Bake many cookies from one recipe!**

**Or like car manufacturing**:
```python
class Tesla:
    def drive(self):
        print("Silent electric drive!")

# Assembly line produces instances
car1 = Tesla()  # VIN: 001
car2 = Tesla()  # VIN: 002
car3 = Tesla()  # VIN: 003
# Same design, different cars!
```

**Or like housing development**:
- **Class House**: Architectural plans (blueprint)
- **house1, house2, house3**: Actual houses (instances)
- **Same floor plan**: All follow class design
- **Different addresses**: Each has unique location, owner
**One blueprint, whole neighborhood!**

---
### Syntax

```python
object_name = ClassName()
```

## Basic Example

```python
class Dog:
    pass

# Create objects
dog1 = Dog()
dog2 = Dog()
dog3 = Dog()

print(dog1)  # <__main__.Dog object at 0x...>
print(dog2)  # <__main__.Dog object at 0x...>
print(dog3)  # <__main__.Dog object at 0x...>
```

Each object has a unique memory address.

## Objects are Independent

```python
class Student:
    pass

alice = Student()
bob = Student()

# They are different objects
print(alice == bob)  # False
print(alice is bob)  # False
```

## Objects with Methods

```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b

# Create calculator objects
calc1 = Calculator()
calc2 = Calculator()

# Use the objects
print(calc1.add(5, 3))       # 8
print(calc2.multiply(4, 2))  # 8
```

## Real-World Examples

### Example 1: Multiple Books

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display(self):
        print(f'"{self.title}" by {self.author}')

# Create multiple book objects
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Use each object
book1.display()  # "1984" by George Orwell
book2.display()  # "To Kill a Mockingbird" by Harper Lee
book3.display()  # "The Great Gatsby" by F. Scott Fitzgerald
```

### Example 2: Bank Accounts

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

# Create account objects
alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 500)

# Each account is independent
alice_account.deposit(200)   # Alice deposited $200. New balance: $1200
bob_account.withdraw(100)    # Bob withdrew $100. New balance: $400

print(f"Alice's balance: ${alice_account.balance}")  # $1200
print(f"Bob's balance: ${bob_account.balance}")      # $400
```

### Example 3: Shopping Cart

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
        print(f"Added {item} for ${price}")
    
    def get_total(self):
        total = sum(item["price"] for item in self.items)
        return total
    
    def show_items(self):
        print("Cart contents:")
        for item in self.items:
            print(f"  - {item['item']}: ${item['price']}")
        print(f"Total: ${self.get_total()}")

# Create separate carts for different customers
alice_cart = ShoppingCart()
bob_cart = ShoppingCart()

# Alice's shopping
alice_cart.add_item("Book", 15)
alice_cart.add_item("Pen", 2)

# Bob's shopping
bob_cart.add_item("Laptop", 800)
bob_cart.add_item("Mouse", 25)

# Show each cart
print("\nAlice's cart:")
alice_cart.show_items()

print("\nBob's cart:")
bob_cart.show_items()
```

### Example 4: Student Records

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.courses = []
    
    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")
    
    def show_info(self):
        print(f"Student: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Courses: {', '.join(self.courses)}")

# Create student objects
alice = Student("Alice", 10)
bob = Student("Bob", 10)
charlie = Student("Charlie", 11)

# Each student enrolls in different courses
alice.enroll("Math")
alice.enroll("Science")

bob.enroll("English")
bob.enroll("History")

charlie.enroll("Math")
charlie.enroll("Computer Science")

# Show info for each
alice.show_info()
print()
bob.show_info()
print()
charlie.show_info()
```

## Creating Objects in a Loop

```python
class Counter:
    def __init__(self, start=0):
        self.count = start
    
    def increment(self):
        self.count += 1
    
    def get_count(self):
        return self.count

# Create multiple counter objects
counters = []
for i in range(5):
    counter = Counter(i * 10)
    counters.append(counter)

# Use each counter
for i, counter in enumerate(counters):
    counter.increment()
    counter.increment()
    print(f"Counter {i}: {counter.get_count()}")

# Output:
# Counter 0: 2
# Counter 1: 12
# Counter 2: 22
# Counter 3: 32
# Counter 4: 42
```

## Storing Objects in Collections

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Create product objects
products = [
    Product("Laptop", 999),
    Product("Mouse", 25),
    Product("Keyboard", 75),
    Product("Monitor", 300)
]

# Process objects from list
total_value = 0
for product in products:
    print(f"{product.name}: ${product.price}")
    total_value += product.price

print(f"\nTotal inventory value: ${total_value}")
```

## Key Takeaways

1. **Multiple objects**: Create many instances from one class
2. **Independent**: Each object has its own data
3. **Same interface**: All objects from same class have same methods
4. **Different states**: Each object can have different attribute values
5. **Memory**: Each object is stored in separate memory location
6. **Collections**: Can store objects in lists, dicts, etc.
