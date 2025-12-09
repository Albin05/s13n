# Post-Class Quiz: Define Variables

## Question 1
What does this code do?
```python
score = 100
```

**A)** Checks if score equals 100
**B)** Assigns 100 to the variable score
**C)** Creates a function called score
**D)** Prints 100

<details>
<summary>Answer</summary>

**B** - Assigns 100 to the variable score

The `=` operator creates/updates a variable with a value.
</details>

---

## Question 2
What will be the final value of `x`?
```python
x = 5
x = 10
x = 15
```

**A)** 5
**B)** 10
**C)** 15
**D)** Error

<details>
<summary>Answer</summary>

**C** - 15

Variables can be reassigned. The final assignment wins.
</details>

---

## Question 3
What's wrong with this code?
```python
print(temperature)
temperature = 72
```

**A)** Nothing, it works fine
**B)** Can't use temperature before creating it
**C)** temperature is a reserved word
**D)** 72 should be in quotes

<details>
<summary>Answer</summary>

**B** - Can't use temperature before creating it

Variables must be created before they're used. Swap the lines!
</details>

---

## Question 4
What does `score = score + 10` mean?

**A)** Checks if score equals score + 10
**B)** Creates two variables
**C)** Adds 10 to current score value
**D)** Causes an error

<details>
<summary>Answer</summary>

**C** - Adds 10 to current score value

Python evaluates the right side first (gets current score, adds 10), then assigns result back to score.
</details>

---

## Question 5
After this code runs, what are the values?
```python
a = 10
b = 20
a = b
```

**A)** a=10, b=20
**B)** a=20, b=10
**C)** a=20, b=20
**D)** Error

<details>
<summary>Answer</summary>

**C** - a=20, b=20

`a = b` copies b's value (20) into a. Both are now 20. The original value of a (10) is lost.
</details>

---

## Scoring
- **5/5**: Excellent! You've mastered variables
- **4/5**: Great! Review the missed question
- **3/5**: Good start, review lecture notes
- **<3**: Please review material and try again
