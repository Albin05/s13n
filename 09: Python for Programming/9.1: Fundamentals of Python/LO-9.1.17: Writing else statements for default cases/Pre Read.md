# Pre-Read: Write Else Statements

## What is Else?

`else` handles "everything else" - what happens when all other conditions are False.

### Simple Analogy

Think of else like **"Plan B"**:
- IF it's sunny, go to beach; ELSE stay home and watch movies
- IF have cash, pay with cash; ELSE use credit card
- IF item in stock, ship it; ELSE send backorder notice

It's your fallback option!

## What You'll Learn
In this lesson, you'll learn how to use else statements to handle cases when all previous conditions are False.

## The Else Statement

`else` provides a **default action** when no previous conditions match:

```python
age = 10

if age >= 18:
    print("Adult ticket")
elif age >= 13:
    print("Teen ticket")
else:
    print("Child ticket")  # Runs for ages < 13

# Output: Child ticket
```

## Key Characteristics

1. **No Condition**: else doesn't check anything - it runs when all above conditions are False
2. **Must Be Last**: else always comes at the end
3. **Catches Everything Else**: Handles all remaining cases

## Syntax

```python
if condition1:
    # Code if condition1 is True
elif condition2:
    # Code if condition2 is True
else:
    # Code if ALL above are False
```

## Examples

### Example 1: Pass/Fail

```python
score = 55

if score >= 60:
    print("Pass")
else:
    print("Fail")  # Runs for score < 60
```

### Example 2: Complete Grade System

```python
score = 45

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")  # Handles everything below 60

# Output: F
```

## What's Next?
In the main lesson, you'll learn:
- Detailed else syntax
- When to use else vs explicit conditions
- Complete if-elif-else patterns
- Real-world applications
