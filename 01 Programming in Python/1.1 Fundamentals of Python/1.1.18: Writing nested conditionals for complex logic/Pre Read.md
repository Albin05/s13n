# Pre-Read: Writing Nested Conditionals

## What You'll Learn
In this lesson, you'll learn how to write if statements inside other if statements (nested conditionals) to handle complex decision-making logic.

## Why This Matters
Real-world programs often need to make decisions based on multiple conditions that depend on each other. For example:
- A login system checks if the username exists, then checks if the password matches
- An online store checks if you have enough money, then checks if the item is in stock
- A game checks if you pressed a key, then checks which key it was

Nested conditionals let you create these layered decision trees.

---

## What are Nested Conditionals?

A **nested conditional** is simply an if statement placed inside another if statement. Think of it like a decision tree where you only check some conditions if previous conditions are met.

```python
if outer_condition:
    if inner_condition:
        # Runs only if BOTH conditions are True
```

## Simple Example

Imagine you're checking if someone can drive:

```python
age = 20
has_license = True

if age >= 18:
    print("You're old enough")
    if has_license:
        print("You can drive!")
    else:
        print("You need to get a license first")
else:
    print("You're too young to drive")
```

**How it works:**
1. First, check if age >= 18
2. **Only if** that's True, then check if they have a license
3. If age < 18, we never check the license (because it doesn't matter)

---

## When to Use Nested Conditionals

Use nested conditionals when:
- The second condition only makes sense if the first is True
- You need different messages or actions at each level
- Conditions depend on each other sequentially

**Example: File Upload System**

```python
file_size = 2.5  # in MB
file_format = "jpg"

if file_size <= 5:
    if file_format in ["jpg", "png", "gif"]:
        print("Upload successful!")
    else:
        print("Invalid format. Use JPG, PNG, or GIF")
else:
    print("File too large. Maximum 5MB")
```

---

## Nested Conditionals vs Logical Operators

Sometimes you can use nested conditionals OR logical operators (`and`). They're not always the same!

### When They're Equivalent

```python
# Using nested if
if age >= 18:
    if has_license:
        print("Can drive")

# Using and operator
if age >= 18 and has_license:
    print("Can drive")
```

### When Nested Is Better

When you need different actions at each level:

```python
# Nested allows different messages
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("Get a license first")
else:
    print("Wait until you're 18")

# With 'and', you only get one message
if age >= 18 and has_license:
    print("You can drive")
else:
    print("You can't drive")  # Why? We don't know!
```

---

## Visual Example: Login System

```python
username = "alice"
password = "secret123"

if username == "alice":
    print("Username found")
    if password == "secret123":
        print("Login successful!")
        print("Welcome to your account")
    else:
        print("Wrong password")
else:
    print("Username not found")
```

**Decision tree:**
```
Is username correct?
├─ NO → "Username not found"
└─ YES → "Username found"
    │
    Is password correct?
    ├─ NO → "Wrong password"
    └─ YES → "Login successful!"
```

---

## Be Careful with Indentation!

Python uses indentation to show which code belongs to which if statement:

```python
# Correct
if condition1:
    if condition2:      # Inside first if
        print("Both True")

# Wrong - IndentationError
if condition1:
if condition2:          # Not indented - Python doesn't know this is nested
    print("Both True")
```

---

## Try It Yourself (Before Class)

Run this code and see what happens:

```python
score = 75
bonus_completed = True

if score >= 60:
    print("You passed!")
    if bonus_completed:
        print("Bonus points added!")
        score = score + 10
        print(f"New score: {score}")
    else:
        print("No bonus")
else:
    print("You need to score at least 60")

print(f"Final score: {score}")
```

**Try changing:**
- `score` to 50 - what happens?
- `bonus_completed` to False - what happens?
- Both values - can you predict the output?

---

## Key Takeaways

Before class, remember:
1. **Nested if = if inside if** - for layered decision-making
2. **Inner code runs only if outer condition is True** - sequential checking
3. **Indentation matters** - shows which if contains which code
4. **Use for dependent conditions** - when second check only makes sense if first is True
5. **Alternative exists** - sometimes `and` operator is simpler

## Questions to Think About

Come to class ready to discuss:
- When would you use nested conditionals instead of `and`/`or` operators?
- Can you have an if nested inside an else block?
- How many levels deep can you nest conditionals? Should you?

## What's Next?

In the live session, we'll:
- Write complex nested conditional structures
- Learn when to use nesting vs logical operators
- Avoid common mistakes like too-deep nesting
- Build programs with multiple decision levels
- Practice debugging nested conditionals

See you in class!
