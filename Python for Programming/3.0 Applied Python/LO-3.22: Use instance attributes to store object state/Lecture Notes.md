# Lecture Notes: Use Instance Attributes

## Instance Attributes

Instance attributes are variables that belong to a specific object. Each object has its own copy of instance attributes.


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---
### Syntax

```python
class ClassName:
    def __init__(self, param):
        self.attribute_name = param  # Instance attribute
```

## Creating and Accessing Attributes

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

alice = Person("Alice", 25)
bob = Person("Bob", 30)

print(alice.name)  # Alice
print(bob.name)    # Bob
print(alice.age)   # 25
print(bob.age)     # 30
```

## Each Object Has Independent Attributes

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Max", "German Shepherd")

print(dog1.name)   # Buddy
print(dog2.name)   # Max
print(dog1.breed)  # Labrador
print(dog2.breed)  # German Shepherd
```

## Modifying Attributes

```python
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.mileage = 0

my_car = Car("Toyota", 2020)
print(my_car.mileage)  # 0

# Modify attribute
my_car.mileage = 15000
print(my_car.mileage)  # 15000

# Modify another attribute
my_car.year = 2021
print(my_car.year)  # 2021
```

## Attributes Created Outside __init__

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

student = Student("Alice")

# Add new attribute
student.gpa = 3.8
print(student.gpa)  # 3.8

# Note: Not recommended! Better to define in __init__
```

## Real-World Examples

### Example 1: Bank Account

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: ${amount}")
        else:
            print("Insufficient funds!")
    
    def show_info(self):
        print(f"Account Owner: {self.owner}")
        print(f"Balance: ${self.balance}")
        print(f"Transactions: {len(self.transactions)}")

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
account.show_info()
# Account Owner: Alice
# Balance: $1300
# Transactions: 2
```

### Example 2: Product Inventory

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_value = price * quantity
    
    def restock(self, amount):
        self.quantity += amount
        self.total_value = self.price * self.quantity
        print(f"Restocked {amount} units. New quantity: {self.quantity}")
    
    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            self.total_value = self.price * self.quantity
            print(f"Sold {amount} units. Remaining: {self.quantity}")
        else:
            print(f"Only {self.quantity} units available!")
    
    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: ${self.total_value}")

laptop = Product("Laptop", 999, 50)
laptop.sell(10)
laptop.restock(20)
laptop.display()
```

### Example 3: Student Record

```python
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.courses = []
        self.gpa = 0.0
    
    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")
    
    def set_gpa(self, gpa):
        self.gpa = gpa
        print(f"GPA updated to {gpa}")
    
    def get_info(self):
        return f"{self.name} (ID: {self.student_id}), Grade {self.grade}, GPA: {self.gpa}, Courses: {len(self.courses)}"

alice = Student("Alice", "S001", 10)
alice.enroll("Math")
alice.enroll("Science")
alice.set_gpa(3.8)
print(alice.get_info())
```

### Example 4: Temperature Sensor

```python
class TemperatureSensor:
    def __init__(self, location):
        self.location = location
        self.current_temp = 0
        self.readings = []
        self.alerts = []
    
    def record(self, temp):
        self.current_temp = temp
        self.readings.append(temp)
        
        if temp > 30:
            alert = f"High temperature alert: {temp}°C"
            self.alerts.append(alert)
            print(alert)
        elif temp < 0:
            alert = f"Freezing alert: {temp}°C"
            self.alerts.append(alert)
            print(alert)
    
    def get_average(self):
        if self.readings:
            return sum(self.readings) / len(self.readings)
        return 0
    
    def report(self):
        print(f"Sensor Location: {self.location}")
        print(f"Current: {self.current_temp}°C")
        print(f"Average: {self.get_average():.1f}°C")
        print(f"Total Readings: {len(self.readings)}")
        print(f"Alerts: {len(self.alerts)}")

sensor = TemperatureSensor("Living Room")
sensor.record(22)
sensor.record(25)
sensor.record(35)
sensor.record(-2)
sensor.report()
```

### Example 5: Shopping List

```python
class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.completed_items = []
        self.created_date = "2024-01-01"
    
    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item}")
    
    def complete_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.completed_items.append(item)
            print(f"Completed: {item}")
        else:
            print(f"{item} not in list!")
    
    def show_list(self):
        print(f"\nShopping List: {self.name}")
        print(f"Created: {self.created_date}")
        print(f"\nTodo ({len(self.items)}):")
        for item in self.items:
            print(f"  - {item}")
        print(f"\nCompleted ({len(self.completed_items)}):")
        for item in self.completed_items:
            print(f"  ✓ {item}")

groceries = ShoppingList("Weekly Groceries")
groceries.add_item("Milk")
groceries.add_item("Bread")
groceries.add_item("Eggs")
groceries.complete_item("Milk")
groceries.show_list()
```

## Accessing Attributes from Methods

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height  # Access attributes with self
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def scale(self, factor):
        self.width *= factor
        self.height *= factor

rect = Rectangle(5, 3)
print(rect.area())       # 15
print(rect.perimeter())  # 16
rect.scale(2)
print(rect.area())       # 60
```

## Private Attributes (Convention)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # "Private" (name mangling)
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
# account.__balance  # AttributeError (can't access directly)
print(account.get_balance())  # 1000 (use method)
```

## Key Takeaways

1. **Instance attributes**: Belong to specific objects
2. **self.attribute**: Created with self in __init__
3. **Independent**: Each object has own copy
4. **Access with dot**: object.attribute
5. **Modify anytime**: Can change attribute values
6. **Use in methods**: Access with self.attribute
7. **Private convention**: __attribute for "private" attributes
