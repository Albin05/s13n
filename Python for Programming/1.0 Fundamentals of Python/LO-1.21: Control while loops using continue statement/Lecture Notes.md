# Lecture Notes: Control While Loops with Continue

## The Continue Statement

`continue` skips the rest of the current iteration and goes to the next one.


---

<div align="center">

![Circular pattern representing loops](https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800&q=80)

*Loops allow you to repeat operations efficiently*

</div>

---
### Basic Syntax

```python
while condition:
    # Code
    if some_condition:
        continue  # Skip to next iteration
    # This code is skipped if continue runs
```

## Examples

### Example 1: Skip Even Numbers

```python
count = 0

while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)  # Only prints odd numbers

# Output: 1 3 5 7 9
```

### Example 2: Input Validation

```python
attempts = 0

while attempts < 5:
    age = int(input("Enter age: "))
    attempts += 1
    
    if age < 0:
        print("Invalid age!")
        continue  # Skip to next attempt
    
    print(f"Valid age: {age}")
    break
```

### Example 3: Filter Data

```python
count = 0
total = 0
num_count = 0

while count < 10:
    num = int(input("Enter number (negative to skip): "))
    count += 1
    
    if num < 0:
        continue  # Skip negative numbers
    
    total += num
    num_count += 1

average = total / num_count if num_count > 0 else 0
print(f"Average: {average}")
```

## Continue vs Break

```python
# continue - skips iteration
while count < 10:
    count += 1
    if count == 5:
        continue  # Skips printing 5
    print(count)

# break - exits loop
while count < 10:
    count += 1
    if count == 5:
        break  # Stops at 5
    print(count)
```

## Key Takeaways

1. **Skips to next**: continue jumps to next iteration
2. **Doesn't exit**: Loop continues running
3. **Use for filtering**: Skip unwanted items
4. **Update before continue**: Make sure loop variable updates
5. **Common with validation**: Skip invalid input
