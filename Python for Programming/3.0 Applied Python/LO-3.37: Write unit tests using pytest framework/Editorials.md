# Editorials: Write Unit Tests with pytest

## Problem 1: Test Simple Functions

```python
def is_even(n):
    return n % 2 == 0

def get_first_element(lst):
    if not lst:
        return None
    return lst[0]

# test_functions.py
def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    assert is_even(-2) == True

def test_get_first_element():
    assert get_first_element([1, 2, 3]) == 1
    assert get_first_element(["a"]) == "a"
    assert get_first_element([]) is None
```

---

## Problem 2: Test String Function

```python
def capitalize_words(sentence):
    return " ".join(word.capitalize() for word in sentence.split())

# test_string.py
def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("HELLO") == "Hello"
    assert capitalize_words("") == ""
    assert capitalize_words("hello") == "Hello"
    assert capitalize_words("hello world python") == "Hello World Python"
```

---

## Problem 3: Test Exception Handling

```python
import pytest

def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)

# test_discount.py
def test_calculate_discount_valid():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(100, 0) == 100
    assert calculate_discount(100, 100) == 0

def test_calculate_discount_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-10, 10)

def test_calculate_discount_invalid_percent():
    with pytest.raises(ValueError):
        calculate_discount(100, -5)
    with pytest.raises(ValueError):
        calculate_discount(100, 101)
```

---

## Problem 4: Parameterized Tests

```python
import pytest

def grade_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# test_grades.py
@pytest.mark.parametrize("score,expected", [
    (95, "A"),
    (90, "A"),
    (89, "B"),
    (80, "B"),
    (79, "C"),
    (70, "C"),
    (69, "D"),
    (60, "D"),
    (59, "F"),
    (0, "F"),
])
def test_grade_score(score, expected):
    assert grade_score(score) == expected
```

---

## Problem 5: Test Shopping Cart Class

```python
import pytest

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })

    def get_total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def get_item_count(self):
        return sum(item["quantity"] for item in self.items)

    def clear(self):
        self.items = []

# test_shopping_cart.py
@pytest.fixture
def cart():
    return ShoppingCart()

def test_empty_cart(cart):
    assert cart.get_total() == 0
    assert cart.get_item_count() == 0

def test_add_single_item(cart):
    cart.add_item("Apple", 1.5)
    assert cart.get_total() == 1.5
    assert cart.get_item_count() == 1

def test_add_multiple_items(cart):
    cart.add_item("Apple", 1.5, 3)
    cart.add_item("Banana", 0.5, 2)
    assert cart.get_total() == 5.5
    assert cart.get_item_count() == 5

def test_add_item_negative_price(cart):
    with pytest.raises(ValueError):
        cart.add_item("Item", -10)

def test_add_item_zero_quantity(cart):
    with pytest.raises(ValueError):
        cart.add_item("Item", 10, 0)

def test_add_item_negative_quantity(cart):
    with pytest.raises(ValueError):
        cart.add_item("Item", 10, -5)

def test_clear_cart(cart):
    cart.add_item("Apple", 1.5, 2)
    cart.clear()
    assert cart.get_total() == 0
    assert cart.get_item_count() == 0

def test_multiple_operations(cart):
    cart.add_item("Apple", 1.0, 2)
    cart.add_item("Banana", 0.5, 3)
    assert cart.get_total() == 3.5
    cart.clear()
    assert cart.get_total() == 0
```
