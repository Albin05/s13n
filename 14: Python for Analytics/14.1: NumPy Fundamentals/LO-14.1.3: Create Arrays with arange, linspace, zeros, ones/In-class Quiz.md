## In-class Quiz: Create Arrays with arange, linspace, zeros, ones

### Question 1
What will be the output of `np.arange(5, 15, 2)`?

A) `[5, 7, 9, 11, 13, 15]`
B) `[5, 7, 9, 11, 13]`
C) `[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
D) `[5, 7, 9, 11]`

**Correct Answer: B**
*Explanation: arange stops before the stop value (15), with step=2*

---

### Question 2
Which function should you use to create exactly 50 evenly-spaced values between 0 and 100?

A) `np.arange(0, 100, 50)`
B) `np.linspace(0, 100, 50)`
C) `np.zeros(50)`
D) `np.ones(50) * 100`

**Correct Answer: B**

---

### Question 3
What is the main difference between `np.arange()` and `np.linspace()`?

A) arange works with integers, linspace works with floats
B) arange uses step size, linspace uses number of points
C) arange is faster than linspace
D) linspace is only for 2D arrays

**Correct Answer: B**

---

### Question 4
What will be the shape of the array created by `np.zeros((3, 4, 2))`?

A) `(3, 4)`
B) `(4, 2)`
C) `(3, 4, 2)`
D) `(9,)`

**Correct Answer: C**
*Explanation: The shape parameter directly defines the dimensions: 3×4×2 = 3D array*

---

### Question 5
How can you create an array of five 10s using NumPy array creation functions?

A) `np.arange(10, 50, 10)`
B) `np.ones(5) * 10`
C) `np.zeros(5) + 10`
D) Both B and C

**Correct Answer: D**
*Explanation: Both multiply ones by 10 or add 10 to zeros to get [10, 10, 10, 10, 10]*
