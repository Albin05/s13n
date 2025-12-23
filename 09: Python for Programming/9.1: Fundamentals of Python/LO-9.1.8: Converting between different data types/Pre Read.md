# Pre-Read: Convert Between Data Types

## Why Convert Types?

User input is always a string - need to convert for math!

```python
age = input("Age: ")  # Returns string "25"
# age + 5  # Error - can't add string and int
age_int = int(age)    # Convert to int
next_year = age_int + 1  # Works!
```

## Conversion Functions

### To Integer
```python
int("25")      # 25
int(25.9)      # 25 (truncates)
int(True)      # 1
```

### To Float
```python
float("3.14")  # 3.14
float(5)       # 5.0
```

### To String
```python
str(25)        # "25"
str(3.14)      # "3.14"
str(True)      # "True"
```

### To Boolean
```python
bool(1)        # True
bool(0)        # False
bool("text")   # True
bool("")       # False
```

## Try It
```python
age_str = "25"
age_int = int(age_str)
age_float = float(age_int)
print(type(age_float))  # <class 'float'>
```
