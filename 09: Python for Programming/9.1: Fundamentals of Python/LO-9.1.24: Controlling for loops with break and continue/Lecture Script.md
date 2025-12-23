# Lecture Script: Controlling For Loops with Break and Continue

**Duration:** 20-25 minutes
**Learning Objective:** Students will be able to use break and continue statements to control for loop execution flow.

---

## Hook (2 minutes)

"Imagine you're looking for your keys in a messy room. You check drawer after drawer. What happens when you find them? Do you keep searching every remaining drawer? Of course not! You stop immediately—you **break** out of the search.

Now imagine you're packing for a trip, going through your clothes. Some items are dirty, so you skip them and move to the next item—you **continue** with the next piece of clothing.

In programming, we have the exact same concepts! **Break** stops a loop when we've found what we need. **Continue** skips unwanted items and moves to the next one. Today, we'll learn how to control for loops using these powerful statements."

---

## Section 1: The Break Statement (6 minutes)

### Concept Introduction

"The `break` statement immediately exits a loop, no matter how many iterations are left. It's like an emergency exit for your loop."

### Basic Syntax

```python
for item in collection:
    if condition:
        break  # Exit loop immediately
    # This code runs only if break doesn't execute
```

### Example 1: Finding First Even Number

```python
numbers = [1, 3, 5, 8, 9, 11]

for num in numbers:
    if num % 2 == 0:
        print(f"Found first even: {num}")
        break
    print(f"Checking {num}")
```

**Output:**
```
Checking 1
Checking 3
Checking 5
Found first even: 8
```

**Key Point:** Notice that 9 and 11 are never checked! Once break executes, the loop stops completely.

### Example 2: Search with Target

"Let's search for a specific name in a list:"

```python
names = ["Alice", "Bob", "Charlie", "David"]
target = "Charlie"

for name in names:
    if name == target:
        print(f"Found {target}!")
        break
    print(f"Not {name}, keep searching...")
```

**Output:**
```
Not Alice, keep searching...
Not Bob, keep searching...
Found Charlie!
```

**Discussion Point:** "Why is this more efficient than checking all names? Because we stop as soon as we find what we're looking for!"

---

## Section 2: The Continue Statement (6 minutes)

### Concept Introduction

"The `continue` statement skips the rest of the current iteration and immediately moves to the next one. It's like saying 'skip this, move to the next.'"

### Basic Syntax

```python
for item in collection:
    if condition:
        continue  # Skip rest of this iteration
    # This code is skipped when continue executes
```

### Example 1: Printing Only Evens

```python
for num in range(1, 11):
    if num % 2 != 0:  # If odd
        continue      # Skip it
    print(num)        # Only evens reach here
```

**Output:**
```
2
4
6
8
10
```

**Key Point:** When continue executes, the print statement is skipped, but the loop continues with the next number.

### Example 2: Filtering Negative Numbers

"Let's print only positive numbers from a list:"

```python
numbers = [5, -2, 8, -7, 3, -1, 9]

for num in numbers:
    if num < 0:
        continue  # Skip negatives
    print(num)
```

**Output:**
```
5
8
3
9
```

**Discussion Point:** "Continue is perfect for filtering! It's cleaner than wrapping everything in an else block."

---

## Section 3: Break vs Continue (3 minutes)

### Visual Comparison

```python
# BREAK - Exits the entire loop
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0 1 2

# CONTINUE - Skips to next iteration
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0 1 2 4
```

**Key Difference:**
- **Break:** Loop stops completely, nothing after 3
- **Continue:** Loop skips 3, but continues with 4

### When to Use Each

| Scenario | Use | Example |
|----------|-----|---------|
| Finding first match | Break | Search for item |
| Processing until condition | Break | Sum until negative |
| Filtering items | Continue | Skip invalid data |
| Skipping special cases | Continue | Skip empty strings |

---

## Section 4: The For-Else Clause (4 minutes)

### Concept Introduction

"Python has a unique feature: the `else` clause in for loops. It executes ONLY if the loop completes without encountering a break."

### Syntax

```python
for item in collection:
    if condition:
        break
else:
    # This runs only if NO break occurred
    print("Loop completed normally")
```

### Example: Search with Not Found Handling

```python
# Search successful
numbers = [2, 4, 15, 8]
for num in numbers:
    if num > 10:
        print(f"Found large number: {num}")
        break
else:
    print("No large number found")

# Output: Found large number: 15

# Search unsuccessful
numbers = [2, 4, 6, 8]
for num in numbers:
    if num > 10:
        print(f"Found large number: {num}")
        break
else:
    print("No large number found")

# Output: No large number found
```

**Key Point:** The else block is a clean way to handle "not found" cases without using flag variables!

### Real-World Application

```python
# Check if password is valid
passwords = ["abc", "pass", "hello"]
min_length = 8

for password in passwords:
    if len(password) >= min_length:
        print(f"Valid password: {password}")
        break
else:
    print("No valid passwords found")

# Output: No valid passwords found
```

---

## Section 5: Combining Break and Continue (4 minutes)

### Using Both Together

"You can use both break and continue in the same loop, but they serve different purposes."

### Example: Skip Some, Stop on Condition

```python
# Print numbers 1-30, skip multiples of 3, stop at first multiple of 17
for num in range(1, 31):
    if num % 17 == 0:  # Check break first
        print(f"Stopping at {num}")
        break
    if num % 3 == 0:   # Then check continue
        continue       # Skip multiples of 3
    print(num, end=' ')
```

**Output:**
```
1 2 4 5 7 8 10 11 13 14 16
Stopping at 17
```

**Important:** Order matters! Check break conditions before continue conditions.

### Example: Processing with Validation

```python
# Process positive numbers, skip zeros, stop at negative
numbers = [5, 10, 0, 15, 0, 20, -5, 25]
total = 0

for num in numbers:
    if num < 0:
        print(f"Found negative ({num}), stopping")
        break
    if num == 0:
        continue  # Skip zeros
    total += num
    print(f"Added {num}, total: {total}")

print(f"Final total: {total}")
```

**Output:**
```
Added 5, total: 5
Added 10, total: 15
Added 15, total: 30
Added 20, total: 50
Found negative (-5), stopping
Final total: 50
```

---

## Section 6: Nested Loops (3 minutes)

### Important Rule

"In nested loops, break and continue only affect the innermost loop they're in."

### Example: 2D Search

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
target = 5
found = False

for row in matrix:
    for num in row:
        if num == target:
            print(f"Found {target}!")
            found = True
            break  # Only exits inner loop
    if found:
        break  # Exits outer loop

# Output: Found 5!
```

**Key Point:** To break out of both loops, we need a flag variable.

### Alternative: Function with Return

```python
def find_in_matrix(matrix, target):
    for row in matrix:
        for num in row:
            if num == target:
                return True  # Exits function (both loops)
    return False

matrix = [[1, 2, 3], [4, 5, 6]]
print(find_in_matrix(matrix, 5))  # True
```

**Discussion:** "Using a function with return is often cleaner than using flags!"

---

## Practice Problems (2 minutes)

### Problem 1 (Quick)

"What does this print?"

```python
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i, end=' ')
```

**Answer:** 0 1 3

**Explanation:** Skips 2 (continue), stops at 4 (break)

### Problem 2 (Quick)

"Will else execute here?"

```python
for i in range(3):
    if i == 10:
        break
else:
    print("Completed")
```

**Answer:** Yes! "Completed" prints because break never executes (i never equals 10).

---

## Common Mistakes to Avoid (2 minutes)

### Mistake 1: Unreachable Code After Break

```python
# BAD
for num in numbers:
    if num == 5:
        break
        print("Found!")  # This NEVER runs!
```

### Mistake 2: Using Return Instead of Break

```python
# BAD (unless in a function)
for num in numbers:
    if num == 5:
        return  # Error if not in function!

# GOOD
for num in numbers:
    if num == 5:
        break  # Correct!
```

### Mistake 3: Forgetting For-Else Behavior

```python
# People often think else always runs
for num in [1, 2, 3]:
    if num == 2:
        break
else:
    print("This doesn't print!")  # Else skipped because break occurred
```

---

## Real-World Applications (1 minute)

### Where We Use These

1. **Search operations:** Finding items in collections
2. **Validation:** Checking data quality, stopping on first error
3. **Processing limits:** Stop when threshold reached
4. **Filtering data:** Skip invalid/unwanted items
5. **Menu systems:** Break on "exit" command
6. **Game loops:** Break when game ends
7. **File processing:** Skip corrupted records, continue with rest

---

## Wrap-Up (1 minute)

### Key Takeaways

**Break:**
- Exits loop immediately
- Use for searches, early exits, thresholds
- Prevents for-else from executing

**Continue:**
- Skips to next iteration
- Use for filtering, skipping invalid data
- Loop continues after continue

**For-Else:**
- Runs only if loop completes without break
- Clean way to handle "not found" cases
- Eliminates need for flag variables

### Quick Reference

```python
# Break: Exit early
for item in items:
    if found_what_i_need:
        break

# Continue: Skip some
for item in items:
    if skip_this:
        continue
    process(item)

# For-else: Handle completion
for item in items:
    if item == target:
        break
else:
    print("Not found")
```

---

## Homework Preview

"For homework, you'll practice:
1. Finding first occurrences with break
2. Filtering with continue
3. Search operations with for-else
4. Combining both in the same loop
5. Working with nested loops

Remember: break stops, continue skips, else detects completion!"

---

## Q&A (Time permitting)

**Common Questions:**

**Q: Can I use multiple breaks in one loop?**
A: Yes, but only the first one encountered will execute.

**Q: What if I want to break multiple nested loops?**
A: Use a flag variable or put code in a function and use return.

**Q: Is continue always better than using if-else?**
A: Not always, but it often makes code cleaner and less nested.

**Q: Can I break from a function?**
A: Use `return` to exit a function, not `break`.

---

## Additional Examples (If Time Permits)

### Example: First Duplicate Finder

```python
numbers = [1, 2, 3, 4, 2, 5]
seen = set()

for num in numbers:
    if num in seen:
        print(f"First duplicate: {num}")
        break
    seen.add(num)
else:
    print("No duplicates")
```

### Example: Skip Vowels

```python
text = "Hello World"

for char in text:
    if char.lower() in 'aeiou':
        continue
    print(char, end='')

# Output: Hll Wrld
```

### Example: Password Validator

```python
passwords = ["short", "toolong123456", "justright"]

for pwd in passwords:
    if len(pwd) < 6:
        print(f"{pwd}: too short")
        continue
    if len(pwd) > 10:
        print(f"{pwd}: too long")
        continue
    print(f"{pwd}: valid!")
    break
else:
    print("No valid password found")
```

---

## Teaching Tips

### For Instructors:

1. **Use Physical Analogies:**
   - Break = emergency exit
   - Continue = skip button
   - For-else = "if I made it here without leaving early"

2. **Live Coding:**
   - Demonstrate each concept with live code
   - Show what happens when you comment out break/continue
   - Use print statements to show flow

3. **Common Confusion:**
   - Students often confuse break with return
   - Emphasize for-else only runs without break
   - Show that continue doesn't exit, just skips

4. **Practice:**
   - Start with simple examples
   - Build to combining break and continue
   - End with nested loops (advanced)

5. **Debugging:**
   - Show how to trace execution with print
   - Demonstrate step-through debugging
   - Explain how to identify infinite loops

### Engagement Strategies:

- Ask students to predict output before running code
- Have students explain when they'd use break vs continue
- Pair programming: one writes condition, other writes loop control
- Challenge: rewrite if-else as continue statements

---

## Assessment Checkpoints

### Understanding Check 1 (After Section 2)

"Quick poll: When does break execute?"
- A) At the end of every iteration
- B) Immediately when its condition is met ✓
- C) After the loop completes
- D) Only in while loops

### Understanding Check 2 (After Section 3)

"What's the difference between break and continue?"
- Ask students to explain in their own words
- Look for: "break exits, continue skips"

### Understanding Check 3 (After Section 4)

"When does for-else run?"
- Common wrong answer: "always after the loop"
- Correct: "only when loop completes without break"

---

## Extension Activities

### For Advanced Students:

1. **Challenge:** Write a prime number finder using break
2. **Optimize:** Convert nested if-else to continue statements
3. **Refactor:** Improve code by using for-else instead of flags
4. **Create:** Build a menu system with break on "quit"

### Real-World Project Ideas:

1. **Password strength checker** (continue for invalid, break for valid)
2. **Search tool** (break on first match, for-else for not found)
3. **Data validator** (continue to skip bad rows, break on critical error)
4. **Game loop** (break when player wins/quits)

---

## Summary Table

| Statement | Purpose | When to Use | Example |
|-----------|---------|-------------|---------|
| `break` | Exit loop immediately | Found what you need, hit a limit | Search, threshold detection |
| `continue` | Skip to next iteration | Filter unwanted items | Skip invalid data, filter by condition |
| `for-else` | Code after successful completion | Detect if search failed | "Not found" handling |

---

## Code Snippets for Reference

```python
# Pattern 1: Search
for item in collection:
    if item == target:
        print("Found!")
        break
else:
    print("Not found")

# Pattern 2: Filter
for item in collection:
    if not valid(item):
        continue
    process(item)

# Pattern 3: Combined
for item in collection:
    if critical_error(item):
        break  # Stop everything
    if minor_issue(item):
        continue  # Skip this one
    process(item)

# Pattern 4: Nested with flag
found = False
for row in matrix:
    for item in row:
        if item == target:
            found = True
            break
    if found:
        break
```

---

**End of Lecture**

"Great job today! You now know how to control loop flow with break and continue. Practice these patterns—they'll make your code more efficient and easier to read!"
