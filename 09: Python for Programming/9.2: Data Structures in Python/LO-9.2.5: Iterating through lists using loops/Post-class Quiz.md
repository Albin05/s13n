# Post-Class Quiz: Iterating Through Lists Using Loops

## Q1: What will this code output?
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit[0])
```
A) apple banana cherry
B) a b c
C) 0 1 2
D) Error

<details><summary>Answer</summary>
B - The code prints the first character ([0]) of each fruit: 'a', 'b', 'c' (each on a new line).
</details>

---

## Q2: Which method should you use to get both index and value while iterating?
A) range(len(list))
B) enumerate(list)
C) zip(list)
D) for i in list

<details><summary>Answer</summary>
B - enumerate(list) returns both the index and value as a tuple, which can be unpacked in the loop: `for i, item in enumerate(list):`
</details>

---

## Q3: What's wrong with this code?
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    numbers.remove(num)
```
A) Nothing, it works fine
B) It removes items while iterating, causing unpredictable behavior
C) remove() doesn't work in loops
D) num is not defined

<details><summary>Answer</summary>
B - Modifying a list's structure (adding/removing items) while iterating over it causes unpredictable behavior because the indices change during iteration. This is a common and dangerous mistake.
</details>

---

## Q4: What does zip() do when lists have different lengths?
```python
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]
for a, b in zip(list1, list2):
    print(a, b)
```
A) Raises an error
B) Pads the shorter list with None
C) Stops at the shortest list
D) Repeats the shorter list

<details><summary>Answer</summary>
C - zip() stops when the shortest list is exhausted. In this case, it will only print 3 pairs: (1, 10), (2, 20), (3, 30).
</details>

---

## Q5: What will be the value of total after this code runs?
```python
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
```
A) 0
B) 50
C) 150
D) Error

<details><summary>Answer</summary>
C - The code calculates the sum: 10 + 20 + 30 + 40 + 50 = 150. This is the accumulation pattern.
</details>

---

## Q6: What does the continue statement do in a loop?
```python
for num in [1, 2, 3, 4, 5]:
    if num % 2 == 0:
        continue
    print(num)
```
A) Exits the loop completely
B) Skips the current iteration and moves to the next
C) Pauses the loop
D) Raises an error

<details><summary>Answer</summary>
B - continue skips the rest of the current iteration and moves to the next item. This code prints only odd numbers: 1, 3, 5 (even numbers are skipped).
</details>

---

## Q7: How do you modify list elements while iterating?
A) for item in list: item = new_value
B) for i in range(len(list)): list[i] = new_value
C) for item in list: list[item] = new_value
D) You cannot modify lists while iterating

<details><summary>Answer</summary>
B - Use range(len(list)) to get indices, then modify using list[i]. Option A creates a new variable but doesn't modify the list.
</details>

---

## Q8: What does enumerate(list, start=1) do?
A) Starts the loop from index 1
B) Starts counting from 1 instead of 0
C) Skips the first element
D) Raises an error

<details><summary>Answer</summary>
B - The start parameter changes the counter value. enumerate(list, start=1) makes the index start at 1 instead of 0, useful for displaying human-friendly numbered lists.
</details>

---

## Q9: What's the output of this code?
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)
```
A) 1 2
B) 1 2 3
C) 1 2 3 4 5
D) 3 4 5

<details><summary>Answer</summary>
A - break exits the loop immediately when num == 3, so only 1 and 2 are printed before the loop terminates.
</details>

---

## Q10: Which approach is BEST for iterating when you only need the values?
```python
fruits = ["apple", "banana", "cherry"]
```
A) `for i in range(len(fruits)): print(fruits[i])`
B) `for fruit in fruits: print(fruit)`
C) `for i, fruit in enumerate(fruits): print(fruit)`
D) `i = 0; while i < len(fruits): print(fruits[i]); i += 1`

<details><summary>Answer</summary>
B - When you only need values (not indices), `for item in list` is the most Pythonic, readable, and efficient approach. The others work but are unnecessarily complex.
</details>

---

## Q11: What will this code output?
```python
students = ["Alice", "Bob"]
scores = [85, 92, 78]
for student, score in zip(students, scores):
    print(f"{student}: {score}")
```
A) Alice: 85, Bob: 92, Error
B) Alice: 85, Bob: 92
C) Alice: 85, Bob: 92, None: 78
D) Error

<details><summary>Answer</summary>
B - zip() stops at the shortest list (students has 2 items), so only "Alice: 85" and "Bob: 92" are printed. The score 78 is ignored.
</details>

---

## Q12: What must you do before using an accumulator in a loop?
```python
# Calculate sum
for num in numbers:
    total += num
```
A) Nothing, it works automatically
B) Initialize the accumulator variable (total = 0)
C) Import the accumulator module
D) Use the global keyword

<details><summary>Answer</summary>
B - You must initialize accumulator variables before the loop (e.g., total = 0). Otherwise, you'll get a NameError because total doesn't exist yet.
</details>

---

## Q13: Which pattern is this code demonstrating?
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
```
A) Accumulation
B) Filtering
C) Transformation
D) Search

<details><summary>Answer</summary>
B - This is the filtering pattern: building a new list containing only items that meet a specific condition (even numbers in this case).
</details>

---

## Q14: What's the output?
```python
for i, letter in enumerate("ABC"):
    print(i, letter)
```
A) 0 A, 1 B, 2 C
B) A 0, B 1, C 2
C) 1 A, 2 B, 3 C
D) Error - strings can't be enumerated

<details><summary>Answer</summary>
A - enumerate() works with any iterable, including strings. It returns: (0, 'A'), (1, 'B'), (2, 'C'), printed as "0 A", "1 B", "2 C".
</details>

---

## Q15: Which code correctly doubles all numbers in a list?
```python
numbers = [1, 2, 3, 4, 5]
```
A) `for num in numbers: num = num * 2`
B) `for num in numbers: numbers[num] = num * 2`
C) `for i in range(len(numbers)): numbers[i] = numbers[i] * 2`
D) `for i, num in enumerate(numbers): num = num * 2`

<details><summary>Answer</summary>
C - To modify list elements in place, you must use indices: `numbers[i] = new_value`. Option A creates a new variable but doesn't change the list. Option B uses num as an index (wrong). Option D modifies the loop variable, not the list.
</details>
