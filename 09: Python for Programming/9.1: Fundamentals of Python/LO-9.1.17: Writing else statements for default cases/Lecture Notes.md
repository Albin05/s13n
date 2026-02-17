# Lecture Notes: Write Else Statements

## Introduction

The `else` statement provides a **catch-all** for when all other conditions fail. It represents "everything else" or "the default case" - ensuring your program always has a response.

### Why Else is Essential

Real decisions need a default:
- **ATM**: IF PIN correct, proceed; ELSE reject
- **Login**: IF credentials match, login; ELSE show error
- **Game**: IF answer correct, award points; ELSE try again

Without else, programs would silently do nothing when conditions fail - confusing for users!

### Real-World Analogy

Else is like a **catch-all bin**:
- Sort laundry: IF white → bin 1, IF colors → bin 2, ELSE (mixed/unknown) → bin 3
- Customer service: IF billing → dept A, IF tech → dept B, ELSE → general support

Or like **"otherwise" in instructions**:
- Recipe: "IF dough is too wet, add flour; OTHERWISE continue to next step"

## Else Statements

The `else` statement provides a **default action** when all previous conditions in an if-elif chain are False.


### Basic Syntax

```python
if condition:
    # Runs if condition is True
else:
    # Runs if condition is False
```

With elif:

```python
if condition1:
    # Code
elif condition2:
    # Code
else:
    # Runs if ALL above conditions are False
```

**Key Points**:
1. No condition needed (no `else score > 50:`)
2. Always comes last
3. Optional - not required
4. Catches all remaining cases

## Simple Examples

### Example 1: Binary Choice

```python
age = 16

if age >= 18:
    print("Can vote")
else:
    print("Cannot vote yet")

# Output: Cannot vote yet
```

### Example 2: Complete Grade System

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")  # Grade: C
```

### Example 3: Number Classification

```python
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Output: Negative
```

## When to Use Else

### Use Else When:
- You want a default action for unmatched cases
- You need to handle "everything else"
- Two possible paths (if-else)

### Skip Else When:
- Not all cases need handling
- You only care about specific conditions

```python
# With else
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Without else (also valid)
age = 15
if age >= 18:
    print("Adult")
# Nothing prints if age < 18
```

## Real-World Applications

### Login Validation

```python
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Login successful")
else:
    print("Invalid credentials")
```

### Ticket Pricing

```python
age = 8

if age >= 65:
    price = 8
elif age >= 18:
    price = 12
elif age >= 5:
    price = 6
else:
    price = 0  # Free for under 5

print(f"Ticket price: ${price}")
```

## Common Mistakes

### 1. Condition in Else

```python
# Wrong
if score >= 60:
    print("Pass")
else score < 60:  # SyntaxError
    print("Fail")

# Correct
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

### 2. Else Before Elif

```python
# Wrong
if score >= 90:
    print("A")
else:
    print("Not A")
elif score >= 80:  # SyntaxError
    print("B")

# Correct
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Below B")
```

## Key Takeaways

1. **No condition**: else doesn't check anything
2. **Always last**: Must come after if/elif
3. **Default handler**: Catches all unmatched cases
4. **Optional**: Not always needed
5. **One else max**: Only one else per if-elif chain
