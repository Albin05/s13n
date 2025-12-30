## Post-class Quiz: Stack, Split, and Concatenate Arrays

### Question 1
What is the difference between `np.concatenate()` and `np.stack()`?

A) They are the same function
B) concatenate joins along existing axis, stack creates new axis
C) stack is faster than concatenate
D) concatenate only works with 1D arrays

**Correct Answer: B**
*Explanation: np.concatenate() joins arrays along an existing axis, while np.stack() creates a new axis. For example, concatenating two (3,) arrays gives (6,), but stacking them gives (2, 3)*

---

### Question 2
Which function should you use to split an array that is NOT evenly divisible?

A) np.split()
B) np.vsplit()
C) np.array_split()
D) np.hsplit()

**Correct Answer: C**
*Explanation: np.array_split() allows unequal splits and won't raise an error if the array cannot be divided evenly. np.split() requires equal division*

---

### Question 3
What does `np.vstack([arr1, arr2])` do to two 1D arrays?

A) Concatenates them horizontally
B) Creates a 2D array with arrays as rows
C) Creates error - requires 2D arrays
D) Stacks them along axis=1

**Correct Answer: B**
*Explanation: np.vstack() stacks arrays vertically, creating a 2D array where each input array becomes a row. arr1=[1,2,3] and arr2=[4,5,6] become [[1,2,3], [4,5,6]]*

---

### Question 4
Given `arr.shape = (6, 4)`, what will be the shape after `np.hsplit(arr, 2)`?

A) Two arrays of shape (6, 2)
B) Two arrays of shape (3, 4)
C) One array of shape (6, 2)
D) Error - cannot split

**Correct Answer: A**
*Explanation: np.hsplit() splits along axis=1 (columns). Splitting 4 columns by 2 gives two arrays each with shape (6, 2)*

---

### Question 5
What is the result shape when stacking three arrays of shape (4,) with `np.stack([a, b, c], axis=1)`?

A) (3, 4)
B) (4, 3)
C) (12,)
D) Error - invalid axis

**Correct Answer: B**
*Explanation: np.stack() with axis=1 creates shape (4, 3). The original dimension 4 becomes first dimension, and stacking 3 arrays creates second dimension of 3*
