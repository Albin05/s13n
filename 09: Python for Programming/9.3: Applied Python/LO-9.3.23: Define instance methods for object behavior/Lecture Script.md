# Lecture Script: LO-65 Define Instance Methods

## [0:00-0:02] Hook (2 min)
**Say**: "A dog can bark, run, and sit. A bank account can deposit, withdraw, and check balance. In OOP, these actions are called methods! Today we learn how to give our objects behavior — not just data, but actions they can perform."

**Demo**:
```python
class Dog:
    def bark(self):
        print("Woof!")

dog = Dog()
dog.bark()  # Woof!
```

**Say**: "That's a method! Let's master them."

## [0:02-0:06] Understanding self (4 min)

**Say**: "Every instance method needs a special parameter: self. Let me show you why."

**Live Code**:
```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1  # 'self' refers to THIS object

    def get_count(self):
        return self.count

# Create two separate counters
counter1 = Counter()
counter2 = Counter()

# Each has its own count!
counter1.increment()
counter1.increment()
counter2.increment()

print(counter1.get_count())  # 2
print(counter2.get_count())  # 1
```

**Point out**: "self lets each object maintain its own state. counter1 and counter2 are independent!"

**Emphasize**: "Python automatically passes the object as self — you never write counter1.increment(counter1). Just counter1.increment()!"

## [0:06-0:10] Methods with Parameters (4 min)

**Say**: "Methods can take parameters just like functions."

**Live Code**:
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

**Say**: "Notice: we define (self, a, b) but call calc.add(5, 3). Python automatically passes calc as self!"

## [0:10-0:14] Methods Accessing Attributes (4 min)

**Say**: "The real power: methods can read and modify the object's attributes using self."

**Live Code**:
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14159 * self.radius

    def scale(self, factor):
        self.radius *= factor  # Modify the radius!

circle = Circle(5)
print(f"Area: {circle.area():.2f}")  # 78.54

circle.scale(2)  # Double the radius
print(f"New area: {circle.area():.2f}")  # 314.16
```

**Point out**: "The scale method changed the radius, so area() returns a different value!"

## [0:14-0:18] Real-World Example: Bank Account (4 min)

**Say**: "Let's build something practical — a bank account with deposit and withdrawal."

**Live Code**:
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit must be positive!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal!")

    def get_balance(self):
        return self.balance

# Use it!
account = BankAccount("Alice", 1000)
account.deposit(500)   # Deposited $500. New balance: $1500
account.withdraw(200)  # Withdrew $200. New balance: $1300
account.withdraw(2000) # Invalid withdrawal!
print(f"Final balance: ${account.get_balance()}")
```

**Say**: "Notice how methods validate inputs, modify state, and provide controlled access to data!"

## [0:18-0:21] Methods Calling Other Methods (3 min)

**Say**: "Methods can call other methods using self!"

**Live Code**:
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
        print(f"Area: {self.area()}")           # Calling another method!
        print(f"Perimeter: {self.perimeter()}") # Calling another method!
        if self.is_square():                    # Calling another method!
            print("This is a square!")

rect = Rectangle(5, 5)
rect.display_info()
```

**Point out**: "display_info() uses other methods to avoid repeating logic. Clean and organized!"

## [0:21-0:23] Practice Challenge (2 min)

**Challenge**: "Create a Student class with methods to add grades and calculate average."

**Give them this skeleton**:
```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        # TODO: Add grade to the list
        pass

    def get_average(self):
        # TODO: Return average of all grades
        pass

# Test it:
alice = Student("Alice")
alice.add_grade(85)
alice.add_grade(92)
alice.add_grade(78)
print(f"{alice.name}'s average: {alice.get_average()}")
```

**Solution** (show after 1-2 minutes):
```python
def add_grade(self, grade):
    if 0 <= grade <= 100:
        self.grades.append(grade)

def get_average(self):
    if self.grades:
        return sum(self.grades) / len(self.grades)
    return 0
```

## [0:23-0:25] Wrap-up (2 min)

**Key Points**:
1. **Instance methods**: Functions defined inside a class
2. **self parameter**: Always first, refers to the current object
3. **Access attributes**: Use self.attribute_name
4. **Call methods**: Use self.method_name()
5. **Methods give behavior**: Objects can perform actions!

**Common Mistakes**:
- Forgetting `self` as the first parameter
- Forgetting `self.` when accessing attributes inside methods
- Trying to pass `self` explicitly when calling a method

**Closing**: "You now know how to give objects both data (attributes) and behavior (methods). This is the foundation of object-oriented programming! Next, we'll learn about inheritance to create even more powerful class hierarchies."
