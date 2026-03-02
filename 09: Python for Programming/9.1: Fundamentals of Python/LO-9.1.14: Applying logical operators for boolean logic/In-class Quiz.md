# Apply Logical Operators

## What's the output?
```python
print(True and False)
```
A) True
B) False
C) Error
D) None

<details><summary>Answer</summary>
B - False (both must be True for `and` to return True)
</details>

## What's the output?
```python
print(True or False)
```
A) True
B) False
C) Error
D) None

<details><summary>Answer</summary>
A - True (at least one is True, so `or` returns True)
</details>

## What does `not True` return?
A) True
B) False
C) None
D) Error

<details><summary>Answer</summary>
B - False (`not` reverses the boolean value)
</details>

## Operator precedence?
```python
print(True or False and False)
```
A) True
B) False
C) Error
D) None

<details><summary>Answer</summary>
A - True (evaluates as `True or (False and False)` = `True or False` = `True`)
</details>

## What's the output?
```python
age = 20
has_id = True
can_enter = age >= 18 and has_id
print(can_enter)
```
A) True
B) False
C) Error
D) 20

<details><summary>Answer</summary>
A - True (both conditions are True: 20 >= 18 is True, has_id is True)
</details>
