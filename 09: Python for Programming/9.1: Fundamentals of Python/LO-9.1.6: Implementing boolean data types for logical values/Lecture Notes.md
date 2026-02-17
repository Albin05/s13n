# Lecture Notes: Implement Boolean Data Types

## What are Booleans?

**Boolean**: Data type with two values - `True` or `False`

```python
is_active = True
is_logged_in = False
game_over = False
```

### The Foundation of Computing

Booleans are named after **George Boole** (1815-1864), an English mathematician who invented Boolean algebra - the mathematics of True and False.

**Why this matters**: Boolean algebra is the **foundation of all digital computing**.

At the hardware level, computers are made of billions of **transistors** - tiny switches that are either:
- **ON** (electricity flowing) = True = 1
- **OFF** (no electricity) = False = 0

Everything your computer does - from displaying this text to running games - reduces to billions of True/False decisions happening billions of times per second.

**Historical Impact**: Without Boolean algebra:
- No computers, smartphones, or internet
- No digital logic gates (AND, OR, NOT)
- No programming languages

### Why Only Two Values?

Other data types have many values:
- Integers: ..., -2, -1, 0, 1, 2, ...
- Strings: infinite possibilities

Booleans have just **two** values because they represent **binary decisions**:
- Is the door open? Yes or No
- Is the user logged in? True or False
- Did the payment succeed? Success or Failure

This simplicity is powerful - it mirrors how we make decisions.

### Real-World Analogy

Think of booleans like **light switches**:
- A switch has two states: ON or OFF
- You can't have a switch "half on"
- Multiple switches control different lights (multiple boolean variables)

Or think of **yes/no questions**:
- "Are you a student?" → True or False
- "Is it raining?" → True or False
- "Have you eaten?" → True or False

## Creating Booleans
```python
# Direct assignment
is_student = True
has_permission = False

# From comparisons (preview of LO-13)
age = 20
is_adult = age >= 18  # True
```

## Boolean Usage

### In Conditions
```python
is_raining = True

if is_raining:
    print("Bring umbrella!")
```

### Storing State
```python
is_game_over = False

while not is_game_over:
    # Game logic
    pass
```

## Naming Convention
Boolean variables should sound like yes/no questions:
```python
is_active = True       # "Is it active?"
has_data = False       # "Has data?"
can_proceed = True     # "Can proceed?"
should_save = False    # "Should save?"
```

## Key Takeaways
1. Only two values: True/False
2. Must be capitalized
3. Used for yes/no logic
4. Name as questions
5. Essential for control flow
