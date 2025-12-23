# Post-Class Quiz: Building Lists Efficiently with Comprehensions

## Q1: What will this list comprehension produce?
```python
result = [x * 2 for x in range(5)]
```
A) [0, 1, 2, 3, 4]
B) [0, 2, 4, 6, 8]
C) [2, 4, 6, 8, 10]
D) Error

<details><summary>Answer</summary>
B - The comprehension multiplies each number in range(5) by 2: 0*2=0, 1*2=2, 2*2=4, 3*2=6, 4*2=8, resulting in [0, 2, 4, 6, 8].
</details>

---

## Q2: Which syntax correctly filters even numbers?
A) `[x for x in numbers if x % 2 == 0 else x]`
B) `[x if x % 2 == 0 for x in numbers]`
C) `[x for x in numbers if x % 2 == 0]`
D) `[if x % 2 == 0: x for x in numbers]`

<details><summary>Answer</summary>
C - For filtering (no else branch), the if goes at the end: `[expression for item in iterable if condition]`. This selects only items that meet the condition.
</details>

---

## Q3: What's the output?
```python
words = ["hi", "hello", "hey"]
result = [len(word) for word in words]
```
A) [2, 5, 3]
B) ["hi", "hello", "hey"]
C) [3, 3, 3]
D) Error

<details><summary>Answer</summary>
A - The comprehension applies len() to each word: len("hi")=2, len("hello")=5, len("hey")=3, producing [2, 5, 3].
</details>

---

## Q4: Where does the if-else go for conditional expressions?
```python
# Want: double evens, keep odds as-is
result = [___ for x in numbers]
```
A) `[x * 2 for x in numbers if x % 2 == 0 else x]`
B) `[x * 2 if x % 2 == 0 else x for x in numbers]`
C) `[for x in numbers if x % 2 == 0: x * 2 else x]`
D) `[x for x in numbers * 2 if x % 2 == 0 else x]`

<details><summary>Answer</summary>
B - For if-else (both branches), the conditional expression goes BEFORE the for: `[expr_if if condition else expr_else for item in iterable]`.
</details>

---

## Q5: What's the equivalent loop for this comprehension?
```python
squares = [n ** 2 for n in range(1, 4)]
```
A)
```python
squares = []
for n in range(1, 4):
    n = n ** 2
```
B)
```python
squares = []
for n in range(1, 4):
    squares.append(n ** 2)
```
C)
```python
for n in range(1, 4):
    squares = n ** 2
```
D)
```python
squares = n ** 2 for n in range(1, 4)
```

<details><summary>Answer</summary>
B - List comprehensions create a new list by appending transformed values. The equivalent is initializing an empty list, then appending each transformed item in a loop.
</details>

---

## Q6: What does this produce?
```python
numbers = [1, 2, 3, 4, 5]
result = [x for x in numbers if x > 2 if x < 5]
```
A) [3, 4]
B) [1, 2, 5]
C) [3, 4, 5]
D) Error

<details><summary>Answer</summary>
A - Multiple if conditions act like AND. This selects numbers where (x > 2) AND (x < 5), which are 3 and 4.
</details>

---

## Q7: Which creates a list of "even" and "odd" labels?
```python
nums = [1, 2, 3, 4]
```
A) `[if n % 2 == 0 "even" else "odd" for n in nums]`
B) `["even" for n in nums if n % 2 == 0 else "odd"]`
C) `["even" if n % 2 == 0 else "odd" for n in nums]`
D) `[for n in nums: "even" if n % 2 == 0 else "odd"]`

<details><summary>Answer</summary>
C - Conditional expression syntax: `[value_if if condition else value_else for item in iterable]`. This evaluates the condition for EACH item and chooses between "even" or "odd".
</details>

---

## Q8: What's wrong with this code?
```python
result = [print(x) for x in numbers]
```
A) Nothing, it works fine
B) print() returns None, creating a list of None values
C) Syntax error
D) print() can't be used in comprehensions

<details><summary>Answer</summary>
B - print() returns None, so this creates a list like [None, None, None...]. List comprehensions should be used to CREATE lists, not for side effects like printing. Use a regular for loop instead.
</details>

---

## Q9: Convert this loop to a comprehension:
```python
result = []
for word in words:
    if len(word) > 4:
        result.append(word.upper())
```
A) `[word.upper() for word in words if len(word) > 4]`
B) `[word.upper() if len(word) > 4 for word in words]`
C) `[for word in words if len(word) > 4: word.upper()]`
D) `[word.upper() for word in words if word > 4]`

<details><summary>Answer</summary>
A - This filters words (if at the end) and transforms them (upper()): `[expression for item in iterable if condition]`.
</details>

---

## Q10: What's the output?
```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
```
A) [[1, 2], [3, 4], [5, 6]]
B) [1, 2, 3, 4, 5, 6]
C) [[1, 3, 5], [2, 4, 6]]
D) Error

<details><summary>Answer</summary>
B - This is a flattening comprehension. Read it like nested loops: for each row, then for each num in that row, collect num. Result: [1, 2, 3, 4, 5, 6].
</details>

---

## Q11: When should you use a traditional loop instead of a comprehension?
A) Never, comprehensions are always better
B) When logic is complex or has multiple statements
C) When working with numbers
D) When the list has more than 10 items

<details><summary>Answer</summary>
B - Use traditional loops when: logic is complex, you need multiple statements per item, you're performing side effects, or the comprehension becomes hard to read.
</details>

---

## Q12: What's the difference between these two?
```python
# Version 1
result1 = [x for x in numbers if x > 5]

# Version 2
result2 = [x if x > 5 else 0 for x in numbers]
```
A) No difference
B) Version 1 filters, Version 2 transforms
C) Version 1 is faster
D) Version 2 has a syntax error

<details><summary>Answer</summary>
B - Version 1 filters (only includes items > 5). Version 2 transforms (includes ALL items, replacing those <= 5 with 0). Filtering if at END, if-else BEFORE for.
</details>

---

## Q13: What does this create?
```python
pairs = [(x, y) for x in [1, 2] for y in ['a', 'b']]
```
A) [(1, 'a'), (2, 'b')]
B) [(1, 2), ('a', 'b')]
C) [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
D) Error

<details><summary>Answer</summary>
C - Nested comprehension creates all combinations (Cartesian product): for each x, pair it with every y. Result: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')].
</details>

---

## Q14: Which is more Pythonic?
```python
# Option A
squares = []
for num in range(10):
    squares.append(num ** 2)

# Option B
squares = [num ** 2 for num in range(10)]
```
A) Option A - more explicit
B) Option B - more concise and Pythonic
C) Both are equally Pythonic
D) Neither, use a while loop

<details><summary>Answer</summary>
B - List comprehensions are considered more Pythonic for simple transformations. They're concise, readable (once you know the syntax), and faster than equivalent loops.
</details>

---

## Q15: What happens here?
```python
numbers = [1, 2, 3]
doubled = [x * 2 for x in numbers]
print(numbers)
```
A) [2, 4, 6] - numbers is modified
B) [1, 2, 3] - numbers is unchanged
C) Error
D) [1, 2, 3, 2, 4, 6] - values are appended

<details><summary>Answer</summary>
B - List comprehensions create a NEW list and don't modify the original. numbers remains [1, 2, 3], while doubled contains [2, 4, 6].
</details>
