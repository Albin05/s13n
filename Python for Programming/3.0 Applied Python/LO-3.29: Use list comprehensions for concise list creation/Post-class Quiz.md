# Post-Class Quiz: Use List Comprehensions

## Q1: What is the output of this list comprehension?
```python
result = [x * 2 for x in range(5)]
```
A) [0, 1, 2, 3, 4]
B) [0, 2, 4, 6, 8]
C) [2, 4, 6, 8, 10]

<details><summary>Answer</summary>
B) [0, 2, 4, 6, 8]

Explanation: The range(5) generates 0, 1, 2, 3, 4, and each is multiplied by 2, resulting in [0, 2, 4, 6, 8].
</details>

## Q2: Which list comprehension correctly filters only odd numbers from a list?
A) `odds = [n for n in numbers if n % 2 == 1]`
B) `odds = [n if n % 2 == 1 for n in numbers]`
C) `odds = [n for n in numbers where n % 2 == 1]`

<details><summary>Answer</summary>
A) `odds = [n for n in numbers if n % 2 == 1]`

Explanation: The correct syntax uses `if` condition at the end to filter items. Option B has incorrect syntax, and option C uses `where` which is not valid Python syntax.
</details>

## Q3: What does this nested list comprehension create?
```python
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
```
A) A 3x3 multiplication table
B) A 4x4 identity matrix
C) A list of sums

<details><summary>Answer</summary>
A) A 3x3 multiplication table

Explanation: This creates [[1, 2, 3], [2, 4, 6], [3, 6, 9]], which is a 3x3 multiplication table where each element is the product of its row and column indices.
</details>

## Q4: Which is the most Pythonic way to create a list of uppercase words?
A)
```python
result = []
for word in words:
    result.append(word.upper())
```
B) `result = [word.upper() for word in words]`
C) `result = map(lambda x: x.upper(), words)`

<details><summary>Answer</summary>
B) `result = [word.upper() for word in words]`

Explanation: List comprehensions are considered more Pythonic than traditional loops for simple transformations. While option C works, list comprehensions are generally preferred for their readability.
</details>

## Q5: What's wrong with this list comprehension?
```python
numbers = [1, 2, 3, 4, 5]
result = [n * 2 if n > 3 for n in numbers]
```
A) Missing else clause
B) Syntax is correct
C) Should use 'where' instead of 'if'

<details><summary>Answer</summary>
A) Missing else clause

Explanation: When using if-else in the expression part (before the for), you must include both if and else: `[n * 2 if n > 3 else n for n in numbers]`. If you only want to filter (without else), the if should come after the for: `[n * 2 for n in numbers if n > 3]`.
</details>
