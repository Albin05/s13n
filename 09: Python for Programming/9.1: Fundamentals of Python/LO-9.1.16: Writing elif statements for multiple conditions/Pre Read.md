# Pre-Read: Write Elif Statements

## Why Elif?

Real life has more than two options:
- **Weather**: Sunny, Cloudy, Rainy, Snowy (not just good/bad)
- **Grades**: A, B, C, D, F (not just pass/fail)
- **Age groups**: Child, Teen, Adult, Senior

Elif lets you handle multiple possibilities elegantly!

### Simple Analogy

Think of elif like **choosing an outfit based on weather**:
- IF temperature > 80: wear shorts
- ELIF temperature > 60: wear jeans
- ELIF temperature > 40: wear jacket
- ELSE: wear heavy coat

The program checks from top to bottom and stops at the first match.

## What You'll Learn
In this lesson, you'll learn how to handle multiple different conditions using elif (else if) statements.

## The Problem with Multiple If Statements

With only `if` statements, every condition is checked:

```python
score = 85

if score >= 90:
    print("Grade: A")

if score >= 80:
    print("Grade: B")  # This also runs!

if score >= 70:
    print("Grade: C")

# Output: Grade: B (and we also check unnecessary conditions)
```

This works, but it's inefficient and can give unexpected results.

## Enter elif (Else If)

`elif` lets you check multiple conditions, but **stops as soon as one is True**:

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # This runs and stops!
elif score >= 70:
    print("Grade: C")  # Never checked

# Output: Grade: B
```

## Basic Syntax

```python
if condition1:
    # Runs if condition1 is True
elif condition2:
    # Runs if condition1 is False and condition2 is True
elif condition3:
    # Runs if condition1 and condition2 are False, and condition3 is True
```

**Key Points**:
- `elif` comes after `if`
- You can have multiple `elif` statements
- Only ONE block runs (the first True condition)
- Once a condition is True, the rest are skipped

## Real-World Example

```python
age = 15

if age >= 18:
    print("Adult ticket: $12")
elif age >= 13:
    print("Teen ticket: $8")  # This runs!
elif age >= 5:
    print("Child ticket: $5")
else:
    print("Free for under 5")

# Output: Teen ticket: $8
```

## What's Next?
In the main lesson, you'll learn:
- Detailed elif syntax and rules
- When to use elif vs multiple if statements
- Common patterns and best practices
- Debugging elif chains
