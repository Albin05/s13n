# Lecture Script: Controlling While Loops Using Continue Statement

**Duration:** 20-25 minutes
**Learning Objective:** Students will be able to use the continue statement to skip specific iterations while keeping the loop running.

---

## [0:00-0:02] Hook (2 minutes)

**Open with a relatable scenario:**

> "Imagine you're a teacher grading homework. You have a stack of 30 submissions. But 5 of them are blank - students didn't submit. Do you waste time grading blank papers? No! You SKIP them and move to the next one. That's what `continue` does - it skips the current item and moves to the next!"

**Interactive question:**
"Have you ever been reading a book and skipped a boring chapter? You didn't stop reading - you just jumped ahead!"

**The connection:**
> "Exactly! The `continue` statement says 'skip this one, but keep going.' Unlike `break` which stops the loop completely, `continue` just jumps to the next iteration."

**Live demo - show the difference:**
```python
# WITH continue - skip evens, keep going
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip evens
    print(num)

print("Loop finished!")
```

**Run it:**
```
1
3
5
7
9
Loop finished!
```

**Point out:**
> "See? It skipped 2, 4, 6, 8, 10 but the loop KEPT RUNNING. All odds printed, then finished normally!"

**Contrast with break:**
```python
# WITH break - stop completely
for num in range(1, 11):
    if num % 2 == 0:
        break  # Stop at first even
    print(num)

print("Loop finished!")
```

**Output:**
```
1
Loop finished!
```

> "Break STOPPED the loop at 2. Continue would have skipped 2 and kept going. BIG difference!"

---

## [0:02-0:08] Main Concept: Continue Basics (6 minutes)

### Part 1: What is Continue? (2 minutes)

**Explain:**
> "The `continue` statement skips the REST of the current iteration and jumps to the NEXT iteration. The loop doesn't exit - it just moves on."

**Syntax:**
```python
while condition:
    # code
    if skip_condition:
        continue  # Jump to next iteration NOW
    # This code is skipped if continue executes
    # more code
```

**Flow diagram on board:**
```
Loop Start
    ↓
Check condition? → False → Exit Loop
    ↓ True
Execute code
    ↓
Continue? → Yes → Jump to Loop Start (skip rest)
    ↓ No
Execute more code
    ↓
Jump to Loop Start
```

**Live code - Simple example:**
```python
count = 0

while count < 5:
    count += 1

    if count == 3:
        print(f"Skipping {count}")
        continue

    print(f"Processing {count}")

print("Done!")
```

**Output:**
```
Processing 1
Processing 2
Skipping 3
Processing 4
Processing 5
Done!
```

**Trace through:**
- count=1: Not 3, print "Processing 1"
- count=2: Not 3, print "Processing 2"
- count=3: IS 3, print "Skipping 3", **CONTINUE** (skip rest)
- count=4: Not 3, print "Processing 4"
- count=5: Not 3, print "Processing 5"
- Loop ends, print "Done!"

**CRITICAL WARNING:**
> "WATCH OUT! In while loops, increment BEFORE continue, otherwise infinite loop!"

```python
# WRONG - Infinite loop!
count = 0
while count < 5:
    if count == 3:
        continue  # Count never increments!
    count += 1
    print(count)
```

```python
# RIGHT - Increment first
count = 0
while count < 5:
    count += 1  # Always increment
    if count == 3:
        continue
    print(count)
```

### Part 2: Continue as Filter (2 minutes)

**Explain the pattern:**
> "Continue is perfect for FILTERING. Check what you DON'T want, skip it. Everything else gets processed."

**Live code:**
```python
numbers = [5, -3, 8, -1, 12, -7, 4]

print("Positive numbers only:")
for num in numbers:
    if num < 0:
        continue  # Skip negatives
    print(num)
```

**Output:**
```
Positive numbers only:
5
8
12
4
```

**Compare without continue:**
```python
# Without continue - nested if
for num in numbers:
    if num >= 0:  # Must check positive
        print(num)
```

**Show why continue is cleaner:**
```python
# With continue - check what to skip
for num in numbers:
    if num < 0:
        continue
    # All code here is for valid items
    print(num)
    # More processing...
    # Even more...
```

**Emphasize:**
> "Continue avoids deep nesting. Check bad case first, skip it. Main logic stays at top level - cleaner code!"

### Part 3: Multiple Filters (2 minutes)

**Show multiple continue statements:**
```python
numbers = [0, 5, -3, 10, 15, -2, 20, 0, 8]
total = 0
count = 0

for num in numbers:
    if num == 0:
        continue  # Skip zeros

    if num < 0:
        continue  # Skip negatives

    # Only positive non-zero numbers reach here
    total += num
    count += 1

print(f"Sum: {total}")  # 5 + 10 + 15 + 20 + 8 = 58
print(f"Count: {count}")  # 5 numbers
```

**Output:**
```
Sum: 58
Count: 5
```

**Explain:**
> "Multiple continues = multiple filters. Each one says 'skip this type.' Only items passing ALL filters get processed."

---

## [0:08-0:14] Pattern: Continue vs Break (6 minutes)

### Part 1: Key Differences (3 minutes)

**Create comparison table on board:**

| Feature | Continue | Break |
|---------|----------|-------|
| **What it does** | Skip this iteration | Exit entire loop |
| **Loop continues?** | YES | NO |
| **When to use** | Filter items | Find and stop |
| **Example** | Skip invalid data | Stop when found |

**Side-by-side demo:**
```python
print("=== CONTINUE Demo ===")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\n=== BREAK Demo ===")
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

**Output:**
```
=== CONTINUE Demo ===
1
2
4
5

=== BREAK Demo ===
1
2
```

**Explain:**
> "Continue skipped 3, but printed 4 and 5. Break stopped AT 3, never checked 4 or 5. Continue is selective, break is final!"

### Part 2: Using Both Together (3 minutes)

**Show real-world example:**
```python
print("Enter numbers to sum (0 to quit):")
total = 0
count = 0

while True:
    num_str = input("Number: ")

    # Break on exit command
    if num_str == "0":
        print("Exiting...")
        break

    # Continue on invalid input
    if not num_str.lstrip('-').isdigit():
        print("Invalid! Please enter a number")
        continue

    # Valid number - process it
    num = int(num_str)
    total += num
    count += 1
    print(f"Running total: {total}")

print(f"\nFinal total: {total}")
print(f"Numbers entered: {count}")
```

**Test interaction:**
```
Enter numbers to sum (0 to quit):
Number: 10
Running total: 10
Number: abc
Invalid! Please enter a number
Number: 20
Running total: 30
Number: xyz
Invalid! Please enter a number
Number: 15
Running total: 45
Number: 0
Exiting...

Final total: 45
Numbers entered: 3
```

**Explain:**
> "Break for EXIT. Continue for SKIP. Invalid inputs don't count or affect total - they're just ignored. Perfect combination!"

---

## [0:14-0:18] Advanced: Common Patterns (4 minutes)

### Part 1: Data Cleaning (2 minutes)

**Real-world example:**
```python
# Sensor data with errors
temperatures = [22.5, -999, 23.1, -999, 21.8, 24.2]
valid_temps = []

for temp in temperatures:
    if temp == -999:  # Error reading
        continue
    valid_temps.append(temp)

avg = sum(valid_temps) / len(valid_temps)
print(f"Valid temperatures: {valid_temps}")
print(f"Average: {avg:.1f}°C")
```

**Output:**
```
Valid temperatures: [22.5, 23.1, 21.8, 24.2]
Average: 22.9°C
```

**Explain:**
> "Sensor errors marked as -999. Continue skips them. We calculate average on CLEAN data only. This is data cleaning!"

### Part 2: Nested Loops (2 minutes)

**Show continue in nested structure:**
```python
print("Multiplication table (skip multiples of 5):")

for i in range(1, 4):
    for j in range(1, 6):
        product = i * j
        if product % 5 == 0:
            continue  # Skip multiples of 5
        print(f"{i} × {j} = {product}")
    print()  # Blank line after each row
```

**Output:**
```
Multiplication table (skip multiples of 5):
1 × 1 = 1
1 × 2 = 2
1 × 3 = 3
1 × 4 = 4

2 × 1 = 2
2 × 2 = 4
2 × 3 = 6
2 × 4 = 8

3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
3 × 4 = 12
```

**Point out:**
> "Continue only affects INNERMOST loop. Skipped 1×5, 2×5, 3×5 but outer loop kept going. Same as break - affects closest loop only."

---

## [0:18-0:22] Practice Time (4 minutes)

**Exercise 1: Filter Strings (1.5 minutes)**
> "Print only strings longer than 3 characters. Use continue to skip short ones."

```python
# Given
words = ["cat", "elephant", "dog", "giraffe", "ant", "bear"]

# Solution
for word in words:
    if len(word) <= 3:
        continue
    print(word)
```

**Output:**
```
elephant
giraffe
bear
```

**Exercise 2: Sum Non-Zeros (2 minutes)**
> "Sum all numbers except zeros from this list."

```python
# Given
numbers = [5, 0, 10, 0, 15, 0, 20]

# Solution
total = 0
for num in numbers:
    if num == 0:
        continue
    total += num

print(f"Sum (no zeros): {total}")  # 50
```

**Walk around and check:**
- Students forgetting to increment before continue in while
- Confusing continue with break
- Not understanding continue skips REST of iteration

---

## [0:22-0:25] Wrap-up and Key Takeaways (3 minutes)

**Summarize the main points:**

1. **Continue skips iteration**: Jump to next, don't exit loop
2. **Break vs Continue**: Break exits, continue skips
3. **Filter pattern**: Check bad case, continue, main logic after
4. **Multiple filters**: Multiple continues for complex filtering
5. **Increment first**: In while loops, update before continue
6. **Works in nested**: Only affects innermost loop
7. **Combine with break**: Both together = powerful control

**Visual on board:**
```python
# Continue pattern
for item in items:
    if unwanted(item):
        continue  # Skip to next
    # Process wanted items
    do_something(item)

# vs Break pattern
for item in items:
    if found(item):
        break  # Stop searching
    # Keep looking
```

**Common use cases:**
- ✅ Skip invalid data (validation)
- ✅ Filter collections (data cleaning)
- ✅ Skip errors in processing
- ✅ Ignore certain values in calculations
- ✅ Process only specific items

**Common mistakes:**
- ❌ Not incrementing before continue (infinite loop in while)
- ❌ Using continue when break is needed
- ❌ Deep nesting instead of early continue
- ❌ Confusing which loop continue affects

**Real-world reminder:**
> "Continue is your 'skip button.' Processing files? Skip corrupted ones. Reading data? Skip empty rows. Validating input? Skip invalid entries. Keep the loop running, just skip the junk!"

**Preview next lesson:**
> "Next: for loops! A different way to iterate - cleaner syntax for counting and sequences. Break and continue work the same in for loops!"

**Final check question:**
"If you have a loop and want to skip even numbers but keep processing odd numbers, which do you use: break or continue?"

**Expected answer:** "Continue! Break would stop at the first even number. Continue skips evens but keeps processing odds."

---

## Teaching Tips

1. **Emphasize the difference** - Continue vs break confusion is common
2. **Demonstrate infinite loops** - Show what happens without proper increment
3. **Use visual diagrams** - Flow charts help
4. **Contrast patterns** - Show with and without continue
5. **Real examples** - Data cleaning, validation are relatable
6. **Practice both** - Use break and continue in same program

## Common Student Questions

**Q: "Can I use continue in a while loop?"**
A: "Yes! But ALWAYS increment/update BEFORE continue, or infinite loop!"

**Q: "What if I have 3 nested loops?"**
A: "Continue only skips the current iteration of the INNERMOST loop you're in."

**Q: "Is it better to use continue or else?"**
A: "Continue is cleaner when you have multiple filters or long processing code. Else works for simple cases."

**Q: "Can I have multiple continue statements?"**
A: "Absolutely! Each one filters out a different unwanted case. First one reached executes."

**Q: "Does continue work in for loops too?"**
A: "Yes! Continue works in BOTH while and for loops exactly the same way."

---

## Additional Examples (if time permits)

### Skip Vowels
```python
text = "hello"
for char in text:
    if char in "aeiou":
        continue
    print(char)  # Prints: h l l
```

### Count Valid Entries
```python
values = [10, -5, 20, 0, 15, -3]
count = 0

for val in values:
    if val <= 0:
        continue
    count += 1

print(f"Positive count: {count}")  # 3
```

### Process Menu
```python
while True:
    choice = input("Menu (1/2/3/quit): ")

    if choice == "quit":
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        continue

    print(f"Processing option {choice}")
```
