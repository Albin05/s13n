## Post-class Quiz: Creating and Using Sets

---

### Question 1
What is the output of the following code?

```python
my_set = {1, 2, 3, 2, 1}
print(len(my_set))
```

A) 5  
B) 3  
C) 2  
D) Error

**Correct Answer: B**

*Explanation: Sets automatically remove duplicates. The set {1, 2, 3, 2, 1} contains only unique elements: {1, 2, 3}. Therefore, len(my_set) returns 3. This is one of the fundamental properties of sets - they only store unique values.*

---

### Question 2
Which of the following correctly creates an empty set?

A) `empty = {}`  
B) `empty = set()`  
C) `empty = []`  
D) `empty = ()`

**Correct Answer: B**

*Explanation: `set()` is the correct way to create an empty set. `{}` creates an empty dictionary, not a set. `[]` creates an empty list, and `()` creates an empty tuple. This is a common pitfall - you must use the set() constructor for empty sets.*

---

### Question 3
What is the result of the following set operation?

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1 & set2
print(result)
```

A) `{1, 2, 3, 4, 5, 6}`  
B) `{3, 4}`  
C) `{1, 2}`  
D) `{5, 6}`

**Correct Answer: B**

*Explanation: The `&` operator performs set intersection, which returns only elements that appear in BOTH sets. Both set1 and set2 contain 3 and 4, so the result is {3, 4}. Option A would be the union (|), C would be set1 - set2, and D would be set2 - set1.*

---

### Question 4
Which statement about sets is FALSE?

A) Sets can contain duplicate elements  
B) Sets are unordered collections  
C) Set membership testing is very fast (O(1))  
D) Set elements must be immutable (hashable)

**Correct Answer: A**

*Explanation: Sets CANNOT contain duplicate elements - they automatically maintain uniqueness. All other statements are true: sets are unordered (no guaranteed order), membership testing is O(1) average case (very fast), and elements must be immutable/hashable (you can't put lists in sets, but you can put tuples).*

---

### Question 5
What does the following code output?

```python
fruits = {'apple', 'banana'}
fruits.add('orange')
fruits.add('apple')
fruits.discard('grape')
print(len(fruits))
```

A) 2  
B) 3  
C) 4  
D) Error

**Correct Answer: B**

*Explanation: Starting with 2 elements {'apple', 'banana'}, add('orange') adds orange (now 3 elements). add('apple') does nothing because apple already exists. discard('grape') does nothing because grape doesn't exist (discard doesn't raise an error). Final set: {'apple', 'banana', 'orange'} with length 3.*

---

### Bonus Question
What is the output of this code?

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2
print(result)
```

A) `{3}`  
B) `{1, 2, 4, 5}`  
C) `{1, 2, 3, 4, 5}`  
D) `{1, 2, 3, 3, 4, 5}`

**Correct Answer: C**

*Explanation: The `|` operator performs set union, which combines all elements from both sets (without duplicates). The union of {1, 2, 3} and {3, 4, 5} is {1, 2, 3, 4, 5}. Note that 3 appears in both sets but is only included once in the result. Option D is impossible because sets cannot contain duplicates.*

