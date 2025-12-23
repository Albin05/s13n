# Editorials: Controlling While Loops Using Break Statement

## Problem 1: Find First Even Number (Easy)

### Solution
```python
numbers = [1, 3, 5, 8, 9, 11]

for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
```

**Output:**
```
First even number: 8
```

### Explanation
- Iterate through list until even number found
- `num % 2 == 0` checks if even
- `break` exits loop immediately when condition met
- Remaining elements (9, 11) are never checked
- Efficient: stops as soon as answer found

---

## Problem 2: Search for Target (Easy)

### Solution
```python
target = "apple"
fruits = ["banana", "orange", "apple", "grape"]

found = False
for fruit in fruits:
    if fruit == target:
        print(f"Found {target}!")
        found = True
        break

if not found:
    print(f"{target} not found")
```

**Output:**
```
Found apple!
```

### Explanation
- Search list for specific item
- Use flag variable to track if found
- Break as soon as target located
- Check flag after loop to handle "not found" case
- Without break, would unnecessarily check remaining items

---

## Problem 3: Stop at Negative (Easy)

### Solution
```python
numbers = [5, 10, 15, -3, 20, 25]
total = 0

for num in numbers:
    if num < 0:
        print("Negative number encountered, stopping")
        break
    total += num

print(f"Sum before negative: {total}")
```

**Output:**
```
Negative number encountered, stopping
Sum before negative: 30
```

### Explanation
- Sum numbers until negative encountered
- Break when `num < 0`
- Total accumulates: 5 + 10 + 15 = 30
- Numbers after -3 (20, 25) are not processed
- Pattern: stop on sentinel condition

---

## Problem 4: Infinite Loop with Break (Medium)

### Solution
```python
count = 0

while True:
    count += 1
    print(f"Count: {count}")
    if count >= 3:
        break

print("Loop exited")
```

**Output:**
```
Count: 1
Count: 2
Count: 3
Loop exited
```

### Explanation
- `while True:` creates infinite loop
- **MUST** have break statement to exit
- Loop runs 3 times before breaking
- Common pattern for menu systems
- Break is ONLY way out of `while True`

---

## Problem 5: User Input Until Quit (Medium)

### Solution
```python
while True:
    command = input("Enter command (or 'quit'): ")

    if command == "quit":
        print("Exiting...")
        break

    print(f"You entered: {command}")

print("Program ended")
```

**Example Interaction:**
```
Enter command (or 'quit'): hello
You entered: hello
Enter command (or 'quit'): world
You entered: world
Enter command (or 'quit'): quit
Exiting...
Program ended
```

### Explanation
- Infinite loop for continuous input
- Check for exit command inside loop
- Break when user wants to quit
- Cleaner than checking condition in while statement
- Processes all commands before checking for quit

---

## Problem 6: Find Divisor (Medium)

### Solution
```python
number = 100

for i in range(2, number):
    if number % i == 0:
        print(f"First divisor of {number}: {i}")
        break
else:
    print(f"{number} is prime")
```

**Output:**
```
First divisor of 100: 2
```

### Explanation
- Find first divisor of number
- Loop from 2 to number-1
- Break as soon as divisor found
- `else` clause runs if loop completes WITHOUT break
- For 100: 2 divides evenly, so break immediately
- Efficient: doesn't check remaining numbers

---

## Problem 7: Password System with Limit (Medium)

### Solution
```python
correct_password = "python123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Enter password: ")
    attempts += 1

    if password == correct_password:
        print("Access granted!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. {remaining} attempts remaining")
else:
    print("Too many failed attempts. Account locked.")
```

**Example Output (correct on 2nd try):**
```
Enter password: wrong
Wrong password. 2 attempts remaining
Enter password: python123
Access granted!
```

### Explanation
- Loop while attempts remain
- Break when correct password entered
- `else` clause runs if all attempts exhausted (no break)
- If break happens, else is skipped
- Real-world security pattern

---

## Problem 8: Find Multiple Conditions (Hard)

### Solution
```python
numbers = [1, 3, 7, 10, 15, 20, 25]

for num in numbers:
    if num > 10 and num % 5 == 0:
        print(f"Found: {num} (>10 and divisible by 5)")
        break
else:
    print("No number found matching criteria")
```

**Output:**
```
Found: 15 (>10 and divisible by 5)
```

### Explanation
- Search for number meeting TWO conditions
- Must be > 10 AND divisible by 5
- Break when both conditions met
- 15 is first to satisfy both
- Demonstrates compound conditions with break

---

## Problem 9: Nested Loop with Break (Hard)

### Solution
```python
found = False

for i in range(1, 5):
    for j in range(1, 5):
        if i * j == 12:
            print(f"Found: {i} x {j} = 12")
            found = True
            break
    if found:
        break
```

**Output:**
```
Found: 3 x 4 = 12
```

### Explanation
- Nested loops to find product combination
- Inner break exits inner loop only
- Use flag to break outer loop too
- Finds 3 × 4 = 12 and stops
- Without outer break, would find 4 × 3 = 12 too
- Pattern: breaking from nested loops requires flag

---

## Problem 10: Validate Input with Break (Hard)

### Solution
```python
while True:
    age = input("Enter age (0-120): ")

    if not age.isdigit():
        print("Please enter a valid number")
        continue

    age = int(age)

    if 0 <= age <= 120:
        print(f"Valid age: {age}")
        break
    else:
        print("Age must be between 0 and 120")

print("Input accepted")
```

**Example Interaction:**
```
Enter age (0-120): abc
Please enter a valid number
Enter age (0-120): 150
Age must be between 0 and 120
Enter age (0-120): 25
Valid age: 25
Input accepted
```

### Explanation
- Infinite loop for validation
- Check if input is numeric first
- Then check range
- Break only when valid
- Forces user to provide acceptable input
- Combines break and continue

---

## Problem 11: Search Matrix (Hard)

### Solution
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5
found = False

for row in matrix:
    for num in row:
        if num == target:
            print(f"Found {target}")
            found = True
            break
    if found:
        break

if not found:
    print(f"{target} not found")
```

**Output:**
```
Found 5
```

### Explanation
- Search 2D matrix for value
- Inner break exits row loop
- Outer break exits matrix loop
- Flag ensures both loops exit
- Stops immediately when found
- Doesn't search remaining rows/columns

---

## Problem 12: Process Until Special Value (Hard)

### Solution
```python
data = [10, 20, 30, -1, 40, 50]
processed = []

for value in data:
    if value == -1:
        print("Sentinel value reached")
        break
    processed.append(value * 2)

print(f"Processed: {processed}")
```

**Output:**
```
Sentinel value reached
Processed: [20, 40, 60]
```

### Explanation
- Process data until sentinel (-1)
- Break when sentinel encountered
- Values after sentinel ignored
- Processed list contains doubled values
- Pattern: partial data processing

---

## Problem 13: Menu System (Very Hard)

### Solution
```python
balance = 1000

while True:
    print(f"\n=== Balance: ${balance} ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        amount = float(input("Deposit amount: $"))
        balance += amount
        print(f"Deposited ${amount}")
    elif choice == "2":
        amount = float(input("Withdraw amount: $"))
        if amount <= balance:
            balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")
    elif choice == "3":
        print(f"Current balance: ${balance}")
    elif choice == "4":
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice")

print(f"Final balance: ${balance}")
```

**Example Output:**
```
=== Balance: $1000 ===
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Choice: 1
Deposit amount: $500
Deposited $500

=== Balance: $1500 ===
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Choice: 4
Thank you for banking with us!
Final balance: $1500
```

### Explanation
- Interactive menu with `while True`
- Break when user selects exit
- State (balance) persists across iterations
- Each option performs different action
- Clean exit with break
- Real-world application pattern

---

## Problem 14: Find Prime Number (Very Hard)

### Solution
```python
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Not prime, no need to continue

    return True  # No divisors found

number = 29
if is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
```

**Output:**
```
29 is prime
```

### Explanation
- Check if number is prime
- Loop only to square root (optimization)
- Return False (like break) when divisor found
- If loop completes, number is prime
- Early return avoids unnecessary checks
- Efficient prime checking

---

## Problem 15: Guessing Game with Hints (Very Hard)

### Solution
```python
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Guess the number between 1 and 100!")

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
    attempts += 1

    if guess == secret:
        print(f"Correct! You won in {attempts} attempts!")
        break
    elif guess < secret:
        diff = secret - guess
        if diff <= 5:
            print("Too low, but very close!")
        else:
            print("Too low")
    else:
        diff = guess - secret
        if diff <= 5:
            print("Too high, but very close!")
        else:
            print("Too high")
else:
    print(f"Game over! The number was {secret}")
```

**Example Output:**
```
Guess the number between 1 and 100!
Attempt 1/7: 50
Too low
Attempt 2/7: 75
Too high
Attempt 3/7: 60
Too low, but very close!
Attempt 4/7: 63
Correct! You won in 4 attempts!
```

### Explanation
- Limited attempts game
- Break when correct guess
- Else clause if all attempts used
- Provides proximity hints
- Demonstrates break vs loop exhaustion
- Game logic with multiple exit paths

---

## Problem 16: Find Pair Sum (Very Hard)

### Solution
```python
numbers = [2, 7, 11, 15, 3, 6]
target_sum = 9

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            print(f"Found pair: {numbers[i]} + {numbers[j]} = {target_sum}")
            found = True
            break
    if found:
        break

if not found:
    print("No pair found")
```

**Output:**
```
Found pair: 2 + 7 = 9
```

### Explanation
- Find two numbers that sum to target
- Nested loops check all pairs
- Break both loops when pair found
- Uses flag to exit outer loop
- Stops at first valid pair
- Algorithm: brute force pair search

---

## Problem 17: Process Commands (Very Hard)

### Solution
```python
commands = ["add 5", "multiply 2", "stop", "add 10", "divide 2"]
result = 0

for cmd in commands:
    parts = cmd.split()
    operation = parts[0]

    if operation == "stop":
        print("Stop command received")
        break

    value = int(parts[1])

    if operation == "add":
        result += value
    elif operation == "multiply":
        result *= value
    elif operation == "divide":
        result //= value

    print(f"After {cmd}: {result}")

print(f"Final result: {result}")
```

**Output:**
```
After add 5: 5
After multiply 2: 10
Stop command received
Final result: 10
```

### Explanation
- Process list of commands
- Break on "stop" command
- Commands after "stop" ignored
- Result accumulates until break
- Demonstrates command processing pattern
- Early termination based on data

---

## Problem 18: Find All Until Condition (Very Hard)

### Solution
```python
numbers = [1, 3, 5, 7, 10, 12, 14, 16]
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        print(f"First even number {num} found, stopping")
        break
    odd_numbers.append(num)

print(f"Odd numbers before even: {odd_numbers}")
```

**Output:**
```
First even number 10 found, stopping
Odd numbers before even: [1, 3, 5, 7]
```

### Explanation
- Collect items until condition met
- Break stops collection
- List contains only pre-break items
- Pattern: accumulate until sentinel
- Partial list processing

---

## Problem 19: Timeout Simulation (Very Hard)

### Solution
```python
max_iterations = 1000
iterations = 0
found = False

while iterations < max_iterations:
    iterations += 1

    # Simulate search (found on iteration 573)
    if iterations == 573:
        found = True
        print(f"Item found at iteration {iterations}")
        break

    if iterations % 100 == 0:
        print(f"Still searching... {iterations} iterations")

if not found:
    print(f"Search timeout after {max_iterations} iterations")
```

**Output:**
```
Still searching... 100 iterations
Still searching... 200 iterations
Still searching... 300 iterations
Still searching... 400 iterations
Still searching... 500 iterations
Item found at iteration 573
```

### Explanation
- Safety limit prevents infinite loop
- Break when item found
- Progress updates every 100 iterations
- Timeout if not found in time
- Real-world pattern: bounded search

---

## Problem 20: Complex Validation (Very Hard)

### Solution
```python
while True:
    username = input("Enter username (3-15 chars, alphanumeric): ")

    # Check length
    if len(username) < 3 or len(username) > 15:
        print("Username must be 3-15 characters")
        continue

    # Check alphanumeric
    if not username.isalnum():
        print("Username must be alphanumeric")
        continue

    # All checks passed
    print(f"Username '{username}' accepted!")
    break

print("Registration complete")
```

**Example Interaction:**
```
Enter username (3-15 chars, alphanumeric): ab
Username must be 3-15 characters
Enter username (3-15 chars, alphanumeric): hello@world
Username must be alphanumeric
Enter username (3-15 chars, alphanumeric): hello123
Username 'hello123' accepted!
Registration complete
```

### Explanation
- Multiple validation criteria
- Continue on failure (ask again)
- Break only when ALL checks pass
- Each check provides specific feedback
- Robust input validation pattern
- Combines break and continue effectively

---

## Key Concepts Demonstrated

1. **Early Exit**: Break stops loop immediately
2. **Infinite Loops**: `while True` requires break
3. **Search Patterns**: Break when target found
4. **Sentinel Values**: Break on special condition
5. **Loop-Else**: Else runs if NO break occurred
6. **Nested Breaks**: Need flag for outer loop
7. **Efficiency**: Avoid unnecessary iterations
8. **Validation**: Break when input valid
9. **Menu Systems**: Break on exit choice
10. **Timeout Protection**: Break prevents infinite loops

## Break vs Continue vs Return

- **break**: Exit loop entirely
- **continue**: Skip to next iteration (next lesson)
- **return**: Exit function (later lessons)

## Best Practices

- Use break for early exit when condition met
- Combine `while True` with break for cleaner code
- Use else clause to detect if loop completed naturally
- Use flag variables to break from nested loops
- Always ensure break is reachable (avoid infinite loops)
- Provide clear feedback before breaking
