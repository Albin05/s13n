# Lecture Notes: Use the super() Function

## Use the super() Function

Calling parent class methods from child classes


---

<div align="center">

![Function machine concept - input to output](https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?w=800&q=80)

*Functions are reusable blocks of code that take inputs and return outputs*

</div>

---

## Introduction

The `super()` function implements **cooperative inheritance** - calling parent methods while maintaining the inheritance chain! This is **method delegation** - extending behavior without duplicating code. `super()` is the **bridge between child and parent** - essential for proper OOP hierarchy!

### Why super() is Critical

**Problem without super()**: Duplicate parent code or break inheritance:
```python
# BAD - duplicates parent logic!
class Parent:
    def __init__(self, value):
        self.value = value
        print("Parent initialized")

class Child(Parent):
    def __init__(self, value, extra):
        # Duplicate parent logic!
        self.value = value
        print("Parent initialized")  # Copy-paste!
        self.extra = extra
# Fragile - if parent changes, child breaks!
```

**Solution with super()**: Delegate to parent properly:
```python
# GOOD - delegates to parent!
class Child(Parent):
    def __init__(self, value, extra):
        super().__init__(value)  # Parent handles its logic!
        self.extra = extra
# DRY - parent logic written once!
```

**This is delegation power** - parent knows how to initialize itself!

### Historical Context

**super() added in Python 2.2** (2001) for new-style classes. Before: manual `Parent.__init__(self)` calls - error-prone with multiple inheritance! **Old-style syntax**:
```python
# Python 2 - verbose!
super(ChildClass, self).__init__()
```

**Python 3 simplified** (2008): just `super().__init__()` - automatic class/self inference! **This syntactic sugar** makes cooperative inheritance elegant.

**Method Resolution Order (MRO)**: Python uses **C3 linearization** (Python 2.3, 2003) to determine which parent method `super()` calls. Solves **diamond problem** in multiple inheritance - ensures each class initialized exactly once!

### Real-World Analogies

**super() like hierarchical management**:
- **Employee.work()**: General "is working"
- **Manager.work()**: Calls `super().work()` (still working) + "is managing team"
- **Senior Manager.work()**: Calls `super().work()` (includes Manager + Employee) + "is setting strategy"
**Each level adds responsibilities, doesn't replace them!**

**Or like building construction**:
```python
class Foundation:
    def __init__(self):
        print("Pour foundation")

class Walls(Foundation):
    def __init__(self):
        super().__init__()  # Foundation first!
        print("Build walls")

class Roof(Walls):
    def __init__(self):
        super().__init__()  # Walls (which builds foundation)!
        print("Add roof")
# Build in correct order automatically!
```

**Or like recipe inheritance**:
- **BasicCake**: Mix ingredients, bake
- **ChocolateCake**: super() for basic steps + add chocolate
- **FancyChocolateCake**: super() for chocolate steps + add decorations
**Each recipe builds on previous, doesn't start from scratch!**

### super() vs Direct Parent Call

**Direct parent call**: Hardcoded, breaks with changes:
```python
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)  # Brittle!
# If inheritance changes, must update every call!
```

**super() call**: Flexible, follows MRO:
```python
class Child(Parent):
    def __init__(self):
        super().__init__()  # Adapts automatically!
# Inheritance changes? super() handles it!
```

**This is future-proofing** - super() respects inheritance structure!

---
### Understanding the Concept

The `super()` function is a built-in Python function that allows you to call methods from a parent class within a child class. It's essential for extending functionality while maintaining the parent's behavior.

**Key concepts**: super().__init__(), super().method(), extending functionality, method resolution order

### Syntax and Usage

```python
class Parent:
    def __init__(self, value):
        self.value = value

class Child(Parent):
    def __init__(self, value, extra):
        super().__init__(value)  # Call parent constructor
        self.extra = extra
```

### Basic super() Usage

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {name}")

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent __init__
        self.breed = breed
        print(f"Dog breed: {breed}")

    def speak(self):
        parent_sound = super().speak()  # Call parent method
        return f"{parent_sound} - Woof!"

# Usage
dog = Dog("Buddy", "Golden Retriever")
# Animal created: Buddy
# Dog breed: Golden Retriever

print(dog.speak())  # Some sound - Woof!
```

### Practical Examples

#### Example 1: Employee Hierarchy

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)  # Initialize Person attributes
        self.employee_id = employee_id
        self.salary = salary

    def introduce(self):
        base_intro = super().introduce()  # Get parent introduction
        return f"{base_intro}. Employee ID: {self.employee_id}"

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)  # Initialize Employee
        self.department = department
        self.team = []

    def introduce(self):
        emp_intro = super().introduce()  # Get Employee introduction
        return f"{emp_intro}. I manage the {self.department} department"

    def add_team_member(self, employee):
        self.team.append(employee)
        print(f"{employee.name} added to {self.name}'s team")

# Usage
person = Person("Alice", 30)
print(person.introduce())
# Hi, I'm Alice, 30 years old

employee = Employee("Bob", 35, "E001", 50000)
print(employee.introduce())
# Hi, I'm Bob, 35 years old. Employee ID: E001

manager = Manager("Charlie", 40, "M001", 75000, "Engineering")
print(manager.introduce())
# Hi, I'm Charlie, 40 years old. Employee ID: M001. I manage the Engineering department

manager.add_team_member(employee)
# Bob added to Charlie's team
```

#### Example 2: Bank Account with Transaction History

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []
        print(f"Account {account_number} created with balance ${balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
            return True
        print("Insufficient funds")
        return False

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)  # Create base account
        self.interest_rate = interest_rate
        self.minimum_balance = 500
        print(f"Savings account interest rate: {interest_rate * 100}%")

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print(f"Cannot withdraw: Minimum balance ${self.minimum_balance} required")
            return False
        return super().withdraw(amount)  # Call parent withdraw

    def add_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Adding interest: ${interest:.2f}")
        super().deposit(interest)  # Use parent deposit method

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
        self.monthly_fee = 10
        print(f"Checking account with ${overdraft_limit} overdraft limit")

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            if self.balance < 0:
                print(f"Overdraft used: ${abs(self.balance)}")
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
            return True
        print("Insufficient funds including overdraft")
        return False

    def charge_monthly_fee(self):
        print(f"Charging monthly fee: ${self.monthly_fee}")
        super().withdraw(self.monthly_fee)  # Use parent withdraw

# Usage
savings = SavingsAccount("SA001", 1000, 0.03)
# Account SA001 created with balance $1000
# Savings account interest rate: 3.0%

savings.withdraw(400)  # Withdrew $400. New balance: $600
savings.withdraw(200)  # Cannot withdraw: Minimum balance $500 required
savings.add_interest()
# Adding interest: $18.00
# Deposited $18.00. New balance: $618.0

print()
checking = CheckingAccount("CA001", 500, 200)
# Account CA001 created with balance $500
# Checking account with $200 overdraft limit

checking.withdraw(600)
# Overdraft used: $100
# Withdrew $600. New balance: $-100

checking.deposit(200)  # Deposited $200. New balance: $100
checking.charge_monthly_fee()
# Charging monthly fee: $10
# Withdrew $10. New balance: $90
```

#### Example 3: Shape Hierarchy with Validation

```python
class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.validate()

    def validate(self):
        if not self.name:
            raise ValueError("Shape must have a name")
        print(f"Creating {self.color} {self.name}")

    def area(self):
        return 0

    def display(self):
        print(f"{self.color} {self.name} - Area: {self.area()}")

class Rectangle(Shape):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        super().__init__("Rectangle", color)  # Call Shape init

    def validate(self):
        super().validate()  # Call parent validation
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive")

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)  # Rectangle with equal sides
        self.name = "Square"

    def display(self):
        super().display()  # Call Rectangle display
        print(f"Side length: {self.width}")

class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        super().__init__("Circle", color)

    def validate(self):
        super().validate()
        if self.radius <= 0:
            raise ValueError("Radius must be positive")

    def area(self):
        return 3.14159 * self.radius ** 2

# Usage
rect = Rectangle(5, 10, "blue")
# Creating blue Rectangle

rect.display()
# blue Rectangle - Area: 50

square = Square(5, "red")
# Creating red Rectangle

square.display()
# red Square - Area: 25
# Side length: 5

circle = Circle(7, "green")
# Creating green Circle

circle.display()
# green Circle - Area: 153.93791
```

#### Example 4: Game Character System

```python
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.level = 1
        print(f"Character '{name}' created with {health} HP")

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage. HP: {self.health}/{self.max_health}")

    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)
        print(f"{self.name} healed {amount}. HP: {self.health}/{self.max_health}")

    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to {self.level}!")

class Warrior(Character):
    def __init__(self, name, health, armor):
        super().__init__(name, health)  # Initialize Character
        self.armor = armor
        self.rage = 0
        print(f"Warrior armor: {armor}")

    def take_damage(self, damage):
        reduced_damage = max(damage - self.armor, 0)
        super().take_damage(reduced_damage)  # Call parent with reduced damage
        self.rage += 10
        print(f"Rage: {self.rage}")

    def level_up(self):
        super().level_up()  # Call parent level up
        self.max_health += 20
        self.health = self.max_health
        self.armor += 2
        print(f"HP increased to {self.max_health}, Armor increased to {self.armor}")

class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana
        self.max_mana = mana
        self.spells_cast = 0
        print(f"Mage mana: {mana}")

    def cast_spell(self, mana_cost, damage):
        if self.mana >= mana_cost:
            self.mana -= mana_cost
            self.spells_cast += 1
            print(f"{self.name} cast spell! Mana: {self.mana}/{self.max_mana}")
            return damage
        print("Not enough mana!")
        return 0

    def heal(self, amount):
        super().heal(amount)  # Call parent heal
        mana_restore = amount // 2
        self.mana = min(self.mana + mana_restore, self.max_mana)
        print(f"Mana restored: {mana_restore}. Mana: {self.mana}/{self.max_mana}")

    def level_up(self):
        super().level_up()
        self.max_mana += 30
        self.mana = self.max_mana
        print(f"Mana increased to {self.max_mana}")

class Paladin(Warrior):
    def __init__(self, name, health, armor, faith):
        super().__init__(name, health, armor)  # Initialize Warrior
        self.faith = faith
        print(f"Paladin faith: {faith}")

    def holy_heal(self):
        heal_amount = self.faith * 5
        print(f"{self.name} uses holy healing!")
        super().heal(heal_amount)  # Call Character's heal via Warrior

    def level_up(self):
        super().level_up()  # Call Warrior level up
        self.faith += 3
        print(f"Faith increased to {self.faith}")

# Usage
warrior = Warrior("Conan", 150, 10)
# Character 'Conan' created with 150 HP
# Warrior armor: 10

warrior.take_damage(30)
# Conan took 20 damage. HP: 130/150
# Rage: 10

print()
mage = Mage("Gandalf", 80, 120)
# Character 'Gandalf' created with 80 HP
# Mage mana: 120

damage = mage.cast_spell(30, 50)
# Gandalf cast spell! Mana: 90/120

mage.heal(20)
# Gandalf healed 20. HP: 80/80
# Mana restored: 10. Mana: 100/120

print()
paladin = Paladin("Arthas", 130, 12, 15)
# Character 'Arthas' created with 130 HP
# Warrior armor: 12
# Paladin faith: 15

paladin.take_damage(40)
# Arthas took 28 damage. HP: 102/130
# Rage: 10

paladin.holy_heal()
# Arthas uses holy healing!
# Arthas healed 75. HP: 130/130

paladin.level_up()
# Arthas leveled up to 2!
# HP increased to 150, Armor increased to 14
# Faith increased to 18
```

#### Example 5: Product Inventory System

```python
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.validate_price()

    def validate_price(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

    def get_display_price(self):
        return f"${self.price:.2f}"

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"ID: {self.product_id}")
        print(f"Price: {self.get_display_price()}")

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, weight, stock):
        super().__init__(product_id, name, price)
        self.weight = weight
        self.stock = stock

    def calculate_shipping(self, distance):
        base_cost = 5.0
        weight_cost = self.weight * 0.5
        distance_cost = distance * 0.1
        return base_cost + weight_cost + distance_cost

    def display_info(self):
        super().display_info()  # Show basic product info
        print(f"Weight: {self.weight} kg")
        print(f"Stock: {self.stock} units")

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, file_size, download_link):
        super().__init__(product_id, name, price)
        self.file_size = file_size
        self.download_link = download_link
        self.downloads = 0

    def get_display_price(self):
        base_price = super().get_display_price()  # Get formatted price
        return f"{base_price} (Digital Download)"

    def download(self):
        self.downloads += 1
        print(f"Downloading from: {self.download_link}")
        print(f"Total downloads: {self.downloads}")

    def display_info(self):
        super().display_info()
        print(f"File size: {self.file_size} MB")
        print(f"Downloads: {self.downloads}")

class SubscriptionProduct(DigitalProduct):
    def __init__(self, product_id, name, monthly_price, file_size, download_link, billing_period):
        super().__init__(product_id, name, monthly_price, file_size, download_link)
        self.billing_period = billing_period

    def get_display_price(self):
        return f"${self.price:.2f}/{self.billing_period}"

    def display_info(self):
        super().display_info()  # Show digital product info
        print(f"Billing: {self.billing_period}")

# Usage
physical = PhysicalProduct("P001", "Laptop", 999.99, 2.5, 10)
physical.display_info()
# Product: Laptop
# ID: P001
# Price: $999.99
# Weight: 2.5 kg
# Stock: 10 units

shipping = physical.calculate_shipping(100)
print(f"Shipping cost: ${shipping:.2f}\n")
# Shipping cost: $16.25

digital = DigitalProduct("D001", "Python Course", 49.99, 1200, "http://download.link")
digital.display_info()
# Product: Python Course
# ID: D001
# Price: $49.99 (Digital Download)
# File size: 1200 MB
# Downloads: 0

digital.download()
# Downloading from: http://download.link
# Total downloads: 1

print()
subscription = SubscriptionProduct("S001", "Streaming Service", 9.99, 0, "http://stream.link", "monthly")
subscription.display_info()
# Product: Streaming Service
# ID: S001
# Price: $9.99/monthly
# File size: 0 MB
# Downloads: 0
# Billing: monthly
```

### Best Practices

1. **Always call super().__init__()**: In child class constructors to properly initialize parent attributes
2. **Call super() early**: Usually call parent methods at the start of child methods
3. **Extend, don't replace**: Use super() to add functionality while keeping parent behavior
4. **Be explicit**: Clear about which parent method you're calling
5. **Multiple inheritance**: super() handles complex inheritance hierarchies correctly

### Common Mistakes

1. **Forgetting to call super().__init__()**:
   ```python
   # Bad - parent not initialized
   class Child(Parent):
       def __init__(self, value, extra):
           self.extra = extra  # Parent attributes not set!

   # Good
   class Child(Parent):
       def __init__(self, value, extra):
           super().__init__(value)  # Initialize parent first
           self.extra = extra
   ```

2. **Calling parent class directly instead of super()**:
   ```python
   # Works but not recommended
   class Child(Parent):
       def __init__(self, value):
           Parent.__init__(self, value)

   # Better - handles multiple inheritance correctly
   class Child(Parent):
       def __init__(self, value):
           super().__init__(value)
   ```

3. **Not passing required arguments**:
   ```python
   # Bad
   class Child(Parent):
       def __init__(self, extra):
           super().__init__()  # Parent expects arguments!
           self.extra = extra

   # Good
   class Child(Parent):
       def __init__(self, required, extra):
           super().__init__(required)  # Pass parent's arguments
           self.extra = extra
   ```

### When to Use

Use super() when:
- Initializing parent class attributes in `__init__`
- Extending parent methods while keeping their functionality
- Working with multiple inheritance
- You want to maintain the method resolution order (MRO)

### Key Takeaways

1. `super()` calls methods from the parent class
2. Essential for proper initialization of parent attributes
3. Allows extending functionality without losing parent behavior
4. Handles complex inheritance hierarchies correctly
5. Use `super().__init__()` in child constructors
6. Can call any parent method with `super().method_name()`
7. Promotes code reuse and maintainability
