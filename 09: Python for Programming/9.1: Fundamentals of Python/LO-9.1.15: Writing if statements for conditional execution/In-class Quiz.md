# Write If Statements

## What's missing?
```python
if age >= 18
    print("Adult")
```
A) Colon after condition
B) Equals sign
C) Parentheses
D) Semicolon after condition

<details><summary>Answer</summary>
A - Colon after condition (should be `if age >= 18:`)
</details>

## What's wrong?
```python
if age >= 18:
print("Adult")
```
A) Missing colon
B) Missing indentation
C) Wrong operator
D) Missing parentheses around condition

<details><summary>Answer</summary>
B - Missing indentation (print statement must be indented)
</details>

## What prints?
```python
x = 10
if x > 15:
    print("A")
print("B")
```
A) A B
B) B
C) A
D) Nothing prints

<details><summary>Answer</summary>
B - Only "B" prints (x is not > 15, so "A" doesn't print. "B" always prints)
</details>

## How many lines run?
```python
if True:
    print("Line 1")
    print("Line 2")
```
A) 0
B) 1
C) 2
D) Error

<details><summary>Answer</summary>
C - Both lines run (both are indented under the if, and condition is True)
</details>

## What's the correct syntax?
A) `if x = 5:`
B) `if x == 5:`
C) `if x == 5`
D) `if (x == 5)`

<details><summary>Answer</summary>
B - `if x == 5:` (use `==` for comparison and include colon)
</details>
