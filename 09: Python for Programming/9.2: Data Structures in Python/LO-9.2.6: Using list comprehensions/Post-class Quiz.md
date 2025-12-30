## Post-class Quiz: Using List Comprehensions

### Question 1
What is the output of `[x * 2 for x in range(3)]`?

A) `[0, 2, 4]`
B) `[2, 4, 6]`
C) `[1, 2, 3]`
D) `[0, 1, 2]`

**Correct Answer: A**
*Explanation: range(3) gives [0, 1, 2]. Multiplying each by 2 gives [0, 2, 4]. The expression is evaluated for each element from the iterable*

---

### Question 2
Which list comprehension correctly filters even numbers from `nums = [1, 2, 3, 4, 5, 6]`?

A) `[x for x in nums where x % 2 == 0]`
B) `[x if x % 2 == 0 for x in nums]`
C) `[x for x in nums if x % 2 == 0]`
D) `[x for x in nums and x % 2 == 0]`

**Correct Answer: C**
*Explanation: The correct syntax for filtering is [expression for item in iterable if condition]. The 'if' comes after the 'for' clause. Python doesn't use 'where' and option B has incorrect syntax*

---

### Question 3
What does `[x if x > 0 else 0 for x in [-2, 3, -1, 5]]` produce?

A) `[3, 5]`
B) `[-2, 3, -1, 5]`
C) `[0, 3, 0, 5]`
D) Error

**Correct Answer: C**
*Explanation: This uses a conditional expression (ternary). For each element: if x > 0, keep x, else use 0. So -2 becomes 0, 3 stays 3, -1 becomes 0, 5 stays 5, giving [0, 3, 0, 5]*

---

### Question 4
What is the result of `[x for row in [[1,2], [3,4]] for x in row]`?

A) `[[1, 2], [3, 4]]`
B) `[1, 2, 3, 4]`
C) `[(1, 2), (3, 4)]`
D) Error

**Correct Answer: B**
*Explanation: This is a flattening comprehension. It iterates over each row, then over each x in that row, creating a flat list. The order is: for row in matrix, then for x in row, giving [1, 2, 3, 4]*

---

### Question 5
When should you avoid using list comprehensions?

A) When transforming simple data
B) When filtering lists
C) When logic is complex and spans multiple conditions
D) When working with small lists

**Correct Answer: C**
*Explanation: List comprehensions are great for simple transformations and filters, but when logic becomes too complex (multiple nested conditions, complex calculations), a regular for loop is more readable and maintainable*
