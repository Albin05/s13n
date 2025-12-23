# Pre-Read: Controlling While Loops Using Break Statement

## What You'll Learn
In this lesson, you'll learn how to use the `break` statement to exit a loop early, before the loop condition becomes False. This gives you more control over when your loops stop.

## Why This Matters
Sometimes you need to stop a loop immediately when something specific happens:
- A user types "quit" in a menu system
- You find what you're searching for in a list
- An error occurs and you need to stop processing
- A maximum number of attempts is reached

The `break` statement lets you exit the loop instantly, without waiting for the normal loop condition to become False.

---

## What is the Break Statement?

The **break statement** immediately exits the current loop, no matter what the loop condition says.

```python
while condition:
    # Some code
    if some_special_condition:
        break  # Exit loop right now!
    # More code
```

When Python hits `break`, it:
1. **Stops the loop immediately**
2. **Jumps to the first line after the loop**
3. **Doesn't check the loop condition again**

---

## Simple Example: Exit on Command

```python
while True:  # This would normally run forever!
    command = input("Enter command (or 'quit' to exit): ")

    if command == "quit":
        break  # Exit the loop

    print(f"You entered: {command}")

print("Program ended")
```

**Output example:**
```
Enter command (or 'quit' to exit): hello
You entered: hello
Enter command (or 'quit' to exit): test
You entered: test
Enter command (or 'quit' to exit): quit
Program ended
```

**Key point:** We used `while True` (infinite loop) but `break` stops it when needed.

---

## When to Use Break

### Use Case 1: Search and Stop

When you're looking for something and want to stop once you find it:

```python
numbers = [3, 7, 2, 9, 5, 11, 8]
target = 9
index = 0

while index < len(numbers):
    if numbers[index] == target:
        print(f"Found {target} at position {index}!")
        break  # No need to keep searching
    index += 1
```

### Use Case 2: Password Attempts

Limit the number of tries:

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == "secret123":
        print("Access granted!")
        break  # Correct password, exit loop

    attempts += 1
    remaining = max_attempts - attempts
    print(f"Wrong! {remaining} attempts remaining")

if password != "secret123":
    print("Account locked")
```

---

## Try It Yourself (Before Class)

Run this code:

```python
total = 0

while True:
    number = input("Enter a number (or 'done' to finish): ")

    if number == "done":
        break

    total += int(number)
    print(f"Running total: {total}")

print(f"Final total: {total}")
```

**Try:**
1. Enter a few numbers, then type "done"
2. What happens if you type "done" immediately?

---

## Key Takeaways

Before class, remember:
1. **break exits immediately** - stops the loop right away
2. **No condition check** - doesn't wait for normal loop condition
3. **Great with while True** - creates controlled infinite loops
4. **Common use cases** - search-and-stop, user input validation, menu systems

## What's Next?

In the live session, we'll:
- Practice using break in various scenarios
- Understand when to use break vs. changing the loop condition
- Build programs with controlled loop exits

See you in class!
