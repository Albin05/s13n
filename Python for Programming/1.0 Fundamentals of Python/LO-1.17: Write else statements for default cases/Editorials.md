# Editorials: Write Else Statements

## Problem 1
```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Explanation
- Use modulo to check divisibility by 2
- If remainder is 0, it's even
- else handles all odd numbers

## Problem 2
```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    years_to_wait = 18 - age
    print(f"You cannot vote yet. Wait {years_to_wait} years")
```

### Explanation
- Check voting age (18)
- If not eligible, calculate years remaining
- else provides feedback with calculation

## Problem 3
```python
score = int(input("Enter score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

if score >= 60:
    print("Result: Passed")
else:
    print("Result: Failed")
```

### Explanation
- Complete if-elif-else chain for grades
- else catches failing scores (< 60)
- Separate if-else for pass/fail status

## Problem 4
```python
weight = float(input("Enter package weight (kg): "))

if weight <= 1:
    cost = 5
elif weight <= 5:
    cost = 10
elif weight <= 10:
    cost = 15
else:
    cost = 25

print(f"Shipping cost: ${cost}")
```

### Explanation
- Check weight brackets in order
- else handles heavy packages (> 10kg)
- Simple and clear pricing logic

## Problem 5
```python
balance = 500
amount = int(input("Enter amount: "))

print(f"Balance: ${balance}")

if amount <= 0:
    print("Invalid amount")
else:
    if amount > balance:
        print("Insufficient funds")
    else:
        if amount % 10 != 0:
            print("Amount must be multiple of 10")
        else:
            balance = balance - amount
            print("Withdrawal successful")
            print(f"New balance: ${balance}")
```

### Explanation
- Nested if-else statements check conditions sequentially
- First check: amount must be positive
- Second check: sufficient balance
- Third check: multiple of 10
- else: all checks passed, process withdrawal
- Each else narrows down to valid transaction
