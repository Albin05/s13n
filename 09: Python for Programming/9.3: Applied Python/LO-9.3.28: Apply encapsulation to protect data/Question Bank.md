# Question Bank: Apply Encapsulation

## Problem 1 (Easy)
Create a class `BankAccount` with a private attribute `__balance` (using double underscore). Provide public methods `deposit(amount)`, `withdraw(amount)`, and `get_balance()` to access and modify the balance. The balance should not be directly accessible from outside the class. Test by trying to access `__balance` directly and through methods.

## Problem 2 (Easy)
Create a class `Temperature` with a private attribute `__celsius`. Provide getter and setter methods `get_celsius()` and `set_celsius(value)`. The setter should validate that temperature is not below absolute zero (-273.15°C). Test with valid and invalid temperatures.

## Problem 3 (Medium)
Create a class `User` with private attributes `__username` and `__password`. Implement:
- `get_username()`: returns the username
- `set_password(old_password, new_password)`: changes password only if old password matches
- `verify_password(password)`: returns True if password matches
- The password should never be directly accessible or displayed

Test the security by attempting various password operations.

## Problem 4 (Medium)
Create a class `Rectangle` with private attributes `__length` and `__width`. Implement:
- Property getters and setters using `@property` and `@attribute.setter` decorators
- Setters should validate that dimensions are positive
- Add a read-only property `area` (no setter) that calculates area
- Add a read-only property `perimeter` that calculates perimeter

Test by setting dimensions and accessing calculated properties.

## Problem 5 (Hard)
Create a banking system with proper encapsulation:
- `Account` class with private `__account_number`, `__balance`, `__transaction_history` (list)
- Public methods: `deposit(amount)`, `withdraw(amount)`, `get_balance()`, `get_statement()`
- Private method `__record_transaction(type, amount)` to log transactions
- `SavingsAccount` subclass with private `__interest_rate` and method `apply_interest()`
- Ensure no direct access to private attributes, all operations go through methods
- Transaction history should record type (deposit/withdraw/interest), amount, and timestamp

Create accounts, perform transactions, apply interest, and print statements showing proper encapsulation in action.
