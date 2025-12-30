## Post-class Quiz: Apply Broadcasting Rules

### Question 1
What happens when you execute `np.array([1, 2, 3]) + 10`?

A) An error occurs
B) [11, 12, 13]
C) [1, 2, 3, 10]
D) 16

**Correct Answer: B**
*Explanation: The scalar 10 is broadcast to match the array shape, adding 10 to each element: [11, 12, 13]*

---

### Question 2
Which shapes are compatible for broadcasting?

A) (3, 4) and (4,)
B) (3, 4) and (3,)
C) (3, 4) and (4, 3)
D) (3, 4) and (2, 4)

**Correct Answer: A**
*Explanation: (4,) can be broadcast to (3, 4) because the trailing dimension matches. It becomes (1, 4) then stretches to (3, 4)*

---

### Question 3
What does `keepdims=True` do in `np.mean(arr, axis=1, keepdims=True)`?

A) Keeps all dimensions the same
B) Preserves the reduced dimension as size 1
C) Prevents broadcasting
D) Calculates mean differently

**Correct Answer: B**
*Explanation: `keepdims=True` keeps the reduced dimension with size 1, making it easier to broadcast. Shape (3, 4) with axis=1 becomes (3, 1) instead of (3,)*

---

### Question 4
What is the purpose of `np.newaxis`?

A) Creates a new array
B) Adds a new dimension of size 1
C) Removes a dimension
D) Resets array indices

**Correct Answer: B**
*Explanation: `np.newaxis` adds a new dimension with size 1, useful for reshaping arrays for broadcasting*

---

### Question 5
Given `arr` with shape (3, 4), which operation will work?

A) `arr + np.array([1, 2, 3])`
B) `arr + np.array([[1], [2], [3]])`
C) `arr + np.array([1, 2])`
D) Both A and B will fail

**Correct Answer: B**
*Explanation: Shape (3, 1) is compatible with (3, 4) and broadcasts across columns. Shape (3,) is NOT compatible with (3, 4) for direct addition*
