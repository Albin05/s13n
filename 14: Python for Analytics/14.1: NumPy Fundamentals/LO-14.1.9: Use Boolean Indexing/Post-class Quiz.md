## Post-class Quiz: Use Boolean Indexing

### Question 1
What does `arr[arr > 5]` return?

A) A boolean array of True/False values
B) Indices of elements greater than 5
C) All elements from arr that are greater than 5
D) An error

**Correct Answer: C**
*Explanation: Boolean indexing filters and returns elements where condition is True*

---

### Question 2
Which operator is used for combining multiple conditions with AND logic?

A) `and`
B) `&`
C) `|`
D) `&&`

**Correct Answer: B**
*Explanation: `&` is the element-wise AND operator for NumPy boolean arrays*

---

### Question 3
What does `arr[(arr > 10) & (arr < 20)]` select?

A) Elements equal to 10 or 20
B) Elements greater than 10 or less than 20
C) Elements between 10 and 20 (exclusive)
D) All elements

**Correct Answer: C**
*Explanation: `&` combines conditions; both must be True (> 10 AND < 20)*

---

### Question 4
How do you modify all values greater than 100 to be exactly 100?

A) `arr[arr > 100] = 100`
B) `arr > 100 = 100`
C) `arr.replace(>100, 100)`
D) `arr[100] = arr[> 100]`

**Correct Answer: A**
*Explanation: Boolean indexing on left side selects elements to modify*

---

### Question 5
What does the `~` operator do in boolean indexing?

A) Combines conditions with OR
B) Combines conditions with AND
C) Inverts/negates the boolean condition
D) Counts True values

**Correct Answer: C**
*Explanation: `~` is the NOT operator, inverting True to False and vice versa*
