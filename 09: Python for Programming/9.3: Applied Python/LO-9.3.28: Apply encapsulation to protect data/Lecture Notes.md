# Lecture Notes: Apply Encapsulation

## Apply Encapsulation

Hiding internal details and controlling access


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---

## Introduction

Encapsulation implements **data hiding and access control** - protecting object internals from external interference! This is **information hiding** - expose only what's necessary, hide implementation details. Encapsulation creates **controlled interfaces** - the foundation of **API design**!

### Why Encapsulation is Fundamental

**Problem without encapsulation**: Anyone can break your objects:
```python
# DANGER - direct access, no validation!
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # Public!

account = BankAccount(1000)
account.balance = -5000  # Invalid! But allowed!
account.balance = "hacked"  # Type error! But allowed!
# Objects broken by external code!
```

**Solution with encapsulation**: Control access, validate changes:
```python
# SAFE - controlled access!
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private!

    def deposit(self, amount):
        if amount > 0:  # Validation!
            self.__balance += amount
        else:
            print("Invalid amount")
# Object protects itself!
```

**This is defensive programming** - objects guard their integrity!

### Historical Context

**Encapsulation** from **Simula 67** (1967) - first language with private/protected. **Smalltalk** (1972) formalized **message passing** - objects communicate only through methods, never direct data access!

**Python's approach**: **No true private** - uses **name mangling** (double underscore) as "strong suggestion". **Guido's philosophy**: "We're all consenting adults here" - trust programmers, but provide conventions. **C++/Java** enforce private with compiler - Python uses cultural convention!

**Property decorators** (Python 2.2, 2001) enable **computed attributes** - look like attributes, act like methods. This **syntactic elegance** makes getters/setters Pythonic - `obj.balance` instead of `obj.get_balance()`!

### Real-World Analogies

**Encapsulation like ATM machine**:
- **Hidden internals**: Cash storage, card reader mechanism (private)
- **Public interface**: Buttons, screen, card slot (public methods)
- **Validation**: Check PIN, sufficient funds (setters validate)
- **Can't reach inside**: Must use buttons, not grab cash directly!
**Controlled access protects the system!**

**Or like smartphone**:
```python
class Smartphone:
    def __init__(self):
        self.__battery_voltage = 3.7  # Internal detail
        self.__cpu_temperature = 40   # Hidden from user

    def get_battery_percent(self):
        # Convert voltage to percentage (abstraction!)
        return int((self.__battery_voltage / 4.2) * 100)

    def charge(self):
        if self.__battery_voltage < 4.2:
            self.__battery_voltage += 0.1  # Safe charging!
# User sees battery %, not raw voltage!
```

**Or like building security**:
- **Public**: Lobby, reception (public methods)
- **Private**: Server room, executive offices (private attributes)
- **Access control**: Keycards, permissions (getters/setters)
**Not everyone gets access to everything!**

### Access Levels in Python

**Public** (`attribute`): No restrictions:
```python
self.name = "Alice"  # Anyone can access/modify
```

**Protected** (`_attribute`): Convention only, "please don't access":
```python
self._internal_id = 123  # Hint: internal use
```

**Private** (`__attribute`): Name mangling, strong suggestion:
```python
self.__password_hash = "..."  # Becomes _ClassName__password_hash
```

**Python philosophy**: **Trust programmers** but provide **tools for encapsulation** - use them wisely!

---
### Understanding the Concept

Encapsulation is the practice of bundling data (attributes) and methods that operate on that data within a class, while restricting direct access to some of the object's components. This is a fundamental principle of object-oriented programming.

**Key concepts**: private attributes, getters, setters, name mangling, data hiding, access control

### Syntax and Usage

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (double underscore)

    def get_balance(self):  # Getter
        return self.__balance

    def deposit(self, amount):  # Setter-like method
        if amount > 0:
            self.__balance += amount
```

### Access Levels in Python

```python
class Example:
    def __init__(self):
        self.public = "I'm public"           # Public
        self._protected = "I'm protected"    # Protected (by convention)
        self.__private = "I'm private"       # Private (name mangling)

obj = Example()
print(obj.public)      # Works
print(obj._protected)  # Works (but shouldn't be used outside)
# print(obj.__private) # AttributeError
print(obj._Example__private)  # Works (name mangling)
```

### Practical Examples

#### Example 1: Bank Account with Encapsulation

```python
class BankAccount:
    def __init__(self, account_number, owner, initial_balance):
        self.__account_number = account_number  # Private
        self.__owner = owner                    # Private
        self.__balance = initial_balance        # Private
        self.__transaction_history = []         # Private

    # Getter methods
    def get_account_number(self):
        return self.__account_number

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def get_transaction_history(self):
        return self.__transaction_history.copy()  # Return copy, not original

    # Controlled modification methods
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return False

        self.__balance += amount
        self.__transaction_history.append(f"Deposit: +${amount}")
        print(f"Deposited ${amount}. New balance: ${self.__balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False

        if amount > self.__balance:
            print("Insufficient funds")
            return False

        self.__balance -= amount
        self.__transaction_history.append(f"Withdrawal: -${amount}")
        print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        return True

    def transfer(self, amount, recipient_account):
        if self.withdraw(amount):
            recipient_account.deposit(amount)
            self.__transaction_history.append(f"Transfer: -${amount} to {recipient_account.get_owner()}")
            return True
        return False

    def display_info(self):
        print(f"\nAccount: {self.__account_number}")
        print(f"Owner: {self.__owner}")
        print(f"Balance: ${self.__balance}")
        print(f"Transactions: {len(self.__transaction_history)}")

# Usage
account1 = BankAccount("ACC001", "Alice", 1000)
account2 = BankAccount("ACC002", "Bob", 500)

account1.deposit(500)
# Deposited $500. New balance: $1500

account1.withdraw(200)
# Withdrew $200. New balance: $1300

account1.transfer(300, account2)
# Withdrew $300. New balance: $1000
# Deposited $300. New balance: $800

account1.display_info()
# Account: ACC001
# Owner: Alice
# Balance: $1000
# Transactions: 4

# Cannot directly access private attributes
# print(account1.__balance)  # AttributeError
print(account1.get_balance())  # 1000 - Controlled access
```

#### Example 2: User Authentication System

```python
import hashlib

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password_hash = self.__hash_password(password)
        self.__is_logged_in = False
        self.__failed_attempts = 0
        self.__max_attempts = 3

    def __hash_password(self, password):
        """Private method to hash passwords"""
        return hashlib.sha256(password.encode()).hexdigest()

    def get_username(self):
        return self.__username

    def is_logged_in(self):
        return self.__is_logged_in

    def login(self, password):
        if self.__failed_attempts >= self.__max_attempts:
            print(f"Account locked due to too many failed attempts")
            return False

        if self.__hash_password(password) == self.__password_hash:
            self.__is_logged_in = True
            self.__failed_attempts = 0
            print(f"{self.__username} logged in successfully")
            return True
        else:
            self.__failed_attempts += 1
            remaining = self.__max_attempts - self.__failed_attempts
            print(f"Incorrect password. {remaining} attempts remaining")
            return False

    def logout(self):
        self.__is_logged_in = False
        print(f"{self.__username} logged out")

    def change_password(self, old_password, new_password):
        if not self.__is_logged_in:
            print("Must be logged in to change password")
            return False

        if self.__hash_password(old_password) != self.__password_hash:
            print("Incorrect old password")
            return False

        if len(new_password) < 8:
            print("New password must be at least 8 characters")
            return False

        self.__password_hash = self.__hash_password(new_password)
        print("Password changed successfully")
        return True

# Usage
user = User("alice", "mypassword123")

user.login("wrongpassword")
# Incorrect password. 2 attempts remaining

user.login("mypassword123")
# alice logged in successfully

user.change_password("mypassword123", "newpass456")
# Password changed successfully

user.logout()
# alice logged out

# Cannot access private data directly
# print(user.__password_hash)  # AttributeError
```

#### Example 3: Temperature Sensor with Validation

```python
class TemperatureSensor:
    def __init__(self, sensor_id, location):
        self.__sensor_id = sensor_id
        self.__location = location
        self.__temperature = 0.0
        self.__min_temp = -50.0
        self.__max_temp = 150.0
        self.__readings = []
        self.__is_active = True

    def get_sensor_id(self):
        return self.__sensor_id

    def get_location(self):
        return self.__location

    def get_temperature(self):
        return self.__temperature

    def is_active(self):
        return self.__is_active

    def __validate_temperature(self, temp):
        """Private validation method"""
        if not isinstance(temp, (int, float)):
            return False
        if temp < self.__min_temp or temp > self.__max_temp:
            return False
        return True

    def __record_reading(self, temp):
        """Private method to record readings"""
        self.__readings.append(temp)
        if len(self.__readings) > 100:
            self.__readings.pop(0)  # Keep only last 100 readings

    def set_temperature(self, temp):
        if not self.__is_active:
            print("Sensor is inactive")
            return False

        if not self.__validate_temperature(temp):
            print(f"Invalid temperature: {temp}")
            self.__is_active = False
            print("Sensor deactivated due to invalid reading")
            return False

        self.__temperature = temp
        self.__record_reading(temp)
        return True

    def get_average_temperature(self):
        if not self.__readings:
            return 0.0
        return sum(self.__readings) / len(self.__readings)

    def get_min_recorded(self):
        if not self.__readings:
            return None
        return min(self.__readings)

    def get_max_recorded(self):
        if not self.__readings:
            return None
        return max(self.__readings)

    def reset_sensor(self):
        self.__temperature = 0.0
        self.__readings = []
        self.__is_active = True
        print(f"Sensor {self.__sensor_id} reset")

    def display_status(self):
        print(f"\nSensor ID: {self.__sensor_id}")
        print(f"Location: {self.__location}")
        print(f"Current Temperature: {self.__temperature}°C")
        print(f"Status: {'Active' if self.__is_active else 'Inactive'}")
        print(f"Readings Count: {len(self.__readings)}")
        if self.__readings:
            print(f"Average: {self.get_average_temperature():.2f}°C")
            print(f"Min: {self.get_min_recorded()}°C")
            print(f"Max: {self.get_max_recorded()}°C")

# Usage
sensor = TemperatureSensor("TEMP-001", "Server Room")

sensor.set_temperature(22.5)
sensor.set_temperature(23.1)
sensor.set_temperature(21.8)
sensor.set_temperature(24.2)

sensor.display_status()
# Sensor ID: TEMP-001
# Location: Server Room
# Current Temperature: 24.2°C
# Status: Active
# Readings Count: 4
# Average: 22.90°C
# Min: 21.8°C
# Max: 24.2°C

sensor.set_temperature(200)  # Invalid
# Invalid temperature: 200
# Sensor deactivated due to invalid reading

sensor.display_status()
# Status: Inactive

sensor.reset_sensor()
# Sensor TEMP-001 reset
```

#### Example 4: Student Grade System with Properties

```python
class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name
        self.__grades = {}
        self.__attendance_rate = 100.0

    # Using @property decorator (Pythonic way)
    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not new_name or not isinstance(new_name, str):
            raise ValueError("Name must be a non-empty string")
        self.__name = new_name

    @property
    def attendance_rate(self):
        return self.__attendance_rate

    @attendance_rate.setter
    def attendance_rate(self, rate):
        if 0 <= rate <= 100:
            self.__attendance_rate = rate
        else:
            raise ValueError("Attendance rate must be between 0 and 100")

    def add_grade(self, subject, score):
        if not isinstance(score, (int, float)):
            print("Score must be a number")
            return False

        if not 0 <= score <= 100:
            print("Score must be between 0 and 100")
            return False

        self.__grades[subject] = score
        print(f"Added {subject}: {score}")
        return True

    def get_grade(self, subject):
        return self.__grades.get(subject, None)

    def get_all_grades(self):
        return self.__grades.copy()

    def __calculate_letter_grade(self, score):
        """Private method to convert score to letter grade"""
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        return "F"

    def get_gpa(self):
        if not self.__grades:
            return 0.0

        grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
        total = sum(grade_points[self.__calculate_letter_grade(score)]
                   for score in self.__grades.values())
        return total / len(self.__grades)

    def get_transcript(self):
        print(f"\nTranscript for {self.__name} (ID: {self.__student_id})")
        print(f"Attendance Rate: {self.__attendance_rate}%")
        print("\nGrades:")

        if not self.__grades:
            print("  No grades recorded")
        else:
            for subject, score in self.__grades.items():
                letter = self.__calculate_letter_grade(score)
                print(f"  {subject}: {score} ({letter})")

        print(f"\nGPA: {self.get_gpa():.2f}")

    def is_eligible_for_honors(self):
        """Private criteria for honors"""
        return self.get_gpa() >= 3.5 and self.__attendance_rate >= 95

# Usage
student = Student("S12345", "Alice Johnson")

# Using property
print(student.name)  # Alice Johnson
student.name = "Alice Smith"  # Using setter
print(student.name)  # Alice Smith

student.add_grade("Math", 95)
# Added Math: 95

student.add_grade("Science", 88)
# Added Science: 88

student.add_grade("English", 92)
# Added English: 92

student.attendance_rate = 98  # Using property setter

student.get_transcript()
# Transcript for Alice Smith (ID: S12345)
# Attendance Rate: 98%
#
# Grades:
#   Math: 95 (A)
#   Science: 88 (B)
#   English: 92 (A)
#
# GPA: 3.67

if student.is_eligible_for_honors():
    print(f"{student.name} is eligible for honors!")
# Alice Smith is eligible for honors!
```

#### Example 5: Shopping Cart with Price Protection

```python
class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = self.__validate_price(price)

    def __validate_price(self, price):
        """Private validation method"""
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        if price < 0:
            raise ValueError("Price cannot be negative")
        return round(price, 2)

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = self.__validate_price(new_price)

    def __str__(self):
        return f"{self.__name} (${self.__price})"

class CartItem:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = self.__validate_quantity(quantity)

    def __validate_quantity(self, quantity):
        """Private validation"""
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        return quantity

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = self.__validate_quantity(new_quantity)

    def get_subtotal(self):
        return self.__product.price * self.__quantity

    def __str__(self):
        return f"{self.__quantity}x {self.__product.name} = ${self.get_subtotal():.2f}"

class ShoppingCart:
    def __init__(self):
        self.__items = []
        self.__discount_rate = 0.0

    def __find_item(self, product_id):
        """Private helper method"""
        for item in self.__items:
            if item.product.product_id == product_id:
                return item
        return None

    def add_item(self, product, quantity=1):
        existing_item = self.__find_item(product.product_id)

        if existing_item:
            existing_item.quantity += quantity
            print(f"Updated {product.name} quantity to {existing_item.quantity}")
        else:
            cart_item = CartItem(product, quantity)
            self.__items.append(cart_item)
            print(f"Added {cart_item}")

    def remove_item(self, product_id):
        item = self.__find_item(product_id)
        if item:
            self.__items.remove(item)
            print(f"Removed {item.product.name}")
            return True
        print("Product not found in cart")
        return False

    def update_quantity(self, product_id, new_quantity):
        item = self.__find_item(product_id)
        if item:
            try:
                item.quantity = new_quantity
                print(f"Updated {item.product.name} quantity to {new_quantity}")
                return True
            except ValueError as e:
                print(f"Error: {e}")
                return False
        print("Product not found in cart")
        return False

    def apply_discount(self, discount_rate):
        if 0 <= discount_rate <= 100:
            self.__discount_rate = discount_rate
            print(f"Applied {discount_rate}% discount")
            return True
        print("Discount must be between 0 and 100")
        return False

    def get_subtotal(self):
        return sum(item.get_subtotal() for item in self.__items)

    def get_discount_amount(self):
        return self.get_subtotal() * (self.__discount_rate / 100)

    def get_total(self):
        return self.get_subtotal() - self.get_discount_amount()

    def get_item_count(self):
        return sum(item.quantity for item in self.__items)

    def clear_cart(self):
        self.__items = []
        self.__discount_rate = 0.0
        print("Cart cleared")

    def display_cart(self):
        print("\n" + "="*50)
        print("SHOPPING CART")
        print("="*50)

        if not self.__items:
            print("Cart is empty")
        else:
            for item in self.__items:
                print(f"  {item}")

            print("-"*50)
            print(f"Subtotal:        ${self.get_subtotal():>10.2f}")

            if self.__discount_rate > 0:
                print(f"Discount ({self.__discount_rate}%): -${self.get_discount_amount():>10.2f}")

            print("="*50)
            print(f"TOTAL:           ${self.get_total():>10.2f}")
            print(f"Items:           {self.get_item_count():>10}")
        print("="*50 + "\n")

# Usage
laptop = Product("P001", "Laptop", 999.99)
mouse = Product("P002", "Mouse", 29.99)
keyboard = Product("P003", "Keyboard", 79.99)

cart = ShoppingCart()

cart.add_item(laptop, 1)
# Added 1x Laptop = $999.99

cart.add_item(mouse, 2)
# Added 2x Mouse = $59.98

cart.add_item(keyboard, 1)
# Added 1x Keyboard = $79.99

cart.add_item(mouse, 1)  # Adding more mice
# Updated Mouse quantity to 3

cart.apply_discount(10)
# Applied 10% discount

cart.display_cart()
# ==================================================
# SHOPPING CART
# ==================================================
#   1x Laptop = $999.99
#   3x Mouse = $89.97
#   1x Keyboard = $79.99
# --------------------------------------------------
# Subtotal:        $   1169.95
# Discount (10%): -$    116.99
# ==================================================
# TOTAL:           $   1052.96
# Items:                    5
# ==================================================

# Cannot access private attributes directly
# print(cart.__items)  # AttributeError
print(f"Item count: {cart.get_item_count()}")  # Controlled access
```

### Best Practices

1. **Use private attributes for internal data**: Prefix with double underscore (`__`)
2. **Provide getters and setters**: Control how data is accessed and modified
3. **Validate in setters**: Ensure data integrity
4. **Use @property decorator**: More Pythonic than get/set methods
5. **Keep validation private**: Make validation methods private
6. **Return copies of mutable data**: Don't expose internal collections directly

### Common Mistakes

1. **Over-encapsulation**: Not everything needs to be private
2. **No validation**: If you use setters, validate the input
3. **Exposing mutable data**: Return copies, not references to internal data
4. **Inconsistent access**: Either use properties or getters/setters, not both

### When to Use

Use encapsulation when:
- Protecting sensitive data (passwords, account numbers)
- Enforcing validation rules
- Maintaining data integrity
- Hiding implementation details
- Creating public interfaces for classes

### Key Takeaways

1. Encapsulation hides internal implementation details
2. Private attributes use double underscore prefix (`__attribute`)
3. Use getter methods to provide read access
4. Use setter methods to control write access with validation
5. `@property` decorator provides Pythonic access control
6. Encapsulation promotes data integrity and security
7. Balance between access control and usability
