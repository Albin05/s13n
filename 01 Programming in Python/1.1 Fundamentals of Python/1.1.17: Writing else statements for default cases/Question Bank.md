# Question Bank: Write Else Statements

## Problem 1 (Easy)
Write a program that checks if a number is even or odd:
- If divisible by 2: "Even"
- Else: "Odd"

Example:
```
Enter a number: 7
Odd
```

## Problem 2 (Easy)
Write a program that checks voting eligibility:
- If age >= 18: "You can vote"
- Else: "You cannot vote yet. Wait X years" (calculate X)

Example:
```
Enter your age: 16
You cannot vote yet. Wait 2 years
```

## Problem 3 (Medium)
Write a complete grade calculator with if-elif-else:
- >= 90: A
- >= 80: B
- >= 70: C
- >= 60: D
- Else: F

Also print whether they passed (>= 60) or failed.

Example:
```
Enter score: 55
Grade: F
Result: Failed
```

## Problem 4 (Medium)
Write a shipping cost calculator:
- If weight <= 1kg: $5
- Elif weight <= 5kg: $10
- Elif weight <= 10kg: $15
- Else: $25

Example:
```
Enter package weight (kg): 12
Shipping cost: $25
```

## Problem 5 (Hard)
Write a comprehensive ATM withdrawal validator:
- Check if amount > 0 (else: "Invalid amount")
- Check if amount <= balance (else: "Insufficient funds")
- Check if amount % 10 == 0 (else: "Amount must be multiple of 10")
- Else: "Withdrawal successful"

Use nested if-else statements.

Example:
```
Balance: $500
Enter amount: $50
Withdrawal successful
New balance: $450
```
