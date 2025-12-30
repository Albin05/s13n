## Post-class Quiz: Accessing List Elements Using Indexing

### Question 1
Given `items = ['a', 'b', 'c', 'd', 'e']`, what is `items[-2]`?

A) 'c'
B) 'd'
C) 'e'
D) Error

**Correct Answer: B**
*Explanation: items[-2] accesses the second element from the end, which is 'd'. Negative indices count backward from the end*

---

### Question 2
What happens when you try `lst[10]` on a list with only 5 elements?

A) Returns None
B) Returns the last element
C) Raises IndexError
D) Returns 0

**Correct Answer: C**
*Explanation: Accessing an index beyond the list bounds raises an IndexError. Valid indices for 5 elements are 0-4 or -5 to -1*

---

### Question 3
Given `matrix = [[1,2], [3,4]]`, what is `matrix[0][1]`?

A) 1
B) 2
C) 3
D) [1, 2]

**Correct Answer: B**
*Explanation: matrix[0] gets [1,2], then [1] gets the second element, which is 2*

---

### Question 4
How do you access the last element of a list without knowing its length?

A) `lst[len(lst)]`
B) `lst[-0]`
C) `lst[-1]`
D) `lst[last]`

**Correct Answer: C**
*Explanation: lst[-1] always accesses the last element regardless of list length. lst[len(lst)] would cause an error (out of bounds)*

---

### Question 5
What does `lst.index(value)` return?

A) The value at that index
B) The first index where value is found
C) All indices where value appears
D) True if value exists

**Correct Answer: B**
*Explanation: .index(value) returns the first index position where the value is found. Raises ValueError if not found*
