# Question Bank: Write Unit Tests with pytest

## Problem 1 (Easy)

**Title:** Test Simple Functions

**Problem Statement:**
Write tests for these functions:

```python
def is_even(n):
    return n % 2 == 0

def get_first_element(lst):
    if not lst:
        return None
    return lst[0]
```

Create a test file with at least 3 test cases for each function.

**Constraints:**
- Use pytest
- Test both normal and edge cases

---

## Problem 2 (Easy)

**Title:** Test String Function

**Problem Statement:**
Write tests for this function:

```python
def capitalize_words(sentence):
    return " ".join(word.capitalize() for word in sentence.split())
```

Test with at least 4 different inputs including edge cases.

**Constraints:**
- Test empty strings
- Test single words
- Test multiple words

---

## Problem 3 (Medium)

**Title:** Test Exception Handling

**Problem Statement:**
Write tests for this function that should raise exceptions for invalid inputs:

```python
def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)
```

Write tests for both valid inputs and exception cases.

**Constraints:**
- Use pytest.raises for exception testing
- Test boundary values

---

## Problem 4 (Medium)

**Title:** Parameterized Tests

**Problem Statement:**
Write parameterized tests for this function:

```python
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
```

Use @pytest.mark.parametrize to test multiple score/grade combinations.

**Constraints:**
- Test at least 10 different scores
- Include boundary values (90, 80, 70, 60)

---

## Problem 5 (Hard)

**Title:** Test Shopping Cart Class

**Problem Statement:**
Write comprehensive tests for this ShoppingCart class:

```python
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
```

Write at least 8 test functions covering all methods and edge cases.

**Constraints:**
- Test all methods
- Test exception cases
- Use fixtures if helpful
