# Editorials: Perform Arithmetic Operations

## Problem 1
```python
a = 25
b = 7

print(f"Sum: {a + b}")              # 32
print(f"Difference: {a - b}")       # 18
print(f"Product: {a * b}")          # 175
print(f"Quotient: {a / b}")         # 3.571...
print(f"Integer Div: {a // b}")     # 3
print(f"Remainder: {a % b}")        # 4
print(f"a squared: {a ** 2}")       # 625
```

## Problem 2
```python
price = 50
price += 20   # 70
price *= 2    # 140
price -= 10   # 130

print(price)  # 130
```

**Explanation**: Start at 50, add 20 (70), double it (140), subtract 10 (130)

## Problem 3
```python
bill = 85.00
tip_rate = 0.18
num_people = 4

tip = bill * tip_rate
total = bill + tip
per_person = total / num_people

print(f"Bill: ${bill:.2f}")
print(f"Tip (18%): ${tip:.2f}")           # $15.30
print(f"Total: ${total:.2f}")             # $100.30
print(f"Per person: ${per_person:.2f}")   # $25.08
```

## Problem 4
```python
hours = 2
minutes = 30
seconds = 45

total_seconds = (hours * 3600) + (minutes * 60) + seconds
print(f"Total: {total_seconds} seconds")  # 9045
```

**Breakdown**:
- 2 hours = 7200 seconds
- 30 minutes = 1800 seconds
- 45 seconds = 45 seconds
- Total = 9045 seconds

## Problem 5
```python
number = 456

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

print(f"Hundreds: {hundreds}, Tens: {tens}, Ones: {ones}")
# Output: Hundreds: 4, Tens: 5, Ones: 6
```

**Explanation**:
- `456 % 10 = 6` (ones place)
- `456 // 10 = 45`, then `45 % 10 = 5` (tens place)
- `456 // 100 = 4` (hundreds place)
