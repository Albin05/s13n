# Lecture Notes: Accept User Input

## The input() Function

### Basic Syntax
```python
variable = input("Prompt message: ")
```


### Example
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

**When run:**
```
Enter your name: Alice
Hello, Alice!
```

## Input Always Returns String

```python
age = input("Enter age: ")
print(type(age))  # <class 'str'>
```

Even if user types a number, it's stored as string!

### Convert for Math
```python
age_str = input("Enter age: ")
age = int(age_str)
next_year = age + 1
print("Next year you'll be", next_year)
```

## Multiple Inputs
```python
first = input("First name: ")
last = input("Last name: ")
age = int(input("Age: "))  # Convert immediately

print(f"{first} {last}, age {age}")
```

## Practical Examples

### Calculator
```python
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
result = num1 + num2
print("Sum:", result)
```

### Profile Creator
```python
name = input("Name: ")
city = input("City: ")
age = int(input("Age: "))

print(f"{name} from {city}, age {age}")
```

## Key Takeaways
1. `input()` creates interactive programs
2. Always returns string
3. Convert to appropriate type for operations
4. Use clear prompts
5. Can convert inline: `int(input("Age: "))`
