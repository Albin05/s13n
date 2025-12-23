# Editorials: Controlling For Loops with Break and Continue

## Problem 1: Find First Even

**Problem:** Write a program that finds and prints the first even number from a list, then stops.

**Solution:**
```python
numbers = [1, 3, 5, 8, 9, 11]

for num in numbers:
    if num % 2 == 0:
        print(f"Found: {num}")
        break
```

**Output:**
```
Found: 8
```

**Explanation:**
- Loop through each number in the list
- Check if the number is even using `num % 2 == 0`
- When we find the first even number (8), print it and use `break` to exit the loop
- Break immediately stops the loop execution, so we don't check 9 or 11

**Key Concept:** Break exits the loop as soon as the condition is met, useful for search operations.

---

## Problem 2: Skip Odd Numbers

**Problem:** Print only even numbers from 1 to 10 using continue to skip odd numbers.

**Solution:**
```python
for num in range(1, 11):
    if num % 2 != 0:
        continue
    print(num)
```

**Output:**
```
2
4
6
8
10
```

**Explanation:**
- Loop through numbers 1 to 10
- If number is odd (`num % 2 != 0`), use `continue` to skip to next iteration
- Continue skips the print statement for odd numbers
- Only even numbers reach the print statement

**Alternative Solution:**
```python
for num in range(1, 11):
    if num % 2 == 0:
        print(num)
```

**Key Concept:** Continue skips the current iteration and moves to the next one, useful for filtering.

---

## Problem 3: Search for Name

**Problem:** Search for "Alice" in a list of names and print "Found!" when you find it.

**Solution:**
```python
names = ["Bob", "Charlie", "Alice", "David"]

for name in names:
    print(f"Checking {name}")
    if name == "Alice":
        print("Found!")
        break
```

**Output:**
```
Checking Bob
Checking Charlie
Checking Alice
Found!
```

**Explanation:**
- Loop through each name in the list
- Print "Checking" message for each name
- When we find "Alice", print "Found!" and break
- David is never checked because break exits the loop

**Key Concept:** Break is useful for early exit when you've found what you're looking for.

---

## Problem 4: Skip Negative Numbers

**Problem:** Print only positive numbers from a list, skipping negative ones.

**Solution:**
```python
numbers = [5, -2, 8, -7, 3, -1, 9]

for num in numbers:
    if num < 0:
        continue
    print(num)
```

**Output:**
```
5
8
3
9
```

**Explanation:**
- Loop through all numbers
- If number is negative (`num < 0`), use continue to skip it
- Only positive numbers get printed
- Continue acts as a filter, skipping unwanted values

**Key Concept:** Continue is perfect for filtering out unwanted values while processing the rest.

---

## Problem 5: First Vowel

**Problem:** Find the first vowel in a string and print its position.

**Solution:**
```python
text = "Python"
vowels = "aeiouAEIOU"

for index, char in enumerate(text):
    if char in vowels:
        print(f"First vowel: {char} at position {index}")
        break
```

**Output:**
```
First vowel: o at position 4
```

**Explanation:**
- Use `enumerate()` to get both index and character
- Check if character is in vowels string
- When found, print the vowel and its position, then break
- Position 4 means it's the 5th character (0-indexed)

**Key Concept:** Enumerate provides index-value pairs, useful for position-based searches.

---

## Problem 6: Sum Until Negative

**Problem:** Calculate sum of numbers until you encounter a negative number.

**Solution:**
```python
numbers = [5, 10, 15, -3, 20, 25]
total = 0

for num in numbers:
    if num < 0:
        break
    total += num

print(f"Sum: {total}")
```

**Output:**
```
Sum: 30
```

**Explanation:**
- Initialize total to 0
- Loop through numbers, adding each to total
- When we encounter -3 (first negative), break immediately
- Total = 5 + 10 + 15 = 30
- Numbers after -3 are never processed

**Key Concept:** Break can stop processing based on a condition, even mid-collection.

---

## Problem 7: Skip Multiples of 3

**Problem:** Print numbers 1 to 20, but skip multiples of 3.

**Solution:**
```python
for num in range(1, 21):
    if num % 3 == 0:
        continue
    print(num, end=' ')
```

**Output:**
```
1 2 4 5 7 8 10 11 13 14 16 17 19 20
```

**Explanation:**
- Loop through 1 to 20
- Check if number is divisible by 3 (`num % 3 == 0`)
- If yes, continue skips the print statement
- Multiples of 3 (3, 6, 9, 12, 15, 18) are skipped
- All other numbers are printed

**Key Concept:** Continue can filter based on mathematical conditions.

---

## Problem 8: Find Target in Range

**Problem:** Search for the number 7 in range 1 to 10. Print all numbers until you find 7.

**Solution:**
```python
for i in range(1, 11):
    print(i, end=' ')
    if i == 7:
        print("\nFound target!")
        break
```

**Output:**
```
1 2 3 4 5 6 7
Found target!
```

**Explanation:**
- Loop through range 1 to 10
- Print each number
- When we reach 7, print success message and break
- Numbers 8, 9, 10 are never processed

**Key Concept:** You can perform actions before breaking from a loop.

---

## Problem 9: Password Validator

**Problem:** Check if a password has at least 8 characters. Stop checking after finding the first valid password.

**Solution:**
```python
passwords = ["abc", "pass123", "SecurePassword", "123"]

for password in passwords:
    print(f"Checking: {password}")
    if len(password) >= 8:
        print("Valid password found!")
        break
```

**Output:**
```
Checking: abc
Checking: pass123
Checking: SecurePassword
Valid password found!
```

**Explanation:**
- Loop through each password
- Print which password we're checking
- Check if length is at least 8 characters
- "SecurePassword" has 14 characters, so it's valid
- Break immediately, "123" is never checked

**Key Concept:** Break saves processing time by stopping once requirement is met.

---

## Problem 10: Skip Spaces

**Problem:** Print each character in a string except spaces.

**Solution:**
```python
text = "Hello World"

for char in text:
    if char == " ":
        continue
    print(char, end=' ')
```

**Output:**
```
H e l l o W o r l d
```

**Explanation:**
- Loop through each character in the string
- If character is a space, continue skips it
- All other characters are printed
- Space between "Hello" and "World" is skipped

**Key Concept:** Continue is useful for filtering specific characters from strings.

---

## Problem 11: First Duplicate

**Problem:** Find the first number that appears more than once in a list.

**Solution:**
```python
numbers = [1, 2, 3, 4, 2, 5]
seen = set()

for num in numbers:
    if num in seen:
        print(f"First duplicate: {num}")
        break
    seen.add(num)
```

**Output:**
```
First duplicate: 2
```

**Explanation:**
- Use a set to track numbers we've seen
- For each number, check if it's already in the set
- If yes, it's a duplicate - print and break
- If no, add it to the set and continue
- First occurrence of 2 is added to set, second occurrence triggers duplicate detection

**Key Concept:** Sets provide O(1) lookup for efficient duplicate detection.

---

## Problem 12: Loop with Else

**Problem:** Search for a number greater than 10. Use for-else to handle "not found" case.

**Solution:**
```python
# List 1
numbers1 = [2, 4, 6, 8]
print("List 1:")
for num in numbers1:
    if num > 10:
        print(f"Found large number: {num}")
        break
else:
    print("No large number found")

print()

# List 2
numbers2 = [2, 4, 15, 8]
print("List 2:")
for num in numbers2:
    if num > 10:
        print(f"Found large number: {num}")
        break
else:
    print("No large number found")
```

**Output:**
```
List 1:
No large number found

List 2:
Found large number: 15
```

**Explanation:**
- The `else` clause of a for loop executes ONLY if the loop completes without encountering a break
- List 1: No number > 10, so loop completes naturally and else executes
- List 2: 15 > 10, so we break, and else does NOT execute
- This is a clean way to handle "search not found" scenarios

**Key Concept:** For-else provides elegant handling of search success/failure.

---

## Problem 13: Count Until Condition

**Problem:** Count how many numbers you can process before encountering a number divisible by 7.

**Solution:**
```python
numbers = [1, 3, 5, 9, 11, 14, 16, 18]
count = 0

for num in numbers:
    if num % 7 == 0:
        break
    count += 1

print(f"Processed {count} numbers before stopping")
```

**Output:**
```
Processed 5 numbers before stopping
```

**Explanation:**
- Initialize counter to 0
- For each number, check if divisible by 7
- If yes (14), break immediately
- If no, increment counter
- We process 1, 3, 5, 9, 11 (5 numbers) before hitting 14
- Counter gives us the count before break

**Key Concept:** Counters can track how many iterations occurred before break.

---

## Problem 14: Skip Short Words

**Problem:** Print words with 5 or more letters, skip shorter words.

**Solution:**
```python
words = ["Hi", "Python", "is", "amazing", "for", "coding"]

for word in words:
    if len(word) < 5:
        continue
    print(word)
```

**Output:**
```
Python
amazing
coding
```

**Explanation:**
- Loop through each word
- Check word length
- If less than 5 characters, continue skips it
- "Hi" (2), "is" (2), "for" (3) are skipped
- "Python" (6), "amazing" (7), "coding" (6) are printed

**Key Concept:** Continue can filter based on string properties like length.

---

## Problem 15: Nested Loop Break

**Problem:** Find a number in a 2D list and print its position (row, col).

**Solution:**
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 5
found = False

for row_idx, row in enumerate(matrix):
    for col_idx, num in enumerate(row):
        if num == target:
            print(f"Found {target} at row {row_idx}, col {col_idx}")
            found = True
            break
    if found:
        break
```

**Output:**
```
Found 5 at row 1, col 1
```

**Explanation:**
- Use nested loops with enumerate to track positions
- Inner loop checks each element in a row
- When target found, set flag and break inner loop
- After inner loop, check flag and break outer loop if needed
- Without flag, only inner loop would break, outer would continue
- Position (1, 1) means second row, second column (0-indexed)

**Key Concept:** Breaking nested loops requires a flag variable or function return.

---

## Problem 16: Remove Consecutive Duplicates

**Problem:** Print a list without consecutive duplicates.

**Solution:**
```python
numbers = [1, 1, 2, 2, 2, 3, 4, 4, 5]
prev = None

for num in numbers:
    if num == prev:
        continue
    print(num, end=' ')
    prev = num
```

**Output:**
```
1 2 3 4 5
```

**Explanation:**
- Track previous value with variable
- For each number, check if it equals previous
- If yes, continue skips it (consecutive duplicate)
- If no, print it and update previous
- First 1: prev is None, so print it, prev becomes 1
- Second 1: equals prev, skip it
- First 2: different from prev (1), print it, prev becomes 2
- And so on...

**Key Concept:** Tracking previous values helps detect consecutive patterns.

---

## Problem 17: Validate All Even

**Problem:** Check if all numbers in a list are even. Stop if you find an odd number.

**Solution:**
```python
# List 1
numbers1 = [2, 4, 6, 8]
print("List 1:")
for num in numbers1:
    if num % 2 != 0:
        print(f"Not all even (found {num})")
        break
else:
    print("All numbers are even")

print()

# List 2
numbers2 = [2, 4, 5, 8]
print("List 2:")
for num in numbers2:
    if num % 2 != 0:
        print(f"Not all even (found {num})")
        break
else:
    print("All numbers are even")
```

**Output:**
```
List 1:
All numbers are even

List 2:
Not all even (found 5)
```

**Explanation:**
- Check each number for oddness
- If odd number found, print message and break
- If loop completes (no odd found), else clause prints success
- List 1: All even, loop completes, else executes
- List 2: 5 is odd, break occurs, else doesn't execute
- This validates "all" condition efficiently

**Key Concept:** For-else elegantly handles "all elements match" validation.

---

## Problem 18: Interactive Search

**Problem:** Search for multiple targets in a list. Stop if any target is not found.

**Solution:**
```python
numbers = [10, 20, 30, 40, 50]
targets = [20, 50, 60]

for target in targets:
    for index, num in enumerate(numbers):
        if num == target:
            print(f"{target} found at index {index}")
            break
    else:
        print(f"{target} not found - stopping search")
        break
```

**Output:**
```
20 found at index 1
50 found at index 4
60 not found - stopping search
```

**Explanation:**
- Outer loop iterates through targets
- Inner loop searches for each target in numbers
- If target found, break inner loop (else doesn't execute)
- If inner loop completes without break, target not found
- The else clause of inner loop breaks outer loop
- 20 found at index 1, 50 found at index 4
- 60 not in list, inner loop completes, else breaks outer loop

**Key Concept:** For-else can control outer loops from inner loop completion.

---

## Problem 19: Skip Range

**Problem:** Print numbers from 1 to 20, but skip numbers 8 through 12 (inclusive).

**Solution:**
```python
for num in range(1, 21):
    if 8 <= num <= 12:
        continue
    print(num, end=' ')
```

**Output:**
```
1 2 3 4 5 6 7 13 14 15 16 17 18 19 20
```

**Explanation:**
- Loop through 1 to 20
- Check if number is in range 8-12 using chained comparison
- If yes, continue skips it
- Numbers 8, 9, 10, 11, 12 are all skipped
- All others are printed

**Key Concept:** Chained comparisons (`8 <= num <= 12`) are concise and readable.

---

## Problem 20: First Prime Number

**Problem:** Find the first prime number in a list of numbers.

**Solution:**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [4, 6, 8, 9, 11, 15, 17]

for num in numbers:
    if is_prime(num):
        print(f"First prime: {num}")
        break
```

**Output:**
```
First prime: 11
```

**Explanation:**
- Helper function checks if a number is prime
- Loop through each number in the list
- Use helper function to check primality
- 4, 6, 8, 9 are not prime
- 11 is prime (only divisible by 1 and 11)
- Print and break when first prime found
- 15 and 17 are never checked

**Key Concept:** Helper functions can encapsulate complex conditions for break statements.

---

## Problem 21: Matrix Row Sum

**Problem:** Calculate sum of each row in a 2D list, but stop if any row sum exceeds 20.

**Solution:**
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row_idx, row in enumerate(matrix):
    row_sum = sum(row)
    if row_sum > 20:
        print(f"Row {row_idx} sum: {row_sum} - exceeds limit, stopping")
        break
    print(f"Row {row_idx} sum: {row_sum}")
```

**Output:**
```
Row 0 sum: 6
Row 1 sum: 15
Row 2 sum: 24 - exceeds limit, stopping
```

**Explanation:**
- Loop through each row with enumerate
- Calculate sum of each row using `sum()` function
- Row 0: 1+2+3 = 6 (OK, continue)
- Row 1: 4+5+6 = 15 (OK, continue)
- Row 2: 7+8+9 = 24 (exceeds 20, break)
- Processing stops at row 2

**Key Concept:** Break can enforce limits or thresholds during processing.

---

## Problem 22: Skip Vowels in String

**Problem:** Print each character in a string except vowels.

**Solution:**
```python
text = "Education"

for char in text:
    if char.lower() in "aeiou":
        continue
    print(char, end=' ')
```

**Output:**
```
E d c t n
```

**Explanation:**
- Loop through each character
- Convert to lowercase for comparison
- Check if it's a vowel (a, e, i, o, u)
- If vowel, continue skips it
- 'E' is capital but we check lowercase 'e' (vowel) - wait, this would skip it!

**Corrected Solution:**
```python
text = "Education"

for char in text:
    if char.lower() in "aeiou":
        continue
    print(char, end=' ')
```

**Actual Output:**
```
d c t n
```

**Explanation (Corrected):**
- 'E' → 'e' is vowel, skip
- 'd' is consonant, print
- 'u' is vowel, skip
- 'c' is consonant, print
- 'a' is vowel, skip
- 't' is consonant, print
- 'i' is vowel, skip
- 'o' is vowel, skip
- 'n' is consonant, print

**Key Concept:** Use `.lower()` to make case-insensitive comparisons.

---

## Problem 23: First N Evens

**Problem:** Print the first 5 even numbers from a range of 1 to 50.

**Solution:**
```python
count = 0

for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=' ')
        count += 1
        if count == 5:
            break
```

**Output:**
```
2 4 6 8 10
```

**Explanation:**
- Initialize counter to track how many evens printed
- Loop through 1 to 50
- Check if number is even
- If even, print it and increment counter
- When counter reaches 5, break
- Only first 5 evens are printed: 2, 4, 6, 8, 10

**Key Concept:** Counters with break can limit output to first N matches.

---

## Problem 24: Dictionary Search

**Problem:** Search for a key in a dictionary. If found, print its value and stop.

**Solution:**
```python
person = {"name": "Alice", "age": 25, "city": "NYC"}
search_key = "age"

for key, value in person.items():
    if key == search_key:
        print(f"Found {key}: {value}")
        break
```

**Output:**
```
Found age: 25
```

**Explanation:**
- Use `.items()` to loop through key-value pairs
- Check if current key matches search key
- When found, print key and value, then break
- More efficient than checking all keys

**Alternative (Direct Access):**
```python
if "age" in person:
    print(f"Found age: {person['age']}")
```
This is actually more efficient for dictionaries, but the loop demonstrates break usage.

**Key Concept:** Break works with dictionary iteration, though direct access is often better.

---

## Problem 25: Skip Empty Strings

**Problem:** Print non-empty strings from a list.

**Solution:**
```python
words = ["Hello", "", "World", "", "Python"]

for word in words:
    if not word:  # or: if word == ""
        continue
    print(word)
```

**Output:**
```
Hello
World
Python
```

**Explanation:**
- Loop through each word
- Empty string is "falsy" in Python, so `not word` is True
- If word is empty, continue skips it
- Only non-empty strings are printed

**Key Concept:** Empty strings are falsy, making `not word` a concise check.

---

## Problem 26: Break on Condition Sum

**Problem:** Add numbers from 1 to N, but stop when sum exceeds 100.

**Solution:**
```python
total = 0
num = 0

for i in range(1, 100):
    total += i
    if total > 100:
        num = i
        break

print(f"Sum exceeded 100 at number: {num}")
print(f"Total sum: {total}")
```

**Output:**
```
Sum exceeded 100 at number: 14
Total sum: 105
```

**Explanation:**
- Start with total = 0
- Add each number: 1, 2, 3, ...
- After adding 13: total = 91
- After adding 14: total = 105 (exceeds 100)
- Store the number that caused excess (14) and break
- Sum of 1+2+3+...+14 = 105

**Key Concept:** Break with accumulation helps find threshold crossings.

---

## Problem 27: Continue Pattern

**Problem:** Print numbers 1 to 15, but skip numbers divisible by 2 OR 3.

**Solution:**
```python
for num in range(1, 16):
    if num % 2 == 0 or num % 3 == 0:
        continue
    print(num, end=' ')
```

**Output:**
```
1 5 7 11 13
```

**Explanation:**
- Check if divisible by 2 OR by 3
- Skip: 2, 3, 4, 6, 8, 9, 10, 12, 14, 15
- Print: 1 (neither), 5 (neither), 7 (neither), 11 (neither), 13 (neither)
- These are numbers coprime to both 2 and 3

**Key Concept:** Logical OR in continue conditions combines multiple filter criteria.

---

## Problem 28: Nested Continue

**Problem:** Print a multiplication table for 1-5, but skip results that are multiples of 5.

**Solution:**
```python
for i in range(1, 5):
    for j in range(1, 5):
        result = i * j
        if result % 5 == 0:
            continue
        print(f"{i}x{j}={result:2}", end="  ")
    print()  # New line after each row
```

**Output:**
```
1x1=1  1x2=2  1x3=3  1x4=4
2x1=2  2x2=4  2x3=6  2x4=8
3x1=3  3x2=6  3x3=9  3x4=12
4x1=4  4x2=8  4x3=12 4x4=16
```

**Explanation:**
- Nested loops for i and j from 1 to 4
- Calculate product
- If product divisible by 5, continue skips printing
- Skipped results: 5 (1×5, but 5 not in range), 10 (2×5), 15 (3×5), 20 (4×5)
- Since j only goes to 4, no multiples of 5 in this range actually
- Table prints completely

**Corrected Solution (Range 1-6):**
```python
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        if result % 5 == 0:
            continue
        print(f"{i}x{j}={result:2}", end="  ")
    print()
```
This would skip 5, 10, 15, 20, 25.

**Key Concept:** Continue in nested loops only affects the innermost loop.

---

## Problem 29: String Pattern Break

**Problem:** Find the first word in a sentence that starts with a capital letter.

**Solution:**
```python
sentence = "hello world Python Programming"
words = sentence.split()

for word in words:
    if word[0].isupper():
        print(f"First capitalized word: {word}")
        break
```

**Output:**
```
First capitalized word: Python
```

**Explanation:**
- Split sentence into words
- Check if first character is uppercase using `.isupper()`
- "hello" → 'h' not uppercase
- "world" → 'w' not uppercase
- "Python" → 'P' is uppercase, print and break
- "Programming" never checked

**Key Concept:** String methods like `.isupper()` work well with break conditions.

---

## Problem 30: Combined Break and Continue

**Problem:** Print numbers 1 to 30 with these rules:
- Skip multiples of 3
- Stop when you reach a multiple of 17

**Solution:**
```python
for num in range(1, 31):
    if num % 17 == 0:
        break
    if num % 3 == 0:
        continue
    print(num, end=' ')
```

**Output:**
```
1 2 4 5 7 8 10 11 13 14 16
```

**Explanation:**
- Loop 1 to 30
- Check break condition first: if divisible by 17, stop
- Then check continue condition: if divisible by 3, skip
- Print: 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16
- Skip: 3, 6, 9, 12, 15 (multiples of 3)
- Stop at: 17 (first multiple of 17)
- Order matters: break before continue

**Key Concept:** When combining break and continue, order of checks matters.

---

## Problem 31: Validate List

**Problem:** Check if a list contains only positive numbers.

**Solution:**
```python
# List 1
numbers1 = [5, 10, 15, 20]
print("List 1:")
for num in numbers1:
    if num <= 0:
        print(f"Invalid: {num}")
        break
else:
    print("All positive")

print()

# List 2
numbers2 = [5, 10, -5, 20]
print("List 2:")
for num in numbers2:
    if num <= 0:
        print(f"Invalid: {num}")
        break
else:
    print("All positive")
```

**Output:**
```
List 1:
All positive

List 2:
Invalid: -5
```

**Explanation:**
- Check each number for non-positive value
- If found, print invalid message and break
- Else clause executes only if loop completes (all positive)
- List 1: All positive, else executes
- List 2: -5 is invalid, break occurs, else doesn't execute

**Key Concept:** For-else is perfect for validation patterns.

---

## Problem 32: Character Counter

**Problem:** Count consonants in a string (skip vowels and spaces).

**Solution:**
```python
text = "Hello World"
count = 0

for char in text:
    if char == " " or char.lower() in "aeiou":
        continue
    count += 1

print(f"Consonants: {count}")
```

**Output:**
```
Consonants: 7
```

**Explanation:**
- Loop through each character
- Skip if it's a space or vowel
- Count all others (consonants)
- 'H', 'l', 'l', 'W', 'r', 'l', 'd' = 7 consonants
- Skip: 'e', 'o', ' ', 'o'

**Key Concept:** Continue with multiple conditions filters complex patterns.

---

## Problem 33: Early Exit Search

**Problem:** Search for "exit" command in a list. Stop processing when found.

**Solution:**
```python
commands = ["start", "run", "exit", "stop", "end"]

for cmd in commands:
    if cmd == "exit":
        print("Exit command found!")
        break
    print(f"Processing: {cmd}")
```

**Output:**
```
Processing: start
Processing: run
Exit command found!
```

**Explanation:**
- Loop through commands
- Check for "exit" first
- If found, print message and break
- Otherwise, process the command
- "stop" and "end" never processed

**Key Concept:** Checking break condition before processing saves unnecessary work.

---

## Problem 34: Range with Both

**Problem:** Print squares of numbers 1 to 20, but skip perfect cubes and stop when square > 200.

**Solution:**
```python
for num in range(1, 21):
    square = num ** 2

    # Check if square exceeds 200
    if square > 200:
        print(f"Stopped at {num} (square = {square})")
        break

    # Check if num is a perfect cube
    cube_root = round(num ** (1/3))
    if cube_root ** 3 == num:
        continue

    print(square, end=' ')
```

**Output:**
```
4 9 16 25 36 49 64 81 100 121 144 169 196
Stopped at 15 (square = 225)
```

**Explanation:**
- For each number, calculate its square
- If square > 200, print stop message and break
- Check if number is perfect cube (1, 8, 27...)
- 1 is perfect cube (1³=1), skip
- 8 is perfect cube (2³=8), skip
- Other numbers printed as squares
- At 15: 15² = 225 > 200, so stop

**Key Concept:** Complex conditions can combine break and continue with calculations.

---

## Problem 35: Nested Break with Flag

**Problem:** Search for a target value in a 2D list. Print "Found" or "Not found".

**Solution:**
```python
matrix = [[1, 2], [3, 4], [5, 6]]
target = 4
found = False

for row_idx, row in enumerate(matrix):
    print(f"Searching row {row_idx}...")
    for col_idx, value in enumerate(row):
        if value == target:
            print(f"Found at row {row_idx}, col {col_idx}!")
            found = True
            break
    if found:
        break

if not found:
    print("Not found in matrix")
```

**Output:**
```
Searching row 0...
Searching row 1...
Found at row 1, col 1!
```

**Explanation:**
- Use flag variable to track if target found
- Search each row with message
- Inner loop searches within row
- When found, set flag and break inner loop
- Check flag after inner loop to break outer loop
- Row 0: [1, 2] - not found
- Row 1: [3, 4] - found 4 at position 1
- Set flag, break inner, check flag, break outer

**Key Concept:** Flag variables enable breaking out of nested loops cleanly.

---

## Summary of Key Concepts

### Break Statement
1. **Exits loop immediately** when condition met
2. **Useful for searches** - stop when found
3. **Works with for-else** - else skipped if break occurs
4. **Only affects innermost loop** in nested structures
5. **Can be combined with counters** to limit iterations

### Continue Statement
1. **Skips current iteration** and moves to next
2. **Perfect for filtering** unwanted values
3. **Can have multiple continues** in one loop
4. **Only affects innermost loop** in nested structures
5. **Reduces nesting** by handling special cases early

### For-Else Clause
1. **Executes if loop completes** without break
2. **Detects search failure** elegantly
3. **Validates "all" conditions** cleanly
4. **Doesn't execute** if break occurs
5. **Works with both break and continue**

### Best Practices
1. **Check break before continue** when combining
2. **Use flags** for nested loop breaking
3. **Keep conditions clear** and well-commented
4. **Prefer for-else** over flag variables when possible
5. **Consider alternatives** - sometimes restructuring is better

### Common Patterns
1. **Search**: Loop until found, break
2. **Filter**: Continue on unwanted, process rest
3. **Limit**: Count and break at threshold
4. **Validate**: Break on invalid, else for success
5. **Early exit**: Break on special condition
