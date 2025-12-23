# Pre-Read: Accept User Input

## The input() Function

Makes programs interactive!

```python
name = input("What's your name? ")
print("Hello, " + name + "!")
```

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
