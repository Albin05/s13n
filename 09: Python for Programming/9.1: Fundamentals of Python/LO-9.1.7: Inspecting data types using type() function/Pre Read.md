# Pre-Read: Inspecting Data Types Using type()

## What is type()?

The `type()` function tells you **what kind of data** a variable contains.

```python
age = 25
print(type(age))  # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>

price = 19.99
print(type(price))  # <class 'float'>
```

## Why Do We Need type()?

In Python, you don't have to declare types:
```python
x = 5  # Python automatically knows it's an int
```

But sometimes you need to **check** what type something is, especially when debugging:
```python
result = some_function()
print(type(result))  # "What did this function return?"
```

### Simple Analogy

Think of `type()` like asking **"What is this?"**

- You find a container in the fridge
- You ask: "Is this milk or juice?"
- `type()` tells you: "This is milk!"

Similarly, with variables:
- You have a variable `x`
- You ask: `type(x)`
- Python tells you: "This is an int!"

## Why Types Can Be Confusing

Consider this surprise:
```python
age = "25"  # Looks like a number, but it's a string!
print(type(age))  # <class 'str'>

result = age + 5  # ❌ Error! Can't add string and int
```

The `type()` function helps you spot these issues:
- `"25"` is text (string)
- `25` is a number (int)
- They look similar but behave differently!

## Python's Flexibility

Unlike some languages, Python lets variables **change types**:
```python
x = 5          # x is an int
print(type(x))  # <class 'int'>

x = "hello"     # Now x is a string!
print(type(x))  # <class 'str'>
```

This flexibility is powerful but can lead to bugs. The `type()` function helps you keep track.

## Try Before Class

```python
a = 10
b = 10.0
c = "10"

print(type(a))  # What will this show?
print(type(b))  # What about this?
print(type(c))  # And this?
```

**Hint**: They all look similar, but have different types!

## Key Points
- `type()` reveals what kind of data a variable holds
- Essential for debugging type errors
- Python variables can change types
- Use `type()` when unsure what you're working with
