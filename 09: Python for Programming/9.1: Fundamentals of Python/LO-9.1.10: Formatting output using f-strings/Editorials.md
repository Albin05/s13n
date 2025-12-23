# Editorials: Format Output with F-strings

## Problem 1
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")
```

## Problem 2
```python
price = 29.99
quantity = 3
total = price * quantity
print(f"Total: ${total:.2f}")
```

## Problem 3
```python
import math
pi = math.pi
print(f"Pi: {pi:.3f}")  # 3.142
```

## Problem 4
```python
name = "Alice Johnson"
math_score = 95
english_score = 87
average = (math_score + english_score) / 2

print(f"Student: {name}")
print(f"Math: {math_score}")
print(f"English: {english_score}")
print(f"Average: {average:.1f}")
```

## Problem 5
```python
print(f"{'Name':<12} | {'Score':>5}")
print(f"{'-'*12}-|-{'-'*5}")
print(f"{'Alice':<12} | {95:>5}")
print(f"{'Bob':<12} | {87:>5}")
print(f"{'Charlie':<12} | {92:>5}")
```
