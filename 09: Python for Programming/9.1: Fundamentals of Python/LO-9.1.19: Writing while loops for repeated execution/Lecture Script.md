### LO-19 Write While Loops (25 minutes)


### CS Theory Bite

> **Origin**: While loops implement **iteration**, one of the two fundamental control structures (alongside selection) that make languages **Turing complete**. Alan Turing's machine (1936) was essentially an infinite while loop.
>
> **Analogy**: A `while` loop is like a **treadmill** — you keep running as long as the condition (your energy) holds True.
>
> **Why it matters**: While loops handle situations where you don't know how many iterations are needed — user input validation, searching, etc.


### Hook (3 minutes)

**Say**: "You're trying to guess a password. You keep trying WHILE you haven't guessed it. That's a while loop - repeating code until a condition becomes False!"

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Attempt {attempts + 1}")
    attempts += 1

print("Done!")
```

### While Loop Basics (8 minutes)

**Say**: "While loops repeat code AS LONG AS a condition is True."

**Structure**:
```python
while condition:
    # Code to repeat
    # Must update variables!
```

**Simple countdown**:
```python
count = 5

while count > 0:
    print(count)
    count -= 1  # MUST update or infinite loop!

print("Blastoff!")
```

**Key Points**:
- Condition checked BEFORE each iteration
- If condition starts False, code never runs
- MUST update variables or loop runs forever
- Use when you don't know how many times to loop

**Infinite loop danger**:
```python
# BAD - infinite loop!
x = 0
while x < 10:
    print(x)
    # Forgot to update x!
```

### Input Validation Pattern (6 minutes)

**Say**: "While loops are perfect for getting valid input from users!"

```python
age = int(input("Enter your age (0-120): "))

while age < 0 or age > 120:
    print("Invalid! Must be 0-120")
    age = int(input("Try again: "))

print(f"Valid age: {age}")
```

**Real-World**: Login system
```python
password = input("Enter password: ")

while len(password) < 8:
    print("Too short! Password must be 8+ characters")
    password = input("Try again: ")

print("Password accepted!")
```

### Advanced Examples (4 minutes)

**Say**: "Let's build a number guessing game!"

```python
secret = 42
guess = int(input("Guess my number (1-100): "))

while guess != secret:
    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))

print("Correct! You win!")
```

### Common Patterns (3 minutes)

**Accumulator pattern**:
```python
total = 0
num = int(input("Enter number (0 to stop): "))

while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))

print(f"Total: {total}")
```

**Counter pattern**:
```python
count = 0
num = 1

while num <= 100:
    count += 1
    num += 1

print(f"Counted to 100: {count} times")
```

### Practice (2 minutes)

New Year countdown:
```python
count = 10

while count > 0:
    print(count)
    count -= 1

print("Happy New Year!")
```
