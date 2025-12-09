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
