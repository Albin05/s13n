## Post-class Quiz: Iterating Through Lists Using Loops

### Question 1
What does `enumerate(['a', 'b', 'c'])` return when used in a for loop?

A) Just the values: 'a', 'b', 'c'
B) Just the indices: 0, 1, 2
C) Tuples of (index, value): (0,'a'), (1,'b'), (2,'c')
D) A dictionary: {0:'a', 1:'b', 2:'c'}

**Correct Answer: C**
*Explanation: enumerate() returns an iterator of tuples where each tuple contains (index, value). In a for loop, you typically unpack these as `for i, val in enumerate(list):`*

---

### Question 2
Given `list1 = [1, 2, 3]` and `list2 = [4, 5]`, what happens with `for a, b in zip(list1, list2):`?

A) Error because lists have different lengths
B) Loops 3 times, using None for missing b value
C) Loops 2 times, stopping at shortest list
D) Loops 3 times, repeating last b value

**Correct Answer: C**
*Explanation: zip() stops when the shortest input iterable is exhausted. Here it will only process (1,4) and (2,5), ignoring the 3 from list1*

---

### Question 3
What is wrong with this code?
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
```

A) Nothing, it works correctly
B) It modifies the list while iterating, causing unpredictable behavior
C) remove() doesn't work in a for loop
D) The condition is wrong

**Correct Answer: B**
*Explanation: Modifying a list while iterating over it can cause elements to be skipped. When you remove an element, the iterator doesn't adjust, so it may skip the next element. Use `for num in numbers[:]` to iterate over a copy, or use list comprehension instead*

---

### Question 4
How do you iterate through a list and get a 1-based position number?

A) `for i in range(len(lst)):`
B) `for i, val in enumerate(lst, start=1):`
C) `for i, val in enumerate(lst) + 1:`
D) `for i in lst.index():`

**Correct Answer: B**
*Explanation: enumerate() accepts a start parameter. enumerate(lst, start=1) will begin counting from 1 instead of 0. You can unpack as `for i, val in enumerate(lst, start=1):`*

---

### Question 5
What is the output?
```python
lst = [1, 2, 3]
for i, val in enumerate(lst):
    lst[i] = val * 2
print(lst)
```

A) `[1, 2, 3]` - unchanged
B) `[2, 4, 6]` - doubled
C) Error - can't modify while iterating
D) `[1, 4, 9]` - squared

**Correct Answer: B**
*Explanation: It's safe to modify list elements by index while iterating. enumerate() gives us the index i, and we use it to update lst[i]. Each value gets doubled, resulting in [2, 4, 6]*
