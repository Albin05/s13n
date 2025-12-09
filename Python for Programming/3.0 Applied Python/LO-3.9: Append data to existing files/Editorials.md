# Editorials: Append to Files

## Problem 1
```python
with open("names.txt", "a") as f:
    f.write("Alice\n")
    f.write("Bob\n")
    f.write("Charlie\n")
    f.write("David\n")
    f.write("Eve\n")
```

### Explanation
- Open file in append mode "a"
- Write each name with \n for new line
- File closes automatically with `with` statement

## Problem 2
```python
# Write initial content
with open("file.txt", "w") as f:
    f.write("Start\n")

# Append middle
with open("file.txt", "a") as f:
    f.write("Middle\n")

# Append end
with open("file.txt", "a") as f:
    f.write("End\n")

# Read and print
with open("file.txt", "r") as f:
    print(f.read())
```

### Explanation
- First use "w" to create file
- Then use "a" twice to append
- Finally use "r" to read
- File contains all three lines

## Problem 3
```python
def add_task(task):
    with open("todo.txt", "a") as f:
        f.write(f"{task}\n")

def show_tasks():
    with open("todo.txt", "r") as f:
        print(f.read())

# Add tasks
add_task("Buy groceries")
add_task("Call dentist")
add_task("Finish homework")

# Display all tasks
show_tasks()
```

### Explanation
- `add_task()` appends each task to file
- `show_tasks()` reads and displays all
- Each task on separate line

## Problem 4
```python
def save_score(name, score):
    with open("scores.txt", "a") as f:
        f.write(f"{name}: {score}\n")

def show_all_scores():
    with open("scores.txt", "r") as f:
        print(f.read())

# Save scores
save_score("Alice", 100)
save_score("Bob", 95)
save_score("Charlie", 110)
save_score("David", 88)
save_score("Eve", 92)

# Display all
show_all_scores()
```

### Explanation
- Format each score as "name: score"
- Append to scores.txt
- Read entire file to display

## Problem 5
```python
import datetime

def log_message(level, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log", "a") as f:
        f.write(f"[{timestamp}] {level}: {message}\n")

def show_errors_only():
    with open("app.log", "r") as f:
        for line in f:
            if "ERROR" in line:
                print(line.strip())

# Log various events
log_message("INFO", "Application started")
log_message("INFO", "User logged in")
log_message("WARNING", "Low memory")
log_message("ERROR", "Connection failed")
log_message("INFO", "Data saved")
log_message("ERROR", "File not found")

print("\nAll Errors:")
show_errors_only()
```

### Explanation
- Use datetime to get current timestamp
- Format timestamp as YYYY-MM-DD HH:MM:SS
- Append each log entry with level and message
- `show_errors_only()` reads file and filters for ERROR lines
- Use strip() to remove extra newlines when printing
