### LO-21 Control Loops with Continue (25 minutes)


### CS Theory Bite

> **Origin**: `continue` implements the **filter pattern** — skip items that don't meet criteria and process only those that do. It's the loop equivalent of "next, please!"
>
> **Analogy**: `continue` is like a **bouncer checking IDs** — "You don't qualify? Skip. Next person." The line keeps moving.
>
> **Why it matters**: `continue` avoids deep nesting — instead of wrapping code in `if`, just skip the unwanted cases.


### Hook (3 minutes)

**Say**: "You're looking through a list of students. You want to print everyone EXCEPT those who are absent. That's continue - skip some, keep going!"

```python
# WITH continue - skip evens, keep going
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip evens
    print(num)  # Only odds print

print("Loop finished!")
# Output: 1 3 5 7 9
```

### Continue Basics (6 minutes)

**Say**: "continue skips the rest of the current iteration and jumps to the next one."

```python
while condition:
    # code
    if skip_condition:
        continue  # Jump to next iteration NOW
    # This code is skipped if continue executes
    # more code
```

**Key Points**:
- `continue` skips remaining code in current iteration
- Loop continues with next iteration
- Different from `break` which exits the loop entirely
- Works in both while and for loops

```python
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue  # Skip when count is 3
    print(count)

# Output: 1 2 4 5 (3 is skipped!)
```

### Continue vs Break (6 minutes)

**Say**: "break EXITS the loop. continue SKIPS to next iteration."

```python
print("=== CONTINUE Demo ===")
for i in range(1, 6):
    if i == 3:
        continue  # Skip 3, keep going
    print(i)
# Output: 1 2 4 5

print("\n=== BREAK Demo ===")
for i in range(1, 6):
    if i == 3:
        break  # Stop at 3
    print(i)
# Output: 1 2
```

**Real-World**: Processing data with errors
```python
scores = [85, 92, -1, 78, -1, 95]  # -1 means error

total = 0
count = 0

for score in scores:
    if score < 0:
        continue  # Skip error values
    total += score
    count += 1

average = total / count
print(f"Average: {average}")  # 87.5
```

### Common Patterns (4 minutes)

**Say**: "Use continue to filter out unwanted items!"

**Skip invalid data**:
```python
temperatures = [22.5, -999, 23.1, -999, 21.8, 24.2]
valid_temps = []

for temp in temperatures:
    if temp == -999:  # Error reading
        continue
    valid_temps.append(temp)

avg = sum(valid_temps) / len(valid_temps)
print(f"Average temp: {avg:.1f}°C")
```

**Process only certain items**:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print only multiples of 3
for num in numbers:
    if num % 3 != 0:
        continue  # Skip non-multiples
    print(num)  # 3, 6, 9
```

### Input Validation with Continue (3 minutes)

```python
while True:
    age = int(input("Enter age: "))

    if age < 0:
        print("Age can't be negative!")
        continue  # Ask again

    if age > 120:
        print("Invalid age!")
        continue  # Ask again

    # Valid age!
    break

print(f"Age accepted: {age}")
```

### Practice (3 minutes)

Print words longer than 3 characters:
```python
words = ["cat", "elephant", "dog", "giraffe", "ant", "bear"]

for word in words:
    if len(word) <= 3:
        continue  # Skip short words
    print(word)

# Output: elephant, giraffe, bear
```
