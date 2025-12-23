# Lecture Script: Writing While Loops for Repeated Execution

**Duration:** 20-25 minutes
**Learning Objective:** Students will be able to write while loops to repeat code while a condition is True.

---

## [0:00-0:02] Hook (2 minutes)

**Open with a relatable scenario:**

> "Imagine you're asking a friend to guess your age. You keep saying 'Try again!' until they get it right. How would we write code that keeps repeating until a condition is met? That's what while loops do - they're like saying 'Keep doing this WHILE something is true.'"

**Interactive question:**
"Who has played a game where you keep trying until you succeed? Like Wordle, or a password login?"

**The connection:**
> "While loops are PERFECT for this! They repeat code as long as a condition stays True. Password wrong? Loop continues. Password correct? Loop stops. Let's see this in action!"

**Live demo - show the magic:**
```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Attempt {attempts + 1}")
    attempts += 1

print("Done!")
```

**Run it:**
```
Attempt 1
Attempt 2
Attempt 3
Done!
```

---

## [0:02-0:10] Main Concept: While Loop Basics (8 minutes)

### Part 1: The Anatomy of a While Loop (3 minutes)

**Explain the structure:**
```python
while condition:
    # Code to repeat
    # Update variables
```

**Live code - Simple counter:**
```python
count = 1

while count <= 5:
    print(f"Count is: {count}")
    count += 1

print("Loop finished!")
```

**Run and explain each part:**
```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
Loop finished!
```

**Draw the flow on board:**
```
1. Check condition (count <= 5)
2. If True → Execute body
3. Go back to step 1
4. If False → Exit loop
```

**CRITICAL point - show what happens WITHOUT update:**
```python
# DANGER: Infinite loop!
count = 1

while count <= 5:
    print(f"Count is: {count}")
    # Forgot to add count += 1 !
```

**Explain:**
> "This will print 'Count is: 1' FOREVER! The condition never becomes False because count never changes. ALWAYS make sure your loop variables get updated!"

### Part 2: The Three Essential Parts (3 minutes)

**Write on board:**
```
1. INITIALIZATION: Set variables before loop
2. CONDITION: Test that eventually becomes False
3. UPDATE: Change variables inside loop
```

**Live code - Countdown:**
```python
# 1. INITIALIZATION
countdown = 5

# 2. CONDITION
while countdown > 0:
    print(countdown)
    # 3. UPDATE
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

**Trace through manually:**
- Start: countdown = 5
- Check: 5 > 0? YES → Print 5, countdown = 4
- Check: 4 > 0? YES → Print 4, countdown = 3
- Check: 3 > 0? YES → Print 3, countdown = 2
- Check: 2 > 0? YES → Print 2, countdown = 1
- Check: 1 > 0? YES → Print 1, countdown = 0
- Check: 0 > 0? NO → Exit loop
- Print "Blast off!"

### Part 3: When to Use While vs For (2 minutes)

**Compare:**
```python
# Use WHILE when: you don't know how many times
password = input("Enter password: ")
while password != "secret":
    print("Wrong!")
    password = input("Try again: ")

# Use FOR when: you know the count
for i in range(5):
    print(i)
```

**Key difference:**
> "WHILE loop = 'repeat until condition becomes False' (unknown iterations)
> FOR loop = 'repeat exactly N times' (known iterations)"

---

## [0:10-0:16] Common Patterns (6 minutes)

### Pattern 1: User Input with Validation (2 minutes)

**Live code:**
```python
age = int(input("Enter your age (0-120): "))

while age < 0 or age > 120:
    print("Invalid! Must be 0-120")
    age = int(input("Try again: "))

print(f"Valid age: {age}")
```

**Test with invalid then valid:**
```
Enter your age (0-120): 150
Invalid! Must be 0-120
Try again: -5
Invalid! Must be 0-120
Try again: 25
Valid age: 25
```

**Explain pattern:**
> "Read input BEFORE loop. Loop WHILE invalid. Read new input AT END of loop. This forces valid input!"

### Pattern 2: Accumulator (2 minutes)

**Live code - Sum numbers:**
```python
total = 0
number = int(input("Enter number (0 to stop): "))

while number != 0:
    total += number
    number = int(input("Enter number (0 to stop): "))

print(f"Total: {total}")
```

**Test:**
```
Enter number (0 to stop): 10
Enter number (0 to stop): 20
Enter number (0 to stop): 5
Enter number (0 to stop): 0
Total: 35
```

**Key terms:**
- **Accumulator**: `total` - builds up result
- **Sentinel value**: `0` - signals to stop
- **Priming read**: First input before loop

### Pattern 3: Menu System (2 minutes)

**Live code:**
```python
choice = ""

while choice != "3":
    print("\n=== Menu ===")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid choice!")

print("Program ended")
```

**Demonstrate:**
```
=== Menu ===
1. Say Hello
2. Say Goodbye
3. Exit
Choice: 1
Hello!

=== Menu ===
1. Say Hello
2. Say Goodbye
3. Exit
Choice: 3
Exiting...
Program ended
```

**Explain:**
> "Loop until user chooses exit. Menu repeats each time. This is how most interactive programs work!"

---

## [0:16-0:20] Advanced Examples (4 minutes)

### Example 1: Number Guessing Game (2 minutes)

```python
secret = 42
guess = int(input("Guess my number: "))

while guess != secret:
    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))

print("You got it!")
```

**Play through:**
```
Guess my number: 50
Too high!
Guess again: 30
Too low!
Guess again: 42
You got it!
```

**Highlight:**
- Feedback in loop
- Loop until correct
- Classic game pattern

### Example 2: Find Digits Sum (2 minutes)

```python
number = 12345
digit_sum = 0

while number > 0:
    digit = number % 10  # Get last digit
    digit_sum += digit
    number //= 10  # Remove last digit

print(f"Sum of digits: {digit_sum}")
```

**Output:**
```
Sum of digits: 15
```

**Trace through:**
- 12345 → digit=5, sum=5, number=1234
- 1234 → digit=4, sum=9, number=123
- 123 → digit=3, sum=12, number=12
- 12 → digit=2, sum=14, number=1
- 1 → digit=1, sum=15, number=0
- 0 > 0? NO → Exit

**Explain the operators:**
> "`% 10` gets rightmost digit. `//= 10` removes it. Loop until no digits left!"

---

## [0:20-0:23] Practice Time (3 minutes)

**Exercise 1: Count Down (1 minute)**
> "Write a loop that counts from 10 down to 1, then prints 'Happy New Year!'"

```python
# Solution
count = 10
while count > 0:
    print(count)
    count -= 1
print("Happy New Year!")
```

**Exercise 2: Sum Even Numbers (1.5 minutes)**
> "Sum all even numbers from 2 to 20. Use a while loop."

```python
# Solution
number = 2
total = 0

while number <= 20:
    total += number
    number += 2

print(f"Sum: {total}")  # 110
```

**Walk around and check common mistakes:**
- Forgetting to update counter
- Wrong condition (< vs <=)
- Initializing inside loop

**Quick variation:**
> "What if we want ODD numbers? Just change initialization to 1!"

```python
number = 1  # Start at 1 instead of 2
total = 0

while number <= 20:
    total += number
    number += 2

print(f"Sum: {total}")  # 100
```

---

## [0:23-0:25] Wrap-up and Key Takeaways (2 minutes)

**Summarize the main points:**

1. **While loop syntax**: `while condition:`
2. **Three parts**: Initialize, Condition, Update
3. **Infinite loops**: Happen when condition never becomes False
4. **Use cases**: Unknown iterations, validation, menus, games
5. **Accumulators**: Build results over iterations
6. **Sentinel values**: Special values that stop loop

**Visual on board:**
```python
# Template
variable = initial_value

while condition:
    # Do something
    # Update variable(s)

# Code after loop
```

**Common mistakes to avoid:**
- ❌ Forgetting to update loop variable
- ❌ Wrong condition operator
- ❌ Initializing inside loop
- ✅ Always ask: "Will this eventually stop?"

**Real-world reminder:**
> "While loops are everywhere: games (keep playing until game over), ATMs (menu until user exits), password systems (retry until correct), download progress (while not complete). Master while loops and you can build interactive programs!"

**Preview next lesson:**
> "Next time: the `break` statement - how to exit a loop early when you find what you're looking for. Perfect for search algorithms!"

**Final check question:**
"What's the difference between a for loop and a while loop?"

**Expected answer:** "For loop runs a specific number of times. While loop runs until a condition becomes False - we don't always know how many times!"

---

## Teaching Tips

1. **Emphasize infinite loops** - Show one, explain how to stop it (Ctrl+C)
2. **Draw flow diagrams** - Visual helps understanding
3. **Trace manually** - Walk through 2-3 iterations on board
4. **Live code everything** - Students see output immediately
5. **Show common errors** - Teach through mistakes
6. **Use real examples** - Games, validation, menus

## Common Student Questions

**Q: "How do I know if I should use while or for?"**
A: "If you know exactly how many times (like 'do this 10 times'), use for. If you're waiting for something to happen (like 'until password is correct'), use while."

**Q: "What if I want to loop forever?"**
A: "Use `while True:` - but make sure you have a way to exit with `break` or the program will never stop!"

**Q: "Why do we read input twice (before and inside loop)?"**
A: "The first read is the 'priming read' - we need an initial value to test. The second read gets the next value. It's a common pattern for sentinel-controlled loops."

**Q: "Can I have a while loop inside another while loop?"**
A: "Yes! Nested while loops work just like nested if statements. Just be EXTRA careful about infinite loops."

**Q: "What happens if the condition is False from the start?"**
A: "The loop body never executes - not even once. Python checks the condition BEFORE entering the loop."

---

## Additional Examples (if time permits)

### Factorial
```python
n = 5
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"{n}! = {factorial}")  # 120
```

### Reverse Number
```python
number = 12345
reversed = 0

while number > 0:
    digit = number % 10
    reversed = reversed * 10 + digit
    number //= 10

print(f"Reversed: {reversed}")  # 54321
```

### Fibonacci
```python
n = 10
a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
# Output: 0 1 1 2 3 5 8 13 21 34
```
