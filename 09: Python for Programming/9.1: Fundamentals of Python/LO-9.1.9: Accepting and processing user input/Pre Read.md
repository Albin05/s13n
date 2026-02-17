# Pre-Read: Accept User Input

## The input() Function

Makes programs interactive!

```python
name = input("What's your name? ")
print("Hello, " + name + "!")
```

### What Makes Programs Useful?

Think about the apps you use:
- **Calculator**: Takes YOUR numbers, not fixed numbers
- **Google**: Searches for YOUR query
- **Games**: Respond to YOUR actions
- **Chat apps**: Send YOUR messages

Without input, programs would be like movies - you just watch. With input, they're like video games - you participate!

### Simple Analogy

**Without input():**
```python
print("Hello Alice!")  # Always greets Alice
```
Like a recording: "Hello Alice!" plays the same way every time.

**With input():**
```python
name = input("Your name: ")
print("Hello " + name + "!")  # Greets anyone!
```
Like a live conversation: "What's your name?" → You answer → "Hello [your name]!"

### Why This Matters

Before input, all your variables had fixed values:
```python
age = 25  # Hard-coded
score = 100  # Fixed
name = "Alice"  # Same every run
```

With input, your programs work with ANY data:
```python
age = int(input("Your age: "))  # Different each time!
```

This is the difference between a **demo** and a **real application**.

## Important: input() Returns String

```python
age = input("Age: ")  # User types: 25
print(type(age))      # <class 'str'>  "25", not 25!
```

Must convert for math:
```python
age = input("Age: ")
age_int = int(age)
next_year = age_int + 1
```

## Example: Interactive Calculator
```python
num1 = input("First number: ")
num2 = input("Second number: ")
sum_result = int(num1) + int(num2)
print("Sum:", sum_result)
```

## Try It
```python
name = input("Your name: ")
age = input("Your age: ")
print(f"Hello {name}, you are {age} years old!")
```
