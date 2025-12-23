# Post-class Quiz: Controlling While Loops Using Continue Statement

Test your understanding of the continue statement and how it differs from break.

---

## Q1: What does the continue statement do?

A) Exits the loop immediately
B) Skips the rest of the current iteration and goes to the next
C) Pauses the loop temporarily
D) Restarts the loop from the beginning

<details><summary>Answer</summary>
**B) Skips the rest of the current iteration and goes to the next**

**Explanation:** Continue jumps to the next iteration, skipping any code below it in the current iteration. The loop continues running.
</details>

---

## Q2: What is the output?
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

A) 1 2 4 5
B) 1 2 3 4 5
C) 1 2
D) 3 4 5

<details><summary>Answer</summary>
**A) 1 2 4 5**

**Explanation:** Loop iterates 1-5. When i=3, continue skips the print statement. Prints 1, 2, (skip 3), 4, 5.
</details>

---

## Q3: What is the difference between break and continue?

A) They do the same thing
B) Break exits the loop, continue skips to next iteration
C) Continue exits the loop, break skips to next iteration
D) Break is for while loops, continue is for for loops

<details><summary>Answer</summary>
**B) Break exits the loop, continue skips to next iteration**

**Explanation:**
- **break**: Terminates loop completely
- **continue**: Skips rest of current iteration, continues with next one
They work in both while and for loops.
</details>

---

## Q4: What is the output?
```python
count = 0
while count < 5:
    count += 1
    if count == 2:
        continue
    print(count)
```

A) 1 3 4 5
B) 1 2 3 4 5
C) 2 3 4 5
D) 1 3 4 5 6

<details><summary>Answer</summary>
**A) 1 3 4 5**

**Explanation:** Increments first (important!), then checks condition. When count=2, continue skips print. Prints 1, (skip 2), 3, 4, 5.
</details>

---

## Q5: What happens if you forget to increment before continue in a while loop?

A) Syntax error
B) Infinite loop
C) Loop runs once
D) Nothing, it's fine

<details><summary>Answer</summary>
**B) Infinite loop**

**Explanation:** If increment is after continue, it never executes when continue happens. Counter never changes, condition stays True forever = infinite loop!

**Wrong:**
```python
while count < 5:
    if count == 3:
        continue  # Infinite loop here!
    count += 1
```

**Right:**
```python
while count < 5:
    count += 1  # Increment first!
    if count == 3:
        continue
```
</details>

---

## Q6: How many times does the print execute?
```python
for num in [1, 2, 3, 4, 5]:
    if num % 2 == 0:
        continue
    print(num)
```

A) 2 times
B) 3 times
C) 4 times
D) 5 times

<details><summary>Answer</summary>
**B) 3 times**

**Explanation:** Skips even numbers (2, 4) with continue. Prints odd numbers: 1, 3, 5 = 3 times.
</details>

---

## Q7: Can you use continue in a for loop?

A) No, only in while loops
B) Yes, in both while and for loops
C) Yes, but only in Python 3
D) No, continue is not valid in Python

<details><summary>Answer</summary>
**B) Yes, in both while and for loops**

**Explanation:** Continue works identically in BOTH while and for loops. It skips to the next iteration in either type.
</details>

---

## Q8: What is the output?
```python
numbers = [5, -2, 8, -1, 3]
total = 0

for num in numbers:
    if num < 0:
        continue
    total += num

print(total)
```

A) 13
B) 16
C) 18
D) 11

<details><summary>Answer</summary>
**B) 16**

**Explanation:** Skip negative numbers (-2, -1). Sum positives: 5 + 8 + 3 = 16. Continue prevents negatives from being added.
</details>

---

## Q9: What happens with nested loops and continue?

A) Continue affects all nested loops
B) Continue only affects the innermost loop
C) Continue causes an error in nested loops
D) Continue affects the outermost loop only

<details><summary>Answer</summary>
**B) Continue only affects the innermost loop**

**Explanation:** Just like break, continue only affects the closest enclosing loop. To skip iteration in outer loop, you need logic there too.
</details>

---

## Q10: What is the output?
```python
for i in range(5):
    if i == 0:
        continue
    if i == 3:
        break
    print(i)
```

A) 1 2
B) 1 2 3
C) 0 1 2
D) 1 2 4

<details><summary>Answer</summary>
**A) 1 2**

**Explanation:**
- i=0: continue (skip print)
- i=1: print 1
- i=2: print 2
- i=3: break (exit loop)
Never reaches i=4. Output: 1, 2.
</details>

---

## Q11: Which pattern is cleaner for filtering?
```python
# Option A
for item in items:
    if valid(item):
        process(item)

# Option B
for item in items:
    if not valid(item):
        continue
    process(item)
```

A) Option A is always better
B) Option B is cleaner for complex processing
C) They're identical
D) Option A is faster

<details><summary>Answer</summary>
**B) Option B is cleaner for complex processing**

**Explanation:** When process(item) is many lines, Option B (early continue) avoids deep nesting. Check invalid case first, skip it, then all processing code stays at top level.
</details>

---

## Q12: What is the output?
```python
word = "hello"
for char in word:
    if char in "aeiou":
        continue
    print(char, end="")
```

A) hello
B) eo
C) hll
D) aeiou

<details><summary>Answer</summary>
**C) hll**

**Explanation:** Skips vowels (e, o) with continue. Prints consonants only: h, l, l.
</details>

---

## Q13: Can a loop have multiple continue statements?

A) No, only one continue per loop
B) Yes, any number of continues
C) Only two continues maximum
D) Continues must be in else clause

<details><summary>Answer</summary>
**B) Yes, any number of continues**

**Explanation:** Multiple continues work like multiple filters. Each one skips different unwanted cases. First one reached executes.

```python
for num in numbers:
    if num == 0:
        continue  # Skip zeros
    if num < 0:
        continue  # Skip negatives
    # Process positive non-zero
```
</details>

---

## Q14: What's the purpose of continue in data processing?

A) Speed up loops
B) Filter out invalid/unwanted data
C) Stop processing when done
D) Count iterations

<details><summary>Answer</summary>
**B) Filter out invalid/unwanted data**

**Explanation:** Continue is perfect for data cleaning - skip error values, outliers, empty entries, etc. Process only valid data without stopping the loop.
</details>

---

## Q15: What is the output?
```python
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(f"{i},{j}", end=" ")
    print()
```

A) 0,0 0,2 1,0 1,2 2,0 2,2
B) 0,0 1,0 2,0
C) All combinations from 0,0 to 2,2
D) 0,1 1,1 2,1

<details><summary>Answer</summary>
**A) 0,0 0,2 1,0 1,2 2,0 2,2**

**Explanation:** For each i (0, 1, 2), inner loop prints j=0 and j=2, skips j=1. Continue only affects inner loop, outer continues normally.

Output (with newlines from print()):
```
0,0 0,2
1,0 1,2
2,0 2,2
```
</details>

---

## Score Interpretation

- **13-15 correct**: Excellent! You've mastered the continue statement.
- **10-12 correct**: Good work! Review continue vs break and increment placement.
- **7-9 correct**: Fair. Practice more with filtering patterns and nested loops.
- **Below 7**: Review the lesson materials on continue statement usage.

## Key Concepts to Remember

1. **Skip iteration**: Continue skips rest of current iteration
2. **Loop continues**: Unlike break, loop keeps running
3. **Increment first**: In while loops, update before continue
4. **Works in all loops**: while, for, nested
5. **Innermost only**: Continue affects closest loop
6. **Multiple continues**: Can have several filters
7. **Data cleaning**: Perfect for skipping invalid data
8. **Vs break**: Continue skips, break exits
9. **No nesting**: Early continue avoids deep if nesting
10. **Common pattern**: Check bad case, continue, main logic
