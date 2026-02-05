# Lecture Script: LO-9.3.37 Write Unit Tests Using pytest Framework

## [0:00-0:02] Hook (2 min)
**Say**: "You deploy your code. It crashes. 'But it worked on my machine!' Sound familiar? Unit tests prevent this. Write tests once, run them forever. Pytest makes testing so simple: def test_add(): assert add(2, 3) == 5. Green means ship it. Red means fix it. Professional developers test EVERYTHING!"

**Demo**:
```python
# The code to test
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# The test file (test_math.py)
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
    assert multiply(-2, 5) == -10

# Run: pytest test_math.py
# All green! Ship it!
```

**Say**: "That's pytest! Let's master testing."

## [0:02-0:06] pytest Basics (4 min)

**Say**: "pytest discovers and runs test functions automatically. Just follow the naming convention."

**Live Code**:
```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# test_calculator.py
from calculator import add, subtract, multiply, divide

def test_add():
    """Test addition"""
    assert add(5, 3) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test subtraction"""
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5

def test_multiply():
    """Test multiplication"""
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0

def test_divide():
    """Test division"""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

# Run in terminal: pytest test_calculator.py -v
```

**Point out**: "Test functions MUST start with 'test_'. pytest finds them automatically!"

**Emphasize**: "Use assert for checks. If assert fails, test fails. Simple!"

## [0:06-0:10] Testing Exceptions with pytest.raises (4 min)

**Say**: "Test that code FAILS correctly using pytest.raises context manager."

**Live Code**:
```python
import pytest

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
from validators import validate_age, divide

def test_validate_age_valid():
    """Test valid ages"""
    assert validate_age(25) == True
    assert validate_age(0) == True
    assert validate_age(150) == True

def test_validate_age_invalid_type():
    """Test type errors"""
    with pytest.raises(TypeError):
        validate_age("25")
    with pytest.raises(TypeError):
        validate_age(25.5)

def test_validate_age_invalid_range():
    """Test value errors"""
    with pytest.raises(ValueError):
        validate_age(-1)
    with pytest.raises(ValueError):
        validate_age(151)

def test_divide_normal():
    """Test normal division"""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    """Test division by zero raises error"""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

**Say**: "pytest.raises ensures your code fails gracefully with proper error messages!"

## [0:10-0:13] Real-World Example: Testing String Functions (3 min)

**Say**: "Let's test real utility functions you'd use in projects."

**Live Code**:
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
    """Test string reversal"""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_is_palindrome():
    """Test palindrome detection"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_count_vowels():
    """Test vowel counting"""
    assert count_vowels("hello") == 2
    assert count_vowels("Python") == 1
    assert count_vowels("aeiou") == 5
    assert count_vowels("xyz") == 0
    assert count_vowels("") == 0
```

**Point out**: "Test edge cases: empty strings, single characters, special cases!"

## [0:13-0:16] Parameterized Tests (3 min)

**Say**: "Test multiple inputs efficiently with @pytest.mark.parametrize."

**Live Code**:
```python
import pytest

# math_utils.py
def factorial(n):
    """Calculate factorial"""
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# test_math_utils.py
from math_utils import factorial, is_prime

@pytest.mark.parametrize("input,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (3, 6),
    (7, 5040),
])
def test_factorial_valid(input, expected):
    """Test factorial with multiple inputs"""
    assert factorial(input) == expected

@pytest.mark.parametrize("input", [-1, -5, -100])
def test_factorial_negative(input):
    """Test factorial rejects negative numbers"""
    with pytest.raises(ValueError):
        factorial(input)

@pytest.mark.parametrize("prime_num", [2, 3, 5, 7, 11, 13, 17, 19, 23])
def test_is_prime_true(prime_num):
    """Test that primes are identified"""
    assert is_prime(prime_num) == True

@pytest.mark.parametrize("non_prime", [0, 1, 4, 6, 8, 9, 10, 12, 15])
def test_is_prime_false(non_prime):
    """Test that non-primes are identified"""
    assert is_prime(non_prime) == False
```

**Say**: "One test function, many test cases! Parameterize saves massive duplication!"

## [0:16-0:19] Real-World Example: Testing Classes (3 min)

**Say**: "Classes need testing too! Test initialization, methods, and state changes."

**Live Code**:
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
    """Test account initialization"""
    account = BankAccount(100)
    assert account.get_balance() == 100

    account_zero = BankAccount()
    assert account_zero.get_balance() == 0

def test_deposit():
    """Test depositing money"""
    account = BankAccount(100)
    new_balance = account.deposit(50)
    assert new_balance == 150
    assert account.get_balance() == 150

def test_deposit_invalid():
    """Test invalid deposits"""
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.deposit(0)
    with pytest.raises(ValueError):
        account.deposit(-10)

def test_withdraw():
    """Test withdrawing money"""
    account = BankAccount(100)
    new_balance = account.withdraw(30)
    assert new_balance == 70
    assert account.get_balance() == 70

def test_withdraw_insufficient_funds():
    """Test overdraft prevention"""
    account = BankAccount(50)
    with pytest.raises(ValueError):
        account.withdraw(100)

def test_withdraw_invalid():
    """Test invalid withdrawals"""
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.withdraw(0)
    with pytest.raises(ValueError):
        account.withdraw(-10)
```

**Point out**: "Create fresh instances for each test. Tests should be independent!"

## [0:19-0:21] Fixtures for Test Setup (2 min)

**Say**: "Fixtures provide reusable test data. Define once, use everywhere!"

**Live Code**:
```python
import pytest
from bank_account import BankAccount

@pytest.fixture
def empty_account():
    """Provide an empty bank account"""
    return BankAccount(0)

@pytest.fixture
def funded_account():
    """Provide a funded bank account"""
    return BankAccount(1000)

@pytest.fixture
def sample_numbers():
    """Provide sample numbers for testing"""
    return [1, 2, 3, 4, 5]

# Using fixtures
def test_empty_account_balance(empty_account):
    """Test empty account"""
    assert empty_account.get_balance() == 0

def test_deposit_to_empty(empty_account):
    """Test depositing to empty account"""
    empty_account.deposit(100)
    assert empty_account.get_balance() == 100

def test_withdraw_from_funded(funded_account):
    """Test withdrawing from funded account"""
    funded_account.withdraw(500)
    assert funded_account.get_balance() == 500

def test_sample_numbers(sample_numbers):
    """Test with sample numbers"""
    assert len(sample_numbers) == 5
    assert sum(sample_numbers) == 15
```

**Say**: "Fixtures run before each test. Clean, isolated test data every time!"

## [0:21-0:23] Running Tests (2 min)

**Say**: "pytest has many options for running tests. Let me show you the most useful."

**Live Code**:
```bash
# Run all tests in current directory
pytest

# Run specific test file
pytest test_calculator.py

# Run with verbose output
pytest -v

# Run specific test function
pytest test_calculator.py::test_add

# Run tests matching a pattern
pytest -k "divide"

# Stop at first failure
pytest -x

# Show print statements
pytest -s

# Generate coverage report
pytest --cov=mymodule
```

**Say**: "pytest discovers tests automatically. Just run pytest!"

## [0:23-0:24] Practice Challenge (1 min)

**Challenge**: "Write tests for a shopping cart class."

**Skeleton**:
```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})

    def get_total(self):
        return sum(item["price"] for item in self.items)

    def clear(self):
        self.items = []

# TODO: Write tests for ShoppingCart
```

**Solution** (show after 1 minute):
```python
def test_empty_cart():
    cart = ShoppingCart()
    assert cart.get_total() == 0

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("Book", 10.99)
    assert cart.get_total() == 10.99

def test_multiple_items():
    cart = ShoppingCart()
    cart.add_item("Book", 10.99)
    cart.add_item("Pen", 1.50)
    assert cart.get_total() == 12.49

def test_clear():
    cart = ShoppingCart()
    cart.add_item("Book", 10.99)
    cart.clear()
    assert cart.get_total() == 0
```

## [0:24-0:25] Wrap-up (1 min)

**Key Points**:
1. **Test functions**: Start with test_, use assert
2. **pytest.raises**: Test exceptions and error handling
3. **Parametrize**: Test multiple inputs efficiently
4. **Fixtures**: Reusable test data and setup
5. **Run tests**: pytest discovers and runs automatically

**Common Mistakes**:
- Not testing edge cases (empty, null, boundary values)
- Tests depend on each other (should be independent)
- Forgetting to test error conditions
- Not running tests before committing code

**Test Organization**:
- One test file per module (test_calculator.py for calculator.py)
- Group related tests in classes
- Use descriptive test names
- Test one thing per test function

**What to Test**:
- Normal cases (happy path)
- Edge cases (empty, boundaries)
- Error conditions (exceptions)
- All public methods
- Different input combinations

**When to Test**:
- Before writing code (TDD - Test Driven Development)
- While writing code
- Before committing
- In CI/CD pipeline (automated)

**Benefits**:
- Catch bugs early
- Confident refactoring
- Living documentation
- Faster debugging
- Professional code quality

**Closing**: "Testing isn't optional — it's essential! Write tests for all your code. pytest makes it easy. Green tests = confidence. Red tests = bugs caught early. Start testing today!"
