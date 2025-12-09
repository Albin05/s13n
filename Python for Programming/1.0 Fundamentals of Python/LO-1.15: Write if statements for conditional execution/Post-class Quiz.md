# Post-Class Quiz: Write If Statements

## Q1: What's missing?
```python
if age >= 18
    print("Adult")
```
A) Colon after condition
B) Equals sign
C) Parentheses

<details><summary>Answer</summary>
A - Colon after condition (should be `if age >= 18:`)
</details>

## Q2: What's wrong?
```python
if age >= 18:
print("Adult")
```
A) Missing colon
B) Missing indentation
C) Wrong operator

<details><summary>Answer</summary>
B - Missing indentation (print statement must be indented)
</details>

## Q3: What prints?
```python
x = 10
if x > 15:
    print("A")
print("B")
```
A) A B
B) B
C) A

<details><summary>Answer</summary>
B - Only "B" prints (x is not > 15, so "A" doesn't print. "B" always prints)
</details>

## Q4: How many lines run?
```python
if True:
    print("Line 1")
    print("Line 2")
```
A) 0
B) 1
C) 2

<details><summary>Answer</summary>
C - Both lines run (both are indented under the if, and condition is True)
</details>

## Q5: What's the correct syntax?
A) `if x = 5:`
B) `if x == 5:`
C) `if x == 5`

<details><summary>Answer</summary>
B - `if x == 5:` (use `==` for comparison and include colon)
</details>
