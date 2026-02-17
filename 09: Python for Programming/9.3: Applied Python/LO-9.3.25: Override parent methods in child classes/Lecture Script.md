# Lecture Script: LO-67 Override Parent Methods


### CS Theory Bite

> **Origin**: Method overriding enables **polymorphism** — "many forms" of the same operation. Python uses **dynamic dispatch** to find the correct method at runtime via the **Method Resolution Order (MRO)**.
>
> **Analogy**: Overriding is like **regional dialects** — everyone "speaks" (same method name), but each region has its own version.
>
> **Why it matters**: Polymorphism lets you write generic code (`for shape in shapes: shape.area()`) that works with any subclass.


## [0:00-0:02] Hook (2 min)
**Say**: "Imagine a phone. All phones can 'make_call()', but a smartphone does it differently than an old landline. It uses the internet, shows the contact's photo, maybe even video calls! That's method overriding — taking a parent's method and customizing it for the child class."

**Demo**:
```python
class Phone:
    def make_call(self):
        print("Dialing...")

class Smartphone(Phone):
    def make_call(self):
        print("Opening contacts with photos...")
        print("Video call initiated!")

smart = Smartphone()
smart.make_call()  # Uses the NEW version!
```

**Say**: "The child class REPLACES the parent's method with its own version. Let's master this!"

## [0:02-0:06] Basic Method Overriding (4 min)

**Say**: "Method overriding means defining a method in the child class with the SAME NAME as one in the parent."

**Live Code**:
```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):  # Override!
        return "Woof!"

class Cat(Animal):
    def speak(self):  # Override!
        return "Meow!"

# Test it
animal = Animal()
dog = Dog()
cat = Cat()

print(animal.speak())  # Some generic sound
print(dog.speak())     # Woof!
print(cat.speak())     # Meow!
```

**Point out**: "Same method name 'speak()', but each class provides its own implementation!"

**Emphasize**: "Python uses the MOST SPECIFIC version. Dog has speak(), so it uses that instead of Animal's speak()."

## [0:06-0:10] Why Override Methods? (4 min)

**Say**: "Why not just create a new method with a different name? Watch this:"

**Live Code**:
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

    def area(self):  # Override!
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):  # Override!
        return 3.14159 * self.radius ** 2

# The power of polymorphism!
shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    shape.display_info()
# Rectangle - Area: 50
# Circle - Area: 153.93791
```

**Say**: "Notice display_info() is NOT overridden! It calls area(), which IS overridden. This is polymorphism — same interface, different behavior!"

## [0:10-0:14] Real-World Example: Payment System (4 min)

**Say**: "Let's build a payment processing system with different payment methods."

**Live Code**:
```python
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        return f"Processing ${self.amount}"

    def receipt(self):
        print(self.process())
        print("Transaction complete")

class CreditCard(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process(self):  # Override!
        return f"Charging ${self.amount} to card ending in {self.card_number[-4:]}"

class PayPal(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process(self):  # Override!
        return f"Sending ${self.amount} via PayPal to {self.email}"

class Bitcoin(Payment):
    def __init__(self, amount, wallet):
        super().__init__(amount)
        self.wallet = wallet

    def process(self):  # Override!
        return f"Transferring ${self.amount} worth of BTC to {self.wallet[:8]}..."

# Use them all!
card = CreditCard(100, "1234567890123456")
card.receipt()
# Charging $100 to card ending in 3456
# Transaction complete

paypal = PayPal(50, "user@email.com")
paypal.receipt()
# Sending $50 via PayPal to user@email.com
# Transaction complete

btc = Bitcoin(200, "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
btc.receipt()
# Transferring $200 worth of BTC to 1A1zP1eP...
# Transaction complete
```

**Point out**: "All three use receipt() from Payment, but each has its own process() method. Clean and organized!"

## [0:14-0:18] Overriding vs Extending (4 min)

**Say**: "Sometimes you want to REPLACE a method completely. Other times, you want to ADD to it. Let's see both."

**Live Code**:
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.is_running = False

    def start(self):
        self.is_running = True
        return "Vehicle started"

# Complete override - REPLACE
class Motorcycle(Vehicle):
    def start(self):  # Completely new implementation
        self.is_running = True
        return "Motorcycle started with a roar!"

# Extending - ADD to parent
class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors
        self.lights_on = False

    def start(self):
        result = super().start()  # Call parent version!
        self.lights_on = True      # Add new behavior
        return f"{result} and lights turned on"

# Test
motorcycle = Motorcycle("Harley")
print(motorcycle.start())  # Motorcycle started with a roar!

car = Car("Toyota", 4)
print(car.start())  # Vehicle started and lights turned on
print(f"Lights on: {car.lights_on}")  # True
```

**Emphasize**: "Use super().method_name() to call the parent version, then add your own logic. This is extending, not replacing!"

## [0:18-0:21] Real-World Example: Bank Accounts (3 min)

**Say**: "Let's see a practical example with different account types."

**Live Code**:
```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.minimum_balance = 500

    def withdraw(self, amount):  # Override with restriction!
        if self.balance - amount < self.minimum_balance:
            print(f"Cannot withdraw: Must maintain ${self.minimum_balance} minimum")
            return False
        return super().withdraw(amount)  # Use parent's logic

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft

    def withdraw(self, amount):  # Override with overdraft!
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            if self.balance < 0:
                print(f"Overdraft: ${abs(self.balance)}")
            return True
        print("Exceeds overdraft limit!")
        return False

# Test
savings = SavingsAccount("SA001", 1000)
savings.withdraw(600)  # Cannot withdraw: Must maintain $500 minimum
savings.withdraw(400)  # Works!
print(f"Savings balance: ${savings.balance}")  # 600

checking = CheckingAccount("CA001", 100, 200)
checking.withdraw(250)  # Overdraft: $150
print(f"Checking balance: ${checking.balance}")  # -150
```

**Say**: "Each account type has its own rules, implemented by overriding withdraw()!"

## [0:21-0:23] Practice Challenge (2 min)

**Challenge**: "Create an Employee class with calculate_salary(). Create FullTime and Hourly child classes that override it."

**Skeleton**:
```python
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        return 0

class FullTime(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        # TODO: return monthly salary
        pass

class Hourly(Employee):
    def __init__(self, name, rate, hours):
        super().__init__(name)
        self.rate = rate
        self.hours = hours

    def calculate_salary(self):
        # TODO: return rate * hours
        pass

# Test
alice = FullTime("Alice", 5000)
bob = Hourly("Bob", 25, 40)
print(f"{alice.name}: ${alice.calculate_salary()}")  # Should be 5000
print(f"{bob.name}: ${bob.calculate_salary()}")      # Should be 1000
```

**Solution** (show after 1-2 minutes):
```python
def calculate_salary(self):  # FullTime
    return self.monthly_salary

def calculate_salary(self):  # Hourly
    return self.rate * self.hours
```

## [0:23-0:25] Wrap-up (2 min)

**Key Points**:
1. **Method overriding**: Child redefines parent's method with same name
2. **Same signature**: Keep the same parameters as parent method
3. **Replace OR extend**: Completely new OR add to parent with super()
4. **Polymorphism**: Different behavior, same interface
5. **Use super()**: To call parent's version and extend it

**Common Mistakes**:
- Changing the method signature (number of parameters)
- Forgetting super() when you want to extend, not replace
- Not calling super().__init__() in child constructors
- Misspelling the method name (creates new method instead of overriding)

**When to Override**:
- Different subclasses need different implementations
- Customizing inherited behavior for specific types
- Implementing polymorphism in your design

**Closing**: "Method overriding is essential for polymorphism! It lets you create flexible, maintainable class hierarchies where different objects can be used interchangeably. Next, we'll dive deeper into super() to understand how to properly call parent methods."
