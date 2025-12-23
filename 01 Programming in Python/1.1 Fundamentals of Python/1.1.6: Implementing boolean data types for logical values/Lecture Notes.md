# Lecture Notes: Implement Boolean Data Types

## What are Booleans?

**Boolean**: Data type with two values - `True` or `False`


```python
is_active = True
is_logged_in = False
game_over = False
```

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
