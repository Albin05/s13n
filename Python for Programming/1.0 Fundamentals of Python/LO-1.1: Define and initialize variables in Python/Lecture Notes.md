# Lecture Notes: Define Variables

## Introduction
Variables are the fundamental building blocks of programming. They allow programs to store, retrieve, and manipulate data. In this lesson, you'll learn how to create and use variables in Python.

---

## What are Variables?

### Definition
A **variable** is a named location in computer memory that stores a value. Think of it as a labeled container where you can put data and retrieve it later.

### Real-World Analogy
Imagine your locker at school:
- The **locker number** is like the variable name
- The **contents inside** are like the value
- You can **change what's inside** anytime

### The Assignment Operator (=)

In Python, we create variables using the `=` operator:

```python
age = 25
```

**Important**: Read this as "age is assigned 25" or "25 is assigned to age"
- The `=` is **assignment**, not mathematical equality
- Variable name goes on the **left**
- Value goes on the **right**

---

---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---

## Creating Variables

### Basic Syntax

```python
variable_name = value
```

### Examples

```python
score = 100
name = "Alice"
price = 19.99
is_active = True
```

### What Happens in Memory

When you write `score = 100`:
1. Python allocates memory space
2. Stores the value `100` in that space
3. Creates a label `score` pointing to that memory location

```
Memory:  [100]
         
Label:   score
```

---

## Variable Reassignment

Variables can be changed - they're called "variables" because their values can **vary**!

### Example

```python
health = 100
print(health)  # Output: 100

health = 75    # Player took damage
print(health)  # Output: 75

health = 100   # Player healed
print(health)  # Output: 100
```

### What Happens to the Old Value?

When you reassign a variable, the old value is **discarded**:

```python
x = 5
x = 10  # The value 5 is gone, x now refers to 10
```

---

## Multiple Variables

You can create many variables in a program:

```python
# Game character
player_name = "DragonSlayer"
health = 100
mana = 50
level = 5
is_alive = True

print(player_name)  # DragonSlayer
print(health)       # 100
print(level)        # 5
```

### Multiple Assignment

Python allows creating multiple variables in one line:

```python
# Create three variables at once
x, y, z = 10, 20, 30

print(x)  # 10
print(y)  # 20
print(z)  # 30
```

### Same Value to Multiple Variables

```python
# All three variables get the same value
a = b = c = 0

print(a)  # 0
print(b)  # 0
print(c)  # 0
```

---

## Using Variables

Once created, you can use variables in your code:

### In Calculations

```python
price = 100
quantity = 3
total = price * quantity
print(total)  # 300
```

### In Strings (Preview)

```python
name = "Alice"
print("Hello, " + name)  # Hello, Alice
```

### Updating Variables Based on Current Value

```python
score = 100
score = score + 50  # Add 50 to current score
print(score)  # 150
```

**Shorthand** (you'll learn more later):
```python
score = 100
score += 50  # Same as: score = score + 50
print(score)  # 150
```

---

## Assignment vs. Equality

This is a common source of confusion for beginners!

### Assignment (=)

**Creates or changes** a variable:
```python
age = 25  # Assigns 25 to age
```

### Equality (==)

**Compares** two values (you'll learn this in LO-13):
```python
age == 25  # Checks if age equals 25 (True or False)
```

### Example

```python
x = 10      # Assignment: x gets value 10
x == 10     # Comparison: Is x equal to 10? (True)
x == 5      # Comparison: Is x equal to 5? (False)
```

---

## Practical Examples

### Example 1: Simple Calculator

```python
num1 = 15
num2 = 7

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

print(sum_result)    # 22
print(difference)    # 8
print(product)       # 105
```

### Example 2: Shopping Cart

```python
item_price = 29.99
quantity = 2
tax_rate = 0.08

subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Subtotal:", subtotal)  # 59.98
print("Tax:", tax)            # 4.7984
print("Total:", total)        # 64.7784
```

### Example 3: Game Score Tracker

```python
player_score = 0
print("Starting score:", player_score)  # 0

# Player completes level 1
player_score = player_score + 100
print("After level 1:", player_score)   # 100

# Player completes level 2
player_score = player_score + 150
print("After level 2:", player_score)   # 250

# Player loses points
player_score = player_score - 50
print("Final score:", player_score)     # 200
```

---

## Common Mistakes and How to Fix Them

### Mistake 1: Trying to Use Before Creating

```python
print(name)  # L NameError: name 'name' is not defined
```

**Fix**: Create the variable first
```python
name = "Alice"
print(name)  #  Alice
```

### Mistake 2: Confusing Assignment Direction

```python
25 = age  # L SyntaxError: cannot assign to literal
```

**Fix**: Variable name goes on the left
```python
age = 25  #  Correct
```

### Mistake 3: Using Quotes for Variable Names

```python
"score" = 100  # L SyntaxError
```

**Fix**: No quotes around variable names
```python
score = 100  #  Correct
```

---

## The print() Function

You've seen `print()` in examples. It displays values:

```python
age = 25
print(age)        # Shows: 25
print("Hello")    # Shows: Hello

# Multiple values
name = "Bob"
age = 30
print(name, age)  # Shows: Bob 30
```

---

## Key Takeaways

1. **Variables store data** - they're like labeled containers in memory
2. **Use `=` to assign values** - variable_name = value
3. **Variables can be reassigned** - their values can change
4. **Create before using** - must define a variable before referencing it
5. **`=` means assign, not equals** - don't confuse with mathematical equality

---

## Practice Exercise

Create a program that tracks a bank account:

```python
# Starting balance
account_balance = 1000
print("Starting balance:", account_balance)

# Deposit money
account_balance = account_balance + 500
print("After deposit:", account_balance)

# Withdraw money
account_balance = account_balance - 200
print("After withdrawal:", account_balance)

# Expected output:
# Starting balance: 1000
# After deposit: 1500
# After withdrawal: 1300
```

---

## What's Next?

In **LO-2: Apply Variable Naming Conventions**, you'll learn:
- Rules for valid variable names
- Python naming conventions (snake_case)
- Reserved keywords to avoid
- Best practices for naming variables
