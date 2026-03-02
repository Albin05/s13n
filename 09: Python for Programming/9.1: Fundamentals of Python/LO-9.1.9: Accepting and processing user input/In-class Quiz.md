# Accept User Input

## What does input() return?
A) int
B) str
C) Depends on input

<details><summary>Answer</summary>
B - Always returns string
</details>

## Fix this:
```python
age = input("Age: ")
result = age + 5
```
A) int(age) + 5
B) age + str(5)
C) float(age) + str(5)
D) int(age) + int("5")

<details><summary>Answer</summary>
A - Convert string to int
</details>

## Get number from user?
A) num = input("Number: ")
B) num = int(input("Number: "))
C) num = str(input("Number: "))
D) num = get("Number: ")

<details><summary>Answer</summary>
B - Convert to int immediately
</details>

## What's wrong?
```python
x = input()
```
A) Missing prompt
B) Nothing wrong
C) Missing quotes

<details><summary>Answer</summary>
B - Prompt is optional (but recommended)
</details>

## Multiple inputs?
A) Can only use input() once
B) Can call input() multiple times
C) Need special function

<details><summary>Answer</summary>
B - Call input() for each value needed
</details>
