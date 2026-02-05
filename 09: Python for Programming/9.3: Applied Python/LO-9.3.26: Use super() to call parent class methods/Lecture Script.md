# Lecture Script: LO-68 Use the super() Function

## [0:00-0:02] Hook (2 min)
**Say**: "Imagine building a robot. You have a basic Robot class that can walk and talk. Now you want to build a DancingRobot that can do everything a Robot can do PLUS dance. You don't want to copy-paste all the Robot code! That's where super() comes in — it lets you use the parent's code while adding your own."

**Demo**:
```python
class Robot:
    def __init__(self, name):
        self.name = name
        print(f"Robot {name} created")

class DancingRobot(Robot):
    def __init__(self, name, dance_style):
        super().__init__(name)  # Call parent's __init__!
        self.dance_style = dance_style
        print(f"Can dance {dance_style}")

robot = DancingRobot("Bender", "breakdance")
# Robot Bender created
# Can dance breakdance
```

**Say**: "super() calls the parent class's method. Let's master it!"

## [0:02-0:06] Understanding super() in __init__ (4 min)

**Say**: "The most common use of super() is in constructors. Watch what happens WITHOUT super():"

**Live Code**:
```python
# Without super() - WRONG!
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed  # Parent attributes NOT initialized!

dog = Dog("Golden Retriever")
print(dog.breed)    # Works
# print(dog.name)   # AttributeError! name not set
```

**Say**: "The dog has no name or age! The parent's __init__ never ran."

**Now show with super()**:
```python
# With super() - CORRECT!
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Animal created: {name}, {age} years old")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Initialize parent!
        self.breed = breed
        print(f"Dog breed: {breed}")

dog = Dog("Buddy", 3, "Golden Retriever")
# Animal created: Buddy, 3 years old
# Dog breed: Golden Retriever

print(f"Name: {dog.name}, Age: {dog.age}, Breed: {dog.breed}")
# Name: Buddy, Age: 3, Breed: Golden Retriever
```

**Point out**: "super().__init__() calls the parent's constructor first, THEN we add dog-specific attributes!"

**Emphasize**: "ALWAYS call super().__init__() in child constructors to properly initialize parent attributes!"

## [0:06-0:10] Using super() with Regular Methods (4 min)

**Say**: "super() isn't just for __init__! You can call ANY parent method."

**Live Code**:
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} salary increased by ${amount}")

    def display_info(self):
        print(f"Employee: {self.name}")
        print(f"Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.bonus = 0

    def give_raise(self, amount):
        super().give_raise(amount)  # Call parent's give_raise!
        self.bonus += amount * 0.1  # Add 10% bonus
        print(f"Bonus increased by ${amount * 0.1}")

    def display_info(self):
        super().display_info()  # Call parent's display!
        print(f"Department: {self.department}")
        print(f"Bonus: ${self.bonus}")

# Test it
mgr = Manager("Alice", 80000, "Engineering")
mgr.give_raise(5000)
# Alice salary increased by $5000
# Bonus increased by $500.0

print()
mgr.display_info()
# Employee: Alice
# Salary: $85000
# Department: Engineering
# Bonus: $500.0
```

**Say**: "Manager's methods use super() to call Employee's methods, then add extra functionality. No code duplication!"

## [0:10-0:14] Real-World Example: Bank Account Hierarchy (4 min)

**Say**: "Let's build a realistic bank account system with savings and checking accounts."

**Live Code**:
```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []
        print(f"Account {account_number} created with ${balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")
        print(f"Deposited ${amount}. Balance: ${self.balance}")

    def get_statement(self):
        print(f"\nAccount: {self.account_number}")
        print(f"Balance: ${self.balance}")
        print("Transactions:")
        for trans in self.transactions:
            print(f"  {trans}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
        print(f"Savings account. Interest rate: {interest_rate}%")

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print(f"\nAdding interest: ${interest:.2f}")
        super().deposit(interest)  # Use parent's deposit!

    def get_statement(self):
        super().get_statement()  # Call parent statement
        print(f"Interest Rate: {self.interest_rate}%")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, monthly_fee):
        super().__init__(account_number, balance)
        self.monthly_fee = monthly_fee
        print(f"Checking account. Monthly fee: ${monthly_fee}")

    def charge_fee(self):
        print(f"\nCharging monthly fee: ${self.monthly_fee}")
        self.balance -= self.monthly_fee
        self.transactions.append(f"Fee: -${self.monthly_fee}")
        print(f"Balance: ${self.balance}")

    def get_statement(self):
        super().get_statement()
        print(f"Monthly Fee: ${self.monthly_fee}")

# Test
savings = SavingsAccount("SA001", 1000, 3)
# Account SA001 created with $1000
# Savings account. Interest rate: 3%

savings.deposit(500)
# Deposited $500. Balance: $1500

savings.add_interest()
# Adding interest: $45.00
# Deposited $45.0. Balance: $1545.0

savings.get_statement()
# Account: SA001
# Balance: $1545.0
# Transactions:
#   Deposit: +$500
#   Deposit: +$45.0
# Interest Rate: 3%
```

**Say**: "See how savings.add_interest() uses super().deposit()? It reuses the parent's logic instead of duplicating code!"

## [0:14-0:18] Multi-Level Inheritance with super() (4 min)

**Say**: "super() works beautifully with multiple inheritance levels. It follows the Method Resolution Order (MRO)."

**Live Code**:
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle: {brand}")

    def start(self):
        print(f"{self.brand} starting...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call Vehicle
        self.model = model
        print(f"Car model: {model}")

    def start(self):
        super().start()  # Call Vehicle's start
        print("Engine started")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Call Car
        self.battery_size = battery_size
        print(f"Battery: {battery_size}kWh")

    def start(self):
        print("Checking battery...")
        super().start()  # Call Car's start
        print("Electric motor engaged")

# Test
tesla = ElectricCar("Tesla", "Model 3", 75)
# Vehicle: Tesla
# Car model: Model 3
# Battery: 75kWh

print()
tesla.start()
# Checking battery...
# Tesla starting...
# Engine started
# Electric motor engaged
```

**Point out**: "Each class calls super(), which calls the next class up. Vehicle → Car → ElectricCar. Python handles the chain automatically!"

**Show MRO**:
```python
print(ElectricCar.__mro__)
# (<class 'ElectricCar'>, <class 'Car'>, <class 'Vehicle'>, <class 'object'>)
```

**Say**: "This is the Method Resolution Order. super() follows this chain!"

## [0:18-0:21] Common Use Cases for super() (3 min)

**Say**: "Let's see the most common patterns with super()."

**Live Code**:
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name}: ${self.price}")

class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)  # Pattern 1: Initialize parent
        self.discount = discount
        self.final_price = price * (1 - discount)

    def display(self):
        super().display()  # Pattern 2: Call parent method first
        print(f"Discount: {self.discount * 100}%")
        print(f"Final price: ${self.final_price:.2f}")

class PremiumProduct(DiscountedProduct):
    def __init__(self, name, price, discount, warranty):
        super().__init__(name, price, discount)  # Pattern 3: Chain calls
        self.warranty = warranty

    def display(self):
        super().display()
        print(f"Warranty: {self.warranty} years")

# Test
product = PremiumProduct("Laptop", 1000, 0.1, 2)
product.display()
# Laptop: $1000
# Discount: 10.0%
# Final price: $900.00
# Warranty: 2 years
```

**Say**: "Three key patterns: 1) Initialize parent in __init__, 2) Call parent method first, 3) Chain through multiple levels!"

## [0:21-0:23] Practice Challenge (2 min)

**Challenge**: "Create a Student class with name and grade. Create HonorsStudent that adds GPA and uses super() properly."

**Skeleton**:
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Student: {self.name}, Grade: {self.grade}")

class HonorsStudent(Student):
    def __init__(self, name, grade, gpa):
        # TODO: Use super() to initialize parent
        pass

    def display_info(self):
        # TODO: Use super() to call parent display, then add GPA
        pass

# Test
student = HonorsStudent("Alice", 12, 3.8)
student.display_info()
# Should print:
# Student: Alice, Grade: 12
# GPA: 3.8
```

**Solution** (show after 1-2 minutes):
```python
def __init__(self, name, grade, gpa):
    super().__init__(name, grade)
    self.gpa = gpa

def display_info(self):
    super().display_info()
    print(f"GPA: {self.gpa}")
```

## [0:23-0:25] Wrap-up (2 min)

**Key Points**:
1. **super().__init__()**: ALWAYS call in child constructors to initialize parent
2. **super().method()**: Call parent's version of any method
3. **Extends, not replaces**: Add to parent's functionality
4. **Works with MRO**: Handles multi-level inheritance automatically
5. **Avoid duplication**: Reuse parent code instead of copying it

**Common Mistakes**:
- Forgetting super().__init__() in child constructor
- Not passing required arguments to parent's __init__
- Calling parent directly (Parent.__init__) instead of super()
- Forgetting super() is a function — need parentheses: super().method()

**When to Use super()**:
- Every child __init__ to initialize parent attributes
- To extend parent methods while keeping their functionality
- When you want to call the parent's version of an overridden method
- In multiple inheritance scenarios

**Closing**: "super() is your best friend for clean inheritance! It prevents code duplication and makes your classes maintainable. Remember: super() lets you stand on the shoulders of giants — use parent functionality and build on top of it!"
