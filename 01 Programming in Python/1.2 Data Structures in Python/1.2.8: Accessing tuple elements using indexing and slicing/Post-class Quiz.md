# Post-Class Quiz: Accessing Tuple Elements Using Indexing and Slicing

Test your understanding of tuple indexing, slicing, and nested tuple access.

---

## Q1: What is the output of this code?
```python
numbers = (10, 20, 30, 40, 50)
print(numbers[2])
```

A) 20
B) 30
C) 40
D) IndexError

<details><summary>Answer</summary>
**B) 30**

**Explanation:** Index 2 refers to the third element (zero-based indexing). The elements are: index 0=10, index 1=20, index 2=30, index 3=40, index 4=50.
</details>

---

## Q2: What does `my_tuple[-1]` return?

A) The first element
B) The last element
C) IndexError
D) The second element

<details><summary>Answer</summary>
**B) The last element**

**Explanation:** Negative indexing starts from the end. -1 is the last element, -2 is second-to-last, etc. This is a convenient way to access elements from the end without knowing the tuple's length.
</details>

---

## Q3: What is the output?
```python
data = (1, 2, 3, 4, 5)
print(data[1:4])
```

A) `(1, 2, 3, 4)`
B) `(2, 3, 4)`
C) `(2, 3, 4, 5)`
D) `(1, 2, 3)`

<details><summary>Answer</summary>
**B) `(2, 3, 4)`**

**Explanation:** Slicing `[1:4]` starts at index 1 (inclusive) and stops at index 4 (exclusive). So it includes indices 1, 2, and 3, which are the values 2, 3, and 4.
</details>

---

## Q4: Which statement about slicing is TRUE?

A) The stop index is included in the result
B) Slicing always raises IndexError if indices are out of range
C) The stop index is NOT included in the result
D) You cannot omit the start parameter

<details><summary>Answer</summary>
**C) The stop index is NOT included in the result**

**Explanation:** In Python slicing, the stop index is exclusive (not included). This is by design - `data[0:5]` gives exactly 5 elements (indices 0-4). Unlike indexing, slicing does NOT raise IndexError if out of range; it returns what it can.
</details>

---

## Q5: What is the output?
```python
letters = ('a', 'b', 'c', 'd', 'e')
print(letters[:3])
```

A) `('a', 'b', 'c')`
B) `('a', 'b')`
C) `('b', 'c', 'd')`
D) `('a', 'b', 'c', 'd')`

<details><summary>Answer</summary>
**A) `('a', 'b', 'c')`**

**Explanation:** `[:3]` means from the beginning to index 3 (exclusive). It includes indices 0, 1, and 2, which are 'a', 'b', and 'c'.
</details>

---

## Q6: What does `my_tuple[::-1]` do?

A) Returns the first element
B) Returns an empty tuple
C) Reverses the tuple
D) Raises an error

<details><summary>Answer</summary>
**C) Reverses the tuple**

**Explanation:** The step parameter of -1 means traverse backwards. `[::-1]` starts from the end and goes to the beginning, effectively reversing the tuple.
</details>

---

## Q7: What is the output?
```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers[::2])
```

A) `(0, 2, 4, 6, 8)`
B) `(1, 3, 5, 7, 9)`
C) `(0, 1, 2, 3, 4)`
D) `(2, 4, 6, 8)`

<details><summary>Answer</summary>
**A) `(0, 2, 4, 6, 8)`**

**Explanation:** `[::2]` means start from beginning, go to end, with step=2. This takes every second element starting from index 0: indices 0, 2, 4, 6, 8.
</details>

---

## Q8: What happens when you try this?
```python
coords = (10, 20, 30)
coords[1] = 25
```

A) coords becomes `(10, 25, 30)`
B) TypeError is raised
C) No error, but nothing changes
D) IndexError is raised

<details><summary>Answer</summary>
**B) TypeError is raised**

**Explanation:** Tuples are immutable. You can READ elements using indexing, but you cannot MODIFY them. Attempting to assign a new value raises: `TypeError: 'tuple' object does not support item assignment`.
</details>

---

## Q9: What is the output?
```python
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(matrix[1][2])
```

A) 2
B) 5
C) 6
D) 8

<details><summary>Answer</summary>
**C) 6**

**Explanation:** `matrix[1]` accesses the second row `(4, 5, 6)`. Then `[2]` accesses the third element of that row, which is 6. First bracket selects row, second bracket selects element in that row.
</details>

---

## Q10: What is the output?
```python
data = (10, 20, 30, 40, 50)
print(data[-2:])
```

A) `(40, 50)`
B) `(30, 40)`
C) `(10, 20, 30, 40)`
D) `(50,)`

<details><summary>Answer</summary>
**A) `(40, 50)`**

**Explanation:** `[-2:]` means from index -2 (second-to-last) to the end. Index -2 is 40, index -1 is 50, so the result is `(40, 50)`.
</details>

---

## Q11: What's the difference between `data[2]` and `data[2:3]`?

A) No difference, they return the same thing
B) First returns an element, second returns a tuple
C) First returns a tuple, second returns an element
D) Both raise IndexError

<details><summary>Answer</summary>
**B) First returns an element, second returns a tuple**

**Explanation:**
- `data[2]` is indexing - returns the element at index 2 (e.g., if it's an integer, you get an integer)
- `data[2:3]` is slicing - always returns a new tuple containing element(s) from index 2 to 3 (exclusive), so `(element,)` - a single-element tuple
</details>

---

## Q12: What is the output?
```python
colors = ("red", "green", "blue")
print(colors[1:-1])
```

A) `('green',)`
B) `('green', 'blue')`
C) `('red', 'green')`
D) `('blue',)`

<details><summary>Answer</summary>
**A) `('green',)`**

**Explanation:** `[1:-1]` means from index 1 (inclusive) to index -1 (exclusive). Index 1 is 'green', index -1 is 'blue' (last element, excluded). So only 'green' is included.
</details>

---

## Q13: What is the output?
```python
numbers = (1, 2, 3, 4, 5)
print(numbers[10:20])
```

A) IndexError
B) `()`
C) `(1, 2, 3, 4, 5)`
D) TypeError

<details><summary>Answer</summary>
**B) `()`**

**Explanation:** Unlike indexing, slicing does NOT raise an error if indices are out of range. It simply returns an empty tuple if there are no elements in that range. Slicing is forgiving!
</details>

---

## Q14: Which expression gets all elements EXCEPT the last two?

A) `my_tuple[:-2]`
B) `my_tuple[-2:]`
C) `my_tuple[:2]`
D) `my_tuple[2:]`

<details><summary>Answer</summary>
**A) `my_tuple[:-2]`**

**Explanation:** `[:-2]` means from the start to index -2 (exclusive). This excludes the last two elements. For example, if tuple is `(1,2,3,4,5)`, `[:-2]` returns `(1,2,3)`.
</details>

---

## Q15: What is the output?
```python
data = (10, 20, 30, 40, 50)
subset = data[1:4]
print(len(subset))
```

A) 2
B) 3
C) 4
D) 5

<details><summary>Answer</summary>
**B) 3**

**Explanation:** `data[1:4]` extracts indices 1, 2, 3 (stop at 4 is exclusive), which are 20, 30, 40. The length of `(20, 30, 40)` is 3.
</details>

---

## Score Interpretation

- **13-15 correct**: Excellent! You've mastered tuple indexing and slicing.
- **10-12 correct**: Good work! Review slicing syntax and negative indexing.
- **7-9 correct**: Fair. Practice more with slicing and nested tuple access.
- **Below 7**: Review the lesson materials, especially stop being exclusive and negative indexing.

## Key Concepts to Remember

1. **Zero-based indexing**: First element is at index 0
2. **Negative indexing**: -1 is last, -2 is second-to-last
3. **Stop is exclusive**: `[1:4]` gets indices 1, 2, 3 (not 4)
4. **Slicing returns tuple**: Even single element slicing returns a tuple
5. **Indexing returns element**: Returns the actual element type
6. **Slicing never fails**: Returns empty or partial tuple if out of range
7. **Immutable**: Can read but cannot modify
8. **Nested access**: Use `[i][j]` for multilevel structures
9. **Reverse with [::-1]**: Negative step goes backwards
10. **Omit parameters**: `[:3]`, `[3:]`, `[:]` are all valid
