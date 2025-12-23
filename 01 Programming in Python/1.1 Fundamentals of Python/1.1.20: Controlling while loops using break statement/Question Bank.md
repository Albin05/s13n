# Question Bank: Controlling While Loops Using Break Statement

## Problem 1: Find First Even Number (Easy)

Write a program that finds and prints the first even number from a list, then stops.

Given list: `[1, 3, 5, 8, 9, 11, 13]`

**Expected Output:**
```
First even number: 8
```

**Hint:** Use a for loop to iterate through the list. When you find an even number (`num % 2 == 0`), print it and use `break` to exit.

---

## Problem 2: Search for Target Word (Easy)

Search for the word "python" in a list of words. Print "Found!" and stop when you find it.

Given list: `["java", "javascript", "python", "ruby", "go"]`

**Expected Output:**
```
Found python!
```

**Hint:** Iterate through the list, check if word equals "python", then break.

---

## Problem 3: Stop at Negative (Easy)

Print numbers from a list until you encounter a negative number. Stop immediately when you find one.

Given list: `[10, 20, 30, -5, 40, 50]`

**Expected Output:**
```
10
20
30
Negative number found, stopping
```

**Hint:** Loop through list, check if `num < 0`, print message and break.

---

## Problem 4: Count Until Threshold (Easy)

Count from 1 upward. Stop when you reach 5.

**Expected Output:**
```
1
2
3
4
5
```

**Hint:** Use a while loop with a counter. When counter reaches 5, print it and break.

---

## Problem 5: Exit on Command (Medium)

Create a simple command loop that keeps asking for input until user types "exit".

**Example Interaction:**
```
Enter command (or 'exit'): hello
You entered: hello
Enter command (or 'exit'): world
You entered: world
Enter command (or 'exit'): exit
Goodbye!
```

**Hint:** Use `while True:` with break when input equals "exit".

---

## Problem 6: Find First Divisor (Medium)

Find and print the first number (greater than 1) that divides 100 evenly.

**Expected Output:**
```
First divisor of 100: 2
```

**Hint:** Loop from 2 to 99, check if `100 % i == 0`, break when found.

---

## Problem 7: Sum Until Zero (Medium)

Keep asking for numbers and summing them. When user enters 0, stop and show the total.

**Example Interaction:**
```
Enter number (0 to stop): 10
Enter number (0 to stop): 25
Enter number (0 to stop): 15
Enter number (0 to stop): 0
Total sum: 50
```

**Hint:** Use `while True:`, check if number is 0, break and print total.

---

## Problem 8: Password System (Medium)

Create a login system with exactly 3 attempts. Correct password is "secret123". If user gets it right, grant access and stop. If all attempts fail, deny access.

**Example Output (correct on 2nd try):**
```
Attempt 1/3
Enter password: wrong
Incorrect

Attempt 2/3
Enter password: secret123
Access granted!
```

**Hint:** Use while loop with attempts counter. Break when correct password entered. Use loop-else for "access denied".

---

## Problem 9: Find Vowel (Medium)

Find and print the first vowel in the word "python". Stop searching after finding it.

**Expected Output:**
```
First vowel: o
```

**Hint:** Iterate through string, check if character is in "aeiou", break when found.

---

## Problem 10: Stop on Condition (Hard)

Given a list of numbers, calculate their running sum. Stop when the sum exceeds 50 and print the final sum.

Given list: `[10, 15, 12, 8, 20, 5]`

**Expected Output:**
```
Running sum: 10
Running sum: 25
Running sum: 37
Running sum: 45
Sum exceeded 50: 65
```

**Hint:** Keep adding to total. After each addition, check if total > 50, then break.

---

## Problem 11: Prime Number Checker with Break (Hard)

Check if a number is prime by searching for divisors. Use break to stop as soon as a divisor is found. Use the loop-else pattern.

Test with number: 29

**Expected Output:**
```
29 is prime
```

Test with number: 15

**Expected Output:**
```
15 is not prime
```

**Hint:** Loop from 2 to sqrt(number). If divisor found, print "not prime" and break. Use else clause to print "is prime".

---

## Problem 12: Menu System (Hard)

Create a menu with 4 options. Loop until user chooses to quit (option 4).

Options:
1. Say Hello
2. Say Goodbye
3. Show Time
4. Quit

**Example Interaction:**
```
=== Menu ===
1. Say Hello
2. Say Goodbye
3. Show Time
4. Quit
Choice: 1
Hello!

=== Menu ===
1. Say Hello
2. Say Goodbye
3. Show Time
4. Quit
Choice: 4
Exiting program
```

**Hint:** Use `while True:`, display menu, get choice, use if/elif for options, break on choice 4.

---

## Problem 13: Nested Loop with Break (Hard)

Find the first pair of numbers whose product equals 24 from two ranges (1-6). Stop searching when found.

**Expected Output:**
```
Found: 4 x 6 = 24
```

**Hint:** Nested loops for i and j. When `i * j == 24`, print result, set flag, break inner loop. Check flag to break outer loop.

---

## Problem 14: Search Until Found or Exhausted (Hard)

Search for number 7 in a list. If found, print position and stop. If not found after checking all, print "not found".

Given list: `[3, 5, 1, 7, 9, 2]`

**Expected Output:**
```
Found 7 at position 3
```

Given list: `[3, 5, 1, 9, 2]`

**Expected Output:**
```
7 not found in list
```

**Hint:** Use enumerate() or counter. Break when found. Use loop-else for "not found" message.

---

## Problem 15: Validate Age Input (Hard)

Keep asking for age until user enters a valid age (0-120). Use break to exit when valid.

**Example Interaction:**
```
Enter age (0-120): 150
Invalid! Try again.
Enter age (0-120): -5
Invalid! Try again.
Enter age (0-120): 25
Valid age: 25
```

**Hint:** Use `while True:`, check if `0 <= age <= 120`, break if valid, otherwise continue loop.

---

## Problem 16: Find First Palindrome (Very Hard)

Given a list of words, find and print the first palindrome (word that reads same forwards and backwards).

Given list: `["hello", "world", "level", "python", "radar"]`

**Expected Output:**
```
First palindrome: level
```

**Hint:** For each word, check if `word == word[::-1]`. Break when found.

---

## Problem 17: Two Sum Problem (Very Hard)

Find two numbers in a list that add up to a target sum. Stop when first pair is found.

Given list: `[2, 7, 11, 15, 3]`
Target sum: 9

**Expected Output:**
```
Found: 2 + 7 = 9
```

**Hint:** Nested loops. Outer loop picks first number, inner loop picks second. Check if sum equals target, use flag to break both loops.

---

## Problem 18: Guessing Game with Hints (Very Hard)

Create a number guessing game. Secret number is 42. Give "too high" or "too low" hints. Allow maximum 5 attempts.

**Example Interaction:**
```
Attempt 1/5
Guess the number: 50
Too high!

Attempt 2/5
Guess the number: 30
Too low!

Attempt 3/5
Guess the number: 42
Correct! You won in 3 attempts!
```

**Hint:** Use while loop with attempts counter. Break when correct. Use loop-else to handle "out of attempts" case.

---

## Problem 19: Process Commands Until Stop (Very Hard)

Process a list of commands. Stop when you encounter "STOP". Count how many commands were processed.

Given commands: `["START", "PROCESS", "EXECUTE", "STOP", "DELETE", "END"]`

**Expected Output:**
```
Processing: START
Processing: PROCESS
Processing: EXECUTE
Stop command found
Commands processed: 3
```

**Hint:** Loop through list with counter. Break when command equals "STOP". Print counter after loop.

---

## Problem 20: Search Matrix (Very Hard)

Search for a target value in a 2D matrix (list of lists). Stop searching as soon as you find it.

Given matrix:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
Target: 5

**Expected Output:**
```
Found 5 at row 1, column 1
```

**Hint:** Nested loops for rows and columns. When value found, print position, set flag, break inner loop. Check flag to break outer loop.

---

## Problem 21: ATM Simulation (Very Hard)

Simulate an ATM with initial balance $500. Provide options to deposit, withdraw, check balance, or exit. Validate transactions.

**Example Interaction:**
```
=== ATM ===
Balance: $500

1. Deposit
2. Withdraw
3. Check Balance
4. Exit

Choice: 1
Amount: $200
Deposited $200

=== ATM ===
Balance: $700

1. Deposit
2. Withdraw
3. Check Balance
4. Exit

Choice: 2
Amount: $100
Withdrew $100

=== ATM ===
Balance: $600

1. Deposit
2. Withdraw
3. Check Balance
4. Exit

Choice: 4
Thank you! Final balance: $600
```

**Hint:** Use `while True:` with menu. Track balance. Validate withdraw (don't allow overdraft). Break on exit choice.

---

## Problem 22: Username Validator (Very Hard)

Keep asking for username until it meets all criteria:
- Length between 3 and 15 characters
- Only alphanumeric characters
- Doesn't start with a number

**Example Interaction:**
```
Enter username: ab
Too short! Must be 3-15 characters

Enter username: hello@world
Invalid characters! Alphanumeric only

Enter username: 123user
Cannot start with number!

Enter username: john123
Username accepted: john123
```

**Hint:** Use `while True:`, check each condition separately, provide specific feedback, break only when all conditions pass.

---

## Problem 23: Find Longest Word (Very Hard)

Find the first word longer than 6 characters in a list. Stop searching when found.

Given list: `["cat", "dog", "elephant", "fish", "giraffe"]`

**Expected Output:**
```
First long word: elephant (8 letters)
```

**Hint:** Loop through words, check `len(word) > 6`, break when found. Use loop-else if none found.

---

## Problem 24: Calculator with Exit (Very Hard)

Create a simple calculator that loops until user chooses to quit. Support add, subtract, multiply, divide.

**Example Interaction:**
```
=== Calculator ===
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Choice: 1
Enter first number: 10
Enter second number: 5
Result: 15

=== Calculator ===
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Choice: 5
Goodbye!
```

**Hint:** Use `while True:`, get choice and numbers, perform operation, break on quit choice.

---

## Problem 25: Collect Until Sentinel (Very Hard)

Collect numbers into a list until user enters -1 (sentinel value). Then print statistics: count, sum, and average.

**Example Interaction:**
```
Enter number (-1 to finish): 10
Enter number (-1 to finish): 20
Enter number (-1 to finish): 30
Enter number (-1 to finish): 40
Enter number (-1 to finish): -1

Statistics:
Count: 4
Sum: 100
Average: 25.0
```

**Hint:** Use `while True:`, append valid numbers to list, break on -1, calculate statistics after loop.

---

## Additional Practice Problems

### Problem 26: Find First Uppercase (Medium)

Find the first uppercase letter in a string and print its position.

Test string: "hello World"

**Expected Output:**
```
First uppercase 'W' at position 6
```

**Hint:** Use enumerate() to get index, check `char.isupper()`, break when found.

---

### Problem 27: Shopping Cart (Very Hard)

Create a shopping system where users can:
1. Add item (with price)
2. View cart
3. Checkout (show total and exit)

**Example:**
```
=== Shopping Cart ===
1. Add item
2. View cart
3. Checkout

Choice: 1
Item name: Apple
Price: $2.50
Added Apple

Choice: 1
Item name: Banana
Price: $1.50
Added Banana

Choice: 2
Cart:
- Apple: $2.50
- Banana: $1.50

Choice: 3
Total: $4.00
Thank you for shopping!
```

**Hint:** Use list to store items/prices, `while True:` for menu, break on checkout.

---

### Problem 28: Password Strength Checker (Hard)

Keep asking for password until it meets requirements:
- At least 8 characters
- Contains at least one digit
- Contains at least one uppercase letter

**Example:**
```
Enter password: short
Too short! Must be at least 8 characters

Enter password: lowercase
Must contain at least one digit

Enter password: nodigit1
Must contain at least one uppercase letter

Enter password: ValidPass1
Password accepted!
```

**Hint:** Check each requirement, give specific feedback, break when all pass.

---

## Key Patterns to Practice

1. **Search and Stop**: Find first item matching condition
2. **while True + break**: Clean menu systems
3. **Loop-else**: Detect if break occurred
4. **Nested break**: Use flag variable
5. **Validation**: Keep asking until valid input
6. **Sentinel values**: Stop on special value
7. **Counter with break**: Limited attempts
8. **Early exit**: Stop when threshold reached

## Common Mistakes to Avoid

1. Forgetting to use break (infinite loop in `while True:`)
2. Breaking too early (before processing current item)
3. Assuming break exits all nested loops (only exits innermost)
4. Not handling loop-else correctly (runs when NO break)
5. Breaking without providing feedback to user
