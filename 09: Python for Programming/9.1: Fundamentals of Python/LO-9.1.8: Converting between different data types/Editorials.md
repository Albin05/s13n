# Editorials: Convert Between Data Types

## Problem 1
```python
int("100")   # 100
str(25)      # "25"
int(3.14)    # 3
```

## Problem 2
```python
age = input("Age: ")
age_int = int(age)  # Convert first!
next_year = age_int + 1
```

## Problem 3
```python
num1 = input("First: ")
num2 = input("Second: ")
sum_result = int(num1) + int(num2)
print(sum_result)
```

## Problem 4
```python
celsius_str = input("Celsius: ")
celsius = float(celsius_str)
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

## Problem 5
```python
print(int(3.9))      # 3 (truncates)
print(int("10"))     # 10
print(bool(0))       # False
print(bool(""))      # False
print(str(True))     # "True"
```
