### **1. Count to 10**

Write a while loop that prints numbers from 1 to 10.

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

**Hint:** Initialize count = 1, loop while count <= 10, increment count each time.

---

---

### **2. Countdown from 5**

Write a program that counts down from 5 to 1, then prints "Blast off!"

**Expected Output:**
```
5
4
3
2
1
Blast off!
```

**Hint:** Start at 5, loop while > 0, decrement each iteration.

---

---

### **3. Sum Numbers Until 0**

Write a program that keeps asking for numbers and sums them. Stop when user enters 0.

**Example Interaction:**
```
Enter a number (0 to stop): 10
Enter a number (0 to stop): 20
Enter a number (0 to stop): 15
Enter a number (0 to stop): 0
Total: 45
```

**Hint:** Use sentinel value 0. Priming read before loop, read again at end of loop.

---

---

### **4. Password Validator**

Create a login system with maximum 3 attempts. Password is "python123". After 3 failed attempts, deny access.

**Example Output (correct on 2nd try):**
```
Enter password: wrong
Incorrect password
Enter password: python123
Access granted
```

**Hint:** Track attempts with counter, loop while password wrong AND attempts < max.

---

---

### **5. Find First Multiple of 7**

Write a program that finds and prints the first positive integer that is a multiple of 7.

**Expected Output:**
```
First multiple of 7: 7
```

**Hint:** Start at 1, loop while `number % 7 != 0`, increment number.

---

---

### **6. Guess the Number**

Create a number guessing game. Secret number is 42. Keep asking until user guesses correctly, providing "Too high" or "Too low" hints.

**Example Interaction:**
```
Guess the number: 50
Too high!
Guess again: 30
Too low!
Guess again: 42
Correct! You guessed it!
```

**Hint:** Loop while guess != secret, provide feedback inside loop.

---

---

### **7. Double Until Exceeds 1000**

Start with value = 1. Keep doubling it until it exceeds 1000. Print each value and count iterations.

**Expected Output:**
```
Iteration 0: 1
Iteration 1: 2
Iteration 2: 4
Iteration 3: 8
Iteration 4: 16
Iteration 5: 32
Iteration 6: 64
Iteration 7: 128
Iteration 8: 256
Iteration 9: 512
Final value: 1024
Total iterations: 10
```

**Hint:** Loop while value <= 1000, multiply value by 2 each time, track iterations.

---

---

### **8. Factorial Calculator**

Calculate factorial of 5 (5! = 5 × 4 × 3 × 2 × 1) using a while loop.

**Expected Output:**
```
5! = 120
```

**Hint:** factorial = 1, i = 1, loop while i <= n, multiply factorial by i.

---

---

### **9. Fibonacci Sequence**

Generate and print the first 10 Fibonacci numbers (0, 1, 1, 2, 3, 5, 8, 13, 21, 34).

**Expected Output:**
```
First 10 Fibonacci numbers:
0 1 1 2 3 5 8 13 21 34
```

**Hint:** Use two variables (a, b), simultaneous assignment: `a, b = b, a + b`.

---

---

### **10. Input Validation**

Ask user for age. Keep asking until they enter a valid age (0-120).

**Example Interaction:**
```
Enter your age (0-120): 150
Invalid age! Must be between 0 and 120
Enter your age (0-120): -5
Invalid age! Must be between 0 and 120
Enter your age (0-120): 25
Valid age entered: 25
```

**Hint:** Priming read, loop while invalid (age < 0 or age > 120).

---

---

### **11. Menu System**

Create an interactive menu that loops until user chooses to exit.

Options:
1. Option A
2. Option B
3. Option C
4. Exit

**Example Output:**
```
=== Menu ===
1. Option A
2. Option B
3. Option C
4. Exit
Enter choice: 1
You selected Option A

=== Menu ===
1. Option A
2. Option B
3. Option C
4. Exit
Enter choice: 4
Exiting...
Program ended
```

**Hint:** Loop while choice != "4", display menu each iteration, use if/elif for choices.

---

---

### **12. Find Digits Sum**

Given number 12345, find the sum of all its digits (1+2+3+4+5 = 15).

**Expected Output:**
```
Sum of digits: 15
```

**Hint:** Use `number % 10` to get last digit, `number //= 10` to remove it. Loop while number > 0.

---

---

### **13. Reverse a Number**

Reverse the digits of 12345 to get 54321.

**Expected Output:**
```
Reversed: 54321
```

**Hint:** Extract digits one by one, build reversed number: `reversed = reversed * 10 + digit`.

---

---

### **14. GCD Calculator**

Calculate the Greatest Common Divisor (GCD) of 48 and 18 using the Euclidean algorithm.

**Expected Output:**
```
GCD: 6
```

**Hint:** While b != 0, swap a and b, set b = a % b. Result is in a when loop ends.

---

---

### **15. Prime Number Checker**

Check if 29 is a prime number. A prime has no divisors except 1 and itself.

**Expected Output:**
```
29 is prime
```

**Hint:** Loop while `divisor * divisor <= number`, check if `number % divisor == 0`. Break if divisor found.

---

---

### **16. Collatz Sequence**

Starting with 10, apply Collatz rules until reaching 1:
- If even: divide by 2
- If odd: multiply by 3 and add 1

Print the sequence and count steps.

**Expected Output:**
```
Starting with 10:
10 → 5 → 16 → 8 → 4 → 2 → 1
Reached 1 in 6 steps
```

**Hint:** Loop while n != 1, apply rule based on n % 2.

---

---

### **17. Bank Account Simulator**

Simulate a bank account with initial balance $1000. Options:
1. Deposit
2. Withdraw
3. Quit

Validate transactions (positive amounts, sufficient balance).

**Example Interaction:**
```
Balance: $1000
1. Deposit
2. Withdraw
3. Quit
Choose action: 1
Deposit amount: $500
Deposited $500

Balance: $1500
1. Deposit
2. Withdraw
3. Quit
Choose action: 2
Withdraw amount: $200
Withdrew $200

Balance: $1300
1. Deposit
2. Withdraw
3. Quit
Choose action: 3
Thank you!
Final balance: $1300
```

**Hint:** Loop until action == "quit", validate amounts before updating balance.

---

---

### **18. Power Calculator Without ****

Calculate 2^5 without using the ** operator. Use repeated multiplication.

**Expected Output:**
```
2^5 = 32
```

**Hint:** result = 1, loop exponent times, multiply result by base each time.

---

---

### **19. String Character Counter**

Count how many times the letter 'l' appears in "hello world" using a while loop and indexing.

**Expected Output:**
```
'l' appears 3 times
```

**Hint:** Use index to access each character, loop while index < len(text).

---

---

### **20. Find Maximum in User Input**

Keep asking user for numbers until they enter "done". Find and print the maximum value entered.

**Example Interaction:**
```
Enter a number (or 'done'): 45
Enter a number (or 'done'): 12
Enter a number (or 'done'): 78
Enter a number (or 'done'): 23
Enter a number (or 'done'): done
Maximum value: 78
```

**Hint:** Use None for initial max_value, update if num > max_value. Handle "no numbers" case.

---

## Additional Practice Problems

#

---

### **21. Sum Even Numbers**

Sum all even numbers from 2 to 20 using a while loop.

**Expected Output:**
```
Sum: 110
```

---

#

---

### **22. Multiplication Table**

Print the multiplication table for 7 (7×1 through 7×10).

**Expected Output:**
```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
```

---

#

---

### **23. Count Vowels**

Count vowels in a given string using a while loop.

Test string: "Hello World"

**Expected Output:**
```
Vowel count: 3
```

**Hint:** Check if each character is in "aeiouAEIOU".

---

#

---

### **24. Digital Root**

Find the digital root of a number (keep summing digits until single digit remains).

For 38: 3+8=11, 1+1=2 → Digital root is 2

**Expected Output:**
```
Digital root of 38: 2
```

**Hint:** Outer loop while number >= 10, inner loop sums digits.

---

#

---

### **25. Binary Conversion**

Convert decimal number 13 to binary using a while loop.

**Expected Output:**
```
13 in binary: 1101
```

**Hint:** Repeatedly divide by 2, collect remainders, reverse at end.

---

