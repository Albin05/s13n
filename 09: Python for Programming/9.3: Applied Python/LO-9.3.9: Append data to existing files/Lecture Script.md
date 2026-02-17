# Lecture Script: LO-51 Append to Files


### CS Theory Bite

> **Origin**: Append mode implements **append-only semantics** — new data added to the end, existing data untouched. This is the basis of **write-ahead logs (WAL)** used in databases for crash recovery.
>
> **Analogy**: Appending is like **writing in a diary** — you add new entries at the end, never erase previous pages.
>
> **Why it matters**: Log files, chat histories, and transaction records all require append, not overwrite.


## [0:00-0:02] Hook (2 min)
**Say**: "Imagine a diary. When you write a new entry, you don't tear out the old pages! You add to the end. That's what append mode does with files!"

## [0:02-0:08] Write vs Append (6 min)

**Say**: "First, let's see the difference between write and append modes."

**Live Code**:
```python
# Write mode - overwrites!
with open("test.txt", "w") as f:
    f.write("First line\n")

# Write again - ERASES previous!
with open("test.txt", "w") as f:
    f.write("Second line\n")

# Read it
with open("test.txt", "r") as f:
    print(f.read())  # Only "Second line"
```

**Point out**: "First line is GONE! Write mode erases everything."

**Now show append**:
```python
# Write first line
with open("test.txt", "w") as f:
    f.write("First line\n")

# Append second line
with open("test.txt", "a") as f:
    f.write("Second line\n")

# Read it
with open("test.txt", "r") as f:
    print(f.read())
# Output:
# First line
# Second line
```

**Emphasize**: "Both lines are there! Append adds without erasing."

## [0:08-0:12] Real-World Example: Log File (4 min)

**Say**: "Let's build a simple log file."

**Live Code**:
```python
def log_event(message):
    with open("app.log", "a") as f:
        f.write(f"{message}\n")

log_event("Program started")
log_event("User logged in")
log_event("Data saved")
log_event("Program closed")

# Show the log
with open("app.log", "r") as f:
    print(f.read())
```

**Run it multiple times** to show new entries keep getting added!

## [0:12-0:15] Practice (3 min)

**Challenge**: "Create an attendance system that appends names."

**Guide students**:
```python
def mark_present(name):
    with open("attendance.txt", "a") as f:
        f.write(f"{name} - Present\n")

mark_present("Alice")
mark_present("Bob")
mark_present("Charlie")
```

## [0:15-0:17] Common Mistake (2 min)

**Show wrong way**:
```python
# Wrong - overwrites each time!
for i in range(5):
    with open("numbers.txt", "w") as f:
        f.write(f"{i}\n")
# Only has last number!

# Right - appends each time
for i in range(5):
    with open("numbers.txt", "a") as f:
        f.write(f"{i}\n")
# Has all numbers!
```

## [0:17-0:20] Wrap-up (3 min)

**Key Points**:
1. "w" = write (overwrites)
2. "a" = append (adds to end)
3. Use append for logs and data collection
4. Don't forget \n for new lines!

**Closing Tip**: "When in doubt: 'w' for starting fresh, 'a' for keeping history!"
