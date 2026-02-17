# Pre-Read: Controlling For Loops with Break and Continue

## Why Control Flow in For Loops?

For loops normally process every single item in a sequence. But real-world programs need **intelligent iteration**:
- **Search**: Stop once you find what you're looking for (don't waste time!)
- **Filtering**: Skip invalid/unwanted items but keep processing others
- **Validation**: Exit immediately when you detect an error

Break and continue give you this power - making loops smart, not just repetitive!

### Simple Analogy

Think of break and continue like **instructions to a mail carrier**:
- **Break**: "Stop delivering mail on this street" (emergency, road closed)
- **Continue**: "Skip this house but keep delivering to others" (no mailbox, dog loose)

The mail carrier doesn't blindly follow the route - they adapt based on conditions!

## What You'll Learn
In this lesson, you'll learn how to use `break` and `continue` statements with for loops to control loop execution. These work the same way as with while loops but are commonly used with for loops in Python.

## Why This Matters
Just like with while loops, you often need to:
- Exit a loop early when you find what you're looking for
- Skip certain items in a sequence
- Handle special cases without breaking your loop logic

Break and continue give you fine control over for loop execution.

---

## Quick Recap

**break** → Exit the loop completely
**continue** → Skip to the next iteration

These work identically in both while and for loops!

---

## Using Break in For Loops

### Example 1: Search and Stop

```python
numbers = [3, 7, 12, 9, 15, 2]

for num in numbers:
    if num > 10:
        print(f"Found number greater than 10: {num}")
        break  # Stop searching
    print(f"Checking {num}...")

# Output:
# Checking 3...
# Checking 7...
# Found number greater than 10: 12
```

### Example 2: Early Exit on Invalid Data

```python
scores = [95, 87, 102, 76, 88]  # 102 is invalid!

for score in scores:
    if score > 100:
        print("Error: Invalid score!")
        break
    print(f"Valid score: {score}")
```

---

## Using Continue in For Loops

### Example 1: Skip Specific Items

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

# Output: 1, 3, 5, 7, 9 (only odd numbers)
```

### Example 2: Filter and Process

```python
words = ["hello", "", "world", "", "python"]

for word in words:
    if word == "":
        continue  # Skip empty strings
    print(f"Word: {word}")

# Output:
# Word: hello
# Word: world
# Word: python
```

---

## Combining Break and Continue

```python
numbers = [5, -2, 10, -7, 15, 20, -3]

for num in numbers:
    if num < 0:
        continue  # Skip negative numbers

    if num > 15:
        print(f"Found large number: {num}")
        break  # Stop at first number > 15

    print(num)

# Output:
# 5
# 10
# 15
# Found large number: 20
```

---

## Real-World Example: Validating Passwords

```python
passwords = ["abc", "secure123", "xyz", "password456"]

for password in passwords:
    if len(password) < 5:
        continue  # Skip short passwords

    if "456" in password:
        print(f"Warning: Weak password found - {password}")
        break

    print(f"Valid: {password}")
```

---

## Try It Yourself (Before Class)

Run this code:

```python
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
```

**Questions:**
1. What numbers get printed?
2. Why is 5 skipped?
3. Why do numbers after 8 not print?

---

## Key Takeaways

Before class, remember:
1. **break in for loops** - exits the loop completely
2. **continue in for loops** - skips to next item in sequence
3. **Same as while loops** - behavior is identical
4. **Common patterns** - search-and-stop, filtering, validation
5. **Can combine** - use both in the same loop for complex logic

## What's Next?

In the live session, we'll:
- Practice break and continue with for loops
- Learn when to use each statement
- Build programs with sophisticated loop control
- Understand nested loops with break/continue

See you in class!
