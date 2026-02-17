# Pre-Read: Implement Boolean Data Types

## What are Booleans?

**Booleans** have only TWO values: `True` or `False`

```python
is_student = True
has_graduated = False
is_raining = True
```

**Important**: Must be capitalized - `True` and `False` (not `true` or `false`)

### Why Booleans Exist

Programs constantly make decisions:
- Should I show this button?
- Is the user allowed to access this?
- Did the file save successfully?
- Has the timer run out?

All these are **yes/no questions**. Booleans are the data type designed specifically for this.

**Without booleans**, we'd have to use numbers:
```python
is_logged_in = 1  # 1 means yes, 0 means no? Confusing!
```

**With booleans**, the code is clear:
```python
is_logged_in = True  # Crystal clear!
```

### Simple Analogy

Booleans are like **checkbox questions** on a form:
- ☑ "Do you accept the terms?" → True (checked)
- ☐ "Subscribe to newsletter?" → False (unchecked)

Not like fill-in-the-blank questions where you can write anything - just check or don't check.

### The Power of Two

Having only two values might seem limiting, but it's incredibly powerful:
- Computers are built on billions of two-state switches
- Every decision tree breaks down into yes/no branches
- Simple + billions of operations = complex behavior

## When to Use Booleans
- Yes/No questions
- On/Off states  
- Enabled/Disabled
- Pass/Fail

## Boolean in Action
```python
is_logged_in = True

if is_logged_in:
    print("Welcome back!")  # This runs
```

## Naming Booleans
Make them sound like questions:
```python
is_active = True      # "Is it active?"
has_permission = False  # "Has permission?"
can_edit = True       # "Can edit?"
```
