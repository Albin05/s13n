# Editorials: Use the super() Function

## Problem 1
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

# Test the class
student = Student("Alice", 20, "S12345")
print(f"Name: {student.name}")
print(f"Age: {student.age}")
print(f"Student ID: {student.student_id}")
```

### Explanation
- `super()` provides access to the parent class without naming it explicitly
- `super().__init__(name, age)` calls the parent's `__init__` method
- This avoids code duplication - we don't need to rewrite the initialization logic
- After calling `super().__init__()`, we can add child-specific initialization
- This is the proper way to extend parent initialization in child classes
- `super()` makes code more maintainable - if parent class name changes, child still works

## Problem 2
```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def describe(self):
        print(f"Rectangle: {self.length} x {self.width}")

class ColoredRectangle(Rectangle):
    def __init__(self, length, width, color):
        super().__init__(length, width)
        self.color = color

    def describe(self):
        super().describe()
        print(f"Color: {self.color}")

# Test the class
rect = ColoredRectangle(10, 5, "blue")
rect.describe()
```

### Explanation
- `super()` can be used to call any parent method, not just `__init__`
- In `describe()`, we first call the parent's version using `super().describe()`
- Then we add additional functionality (printing the color)
- This extends parent behavior rather than replacing it completely
- The pattern is: call parent method, then add child-specific logic
- This promotes code reuse and maintains parent functionality

## Problem 3
```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

class InterestAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        # Call parent deposit first
        super().deposit(amount)

        # Calculate and add interest
        interest = amount * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest earned: ${interest:.2f}. New balance: ${self.balance:.2f}")

# Test the class
account = InterestAccount("12345", 1000, 5)
print("Initial balance:", account.balance)
print()

account.deposit(500)
print()
account.deposit(200)
```

### Explanation
- The child's `deposit()` first calls `super().deposit(amount)` to execute parent logic
- This ensures the parent's deposit functionality is preserved
- After parent's deposit completes, child adds interest calculation
- Using `super()` avoids duplicating the deposit logic
- The balance is updated twice: once by parent, once for interest
- This demonstrates extending method behavior while reusing parent code

## Problem 4
```python
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        base = super().calculate_salary()
        return base + self.bonus

class SalesRep(Employee):
    def __init__(self, name, base_salary, commission):
        super().__init__(name, base_salary)
        self.commission = commission

    def calculate_salary(self):
        base = super().calculate_salary()
        return base + self.commission

class Executive(Manager):
    def __init__(self, name, base_salary, bonus, stock_options):
        super().__init__(name, base_salary, bonus)
        self.stock_options = stock_options

    def calculate_salary(self):
        manager_salary = super().calculate_salary()
        return manager_salary + self.stock_options

# Test the classes
employee = Employee("John", 50000)
print(f"{employee.name}'s salary: ${employee.calculate_salary()}")

manager = Manager("Sarah", 60000, 10000)
print(f"{manager.name}'s salary: ${manager.calculate_salary()}")

sales = SalesRep("Mike", 45000, 15000)
print(f"{sales.name}'s salary: ${sales.calculate_salary()}")

executive = Executive("Lisa", 80000, 20000, 30000)
print(f"{executive.name}'s salary: ${executive.calculate_salary()}")
print("\nExecutive salary breakdown:")
print(f"  Base: ${executive.base_salary}")
print(f"  Bonus: ${executive.bonus}")
print(f"  Stock: ${executive.stock_options}")
print(f"  Total: ${executive.calculate_salary()}")
```

### Explanation
- Multi-level inheritance: `Executive` inherits from `Manager`, which inherits from `Employee`
- Each level uses `super().calculate_salary()` to get the parent's calculation
- `Executive.calculate_salary()` calls `Manager.calculate_salary()`, which calls `Employee.calculate_salary()`
- This creates a chain: Employee base → Manager adds bonus → Executive adds stock options
- Each class adds its own logic on top of the parent's result
- `super()` makes the chain work seamlessly across multiple inheritance levels
- Changing parent logic automatically affects all children

## Problem 5
```python
from datetime import datetime

class Logger:
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Logger: {message}")

class FileLogger(Logger):
    def log(self, message):
        print("  → FileLogger: Calling parent...")
        super().log(message)
        print("  → FileLogger: Writing to file: log.txt")

class EmailLogger(FileLogger):
    def log(self, message):
        print("  → EmailLogger: Calling parent...")
        super().log(message)
        print("  → EmailLogger: Sending email to admin@example.com")

class AlertLogger(EmailLogger):
    def log(self, message):
        print("  → AlertLogger: Calling parent...")
        super().log(message)
        print("  → AlertLogger: Triggering alert notification")

# Test the logging system
print("=== Creating AlertLogger ===")
logger = AlertLogger()

print("\n=== Logging a critical message ===")
print("Execution flow:")
logger.log("CRITICAL: System failure detected!")

print("\n" + "="*50)
print("Order of execution:")
print("1. AlertLogger.log() starts")
print("2. Calls super() -> EmailLogger.log()")
print("3. EmailLogger calls super() -> FileLogger.log()")
print("4. FileLogger calls super() -> Logger.log()")
print("5. Logger.log() executes (base implementation)")
print("6. Returns to FileLogger, writes to file")
print("7. Returns to EmailLogger, sends email")
print("8. Returns to AlertLogger, triggers alert")
```

### Explanation
- This demonstrates cascading `super()` calls through multiple inheritance levels
- Each class calls `super().log()` before adding its own functionality
- The call chain: AlertLogger → EmailLogger → FileLogger → Logger
- Logger (base class) executes first, then control returns up the chain
- Each level adds its functionality as control returns from `super()`
- This creates a "wrapper" pattern where each level wraps the parent's behavior
- The execution order is: down to base (via super), then up (adding functionality)
- All four log implementations execute from a single `logger.log()` call
- This demonstrates the power of `super()` in creating extensible, layered functionality

**Key Concepts**:
1. **super()** provides access to parent class methods without naming the parent
2. **Code reuse**: calling parent methods avoids duplicating code
3. **Extension vs replacement**: `super()` extends behavior instead of replacing it
4. **Initialization chaining**: `super().__init__()` properly initializes parent attributes
5. **Method chaining**: multiple inheritance levels can chain calls using `super()`
6. **Execution flow**: `super()` calls go down to base, execution happens on the way back up
7. **Maintainability**: changing parent class name doesn't break child classes using `super()`
