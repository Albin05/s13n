## Editorials: Debug Python Programs Effectively

---

### Q1 Solution: Read the Traceback

**Error:** `TypeError: unsupported operand type(s) for +: 'int' and 'str'`
**Line:** `app.py`, line 3 in `sum_values`
**Cause:** Trying to add an integer and a string
**Fix:** Ensure all elements are numbers: `return int(a) + int(b)` or validate input types.

---

### Q2 Solution: Find the Bug

```python
# Bug 1: Operator precedence — division happens before subtraction
def average(numbers):
    return sum(numbers) / len(numbers)  # Removed "- 1"
    # Or if intent was len-1: return sum(numbers) / (len(numbers) - 1)

# Bug 2: Missing indentation
def greet(names):
    for name in names:
        print(f"Hello, {name}")  # Indented under for

# Bug 3: return is inside the loop — only checks first char
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count  # Dedented — outside the loop
```

---

### Q3 Solution: Debug with Print

```python
def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]  # BUG: if first element IS the largest, second starts wrong
    for num in numbers:
        print(f"  num={num}, largest={largest}, second={second}")
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:  # FIX: need this condition
            second = num
    return second

print(second_largest([5, 3, 8, 1, 9, 2]))  # Should return 8
```

**Bug:** The original doesn't handle numbers between `second` and `largest`. Adding `elif num > second and num != largest` fixes it.

---

### Q4 Solution: Fix the Mutable Default

```python
# Explanation: Default [] is created ONCE, shared across all calls.
# Each call appends to the SAME list.

# Fix:
def add_student(name, class_list=None):
    if class_list is None:
        class_list = []
    class_list.append(name)
    return class_list

# Verify fix:
result1 = add_student("Alice")
result2 = add_student("Bob")
result3 = add_student("Charlie")
assert result1 == ["Alice"]
assert result2 == ["Bob"]
assert result3 == ["Charlie"]
print("All tests pass!")
```

---

### Q5 Solution: Systematic Debugging

```python
def merge_sorted(list1, list2):
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:  # FIX 1: use <= for stability
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1  # FIX 2: was missing j += 1!
    result += list1[i:]
    result += list2[j:]
    return result

# BUG: missing j += 1 caused infinite loop when list2 element was smaller
print(merge_sorted([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
```

**Bug found:** The `else` branch appended from list2 but never incremented `j`, causing an infinite loop.
