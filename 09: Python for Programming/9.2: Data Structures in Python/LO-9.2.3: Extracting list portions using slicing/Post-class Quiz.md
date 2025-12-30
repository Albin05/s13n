## Post-class Quiz: Extracting List Portions Using Slicing

### Question 1
Given `lst = [10, 20, 30, 40, 50]`, what is `lst[1:4]`?

A) `[10, 20, 30]`
B) `[20, 30, 40]`
C) `[20, 30, 40, 50]`
D) `[10, 20, 30, 40]`

**Correct Answer: B**
*Explanation: lst[1:4] starts at index 1 (20) and stops before index 4. So it includes indices 1, 2, 3, which are [20, 30, 40]. Remember: stop index is exclusive*

---

### Question 2
What does `numbers[::-1]` do?

A) Returns the first element
B) Returns the last element
C) Reverses the list
D) Returns every other element

**Correct Answer: C**
*Explanation: The step of -1 means move backwards through the list. Starting from the end and going to the beginning with step -1 effectively reverses the entire list*

---

### Question 3
Given `data = [1, 2, 3, 4, 5, 6, 7, 8]`, what is `data[::2]`?

A) `[1, 2, 3, 4]`
B) `[2, 4, 6, 8]`
C) `[1, 3, 5, 7]`
D) `[1, 2]`

**Correct Answer: C**
*Explanation: [::2] means start at 0, go to the end, with step 2. This gives every second element starting from index 0: indices 0, 2, 4, 6 → [1, 3, 5, 7]*

---

### Question 4
What happens when you do `lst[2:2] = [10, 20]`?

A) Replaces elements at index 2
B) Inserts [10, 20] at index 2
C) Deletes element at index 2
D) Causes an error

**Correct Answer: B**
*Explanation: lst[2:2] is an empty slice at position 2. Assigning to an empty slice inserts the new elements at that position without replacing anything*

---

### Question 5
Given `lst = [0, 1, 2, 3, 4, 5]`, what is `lst[-3:-1]`?

A) `[3, 4, 5]`
B) `[3, 4]`
C) `[4, 5]`
D) `[2, 3, 4]`

**Correct Answer: B**
*Explanation: lst[-3] is index 3 (value 3), lst[-1] is index 5 (value 5). Slice [-3:-1] goes from index 3 up to (but not including) index 5, giving indices 3 and 4 → [3, 4]*
