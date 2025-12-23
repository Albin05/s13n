# Question Bank: Append to Files

## Problem 1 (Easy)
Create a program that appends 5 names to a file called "names.txt", one per line.

Example:
```
names.txt should contain:
Alice
Bob
Charlie
David
Eve
```

## Problem 2 (Easy)
Write a program that:
1. Writes "Start" to a file
2. Appends "Middle" to the same file
3. Appends "End" to the same file
4. Reads and prints the entire file

## Problem 3 (Medium)
Create a simple todo list program:
- Function `add_task(task)` that appends tasks to "todo.txt"
- Function `show_tasks()` that reads and prints all tasks
- Add at least 3 tasks and display them

Example:
```
Buy groceries
Call dentist
Finish homework
```

## Problem 4 (Medium)
Create a score tracking system:
- Function `save_score(name, score)` that appends "name: score" to "scores.txt"
- Function `show_all_scores()` that displays all scores
- Add scores for 5 different players

Example output:
```
Alice: 100
Bob: 95
Charlie: 110
David: 88
Eve: 92
```

## Problem 5 (Hard)
Create a comprehensive log system:
- Function `log_message(level, message)` where level is "INFO", "WARNING", or "ERROR"
- Each log entry should have timestamp, level, and message
- Log at least 5 different events
- Create a function `show_errors_only()` that reads the log and displays only ERROR entries

Use the datetime module for timestamps.

Example log entry:
```
[2024-01-15 10:30:45] INFO: Application started
[2024-01-15 10:31:00] WARNING: Low memory
[2024-01-15 10:31:15] ERROR: Connection failed
```
