# Editorials: Writing While Loops for Repeated Execution

## Problem 1: Count to 10 (Easy)

### Solution
```python
count = 1

while count <= 10:
    print(count)
    count += 1
```

**Output:**
```
1
2
3
4
5
6
7
8
9
10
```

### Explanation
- Initialize `count = 1` before loop
- Loop continues while `count <= 10`
- Print current count
- **CRITICAL**: Increment `count += 1` to eventually make condition False
- Without increment, loop would run forever (infinite loop)
- Loop stops when count becomes 11 (condition False)

---

## Problem 2: Countdown from 5 (Easy)

### Solution
```python
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Blast off!")
```

**Output:**
```
5
4
3
2
1
Blast off!
```

### Explanation
- Start at 5, decrement each iteration
- Condition `countdown > 0` means loop stops when countdown reaches 0
- `countdown -= 1` decreases value by 1 each time
- After loop exits, print "Blast off!"
- Common pattern for countdowns and timers

---

## Problem 3: Sum Numbers Until 0 (Easy)

### Solution
```python
total = 0
number = int(input("Enter a number (0 to stop): "))

while number != 0:
    total += number
    number = int(input("Enter a number (0 to stop): "))

print(f"Total: {total}")
```

**Example Interaction:**
```
Enter a number (0 to stop): 10
Enter a number (0 to stop): 20
Enter a number (0 to stop): 15
Enter a number (0 to stop): 0
Total: 45
```

### Explanation
- Read first number before loop (priming read)
- Loop continues until user enters 0
- Add each number to total
- Read next number at end of loop
- Sentinel value (0) controls loop termination
- Final print happens after loop exits

---

## Problem 4: Password Validator (Medium)

### Solution
```python
correct_password = "python123"
attempts = 0
max_attempts = 3

password = input("Enter password: ")
attempts += 1

while password != correct_password and attempts < max_attempts:
    print("Incorrect password")
    password = input("Enter password: ")
    attempts += 1

if password == correct_password:
    print("Access granted")
else:
    print("Too many failed attempts")
```

**Example Output (successful):**
```
Enter password: wrong
Incorrect password
Enter password: python123
Access granted
```

### Explanation
- First attempt before loop
- Loop continues if: password wrong AND attempts remain
- Tracks number of attempts
- After loop, check WHY it stopped:
  - Password correct → Access granted
  - Too many attempts → Locked out
- Prevents brute force attacks with attempt limit

---

## Problem 5: Find First Multiple of 7 (Medium)

### Solution
```python
number = 1

while number % 7 != 0:
    number += 1

print(f"First multiple of 7: {number}")
```

**Output:**
```
First multiple of 7: 7
```

### Explanation
- Start at 1, increment until divisible by 7
- Condition: `number % 7 != 0` (not a multiple)
- Loop stops when `number % 7 == 0` (is a multiple)
- In this case, stops at 7
- Pattern: loop until condition is met
- Could modify to find nth multiple by adding counter

---

## Problem 6: Guess the Number (Medium)

### Solution
```python
secret_number = 42
guess = int(input("Guess the number: "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))

print("Correct! You guessed it!")
```

**Example Interaction:**
```
Guess the number: 50
Too high!
Guess again: 30
Too low!
Guess again: 42
Correct! You guessed it!
```

### Explanation
- Loop until guess matches secret
- Provide feedback (too high/low) each iteration
- Update guess inside loop
- Classic game pattern
- Could enhance with attempt counter

---

## Problem 7: Double Until Exceeds 1000 (Medium)

### Solution
```python
value = 1
iterations = 0

while value <= 1000:
    print(f"Iteration {iterations}: {value}")
    value *= 2
    iterations += 1

print(f"Final value: {value}")
print(f"Total iterations: {iterations}")
```

**Output:**
```
Iteration 0: 1
Iteration 1: 2
Iteration 2: 4
Iteration 3: 8
Iteration 4: 16
Iteration 5: 32
Iteration 6: 64
Iteration 7: 128
Iteration 8: 256
Iteration 9: 512
Final value: 1024
Total iterations: 10
```

### Explanation
- Exponential growth: doubles each iteration
- Tracks iterations with counter
- Loop while `value <= 1000`
- Stops when value exceeds 1000 (1024)
- Shows power of exponential growth
- Takes only 10 iterations to exceed 1000

---

## Problem 8: Factorial Calculator (Hard)

### Solution
```python
n = 5
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"{n}! = {factorial}")
```

**Output:**
```
5! = 120
```

### Explanation
- Calculate 5! = 5 × 4 × 3 × 2 × 1 = 120
- Initialize factorial = 1 (multiplicative identity)
- Multiply by each number from 1 to n
- Increment counter each iteration
- Alternative to for loop
- Pattern: accumulator with multiplication

---

## Problem 9: Fibonacci Sequence (Hard)

### Solution
```python
n = 10
a, b = 0, 1
count = 0

print("First 10 Fibonacci numbers:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

print()
```

**Output:**
```
First 10 Fibonacci numbers:
0 1 1 2 3 5 8 13 21 34
```

### Explanation
- Generate first n Fibonacci numbers
- Pattern: each number is sum of previous two
- `a, b = b, a + b` is simultaneous assignment:
  - New a = old b
  - New b = old a + old b
- Elegant way to update two variables
- Counter tracks how many generated

---

## Problem 10: Input Validation (Hard)

### Solution
```python
age = int(input("Enter your age (0-120): "))

while age < 0 or age > 120:
    print("Invalid age! Must be between 0 and 120")
    age = int(input("Enter your age (0-120): "))

print(f"Valid age entered: {age}")
```

**Example Interaction:**
```
Enter your age (0-120): 150
Invalid age! Must be between 0 and 120
Enter your age (0-120): -5
Invalid age! Must be between 0 and 120
Enter your age (0-120): 25
Valid age entered: 25
```

### Explanation
- Validate input is within acceptable range
- Loop while input is invalid
- Force user to provide valid input
- Common pattern for robust programs
- Prevents downstream errors from bad data

---

## Problem 11: Menu System (Hard)

### Solution
```python
choice = ""

while choice != "4":
    print("\n=== Menu ===")
    print("1. Option A")
    print("2. Option B")
    print("3. Option C")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print("You selected Option A")
    elif choice == "2":
        print("You selected Option B")
    elif choice == "3":
        print("You selected Option C")
    elif choice == "4":
        print("Exiting...")
    else:
        print("Invalid choice")

print("Program ended")
```

**Example Output:**
```
=== Menu ===
1. Option A
2. Option B
3. Option C
4. Exit
Enter choice: 1
You selected Option A

=== Menu ===
1. Option A
2. Option B
3. Option C
4. Exit
Enter choice: 4
Exiting...
Program ended
```

### Explanation
- Loop until user chooses to exit
- Display menu each iteration
- Process choice with if/elif
- Invalid input doesn't crash program
- Common pattern for interactive programs
- User controls when to exit

---

## Problem 12: Find Digits Sum (Hard)

### Solution
```python
number = 12345
sum_digits = 0

while number > 0:
    digit = number % 10
    sum_digits += digit
    number //= 10

print(f"Sum of digits: {sum_digits}")
```

**Output:**
```
Sum of digits: 15
```

### Explanation
- Extract and sum all digits: 1+2+3+4+5 = 15
- `number % 10` gets rightmost digit
- `number //= 10` removes rightmost digit
- Loop until no digits remain
- Pattern: process number digit by digit
- Works for any positive integer

---

## Problem 13: Reverse a Number (Very Hard)

### Solution
```python
number = 12345
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(f"Reversed: {reversed_number}")
```

**Output:**
```
Reversed: 54321
```

### Explanation
- Build reversed number digit by digit
- Extract rightmost digit from original
- Add it to reversed (multiplying by 10 first to shift)
- Process: 0 → 5 → 54 → 543 → 5432 → 54321
- Each iteration:
  - Shift reversed left (×10)
  - Add new digit
  - Remove digit from original
- Common algorithm pattern

---

## Problem 14: GCD Calculator (Very Hard)

### Solution
```python
a = 48
b = 18

while b != 0:
    temp = b
    b = a % b
    a = temp

print(f"GCD: {a}")
```

**Output:**
```
GCD: 6
```

### Explanation
- Euclidean algorithm for GCD
- Iteration trace:
  - a=48, b=18: b becomes 48%18=12, a becomes 18
  - a=18, b=12: b becomes 18%12=6, a becomes 12
  - a=12, b=6: b becomes 12%6=0, a becomes 6
  - b=0: loop stops, a=6 is GCD
- Efficient algorithm (logarithmic time)
- Classic use of while loop

---

## Problem 15: Prime Number Checker (Very Hard)

### Solution
```python
number = 29
is_prime = True
divisor = 2

if number < 2:
    is_prime = False
else:
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

if is_prime and number >= 2:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
```

**Output:**
```
29 is prime
```

### Explanation
- Check if number has any divisors
- Only check up to square root (optimization)
- If divisor found, set flag and break
- Loop while `divisor * divisor <= number`
- Example: for 29, check 2,3,4,5 (5²=25 < 29, 6²=36 > 29)
- No divisors found → prime
- Efficient primality test for small numbers

---

## Problem 16: Collatz Sequence (Very Hard)

### Solution
```python
n = 10
steps = 0

print(f"Starting with {n}:")
while n != 1:
    print(n, end=" → ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    steps += 1

print(f"1\nReached 1 in {steps} steps")
```

**Output:**
```
Starting with 10:
10 → 5 → 16 → 8 → 4 → 2 → 1
Reached 1 in 6 steps
```

### Explanation
- Collatz conjecture: any number eventually reaches 1
- Rule: if even divide by 2, if odd multiply by 3 and add 1
- Sequence for 10: 10→5→16→8→4→2→1
- Track number of steps
- Famous unsolved problem in mathematics
- Demonstrates conditional logic in loops

---

## Problem 17: Bank Account Simulator (Very Hard)

### Solution
```python
balance = 1000
action = ""

while action != "quit":
    print(f"\nBalance: ${balance}")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Quit")
    action = input("Choose action: ")

    if action == "1":
        amount = float(input("Deposit amount: $"))
        if amount > 0:
            balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount")
    elif action == "2":
        amount = float(input("Withdraw amount: $"))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Invalid amount or insufficient funds")
    elif action == "3":
        action = "quit"
        print("Thank you!")
    else:
        print("Invalid choice")

print(f"Final balance: ${balance}")
```

**Example Output:**
```
Balance: $1000
1. Deposit
2. Withdraw
3. Quit
Choose action: 1
Deposit amount: $500
Deposited $500

Balance: $1500
1. Deposit
2. Withdraw
3. Quit
Choose action: 2
Withdraw amount: $200
Withdrew $200

Balance: $1300
1. Deposit
2. Withdraw
3. Quit
Choose action: 3
Thank you!
Final balance: $1300
```

### Explanation
- Simulate bank account operations
- Loop until user quits
- Validate transactions (positive amounts, sufficient balance)
- Update balance based on operation
- State persists across iterations
- Real-world application pattern

---

## Problem 18: Power Calculator Without ** (Very Hard)

### Solution
```python
base = 2
exponent = 5
result = 1
counter = 0

while counter < exponent:
    result *= base
    counter += 1

print(f"{base}^{exponent} = {result}")
```

**Output:**
```
2^5 = 32
```

### Explanation
- Calculate 2⁵ = 2×2×2×2×2 = 32
- Multiply base by itself exponent times
- Initialize result = 1 (multiplicative identity)
- Loop exponent times
- Alternative to using ** operator
- Demonstrates loop-based accumulation

---

## Problem 19: String Character Counter (Hard)

### Solution
```python
text = "hello world"
char_to_count = "l"
index = 0
count = 0

while index < len(text):
    if text[index] == char_to_count:
        count += 1
    index += 1

print(f"'{char_to_count}' appears {count} times")
```

**Output:**
```
'l' appears 3 times
```

### Explanation
- Count occurrences of character in string
- Use index to access each character
- Increment index each iteration
- Increment count when character matches
- Loop while index < string length
- Alternative to for loop with strings

---

## Problem 20: Find Maximum in User Input (Very Hard)

### Solution
```python
max_value = None
value = input("Enter a number (or 'done'): ")

while value != "done":
    num = int(value)
    if max_value is None or num > max_value:
        max_value = num
    value = input("Enter a number (or 'done'): ")

if max_value is not None:
    print(f"Maximum value: {max_value}")
else:
    print("No numbers entered")
```

**Example Interaction:**
```
Enter a number (or 'done'): 45
Enter a number (or 'done'): 12
Enter a number (or 'done'): 78
Enter a number (or 'done'): 23
Enter a number (or 'done'): done
Maximum value: 78
```

### Explanation
- Find largest number from user input
- Use None to represent "no value yet"
- First number automatically becomes max
- Update max if current number is larger
- Sentinel value "done" stops input
- Handle edge case: no numbers entered
- Pattern: finding extremes in sequences

---

## Key Concepts Demonstrated

1. **Loop Initialization**: Set variables before loop starts
2. **Loop Condition**: Must eventually become False
3. **Update Statement**: Change variables to progress toward termination
4. **Infinite Loops**: Forget to update → loop never stops
5. **Sentinel Values**: Special values that signal end of input
6. **Accumulators**: Variables that collect results (sum, count, etc.)
7. **Counters**: Track iterations or occurrences
8. **Input Validation**: Keep asking until valid
9. **State Persistence**: Variables retain values across iterations
10. **Early Exit**: Break when condition met

## Common Patterns

- **Counter loop**: `while count < limit`
- **Sentinel loop**: `while input != sentinel_value`
- **Search loop**: `while not found`
- **Validation loop**: `while input_invalid`
- **Menu loop**: `while choice != quit_option`
- **Accumulator**: Build result piece by piece

## Best Practices

- Always update loop variables
- Initialize before loop
- Avoid infinite loops
- Use meaningful variable names
- Consider edge cases (empty input, zero, negative)
- Provide user feedback
- Validate all input
