## Post-class Quiz: Index and Slice 1D Arrays

### Question 1
What will be the output of `arr[-2]` for `arr = np.array([10, 20, 30, 40, 50])`?

A) 30
B) 40
C) 50
D) IndexError

**Correct Answer: B**

---

### Question 2
Which slicing operation extracts the last 3 elements of an array?

A) `arr[3:]`
B) `arr[-3]`
C) `arr[-3:]`
D) `arr[:3]`

**Correct Answer: C**

---

### Question 3
What does `arr[1:5]` extract?

A) Elements at indices 1, 2, 3, 4
B) Elements at indices 1, 2, 3, 4, 5
C) Elements at indices 0, 1, 2, 3, 4
D) Elements at indices 2, 3, 4, 5

**Correct Answer: A**
*Explanation: Slicing is inclusive of start (1) and exclusive of stop (5), so indices 1, 2, 3, 4*

---

### Question 4
What will `arr[::2]` return for `arr = np.array([1, 2, 3, 4, 5, 6])`?

A) `[1, 2, 3]`
B) `[2, 4, 6]`
C) `[1, 3, 5]`
D) `[1, 2, 3, 4, 5, 6]`

**Correct Answer: C**
*Explanation: `::2` takes every 2nd element starting from index 0*

---

### Question 5
How do you reverse an array using slicing?

A) `arr[::-1]`
B) `arr[-1:]`
C) `arr[::1]`
D) `arr.reverse()`

**Correct Answer: A**
*Explanation: Negative step (-1) reverses the array*
