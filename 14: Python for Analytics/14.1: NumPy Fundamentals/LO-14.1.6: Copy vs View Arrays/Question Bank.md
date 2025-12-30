## Question Bank: Copy vs View Arrays

### Q1: Test Assignment Behavior (3 minutes, Low Difficulty)

**Problem:**
Create an array `arr1 = np.array([10, 20, 30, 40, 50])`. Create `arr2` by assigning `arr1` to it. Modify `arr2[0]` to 999. Print both arrays and use `np.shares_memory()` to check if they share memory.

**Expected Output:**
```
arr1: [999  20  30  40  50]
arr2: [999  20  30  40  50]
Shares memory: True
```

---

### Q2: Test Slicing Behavior (3 minutes, Low Difficulty)

**Problem:**
Create an array `arr = np.array([5, 10, 15, 20, 25, 30])`. Create a slice `sub` from indices 1 to 4. Modify `sub[0]` to 999. Print both arrays to demonstrate that slicing creates a view.

**Expected Output:**
```
Original array: [  5 999  15  20  25  30]
Slice: [999  15  20]
```

---

### Q3: Create Independent Copy (5 minutes, Medium Difficulty)

**Problem:**
Create an array `original = np.array([1, 2, 3, 4, 5])`. Create a true copy called `independent` using `.copy()`. Modify `independent[2]` to 100. Print both arrays and verify they don't share memory using `np.shares_memory()`.

**Expected Output:**
```
Original: [1 2 3 4 5]
Independent: [  1   2 100   4   5]
Shares memory: False
```

---

### Q4: Fix Unintended Modification (5 minutes, Medium Difficulty)

**Problem:**
Given this function that modifies the original array unintentionally:
```python
def double_values(arr):
    arr = arr * 2
    return arr
```

Test it with `data = np.array([10, 20, 30])`. Then create a corrected version `double_values_safe()` that uses `.copy()` to avoid modifying the original. Demonstrate both functions.

**Expected Output:**
```
Using unsafe function:
Original data after: [20 40 60]
Result: [20 40 60]

Using safe function:
Original data after: [10 20 30]
Result: [20 40 60]
```

---

### Q5: Detect View vs Copy (5 minutes, Medium Difficulty)

**Problem:**
Write a function `check_relationship(arr1, arr2)` that determines if two arrays are:
- "Same object" (using `is`)
- "View" (share memory but different objects)
- "Independent copy" (don't share memory)

Test with:
1. `a = np.array([1, 2, 3])` and `b = a`
2. `a = np.array([1, 2, 3])` and `b = a[:]`
3. `a = np.array([1, 2, 3])` and `b = a.copy()`

**Expected Output:**
```
Test 1: Same object
Test 2: View
Test 3: Independent copy
```
