# Pre-Read: Apply Logical Operators

## What You'll Learn
In this lesson, you'll learn how to combine multiple conditions using logical operators.

## Why Logical Operators?
Sometimes you need to check **multiple conditions** at once:
- "Is the user logged in AND is the password correct?"
- "Is it weekend OR is it a holiday?"
- "Is the form NOT submitted yet?"

## The Three Logical Operators

### AND - Both Must Be True
```python
age = 20
has_license = True

can_drive = age >= 18 and has_license
print(can_drive)  # True (both conditions are true)
```

### OR - At Least One Must Be True
```python
is_weekend = True
is_holiday = False

can_relax = is_weekend or is_holiday
print(can_relax)  # True (one condition is true)
```

### NOT - Reverses the Value
```python
is_raining = False
should_go_out = not is_raining
print(should_go_out)  # True (reversed False to True)
```

## Quick Reference

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both must be True | `a and b` |
| `or` | At least one True | `a or b` |
| `not` | Reverse the value | `not a` |

## Real-World Example
```python
age = 25
income = 50000

qualifies_for_loan = age >= 21 and income >= 30000
print(qualifies_for_loan)  # True
```

## What's Next?
In the main lesson, you'll learn:
- Truth tables for each operator
- How to combine multiple logical operators
- Short-circuit evaluation
- Practical applications
