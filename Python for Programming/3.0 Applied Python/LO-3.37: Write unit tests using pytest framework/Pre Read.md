# Pre-Read: Write Unit Tests with pytest

## Unit Testing with pytest

Unit tests verify that individual functions work correctly:

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# test_calculator.py
import pytest
from calculator import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
```

## Running Tests

```bash
# Install pytest
pip install pytest

# Run tests
pytest test_calculator.py

# Output:
# ===== test session starts =====
# collected 2 items
#
# test_calculator.py ..  [100%]
#
# ===== 2 passed in 0.01s =====
```

## Basic Assertions

```python
def test_assertions():
    # Basic equality
    assert 5 == 5

    # Inequality
    assert 10 != 5

    # Comparisons
    assert 10 > 5
    assert 3 < 7

    # Boolean
    assert True
    assert not False

    # Membership
    assert 3 in [1, 2, 3]
    assert "hello" in "hello world"
```
