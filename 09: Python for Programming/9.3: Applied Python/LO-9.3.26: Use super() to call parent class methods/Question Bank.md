# Question Bank: Use the super() Function

## Problem 1 (Easy)
Create a base class `Person` with attributes `name` and `age`. Create a child class `Student` that adds attribute `student_id`. Use `super().__init__()` in the Student class to initialize the parent attributes. Test by creating a student.

## Problem 2 (Easy)
Create a base class `Rectangle` with attributes `length` and `width`, and a method `describe()` that prints the dimensions. Create a child class `ColoredRectangle` that adds a `color` attribute. Use `super()` to call the parent's `__init__()` and `describe()`, then add color information.

## Problem 3 (Medium)
Create a base class `BankAccount` with attributes `account_number` and `balance`, and a method `deposit(amount)`. Create a child class `InterestAccount` that adds an `interest_rate` attribute and overrides `deposit()` to:
- Call parent's `deposit()` using `super()`
- Calculate and add interest on the deposited amount
- Print the interest earned

Test with multiple deposits.

## Problem 4 (Medium)
Create a base class `Employee` with attributes `name` and `base_salary`, and a method `calculate_salary()` that returns base_salary. Create child classes:
- `Manager`: adds `bonus` attribute, uses `super()` to get base salary, then adds bonus
- `SalesRep`: adds `commission` attribute, uses `super()` to get base salary, then adds commission
- `Executive`: inherits from Manager, adds `stock_options`, uses `super()` to get manager's salary, then adds stock value

Test all three types showing how super() chains through multiple levels.

## Problem 5 (Hard)
Create a logging system with method chaining using super():
- Base class `Logger` with method `log(message)` that prints with timestamp
- `FileLogger` inherits from Logger, overrides `log()` to call `super().log()` first, then writes to file
- `EmailLogger` inherits from FileLogger, overrides `log()` to call `super().log()` first, then sends email
- `AlertLogger` inherits from EmailLogger, overrides `log()` for critical messages to call `super().log()` first, then triggers alert

Create an AlertLogger and demonstrate how a single log call cascades through all parent implementations using super(). Show the execution order.
