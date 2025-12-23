### LO-6 Implement Boolean Data Types (15 minutes)

### Hook (3 minutes)

**Say**: "Is the light on or off? Is the door open or closed? Life is full of yes/no questions - that's what booleans are for!"

```python
is_logged_in = True
has_permission = False
```

### Boolean Basics (6 minutes)

**Say**: "Booleans have only two values: True and False. Notice the capital letters - Python is picky!"

```python
is_raining = True
is_weekend = False

print(type(is_raining))  # <class 'bool'>
```

**Key Points**:
- Only two values: `True` and `False`
- Must be capitalized (true/false won't work!)
- Used for conditions and logic
- Result of comparisons are booleans

```python
age = 20
is_adult = age >= 18  # True (comparison result)
print(is_adult)  # True
```

**Real-World**: Every login system uses booleans - is user authenticated? Does user have admin rights?

### Boolean in Conditionals (4 minutes)

**Say**: "Booleans power if statements. They decide which code runs."

```python
is_member = True

if is_member:
    print("Welcome back!")
else:
    print("Please sign up")
```

### Practice (2 minutes)

Create booleans for real scenarios:
```python
is_sunny = True
has_homework = False
is_class_over = False

# Use in condition
if is_sunny:
    print("Let's go outside!")
```
