# Lecture Notes: Write Nested Conditionals

## Introduction

Nested conditionals create **decision trees** - multi-level logic where each branch can split further. This mirrors how humans make complex decisions with multiple factors.

### Why Nesting is Powerful

Real decisions are hierarchical:
- **Security system**: IF motion detected → THEN IF after hours → THEN IF not authorized → sound alarm
- **Email filter**: IF from known sender → THEN IF has attachment → THEN IF attachment type safe → allow

Each decision depends on previous ones - nesting models this perfectly.

### Real-World Analogy

Nested conditionals are like **nested boxes**:
- Open big box → IF it contains small box → open small box → IF it contains item → retrieve item

Or like **navigation instructions**:
- "IF you see the gas station, turn right. THEN IF you see the school, turn left. THEN IF you see the blue house, you've arrived."

## Nested Conditionals

A nested conditional is an if statement inside another if statement.


### Basic Syntax

```python
if condition1:
    if condition2:
        # Runs if both condition1 AND condition2 are True
    else:
        # Runs if condition1 is True but condition2 is False
else:
    # Runs if condition1 is False
```

## Why Use Nested Conditionals?

When you need to check a second condition **only if** the first one is True.

### Example 1: Age and License Check

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("Too young to drive")
```

### Example 2: Login System

```python
username = "admin"
password = "secret"

if username == "admin":
    if password == "secret":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")
```

## Multiple Levels of Nesting

```python
score = 85
submitted = True
on_time = True

if score >= 60:
    if submitted:
        if on_time:
            print("Full credit")
        else:
            print("Late penalty")
    else:
        print("Missing assignment")
else:
    print("Failed")
```

## Nested vs Logical Operators

These are equivalent:

```python
# Using nested if
if age >= 18:
    if has_license:
        print("Can drive")

# Using and operator
if age >= 18 and has_license:
    print("Can drive")
```

**When to use nested**: When you need different actions at each level

**When to use and**: When you just need to check multiple conditions

## Real-World Application: Discount Calculator

```python
total = 150
is_member = True
has_coupon = True

if total >= 100:
    discount = 10  # Base discount
    if is_member:
        discount += 5  # Member bonus
        if has_coupon:
            discount += 10  # Coupon bonus
    print(f"Total discount: {discount}%")
else:
    print("No discount (minimum $100)")
```

## Common Mistakes

### 1. Too Much Nesting

```python
# Avoid - too deep
if a:
    if b:
        if c:
            if d:
                if e:  # Hard to read!
                    print("Something")

# Better - use logical operators
if a and b and c and d and e:
    print("Something")
```

### 2. Forgetting Indentation

```python
# Wrong
if age >= 18:
if has_license:  # IndentationError
    print("Can drive")

# Correct
if age >= 18:
    if has_license:
        print("Can drive")
```

## Key Takeaways

1. **Nested if**: if inside another if
2. **Sequential checking**: Checks inner condition only if outer is True
3. **Use sparingly**: Too much nesting is hard to read
4. **Alternative**: Consider using logical operators (and, or)
5. **Indentation**: Each level needs proper indentation
