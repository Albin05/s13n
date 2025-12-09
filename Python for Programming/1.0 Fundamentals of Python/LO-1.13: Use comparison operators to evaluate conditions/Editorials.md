# Editorials: Use Comparison Operators

## Problem 1
```python
age = int(input("Enter your age: "))
can_vote = age >= 18
print(f"Can vote: {can_vote}")
```

### Explanation
- Get age as integer input
- Use `>=` to check if 18 or older
- Store boolean result in `can_vote`
- Print the result

## Problem 2
```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")
```

### Explanation
- Get two numbers from user
- Perform all six comparisons
- Use f-strings to display each comparison and its result
- Each comparison returns True or False

## Problem 3
```python
score = int(input("Enter your score: "))

failed = score < 60
passed = score >= 60
excellent = score >= 90

print(f"Failed: {failed}")
print(f"Passed: {passed}")
print(f"Excellent: {excellent}")
```

### Explanation
- Store score from user
- Create three boolean variables:
  - `failed`: score less than 60
  - `passed`: score 60 or higher
  - `excellent`: score 90 or higher
- Print all three results

## Problem 4
```python
password = input("Enter password: ")
length = len(password)

minimum_strength = length >= 8
strong = length >= 12

print(f"Minimum strength (8+ chars): {minimum_strength}")
print(f"Strong (12+ chars): {strong}")
```

### Explanation
- Get password string from user
- Calculate length using `len()`
- Check if length meets minimum (8 chars)
- Check if length is strong (12 chars)
- Print both results

## Problem 5
```python
temp = float(input("Enter temperature in Celsius: "))

is_freezing = temp <= 0
is_cold = temp < 15
is_comfortable = temp >= 15 and temp <= 25
is_hot = temp > 25
is_very_hot = temp >= 35

print(f"Freezing: {is_freezing}")
print(f"Cold: {is_cold}")
print(f"Comfortable: {is_comfortable}")
print(f"Hot: {is_hot}")
print(f"Very hot: {is_very_hot}")
```

### Explanation
- Get temperature as float (can have decimals)
- Create five boolean variables with different conditions:
  - `is_freezing`: 0 or below
  - `is_cold`: below 15
  - `is_comfortable`: between 15 and 25 (uses `and` - will learn more in next LO!)
  - `is_hot`: above 25
  - `is_very_hot`: 35 or above
- Print all results

**Note**: The `and` keyword used in `is_comfortable` combines two conditions. This is a preview of logical operators (next lesson)!

### Alternative Solution (without `and`)
```python
temp = float(input("Enter temperature in Celsius: "))

is_freezing = temp <= 0
is_cold = temp < 15
is_warm_enough = temp >= 15
is_not_too_hot = temp <= 25
is_comfortable = is_warm_enough and is_not_too_hot  # Combine two booleans
is_hot = temp > 25
is_very_hot = temp >= 35

print(f"Freezing: {is_freezing}")
print(f"Cold: {is_cold}")
print(f"Comfortable: {is_comfortable}")
print(f"Hot: {is_hot}")
print(f"Very hot: {is_very_hot}")
```
