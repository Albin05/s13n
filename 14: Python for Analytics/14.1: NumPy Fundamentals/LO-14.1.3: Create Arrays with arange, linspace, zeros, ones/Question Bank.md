## Question Bank: Create Arrays with arange, linspace, zeros, ones

### Q1: Create Array Using arange (3 minutes, Low Difficulty)

**Problem:**
Use `np.arange()` to create an array of even numbers from 2 to 20 (inclusive). Print the array.

**Expected Output:**
```
[ 2  4  6  8 10 12 14 16 18 20]
```

---

### Q2: Create Array Using linspace (3 minutes, Low Difficulty)

**Problem:**
Use `np.linspace()` to create an array of exactly 7 evenly-spaced values between 0 and 1 (both inclusive). Print the array.

**Expected Output:**
```
[0.         0.16666667 0.33333333 0.5        0.66666667 0.83333333
 1.        ]
```

---

### Q3: Create 2D Zero and One Arrays (5 minutes, Medium Difficulty)

**Problem:**
Create two 2D arrays:
1. A 4x5 array filled with zeros
2. A 3x3 array filled with ones

Print both arrays and their shapes.

**Expected Output:**
```
Zeros array:
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
Shape: (4, 5)

Ones array:
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
Shape: (3, 3)
```

---

### Q4: Temperature Scale Conversion (5 minutes, Medium Difficulty)

**Problem:**
Create an array of Celsius temperatures from 0°C to 100°C with steps of 10°C using `np.arange()`. Then convert these temperatures to Fahrenheit using the formula: F = (C × 9/5) + 32. Print both arrays.

**Expected Output:**
```
Celsius:    [  0  10  20  30  40  50  60  70  80  90 100]
Fahrenheit: [ 32.  50.  68.  86. 104. 122. 140. 158. 176. 194. 212.]
```

---

### Q5: Create Multiplication Table (5 minutes, Medium Difficulty)

**Problem:**
Create a 10x10 multiplication table using array creation functions:
1. Use `np.arange()` to create arrays from 1 to 10
2. Use broadcasting to create the multiplication table
3. Print the resulting table

Hint: You can reshape or use outer operations.

**Expected Output:**
```
[[  1   2   3   4   5   6   7   8   9  10]
 [  2   4   6   8  10  12  14  16  18  20]
 [  3   6   9  12  15  18  21  24  27  30]
 [  4   8  12  16  20  24  28  32  36  40]
 [  5  10  15  20  25  30  35  40  45  50]
 [  6  12  18  24  30  36  42  48  54  60]
 [  7  14  21  28  35  42  49  56  63  70]
 [  8  16  24  32  40  48  56  64  72  80]
 [  9  18  27  36  45  54  63  72  81  90]
 [ 10  20  30  40  50  60  70  80  90 100]]
```
