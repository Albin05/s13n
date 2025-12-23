# Pre-Read: Writing While Loops

## What You'll Learn
In this lesson, you'll learn how to use while loops to repeat code as long as a condition remains True. This is one of the most fundamental tools for making programs do repetitive tasks automatically.

## Why This Matters
Imagine you're building:
- A password checker that keeps asking until the user enters the correct password
- A game that runs until the player loses all lives
- A calculator app that keeps running until the user chooses "quit"
- A shopping cart that lets users add items until they're done

Without loops, you'd have to copy-paste the same code hundreds of times. Loops let you write the code once and run it as many times as needed!

---

## What is a While Loop?

A **while loop** repeats a block of code **as long as** a condition is True. Think of it like telling Python: "Keep doing this while this condition is true."

```python
while condition:
    # Code to repeat
```

The loop checks the condition **before** each repetition. If True, it runs the code. If False, it stops.

---

## Simple Example: Counting

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1

print("Done!")
```

**Output:**
```
1
2
3
4
5
Done!
```

**How it works:**
1. Start: `count` is 1
2. Check: Is `count <= 5`? Yes (1 <= 5) → Run code
3. Print 1, then `count` becomes 2
4. Check: Is `count <= 5`? Yes (2 <= 5) → Run code
5. Print 2, then `count` becomes 3
6. ... continues ...
7. Check: Is `count <= 5`? Yes (5 <= 5) → Run code
8. Print 5, then `count` becomes 6
9. Check: Is `count <= 5`? No (6 > 5) → Stop loop
10. Print "Done!"

---

## Real-World Example: Password Validation

```python
password = ""

while len(password) < 8:
    password = input("Enter password (min 8 characters): ")
    if len(password) < 8:
        print("Too short! Try again.")

print("Password accepted!")
```

**How this works:**
- Keeps asking for a password **while** it's too short
- Once user enters 8+ characters, condition becomes False and loop stops
- No matter how many times they enter a wrong password, the code is written once!

---

## The Critical Part: Updating the Condition

**WARNING:** The condition must eventually become False, or your loop will run forever!

### Infinite Loop (BAD)

```python
count = 1

while count <= 5:
    print(count)
    # Forgot to change count!
    # count will always be 1, so count <= 5 is always True
    # Loop never stops!
```

### Correct Loop (GOOD)

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1  # This makes condition eventually False!
```

**Key rule:** Your loop must change something that affects the condition, or it will run forever.

---

## Another Example: Game Menu

```python
choice = ""

while choice != "quit":
    print("\n--- Game Menu ---")
    print("1. Start Game")
    print("2. View Score")
    print("Type 'quit' to exit")

    choice = input("Your choice: ")

    if choice == "1":
        print("Starting game...")
    elif choice == "2":
        print("Your score: 100")
    elif choice == "quit":
        print("Thanks for playing!")
    else:
        print("Invalid choice")
```

**This keeps showing the menu until** the user types "quit".

---

## While Loops vs If Statements

### If Statement (Runs Once)

```python
score = 50

if score < 100:
    print("Keep playing")  # Prints once
```

### While Loop (Repeats)

```python
score = 50

while score < 100:
    print("Keep playing")  # Prints repeatedly
    score = score + 10     # Must update score!
```

**Key difference:**
- `if` checks once and moves on
- `while` checks repeatedly and keeps running

---

## Try It Yourself (Before Class)

Run this code and observe the output:

```python
number = 1

while number <= 10:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    number = number + 1

print("Finished checking numbers!")
```

**Expected output:** It will print whether each number from 1 to 10 is even or odd.

**Try modifying:**
1. Change `number <= 10` to `number <= 3` - what happens?
2. Change `number = number + 1` to `number = number + 2` - what happens?
3. Comment out the `number = number + 1` line - what happens? (Stop it with Ctrl+C!)

---

## Common While Loop Patterns

### Pattern 1: Counting

```python
count = 0
while count < 5:
    print("Hello")
    count += 1  # += is shorthand for count = count + 1
```

### Pattern 2: User Input Until Valid

```python
age = -1
while age < 0 or age > 120:
    age = int(input("Enter your age (0-120): "))
```

### Pattern 3: Keep Running Until Command

```python
command = ""
while command != "stop":
    command = input("Enter command (type 'stop' to quit): ")
    print(f"You entered: {command}")
```

---

## Warning: Infinite Loops

If you accidentally create an infinite loop, your program will hang. Here's what to do:

**How to stop a stuck program:**
- Press `Ctrl + C` (or `Cmd + C` on Mac) in the terminal
- Or close the terminal window

**Common infinite loop mistake:**

```python
x = 5
while x > 0:
    print("Hello")
    # Forgot to change x!
```

This will print "Hello" forever because `x` is always 5, and 5 > 0 is always True.

---

## Key Takeaways

Before class, remember:
1. **While loops repeat** - as long as condition is True
2. **Condition checked first** - before each iteration
3. **Must update** - something in the loop must make condition False eventually
4. **Infinite loops are bad** - always make sure your condition can become False
5. **Great for user input** - when you don't know how many times to repeat

## Questions to Think About

Come to class ready to discuss:
- When would you use a while loop instead of just writing code multiple times?
- What happens if the condition is False from the start?
- How do you decide what condition to use for a while loop?

## What's Next?

In the live session, we'll:
- Write while loops for various scenarios
- Learn how to avoid infinite loops
- Use break and continue statements with while loops
- Build interactive programs with while loops
- Practice debugging loop problems

See you in class!
