# Post-class Quiz: Controlling While Loops Using Break Statement

Test your understanding of the break statement and its use in controlling loop flow.

---

## Q1: What does the break statement do?

A) Pauses the loop temporarily
B) Exits the loop immediately
C) Skips to the next iteration
D) Restarts the loop from the beginning

<details><summary>Answer</summary>
**B) Exits the loop immediately**

**Explanation:** The break statement terminates the loop right away, regardless of the loop condition. Execution continues after the loop.
</details>

---

## Q2: What is the output?
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

A) 0 1 2
B) 0 1 2 3
C) 0 1 2 3 4
D) 3 4

<details><summary>Answer</summary>
**A) 0 1 2**

**Explanation:** Loop prints 0, 1, 2. When i=3, the break statement executes, exiting the loop before printing 3.
</details>

---

## Q3: Can you use break in a for loop?

A) No, only in while loops
B) Yes, in both while and for loops
C) Yes, but only in Python 3
D) No, break is not a Python keyword

<details><summary>Answer</summary>
**B) Yes, in both while and for loops**

**Explanation:** The break statement works in ANY type of loop - while, for, or nested combinations of both.
</details>

---

## Q4: What happens with nested loops and break?

A) Break exits all nested loops
B) Break only exits the innermost loop
C) Break causes an error in nested loops
D) Break exits the outermost loop only

<details><summary>Answer</summary>
**B) Break only exits the innermost loop**

**Explanation:** Break exits the closest enclosing loop. To exit outer loops, you need a flag variable and check it in the outer loop.
</details>

---

## Q5: What is the output?
```python
count = 0
while True:
    count += 1
    if count == 3:
        break
    print(count)
```

A) 1 2
B) 1 2 3
C) Infinite loop
D) 0 1 2

<details><summary>Answer</summary>
**A) 1 2**

**Explanation:** Prints 1, then 2. When count=3, breaks before printing. `while True` creates infinite loop, but break provides exit.
</details>

---

## Q6: When does the else clause of a loop execute?

A) Always after the loop
B) Only if break was used
C) Only if loop completed without break
D) Never

<details><summary>Answer</summary>
**C) Only if loop completed without break**

**Explanation:** Loop-else runs if the loop finishes normally (condition becomes False). If break executes, else is skipped.
</details>

---

## Q7: What is the output?
```python
for num in [1, 3, 5, 6, 7]:
    if num % 2 == 0:
        print("Found even")
        break
else:
    print("No even numbers")
```

A) Found even
B) No even numbers
C) Found even<br>No even numbers
D) Error

<details><summary>Answer</summary>
**A) Found even**

**Explanation:** Found 6 (even), printed "Found even", broke. Since break executed, else clause is skipped.
</details>

---

## Q8: Is `while True:` with break a common pattern?

A) No, it's bad practice
B) Yes, common for menus and input
C) It causes infinite loops always
D) Only used for debugging

<details><summary>Answer</summary>
**B) Yes, common for menus and input**

**Explanation:** `while True:` with break is a standard pattern for menu systems, continuous input, and event loops. It's clean and readable when used properly.
</details>

---

## Q9: What is the output?
```python
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n > 3:
        break
    print(n * 2)
```

A) 2 4 6
B) 2 4 6 8
C) 2 4 6 8 10
D) 8 10

<details><summary>Answer</summary>
**A) 2 4 6**

**Explanation:** Prints doubled values: 2, 4, 6 (for n=1, 2, 3). When n=4, condition n > 3 is True, so break executes.
</details>

---

## Q10: How do you break from BOTH loops in nested loops?

A) Use break twice
B) Use flag variable
C) Break automatically exits all loops
D) It's not possible

<details><summary>Answer</summary>
**B) Use flag variable**

**Explanation:** Set a flag in inner loop when breaking, then check flag in outer loop to break that too. Pattern:
```python
found = False
for i in ...:
    for j in ...:
        if condition:
            found = True
            break
    if found:
        break
```
</details>

---

## Q11: What is the output?
```python
i = 0
while i < 5:
    i += 1
    if i == 2:
        break
print(i)
```

A) 1
B) 2
C) 5
D) 0

<details><summary>Answer</summary>
**B) 2**

**Explanation:** i increments to 1, then to 2. When i==2, break exits loop. Final value of i is 2.
</details>

---

## Q12: Can a loop have multiple break statements?

A) No, only one break per loop
B) Yes, any number of breaks
C) Only two breaks maximum
D) Breaks must be in else clause

<details><summary>Answer</summary>
**B) Yes, any number of breaks**

**Explanation:** You can have as many break statements as needed. First one that executes will exit the loop.
</details>

---

## Q13: What is the output?
```python
for i in range(10):
    if i % 2 == 0:
        continue
    if i > 5:
        break
    print(i)
```

A) 1 3 5
B) 1 3 5 7
C) 0 2 4 6 8
D) 7 9

<details><summary>Answer</summary>
**A) 1 3 5**

**Explanation:** Skips evens (continue). Prints odds: 1, 3, 5. When i=7 (odd and > 5), break executes. (Note: This question uses continue from next lesson but tests break understanding)
</details>

---

## Q14: Where does execution continue after break?

A) At the beginning of the loop
B) At the line after the loop
C) Program terminates
D) At the nearest else clause

<details><summary>Answer</summary>
**B) At the line after the loop**

**Explanation:** Break exits the loop and execution continues with the first statement after the loop body.
</details>

---

## Q15: What is the output?
```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f"{i},{j}")
```

A) 0,0 1,0 2,0
B) 0,0 0,1 1,0 1,1 2,0 2,1
C) 0,0
D) All combinations from 0,0 to 2,2

<details><summary>Answer</summary>
**A) 0,0 1,0 2,0**

**Explanation:** For each i (0, 1, 2), inner loop prints once (j=0), then breaks at j=1. Outer loop continues normally.
</details>

---

## Score Interpretation

- **13-15 correct**: Excellent! You've mastered the break statement.
- **10-12 correct**: Good work! Review loop-else and nested breaks.
- **7-9 correct**: Fair. Practice more with break patterns and while True.
- **Below 7**: Review the lesson materials on break statement usage.

## Key Concepts to Remember

1. **Immediate exit**: Break stops loop right away
2. **Works in all loops**: while, for, nested
3. **Innermost only**: Break exits closest loop
4. **while True pattern**: Common with break
5. **Loop-else**: Skipped if break executes
6. **Flag variables**: Break from nested loops
7. **Multiple breaks**: First to execute wins
8. **Efficiency**: Skip unnecessary iterations
9. **Search patterns**: Stop when found
10. **Validation**: Break when input valid
