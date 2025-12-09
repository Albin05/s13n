# Post-Class Quiz: Use Dictionary Comprehensions

## Q1: What is the output of this dictionary comprehension?
```python
result = {x: x * 2 for x in range(1, 4)}
```
A) {1: 2, 2: 4, 3: 6}
B) {2: 2, 4: 4, 6: 6}
C) [2, 4, 6]

<details><summary>Answer</summary>
A) {1: 2, 2: 4, 3: 6}

Explanation: The range(1, 4) generates 1, 2, 3. For each value x, the dictionary creates a key-value pair where key is x and value is x*2.
</details>

## Q2: How do you create a dictionary from two lists using comprehension?
A) `{x, y for x, y in zip(list1, list2)}`
B) `{x: y for x, y in zip(list1, list2)}`
C) `{x: y for x in list1 for y in list2}`

<details><summary>Answer</summary>
B) `{x: y for x, y in zip(list1, list2)}`

Explanation: The zip() function pairs elements from both lists, and the comprehension creates key-value pairs using the colon (:) syntax. Option A uses comma which would create a set of tuples. Option C creates a Cartesian product.
</details>

## Q3: What does this comprehension do?
```python
data = {"a": 1, "b": 2, "c": 3}
result = {v: k for k, v in data.items()}
```
A) Creates a copy of data
B) Swaps keys and values
C) Doubles all values

<details><summary>Answer</summary>
B) Swaps keys and values

Explanation: By using `v: k` instead of `k: v`, the comprehension creates a new dictionary where the original values become keys and original keys become values. Result: {1: 'a', 2: 'b', 3: 'c'}
</details>

## Q4: Which comprehension filters dictionary items correctly?
A) `{k: v for k, v in items if v > 10}`
B) `{k: v if v > 10 for k, v in items}`
C) `{k: v where v > 10 for k, v in items}`

<details><summary>Answer</summary>
A) `{k: v for k, v in items if v > 10}`

Explanation: The if condition for filtering should come at the end of the comprehension. Option B has incorrect syntax (would need else clause), and option C uses 'where' which is not valid Python syntax.
</details>

## Q5: What's the result of this nested dictionary comprehension?
```python
result = {i: {j: i*j for j in range(1, 3)} for i in range(1, 3)}
```
A) {1: {1: 1, 2: 2}, 2: {1: 2, 2: 4}}
B) {1: 1, 2: 4}
C) [[1, 2], [2, 4]]

<details><summary>Answer</summary>
A) {1: {1: 1, 2: 2}, 2: {1: 2, 2: 4}}

Explanation: The outer comprehension creates keys 1 and 2. For each key i, the inner comprehension creates a dictionary with keys from range(1, 3) and values i*j. This creates a 2x2 multiplication table as a nested dictionary.
</details>
