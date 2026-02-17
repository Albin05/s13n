### LO-18 Write Nested Conditionals (25 minutes)


### CS Theory Bite

> **Origin**: Nested conditionals increase **cyclomatic complexity** (Thomas McCabe, 1976) — a measure of code complexity. High nesting depth signals code that's hard to test and maintain.
>
> **Analogy**: Nested ifs are like **Russian nesting dolls** — decisions inside decisions. Too many layers become hard to follow.
>
> **Why it matters**: Sometimes complex logic requires nesting, but prefer flattening with `elif` or early returns when possible.


### Hook (3 minutes)

**Say**: "To drive, you need: age 18+ AND a license AND a car. That's checking conditions INSIDE conditions - nested logic!"

```python
age = 25
has_license = True
has_car = True

if age >= 18:
    if has_license:
        if has_car:
            print("You can drive!")
        else:
            print("You need a car")
    else:
        print("You need a license")
else:
    print("Too young to drive")
```

### Basic Nested Conditionals (6 minutes)

**Say**: "Nested means putting one if statement INSIDE another. Each level adds more detail."

```python
temperature = 85
is_sunny = True

if temperature > 80:
    print("It's hot!")
    if is_sunny:
        print("And it's sunny - perfect beach weather!")
    else:
        print("But it's cloudy")
else:
    print("Not too hot today")
```

**Key Points**:
- Inner if only runs if outer if is True
- Each level needs proper indentation
- Each if block can have its own elif/else

### Decision Trees (6 minutes)

**Say**: "Nested conditionals create decision trees - each branch leads to more decisions."

```python
age = 25

if age >= 0:
    if age < 13:
        category = "Child"
    elif age < 20:
        category = "Teenager"
    elif age < 60:
        category = "Adult"
    else:
        category = "Senior"
    print(f"Category: {category}")
else:
    print("Invalid age")
```

**Real-World**: Discount calculator
```python
price = 100
is_member = True
is_sale = True

if is_member:
    if is_sale:
        discount = 0.30  # Member + Sale
    else:
        discount = 0.10  # Member only
else:
    if is_sale:
        discount = 0.15  # Sale only
    else:
        discount = 0  # No discount

final_price = price * (1 - discount)
print(f"Price: ${final_price}")
```

### Avoiding Deep Nesting (5 minutes)

**Say**: "More than 2-3 levels? Too complex! Use 'and' instead."

```python
# TOO DEEP - hard to read!
if condition1:
    if condition2:
        if condition3:
            if condition4:
                print("All conditions met")

# BETTER - use 'and'
if condition1 and condition2 and condition3 and condition4:
    print("All conditions met")
```

**When to nest**: When the inner logic DEPENDS on the outer condition
```python
# Good nesting - inner logic depends on outer
if has_account:
    if balance > 100:
        print("Can withdraw")
    else:
        print("Insufficient funds")
else:
    print("Please create account")
```

### Practice (3 minutes)

Calculate tip based on bill and service:
```python
bill = 75
service = "excellent"

if bill > 50:
    if service == "excellent":
        tip_percent = 0.20
    else:
        tip_percent = 0.15
else:
    if service == "excellent":
        tip_percent = 0.15
    else:
        tip_percent = 0.10

tip = bill * tip_percent
print(f"Tip: ${tip}")
```

### Wrap-up (2 minutes)

**Key Takeaways**:
- Nest when inner conditions depend on outer ones
- Keep nesting shallow (2-3 levels max)
- Use `and`/`or` for independent conditions
- Proper indentation is critical!
