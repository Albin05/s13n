# Lecture Notes: Convert Between Data Types

## Type Conversion Functions

### int() - Convert to Integer
```python
int("25")       # 25 (string to int)
int(25.9)       # 25 (float to int - truncates)
int(True)       # 1
int(False)      # 0
# int("25.5")   # Error - can't convert decimal string
```


### float() - Convert to Float
```python
float("3.14")   # 3.14
float(5)        # 5.0
float("5")      # 5.0
float(True)     # 1.0
```

### str() - Convert to String
```python
str(25)         # "25"
str(3.14)       # "3.14"
str(True)       # "True"
str(False)      # "False"
```

### bool() - Convert to Boolean
```python
bool(1)         # True (non-zero = True)
bool(0)         # False (zero = False)
bool("text")    # True (non-empty = True)
bool("")        # False (empty = False)
bool([1,2,3])   # True (non-empty = True)
```

## Common Use Cases

### User Input
```python
age_str = input("Enter age: ")  # Returns string
age = int(age_str)               # Convert to int
next_year = age + 1              # Now can do math
```

### String Concatenation
```python
score = 95
message = "Score: " + str(score)  # Convert int to str
print(message)  # "Score: 95"
```

### Calculation Display
```python
result = 10 / 3
print("Result: " + str(result))  # Convert float to str
```

## Key Takeaways
1. Use `int()`, `float()`, `str()`, `bool()` to convert
2. User input always needs conversion
3. Can't concatenate str and numbers without conversion
4. Some conversions may raise errors
5. Know conversion rules for each type
