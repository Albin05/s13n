# Lecture Script: Controlling While Loops Using Break Statement

**Duration:** 20-25 minutes
**Learning Objective:** Students will be able to use the break statement to exit loops early when a condition is met.

---

## [0:00-0:02] Hook (2 minutes)

**Open with a relatable scenario:**

> "Imagine you're searching for your keys in a messy room. You check drawer after drawer. Once you FIND the keys, do you keep searching? No! You STOP immediately. That's what `break` does in programming - it stops a loop as soon as you find what you're looking for!"

**Interactive question:**
"Who has played Where's Waldo? Once you spot Waldo, do you keep looking?"

**The connection:**
> "Exactly! The `break` statement is like shouting 'Found it!' and stopping the search. It makes your code more efficient by avoiding unnecessary work."

**Live demo - show the power:**
```python
numbers = [1, 3, 5, 8, 9, 11, 13]

for num in numbers:
    if num % 2 == 0:
        print(f"Found first even number: {num}")
        break
    print(f"Checking {num}...")

print("Search complete!")
```

**Run it:**
```
Checking 1...
Checking 3...
Checking 5...
Found first even number: 8
Search complete!
```

**Point out:**
> "Notice it stopped at 8! It never checked 9, 11, or 13. That's the power of break!"

---

## [0:02-0:08] Main Concept: Break Basics (6 minutes)

### Part 1: What is Break? (2 minutes)

**Explain:**
> "The `break` statement exits the loop IMMEDIATELY. It doesn't wait for the condition to become False - it just jumps out right away!"

**Syntax:**
```python
while condition:
    # code
    if some_condition:
        break  # Exit loop NOW
    # more code
```

**Live code - Simple example:**
```python
count = 1

while count <= 10:
    print(count)
    if count == 5:
        print("Breaking at 5!")
        break
    count += 1

print("Loop ended")
```

**Output:**
```
1
2
3
4
5
Breaking at 5!
Loop ended
```

**Trace through:**
- count=1: Print 1, not 5, increment
- count=2: Print 2, not 5, increment
- count=3: Print 3, not 5, increment
- count=4: Print 4, not 5, increment
- count=5: Print 5, IS 5, **BREAK**
- Jump to "Loop ended"

### Part 2: Break vs Normal Exit (2 minutes)

**Compare two approaches:**

```python
# WITHOUT break - check all items
fruits = ["apple", "banana", "orange", "grape"]
target = "orange"

for fruit in fruits:
    if fruit == target:
        print(f"Found {target}!")
    print(f"Checked {fruit}")  # Always executes
```

**Output:**
```
Checked apple
Checked banana
Found orange!
Checked orange
Checked grape
```

```python
# WITH break - stop when found
fruits = ["apple", "banana", "orange", "grape"]
target = "orange"

for fruit in fruits:
    if fruit == target:
        print(f"Found {target}!")
        break
    print(f"Checked {fruit}")  # Before break check
```

**Output:**
```
Checked apple
Checked banana
Found orange!
```

**Emphasize:**
> "With break, we never check 'grape'! More efficient, especially with large datasets."

### Part 3: Infinite Loops + Break (2 minutes)

**The power combo:**
```python
while True:
    command = input("Enter command (or 'quit'): ")

    if command == "quit":
        print("Exiting...")
        break

    print(f"Processing: {command}")

print("Program ended")
```

**Explain:**
> "`while True` creates an infinite loop - it would run FOREVER. But break gives us a way out! This pattern is super clean for menus and user input."

**Test it:**
```
Enter command (or 'quit'): hello
Processing: hello
Enter command (or 'quit'): world
Processing: world
Enter command (or 'quit'): quit
Exiting...
Program ended
```

---

## [0:08-0:14] Pattern: Loop + Else Clause (6 minutes)

### Part 1: Understanding Loop-Else (3 minutes)

**Introduce the concept:**
> "Python has a special feature: `else` clause on loops! It runs only if the loop completes WITHOUT breaking."

**Syntax:**
```python
for item in sequence:
    if condition:
        break
else:
    # Runs if NO break occurred
    print("Loop completed normally")
```

**Live code - Search example:**
```python
# Search for prime number
number = 29

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime (divisible by {i})")
        break
else:
    print(f"{number} is prime!")
```

**Output:**
```
29 is prime!
```

**Test with non-prime:**
```python
number = 15

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime (divisible by {i})")
        break
else:
    print(f"{number} is prime!")
```

**Output:**
```
15 is not prime (divisible by 3)
```

**Explain:**
> "For 29: loop completes without break → else runs. For 15: found divisor (3) → break → else SKIPPED."

### Part 2: Password with Attempts (3 minutes)

**Real-world example:**
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
            print(f"Wrong! {remaining} attempts left")
else:
    print("Account locked - too many attempts")
```

**Test scenario 1 (success on 2nd try):**
```
Enter password: wrong
Wrong! 2 attempts left
Enter password: python123
Access granted!
```

**Test scenario 2 (all attempts fail):**
```
Enter password: wrong1
Wrong! 2 attempts left
Enter password: wrong2
Wrong! 1 attempts left
Enter password: wrong3
Account locked - too many attempts
```

**Explain:**
> "If break happens (correct password), else is skipped. If all 3 attempts fail (no break), else runs and locks account. Perfect for security!"

---

## [0:14-0:18] Advanced: Nested Loops (4 minutes)

### Part 1: Breaking Inner Loop (2 minutes)

**Show the issue:**
```python
for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(3):
        print(f"  Inner loop: {j}")
        if j == 1:
            break  # Only breaks INNER loop
    print(f"Outer continues...")
```

**Output:**
```
Outer loop: 0
  Inner loop: 0
  Inner loop: 1
Outer continues...
Outer loop: 1
  Inner loop: 0
  Inner loop: 1
Outer continues...
Outer loop: 2
  Inner loop: 0
  Inner loop: 1
Outer continues...
```

**Point out:**
> "Break only exits the CLOSEST loop - the inner one. Outer loop continues normally."

### Part 2: Breaking Both Loops (2 minutes)

**Solution with flag:**
```python
found = False

for i in range(1, 5):
    for j in range(1, 5):
        if i * j == 12:
            print(f"Found: {i} x {j} = 12")
            found = True
            break  # Exit inner
    if found:
        break  # Exit outer

print("Search complete")
```

**Output:**
```
Found: 3 x 4 = 12
Search complete
```

**Explain:**
> "Use a flag variable. Inner break exits inner loop, then check flag to break outer loop. This stops entire search when answer found."

---

## [0:18-0:22] Practice Time (4 minutes)

**Exercise 1: Find First Negative (1.5 minutes)**
> "Given list [5, 10, -3, 8, 12], find and print the first negative number, then stop."

```python
# Solution
numbers = [5, 10, -3, 8, 12]

for num in numbers:
    if num < 0:
        print(f"First negative: {num}")
        break
```

**Exercise 2: Sum Until Zero (2 minutes)**
> "Keep asking for numbers and sum them. When user enters 0, stop and print total."

```python
# Solution
total = 0

while True:
    num = int(input("Enter number (0 to stop): "))

    if num == 0:
        break

    total += num

print(f"Total: {total}")
```

**Walk around and check:**
- Students forgetting to break
- Breaking too early/late
- Not handling loop-else correctly

---

## [0:22-0:25] Wrap-up and Key Takeaways (3 minutes)

**Summarize the main points:**

1. **Break exits immediately**: Doesn't wait for condition
2. **Efficiency**: Skip unnecessary iterations
3. **while True + break**: Common pattern for menus
4. **Loop-else**: Runs if NO break occurred
5. **Nested loops**: Break only exits closest loop
6. **Flag variables**: Break outer loops from inner

**Visual on board:**
```python
# Break pattern
while condition:
    # code
    if exit_condition:
        break  # Jump out NOW
    # more code
# Continues here after break

# Loop-else pattern
while condition:
    if exit_condition:
        break
else:
    # Runs if NO break
```

**Common use cases:**
- ✅ Search algorithms (stop when found)
- ✅ Menu systems (while True + break)
- ✅ Input validation (break when valid)
- ✅ Early exit (break on error)

**Common mistakes:**
- ❌ Forgetting break in `while True`
- ❌ Breaking too early
- ❌ Assuming break exits all nested loops
- ❌ Not handling loop-else properly

**Real-world reminder:**
> "Break makes code efficient! Database searches, file processing, game loops - all use break to stop as soon as the job is done. No wasted effort!"

**Preview next lesson:**
> "Next: the `continue` statement - skip to the next iteration without exiting the loop. Perfect for filtering!"

**Final check question:**
"What's the difference between break and just making the loop condition False?"

**Expected answer:** "Break exits immediately, right then. Making condition False means the loop checks the condition at the top, so current iteration finishes first."

---

## Teaching Tips

1. **Emphasize efficiency** - Show time saved by breaking early
2. **Demonstrate infinite loops** - Show while True safely
3. **Visual diagrams** - Draw loop flow with break exit
4. **Contrast with continue** - Briefly mention difference
5. **Practice loop-else** - Many students miss this feature
6. **Real examples** - Search, validation, menus

## Common Student Questions

**Q: "Can I use break in a for loop too?"**
A: "Absolutely! Break works in BOTH while and for loops."

**Q: "What if I have 3 nested loops?"**
A: "Break still only exits the innermost loop. You'd need flags to break all three."

**Q: "Is while True bad practice?"**
A: "Not at all! It's very common with break. Just make sure break is reachable!"

**Q: "Does else always run after a loop?"**
A: "No! Only if the loop completes WITHOUT break. If break happens, else is skipped."

**Q: "Can I have multiple breaks in one loop?"**
A: "Yes! Each break exits the loop. First one reached wins."

---

## Additional Examples (if time permits)

### Find First Vowel
```python
text = "python"

for char in text:
    if char in "aeiou":
        print(f"First vowel: {char}")
        break
else:
    print("No vowels found")
```

### Guess Game
```python
secret = 7

while True:
    guess = int(input("Guess (1-10): "))

    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
```

### Validate Input
```python
while True:
    age = input("Enter age: ")

    if age.isdigit() and 0 <= int(age) <= 120:
        print("Valid!")
        break

    print("Invalid age, try again")
```
