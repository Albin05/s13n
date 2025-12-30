## Post-class Quiz: Modifying Lists Using Built-in Methods

### Question 1
What is the difference between `append()` and `extend()`?

A) append adds to beginning, extend adds to end
B) append adds single element, extend adds multiple elements
C) append modifies list, extend creates new list
D) No difference, they work the same way

**Correct Answer: B**
*Explanation: append() adds a single element (even if it's a list) to the end. extend() iterates through an iterable and adds each element individually. Example: [1,2].append([3,4]) gives [1,2,[3,4]] but [1,2].extend([3,4]) gives [1,2,3,4]*

---

### Question 2
Which method removes AND returns an element from a list?

A) remove()
B) del
C) pop()
D) clear()

**Correct Answer: C**
*Explanation: pop() removes an element at a specified index (or last element if no index given) and returns it. remove() only removes by value and returns None. del is a statement that deletes but doesn't return. clear() removes all elements*

---

### Question 3
Given `numbers = [3, 1, 4, 1, 5]`, what does `numbers.sort()` return?

A) [1, 1, 3, 4, 5]
B) None
C) A sorted copy
D) True

**Correct Answer: B**
*Explanation: sort() modifies the list in-place and returns None. The list itself becomes [1, 1, 3, 4, 5], but the return value is None. This is why you shouldn't do numbers = numbers.sort() as you'll lose your list*

---

### Question 4
What happens when you call `lst.remove(x)` and x is not in the list?

A) Returns None
B) Returns -1
C) Raises ValueError
D) Does nothing

**Correct Answer: C**
*Explanation: remove() raises a ValueError if the value is not found in the list. To avoid this, check with 'if x in lst:' before calling remove(), or use a try-except block*

---

### Question 5
Given `fruits = ['apple', 'banana']`, what is `fruits` after `fruits.copy().append('orange')`?

A) ['apple', 'banana', 'orange']
B) ['apple', 'banana']
C) ['orange']
D) Error

**Correct Answer: B**
*Explanation: fruits.copy() creates a new list, and append() is called on that copy, not on the original. The original fruits list remains ['apple', 'banana']. The copy (which has 'orange' added) is not saved anywhere so it's lost*
