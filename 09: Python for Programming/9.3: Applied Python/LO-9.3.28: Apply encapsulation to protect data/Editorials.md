# Editorials: Apply Encapsulation

## Problem 1
```python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. Balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.__balance}")
        else:
            print("Withdrawal amount must be positive")

    def get_balance(self):
        return self.__balance

# Test the class
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")

# Try to access private attribute directly
print("\nTrying to access __balance directly:")
try:
    print(account.__balance)
except AttributeError as e:
    print(f"Error: {e}")

# Python name mangling makes it accessible as _BankAccount__balance
print("\nPython's name mangling (not recommended to use):")
print(f"Accessing via name mangling: ${account._BankAccount__balance}")
```

### Explanation
- Double underscore `__` makes an attribute private (name mangling)
- Private attributes cannot be accessed directly from outside the class
- We provide public methods (`deposit`, `withdraw`, `get_balance`) as the interface
- This prevents direct manipulation of the balance, ensuring validation rules are enforced
- Python's name mangling changes `__balance` to `_ClassName__balance` internally
- While technically accessible via name mangling, this is considered bad practice
- Encapsulation protects data integrity by controlling how attributes are accessed and modified

## Problem 2
```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = None
        self.set_celsius(celsius)

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, value):
        if value < -273.15:
            print(f"Error: Temperature cannot be below absolute zero (-273.15°C)")
            print(f"Temperature remains at {self.__celsius}°C")
        else:
            self.__celsius = value
            print(f"Temperature set to {self.__celsius}°C")

    def get_fahrenheit(self):
        return (self.__celsius * 9/5) + 32

# Test the class
print("Creating temperature at 25°C:")
temp = Temperature(25)

print(f"\nCurrent temperature: {temp.get_celsius()}°C")
print(f"In Fahrenheit: {temp.get_fahrenheit():.1f}°F")

print("\nSetting to 100°C:")
temp.set_celsius(100)

print("\nTrying to set below absolute zero (-300°C):")
temp.set_celsius(-300)

print(f"\nFinal temperature: {temp.get_celsius()}°C")
```

### Explanation
- The `__celsius` attribute is private and can only be modified through `set_celsius()`
- The setter validates input, preventing invalid temperatures
- If validation fails, the temperature remains unchanged
- The getter provides read access to the value
- Encapsulation ensures data integrity by enforcing business rules in setters
- Additional methods like `get_fahrenheit()` can use the private data
- The constructor uses the setter to ensure validation even during initialization

## Problem 3
```python
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            print("Password changed successfully")
            return True
        else:
            print("Incorrect old password")
            return False

    def verify_password(self, password):
        return self.__password == password

# Test the class
user = User("alice", "password123")

print(f"Username: {user.get_username()}")

# Try to access password directly
print("\nTrying to access password directly:")
try:
    print(user.__password)
except AttributeError as e:
    print("Cannot access password directly (good!)")

# Verify password
print("\nVerifying correct password:")
print(f"Is 'password123' correct? {user.verify_password('password123')}")

print("\nVerifying incorrect password:")
print(f"Is 'wrong' correct? {user.verify_password('wrong')}")

# Change password with wrong old password
print("\nTrying to change password with wrong old password:")
user.set_password("wrongpass", "newpassword")

# Change password with correct old password
print("\nChanging password with correct old password:")
user.set_password("password123", "newsecurepass456")

# Verify new password
print("\nVerifying new password:")
print(f"Is 'newsecurepass456' correct? {user.verify_password('newsecurepass456')}")
```

### Explanation
- The password is private and never exposed directly
- `verify_password()` compares internally without returning the actual password
- `set_password()` requires the old password, preventing unauthorized changes
- This is security through encapsulation: the password is protected
- Even if you have a User object, you cannot read the password
- This models real-world security where passwords should never be displayed
- The username is read-only (no setter provided)
- Encapsulation provides security by controlling access to sensitive data

## Problem 4
```python
class Rectangle:
    def __init__(self, length, width):
        self.__length = None
        self.__width = None
        # Use setters for validation
        self.length = length
        self.width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError("Length must be positive")
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self.__width = value

    @property
    def area(self):
        return self.__length * self.__width

    @property
    def perimeter(self):
        return 2 * (self.__length + self.__width)

# Test the class
print("Creating rectangle with length=5, width=3:")
rect = Rectangle(5, 3)

print(f"Length: {rect.length}")
print(f"Width: {rect.width}")
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")

print("\nChanging dimensions to length=10, width=4:")
rect.length = 10
rect.width = 4

print(f"New area: {rect.area}")
print(f"New perimeter: {rect.perimeter}")

print("\nTrying to set negative length:")
try:
    rect.length = -5
except ValueError as e:
    print(f"Error: {e}")

print("\nTrying to set area directly (read-only):")
try:
    rect.area = 100
except AttributeError as e:
    print(f"Error: can't set attribute (area is read-only)")

print(f"\nFinal dimensions: {rect.length} x {rect.width}")
print(f"Final area: {rect.area}")
```

### Explanation
- `@property` decorator creates a getter that looks like an attribute access
- `@attribute.setter` creates a setter with validation
- Properties allow attribute-like syntax (`rect.length`) while using method logic
- The actual attributes are private (`__length`, `__width`)
- Setters validate input, raising exceptions for invalid values
- Read-only properties (`area`, `perimeter`) have no setter
- This is computed property pattern: values calculated on demand
- Properties provide a clean interface while maintaining encapsulation
- You can change implementation without changing the interface

## Problem 5
```python
from datetime import datetime

class Account:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance
        self.__transaction_history = []
        self.__record_transaction("Opening", initial_balance)

    def __record_transaction(self, type, amount):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = {
            "timestamp": timestamp,
            "type": type,
            "amount": amount,
            "balance": self.__balance
        }
        self.__transaction_history.append(transaction)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return False
        self.__balance += amount
        self.__record_transaction("Deposit", amount)
        print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        if amount > self.__balance:
            print("Insufficient funds")
            return False
        self.__balance -= amount
        self.__record_transaction("Withdrawal", amount)
        print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True

    def get_balance(self):
        return self.__balance

    def get_statement(self):
        print(f"\n{'='*60}")
        print(f"Account Statement - Account #{self.__account_number}")
        print(f"{'='*60}")
        print(f"{'Timestamp':<20} {'Type':<12} {'Amount':>10} {'Balance':>10}")
        print(f"{'-'*60}")
        for txn in self.__transaction_history:
            print(f"{txn['timestamp']:<20} {txn['type']:<12} "
                  f"${txn['amount']:>9.2f} ${txn['balance']:>9.2f}")
        print(f"{'-'*60}")
        print(f"Current Balance: ${self.__balance:.2f}")
        print(f"{'='*60}\n")

class SavingsAccount(Account):
    def __init__(self, account_number, initial_balance, interest_rate):
        super().__init__(account_number, initial_balance)
        self.__interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * (self.__interest_rate / 100)
        # Use parent's deposit to add interest
        print(f"Applying {self.__interest_rate}% interest: ${interest:.2f}")
        self.deposit(interest)

    def get_interest_rate(self):
        return self.__interest_rate

# Test the banking system
print("Creating checking account with $1000:")
checking = Account("CHK001", 1000)

print("\nPerforming transactions on checking account:")
checking.deposit(500)
checking.withdraw(200)
checking.withdraw(50)

checking.get_statement()

print("\nCreating savings account with $5000 at 3% interest:")
savings = SavingsAccount("SAV001", 5000, 3)

print("\nPerforming transactions on savings account:")
savings.deposit(1000)
savings.withdraw(500)
savings.apply_interest()

savings.get_statement()

print("Demonstrating encapsulation:")
print(f"Checking balance (through getter): ${checking.get_balance():.2f}")
print("\nTrying to access private attributes directly:")
try:
    print(checking.__balance)
except AttributeError:
    print("Cannot access __balance directly (encapsulated!)")

try:
    print(checking.__transaction_history)
except AttributeError:
    print("Cannot access __transaction_history directly (encapsulated!)")

print("\nAll data access must go through public methods!")
```

### Explanation
- All critical data is private: `__balance`, `__account_number`, `__transaction_history`
- Private method `__record_transaction()` is internal implementation detail
- Public methods provide controlled access to functionality
- Transaction history is maintained internally but only accessible through `get_statement()`
- The balance can be queried but not set directly
- `SavingsAccount` inherits but still cannot directly access parent's private attributes
- It must use public methods (`get_balance()`, `deposit()`) to interact with parent data
- This demonstrates strong encapsulation: implementation is hidden, only interface is exposed
- Private methods can change without affecting external code
- Data integrity is maintained through validation in public methods

**Key Concepts**:
1. **Encapsulation** hides internal state and requires interaction through methods
2. **Private attributes** use double underscore `__attribute` (name mangling)
3. **Public interface** provides controlled access to private data
4. **Validation** in setters ensures data integrity
5. **Properties** (`@property`) provide attribute-like access with method logic
6. **Read-only properties** have getters but no setters
7. **Information hiding** keeps implementation details private
8. **Security** through encapsulation prevents unauthorized access or modification
