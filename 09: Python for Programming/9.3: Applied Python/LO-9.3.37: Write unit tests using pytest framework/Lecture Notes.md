# Lecture Notes: Write Unit Tests with pytest

## Unit Testing with pytest

pytest is a popular testing framework that makes it easy to write and run tests in Python. Tests verify that code works correctly and help catch bugs early.


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---

## Introduction

Unit testing implements **automated verification** - proving code works correctly with repeatable tests! This is **test-driven confidence** - change code fearlessly because tests catch regressions. Testing is **professional software engineering** - the safety net beneath every change!

### Why Unit Testing is Non-Negotiable

**Problem without tests**: Fear of change:
```python
# SCARY - does this refactor break anything?
def calculate_total(items):
    return sum(i.price * i.qty for i in items)  # Changed!
# Hope it works... deploy and pray!
```

**Solution with tests**: Confidence in changes:
```python
# CONFIDENT - tests verify correctness!
def test_calculate_total():
    items = [Item(10, 2), Item(5, 3)]
    assert calculate_total(items) == 35  # Verified!
# Refactor freely - tests catch mistakes!
```

**This is regression prevention** - tests guard against breaking changes!

### Historical Context

**Unit testing** formalized by **Kent Beck** (1999) with **JUnit** for Java. Inspired by **SUnit** (Smalltalk, 1994) - first unit testing framework! **Test-Driven Development (TDD)** (Beck, 2003): write tests FIRST, then code to pass them!

**pytest** created by **Holger Krekel** (2004) - simpler than Python's built-in `unittest` (which copied Java's JUnit). **pytest philosophy**: minimal boilerplate - just use `assert`! No classes needed, no `self.assertEqual()` verbosity!

**Testing pyramid** (Mike Cohn, 2009): Many unit tests (fast, cheap), fewer integration tests, fewest end-to-end tests. **Unit tests** are the foundation - test individual functions in isolation!

### Real-World Analogies

**Unit tests like quality control**:
- **Factory**: Each component tested before assembly
- **Unit test**: Each function tested before deployment
- **Regression**: Re-test after changes (didn't break anything?)
**Quality control prevents defective products!**

**Or like spell-checking**:
```python
# Like spell-check for code logic:
# - Write document (code)
# - Run spell-check (tests)
# - Fix errors before publishing (deploy)
# Automated checking catches human mistakes!
```

**Or like medical checkups**:
- **Regular checkup**: Run tests periodically (CI/CD)
- **Specific test**: Check one organ/function (unit test)
- **Test results**: Pass/fail with details (test report)
**Early detection prevents catastrophic failures!**

### Test-Driven Development (TDD) Cycle

**Red-Green-Refactor**:
1. **Red**: Write failing test (test doesn't pass yet)
2. **Green**: Write minimum code to pass test
3. **Refactor**: Clean up code, tests still pass

**This is disciplined development** - tests guide design!

---
### Installation

```bash
pip install pytest
```

### Basic Test Structure

```python
# math_operations.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# test_math_operations.py
from math_operations import add, multiply

def test_add():
    """Test the add function"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    """Test the multiply function"""
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
    assert multiply(-2, 5) == -10
```

### Running Tests

```bash
# Run all tests in current directory
pytest

# Run specific test file
pytest test_math_operations.py

# Run with verbose output
pytest -v

# Run specific test function
pytest test_math_operations.py::test_add
```

## Assertions

```python
def test_various_assertions():
    # Equality
    assert 5 == 5
    assert "hello" == "hello"

    # Inequality
    assert 10 != 5

    # Comparisons
    assert 10 > 5
    assert 3 <= 3
    assert 7 >= 7

    # Boolean
    assert True
    assert not False

    # Membership
    assert 3 in [1, 2, 3, 4]
    assert "world" in "hello world"
    assert 10 not in [1, 2, 3]

    # Type checking
    assert isinstance(5, int)
    assert isinstance("hello", str)
    assert isinstance([1, 2], list)
```

## Real-World Examples

### Example 1: Testing String Functions

```python
# string_utils.py
def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

def is_palindrome(s):
    """Check if string is a palindrome"""
    clean = s.lower().replace(" ", "")
    return clean == clean[::-1]

def count_vowels(s):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# test_string_utils.py
from string_utils import reverse_string, is_palindrome, count_vowels

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("") == True

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("Python") == 1
    assert count_vowels("aeiou") == 5
    assert count_vowels("xyz") == 0
```

### Example 2: Testing List Functions

```python
# list_operations.py
def find_max(numbers):
    """Find maximum number in list"""
    if not numbers:
        return None
    return max(numbers)

def remove_duplicates(items):
    """Remove duplicates while preserving order"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def chunk_list(items, size):
    """Split list into chunks of specified size"""
    return [items[i:i + size] for i in range(0, len(items), size)]

# test_list_operations.py
from list_operations import find_max, remove_duplicates, chunk_list

def test_find_max():
    assert find_max([1, 5, 3, 9, 2]) == 9
    assert find_max([10]) == 10
    assert find_max([-5, -2, -10]) == -2
    assert find_max([]) is None

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

def test_chunk_list():
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert chunk_list([], 3) == []
    assert chunk_list([1, 2], 5) == [[1, 2]]
```

### Example 3: Testing with pytest.raises

```python
# validators.py
def validate_age(age):
    """Validate age is between 0 and 150"""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age cannot exceed 150")
    return True

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# test_validators.py
import pytest
from validators import validate_age, divide

def test_validate_age_valid():
    assert validate_age(25) == True
    assert validate_age(0) == True
    assert validate_age(150) == True

def test_validate_age_invalid_type():
    with pytest.raises(TypeError):
        validate_age("25")
    with pytest.raises(TypeError):
        validate_age(25.5)

def test_validate_age_invalid_range():
    with pytest.raises(ValueError):
        validate_age(-1)
    with pytest.raises(ValueError):
        validate_age(151)

def test_divide_normal():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    assert divide(0, 5) == 0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

### Example 4: Parameterized Tests

```python
# calculator.py
def factorial(n):
    """Calculate factorial"""
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# test_calculator.py
import pytest
from calculator import factorial

@pytest.mark.parametrize("input,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (3, 6),
    (7, 5040),
])
def test_factorial_valid(input, expected):
    assert factorial(input) == expected

@pytest.mark.parametrize("input", [-1, -5, -100])
def test_factorial_negative(input):
    with pytest.raises(ValueError):
        factorial(input)
```

### Example 5: Testing Classes

```python
# bank_account.py
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

# test_bank_account.py
import pytest
from bank_account import BankAccount

def test_initial_balance():
    account = BankAccount(100)
    assert account.get_balance() == 100

def test_deposit():
    account = BankAccount(100)
    new_balance = account.deposit(50)
    assert new_balance == 150
    assert account.get_balance() == 150

def test_deposit_invalid():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.deposit(0)
    with pytest.raises(ValueError):
        account.deposit(-10)

def test_withdraw():
    account = BankAccount(100)
    new_balance = account.withdraw(30)
    assert new_balance == 70
    assert account.get_balance() == 70

def test_withdraw_insufficient_funds():
    account = BankAccount(50)
    with pytest.raises(ValueError):
        account.withdraw(100)

def test_withdraw_invalid():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.withdraw(0)
    with pytest.raises(ValueError):
        account.withdraw(-10)
```

## Fixtures

```python
# conftest.py or in test file
import pytest

@pytest.fixture
def sample_list():
    """Provide a sample list for tests"""
    return [1, 2, 3, 4, 5]

@pytest.fixture
def bank_account():
    """Provide a BankAccount instance"""
    return BankAccount(1000)

# Using fixtures
def test_with_fixture(sample_list):
    assert len(sample_list) == 5
    assert sum(sample_list) == 15

def test_account_with_fixture(bank_account):
    bank_account.deposit(500)
    assert bank_account.get_balance() == 1500
```

## Test Organization

```python
# Grouping tests with classes
class TestStringOperations:
    def test_uppercase(self):
        assert "hello".upper() == "HELLO"

    def test_lowercase(self):
        assert "WORLD".lower() == "world"

class TestListOperations:
    def test_append(self):
        lst = [1, 2, 3]
        lst.append(4)
        assert lst == [1, 2, 3, 4]

    def test_extend(self):
        lst = [1, 2]
        lst.extend([3, 4])
        assert lst == [1, 2, 3, 4]
```

## pytest Output

```bash
# Normal run
$ pytest
===== test session starts =====
collected 10 items

test_math_operations.py ..        [ 20%]
test_string_utils.py ...          [ 50%]
test_validators.py .....          [100%]

===== 10 passed in 0.05s =====

# Verbose mode
$ pytest -v
===== test session starts =====
collected 10 items

test_math_operations.py::test_add PASSED
test_math_operations.py::test_multiply PASSED
test_string_utils.py::test_reverse_string PASSED
...

===== 10 passed in 0.05s =====

# Show print statements
$ pytest -s

# Stop at first failure
$ pytest -x
```

## Key Takeaways

1. **pytest**: Popular Python testing framework
2. **Test functions**: Start with `test_`
3. **Assertions**: Use `assert` to verify behavior
4. **pytest.raises**: Test for expected exceptions
5. **Parameterize**: Test multiple inputs efficiently
6. **Fixtures**: Reusable test setup code
7. **Organization**: Group related tests in classes
8. **Best practice**: Write tests for all public functions
