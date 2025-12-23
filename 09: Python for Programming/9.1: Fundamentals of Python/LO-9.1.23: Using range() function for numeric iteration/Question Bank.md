### **1. Count to 10**

Write a program that prints numbers from 1 to 10 using range().

**Expected Output:**
```
1
2
3
4
5
6
7
8
9
10
```

**Hint:** Use `range(1, 11)` - remember the stop value is exclusive.

---

---

### **2. Count to 5**

Write a program that prints numbers from 0 to 4 using range() with a single argument.

**Expected Output:**
```
0
1
2
3
4
```

**Hint:** `range(5)` generates 5 numbers starting from 0.

---

---

### **3. Sum Numbers 1 to 100**

Calculate the sum of all numbers from 1 to 100 using range() and a for loop.

**Expected Output:**
```
Sum: 5050
```

**Hint:** Initialize total = 0, then use `range(1, 101)` to iterate and add each number.

---

---

### **4. Even Numbers**

Print all even numbers from 0 to 10 using range() with a step parameter.

**Expected Output:**
```
0
2
4
6
8
10
```

**Hint:** Use `range(0, 11, 2)` - step of 2 creates even numbers.

---

---

### **5. Countdown from 10**

Create a countdown from 10 to 1 using range() with a negative step.

**Expected Output:**
```
10
9
8
7
6
5
4
3
2
1
Blast off!
```

**Hint:** `range(10, 0, -1)` counts backwards. Don't forget to print "Blast off!" after the loop.

---

---

### **6. Multiples of 5**

Print all multiples of 5 from 5 to 50 using range().

**Expected Output:**
```
5
10
15
20
25
30
35
40
45
50
```

**Hint:** Use `range(5, 51, 5)` - start at 5, step by 5.

---

---

### **7. Create List of Squares**

Create a list containing squares of numbers from 1 to 5 using range().

**Expected Output:**
```
Squares: [1, 4, 9, 16, 25]
```

**Hint:** Initialize empty list, iterate `range(1, 6)`, append `i**2` to the list.

---

---

### **8. Index with Range**

Given a list of fruits, print each fruit with its index using range().

Given list: `["apple", "banana", "orange"]`

**Expected Output:**
```
Index 0: apple
Index 1: banana
Index 2: orange
```

**Hint:** Use `range(len(fruits))` to generate indices 0, 1, 2.

---

---

### **9. Nested Range Loops**

Print all coordinate pairs for a 3×3 grid using nested range loops.

**Expected Output:**
```
(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)
```

**Hint:** Outer loop: `range(1, 4)`, inner loop: `range(1, 4)`, use `end=" "` for inner, `print()` after inner loop completes.

---

---

### **10. Skip Numbers**

Print every 3rd number from 0 to 20 using range().

**Expected Output:**
```
0
3
6
9
12
15
18
```

**Hint:** Use `range(0, 20, 3)` - step of 3 skips by threes.

---

---

### **11. Reverse Range**

Print numbers from 5 down to 1 using range().

**Expected Output:**
```
5
4
3
2
1
```

**Hint:** `range(5, 0, -1)` - start at 5, stop before 0, step -1.

---

---

### **12. Multiplication Table**

Generate a multiplication table for the number 7 (from 7×1 to 7×10) using range().

**Expected Output:**
```
7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
7 × 4 = 28
7 × 5 = 35
7 × 6 = 42
7 × 7 = 49
7 × 8 = 56
7 × 9 = 63
7 × 10 = 70
```

**Hint:** Use `range(1, 11)` and multiply 7 by each number i.

---

---

### **13. Generate Fibonacci**

Generate the first 10 Fibonacci numbers using range().

**Expected Output:**
```
0 1 1 2 3 5 8 13 21 34
```

**Hint:** Use `range(10)` for 10 iterations. Initialize a=0, b=1, print a, then swap: a, b = b, a+b.

---

---

### **14. Factorial with Range**

Calculate the factorial of 5 using range().

**Expected Output:**
```
5! = 120
```

**Hint:** Initialize factorial = 1, use `range(1, n+1)` where n=5, multiply factorial by each i.

---

---

### **15. Pattern Printing**

Print a triangle pattern of stars using nested range loops.

**Expected Output:**
```
*
**
***
****
*****
```

**Hint:** Outer loop `range(1, 6)`, inner loop `range(i)`, print "*" with `end=""`, then `print()` for newline.

---

---

### **16. Sum Odd Numbers**

Calculate the sum of all odd numbers from 1 to 20 using range().

**Expected Output:**
```
Sum of odds 1-20: 100
```

**Hint:** Use `range(1, 21, 2)` to get odd numbers, accumulate the sum.

---

---

### **17. Power Table**

Create a table showing powers of 2 from 2^0 to 2^10 using range().

**Expected Output:**
```
2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64
2^7 = 128
2^8 = 256
2^9 = 512
2^10 = 1024
```

**Hint:** Use `range(0, 11)` for exponents, calculate `2 ** exp` for each.

---

---

### **18. List Reversal with Range**

Reverse a list by accessing elements in reverse order using range().

Given list: `[10, 20, 30, 40, 50]`

**Expected Output:**
```
Reversed: [50, 40, 30, 20, 10]
```

**Hint:** Use `range(len(numbers)-1, -1, -1)` to get indices 4, 3, 2, 1, 0. Append `numbers[i]` to new list.

---

---

### **19. Skip Pattern**

Print every 7th number from 0 to 50 using range().

**Expected Output:**
```
0 7 14 21 28 35 42 49
```

**Hint:** Use `range(0, 50, 7)` - step of 7, `end=" "` for horizontal output.

---

---

### **20. Grid Coordinates**

Print coordinates for a 3×4 grid (3 rows, 4 columns) using nested range loops.

**Expected Output:**
```
(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
```

**Hint:** Outer loop `range(3)` for rows, inner loop `range(4)` for columns.

---

---

### **21. Count Down Timer**

Create a countdown timer from 5 to 0 using range().

**Expected Output:**
```
5
4
3
2
1
0
Time's up!
```

**Hint:** Use `range(5, -1, -1)` to include 0. Print "Time's up!" after the loop.

---

---

### **22. Odd Numbers Only**

Print all odd numbers from 1 to 19 using range().

**Expected Output:**
```
1 3 5 7 9 11 13 15 17 19
```

**Hint:** `range(1, 20, 2)` - start at 1 (odd), step by 2.

---

---

### **23. Sum First n Numbers**

Calculate the sum of the first n numbers where n=50.

**Expected Output:**
```
Sum of first 50 numbers: 1275
```

**Hint:** Use `range(1, n+1)` where n=50, accumulate sum.

---

---

### **24. Multiples of 3**

Print all multiples of 3 from 3 to 30 using range().

**Expected Output:**
```
3 6 9 12 15 18 21 24 27 30
```

**Hint:** `range(3, 31, 3)` - start at 3, step by 3.

---

---

### **25. Reverse Alphabet Positions**

Print numbers from 26 down to 1 (like reverse alphabet positions) using range().

**Expected Output:**
```
26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
```

**Hint:** `range(26, 0, -1)`, use `end=" "` for horizontal output.

---

---

### **26. Squares Pattern**

Print the squares of numbers from 1 to 10 on one line.

**Expected Output:**
```
1 4 9 16 25 36 49 64 81 100
```

**Hint:** Use `range(1, 11)`, print `i**2` with `end=" "`.

---

---

### **27. Every 5th Number**

Print every 5th number from 0 to 100 using range().

**Expected Output:**
```
0 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
```

**Hint:** `range(0, 101, 5)` - step of 5.

---

---

### **28. Countdown from 100 by 10s**

Count down from 100 to 0 by tens using range().

**Expected Output:**
```
100 90 80 70 60 50 40 30 20 10 0
```

**Hint:** `range(100, -1, -10)` - start 100, stop before -1, step -10.

---

---

### **29. Nested Multiplication**

Create a simple multiplication grid (1-5) using nested range loops.

**Expected Output:**
```
1  2  3  4  5
2  4  6  8  10
3  6  9  12 15
4  8  12 16 20
5  10 15 20 25
```

**Hint:** Outer `range(1, 6)` for i, inner `range(1, 6)` for j, print `i*j` with proper spacing.

---

---

### **30. Sum Even Numbers**

Calculate the sum of all even numbers from 2 to 100 using range().

**Expected Output:**
```
Sum of evens 2-100: 2550
```

**Hint:** Use `range(2, 101, 2)` to get even numbers, accumulate sum.

---

## Additional Practice Problems

#

---

### **31. Range Length**

How many numbers are generated by `range(10, 20)`?

**Expected Answer:** 10 numbers (10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

**Hint:** Stop is exclusive, so 20 is not included. Count: 20-10 = 10.

---

#

---

### **32. Empty Range**

What does `range(5, 5)` generate?

**Expected Answer:** Empty range (no numbers)

**Hint:** When start equals stop, range is empty.

---

#

---

### **33. Negative Numbers**

Print numbers from -5 to 5 using range().

**Expected Output:**
```
-5 -4 -3 -2 -1 0 1 2 3 4 5
```

**Hint:** `range(-5, 6)` - start at -5, stop before 6.

---

#

---

### **34. Every Other Number**

Print every other number from 1 to 20 using range().

**Expected Output:**
```
1 3 5 7 9 11 13 15 17 19
```

**Hint:** `range(1, 21, 2)` - step of 2 skips every other.

---

#

---

### **35. Backward Evens**

Print even numbers from 20 down to 0 using range().

**Expected Output:**
```
20 18 16 14 12 10 8 6 4 2 0
```

**Hint:** `range(20, -1, -2)` - start 20, stop before -1, step -2.

---

## Key Patterns to Practice

1. **Single argument**: `range(n)` for n iterations (0 to n-1)
2. **Two arguments**: `range(start, stop)` for custom range
3. **Three arguments**: `range(start, stop, step)` for custom increment
4. **Negative step**: Count backwards
5. **Step by 2**: Get evens or odds
6. **Step by n**: Get multiples of n
7. **Nested ranges**: 2D patterns and grids
8. **range(len())**: Generate list indices
9. **Inclusive ranges**: `range(1, n+1)` for 1 to n
10. **Reverse order**: Negative step with start > stop

## Common Mistakes to Avoid

1. **Forgetting exclusive stop**: `range(10)` is 0-9, not 0-10
2. **Wrong backward range**: `range(10, 1)` is empty, need negative step
3. **Off-by-one**: For 1-10, use `range(1, 11)` not `range(1, 10)`
4. **Float arguments**: range() only accepts integers
5. **Missing step for reverse**: Can't count down without negative step
6. **Step of 0**: Causes infinite loop error
7. **Assuming inclusive**: Stop is always exclusive

## Formulas to Remember

```python
# n iterations (0 to n-1)
range(n)

# a to b inclusive
range(a, b+1)

# All indices of a list
range(len(my_list))

# Evens from 0 to n
range(0, n+1, 2)

# Odds from 1 to n
range(1, n+1, 2)

# Countdown from n to 1
range(n, 0, -1)

# Countdown from n to 0 (inclusive)
range(n, -1, -1)

# Multiples of k up to n
range(k, n+1, k)

# Reverse indices of list
range(len(my_list)-1, -1, -1)
```

## Tips for Success

1. **Always remember**: Stop value is **exclusive**
2. **Default start**: 0 if not specified
3. **Default step**: 1 if not specified
4. **Negative step**: Required for counting backwards
5. **Test edge cases**: Empty ranges, single value ranges
6. **Visualize**: Draw the sequence before coding
7. **Count carefully**: Off-by-one errors are common
8. **Use step creatively**: For patterns (evens, odds, multiples)
9. **Nested ranges**: Useful for grids and tables
10. **Practice**: The more you use range(), the more intuitive it becomes

---

