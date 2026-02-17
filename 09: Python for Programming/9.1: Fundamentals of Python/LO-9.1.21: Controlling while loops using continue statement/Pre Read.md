# Pre-Read: Controlling While Loops Using Continue Statement

## What is Continue?

`continue` skips the **rest of the current loop iteration** and jumps to the next one. Unlike `break` (which exits the loop), continue just skips this round.

### Simple Analogy

Think of continue like **skipping a song**:
- Playing playlist → Don't like this song → Skip to next (continue) → Keep playing
- vs. Don't like playlist → Stop playback (break)

Or like **skipping questions on a test**:
- Question too hard? Skip it (continue), answer next question
- vs. Give up on test entirely (break)

## What You'll Learn
In this lesson, you'll learn how to use the `continue` statement to skip the rest of the current loop iteration and jump to the next one. This is useful when you want to skip certain cases but keep the loop running.

## Why This Matters
Sometimes you want to skip specific iterations without stopping the entire loop:
- Skipping invalid data while processing a list
- Filtering out unwanted items
- Ignoring certain conditions while continuing with others
- Processing only items that meet certain criteria

The `continue` statement gives you fine-grained control over individual loop iterations.

---

## What is the Continue Statement?

The **continue statement** skips the rest of the current iteration and immediately jumps to the next iteration of the loop.

```python
while condition:
    # Some code
    if skip_this_iteration:
        continue  # Skip rest of this iteration, go to next
    # This code is skipped when continue runs
```

**Key difference from break:**
- `break` → **Exit the entire loop**
- `continue` → **Skip to the next iteration**

---

## Simple Example: Skip Even Numbers

```python
number = 0

while number < 5:
    number += 1
    if number % 2 == 0:
        continue  # Skip even numbers
    print(number)
```

**Output:**
```
1
3
5
```

**What happens:**
1. number = 1 → not even → print 1
2. number = 2 → even → `continue` skips print
3. number = 3 → not even → print 3
4. number = 4 → even → `continue` skips print
5. number = 5 → not even → print 5

---

## When to Use Continue

### Use Case 1: Filtering Input

Skip invalid entries:

```python
total = 0
count = 0

while count < 5:
    value = input("Enter a positive number: ")

    if int(value) <= 0:
        print("Invalid! Must be positive.")
        continue  # Skip to next iteration, don't count this

    total += int(value)
    count += 1  # Only increment for valid input

print(f"Average: {total / count}")
```

### Use Case 2: Processing Only Specific Items

```python
names = ["Alice", "Bob", "", "Charlie", "", "David"]
index = 0

while index < len(names):
    name = names[index]
    index += 1

    if name == "":
        continue  # Skip empty names

    print(f"Hello, {name}!")
```

**Output:**
```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
Hello, David!
```

---

## Break vs Continue

### Break: Stop Everything

```python
for i in range(5):
    if i == 2:
        break  # Exit loop completely
    print(i)
# Output: 0, 1
```

### Continue: Skip One Iteration

```python
for i in range(5):
    if i == 2:
        continue  # Skip only i=2
    print(i)
# Output: 0, 1, 3, 4
```

---

## Real-World Example: Menu with Validation

```python
while True:
    print("\n1. Add item")
    print("2. View items")
    print("3. Quit")

    choice = input("Choose: ")

    if choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        continue  # Skip rest, show menu again

    if choice == "1":
        print("Adding item...")
    elif choice == "2":
        print("Viewing items...")
    elif choice == "3":
        print("Goodbye!")
        break
```

---

## Try It Yourself (Before Class)

Run this code:

```python
count = 0

while count < 10:
    count += 1

    if count % 3 == 0:
        continue

    print(count)
```

**Questions:**
1. What numbers get printed?
2. What numbers are skipped?
3. Try changing `count % 3 == 0` to `count == 5` - what happens?

---

## Key Takeaways

Before class, remember:
1. **continue skips to next iteration** - doesn't exit loop
2. **Rest of iteration is skipped** - code after continue doesn't run
3. **Loop keeps running** - unlike break which exits
4. **Great for filtering** - skip unwanted cases
5. **Loop condition still checked** - after each iteration

## What's Next?

In the live session, we'll:
- Practice using continue in various scenarios
- Learn when to use continue vs break
- Combine continue with break for complex logic
- Build programs with sophisticated loop control

See you in class!
