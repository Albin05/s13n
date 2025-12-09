# Pre-Read: Write If Statements

## What You'll Learn
In this lesson, you'll learn how to make your program execute code only when certain conditions are met.

## What is an If Statement?
An `if` statement lets your program make decisions:
- "IF it's raining, bring an umbrella"
- "IF age is 18 or above, allow voting"
- "IF password is correct, log in"

## Basic Syntax

```python
if condition:
    # Code to run if condition is True
    print("Condition was True!")
```

**Important**: Notice the colon `:` and the indentation!

## Simple Example

```python
age = 20

if age >= 18:
    print("You are an adult")
```

This will print "You are an adult" because 20 >= 18 is True.

## The Condition Can Be False

```python
age = 15

if age >= 18:
    print("You are an adult")

# Nothing prints because condition is False
```

## Indentation Matters!

```python
# Correct - indented code runs if condition is True
if age >= 18:
    print("You can vote")
    print("You are an adult")

# Wrong - IndentationError
if age >= 18:
print("You can vote")  # Missing indentation!
```

## Using Comparison Operators

```python
score = 85

if score >= 60:
    print("You passed!")

if score >= 90:
    print("Excellent work!")
```

## Using Logical Operators

```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive")
```

## What's Next?
In the main lesson, you'll learn:
- Detailed syntax rules
- Multiple statements in if blocks
- Common mistakes and how to avoid them
- Real-world applications
