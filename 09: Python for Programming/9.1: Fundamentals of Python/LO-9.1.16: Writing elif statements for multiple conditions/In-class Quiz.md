# Write Elif Statements

## What runs?
```python
x = 15
if x > 20:
    print("A")
elif x > 10:
    print("B")
elif x > 5:
    print("C")
```
A) A
B) B
C) B and C
D) C

<details><summary>Answer</summary>
B - Only "B" prints (first True condition, then stops)
</details>

## What's wrong?
```python
elif x > 10:
    print("Big")
```
A) Missing if statement before elif
B) Missing colon
C) Wrong indentation
D) elif cannot be used with print

<details><summary>Answer</summary>
A - elif must come after an if statement
</details>

## What prints?
```python
score = 95
if score >= 70:
    print("Pass")
elif score >= 90:
    print("Excellent")
```
A) Pass
B) Excellent
C) Pass and Excellent
D) No output

<details><summary>Answer</summary>
A - "Pass" (first condition is True, so elif never runs)
</details>

## Best practice for order?
A) General conditions first, specific last
B) Specific conditions first, general last
C) Order doesn't matter
D) Alphabetical order of variable names

<details><summary>Answer</summary>
B - Specific conditions first, general last
</details>

## How many elif statements can you have?
A) Only one
B) Maximum two
C) As many as needed
D) Maximum five

<details><summary>Answer</summary>
C - You can chain as many elif statements as needed
</details>
