### **1. Find First Even**

Write a program that finds and prints the first even number from a list, then stops.

Given list: `[1, 3, 5, 8, 9, 11]`

**Expected Output:**
```
Found: 8
```

**Hint:** Use break when you find the first even number (num % 2 == 0).

---

---

### **2. Skip Odd Numbers**

Print only even numbers from 1 to 10 using continue to skip odd numbers.

**Expected Output:**
```
2
4
6
8
10
```

**Hint:** Use continue when `num % 2 != 0` to skip odd numbers.

---

---

### **3. Search for Name**

Search for "Alice" in a list of names and print "Found!" when you find it.

Given list: `["Bob", "Charlie", "Alice", "David"]`

**Expected Output:**
```
Checking Bob
Checking Charlie
Checking Alice
Found!
```

**Hint:** Loop through names, print "Checking {name}", use break when name == "Alice".

---

---

### **4. Skip Negative Numbers**

Print only positive numbers from a list, skipping negative ones.

Given list: `[5, -2, 8, -7, 3, -1, 9]`

**Expected Output:**
```
5
8
3
9
```

**Hint:** Use continue when `num < 0` to skip negative numbers.

---

---

### **5. First Vowel**

Find the first vowel in a string and print its position.

Given string: `"Python"`

**Expected Output:**
```
First vowel: o at position 4
```

**Hint:** Loop with enumerate(), check if char in "aeiouAEIOU", use break.

---

---

### **6. Sum Until Negative**

Calculate sum of numbers until you encounter a negative number.

Given list: `[5, 10, 15, -3, 20, 25]`

**Expected Output:**
```
Sum: 30
```

**Hint:** Use break when encountering a negative number.

---

---

### **7. Skip Multiples of 3**

Print numbers 1 to 20, but skip multiples of 3.

**Expected Output:**
```
1 2 4 5 7 8 10 11 13 14 16 17 19 20
```

**Hint:** Use `range(1, 21)` and continue when `num % 3 == 0`.

---

---

### **8. Find Target in Range**

Search for the number 7 in range 1 to 10. Print all numbers until you find 7.

**Expected Output:**
```
1 2 3 4 5 6 7
Found target!
```

**Hint:** Loop through range, print each number, break when i == 7.

---

---

### **9. Password Validator**

Check if a password has at least 8 characters. If it does, print "Valid". Stop checking after finding the first valid password.

Given passwords: `["abc", "pass123", "SecurePassword", "123"]`

**Expected Output:**
```
Checking: abc
Checking: pass123
Checking: SecurePassword
Valid password found!
```

**Hint:** Use break when `len(password) >= 8`.

---

---

### **10. Skip Spaces**

Print each character in a string except spaces.

Given string: `"Hello World"`

**Expected Output:**
```
H e l l o W o r l d
```

**Hint:** Loop through string, use continue when `char == " "`.

---

---

### **11. First Duplicate**

Find the first number that appears more than once in a list.

Given list: `[1, 2, 3, 4, 2, 5]`

**Expected Output:**
```
First duplicate: 2
```

**Hint:** Use a set to track seen numbers, break when number already in set.

---

---

### **12. Loop with Else**

Search for a number greater than 10 in a list. If found, print it. If not found (loop completes), print "No large number found".

Test with two lists:
- List 1: `[2, 4, 6, 8]`
- List 2: `[2, 4, 15, 8]`

**Expected Output:**
```
List 1:
No large number found

List 2:
Found large number: 15
```

**Hint:** Use for-else clause. The else runs only if loop completes without break.

---

---

### **13. Count Until Condition**

Count how many numbers you can process before encountering a number divisible by 7.

Given list: `[1, 3, 5, 9, 11, 14, 16, 18]`

**Expected Output:**
```
Processed 5 numbers before stopping
```

**Hint:** Use counter variable, increment in loop, break when `num % 7 == 0`.

---

---

### **14. Skip Short Words**

Print words with 5 or more letters, skip shorter words.

Given list: `["Hi", "Python", "is", "amazing", "for", "coding"]`

**Expected Output:**
```
Python
amazing
coding
```

**Hint:** Use continue when `len(word) < 5`.

---

---

### **15. Nested Loop Break**

Find a number in a 2D list and print its position (row, col).

Given 2D list: `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
Target: `5`

**Expected Output:**
```
Found 5 at row 1, col 1
```

**Hint:** Nested loops with flag variable or return from function to break both loops.

---

---

### **16. Remove Consecutive Duplicates**

Print a list without consecutive duplicates.

Given list: `[1, 1, 2, 2, 2, 3, 4, 4, 5]`

**Expected Output:**
```
1 2 3 4 5
```

**Hint:** Track previous value, use continue when `num == prev`.

---

---

### **17. Validate All Even**

Check if all numbers in a list are even. If you find an odd number, stop and print "Not all even".

Test with two lists:
- List 1: `[2, 4, 6, 8]`
- List 2: `[2, 4, 5, 8]`

**Expected Output:**
```
List 1:
All numbers are even

List 2:
Not all even (found 5)
```

**Hint:** Use for-else with break when odd number found.

---

---

### **18. Interactive Search**

Search for multiple targets in a list. For each target, find and print its index. Stop searching if target is not found.

Given list: `[10, 20, 30, 40, 50]`
Targets: `[20, 50, 60]`

**Expected Output:**
```
20 found at index 1
50 found at index 4
60 not found - stopping search
```

**Hint:** Outer loop for targets, inner loop for search, break outer when target not found.

---

---

### **19. Skip Range**

Print numbers from 1 to 20, but skip numbers 8 through 12 (inclusive).

**Expected Output:**
```
1 2 3 4 5 6 7 13 14 15 16 17 18 19 20
```

**Hint:** Use continue when `8 <= num <= 12`.

---

---

### **20. First Prime Number**

Find the first prime number in a list of numbers.

Given list: `[4, 6, 8, 9, 11, 15, 17]`

**Expected Output:**
```
First prime: 11
```

**Hint:** Create is_prime check with loop, use break in main loop when prime found.

---

---

### **21. Matrix Row Sum**

Calculate sum of each row in a 2D list, but stop if any row sum exceeds 20.

Given matrix:
```python
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

**Expected Output:**
```
Row 0 sum: 6
Row 1 sum: 15
Row 2 sum: 24 - exceeds limit, stopping
```

**Hint:** Outer loop for rows, calculate sum, break if sum > 20.

---

---

### **22. Skip Vowels in String**

Print each character in a string except vowels.

Given string: `"Education"`

**Expected Output:**
```
d c t n
```

**Hint:** Use continue when `char.lower() in "aeiou"`.

---

---

### **23. First N Evens**

Print the first 5 even numbers from a range of 1 to 50.

**Expected Output:**
```
2 4 6 8 10
```

**Hint:** Use counter, break when counter reaches 5.

---

---

### **24. Dictionary Search**

Search for a key in a dictionary. If found, print its value and stop.

Given dict: `{"name": "Alice", "age": 25, "city": "NYC"}`
Search key: `"age"`

**Expected Output:**
```
Found age: 25
```

**Hint:** Loop through dict.items(), break when key matches.

---

---

### **25. Skip Empty Strings**

Print non-empty strings from a list.

Given list: `["Hello", "", "World", "", "Python"]`

**Expected Output:**
```
Hello
World
Python
```

**Hint:** Use continue when string is empty (`not word` or `word == ""`).

---

---

### **26. Break on Condition Sum**

Add numbers from 1 to N, but stop when sum exceeds 100. Print the last number added.

**Expected Output:**
```
Sum exceeded 100 at number: 14
Total sum: 105
```

**Hint:** Loop through range, track sum, break when sum > 100.

---

---

### **27. Continue Pattern**

Print numbers 1 to 15, but skip numbers that are divisible by 2 OR 3.

**Expected Output:**
```
1 5 7 11 13
```

**Hint:** Use continue when `num % 2 == 0 or num % 3 == 0`.

---

---

### **28. Nested Continue**

Print a multiplication table for 1-5, but skip results that are multiples of 5.

**Expected Output:**
```
1x1=1  1x2=2  1x3=3  1x4=4
2x1=2  2x2=4  2x3=6  2x4=8
3x1=3  3x2=6  3x3=9  3x4=12
4x1=4  4x2=8  4x3=12 4x4=16
```

**Hint:** Nested loops with continue when `i * j % 5 == 0`.

---

---

### **29. String Pattern Break**

Find the first word in a sentence that starts with a capital letter.

Given string: `"hello world Python Programming"`
(Split into words)

**Expected Output:**
```
First capitalized word: Python
```

**Hint:** Split string, loop through words, break when `word[0].isupper()`.

---

---

### **30. Combined Break and Continue**

Print numbers 1 to 30 with these rules:
- Skip multiples of 3
- Stop when you reach a multiple of 17

**Expected Output:**
```
1 2 4 5 7 8 10 11 13 14 16
```

**Hint:** Use continue for multiples of 3, break for multiples of 17.

---

---

### **31. Validate List**

Check if a list contains only positive numbers. Print "Invalid" and stop if you find a non-positive number.

Test lists:
- List 1: `[5, 10, 15, 20]`
- List 2: `[5, 10, -5, 20]`

**Expected Output:**
```
List 1:
All positive

List 2:
Invalid: -5
```

**Hint:** Use for-else with break when non-positive found.

---

---

### **32. Character Counter**

Count consonants in a string (skip vowels and spaces).

Given string: `"Hello World"`

**Expected Output:**
```
Consonants: 7
```

**Hint:** Use continue to skip vowels and spaces, count others.

---

---

### **33. Early Exit Search**

Search for "exit" command in a list. Stop processing when found.

Given list: `["start", "run", "exit", "stop", "end"]`

**Expected Output:**
```
Processing: start
Processing: run
Exit command found!
```

**Hint:** Loop through commands, print each, break on "exit".

---

---

### **34. Range with Both**

Print squares of numbers 1 to 20, but:
- Skip perfect cubes (1, 8, 27...)
- Stop at first number whose square exceeds 200

**Expected Output:**
```
4 9 16 25 36 49 64 81 100 121 144 169 196
Stopped at 15 (square = 225)
```

**Hint:** Check if cube root is integer for skip, break when square > 200.

---

---

### **35. Nested Break with Flag**

Search for a target value in a 2D list. Print "Found" or "Not found" for entire matrix.

Given matrix: `[[1, 2], [3, 4], [5, 6]]`
Target: `4`

**Expected Output:**
```
Searching row 0...
Searching row 1...
Found at row 1, col 1!
```

**Hint:** Use flag variable to track if found, break inner loop, check flag to break outer.

---

## Key Patterns to Practice

### Break Patterns
1. **Early exit**: Stop when condition met
2. **Search**: Find first occurrence
3. **Limit**: Stop at threshold
4. **Validation**: Stop on invalid input
5. **Loop-else**: Detect if loop completed naturally

### Continue Patterns
1. **Filter**: Skip unwanted items
2. **Validation**: Skip invalid data
3. **Pattern matching**: Skip non-matches
4. **Conditional processing**: Process only certain items
5. **Error handling**: Skip errors, continue with rest

### Combined Usage
1. **Skip some, stop on condition**: Continue for filter, break for limit
2. **Nested loops**: Break inner, continue outer (or vice versa)
3. **Complex conditions**: Multiple continue/break points

## Common Mistakes to Avoid

1. **Break in wrong scope**: Break only exits innermost loop
2. **Continue without condition**: Infinite loop if not careful
3. **Forgetting else clause**: for-else executes if NO break occurred
4. **Multiple breaks**: Only first break executes
5. **Break in nested loops**: Only breaks inner loop, not outer
6. **Using return instead of break**: Changes function behavior
7. **Unreachable code after break**: Code after break never runs

## Best Practices

```python
# Good: Clear break condition
for item in items:
    if item == target:
        print("Found!")
        break
    process(item)

# Good: Continue for filtering
for num in numbers:
    if num < 0:
        continue
    print(num)

# Good: For-else pattern
for item in items:
    if item == target:
        print("Found")
        break
else:
    print("Not found")

# Good: Flag for nested loops
found = False
for row in matrix:
    for item in row:
        if item == target:
            found = True
            break
    if found:
        break
```

## Control Flow Summary

```python
# Break: Exit loop immediately
for i in range(10):
    if i == 5:
        break  # Stops at 5
    print(i)  # Prints 0, 1, 2, 3, 4

# Continue: Skip to next iteration
for i in range(5):
    if i == 2:
        continue  # Skips 2
    print(i)  # Prints 0, 1, 3, 4

# For-else: Runs if no break
for i in range(5):
    if i == 10:
        break
else:
    print("Completed")  # Runs because no break

# Combined
for i in range(10):
    if i % 2 == 0:
        continue  # Skip evens
    if i > 7:
        break  # Stop after 7
    print(i)  # Prints 1, 3, 5, 7
```

## Real-World Applications

1. **Search operations**: Finding items in collections
2. **Validation**: Checking data quality
3. **Filtering**: Processing selected items
4. **Early termination**: Stopping when goal reached
5. **Error handling**: Skipping bad data
6. **Game loops**: Exit on win/loss condition
7. **Menu systems**: Break on exit command
8. **Data processing**: Skip corrupted records
9. **Optimization**: Stop when good enough solution found
10. **User input**: Continue until valid input

## Practice Tips

1. **Understand scope**: Know which loop break/continue affects
2. **Use for-else**: Powerful pattern for search operations
3. **Clear conditions**: Make break/continue conditions obvious
4. **Avoid overuse**: Sometimes a better approach exists
5. **Test edge cases**: Empty lists, first/last items
6. **Nested loops**: Use flags or functions for clarity
7. **Comment intent**: Explain why breaking/continuing
8. **Combine wisely**: Can use both in same loop

---

