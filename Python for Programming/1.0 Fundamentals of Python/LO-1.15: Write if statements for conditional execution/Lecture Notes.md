# Lecture Notes: Write If Statements

## If Statements

An `if` statement allows your program to execute code **only when a condition is True**.


---

<div align="center">

![Flowchart showing decision making](https://images.unsplash.com/photo-1559027615-cd4628902d4a?w=800&q=80)

*Control flow determines the execution path of your program*

</div>

---
### Basic Syntax

```python
if condition:
    # Code block (indented)
    # Runs only if condition is True
```

**Key Components**:
1. The `if` keyword
2. A condition (boolean expression)
3. A colon `:`
4. Indented code block

## Simple Examples

### Example 1: Basic If Statement

```python
age = 20

if age >= 18:
    print("You are an adult")

# Output: You are an adult
```

### Example 2: Condition is False

```python
age = 15

if age >= 18:
    print("You are an adult")

# No output (condition is False, code doesn't run)
```

### Example 3: Multiple Statements

```python
score = 95

if score >= 90:
    print("Excellent work!")
    print("You got an A")
    print("Keep it up!")

# All three lines print because condition is True
```

## Indentation Rules

Python uses **indentation** (spaces or tabs) to group code blocks. This is **required**, not optional!

### Correct Indentation

```python
if age >= 18:
    print("You can vote")      # Indented - part of if block
    print("You are an adult")  # Indented - part of if block
print("Program continues")     # Not indented - always runs
```

### Indentation Error

```python
if age >= 18:
print("You can vote")  # IndentationError: expected an indented block
```

### Inconsistent Indentation

```python
if age >= 18:
    print("Line 1")  # 4 spaces
        print("Line 2")  # 8 spaces - IndentationError!
```

**Best Practice**: Use **4 spaces** for each indentation level (standard Python convention)

## Using Conditions

### With Comparison Operators

```python
temperature = 30

if temperature > 25:
    print("It's hot outside")

score = 85
if score >= 60:
    print("You passed")

password = "secret"
if password == "secret":
    print("Access granted")
```

### With Logical Operators

```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive")

is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("You can sleep in")

form_submitted = False
if not form_submitted:
    print("You can still edit")
```

### With Variables

```python
is_logged_in = True

if is_logged_in:
    print("Welcome back!")

is_admin = False
if is_admin:
    print("Admin panel")  # Doesn't print (False)
```

## Multiple If Statements

You can have multiple independent if statements:

```python
score = 85

if score >= 60:
    print("You passed")

if score >= 70:
    print("You got a C or better")

if score >= 80:
    print("You got a B or better")

if score >= 90:
    print("You got an A")

# Output:
# You passed
# You got a C or better
# You got a B or better
```

**Note**: Each if statement is checked independently!

## Real-World Examples

### Example 1: Age Verification

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You can create an account")
    print("Welcome!")

if age >= 21:
    print("You can access premium features")
```

### Example 2: Password Validation

```python
password = input("Enter password: ")

if len(password) < 8:
    print("Password too short")

if len(password) >= 8:
    print("Password length OK")

if len(password) >= 12:
    print("Strong password!")
```

### Example 3: Grade Checker

```python
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
    print("Excellent!")

if score >= 80 and score < 90:
    print("Grade: B")
    print("Good job!")

if score >= 70 and score < 80:
    print("Grade: C")
    print("Not bad!")

if score < 60:
    print("Grade: F")
    print("Need improvement")
```

### Example 4: Login System

```python
username = input("Enter username: ")
password = input("Enter password: ")

correct_username = "admin"
correct_password = "secret123"

if username == correct_username and password == correct_password:
    print("Login successful!")
    print("Welcome, admin!")

if username != correct_username:
    print("Invalid username")

if password != correct_password:
    print("Invalid password")
```

### Example 5: Temperature Alert

```python
temperature = float(input("Enter temperature: "))

if temperature >= 37.5:
    print("You have a fever")
    print("Please see a doctor")

if temperature >= 39:
    print("High fever - seek immediate medical attention!")

if temperature < 35:
    print("Low temperature - hypothermia risk")
```

## Flow Control Visualization

```python
age = 20

print("Start")

if age >= 18:
    print("Adult")  # This runs

print("End")

# Output:
# Start
# Adult
# End
```

```python
age = 15

print("Start")

if age >= 18:
    print("Adult")  # This does NOT run

print("End")

# Output:
# Start
# End
```

## Common Mistakes

### 1. Forgetting the Colon

```python
# Wrong
if age >= 18
    print("Adult")  # SyntaxError: invalid syntax

# Correct
if age >= 18:
    print("Adult")
```

### 2. No Indentation

```python
# Wrong
if age >= 18:
print("Adult")  # IndentationError

# Correct
if age >= 18:
    print("Adult")
```

### 3. Using `=` Instead of `==`

```python
# Wrong - This assigns 18 to age!
if age = 18:  # SyntaxError
    print("18 years old")

# Correct - This compares
if age == 18:
    print("18 years old")
```

### 4. Forgetting Indentation for Multiple Lines

```python
# Wrong - Only first line is in if block
if age >= 18:
    print("You are an adult")
print("You can vote")  # Always runs!

# Correct - Both lines in if block
if age >= 18:
    print("You are an adult")
    print("You can vote")  # Both indented
```

### 5. Empty If Block

```python
# Wrong - If block can't be empty
if age >= 18:

# Correct - Use pass as placeholder
if age >= 18:
    pass  # Do nothing (placeholder)
```

## Practice Exercise

Predict what will be printed:

```python
x = 10

if x > 5:
    print("A")
    print("B")

if x > 15:
    print("C")

print("D")
```

<details>
<summary>Answer</summary>

```
A
B
D
```

Explanation:
- x > 5 is True (10 > 5), so "A" and "B" print
- x > 15 is False (10 is not > 15), so "C" doesn't print
- "D" always prints (not in any if block)
</details>

## Key Takeaways

1. **Syntax**: `if condition:`
2. **Colon required**: After the condition
3. **Indentation required**: 4 spaces is standard
4. **Condition**: Any boolean expression
5. **Code block**: All indented lines run if condition is True
6. **Independent checks**: Multiple if statements check independently

## What's Next?

In the next lessons, you'll learn:
- `elif` (else if) for multiple conditions
- `else` for default cases
- Nested if statements
- More complex decision-making
