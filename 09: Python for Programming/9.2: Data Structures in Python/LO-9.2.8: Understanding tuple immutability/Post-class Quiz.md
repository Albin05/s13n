## Post-class Quiz: Understanding Tuple Immutability

### Question 1
What makes tuples immutable?

A) You cannot access their elements
B) You cannot change the tuple's structure after creation
C) They take less memory than lists
D) They can only contain numbers

**Correct Answer: B**
*Explanation: Tuples are immutable because you cannot change their structure - you cannot add, remove, or reassign elements. You CAN access elements, they can contain any type, and while they do use less memory, that's not what makes them immutable*

---

### Question 2
Given `data = (1, 2, [3, 4])`, which operation will succeed?

A) `data[0] = 10`
B) `data.append(5)`
C) `data[2].append(5)`
D) `data[2] = [5, 6]`

**Correct Answer: C**
*Explanation: The tuple structure is immutable, so you cannot reassign elements (A, D) or use list methods (B). However, the list INSIDE the tuple is mutable, so data[2].append(5) works. The tuple still points to the same list object*

---

### Question 3
Why can tuples be used as dictionary keys but lists cannot?

A) Tuples are smaller
B) Tuples are faster
C) Tuples are immutable and hashable
D) Lists are too complex

**Correct Answer: C**
*Explanation: Dictionary keys must be hashable (have a stable hash value). Tuples are immutable, so their hash never changes, making them valid keys. Lists are mutable - they can change, so their hash would change, making them unsuitable as dictionary keys*

---

### Question 4
What is "shallow immutability"?

A) Tuples that are almost immutable
B) The tuple structure is immutable but nested mutable objects can change
C) Tuples can only contain simple types
D) Immutability that doesn't work properly

**Correct Answer: B**
*Explanation: Shallow immutability means the tuple itself cannot be modified (its structure is fixed), but if it contains mutable objects like lists or dictionaries, those objects' contents can still be changed. The tuple still references the same objects*

---

### Question 5
Which tuple can be used as a dictionary key?

A) `(1, 2, [3, 4])`
B) `(1, 2, {'a': 3})`
C) `(1, 2, (3, 4))`
D) `(1, 2, [3, 4], 5)`

**Correct Answer: C**
*Explanation: Only tuples containing entirely immutable/hashable objects can be used as dictionary keys. (1, 2, (3, 4)) contains only immutables. Options A and D contain lists (mutable), B contains a dict (mutable), making them unhashable*
