## Post-class Quiz: Adding Elements to Sets using add() and update()

**Duration:** 5 minutes

---

### Q1: Basic add() Syntax

What will be the output of the following code?

```python
fruits = {'apple', 'banana'}
fruits.add('orange')
print(len(fruits))
```

**A)** 2
**B)** 3
**C)** 4
**D)** Error

**Correct Answer:** B) 3

**Explanation:** The add() method adds a single element to the set. The set initially has 2 elements, and adding 'orange' makes it 3 elements total.

---

### Q2: Handling Duplicates

What will be the output?

```python
numbers = {1, 2, 3}
numbers.add(2)
numbers.add(4)
print(numbers)
```

**A)** {1, 2, 2, 3, 4}
**B)** {1, 2, 3, 4}
**C)** {2, 3, 4}
**D)** Error

**Correct Answer:** B) {1, 2, 3, 4}

**Explanation:** Sets automatically ignore duplicate values. Adding 2 again has no effect since 2 is already in the set. Adding 4 succeeds since it's new. The exact order may vary as sets are unordered.

---

### Q3: update() Method Behavior

What will be the output?

```python
tags = {'python'}
tags.update(['web', 'tutorial'])
print(len(tags))
```

**A)** 1
**B)** 2
**C)** 3
**D)** Error

**Correct Answer:** C) 3

**Explanation:** The update() method adds all elements from an iterable. It adds both 'web' and 'tutorial' to the existing set that contains 'python', resulting in 3 total elements.

---

### Q4: Common Mistake

What happens when you run this code?

```python
my_set = set()
my_set.add([1, 2, 3])
```

**A)** Set contains one element: [1, 2, 3]
**B)** Set contains three elements: 1, 2, 3
**C)** TypeError: unhashable type: 'list'
**D)** Set becomes {1, 2, 3}

**Correct Answer:** C) TypeError: unhashable type: 'list'

**Explanation:** Sets can only contain immutable (hashable) elements. Lists are mutable and therefore cannot be added to sets. To add multiple elements from a list, use update() instead: `my_set.update([1, 2, 3])`.

---

### Q5: Best Practice Selection

Which approach is MOST efficient for adding multiple elements to a set?

**A)**
```python
s = {1, 2}
s.add(3)
s.add(4)
s.add(5)
```

**B)**
```python
s = {1, 2}
for num in [3, 4, 5]:
    s.add(num)
```

**C)**
```python
s = {1, 2}
s.update([3, 4, 5])
```

**D)** All are equally efficient

**Correct Answer:** C) `s.update([3, 4, 5])`

**Explanation:** The update() method is optimized for adding multiple elements at once and is more efficient than calling add() multiple times in a loop. It performs the operation in a single call rather than multiple individual operations.

---

## Answer Key

| Question | Correct Answer | Key Concept                          |
| -------- | -------------- | ------------------------------------ |
| Q1       | B              | add() syntax and basic usage         |
| Q2       | B              | Automatic duplicate handling         |
| Q3       | C              | update() with iterable               |
| Q4       | C              | Hashability requirement for elements |
| Q5       | C              | Performance: update() vs add()       |
