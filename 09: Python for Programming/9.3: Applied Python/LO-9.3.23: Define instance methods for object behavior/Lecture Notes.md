# Lecture Notes: Define Instance Methods

## Instance Methods

Instance methods are functions defined inside a class that operate on instance objects.


---

<div align="center">

![Python self Parameter Instance Method Behavior](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.23.png)

*Instance methods act as function machines that operate on and transform an object's internal state*

</div>

---

## Introduction

Instance methods implement **object behavior** - actions objects can perform! This is **encapsulation of logic** - data and operations bundled together. Methods are **verbs** (actions) while attributes are **nouns** (properties). Together they create **living objects**!

### Why Instance Methods are Powerful

**Problem with scattered functions**: Data and logic separated:
```python
# MESSY - data separate from operations!
balance = 1000
def deposit(amount):
    global balance
    balance += amount  # Which account?
# Functions disconnected from data!
```

**Solution with methods**: Behavior belongs to object:
```python
# CLEAN - operations bound to data!
class Account:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount  # THIS account!
account1.deposit(500)  # Clear ownership!
```

**This is object-oriented thinking** - objects know what they can do!

### Historical Context

**Methods** invented by **Simula 67** (1967) as "procedures inside objects". **Smalltalk** (1972) called them "messages" - objects communicate by sending messages! Alan Kay: "**Objects are like biological cells - communicate via messages**".

**Message passing vs function calls**: Smalltalk views `obj.method()` as sending "method" message to `obj`. Python uses **late binding** - method looked up at runtime, enabling dynamic dispatch! This **dynamic method resolution** powers polymorphism!

**self parameter**: **Explicit self** is Python design choice. Guido van Rossum: "Explicit is better than implicit" (Zen of Python). **C++/Java** hide `this` pointer - Python exposes `self` for clarity. **This transparency** helps beginners understand object mechanics!

### Real-World Analogies

**Methods like object capabilities**:
- **Dog object**: Can bark, eat, sleep (methods)
- **Car object**: Can drive, brake, honk (methods)
- **Phone object**: Can call, text, take_photo (methods)
**Objects are defined by what they DO!**

**Or like appliance operations**:
```python
class Microwave:
    def __init__(self):
        self.timer = 0
        self.power = 0

    def start(self, seconds, power_level):
        self.timer = seconds
        self.power = power_level
        print(f"Heating for {seconds}s at {power_level}% power")

    def stop(self):
        self.timer = 0
        print("Stopped")
# Microwave knows how to heat food!
```

**Or like employee responsibilities**:
- **Developer**: Can code(), debug(), review_code() (methods)
- **Manager**: Can hire(), schedule(), conduct_meeting()
- **Designer**: Can design(), prototype(), user_test()
**Each role has specific actions - methods define capabilities!**

### Methods vs Functions: The OOP Shift

**Procedural style**: Functions operate on data:
```python
def calculate_area(width, height):
    return width * height
area = calculate_area(5, 3)  # Function takes data
```

**Object-oriented style**: Objects operate on themselves:
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height  # Object knows its dimensions
rect = Rectangle(5, 3)
area = rect.area()  # Object calculates itself!
```

**This is the OOP paradigm shift** - objects active, not passive!

---
### Syntax

```python
class ClassName:
    def method_name(self, parameters):
        # Method body
        pass
```

## The self Parameter

Every instance method must have `self` as the first parameter:

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):  # self is required
        print(f"{self.name} says Woof!")

dog = Dog("Buddy")
dog.bark()  # Buddy says Woof!
```

## Why self?

`self` refers to the object calling the method:

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1  # Modify THIS object's count
    
    def get_count(self):
        return self.count  # Return THIS object's count

counter1 = Counter()
counter2 = Counter()

counter1.increment()
counter1.increment()
counter2.increment()

print(counter1.get_count())  # 2
print(counter2.get_count())  # 1
```

## Methods with Parameters

```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
    def power(self, base, exponent):
        return base ** exponent

calc = Calculator()
print(calc.add(5, 3))        # 8
print(calc.multiply(4, 2))   # 8
print(calc.power(2, 3))      # 8
```

## Methods Accessing Attributes

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def circumference(self):
        return 2 * 3.14159 * self.radius
    
    def scale(self, factor):
        self.radius *= factor

circle = Circle(5)
print(circle.area())           # 78.53975
print(circle.circumference())  # 31.4159
circle.scale(2)
print(circle.area())           # 314.159
```

## Real-World Examples

### Example 1: Bank Account

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive!")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrawal: -${amount}")
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive!")
    
    def get_balance(self):
        return self.balance
    
    def show_history(self):
        print(f"\nTransaction History for {self.owner}:")
        for transaction in self.transaction_history:
            print(f"  {transaction}")
        print(f"Current Balance: ${self.balance}")

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Insufficient funds
account.show_history()
```

### Example 2: Student Grade Manager

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Added grade: {grade}")
        else:
            print("Grade must be between 0 and 100!")
    
    def get_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0
    
    def get_letter_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
    def display_report(self):
        print(f"\nStudent: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")

alice = Student("Alice")
alice.add_grade(85)
alice.add_grade(92)
alice.add_grade(78)
alice.add_grade(95)
alice.display_report()
```

### Example 3: Shopping Cart

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        item = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "total": price * quantity
        }
        self.items.append(item)
        print(f"Added {quantity}x {name} @ ${price} each")
    
    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                print(f"Removed {name}")
                return
        print(f"{name} not found in cart!")
    
    def get_total(self):
        total = sum(item["total"] for item in self.items)
        return total
    
    def apply_discount(self, percentage):
        discount_amount = self.get_total() * (percentage / 100)
        print(f"Discount applied: ${discount_amount:.2f} ({percentage}%)")
        return self.get_total() - discount_amount
    
    def show_cart(self):
        print("\nShopping Cart:")
        print("-" * 50)
        for item in self.items:
            print(f"{item['quantity']}x {item['name']} @ ${item['price']} = ${item['total']}")
        print("-" * 50)
        print(f"Total: ${self.get_total():.2f}")

cart = ShoppingCart()
cart.add_item("Laptop", 999, 1)
cart.add_item("Mouse", 25, 2)
cart.add_item("Keyboard", 75, 1)
cart.show_cart()
final_price = cart.apply_discount(10)
print(f"Final Price: ${final_price:.2f}")
```

### Example 4: Temperature Converter

```python
class TemperatureConverter:
    def __init__(self, temp, unit):
        self.temperature = temp
        self.unit = unit.upper()
    
    def to_celsius(self):
        if self.unit == "C":
            return self.temperature
        elif self.unit == "F":
            return (self.temperature - 32) * 5/9
        elif self.unit == "K":
            return self.temperature - 273.15
    
    def to_fahrenheit(self):
        if self.unit == "F":
            return self.temperature
        elif self.unit == "C":
            return (self.temperature * 9/5) + 32
        elif self.unit == "K":
            return (self.temperature - 273.15) * 9/5 + 32
    
    def to_kelvin(self):
        if self.unit == "K":
            return self.temperature
        elif self.unit == "C":
            return self.temperature + 273.15
        elif self.unit == "F":
            return (self.temperature - 32) * 5/9 + 273.15
    
    def convert_to(self, target_unit):
        target = target_unit.upper()
        if target == "C":
            result = self.to_celsius()
        elif target == "F":
            result = self.to_fahrenheit()
        elif target == "K":
            result = self.to_kelvin()
        else:
            return "Invalid unit!"
        
        print(f"{self.temperature}°{self.unit} = {result:.2f}°{target}")
        return result

temp = TemperatureConverter(100, "C")
temp.convert_to("F")  # 100°C = 212.00°F
temp.convert_to("K")  # 100°C = 373.15°K

temp2 = TemperatureConverter(32, "F")
temp2.convert_to("C")  # 32°F = 0.00°C
```

### Example 5: Task Manager

```python
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.completed = []
    
    def add_task(self, task, priority="Normal"):
        task_item = {
            "task": task,
            "priority": priority,
            "completed": False
        }
        self.tasks.append(task_item)
        print(f"Added task: {task} (Priority: {priority})")
    
    def complete_task(self, task_name):
        for task in self.tasks:
            if task["task"] == task_name:
                task["completed"] = True
                self.completed.append(task)
                self.tasks.remove(task)
                print(f"Completed: {task_name}")
                return
        print(f"Task '{task_name}' not found!")
    
    def list_tasks(self):
        print("\nPending Tasks:")
        if not self.tasks:
            print("  No pending tasks!")
        for i, task in enumerate(self.tasks, 1):
            print(f"  {i}. {task['task']} [{task['priority']}]")
    
    def list_completed(self):
        print("\nCompleted Tasks:")
        if not self.completed:
            print("  No completed tasks!")
        for i, task in enumerate(self.completed, 1):
            print(f"  {i}. {task['task']}")
    
    def get_summary(self):
        total = len(self.tasks) + len(self.completed)
        print(f"\nTask Summary:")
        print(f"  Total: {total}")
        print(f"  Pending: {len(self.tasks)}")
        print(f"  Completed: {len(self.completed)}")

manager = TaskManager()
manager.add_task("Write report", "High")
manager.add_task("Check emails", "Normal")
manager.add_task("Call client", "High")
manager.list_tasks()
manager.complete_task("Check emails")
manager.list_tasks()
manager.list_completed()
manager.get_summary()
```

## Methods Calling Other Methods

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height
    
    def display_info(self):
        print(f"Rectangle: {self.width}x{self.height}")
        print(f"Area: {self.area()}")           # Calling other method
        print(f"Perimeter: {self.perimeter()}") # Calling other method
        if self.is_square():                    # Calling other method
            print("This is a square!")

rect = Rectangle(5, 5)
rect.display_info()
```

## Key Takeaways

1. **Instance methods**: Functions inside a class
2. **self parameter**: Always first parameter
3. **Access attributes**: Use self.attribute
4. **Call methods**: Use self.method()
5. **Return values**: Methods can return data
6. **Modify state**: Methods can change attributes
7. **Organization**: Group related functionality
