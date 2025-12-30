## Post-class Quiz: Creating and Initializing Lists in Python

### Question 1
Which of the following creates an empty list?

A) `list = {}`
B) `list = []`
C) `list = ()`
D) `list = ""`

**Correct Answer: B**
*Explanation: [] creates an empty list. {} creates an empty dictionary, () creates an empty tuple, and "" creates an empty string*

---

### Question 2
What is the output of `list(range(3, 8))`?

A) [3, 4, 5, 6, 7, 8]
B) [3, 4, 5, 6, 7]
C) [4, 5, 6, 7]
D) [3, 8]

**Correct Answer: B**
*Explanation: range(3, 8) starts at 3 and goes up to but not including 8, so it produces [3, 4, 5, 6, 7]*

---

### Question 3
What does `"hello world".split()` return?

A) ['hello world']
B) ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
C) ['hello', 'world']
D) ['h', 'w']

**Correct Answer: C**
*Explanation: split() without arguments splits on whitespace, creating ['hello', 'world']. To get individual characters, use list("hello world")*

---

### Question 4
Given `matrix = [[1, 2], [3, 4], [5, 6]]`, what is `matrix[1][1]`?

A) 1
B) 2
C) 3
D) 4

**Correct Answer: D**
*Explanation: matrix[1] selects the second inner list [3, 4], then [1] selects the second element 4*

---

### Question 5
What is the output of `[1, 2] + [3, 4]`?

A) [1, 2, 3, 4]
B) [[1, 2], [3, 4]]
C) [4, 6]
D) Error

**Correct Answer: A**
*Explanation: The + operator concatenates lists, combining them into a single list [1, 2, 3, 4]*
