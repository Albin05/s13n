# Lecture Notes: Apply Logical Operators

## Introduction

Logical operators are the **building blocks of complex decision-making**. They allow programs to combine multiple conditions and make sophisticated choices.

---

<div align="center">

![Python Logical Operators Truth Table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.14.png)

*Truth tables for AND, OR, and NOT — Python's logical operators (and, or, not) follow these exact rules*

</div>

---

### The Foundation: Boolean Algebra

These operators implement **Boolean algebra**, invented by George Boole in 1847. This mathematical system forms the foundation of:
- All digital logic circuits (AND, OR, NOT gates)
- Database queries (SQL WHERE clauses)
- Search engines (Google's AND, OR, NOT operators)
- Every programming language's conditional logic

**Why this matters**: The logic gates in your CPU physically implement these operations billions of times per second!

### Real-World Analogy

Think of logical operators like **decision-making rules**:

**AND** is like **requirements** that ALL must be met:
- To drive: Need license AND age >= 16 AND vehicle
- To graduate: Pass all courses AND complete project AND attend ceremony

**OR** is like **alternatives** where ANY works:
- To pay: Cash OR card OR mobile payment
- To contact: Email OR phone OR in-person

**NOT** is like **opposite/negation**:
- NOT raining = sunny
- NOT logged_in = logged_out
- NOT available = busy

Or think of them like **filters stacked on each other**:
- Photo filter 1 AND filter 2 AND filter 3 = all must apply
- Show results from source A OR source B = either is fine

## Logical Operators

Logical operators combine or modify boolean values. They're essential for creating complex conditions.


### The Three Logical Operators

| Operator | Description | Returns True When |
|----------|-------------|-------------------|
| `and` | Both conditions must be True | Both are True |
| `or` | At least one condition must be True | One or both are True |
| `not` | Reverses the boolean value | The value is False |

## The `and` Operator

Returns `True` only if **both** conditions are True.

### Truth Table

| A | B | A and B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

### Examples

```python
# Simple example
age = 20
has_license = True
can_drive = age >= 18 and has_license
print(can_drive)  # True

# Multiple conditions
temperature = 25
is_sunny = True
is_weekend = True
perfect_day = temperature > 20 and is_sunny and is_weekend
print(perfect_day)  # True

# When one is False
score = 85
passed_exam = score >= 60
submitted_assignment = False
can_pass_course = passed_exam and submitted_assignment
print(can_pass_course)  # False (one is False!)
```

### Real-World: Loan Qualification

```python
age = 25
income = 50000
has_good_credit = True

qualifies = age >= 21 and income >= 30000 and has_good_credit
print(f"Qualifies for loan: {qualifies}")  # True
```

## The `or` Operator

Returns `True` if **at least one** condition is True.

### Truth Table

| A | B | A or B |
|---|---|--------|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

### Examples

```python
# Simple example
is_weekend = True
is_holiday = False
can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)  # True (one is True!)

# Both are True
has_cash = True
has_card = True
can_pay = has_cash or has_card
print(can_pay)  # True

# Both are False
is_raining = False
is_snowing = False
is_bad_weather = is_raining or is_snowing
print(is_bad_weather)  # False (both are False)
```

### Real-World: Access Control

```python
is_admin = False
is_owner = True
has_access = is_admin or is_owner
print(f"Has access: {has_access}")  # True
```

## The `not` Operator

Reverses the boolean value.

### Truth Table

| A | not A |
|---|-------|
| True | False |
| False | True |

### Examples

```python
# Simple reversal
is_raining = False
is_sunny = not is_raining
print(is_sunny)  # True

# With comparisons
age = 16
is_adult = not (age < 18)  # Same as age >= 18
print(is_adult)  # False

# Double negative
is_logged_in = True
is_not_logged_in = not is_logged_in
is_logged_in_again = not is_not_logged_in
print(is_logged_in_again)  # True (double negative!)
```

### Real-World: Form Validation

```python
form_submitted = False
can_edit = not form_submitted
print(f"Can edit: {can_edit}")  # True
```

## Combining Logical Operators

You can combine multiple logical operators to create complex conditions.

### Example 1: Age Range Check

```python
age = 25
is_adult = age >= 18 and age < 65
print(f"Working age adult: {is_adult}")  # True
```

### Example 2: Access Control

```python
is_admin = False
is_moderator = True
is_owner = False

has_special_access = is_admin or is_moderator or is_owner
print(f"Has special access: {has_special_access}")  # True
```

### Example 3: Complex Validation

```python
age = 17
has_parent_consent = True
has_id = True

# Can register if (18+) OR (under 18 but has parent consent)
can_register = (age >= 18) or (age < 18 and has_parent_consent and has_id)
print(f"Can register: {can_register}")  # True
```

### Example 4: Nested Logic

```python
temperature = 28
humidity = 70
has_ac = False

is_uncomfortable = (temperature > 25 and humidity > 60) and not has_ac
print(f"Uncomfortable: {is_uncomfortable}")  # True
```

## Operator Precedence

When combining operators, Python evaluates in this order:

1. **Parentheses** `()`
2. **not**
3. **and**
4. **or**

### Examples

```python
# Without parentheses
result = True or True and False
# Evaluates as: True or (True and False) = True or False = True
print(result)  # True

# With parentheses to force different order
result = (True or True) and False
# Evaluates as: True and False = False
print(result)  # False
```

**Best Practice**: Use parentheses for clarity!

```python
# Harder to read
can_proceed = age >= 18 and has_license or has_permit and has_supervisor

# Clearer with parentheses
can_proceed = (age >= 18 and has_license) or (has_permit and has_supervisor)
```

## Short-Circuit Evaluation

Python evaluates logical operators **left to right** and stops as soon as the result is determined.

### With `and`

```python
# If first is False, second is never checked
def expensive_check():
    print("Expensive check called")
    return True

age = 16
result = age >= 18 and expensive_check()
# expensive_check() is NEVER called because age >= 18 is False
print(result)  # False
```

### With `or`

```python
# If first is True, second is never checked
is_admin = True
result = is_admin or expensive_check()
# expensive_check() is NEVER called because is_admin is already True
print(result)  # True
```

**Why This Matters**: You can safely check conditions without errors:

```python
username = None
# Safe: won't error because len() is never called if username is None
is_valid = username is not None and len(username) > 0
print(is_valid)  # False
```

## Common Patterns

### Checking Ranges

```python
# Age between 18 and 65
age = 30
is_working_age = age >= 18 and age <= 65
# Or more concisely:
is_working_age = 18 <= age <= 65  # Python allows chaining!
print(is_working_age)  # True
```

### Validating Multiple Conditions

```python
password = "secure123"
username = "john_doe"

# All must be true
is_valid = (
    len(username) >= 3 and
    len(password) >= 8 and
    username != password
)
print(f"Valid registration: {is_valid}")  # True
```

### Default Values with `or`

```python
name = ""
display_name = name or "Guest"
print(display_name)  # "Guest" (empty string is falsy)

name = "Alice"
display_name = name or "Guest"
print(display_name)  # "Alice"
```

## Common Mistakes

### 1. Using `&` or `|` Instead of `and`/`or`

```python
# Wrong (these are bitwise operators)
result = True & False  # Works but not recommended for booleans

# Correct
result = True and False
```

### 2. Forgetting Parentheses

```python
# Confusing
age = 20
has_license = True
can_drive = age >= 18 and has_license or not has_license

# Clear
can_drive = (age >= 18 and has_license) or (not has_license)
```

### 3. Redundant Comparisons

```python
# Redundant
is_adult = (age >= 18) == True

# Better
is_adult = age >= 18
```

## Practice Exercise

Predict the output:

```python
a = True
b = False
c = True

print(a and b)           # ?
print(a or b)            # ?
print(not b)             # ?
print(a and b or c)      # ?
print(a and (b or c))    # ?
print(not (a and b))     # ?
```

<details>
<summary>Answer</summary>

```python
print(a and b)           # False
print(a or b)            # True
print(not b)             # True
print(a and b or c)      # True (evaluates as (a and b) or c)
print(a and (b or c))    # True
print(not (a and b))     # True
```
</details>

## Key Takeaways

1. **`and`**: Both conditions must be True
2. **`or`**: At least one condition must be True
3. **`not`**: Reverses the boolean value
4. **Precedence**: `not` > `and` > `or`
5. **Short-circuit**: Evaluation stops when result is determined
6. **Use parentheses**: Makes complex conditions clearer
