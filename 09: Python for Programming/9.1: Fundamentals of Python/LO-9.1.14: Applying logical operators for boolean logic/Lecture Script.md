### LO-14 Apply Logical Operators (20 minutes)


### CS Theory Bite

> **Origin**: Logical operators (`and`, `or`, `not`) implement **Boolean algebra** (George Boole, 1854) and **De Morgan's Laws**: `not (A and B)` = `not A or not B`. These same operations are hardwired into CPU logic gates.
>
> **Analogy**: Logical operators are like **bouncers at a club** — `and` means BOTH conditions pass, `or` means EITHER passes, `not` reverses the decision.
>
> **Why it matters**: Complex conditions require combining simple comparisons — logical operators are the glue.


### Hook (2 minutes)

**Say**: "You're at a restaurant. You can order dessert if you finished your meal AND you're still hungry. OR if it's your birthday. That's logical operators in real life!"

### The `and` Operator (6 minutes)

**Say**: "`and` means BOTH conditions must be true."

```python
age = 20
has_license = True

can_drive = age >= 18 and has_license
print(can_drive)  # True
```

### The `or` Operator (6 minutes)

**Say**: "`or` means AT LEAST ONE condition must be true."

```python
is_weekend = True
is_holiday = False

can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)  # True
```

### The `not` Operator (4 minutes)

**Say**: "`not` flips True to False and False to True."

```python
is_raining = False
is_sunny = not is_raining
print(is_sunny)  # True
```

**Real-World**: ```python
form_submitted = False
can_edit = not form_submitted
print(f"Can edit: {can_edit}")  # True
```

### Combining Operators (4 minutes)

**Say**: "Now let's combine them all!"

```python
age = 17
has_parent_consent = True
has_id = True

# Can register if 18+ OR (under 18 but has consent AND ID)
can_register = age >= 18 or (age < 18 and has_parent_consent and has_id)
print(f"Can register: {can_register}")  # True
```

### Practice & Wrap-up (3 minutes)

```python
a = True
b = False
print(a and b)
print(a or b)
print(not b)
```

