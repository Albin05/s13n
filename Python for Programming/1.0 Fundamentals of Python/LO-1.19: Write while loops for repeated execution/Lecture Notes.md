# Lecture Notes: Write While Loops

## While Loops

A while loop repeats code **as long as** a condition is True.


---

<div align="center">

![Circular pattern representing loops](https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800&q=80)

*Loops allow you to repeat operations efficiently*

</div>

---
### Basic Syntax

```python
while condition:
    # Code to repeat
    # Must eventually make condition False!
```

## Simple Examples

### Example 1: Count to 5

```python
count = 1

while count <= 5:
    print(count)
    count += 1

# Output: 1 2 3 4 5
```

### Example 2: User Input Validation

```python
password = ""

while len(password) < 8:
    password = input("Enter password (min 8 chars): ")

print("Password accepted!")
```

### Example 3: Menu System

```python
choice = ""

while choice != "quit":
    print("\n1. New Game")
    print("2. Load Game")
    print("3. Quit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        print("Starting new game...")
    elif choice == "2":
        print("Loading game...")
    elif choice == "quit":
        print("Goodbye!")
```

## Infinite Loops

**Warning**: If condition never becomes False, loop runs forever!

```python
# Infinite loop - BAD!
count = 1
while count <= 5:
    print(count)
    # Forgot to increment count!

# Correct
count = 1
while count <= 5:
    print(count)
    count += 1  # Makes condition eventually False
```

## While with Break

```python
while True:  # Infinite loop
    password = input("Enter password: ")
    if password == "secret":
        break  # Exit loop
    print("Wrong password!")
```

## Real-World Applications

### ATM Withdrawal

```python
balance = 1000

while balance > 0:
    print(f"Balance: ${balance}")
    amount = int(input("Withdraw amount (0 to quit): "))
    
    if amount == 0:
        break
    elif amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        print(f"Withdrew ${amount}")

print("Thank you!")
```

### Number Guessing Game

```python
secret = 42
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("Correct!")
```

## Key Takeaways

1. **Repeats while True**: Loop continues as long as condition is True
2. **Must update**: Condition must eventually become False
3. **Check before run**: Condition checked before each iteration
4. **Infinite loops**: Dangerous if condition never becomes False
5. **Use for validation**: Great for user input validation
