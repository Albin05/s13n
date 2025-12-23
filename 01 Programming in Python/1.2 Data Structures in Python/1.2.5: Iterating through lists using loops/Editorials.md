# Editorials: Iterating Through Lists Using Loops

## Problem 1: Calculate Average (Easy)

### Solution
```python
scores = [85, 92, 78, 95, 88]

total = 0
count = 0

for score in scores:
    total += score
    count += 1

average = total / count
print(f"Average score: {average:.2f}")
```

### Explanation
- Initialize `total` and `count` to 0
- Loop through each score, adding to total and incrementing count
- Calculate average by dividing total by count
- Format to 2 decimal places using `:.2f`

**Alternative (using built-ins):**
```python
average = sum(scores) / len(scores)
print(f"Average score: {average:.2f}")
```

---

## Problem 2: Count Vowels in Names (Easy)

### Solution
```python
names = ["Alice", "Bob", "Emily", "David", "Oliver", "Sarah"]

vowels = "AEIOU"
count = 0

for name in names:
    if name[0].upper() in vowels:
        count += 1

print(f"Names starting with vowels: {count}")
```

### Explanation
- Define vowels string (uppercase for easy checking)
- Loop through names, check if first character (name[0]) is a vowel
- Use `.upper()` to handle both uppercase and lowercase
- Increment counter when match found

---

## Problem 3: Find Maximum and Its Position (Easy)

### Solution
```python
numbers = [45, 23, 67, 89, 12, 56]

max_value = numbers[0]
max_index = 0

for i, num in enumerate(numbers):
    if num > max_value:
        max_value = num
        max_index = i

print(f"Maximum value: {max_value}")
print(f"Position: {max_index}")
```

### Explanation
- Initialize max_value with first element and max_index with 0
- Use enumerate() to get both index and value
- Update both max_value and max_index when larger number found
- This approach tracks position as we find the maximum

---

## Problem 4: Temperature Converter (Medium)

### Solution
```python
celsius = [0, 10, 20, 30, 40]
fahrenheit = []

# Convert each temperature
for temp_c in celsius:
    temp_f = (temp_c * 9/5) + 32
    fahrenheit.append(temp_f)

# Display results
for c, f in zip(celsius, fahrenheit):
    print(f"{c}°C = {f}°F")
```

### Explanation
- Create empty fahrenheit list
- Loop through celsius temperatures, apply formula, append to new list
- Use zip() to pair corresponding celsius and fahrenheit values for display
- Formula: F = (C × 9/5) + 32

---

## Problem 5: Filter by Length (Medium)

### Solution
```python
words = ["apple", "pie", "banana", "cat", "strawberry", "dog"]
min_length = 5

long_words = []

for word in words:
    if len(word) >= min_length:
        long_words.append(word)

print(f"Long words: {long_words}")
```

### Explanation
- Create empty list for filtered results
- Loop through words, check length
- Only append words that meet minimum length requirement
- This is the filtering pattern

**Alternative (list comprehension):**
```python
long_words = [word for word in words if len(word) >= min_length]
```

---

## Problem 6: Parallel List Processing (Medium)

### Solution
```python
products = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 25.50, 79.99]
quantities = [1, 2, 1]

grand_total = 0

for product, price, quantity in zip(products, prices, quantities):
    total = price * quantity
    grand_total += total
    print(f"{product}: ${price:.2f} x {quantity} = ${total:.2f}")

print(f"Grand Total: ${grand_total:.2f}")
```

### Explanation
- Use zip() to iterate through all three lists simultaneously
- Calculate individual total (price × quantity)
- Accumulate grand_total as we process each item
- Format currency with 2 decimal places

---

## Problem 7: Find All Occurrences (Medium)

### Solution
```python
numbers = [5, 2, 8, 2, 9, 2, 1, 2]
target = 2

positions = []

for i, num in enumerate(numbers):
    if num == target:
        positions.append(i)

print(f"Value {target} found at positions: {positions}")
```

### Explanation
- Create empty list for storing positions
- Use enumerate() to get both index and value
- When value matches target, append the index
- Result is a list of all positions where target appears

---

## Problem 8: Running Total (Medium)

### Solution
```python
numbers = [1, 2, 3, 4, 5]
running_totals = []

total = 0
for num in numbers:
    total += num
    running_totals.append(total)

print(f"Running totals: {running_totals}")
```

### Explanation
- Maintain a running total variable
- For each number, add to running total
- Append current total to result list
- Each element represents cumulative sum up to that point
- Result: [1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5] = [1, 3, 6, 10, 15]

---

## Problem 9: Pair Adjacent Elements (Hard)

### Solution
```python
numbers = [1, 2, 3, 4, 5]
pairs = []

for i in range(len(numbers) - 1):
    pair = (numbers[i], numbers[i+1])
    pairs.append(pair)

print(f"Pairs: {pairs}")
```

### Explanation
- Use range(len(numbers) - 1) to avoid index out of bounds
- Access current element (numbers[i]) and next element (numbers[i+1])
- Create tuple for each pair
- Stop one before the end since we're accessing i+1

**Alternative:**
```python
pairs = [(numbers[i], numbers[i+1]) for i in range(len(numbers)-1)]
```

---

## Problem 10: Student Grade Statistics (Hard)

### Solution
```python
students = [
    ["Alice", 85, 90, 88],
    ["Bob", 92, 88, 95],
    ["Charlie", 78, 85, 80],
    ["David", 95, 98, 97]
]

top_student = ""
top_average = 0

for student_data in students:
    name = student_data[0]
    scores = student_data[1:]  # All elements except first

    average = sum(scores) / len(scores)
    print(f"{name}: Average = {average:.2f}")

    # Track top performer
    if average > top_average:
        top_average = average
        top_student = name

print(f"\nTop performer: {top_student} with {top_average:.2f}")
```

### Explanation
- Each student is a list: [name, score1, score2, score3]
- Extract name (first element) and scores (rest with slicing [1:])
- Calculate average for each student
- Track highest average and corresponding student name
- Display all averages, then top performer

---

## Problem 11: Remove Duplicates (Hard)

### Solution
```python
numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(f"Unique numbers: {unique}")
```

### Explanation
- Create empty list for unique values
- For each number, check if it's already in unique list
- Only append if not present
- This preserves original order (first occurrence kept)
- Time complexity: O(n²) due to `in` check

**More efficient with set (but loses order):**
```python
unique = list(set(numbers))  # Loses original order
```

---

## Problem 12: Merge and Sort Parallel Lists (Hard)

### Solution
```python
names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 22, 28]

# Combine into list of tuples
combined = list(zip(names, ages))

# Sort by age (second element of tuple)
combined.sort(key=lambda x: x[1])

print("Sorted by age:")
for name, age in combined:
    print(f"{name} ({age})")
```

### Explanation
- Use zip() to combine names and ages into tuples
- Convert to list so we can sort it
- Sort using key parameter (sorts by age, the second element)
- Iterate through sorted list to display results
- Lambda function `lambda x: x[1]` returns age for sorting

**Alternative without lambda (if not covered):**
```python
# Manual bubble sort or insertion sort approach
for i in range(len(ages)):
    for j in range(i+1, len(ages)):
        if ages[i] > ages[j]:
            ages[i], ages[j] = ages[j], ages[i]
            names[i], names[j] = names[j], names[i]
```

---

## Problem 13: Matrix Row Sums (Hard)

### Solution
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i, row in enumerate(matrix):
    row_sum = 0
    for num in row:
        row_sum += num
    print(f"Row {i} sum: {row_sum}")
```

### Explanation
- Outer loop iterates through rows (each row is a list)
- Use enumerate() to get row index
- Inner loop sums all numbers in current row
- This demonstrates nested iteration

**Alternative (using sum()):**
```python
for i, row in enumerate(matrix):
    print(f"Row {i} sum: {sum(row)}")
```

---

## Problem 14: Word Frequency Counter (Hard)

### Solution
```python
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Get unique words first
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

# Count each unique word
for word in unique_words:
    count = 0
    for w in words:
        if w == word:
            count += 1
    print(f"{word}: {count}")
```

### Explanation
- First loop: Build list of unique words
- Second loop: For each unique word, count occurrences in original list
- Inner loop checks each word in original list against current unique word
- This uses nested loops for counting

**Better approach with dictionary (if covered):**
```python
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word, count in frequency.items():
    print(f"{word}: {count}")
```

---

## Problem 15: Longest Increasing Sequence (Very Hard)

### Solution
```python
numbers = [1, 3, 2, 4, 5, 6, 3, 7, 8]

max_length = 1
max_start = 0
current_length = 1
current_start = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        # Continue current sequence
        current_length += 1
    else:
        # Sequence broken, check if it was the longest
        if current_length > max_length:
            max_length = current_length
            max_start = current_start
        # Start new sequence
        current_length = 1
        current_start = i

# Check last sequence
if current_length > max_length:
    max_length = current_length
    max_start = current_start

# Extract the sequence
sequence = numbers[max_start:max_start + max_length]

print(f"Longest increasing sequence length: {max_length}")
print(f"Sequence: {sequence}")
```

### Explanation
- Track current sequence (length and start position)
- Track maximum sequence found so far
- Compare each number with previous (i-1)
- If increasing, extend current sequence
- If not, save current if it's longest, then reset
- Don't forget to check final sequence after loop ends
- Use slicing to extract the actual sequence

**Key insight:** This is a sliding window problem requiring careful state tracking of both current and maximum sequences.
