## Question Bank: Debug Python Programs Effectively

---

### Q1: Read the Traceback (3 minutes, Low Difficulty)

Given this traceback, identify: the error type, which line caused it, and what the fix is.

```
Traceback (most recent call last):
  File "app.py", line 10, in <module>
    result = process_data(records)
  File "app.py", line 6, in process_data
    total = sum(scores)
  File "app.py", line 3, in sum_values
    return a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

**Key Concepts:** Traceback reading, error identification

---

### Q2: Find the Bug (3 minutes, Low Difficulty)

Each function has a bug. Find and fix it:

```python
# Bug 1
def average(numbers):
    return sum(numbers) / len(numbers) - 1

# Bug 2
def greet(names):
    for name in names:
    print(f"Hello, {name}")

# Bug 3
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
        return count
```

**Key Concepts:** Operator precedence, indentation, early return

---

### Q3: Debug with Print (5 minutes, Medium Difficulty)

This function should return the second largest number but gives wrong results:

```python
def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
    return second
```

Add print statements to find the bug. Test with `[5, 3, 8, 1, 9, 2]` (should return 8).

**Key Concepts:** Print debugging, logic error detection

---

### Q4: Fix the Mutable Default (5 minutes, Medium Difficulty)

This code behaves unexpectedly:

```python
def add_student(name, class_list=[]):
    class_list.append(name)
    return class_list

print(add_student("Alice"))   # ['Alice'] ✓
print(add_student("Bob"))     # Expected: ['Bob'], Got: ['Alice', 'Bob'] ✗
print(add_student("Charlie")) # Expected: ['Charlie'], Got: ['Alice', 'Bob', 'Charlie'] ✗
```

1. Explain why this happens
2. Fix the function
3. Write a test to verify the fix

**Key Concepts:** Mutable default argument bug

---

### Q5: Systematic Debugging (5 minutes, Medium Difficulty)

This function should merge two sorted lists into one sorted list, but it has multiple bugs:

```python
def merge_sorted(list1, list2):
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
    result += list1[i:]
    result += list2[j:]
    return result
```

Find all bugs using print debugging. Test with `[1, 3, 5]` and `[2, 4, 6]`.

**Key Concepts:** Systematic debugging, finding multiple bugs
