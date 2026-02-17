# Lecture Script: LO-70 Apply Encapsulation


### CS Theory Bite

> **Origin**: Encapsulation from **Simula 67** — hiding internal details behind public interfaces. Python uses **name mangling** (`__attr` → `_Class__attr`) as a "strong suggestion" rather than strict enforcement.
>
> **Analogy**: Encapsulation is like an **ATM** — you interact through buttons (public methods), never touching the cash mechanism directly (private attributes).
>
> **Why it matters**: Encapsulation protects data integrity — validation in setters prevents invalid state.


## [0:00-0:02] Hook (2 min)
**Say**: "Imagine your bank account. Can strangers directly access your balance and change it? No! The bank protects your data and only lets you access it through approved methods like deposit() and withdraw(). That's encapsulation — hiding data and controlling access to it!"

**Demo**:
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private! Can't access directly

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

account = BankAccount(1000)
# print(account.__balance)  # ERROR! Can't access directly
print(account.get_balance())  # 1000 - Controlled access!
```

**Say**: "The double underscore makes __balance private. Let's master data protection!"

## [0:02-0:06] Public vs Private Attributes (4 min)

**Say**: "Python has three levels of access: public, protected, and private."

**Live Code**:
```python
class Example:
    def __init__(self):
        self.public = "Everyone can see me"
        self._protected = "Convention: internal use"
        self.__private = "Truly hidden!"

obj = Example()

# Public - no restrictions
print(obj.public)  # Works fine

# Protected - convention only (still accessible)
print(obj._protected)  # Works, but shouldn't use outside class

# Private - name mangling makes it hard to access
# print(obj.__private)  # AttributeError!

# Can still access with name mangling (not recommended!)
print(obj._Example__private)  # Works but ugly!
```

**Point out**: "Single underscore _ is a CONVENTION saying 'please don't use this outside the class'. Double underscore __ is ENFORCED privacy through name mangling."

**Emphasize**: "Use double underscore __ for truly sensitive data that should never be accessed directly!"

## [0:06-0:10] Getters and Setters (4 min)

**Say**: "Private attributes need controlled access through getter and setter methods."

**Live Code**:
```python
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_grades(self):
        return self.__grades.copy()  # Return copy, not original!

    # Setter with validation
    def set_age(self, age):
        if 0 <= age <= 120:
            self.__age = age
            print(f"Age updated to {age}")
        else:
            print("Invalid age!")

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"Grade {grade} added")
        else:
            print("Invalid grade!")

# Test
student = Student("Alice", 20)
print(student.get_name())  # Alice

student.set_age(21)  # Age updated to 21
student.set_age(200)  # Invalid age!

student.add_grade(85)  # Grade 85 added
student.add_grade(150)  # Invalid grade!

print(student.get_grades())  # [85]
```

**Say**: "Getters read data. Setters modify data WITH VALIDATION. This prevents invalid states!"

**Point out**: "Notice get_grades() returns a COPY, not the original list. This prevents external code from modifying internal data!"

## [0:10-0:14] Using @property Decorator (4 min)

**Say**: "Python has a more elegant way: the @property decorator. It makes getters and setters look like attributes!"

**Live Code**:
```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        """Getter"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Setter with validation"""
        if value > 0:
            self.__radius = value
        else:
            raise ValueError("Radius must be positive!")

    @property
    def area(self):
        """Computed property"""
        return 3.14159 * self.__radius ** 2

    @property
    def circumference(self):
        """Computed property"""
        return 2 * 3.14159 * self.__radius

# Test - looks like attributes!
circle = Circle(5)
print(f"Radius: {circle.radius}")  # Uses getter
print(f"Area: {circle.area:.2f}")  # Computed

circle.radius = 10  # Uses setter
print(f"New radius: {circle.radius}")
print(f"New area: {circle.area:.2f}")

# circle.radius = -5  # ValueError! Validation works
```

**Emphasize**: "With @property, you use circle.radius instead of circle.get_radius(). Much cleaner!"

**Say**: "Notice area and circumference are READ-ONLY properties — computed on the fly, no setters!"

## [0:14-0:18] Real-World Example: Bank Account (4 min)

**Say**: "Let's build a secure bank account with proper encapsulation."

**Live Code**:
```python
class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.__account_number = account_number  # Private
        self.__owner = owner                    # Private
        self.__balance = balance                # Private
        self.__transaction_history = []         # Private

    # Read-only properties
    @property
    def account_number(self):
        return self.__account_number

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    # Controlled modification methods
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive!")
            return False

        self.__balance += amount
        self.__transaction_history.append(f"Deposit: +${amount}")
        print(f"Deposited ${amount}. Balance: ${self.__balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive!")
            return False

        if amount > self.__balance:
            print("Insufficient funds!")
            return False

        self.__balance -= amount
        self.__transaction_history.append(f"Withdrawal: -${amount}")
        print(f"Withdrew ${amount}. Balance: ${self.__balance}")
        return True

    def get_transaction_history(self):
        return self.__transaction_history.copy()  # Return copy!

    def display_info(self):
        print(f"\nAccount: {self.__account_number}")
        print(f"Owner: {self.__owner}")
        print(f"Balance: ${self.__balance}")
        print(f"Transactions: {len(self.__transaction_history)}")

# Test
account = BankAccount("ACC001", "Alice", 1000)

# Can read balance through property
print(f"Current balance: ${account.balance}")  # 1000

# Can't modify balance directly
# account.balance = 999999  # AttributeError!

# Must use controlled methods
account.deposit(500)   # Deposited $500. Balance: $1500
account.withdraw(200)  # Withdrew $200. Balance: $1300
account.withdraw(2000) # Insufficient funds!

account.display_info()
# Account: ACC001
# Owner: Alice
# Balance: $1300
# Transactions: 2
```

**Say**: "Notice: balance is READ-ONLY. You can't set it directly. You MUST use deposit() or withdraw() which validate the operation!"

## [0:18-0:21] Real-World Example: Password System (3 min)

**Say**: "Let's see encapsulation protecting sensitive data like passwords."

**Live Code**:
```python
import hashlib

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password_hash = self.__hash_password(password)
        self.__failed_attempts = 0
        self.__max_attempts = 3

    def __hash_password(self, password):
        """Private method - can't be called outside class"""
        return hashlib.sha256(password.encode()).hexdigest()

    @property
    def username(self):
        return self.__username

    def login(self, password):
        if self.__failed_attempts >= self.__max_attempts:
            print("Account locked!")
            return False

        if self.__hash_password(password) == self.__password_hash:
            self.__failed_attempts = 0
            print(f"{self.__username} logged in successfully")
            return True
        else:
            self.__failed_attempts += 1
            remaining = self.__max_attempts - self.__failed_attempts
            print(f"Wrong password! {remaining} attempts remaining")
            return False

    def change_password(self, old_password, new_password):
        if self.__hash_password(old_password) != self.__password_hash:
            print("Incorrect old password!")
            return False

        if len(new_password) < 8:
            print("Password must be at least 8 characters!")
            return False

        self.__password_hash = self.__hash_password(new_password)
        print("Password changed successfully")
        return True

# Test
user = User("alice", "mypassword123")

# Can't access password hash!
# print(user.__password_hash)  # AttributeError!

user.login("wrongpass")    # Wrong password! 2 attempts remaining
user.login("mypassword123") # alice logged in successfully

user.change_password("mypassword123", "newpass456")
# Password changed successfully
```

**Point out**: "The password is NEVER stored in plain text. Even __hash_password() is private!"

**Say**: "This is real security — the password hash can never be accessed directly!"

## [0:21-0:23] Practice Challenge (2 min)

**Challenge**: "Create a Temperature sensor that only accepts valid temperatures (-50 to 150) and tracks min/max."

**Skeleton**:
```python
class TemperatureSensor:
    def __init__(self, sensor_id):
        self.__sensor_id = sensor_id
        self.__temperature = 0
        self.__min_temp = 0
        self.__max_temp = 0

    @property
    def sensor_id(self):
        return self.__sensor_id

    @property
    def temperature(self):
        # TODO: Return current temperature
        pass

    def set_temperature(self, temp):
        # TODO: Validate (-50 to 150), update temperature
        # TODO: Track min and max
        pass

    def get_min_max(self):
        # TODO: Return (min, max) tuple
        pass

# Test
sensor = TemperatureSensor("TEMP-001")
sensor.set_temperature(25)
sensor.set_temperature(30)
sensor.set_temperature(20)
print(f"Current: {sensor.temperature}")
print(f"Min/Max: {sensor.get_min_max()}")
```

**Solution** (show after 1-2 minutes):
```python
@property
def temperature(self):
    return self.__temperature

def set_temperature(self, temp):
    if -50 <= temp <= 150:
        self.__temperature = temp
        if temp < self.__min_temp or self.__min_temp == 0:
            self.__min_temp = temp
        if temp > self.__max_temp:
            self.__max_temp = temp
        return True
    print("Temperature out of range!")
    return False

def get_min_max(self):
    return (self.__min_temp, self.__max_temp)
```

## [0:23-0:25] Wrap-up (2 min)

**Key Points**:
1. **Private attributes**: Use double underscore __ prefix
2. **Protected attributes**: Use single underscore _ prefix (convention)
3. **Getters**: Methods to read private data
4. **Setters**: Methods to modify private data with validation
5. **@property**: Pythonic way to create getters and setters
6. **Validation**: Always validate input in setters!

**Common Mistakes**:
- Over-encapsulation — not everything needs to be private
- No validation in setters (defeats the purpose!)
- Returning mutable objects directly (return copies instead)
- Forgetting @property makes code cleaner than get/set methods

**When to Encapsulate**:
- Sensitive data (passwords, account numbers, personal info)
- Data that needs validation (age, price, temperature)
- Data that must maintain invariants (balance can't go negative)
- Internal implementation details that might change

**Benefits**:
- Data integrity — invalid states impossible
- Security — sensitive data protected
- Flexibility — change internal implementation without breaking code
- Controlled access — track who modifies what

**Closing**: "Encapsulation is one of the pillars of OOP! It's about building walls around your data with controlled gates. Master it, and you'll write secure, maintainable code. Remember: make everything as private as possible, and only expose what's necessary!"
