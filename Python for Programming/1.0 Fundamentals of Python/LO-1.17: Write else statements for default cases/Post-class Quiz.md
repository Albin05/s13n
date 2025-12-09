# Post-Class Quiz: Write Else Statements

## Q1: What's wrong?
```python
if x > 10:
    print("Big")
else x <= 10:
    print("Small")
```
A) else can't have a condition
B) Missing colon
C) Wrong indentation

<details><summary>Answer</summary>
A - else should not have a condition (remove `x <= 10`)
</details>

## Q2: When does else run?
```python
if x > 10:
    print("A")
elif x > 5:
    print("B")
else:
    print("C")
```
A) When x > 10
B) When x > 5
C) When x <= 5

<details><summary>Answer</summary>
C - else runs when ALL previous conditions are False (x <= 5)
</details>

## Q3: What prints?
```python
score = 75
if score >= 60:
    print("Pass")
else:
    print("Fail")
```
A) Pass
B) Fail
C) Both

<details><summary>Answer</summary>
A - Pass (75 >= 60 is True)
</details>

## Q4: Can you have multiple else blocks?
```python
if x > 10:
    print("A")
else:
    print("B")
else:
    print("C")
```
A) Yes
B) No
C) Only with elif

<details><summary>Answer</summary>
B - No, only ONE else per if-elif chain (this is a SyntaxError)
</details>

## Q5: Where must else go?
A) Before if
B) Before elif
C) After all if/elif

<details><summary>Answer</summary>
C - else must come AFTER all if/elif statements
</details>
