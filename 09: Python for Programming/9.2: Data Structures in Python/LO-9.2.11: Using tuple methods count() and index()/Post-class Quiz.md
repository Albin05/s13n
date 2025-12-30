## Post-class Quiz: Using Tuple Methods count() and index()

---

### Question 1
What does `numbers.count(5)` return if `numbers = (1, 2, 3, 4)`?

A) ValueError  
B) -1  
C) 0  
D) None

**Correct Answer: C**

*Explanation: The count() method returns 0 if the value is not found in the tuple. It never raises an exception, making it safe to use without error handling. This is different from index() which raises ValueError if the value is not found.*

---

### Question 2
Given `data = (10, 20, 30, 20, 40)`, what does `data.index(20)` return?

A) 1  
B) 3  
C) [1, 3]  
D) 2

**Correct Answer: A**

*Explanation: The index() method returns the index of the FIRST occurrence of the value. Even though 20 appears at both index 1 and index 3, index() only returns 1 (the first occurrence). To find all occurrences, you need to use index() with the start parameter in a loop.*

---

### Question 3
What happens when you run `colors.index('purple')` if `colors = ('red', 'blue', 'green')`?

A) Returns 0  
B) Returns -1  
C) Raises ValueError  
D) Returns None

**Correct Answer: C**

*Explanation: The index() method raises a ValueError if the value is not found in the tuple. This is why it's important to either use try-except when calling index(), or check with count() first to ensure the value exists before calling index().*

---

### Question 4
How can you find the second occurrence of a value in a tuple?

A) `tup.index(value, 2)`  
B) `tup.index(value)[1]`  
C) `tup.index(value, first_index + 1)`  
D) `tup.count(value, 2)`

**Correct Answer: C**

*Explanation: To find the second occurrence, first find the first occurrence, then use the start parameter: `first = tup.index(value)` followed by `second = tup.index(value, first + 1)`. This tells index() to start searching after the first occurrence. Option A would start at index 2, not find the 2nd occurrence.*

---

### Question 5
Which method is safer to use without error handling?

A) index()  
B) count()  
C) Both are equally safe  
D) Neither is safe

**Correct Answer: B**

*Explanation: count() is safer because it never raises an exception - it simply returns 0 if the value is not found. The index() method, on the other hand, raises ValueError if the value doesn't exist, requiring try-except or a preliminary count() check for safe usage.*

---

### Bonus Question
Given `numbers = (5, 10, 5, 15, 5)`, what is the output of `numbers.count(5) + numbers.index(5)`?

A) 3  
B) 4  
C) 5  
D) 8

**Correct Answer: A**

*Explanation: `numbers.count(5)` returns 3 (three occurrences of 5), and `numbers.index(5)` returns 0 (first occurrence at index 0). Therefore, 3 + 0 = 3. This demonstrates that count() returns how many times a value appears, while index() returns the position of the first occurrence.*
