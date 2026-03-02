# Apply Encapsulation

## Apply Encapsulation

Hiding internal details and controlling access

---

<div align="center">

![Python Encapsulation Data Hiding Private Attributes](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/.jpg)

*Encapsulation protects internal data within Python's type system, controlling access through defined interfaces*

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
# x Laptop = $999.99
# x Mouse = $89.97
# x Keyboard = $79.99
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
