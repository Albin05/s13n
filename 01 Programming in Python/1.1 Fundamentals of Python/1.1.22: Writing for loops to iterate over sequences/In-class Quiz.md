# Post-class Quiz: Writing For Loops to Iterate Over Sequences

Test your understanding of for loops and iteration in Python.

---

## Q1: What is the output?
```python
fruits = ["apple", "banana"]
for fruit in fruits:
    print(fruit)
```

A) apple banana
B) apple<br>banana
C) ["apple", "banana"]
D) 0 1

<details><summary>Answer</summary>
**B) apple<br>banana**

**Explanation:** For loop iterates through list, printing each fruit on a new line. Output is:
```
apple
banana
```
</details>

---

## Q2: What does the loop variable represent?

```python
for item in my_list:
    print(item)
```

A) The index of the current element
B) The actual value of the current element
C) The entire list
D) The number of items

<details><summary>Answer</summary>
**B) The actual value of the current element**

**Explanation:** In a for loop, the loop variable (`item`) holds the actual value from the sequence, not the index. Each iteration assigns the next value to `item`.
</details>

---

## Q3: What is the output?
```python
total = 0
for num in [1, 2, 3, 4, 5]:
    total += num
print(total)
```

A) 15
B) 5
C) 12345
D) [1, 2, 3, 4, 5]

<details><summary>Answer</summary>
**A) 15**

**Explanation:** Accumulator pattern. Starts at 0, adds each number: 0+1=1, 1+2=3, 3+3=6, 6+4=10, 10+5=15.
</details>

---

## Q4: Can you iterate through a string with a for loop?

A) No, only lists
B) Yes, strings are sequences
C) Only if you convert to list first
D) No, strings are not iterable

<details><summary>Answer</summary>
**B) Yes, strings are sequences**

**Explanation:** Strings are iterable sequences. For loop iterates one character at a time:
```python
for char in "hi":
    print(char)
# Prints: h, then i
```
</details>

---

## Q5: What is the output?
```python
word = "cat"
for letter in word:
    print(letter, end=" ")
```

A) cat
B) c a t
C) c a t (with newlines)
D) Error

<details><summary>Answer</summary>
**B) c a t**

**Explanation:** Loop iterates each character. `end=" "` prints space instead of newline. Output: `c a t `
</details>

---

## Q6: What does enumerate() do?

A) Counts the items
B) Provides both index and value
C) Sorts the list
D) Only works with numbers

<details><summary>Answer</summary>
**B) Provides both index and value**

**Explanation:** `enumerate()` returns pairs of (index, value):
```python
for i, item in enumerate(["a", "b"]):
    print(i, item)
# Output: 0 a, then 1 b
```
</details>

---

## Q7: What is the output?
```python
for i, color in enumerate(["red", "blue"]):
    print(f"{i}: {color}")
```

A) 0: red<br>1: blue
B) 1: red<br>2: blue
C) red blue
D) Error

<details><summary>Answer</summary>
**A) 0: red<br>1: blue**

**Explanation:** enumerate() starts at index 0 by default. First pair is (0, "red"), second is (1, "blue").
</details>

---

## Q8: What does zip() do?

A) Compresses files
B) Combines multiple sequences
C) Sorts lists
D) Filters items

<details><summary>Answer</summary>
**B) Combines multiple sequences**

**Explanation:** `zip()` pairs elements from multiple sequences:
```python
for a, b in zip([1, 2], ["x", "y"]):
    print(a, b)
# Output: 1 x, then 2 y
```
</details>

---

## Q9: What is the output?
```python
names = ["Alice", "Bob"]
ages = [25, 30]

for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

A) Alice: 25<br>Bob: 30
B) Alice Bob 25 30
C) Error
D) [Alice, 25] [Bob, 30]

<details><summary>Answer</summary>
**A) Alice: 25<br>Bob: 30**

**Explanation:** zip() creates pairs: ("Alice", 25) and ("Bob", 30). Loop unpacks and prints each pair.
</details>

---

## Q10: How do you iterate over dictionary key-value pairs?

A) `for item in dict:`
B) `for key, value in dict.items():`
C) `for i in range(len(dict)):`
D) `for dict[key]:`

<details><summary>Answer</summary>
**B) `for key, value in dict.items():`**

**Explanation:** `.items()` returns key-value pairs:
```python
for k, v in {"a": 1, "b": 2}.items():
    print(k, v)
# Prints: a 1, then b 2
```
</details>

---

## Q11: What is the output?
```python
student = {"name": "Alice", "age": 20}

for key in student:
    print(key)
```

A) name age
B) Alice 20
C) name: Alice<br>age: 20
D) Error

<details><summary>Answer</summary>
**A) name age**

**Explanation:** Iterating dictionary directly gives keys only (same as `.keys()`). Each key printed on new line.
</details>

---

## Q12: What happens with nested for loops?

```python
for i in [1, 2]:
    for j in [3, 4]:
        print(i, j)
```

A) Prints 4 combinations
B) Prints 2 combinations
C) Error
D) Prints only outer loop

<details><summary>Answer</summary>
**A) Prints 4 combinations**

**Explanation:** Outer loop runs twice, inner loop runs twice per outer iteration: (1,3), (1,4), (2,3), (2,4) = 4 total.
</details>

---

## Q13: When should you use a for loop instead of while?

A) Always use for
B) When iterating known sequences
C) When you need infinite loops
D) Only for numbers

<details><summary>Answer</summary>
**B) When iterating known sequences**

**Explanation:** For loops are ideal for sequences (lists, strings, ranges). While loops better for unknown iterations or conditions.
</details>

---

## Q14: What is the output?
```python
numbers = [1, 2, 3]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print(doubled)
```

A) [2, 4, 6]
B) [1, 2, 3]
C) 2 4 6
D) 6

<details><summary>Answer</summary>
**A) [2, 4, 6]**

**Explanation:** Loop transforms each number (multiply by 2) and appends to new list. Result: [2, 4, 6].
</details>

---

## Q15: Do break and continue work in for loops?

A) No, only in while loops
B) Yes, same as while loops
C) Only break works
D) Only continue works

<details><summary>Answer</summary>
**B) Yes, same as while loops**

**Explanation:** Both `break` (exit loop) and `continue` (skip to next iteration) work identically in for and while loops.
</details>

---

## Score Interpretation

- **13-15 correct**: Excellent! You've mastered for loops.
- **10-12 correct**: Good work! Review enumerate and zip.
- **7-9 correct**: Fair. Practice more with iteration patterns.
- **Below 7**: Review the lesson materials on for loops.

## Key Concepts to Remember

1. **Direct iteration**: `for item in sequence` - no index needed
2. **Works on sequences**: Lists, strings, tuples, ranges
3. **Enumerate**: Get both index and value
4. **Zip**: Iterate multiple sequences together
5. **Dictionary methods**: `.items()`, `.keys()`, `.values()`
6. **Accumulator pattern**: Build results during iteration
7. **Nested loops**: Loop inside loop for 2D data
8. **Cleaner than while**: For known sequences
9. **Break/continue**: Work same as while loops
10. **No manual indexing**: Python handles automatically
