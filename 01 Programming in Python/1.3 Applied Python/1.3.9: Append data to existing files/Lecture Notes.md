# Lecture Notes: Append to Files

## Append Mode

Append mode ("a") adds content to the end of a file without deleting existing content.


---

<div align="center">

![File folders and documents](https://images.unsplash.com/photo-1544396821-4dd40b938ad3?w=800&q=80)

*Python can read from and write to files on your system*

</div>

---
### Syntax

```python
with open("filename.txt", "a") as file:
    file.write("new content\n")
```

## Write vs Append

### Write Mode ("w") - Overwrites

```python
# First write
with open("data.txt", "w") as f:
    f.write("Line 1\n")

# Second write - ERASES previous content!
with open("data.txt", "w") as f:
    f.write("Line 2\n")

# File only contains: Line 2
```

### Append Mode ("a") - Adds to End

```python
# First write
with open("data.txt", "w") as f:
    f.write("Line 1\n")

# Append - keeps previous content
with open("data.txt", "a") as f:
    f.write("Line 2\n")

# File contains:
# Line 1
# Line 2
```

## Examples

### Example 1: Simple Append

```python
# Create file
with open("notes.txt", "w") as f:
    f.write("First note\n")

# Add more notes
with open("notes.txt", "a") as f:
    f.write("Second note\n")
    f.write("Third note\n")

# Read result
with open("notes.txt", "r") as f:
    print(f.read())

# Output:
# First note
# Second note
# Third note
```

### Example 2: Log File

```python
import datetime

def log_event(event):
    timestamp = datetime.datetime.now()
    with open("app.log", "a") as f:
        f.write(f"[{timestamp}] {event}\n")

log_event("Application started")
log_event("User logged in")
log_event("Data saved")

# app.log contains all events with timestamps
```

### Example 3: Attendance System

```python
def mark_attendance(name):
    with open("attendance.txt", "a") as f:
        f.write(f"{name} - Present\n")

mark_attendance("Alice")
mark_attendance("Bob")
mark_attendance("Charlie")

# attendance.txt:
# Alice - Present
# Bob - Present
# Charlie - Present
```

### Example 4: Score Tracker

```python
def save_score(player, score):
    with open("scores.txt", "a") as f:
        f.write(f"{player}: {score}\n")

save_score("Alice", 100)
save_score("Bob", 95)
save_score("Charlie", 110)
```

## File Creation

If file doesn't exist, append mode creates it:

```python
# File doesn't exist yet
with open("newfile.txt", "a") as f:
    f.write("First line\n")

# File is created with this content
```

## Real-World Applications

### Application 1: Chat Log

```python
def add_message(user, message):
    with open("chat.txt", "a") as f:
        f.write(f"{user}: {message}\n")

add_message("Alice", "Hello!")
add_message("Bob", "Hi Alice!")
add_message("Alice", "How are you?")
```

### Application 2: Transaction Log

```python
def log_transaction(amount, type):
    with open("transactions.txt", "a") as f:
        f.write(f"{type}: ${amount}\n")

log_transaction(50, "Deposit")
log_transaction(20, "Withdrawal")
log_transaction(100, "Deposit")
```

### Application 3: Error Log

```python
def log_error(error_msg):
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("errors.log", "a") as f:
        f.write(f"[{timestamp}] ERROR: {error_msg}\n")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    log_error(str(e))
```

## Reading and Appending

```python
# Read current content
with open("data.txt", "r") as f:
    current = f.read()
    print("Current content:", current)

# Append new content
with open("data.txt", "a") as f:
    f.write("New line\n")

# Read updated content
with open("data.txt", "r") as f:
    updated = f.read()
    print("Updated content:", updated)
```

## Common Mistakes

### 1. Using "w" When You Want "a"

```python
# Wrong - erases file each time!
for i in range(5):
    with open("numbers.txt", "w") as f:
        f.write(f"{i}\n")
# File only contains: 4

# Correct - appends each time
for i in range(5):
    with open("numbers.txt", "a") as f:
        f.write(f"{i}\n")
# File contains: 0 1 2 3 4
```

### 2. Forgetting Newline

```python
# Wrong - all on one line
with open("data.txt", "a") as f:
    f.write("Line 1")
    f.write("Line 2")
# Output: Line 1Line 2

# Correct - separate lines
with open("data.txt", "a") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
# Output:
# Line 1
# Line 2
```

## Mode Summary

| Mode | Creates? | Overwrites? | Reads? | Writes? | Appends? |
|------|----------|-------------|--------|---------|----------|
| "r"  | No       | -           | Yes    | No      | No       |
| "w"  | Yes      | Yes         | No     | Yes     | No       |
| "a"  | Yes      | No          | No     | Yes     | Yes      |
| "r+" | No       | No          | Yes    | Yes     | No       |
| "a+" | Yes      | No          | Yes    | Yes     | Yes      |

## Key Takeaways

1. **"a" mode**: Appends to end of file
2. **Preserves content**: Doesn't erase existing data
3. **Creates if missing**: File created if doesn't exist
4. **Use for logs**: Perfect for log files
5. **Add newlines**: Remember \n for separate lines
