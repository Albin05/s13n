# Lecture Notes: Override Methods

## Override Methods

Redefining parent class methods in child classes


---

<div align="center">

![Python Method Override Polymorphism](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.25.png)

*Method overriding replaces parent behavior at specific nodes in the class hierarchy tree*

</div>

---

## Introduction

Method overriding implements **polymorphism** - "many forms" of the same operation! This is **behavioral specialization** - child classes customize inherited behavior for their specific needs. Overriding is **customization inheritance** - take what parent gives, make it yours!

### Why Method Overriding is Essential

**Problem without overriding**: All objects act identically:
```python
# BORING - all animals sound the same!
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal): pass
class Cat(Animal): pass

dog = Dog()
cat = Cat()
print(dog.speak())  # "Some sound" - wrong!
print(cat.speak())  # "Some sound" - wrong!
```

**Solution with overriding**: Each class customizes behavior:
```python
# REALISTIC - each animal unique sound!
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):  # Override!
        return "Woof!"

class Cat(Animal):
    def speak(self):  # Override!
        return "Meow!"
# Each animal speaks correctly!
```

**This is polymorphism** - same interface, different implementations!

### Historical Context

**Polymorphism** from **Simula 67** (1967) - virtual methods enable runtime dispatch. **Smalltalk** (1972) made all methods **virtual by default** - Python followed this design! **C++** requires `virtual` keyword - Python methods always overridable!

**Dynamic dispatch**: At runtime, Python looks up method in **object's class first**, then parent classes. This **method resolution order (MRO)** - Python 2.3 introduced **C3 linearization** (2003) to solve diamond problem in multiple inheritance!

**Liskov Substitution Principle** (Barbara Liskov, 1987): "Overridden methods must honor parent's contract". If parent's `speak()` returns string, child's override must too! **Contract preservation** - critical to polymorphism working correctly!

### Real-World Analogies

**Overriding like specialized employees**:
- **Employee.work()**: Generic "is working"
- **Developer.work()**: Override → "is coding"
- **Designer.work()**: Override → "is designing"
- **Manager.work()**: Override → "is managing"
**Same method name, different actions!**

**Or like payment methods**:
```python
class Payment:
    def process(self):
        return "Processing payment..."

class CreditCard(Payment):
    def process(self):  # Override
        return "Processing credit card..."

class PayPal(Payment):
    def process(self):  # Override
        return "Processing PayPal..."

class Crypto(Payment):
    def process(self):  # Override
        return "Processing crypto..."
# Same interface, different backends!
```

**Or like vehicle starting procedures**:
- **Vehicle.start()**: Generic "vehicle started"
- **Car.start()**: Override → "turn key, engine ignition"
- **ElectricCar.start()**: Override → "press power button, silent start"
- **Motorcycle.start()**: Override → "kickstand up, ignition, roar!"
**Each vehicle starts differently, but all START!**

### Overriding vs Overloading

**Overriding**: Same name, **different classes** (parent/child):
```python
class Parent:
    def method(self): pass
class Child(Parent):
    def method(self): pass  # Overrides parent!
```

**Overloading**: Same name, **different parameters** (Python doesn't support!):
```python
# Not possible in Python!
def add(a, b): pass
def add(a, b, c): pass  # Replaces first, doesn't overload!
```

**Python uses default parameters** instead of overloading!

---
### Understanding the Concept

Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class. This is a key aspect of polymorphism in object-oriented programming.

**Key concepts**: method overriding, polymorphism, customizing behavior

### Syntax and Usage

```python
class Parent:
    def method_name(self):
        # Parent implementation
        pass

class Child(Parent):
    def method_name(self):
        # Child implementation (overrides parent)
        pass
```

### Basic Method Overriding

```python
class Animal:
    def speak(self):
        return "Some sound"

    def move(self):
        return "Moving"

class Dog(Animal):
    def speak(self):  # Overriding speak method
        return "Woof!"

class Cat(Animal):
    def speak(self):  # Overriding speak method
        return "Meow!"

# Usage
animal = Animal()
dog = Dog()
cat = Cat()

print(animal.speak())  # Some sound
print(dog.speak())     # Woof!
print(cat.speak())     # Meow!
```

### Practical Examples

#### Example 1: Shape Area Calculation

```python
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def display_info(self):
        print(f"{self.name} - Area: {self.area()}")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):  # Override
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):  # Override
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):  # Override
        return 0.5 * self.base * self.height

# Usage
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(6, 8)
]

for shape in shapes:
    shape.display_info()
# Rectangle - Area: 50
# Circle - Area: 153.93791
# Triangle - Area: 24.0
```

#### Example 2: Employee Payment System

```python
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        return 0

    def display_info(self):
        print(f"Employee: {self.name} (ID: {self.employee_id})")
        print(f"Salary: ${self.calculate_salary()}")

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):  # Override
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):  # Override
        regular_hours = min(self.hours_worked, 40)
        overtime_hours = max(self.hours_worked - 40, 0)
        return (regular_hours * self.hourly_rate) + (overtime_hours * self.hourly_rate * 1.5)

class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales, commission_rate):
        super().__init__(name, employee_id)
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_salary(self):  # Override
        return self.base_salary + (self.sales * self.commission_rate)

# Usage
employees = [
    FullTimeEmployee("Alice", "E001", 5000),
    HourlyEmployee("Bob", "E002", 25, 45),
    CommissionEmployee("Charlie", "E003", 2000, 50000, 0.05)
]

for emp in employees:
    emp.display_info()
    print()
# Employee: Alice (ID: E001)
# Salary: $5000
#
# Employee: Bob (ID: E002)
# Salary: $1187.5
#
# Employee: Charlie (ID: E003)
# Salary: $4500
```

#### Example 3: Bank Account Types

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return True
        return False

    def get_interest(self):
        return 0

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def get_interest(self):  # Override
        return self.balance * self.interest_rate

    def withdraw(self, amount):  # Override with restriction
        if self.balance - amount < 500:  # Minimum balance requirement
            print("Cannot withdraw: Minimum balance of $500 required")
            return False
        return super().withdraw(amount)

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):  # Override with overdraft
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            if self.balance < 0:
                print(f"Warning: Overdraft used. Balance: ${self.balance}")
            return True
        print("Insufficient funds including overdraft")
        return False

class PremiumAccount(SavingsAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, 0.05)  # 5% interest
        self.reward_points = 0

    def deposit(self, amount):  # Override to add rewards
        super().deposit(amount)
        self.reward_points += int(amount / 100)  # 1 point per $100
        print(f"Earned {int(amount / 100)} reward points!")
        return self.balance

# Usage
savings = SavingsAccount("SA001", 1000, 0.03)
checking = CheckingAccount("CA001", 500, 200)
premium = PremiumAccount("PA001", 5000)

print("Savings account interest:", savings.get_interest())  # 30.0
savings.withdraw(600)  # Cannot withdraw: Minimum balance of $500 required

checking.withdraw(600)  # Warning: Overdraft used. Balance: $-100

premium.deposit(1000)  # Earned 10 reward points!
print("Premium balance:", premium.balance)  # 6000
print("Premium interest:", premium.get_interest())  # 300.0
```

#### Example 4: Vehicle System

```python
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        return "Vehicle started"

    def stop(self):
        self.is_running = False
        return "Vehicle stopped"

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        self.trunk_open = False

    def start(self):  # Override
        if not self.trunk_open:
            self.is_running = True
            return "Car engine started"
        return "Cannot start: Close trunk first"

    def display_info(self):  # Override
        super().display_info()
        print(f"Doors: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc
        self.kickstand_up = False

    def start(self):  # Override
        if self.kickstand_up:
            self.is_running = True
            return "Motorcycle started with a roar!"
        return "Cannot start: Put kickstand up first"

    def display_info(self):  # Override
        super().display_info()
        print(f"Engine: {self.engine_cc}cc")

class ElectricCar(Car):
    def __init__(self, brand, model, year, num_doors, battery_capacity):
        super().__init__(brand, model, year, num_doors)
        self.battery_capacity = battery_capacity
        self.battery_level = 100

    def start(self):  # Override
        if self.battery_level > 0:
            self.is_running = True
            return "Electric car started silently"
        return "Cannot start: Battery empty"

    def display_info(self):  # Override
        super().display_info()
        print(f"Battery: {self.battery_capacity}kWh ({self.battery_level}% charged)")

# Usage
car = Car("Toyota", "Camry", 2023, 4)
motorcycle = Motorcycle("Harley", "Sportster", 2023, 883)
electric = ElectricCar("Tesla", "Model 3", 2023, 4, 75)

print(car.start())  # Car engine started
car.display_info()
# 2023 Toyota Camry
# Doors: 4

print()
motorcycle.kickstand_up = True
print(motorcycle.start())  # Motorcycle started with a roar!
motorcycle.display_info()
# 2023 Harley Sportster
# Engine: 883cc

print()
print(electric.start())  # Electric car started silently
electric.display_info()
# 2023 Tesla Model 3
# Doors: 4
# Battery: 75kWh (100% charged)
```

#### Example 5: Document Processing

```python
class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def format(self):
        return f"Title: {self.title}\n{self.content}"

    def word_count(self):
        return len(self.content.split())

class Report(Document):
    def __init__(self, title, content, author, date):
        super().__init__(title, content)
        self.author = author
        self.date = date

    def format(self):  # Override
        header = f"REPORT\n{'=' * 50}\n"
        header += f"Title: {self.title}\n"
        header += f"Author: {self.author}\n"
        header += f"Date: {self.date}\n"
        header += f"{'=' * 50}\n\n"
        return header + self.content

class Email(Document):
    def __init__(self, title, content, sender, recipient):
        super().__init__(title, content)
        self.sender = sender
        self.recipient = recipient

    def format(self):  # Override
        header = f"From: {self.sender}\n"
        header += f"To: {self.recipient}\n"
        header += f"Subject: {self.title}\n"
        header += "-" * 50 + "\n\n"
        return header + self.content

class Article(Document):
    def __init__(self, title, content, author, tags):
        super().__init__(title, content)
        self.author = author
        self.tags = tags
        self.views = 0

    def format(self):  # Override
        header = f"{self.title}\n"
        header += f"By {self.author}\n"
        header += f"Tags: {', '.join(self.tags)}\n"
        header += f"Views: {self.views}\n"
        header += "=" * 50 + "\n\n"
        return header + self.content

    def word_count(self):  # Override to exclude title
        return len(self.content.split())

# Usage
report = Report(
    "Q4 Sales Report",
    "Sales increased by 25% this quarter...",
    "John Doe",
    "2023-12-31"
)

email = Email(
    "Meeting Tomorrow",
    "Don't forget about the team meeting at 10 AM.",
    "boss@company.com",
    "team@company.com"
)

article = Article(
    "Python Best Practices",
    "Here are some tips for writing better Python code...",
    "Jane Smith",
    ["Python", "Programming", "Tutorial"]
)

print(report.format())
print("\n" + "=" * 50 + "\n")
print(email.format())
print("\n" + "=" * 50 + "\n")
print(article.format())
```

### Best Practices

1. **Keep the same signature**: Overridden methods should have the same parameters as the parent method
2. **Call parent when needed**: Use `super()` to extend functionality rather than replace it completely
3. **Maintain the contract**: Overridden methods should honor the parent class's expectations
4. **Document changes**: Clearly document how the overridden method differs from the parent
5. **Test thoroughly**: Ensure overridden methods work correctly in all contexts

### Common Mistakes

1. **Changing method signature**: Don't change the number or type of parameters when overriding
   ```python
   # Bad
   class Parent:
       def method(self, x):
           pass

   class Child(Parent):
       def method(self, x, y):  # Different signature!
           pass
   ```

2. **Forgetting to call super()**: When you want to extend behavior, not replace it
   ```python
   # Bad - loses parent functionality
   class Child(Parent):
       def method(self):
           # New code only
           pass

   # Good - extends parent functionality
   class Child(Parent):
       def method(self):
           super().method()  # Keep parent behavior
           # Add new code
   ```

### When to Use

Use method overriding when:
- Different subclasses need different implementations of the same operation
- You want to customize inherited behavior for specific subclasses
- Implementing polymorphism in your design
- Creating specialized versions of general classes

### Key Takeaways

1. Method overriding allows child classes to provide specific implementations
2. The overridden method has the same name and signature as the parent method
3. Use `super()` to call the parent method when needed
4. Overriding is essential for polymorphism
5. Child class methods can completely replace or extend parent methods
6. Proper overriding maintains the parent class contract
