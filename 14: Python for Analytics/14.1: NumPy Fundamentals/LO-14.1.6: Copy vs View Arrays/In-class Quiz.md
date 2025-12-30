## In-class Quiz: Copy vs View Arrays

### Question 1
What happens when you execute `arr2 = arr1` where `arr1` is a NumPy array?

A) Creates an independent copy of `arr1`
B) Creates a view that shares memory with `arr1`
C) Creates an alias; both variables point to the same object
D) Raises an error

**Correct Answer: C**

---

### Question 2
How does NumPy slicing differ from Python list slicing?

A) They work exactly the same way
B) NumPy slicing creates a view; list slicing creates a copy
C) NumPy slicing creates a copy; list slicing creates a view
D) Both create copies

**Correct Answer: B**

---

### Question 3
Which method creates an independent copy of a NumPy array?

A) `arr2 = arr1`
B) `arr2 = arr1[:]`
C) `arr2 = arr1.copy()`
D) `arr2 = arr1.view()`

**Correct Answer: C**

---

### Question 4
What will be the value of `original` after this code?
```python
original = np.array([1, 2, 3, 4, 5])
view = original[1:3]
view[0] = 999
```

A) `[1, 2, 3, 4, 5]`
B) `[1, 999, 3, 4, 5]`
C) `[999, 2, 3, 4, 5]`
D) An error occurs

**Correct Answer: B**
*Explanation: Slicing creates a view, so modifying view[0] modifies original[1]*

---

### Question 5
Which function checks if two arrays share memory?

A) `np.is_same(arr1, arr2)`
B) `np.shares_memory(arr1, arr2)`
C) `arr1.shares(arr2)`
D) `arr1 == arr2`

**Correct Answer: B**
