# Post-Class Quiz: Apply Logical Operators

## Q1: What's the output?
```python
print(True and False)
```
A) True
B) False
C) Error

<details><summary>Answer</summary>
B - False (both must be True for `and` to return True)
</details>

## Q2: What's the output?
```python
print(True or False)
```
A) True
B) False
C) Error

<details><summary>Answer</summary>
A - True (at least one is True, so `or` returns True)
</details>

## Q3: What does `not True` return?
A) True
B) False
C) None

<details><summary>Answer</summary>
B - False (`not` reverses the boolean value)
</details>

## Q4: Operator precedence?
```python
print(True or False and False)
```
A) True
B) False
C) Error

<details><summary>Answer</summary>
A - True (evaluates as `True or (False and False)` = `True or False` = `True`)
</details>

## Q5: What's the output?
```python
age = 20
has_id = True
can_enter = age >= 18 and has_id
print(can_enter)
```
A) True
B) False
C) Error

<details><summary>Answer</summary>
A - True (both conditions are True: 20 >= 18 is True, has_id is True)
</details>
