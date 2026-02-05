## Question Bank: Read Text Files in Python

---

### Q1: Basic File Reading (3 minutes, Low Difficulty)

Write a program that reads a file "sample.txt" and prints:
1. The entire content using `read()`
2. The number of lines
3. The number of words
4. The number of characters (excluding newlines)

Handle `FileNotFoundError` gracefully.

**Key Concepts:** read(), line/word/char counting

---

### Q2: Line-by-Line Processing (3 minutes, Low Difficulty)

Write a function `print_numbered(filename)` that reads a file and prints each line with its line number:

```
1: First line of the file
2: Second line of the file
3: Third line of the file
```

Also print total lines at the end.

**Key Concepts:** enumerate, line iteration

---

### Q3: Log File Analyzer (5 minutes, Medium Difficulty)

Given a log file with lines like:
```
2024-01-15 10:30:00 INFO User logged in
2024-01-15 10:31:00 ERROR Database connection failed
2024-01-15 10:32:00 WARNING Disk space low
2024-01-15 10:33:00 ERROR File not found
```

Write `analyze_log(filename)` that returns:
- Count of each log level (INFO, ERROR, WARNING)
- All ERROR messages
- First and last timestamps

**Key Concepts:** Parsing text, counting, filtering

---

### Q4: Config File Reader (5 minutes, Medium Difficulty)

Write `read_config(filename)` that reads a config file:
```
# Database settings
host = localhost
port = 5432
database = myapp

# App settings
debug = true
log_level = info
```

Rules: skip empty lines and comments (#). Parse `key = value` pairs into a dictionary. Convert `true`/`false` to booleans and numbers to ints.

**Key Concepts:** Parsing, type conversion, filtering

---

### Q5: File Comparison (5 minutes, Medium Difficulty)

Write `compare_files(file1, file2)` that:
- Reads both files
- Reports which lines are identical
- Reports which lines differ (showing both versions)
- Reports lines only in one file (if files have different lengths)
- Returns a summary: same count, different count, only-in-one count

**Key Concepts:** Parallel iteration, file comparison
