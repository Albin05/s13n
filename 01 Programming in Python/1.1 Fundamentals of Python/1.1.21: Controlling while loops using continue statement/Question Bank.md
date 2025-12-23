# Question Bank: Controlling While Loops Using Continue Statement

## Problem 1: Skip Even Numbers (Easy)

Write a program that prints odd numbers from 1 to 10 using a while loop and continue.

**Expected Output:**
```
1
3
5
7
9
```

**Hint:** Increment first, then check if even (`num % 2 == 0`), use continue to skip.

---

## Problem 2: Print Positive Numbers Only (Easy)

Given a list of numbers, print only the positive ones using continue to skip negatives.

Given list: `[5, -3, 8, -1, 12, -7, 4]`

**Expected Output:**
```
5
8
12
4
```

**Hint:** Use for loop, check if `num < 0`, continue to skip negative.

---

## Problem 3: Skip Vowels (Easy)

Print all consonants from the word "python" by skipping vowels.

**Expected Output:**
```
p
y
t
h
n
```

**Hint:** Check if `char in "aeiou"`, use continue to skip vowels.

---

## Problem 4: Sum Non-Zero Numbers (Easy)

Calculate the sum of all non-zero numbers from a list using continue to skip zeros.

Given list: `[10, 0, 5, 0, 8, 0, 3]`

**Expected Output:**
```
Sum: 26
```

**Hint:** If `num == 0`, continue. Otherwise add to total.

---

## Problem 5: Skip Multiples of 5 (Medium)

Print numbers from 1 to 20, but skip all multiples of 5.

**Expected Output:**
```
1 2 3 4 6 7 8 9 11 12 13 14 16 17 18 19
```

**Hint:** Check if `num % 5 == 0`, use continue to skip.

---

## Problem 6: Filter Empty Strings (Medium)

Given a list of strings, print only non-empty ones.

Given list: `["hello", "", "world", "", "python", ""]`

**Expected Output:**
```
hello
world
python
```

**Hint:** If `word == ""`, continue. Otherwise print.

---

## Problem 7: Count Consonants (Medium)

Count the number of consonants in "hello world" by skipping vowels and spaces.

**Expected Output:**
```
Consonants: 7
```

**Hint:** If `char in "aeiou "`, continue. Otherwise increment counter.

---

## Problem 8: Skip Range (Medium)

Print numbers 1-20 except numbers from 8 to 12 (inclusive).

**Expected Output:**
```
1 2 3 4 5 6 7 13 14 15 16 17 18 19 20
```

**Hint:** Use condition `8 <= num <= 12`, continue if in this range.

---

## Problem 9: Process Valid Commands (Hard)

Keep asking for 5 commands. If user enters "skip", don't count it and ask again.

**Example Interaction:**
```
Command 1: hello
Command 2: skip
Command 2: world
Command 3: python
Command 4: skip
Command 4: code
Command 5: test
All commands collected!
```

**Hint:** Use while loop with counter. If command == "skip", continue (don't increment).

---

## Problem 10: Sum Positive Numbers (Hard)

Calculate sum and average of positive numbers only from a list.

Given list: `[10, -5, 20, -3, 15, -8, 5]`

**Expected Output:**
```
Positive sum: 50
Positive count: 4
Average: 12.5
```

**Hint:** Skip negatives with continue, accumulate sum and count for positives.

---

## Problem 11: Skip Invalid Grades (Hard)

Given grades including invalid entries (negative or > 100), calculate valid grade statistics.

Given grades: `[85, -1, 92, 150, 78, -1, 95, 88]`

**Expected Output:**
```
Valid grades: 5
Average: 87.6
Highest: 95
```

**Hint:** Skip if `grade < 0 or grade > 100`, collect valid ones, calculate stats.

---

## Problem 12: Data Cleaning (Hard)

Filter sensor readings, removing error values (-999) and calculate average.

Given readings: `[22.5, -999, 23.1, -999, 21.8, 24.2]`

**Expected Output:**
```
Valid readings: 4
Average: 22.9°C
```

**Hint:** If `reading == -999`, continue. Collect valid readings, compute average.

---

## Problem 13: Username Validation (Hard)

From a list of usernames, print only those that are alphanumeric (no special characters or digits).

Given usernames: `["alice", "b0b", "charlie", "d@ve", "eve123", "frank"]`

**Expected Output:**
```
Valid usernames:
alice
charlie
frank
```

**Hint:** Use `name.isalpha()` to check. Continue if contains digits or special chars.

---

## Problem 14: Skip Based on Multiple Conditions (Very Hard)

Print numbers 1-20, but skip:
- Even numbers less than 10
- Odd numbers greater than 15

**Expected Output:**
```
1 3 5 7 9 10 11 12 13 14 15
```

**Hint:** Two continue statements with different conditions.

---

## Problem 15: Process User Input with Validation (Very Hard)

Keep asking for numbers until user enters "done". Skip invalid (non-numeric) input without counting it.

**Example Interaction:**
```
Enter number (or 'done'): 10
Total: 10
Enter number (or 'done'): abc
Invalid input, try again
Enter number (or 'done'): 20
Total: 30
Enter number (or 'done'): xyz
Invalid input, try again
Enter number (or 'done'): done
Final total: 30
Count: 2
```

**Hint:** Use `while True`, break on "done", continue on invalid, process valid numbers.

---

## Problem 16: Filter Word Lengths (Very Hard)

From a sentence, collect words that are between 4 and 7 characters long (inclusive).

Given sentence: "the quick brown fox jumps over the lazy dog"

**Expected Output:**
```
Words (4-7 chars): quick, brown, jumps, over, lazy
Count: 5
```

**Hint:** Split sentence, check length, continue if too short or too long.

---

## Problem 17: Matrix Non-Zero Sum (Very Hard)

Calculate sum and average of all non-zero values in a 2D matrix.

Given matrix:
```python
matrix = [
    [1, 0, 3],
    [0, 5, 6],
    [7, 8, 0]
]
```

**Expected Output:**
```
Non-zero sum: 30
Non-zero count: 6
Average: 5.0
```

**Hint:** Nested loops, continue when value is 0, accumulate others.

---

## Problem 18: Skip Digits in String (Very Hard)

Remove all digits from a string and print the cleaned version.

Given string: "h3ll0 w0rld 2023!"

**Expected Output:**
```
Cleaned: hll wrld !
```

**Hint:** Iterate through characters, if `char.isdigit()`, continue. Build result string.

---

## Problem 19: Temperature Range Filter (Very Hard)

Process temperature readings. Skip:
- Error readings (-999)
- Out of range readings (< -50 or > 50)

Given readings: `[22.5, -999, 23.1, 150, 21.8, -999, 24.2, -10]`

**Expected Output:**
```
Valid readings: [22.5, 23.1, 21.8, 24.2, -10]
Count: 5
Average: 18.3°C
```

**Hint:** Two continues - one for error, one for range. Collect valid, calculate average.

---

## Problem 20: Complex Number Filter (Very Hard)

From a list, process only numbers that are:
- Positive
- Not divisible by 3
- Less than 50

Given list: `[5, -3, 12, 18, 25, 60, 7, 30, 45, 11]`

**Expected Output:**
```
Filtered numbers: [5, 25, 7, 11]
Sum: 48
```

**Hint:** Multiple continue statements for each skip condition.

---

## Problem 21: Nested Loop Filtering (Very Hard)

Print multiplication table for 1-5, but skip any product that is a multiple of 6.

**Example Output:**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
2 x 1 = 2
2 x 2 = 4
2 x 4 = 8
2 x 5 = 10
...
(skips 2x3=6, 3x2=6, 3x4=12, etc.)
```

**Hint:** Nested loops, calculate product, if `product % 6 == 0`, continue.

---

## Problem 22: Skip File Extensions (Hard)

From a list of filenames, print only those that don't end with ".tmp" or ".log".

Given files: `["data.txt", "temp.tmp", "info.log", "report.pdf", "cache.tmp", "notes.txt"]`

**Expected Output:**
```
data.txt
report.pdf
notes.txt
```

**Hint:** Check if filename ends with ".tmp" or ".log", continue to skip.

---

## Problem 23: Collect Valid Ages (Very Hard)

Keep asking for ages until user enters "done". Skip invalid ages (< 0 or > 120) without counting them.

**Example Interaction:**
```
Enter age (or 'done'): 25
Valid age added
Enter age (or 'done'): 150
Invalid age, skipped
Enter age (or 'done'): -5
Invalid age, skipped
Enter age (or 'done'): 30
Valid age added
Enter age (or 'done'): done

Valid ages collected: 2
Ages: [25, 30]
Average age: 27.5
```

**Hint:** while True with break on "done", continue on invalid age, collect valid ones.

---

## Problem 24: Skip Pattern in Grid (Very Hard)

Print a coordinate grid (0,0 to 4,4) but skip coordinates where x equals y (diagonal).

**Expected Output:**
```
0,1 0,2 0,3 0,4
1,0 1,2 1,3 1,4
2,0 2,1 2,3 2,4
3,0 3,1 3,2 3,4
4,0 4,1 4,2 4,3
```

**Hint:** Nested loops for x and y, if `x == y`, continue.

---

## Problem 25: Grade Letter Calculator (Very Hard)

From a list of numeric grades, calculate statistics skipping invalid entries (< 0 or > 100), and convert valid ones to letter grades.

Given grades: `[85, -1, 92, 105, 78, 0, 95, 88]`

**Expected Output:**
```
Valid grades: 5
A: 3 students
B: 2 students
Average: 87.6
```

**Hint:** Skip invalid with continue. For valid: count letter grades (A≥90, B≥80), calculate average.

---

## Additional Practice Problems

### Problem 26: Remove Duplicates (Medium)

Print each number only once from a list, skipping duplicates.

Given: `[1, 2, 2, 3, 1, 4, 3, 5]`

**Expected Output:**
```
1
2
3
4
5
```

**Hint:** Use a set to track seen numbers, continue if already seen.

---

### Problem 27: Process Menu with Validation (Hard)

Create a calculator menu. Skip invalid choices without counting them.

**Example:**
```
Calculator:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Choice: 9
Invalid choice!
Choice: 1
Enter numbers: 10 5
Result: 15
Choice: 5
Goodbye!
```

**Hint:** while True, break on "5", continue on invalid choice.

---

### Problem 28: Two-Stage Filter (Very Hard)

From a list of strings, print only those that:
- Are longer than 3 characters
- Don't contain digits

Given: `["cat", "hello", "a1b", "world", "xy", "test123", "python"]`

**Expected Output:**
```
hello
world
python
```

**Hint:** First continue for length, second continue for digits check.

---

## Key Patterns to Practice

1. **Single filter**: Skip one type of unwanted item
2. **Multiple filters**: Several continue statements for complex filtering
3. **Data validation**: Skip invalid while processing valid
4. **Input retry**: Continue without counting on bad input
5. **Nested loops**: Continue affects innermost loop only
6. **Data cleaning**: Remove errors, outliers, empty values
7. **Range exclusion**: Skip values within a range
8. **Condition combination**: Skip based on multiple conditions

## Common Mistakes to Avoid

1. Forgetting to increment before continue in while loop (infinite loop)
2. Using continue when break is needed (want to exit, not skip)
3. Not understanding continue only affects current iteration
4. Placing increment after continue in while loop
5. Confusing which loop continue affects in nested loops
