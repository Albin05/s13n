## Post-class Quiz: Perform Element-wise Operations

### Question 1
What is the result of `np.array([10, 20, 30]) + 5`?

A) [15, 25, 35]
B) [10, 20, 30, 5]
C) [50]
D) An error occurs

**Correct Answer: A**
*Explanation: Element-wise addition adds 5 to each element: [10+5, 20+5, 30+5] = [15, 25, 35]*

---

### Question 2
What does `arr1 * arr2` do when both arrays have the same shape?

A) Matrix multiplication
B) Element-wise multiplication
C) Dot product
D) Concatenation

**Correct Answer: B**
*Explanation: The `*` operator performs element-wise multiplication, multiplying corresponding elements: [a1*b1, a2*b2, ...]*

---

### Question 3
What is the difference between `arr = arr + 10` and `arr += 10`?

A) No difference, they are exactly the same
B) `+=` modifies the array in-place, `+` creates a new array
C) `+` is faster than `+=`
D) `+=` only works with scalars

**Correct Answer: B**
*Explanation: `arr += 10` modifies the existing array in-place (memory efficient), while `arr = arr + 10` creates a new array and reassigns*

---

### Question 4
What does `np.array([10, 20, 30]) > 15` return?

A) [True, True, True]
B) [False, True, True]
C) [10, 20, 30]
D) 2

**Correct Answer: B**
*Explanation: Comparison operators return boolean arrays element-wise: [10>15, 20>15, 30>15] = [False, True, True]*

---

### Question 5
Given `arr = np.array([10, 20, 30])`, what is the result of `arr ** 2`?

A) [20, 40, 60]
B) [100, 400, 900]
C) [12, 22, 32]
D) 60

**Correct Answer: B**
*Explanation: The `**` operator performs element-wise exponentiation: [10², 20², 30²] = [100, 400, 900]*
