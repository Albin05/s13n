# Editorials: Controlling While Loops Using Continue Statement

## Problem 1: Skip Even Numbers (Easy)

### Solution
```python
count = 1

while count <= 10:
    if count % 2 == 0:
        count += 1
        continue
    print(count)
    count += 1
```

**Output:**
```
1
3
5
7
9
```

### Explanation
- Loop from 1 to 10
- When count is even (`count % 2 == 0`), increment and `continue`
- `continue` skips the print statement for even numbers
- Only odd numbers get printed
- **CRITICAL**: Must increment before continue, otherwise infinite loop
- Pattern: skip unwanted items

---

## Problem 2: Print Only Positives (Easy)

### Solution
```python
numbers = [5, -3, 8, -1, 12, -7, 4]

for num in numbers:
    if num < 0:
        continue
    print(num)
```

**Output:**
```
5
8
12
4
```

### Explanation
- Iterate through list
- If number is negative, `continue` (skip to next iteration)
- Print statement only reached for positive numbers
- `continue` acts as filter
- Cleaner than wrapping everything in else block

---

## Problem 3: Skip Multiples of 3 (Easy)

### Solution
```python
i = 1

while i <= 15:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1
```

**Output:**
```
1
2
4
5
7
8
10
11
13
14
```

### Explanation
- Print numbers 1-15 except multiples of 3
- When `i % 3 == 0`, increment and continue
- Skips 3, 6, 9, 12, 15
- Must increment before continue (avoid infinite loop)
- Filter pattern for excluding items

---

## Problem 4: Process Valid Input Only (Medium)

### Solution
```python
numbers = [10, 0, 5, 0, 8, 0, 3]
total = 0

for num in numbers:
    if num == 0:
        continue
    total += num

print(f"Sum (excluding zeros): {total}")
```

**Output:**
```
Sum (excluding zeros): 26
```

### Explanation
- Sum all numbers except zeros
- When num is 0, continue (skip addition)
- Total accumulates only non-zero values: 10 + 5 + 8 + 3 = 26
- `continue` prevents zeros from being added
- Validation pattern: skip invalid data

---

## Problem 5: Count Non-Vowels (Medium)

### Solution
```python
text = "hello world"
consonant_count = 0

for char in text:
    if char in "aeiou ":
        continue
    consonant_count += 1

print(f"Consonants: {consonant_count}")
```

**Output:**
```
Consonants: 7
```

### Explanation
- Count consonants by skipping vowels and spaces
- If character is vowel or space, continue
- Only consonants increment counter
- Characters in text: h, l, l, r, w, l, d = 7 consonants
- Filter approach cleaner than complex condition

---

## Problem 6: Skip Empty Strings (Medium)

### Solution
```python
words = ["hello", "", "world", "", "python", ""]
valid_words = []

for word in words:
    if word == "":
        continue
    valid_words.append(word)

print(f"Valid words: {valid_words}")
```

**Output:**
```
Valid words: ['hello', 'world', 'python']
```

### Explanation
- Build list excluding empty strings
- When word is empty, continue (skip append)
- Only non-empty words added to list
- Result contains 3 valid words
- Data cleaning pattern

---

## Problem 7: Skip Based on Condition (Medium)

### Solution
```python
i = 0

while i < 20:
    i += 1
    if i > 10 and i % 2 == 0:
        continue
    print(i)
```

**Output:**
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
11
13
15
17
19
```

### Explanation
- Print 1-20, but skip even numbers greater than 10
- Increment at start to avoid missing values
- Condition: i > 10 AND i is even → continue
- Skips: 12, 14, 16, 18, 20
- Prints all numbers 1-10, then only odds 11-19
- Complex filtering with compound condition

---

## Problem 8: Process User Input (Hard)

### Solution
```python
count = 0

while count < 5:
    command = input(f"Command {count + 1}: ")

    if command == "skip":
        print("Skipping this entry")
        continue

    print(f"Processing: {command}")
    count += 1

print("All commands processed")
```

**Example Output:**
```
Command 1: hello
Processing: hello
Command 2: skip
Skipping this entry
Command 2: world
Processing: world
Command 3: skip
Skipping this entry
Command 3: python
Processing: python
Command 4: code
Processing: code
Command 5: test
Processing: test
All commands processed
```

### Explanation
- Collect 5 valid commands
- "skip" doesn't count toward total
- `continue` prevents count increment for skipped items
- Loop repeats until 5 valid commands processed
- Validation pattern: retry without counting invalid

---

## Problem 9: Skip Negative in Accumulator (Hard)

### Solution
```python
values = [10, -5, 20, -3, 15, -8, 5]
positive_sum = 0
positive_count = 0

for value in values:
    if value < 0:
        continue

    positive_sum += value
    positive_count += 1

average = positive_sum / positive_count
print(f"Sum: {positive_sum}")
print(f"Count: {positive_count}")
print(f"Average of positives: {average}")
```

**Output:**
```
Sum: 50
Count: 4
Average of positives: 12.5
```

### Explanation
- Calculate statistics for positive numbers only
- Negative values skipped with continue
- Positive values: 10, 20, 15, 5
- Sum = 50, Count = 4, Average = 12.5
- Multiple operations all skipped for negatives
- Selective processing pattern

---

## Problem 10: Nested Loop Continue (Hard)

### Solution
```python
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(f"{i},{j}")
```

**Output:**
```
1,1
1,3
2,1
2,3
3,1
3,3
```

### Explanation
- Nested loops: outer i (1-3), inner j (1-3)
- When j=2, continue skips that iteration
- Each outer loop iteration prints j=1 and j=3 only
- `continue` only affects innermost loop
- Creates 2×3 grid minus middle column
- Selective iteration in nested structures

---

## Problem 11: Filter Data Stream (Hard)

### Solution
```python
data = [100, -999, 200, -999, 300, 150, -999, 250]
valid_data = []

for value in data:
    if value == -999:  # Sentinel/error value
        continue
    valid_data.append(value)

print(f"Valid readings: {valid_data}")
print(f"Average: {sum(valid_data) / len(valid_data)}")
```

**Output:**
```
Valid readings: [100, 200, 300, 150, 250]
Average: 200.0
```

### Explanation
- Filter out error values (-999) from sensor data
- `continue` skips sentinel values
- Collect only valid readings
- 5 valid values with average 200
- Real-world data cleaning scenario
- Sentinel filtering pattern

---

## Problem 12: Skip Characters (Hard)

### Solution
```python
text = "h3ll0 w0rld!"
clean = ""

for char in text:
    if char.isdigit():
        continue
    clean += char

print(f"Cleaned text: {clean}")
```

**Output:**
```
Cleaned text: hll wrld!
```

### Explanation
- Remove all digits from string
- If character is digit, continue (don't add to result)
- Only non-digit characters accumulated
- Removed: 3, 0, 0
- String filtering pattern
- Alternative to regex for simple cases

---

## Problem 13: Conditional Processing (Very Hard)

### Solution
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for num in numbers:
    # Skip odd numbers less than 5
    if num < 5 and num % 2 != 0:
        continue

    # Skip even numbers greater than 7
    if num > 7 and num % 2 == 0:
        continue

    result.append(num)

print(f"Filtered: {result}")
```

**Output:**
```
Filtered: [2, 4, 5, 6, 7, 9]
```

### Explanation
- Two separate filter conditions
- First continue skips: 1, 3 (odd and < 5)
- Second continue skips: 8, 10 (even and > 7)
- Remaining numbers pass both filters
- Multiple continue statements possible
- Complex filtering logic

---

## Problem 14: Grade Processing (Very Hard)

### Solution
```python
grades = [85, -1, 92, 0, 78, -1, 95, 88]
valid_grades = []

for grade in grades:
    # Skip invalid grades (negative or zero)
    if grade <= 0:
        continue

    valid_grades.append(grade)

if valid_grades:
    average = sum(valid_grades) / len(valid_grades)
    print(f"Valid grades: {valid_grades}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {max(valid_grades)}")
else:
    print("No valid grades")
```

**Output:**
```
Valid grades: [85, 92, 78, 95, 88]
Average: 87.60
Highest: 95
```

### Explanation
- Filter out invalid grades (≤ 0)
- -1 and 0 represent missing data
- `continue` skips invalid entries
- Calculate statistics on clean data
- 5 valid grades with average 87.6
- Data validation and processing

---

## Problem 15: Username Filter (Very Hard)

### Solution
```python
usernames = ["alice", "b0b", "charlie", "d@ve", "eve123", "frank"]
valid_users = []

for name in usernames:
    # Skip if contains digits
    if any(char.isdigit() for char in name):
        print(f"Skipping '{name}': contains digits")
        continue

    # Skip if contains special characters
    if not name.isalpha():
        print(f"Skipping '{name}': special characters")
        continue

    valid_users.append(name)

print(f"\nValid usernames: {valid_users}")
```

**Output:**
```
Skipping 'b0b': contains digits
Skipping 'd@ve': special characters
Skipping 'eve123': contains digits
Valid usernames: ['alice', 'charlie', 'frank']
```

### Explanation
- Multiple validation rules
- First continue: reject if has digits
- Second continue: reject if has special chars
- Provides feedback for each rejection
- Only alphabetic names accepted
- Multi-stage validation pattern

---

## Problem 16: Skip Range (Very Hard)

### Solution
```python
count = 0

while count < 20:
    count += 1

    # Skip numbers 5-10
    if 5 <= count <= 10:
        continue

    print(count)
```

**Output:**
```
1
2
3
4
11
12
13
14
15
16
17
18
19
20
```

### Explanation
- Print 1-20 except 5-10
- Range condition: `5 <= count <= 10`
- `continue` skips entire range
- Must increment before check
- Prints 1-4, then 11-20
- Range exclusion pattern

---

## Problem 17: Process Menu Until Exit (Very Hard)

### Solution
```python
total = 0
count = 0

while True:
    command = input("Enter number (or 'done'): ")

    if command == "done":
        break

    # Skip non-numeric input
    if not command.lstrip('-').isdigit():
        print("Invalid input, please enter a number")
        continue

    num = int(command)
    total += num
    count += 1

if count > 0:
    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {total / count}")
else:
    print("No numbers entered")
```

**Example Output:**
```
Enter number (or 'done'): 10
Enter number (or 'done'): abc
Invalid input, please enter a number
Enter number (or 'done'): 20
Enter number (or 'done'): xyz
Invalid input, please enter a number
Enter number (or 'done'): 30
Enter number (or 'done'): done
Total: 60
Count: 3
Average: 20.0
```

### Explanation
- Input validation with continue
- Invalid inputs don't count or affect total
- `continue` forces re-prompt
- Only valid numbers processed
- Combines break (exit) and continue (skip)
- Robust input handling

---

## Problem 18: Matrix Processing (Very Hard)

### Solution
```python
matrix = [
    [1, 0, 3],
    [0, 5, 6],
    [7, 8, 0]
]

non_zero_sum = 0
non_zero_count = 0

for row in matrix:
    for value in row:
        if value == 0:
            continue

        non_zero_sum += value
        non_zero_count += 1

print(f"Non-zero sum: {non_zero_sum}")
print(f"Non-zero count: {non_zero_count}")
print(f"Average: {non_zero_sum / non_zero_count}")
```

**Output:**
```
Non-zero sum: 30
Non-zero count: 6
Average: 5.0
```

### Explanation
- Process 2D matrix, skip zeros
- Nested loop with continue in inner loop
- Non-zero values: 1, 3, 5, 6, 7, 8
- Sum = 30, Count = 6, Average = 5.0
- `continue` works in nested structures
- Selective matrix processing

---

## Problem 19: Word Length Filter (Very Hard)

### Solution
```python
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
long_words = []

for word in words:
    # Skip short words (≤ 3 letters)
    if len(word) <= 3:
        continue

    long_words.append(word)

print(f"Long words: {long_words}")
print(f"Count: {len(long_words)}")
```

**Output:**
```
Long words: ['quick', 'brown', 'jumps', 'over', 'lazy']
Count: 5
```

### Explanation
- Extract words longer than 3 letters
- Skip "the", "fox", "the", "dog" (≤ 3 chars)
- `continue` filters short words
- Remaining 5 words collected
- Length-based filtering
- Text processing pattern

---

## Problem 20: Temperature Validator (Very Hard)

### Solution
```python
readings = [22.5, -999, 23.1, 150, 21.8, -999, 24.2, -10]
valid_temps = []

for temp in readings:
    # Skip sensor errors (-999)
    if temp == -999:
        print(f"Skipping error reading: {temp}")
        continue

    # Skip unrealistic temperatures
    if temp < -50 or temp > 50:
        print(f"Skipping unrealistic temp: {temp}")
        continue

    valid_temps.append(temp)

if valid_temps:
    avg_temp = sum(valid_temps) / len(valid_temps)
    print(f"\nValid temperatures: {valid_temps}")
    print(f"Average: {avg_temp:.2f}°C")
```

**Output:**
```
Skipping error reading: -999
Skipping unrealistic temp: 150
Skipping error reading: -999
Valid temperatures: [22.5, 23.1, 21.8, 24.2]
Average: 22.9°C
```

### Explanation
- Two-stage validation
- First continue: skip error sentinel (-999)
- Second continue: skip out-of-range values
- Valid range: -50 to 50°C
- 4 valid readings with average 22.9°C
- Real-world sensor data filtering

---

## Key Concepts Demonstrated

1. **Skip Iteration**: Continue jumps to next iteration immediately
2. **Filter Pattern**: Exclude unwanted items from processing
3. **Validation**: Skip invalid data without stopping loop
4. **Early Continue**: Place increment before continue in while loops
5. **Multiple Continues**: Can have several in one loop
6. **Nested Loops**: Continue only affects innermost loop
7. **Continue vs Break**: Continue skips, break exits
8. **Data Cleaning**: Remove errors, outliers, invalid entries
9. **Conditional Skip**: Complex conditions determine skip
10. **Input Validation**: Re-prompt without counting invalid

## Continue vs Break

| Feature | Continue | Break |
|---------|----------|-------|
| **Action** | Skip to next iteration | Exit loop entirely |
| **Loop continues?** | Yes | No |
| **Use case** | Filter items | Find and stop |
| **Example** | Skip negatives | Stop at sentinel |

## Best Practices

1. **Increment before continue**: In while loops, update counter before continue
2. **Provide feedback**: Print why item was skipped (debugging)
3. **Early continue**: Check skip conditions first, main logic last
4. **Avoid deep nesting**: Continue can flatten complex if-else
5. **Document intention**: Comment why continue is needed
6. **Combine with break**: Use both for flexible control
7. **Validate data**: Use continue for data cleaning
8. **Keep simple**: Don't overuse, maintain readability

## Common Patterns

```python
# Pattern 1: Filter unwanted items
for item in collection:
    if not_wanted(item):
        continue
    process(item)

# Pattern 2: Skip invalid data
while condition:
    data = get_data()
    if invalid(data):
        continue
    accumulate(data)

# Pattern 3: Multiple filters
for value in values:
    if condition1:
        continue
    if condition2:
        continue
    use(value)

# Pattern 4: Validation with retry
while attempts < max:
    input_data = get_input()
    if not valid(input_data):
        continue  # Don't count invalid
    attempts += 1
    process(input_data)
```
