## Post-class Quiz: Removing Elements using remove() and discard()

**Duration:** 5 minutes

---

### Q1: Error Behavior

What happens when you run this code?

```python
fruits = {'apple', 'banana'}
fruits.remove('orange')
```

**A)** Prints None
**B)** Raises KeyError
**C)** Silently does nothing
**D)** Removes 'apple' instead

**Correct Answer:** B) Raises KeyError

**Explanation:** The remove() method raises a KeyError when trying to remove an element that doesn't exist in the set. This is the key difference from discard().

---

### Q2: Safe Removal

What will be the output?

```python
tags = {'python', 'web', 'tutorial'}
tags.discard('java')
tags.discard('python')
print(len(tags))
```

**A)** Error
**B)** 1
**C)** 2
**D)** 3

**Correct Answer:** C) 2

**Explanation:** discard() safely removes elements if they exist. The first discard('java') does nothing since 'java' isn't in the set. The second discard('python') removes 'python', leaving {'web', 'tutorial'} with length 2.

---

### Q3: Method Comparison

Which statement is TRUE about remove() and discard()?

**A)** remove() is faster than discard()
**B)** discard() can remove multiple elements at once
**C)** remove() raises an error if element not found, discard() doesn't
**D)** discard() returns the removed element, remove() doesn't

**Correct Answer:** C) remove() raises an error if element not found, discard() doesn't

**Explanation:** The main difference is error handling: remove() raises KeyError for missing elements, while discard() silently does nothing. Both have O(1) performance, both remove one element at a time, and neither returns the removed element.

---

### Q4: pop() Behavior

What is TRUE about the pop() method for sets?

```python
numbers = {1, 2, 3, 4, 5}
x = numbers.pop()
```

**A)** x is guaranteed to be 1
**B)** x is guaranteed to be 5
**C)** x could be any element from the set
**D)** x is always the smallest element

**Correct Answer:** C) x could be any element from the set

**Explanation:** Sets are unordered collections, so pop() removes and returns an arbitrary (unpredictable) element. You cannot rely on any particular element being removed. This is different from list.pop() which removes from a specific position.

---

### Q5: Best Practice

You're building a feature where users can remove items from their wishlist. Which method should you use?

**A)** remove() - to ensure item exists
**B)** discard() - to handle duplicate clicks safely
**C)** pop() - to remove items randomly
**D)** clear() - to remove all items

**Correct Answer:** B) discard() - to handle duplicate clicks safely

**Explanation:** For user-driven operations, discard() is the safest choice because users might click "remove" multiple times, or the item might already be removed in another browser tab. discard() is idempotent - it can be called multiple times without causing errors.

---

## Answer Key

| Question | Correct Answer | Key Concept                     |
| -------- | -------------- | ------------------------------- |
| Q1       | B              | remove() raises KeyError        |
| Q2       | C              | discard() is safe and silent    |
| Q3       | C              | Error handling difference       |
| Q4       | C              | pop() removes arbitrary element |
| Q5       | B              | discard() for user actions      |
