### LO-20 Control Loops with Break (25 minutes)


### CS Theory Bite

> **Origin**: `break` implements **early termination** — exiting a loop before its natural end. This pattern uses **sentinel values** in algorithms — stop when you find what you're looking for.
>
> **Analogy**: `break` is like pulling the **emergency brake** — the loop stops immediately, no questions asked.
>
> **Why it matters**: Without `break`, you'd need complex boolean flags to exit loops — `break` keeps code clean.


### Hook (3 minutes)

**Say**: "You're searching for your keys. You check rooms one by one. BREAK means you found them - stop searching!"

```python
rooms = ["kitchen", "bedroom", "bathroom", "garage"]

for room in rooms:
    print(f"Checking {room}...")
    if room == "bathroom":
        print("Found keys!")
        break  # Stop searching!

print("Search complete!")
```

### Break Basics (6 minutes)

**Say**: "break exits a loop immediately, even if the condition is still True."

```python
count = 0

while count < 10:
    print(count)
    if count == 5:
        print("Breaking out!")
        break  # Exit loop NOW
    count += 1

print("After loop")  # This runs
```

**Key Points**:
- `break` exits the loop immediately
- Skips remaining code in loop
- Continues execution after the loop
- Works in both while and for loops

```python
while True:  # Infinite loop!
    password = input("Enter password: ")
    if password == "secret":
        print("Access granted!")
        break  # Exit the infinite loop
    print("Wrong password")
```

### Break with While Loops (6 minutes)

**Say**: "Perfect for input validation with an escape!"

```python
while True:
    age = int(input("Enter age: "))

    if age < 0:
        print("Age can't be negative!")
        continue  # Skip to next iteration

    if age > 120:
        print("Invalid age!")
        continue

    # Valid age!
    break

print(f"Age accepted: {age}")
```

**Real-World**: Search pattern
```python
numbers = [10, 25, 30, 15, 40]
target = 30
found = False

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        found = True
        break

if not found:
    print(f"{target} not in list")
```

### Loop-Else Clause (6 minutes)

**Say**: "else after a loop runs ONLY if break was never called!"

```python
for item in sequence:
    if condition:
        break
else:
    # Runs if NO break occurred
    print("Loop completed normally")
```

**Example**: Finding a prime number
```python
number = 17

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime")
        break
else:
    print(f"{number} is prime!")
```

**Real-World**: Authentication
```python
users = ["alice", "bob", "charlie"]
username = input("Username: ")

for user in users:
    if user == username:
        print("User found!")
        break
else:
    print("User not found - creating new account")
```

### Nested Loops with Break (4 minutes)

**Say**: "break only exits the INNER loop, not the outer one!"

```python
for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(3):
        print(f"  Inner loop: {j}")
        if j == 1:
            break  # Only breaks INNER loop
    print("Outer continues...")
```

### Practice (3 minutes)

Find first negative number:
```python
numbers = [5, 10, -3, 8, 12]

for num in numbers:
    if num < 0:
        print(f"First negative: {num}")
        break
else:
    print("No negative numbers found")
```
