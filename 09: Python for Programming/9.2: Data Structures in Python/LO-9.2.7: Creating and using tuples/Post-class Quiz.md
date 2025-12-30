## Post-class Quiz: Creating and Using Tuples

### Question 1
Which of these correctly creates a single-element tuple?

A) `single = (5)`
B) `single = [5]`
C) `single = (5,)`
D) `single = tuple(5)`

**Correct Answer: C**
*Explanation: A single-element tuple requires a trailing comma: (5,). Without the comma, (5) is just the integer 5 in parentheses. [5] is a list, and tuple(5) would cause an error*

---

### Question 2
What happens when you try to modify a tuple element: `t = (1, 2, 3); t[0] = 10`?

A) The tuple becomes (10, 2, 3)
B) A new tuple (10, 2, 3) is created
C) TypeError: tuple object does not support item assignment
D) The first element is replaced silently

**Correct Answer: C**
*Explanation: Tuples are immutable. You cannot modify, add, or remove elements after creation. Attempting to assign to an index raises a TypeError*

---

### Question 3
What does this code return: `def func(): return 1, 2, 3`?

A) Three separate values
B) A list [1, 2, 3]
C) A tuple (1, 2, 3)
D) Error: can only return one value

**Correct Answer: C**
*Explanation: When a function returns multiple comma-separated values, Python automatically packs them into a tuple. So return 1, 2, 3 returns the tuple (1, 2, 3)*

---

### Question 4
How many methods do tuples have?

A) Same as lists (11 methods)
B) Only 2: count() and index()
C) None - tuples have no methods
D) 5: count(), index(), append(), remove(), pop()

**Correct Answer: B**
*Explanation: Tuples have only 2 methods: count() to count occurrences and index() to find position. They don't have methods like append, remove, or pop because tuples are immutable*

---

### Question 5
Why can tuples be used as dictionary keys but lists cannot?

A) Tuples are faster
B) Tuples are immutable and hashable
C) Tuples take less memory
D) Lists are too long

**Correct Answer: B**
*Explanation: Dictionary keys must be hashable (unchangeable). Tuples are immutable, making them hashable and suitable as dict keys. Lists are mutable, so they can't be hashed and can't be used as keys*
