# Editorials: Write Elif Statements

## Problem 1
```python
chest = int(input("Enter chest measurement (inches): "))

if chest >= 42:
    print("Size: XL")
elif chest >= 38:
    print("Size: L")
elif chest >= 34:
    print("Size: M")
elif chest >= 30:
    print("Size: S")
else:
    print("Size: XS")
```

### Explanation
- Check from largest to smallest size
- Each elif checks next smaller size
- else catches anything under 30 inches
- Only one size prints

## Problem 2
```python
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### Explanation
- Three mutually exclusive categories
- if checks positive, elif checks negative
- else handles the only remaining case: zero
- Simple and clear logic flow

## Problem 3
```python
speed_limit = int(input("Enter speed limit: "))
speed = int(input("Enter your speed: "))

if speed <= speed_limit:
    print("No fine")
elif speed <= speed_limit + 10:
    print("Warning")
elif speed <= speed_limit + 20:
    print("Fine: $50")
elif speed <= speed_limit + 30:
    print("Fine: $100")
else:
    print("Fine: $200 and court appearance")
```

### Explanation
- Check in order from no violation to severe
- Each elif adds 10 mph to the threshold
- else catches extreme speeding (30+ over limit)
- Order is crucial for correct categorization

## Problem 4
```python
score = int(input("Enter score (0-100): "))

if score >= 97:
    print("A+")
elif score >= 93:
    print("A")
elif score >= 90:
    print("A-")
elif score >= 87:
    print("B+")
elif score >= 83:
    print("B")
elif score >= 80:
    print("B-")
elif score >= 77:
    print("C+")
elif score >= 73:
    print("C")
elif score >= 70:
    print("C-")
elif score >= 60:
    print("D")
else:
    print("F")
```

### Explanation
- Check from highest grade to lowest
- Each threshold is carefully ordered
- First True condition wins
- else handles failing grades (below 60)

## Problem 5
```python
income = float(input("Enter annual income: "))

if income <= 10000:
    tax_rate = 0
    bracket = "0%"
elif income <= 40000:
    tax_rate = 0.10
    bracket = "10%"
elif income <= 85000:
    tax_rate = 0.20
    bracket = "20%"
elif income <= 160000:
    tax_rate = 0.30
    bracket = "30%"
else:
    tax_rate = 0.40
    bracket = "40%"

tax_amount = income * tax_rate

print(f"Tax bracket: {bracket}")
print(f"Tax amount: ${tax_amount:.2f}")
```

### Explanation
- Check income brackets from lowest to highest
- Store both tax rate and bracket name
- Calculate tax after determining bracket
- Use f-string with :.2f for currency formatting
- Each elif represents a different tax bracket

### Alternative Solution (More Detailed)
```python
income = float(input("Enter annual income: "))

if income <= 10000:
    tax_rate = 0.0
    tax_amount = income * tax_rate
    print("Tax bracket: 0%")
elif income <= 40000:
    tax_rate = 0.10
    tax_amount = income * tax_rate
    print("Tax bracket: 10%")
elif income <= 85000:
    tax_rate = 0.20
    tax_amount = income * tax_rate
    print("Tax bracket: 20%")
elif income <= 160000:
    tax_rate = 0.30
    tax_amount = income * tax_rate
    print("Tax bracket: 30%")
else:
    tax_rate = 0.40
    tax_amount = income * tax_rate
    print("Tax bracket: 40%")

print(f"Tax amount: ${tax_amount:.2f}")
```
