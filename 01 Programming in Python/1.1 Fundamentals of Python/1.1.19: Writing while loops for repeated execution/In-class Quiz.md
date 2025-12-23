# Post-class Quiz: Writing While Loops for Repeated Execution

Test your understanding of while loops and their application in Python.

---

## Q1: What is the output of this code?
```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

A) 1 2 3
B) 1 2 3 4
C) 0 1 2 3
D) Infinite loop

<details><summary>Answer</summary>
**A) 1 2 3**

**Explanation:** Starts at 1, loops while count <= 3, increments each time. Prints 1, 2, 3. When count becomes 4, condition (4 <= 3) is False, loop stops.
</details>

---

## Q2: What are the THREE essential parts of a while loop?

A) Start, Middle, End
B) Initialization, Condition, Update
C) Begin, Loop, Finish
D) Input, Process, Output

<details><summary>Answer</summary>
**B) Initialization, Condition, Update**

**Explanation:**
- **Initialization**: Set variables before loop
- **Condition**: Test that determines if loop continues
- **Update**: Modify variables to eventually make condition False
Missing any part can cause errors or infinite loops.
</details>

---

## Q3: What causes an infinite loop?

A) Loop condition that's always True
B) Forgetting to update loop variables
C) Condition that never becomes False
D) All of the above

<details><summary>Answer</summary>
**D) All of the above**

**Explanation:** An infinite loop occurs when the condition never becomes False. This happens when:
- Condition is literally `while True:` without break
- Loop variables aren't updated (`count += 1` missing)
- Logic error prevents condition from becoming False
</details>

---

## Q4: What is the output?
```python
x = 5
while x > 0:
    print(x)
    x -= 2
```

A) 5 4 3 2 1
B) 5 3 1
C) 5 3 1 -1
D) Infinite loop

<details><summary>Answer</summary>
**B) 5 3 1**

**Explanation:** Starts at 5, decrements by 2 each time:
- x=5: 5 > 0? YES → Print 5, x=3
- x=3: 3 > 0? YES → Print 3, x=1
- x=1: 1 > 0? YES → Print 1, x=-1
- x=-1: -1 > 0? NO → Stop
</details>

---

## Q5: What is a sentinel value?

A) A guard that protects code
B) A special value that signals loop termination
C) A counter variable
D) An error message

<details><summary>Answer</summary>
**B) A special value that signals loop termination**

**Explanation:** A sentinel value is a specific value that tells the loop to stop. Example: entering "quit" to exit a menu, or 0 to stop summing numbers. It acts as a signal that input is complete.
</details>

---

## Q6: When should you use a while loop instead of a for loop?

A) Always use while, never for
B) When you know exact number of iterations
C) When you don't know how many iterations in advance
D) Only for infinite loops

<details><summary>Answer</summary>
**C) When you don't know how many iterations in advance**

**Explanation:** Use while when iterations depend on a condition (e.g., "until user enters correct password"). Use for when you know the count (e.g., "exactly 10 times").
</details>

---

## Q7: What is the output?
```python
total = 0
num = 1

while num <= 4:
    total += num
    num += 1

print(total)
```

A) 4
B) 10
C) 14
D) 15

<details><summary>Answer</summary>
**B) 10**

**Explanation:** Sum of 1+2+3+4 = 10
- num=1: total=0+1=1, num=2
- num=2: total=1+2=3, num=3
- num=3: total=3+3=6, num=4
- num=4: total=6+4=10, num=5
- num=5: 5 <= 4? NO → Exit, print 10
</details>

---

## Q8: What is an accumulator in a loop?

A) A variable that accumulates speed
B) A variable that builds up a result over iterations
C) A type of loop
D) An error counter

<details><summary>Answer</summary>
**B) A variable that builds up a result over iterations**

**Explanation:** An accumulator collects results as the loop runs. Examples:
- `total += number` (sum accumulator)
- `count += 1` (counter)
- `product *= num` (multiplication accumulator)
Initialized before loop, updated inside loop.
</details>

---

## Q9: What happens if the while condition is False from the start?

A) Error occurs
B) Loop runs once anyway
C) Loop body never executes
D) Program crashes

<details><summary>Answer</summary>
**C) Loop body never executes**

**Explanation:** Python checks the condition BEFORE entering the loop. If False initially, the body is skipped entirely (zero iterations). This is normal behavior, not an error.
</details>

---

## Q10: What is the output?
```python
i = 0
while i < 3:
    print(i * 2)
    i += 1
```

A) 0 1 2
B) 0 2 4
C) 2 4 6
D) 0 2 4 6

<details><summary>Answer</summary>
**B) 0 2 4**

**Explanation:** Loop runs 3 times (i=0, 1, 2), printing i*2:
- i=0: Print 0*2=0, i=1
- i=1: Print 1*2=2, i=2
- i=2: Print 2*2=4, i=3
- i=3: 3 < 3? NO → Stop
</details>

---

## Q11: What is a "priming read"?

A) Reading input to prime a pump
B) First input read before entering the loop
C) Reading input twice
D) Fastest way to read input

<details><summary>Answer</summary>
**B) First input read before entering the loop**

**Explanation:** Priming read gets initial value to test in loop condition. Pattern:
```python
value = input()  # Priming read
while value != "quit":
    # Process value
    value = input()  # Read next
```
Ensures first value is available for condition check.
</details>

---

## Q12: What is the output?
```python
n = 10
count = 0

while n > 1:
    n //= 2
    count += 1

print(count)
```

A) 3
B) 4
C) 5
D) 10

<details><summary>Answer</summary>
**A) 3**

**Explanation:** Counts how many times you can divide by 2:
- n=10: 10//2=5, count=1
- n=5: 5//2=2, count=2
- n=2: 2//2=1, count=3
- n=1: 1 > 1? NO → Stop, print 3
</details>

---

## Q13: Which code pattern validates user input?

A) `while input_valid: get_input()`
B) `while input_invalid: get_input()`
C) `for i in range(10): get_input()`
D) `if input_invalid: get_input()`

<details><summary>Answer</summary>
**B) `while input_invalid: get_input()`**

**Explanation:** Validation pattern loops WHILE input is invalid:
```python
age = int(input())
while age < 0 or age > 120:  # While invalid
    age = int(input("Try again: "))
```
Forces user to provide valid input before continuing.
</details>

---

## Q14: What is the difference between `count += 1` and `count = count + 1`?

A) They're completely different
B) They're equivalent (same result)
C) First is faster
D) Second is more accurate

<details><summary>Answer</summary>
**B) They're equivalent (same result)**

**Explanation:** `count += 1` is shorthand for `count = count + 1`. Both increment count by 1. The `+=` operator is more concise and commonly used. Other compound operators: `-=`, `*=`, `//=`, etc.
</details>

---

## Q15: What is the output?
```python
password = "secret"
attempts = 0

while password != "python" and attempts < 2:
    password = "python"
    attempts += 1

print(attempts)
```

A) 0
B) 1
C) 2
D) Infinite loop

<details><summary>Answer</summary>
**B) 1**

**Explanation:**
- Initial: password="secret", attempts=0
- Check: "secret" != "python" AND 0 < 2? YES → Enter loop
- Set password="python", attempts=1
- Check: "python" != "python" AND 1 < 2? NO (first condition False)
- Exit loop, print 1
</details>

---

## Score Interpretation

- **13-15 correct**: Excellent! You've mastered while loops.
- **10-12 correct**: Good work! Review loop conditions and update statements.
- **7-9 correct**: Fair. Practice more with accumulators and sentinel values.
- **Below 7**: Review the lesson materials on while loop structure and patterns.

## Key Concepts to Remember

1. **Three parts**: Initialize, Condition, Update
2. **Condition checked first**: Before each iteration
3. **Update is critical**: Without it, infinite loop
4. **Accumulator pattern**: Build result over iterations
5. **Sentinel value**: Special value that stops loop
6. **While vs For**: While for unknown iterations
7. **Priming read**: Get first value before loop
8. **Validation pattern**: Loop while invalid
9. **Zero iterations**: If condition False from start
10. **Compound operators**: `+=`, `-=`, `*=`, `//=`
