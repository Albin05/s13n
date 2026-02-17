# Pre-Read: Format Output with F-strings

## What are F-strings?

**F-strings** make it easy to embed variables in strings!

### Old Way (Concatenation)
```python
name = "Alice"
age = 25
message = "My name is " + name + " and I am " + str(age)
```

### New Way (F-strings) ✨
```python
name = "Alice"
age = 25
message = f"My name is {name} and I am {age}"
```

Much cleaner!

### The Problem F-strings Solve

Without f-strings, combining text and variables is painful:
```python
name = "Bob"
score = 95
level = 10

# Concatenation - lots of + and str()
msg = "Player " + name + " scored " + str(score) + " at level " + str(level)
# 😩 Hard to read! Easy to mess up!
```

With f-strings, it's natural:
```python
msg = f"Player {name} scored {score} at level {level}"
# 😊 Clean and obvious!
```

### Simple Analogy

Think of f-strings like **filling in blanks**:
- You write a sentence with blanks: "My name is _____ and I'm _____ years old"
- Python fills them in: "My name is Alice and I'm 25 years old"

Or think of them like **customizable t-shirts**:
- Template: "I ❤️ {city}"
- For you: "I ❤️ New York"
- For me: "I ❤️ Boston"
- Same template, different data!

### Why "F" String?

The `f` stands for **"formatted"** - it tells Python: "This string has special formatting with `{}` placeholders."

Without `f`:
```python
name = "Alice"
print("Hello {name}")  # Prints: Hello {name} (literal)
```

With `f`:
```python
name = "Alice"
print(f"Hello {name}")  # Prints: Hello Alice (filled in!)
```

That little `f` makes all the difference!

## F-string Syntax

Put `f` before the string, use `{}` for variables:

```python
score = 95
print(f"You scored {score} points!")
```

## Expressions in F-strings

Can do calculations inside `{}`:

```python
price = 50
quantity = 3
print(f"Total: ${price * quantity}")  # Total: $150
```

## Formatting Numbers

```python
pi = 3.14159265
print(f"Pi is approximately {pi:.2f}")  # Pi is approximately 3.14
```

`.2f` means: 2 decimal places, float

## Try It
```python
name = "Bob"
age = 30
city = "Boston"
print(f"{name} is {age} years old and lives in {city}")
```
