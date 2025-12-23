# Lecture Script: LO-14 Apply Logical Operators

## [0:00-0:02] Hook (2 min)
**Say**: "You're at a restaurant. You can order dessert if you finished your meal AND you're still hungry. OR if it's your birthday. That's logical operators in real life!"

**Write on board**: `finished_meal AND still_hungry OR is_birthday`

## [0:02-0:08] The `and` Operator (6 min)

**Say**: "`and` means BOTH conditions must be true."

**Live Code**:
```python
age = 20
has_license = True

can_drive = age >= 18 and has_license
print(can_drive)  # True
```

**Ask**: "What if has_license was False?"
**Change and show**: `has_license = False` → Output is False

**Write truth table on board**:
```
True and True = True
True and False = False
False and True = False
False and False = False
```

**Key Point**: "BOTH must be True, or the result is False!"

### Real-World Example

**Say**: "Let's check if someone qualifies for a loan."

**Live Code**:
```python
age = 25
income = 50000
good_credit = True

qualifies = age >= 21 and income >= 30000 and good_credit
print(f"Qualifies: {qualifies}")  # True
```

**Try different values** to show when it becomes False

## [0:08-0:14] The `or` Operator (6 min)

**Say**: "`or` means AT LEAST ONE condition must be true."

**Live Code**:
```python
is_weekend = True
is_holiday = False

can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)  # True
```

**Write truth table**:
```
True or True = True
True or False = True
False or True = True
False or False = False
```

**Key Point**: "Only False when BOTH are False!"

### Real-World Example

**Live Code**:
```python
has_cash = False
has_card = True

can_pay = has_cash or has_card
print(f"Can pay: {can_pay}")  # True
```

## [0:14-0:18] The `not` Operator (4 min)

**Say**: "`not` flips True to False and False to True."

**Live Code**:
```python
is_raining = False
is_sunny = not is_raining
print(is_sunny)  # True
```

**Show both ways**:
```python
is_raining = True
print(not is_raining)  # False

is_raining = False
print(not is_raining)  # True
```

**Real-World Example**:
```python
form_submitted = False
can_edit = not form_submitted
print(f"Can edit: {can_edit}")  # True
```

## [0:18-0:22] Combining Operators (4 min)

**Say**: "Now let's combine them all!"

**Live Code**:
```python
age = 17
has_parent_consent = True
has_id = True

# Can register if 18+ OR (under 18 but has consent AND ID)
can_register = age >= 18 or (age < 18 and has_parent_consent and has_id)
print(f"Can register: {can_register}")  # True
```

**Point out parentheses**: "These make it clear which conditions go together!"

**Show precedence**:
```python
# Without parentheses - harder to read
result = True or True and False
print(result)  # True

# With parentheses - crystal clear
result = True or (True and False)
print(result)  # True
```

## [0:22-0:25] Practice & Wrap-up (3 min)

**Challenge**: "Without running it, predict the output:"

**Write on board**:
```python
a = True
b = False
print(a and b)
print(a or b)
print(not b)
```

**Give students 30 seconds**

**Reveal**:
```python
False  # both must be True
True   # at least one is True
True   # reverses False
```

**Bonus Challenge**:
```python
print(a and b or not b)  # What is this?
```

**Walk through**:
- `a and b` = False
- `not b` = True
- `False or True` = True

**Closing Tip**: "When using multiple logical operators, use parentheses! Your future self will thank you."

## Key Points to Reinforce
1. `and` needs BOTH True
2. `or` needs AT LEAST ONE True
3. `not` flips the value
4. Always use parentheses for clarity
5. Precedence: not → and → or
