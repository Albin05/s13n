## Question Bank: Handle File Paths Across Platforms

---

### Q1: Basic Path Operations (3 minutes, Low Difficulty)

Using `pathlib.Path`, write code that:
1. Creates a path to `"documents/reports/annual.txt"`
2. Prints the file name, stem, suffix, and parent directory
3. Checks if the path is absolute or relative

**Key Concepts:** Path components, is_absolute()

---

### Q2: Build Paths Dynamically (3 minutes, Low Difficulty)

Write a function `build_output_path(base_dir, project, filename)` that creates platform-safe paths using `/` operator:
```python
path = build_output_path("/home/user", "myproject", "data.csv")
# /home/user/myproject/output/data.csv
```

**Key Concepts:** Path joining with `/` operator

---

### Q3: Directory Explorer (5 minutes, Medium Difficulty)

Write `list_files(directory, extension=None)` that:
- Lists all files in a directory
- Optionally filters by extension (e.g., ".py", ".txt")
- Returns sorted list of Path objects
- Handles non-existent directories gracefully

**Key Concepts:** Path.iterdir(), glob(), suffix

---

### Q4: Path Resolver (5 minutes, Medium Difficulty)

Write `resolve_path(path_string)` that:
- Converts string to Path
- Resolves to absolute path
- Expands `~` to home directory
- Checks if path exists and what type (file/dir/neither)
- Returns dict with path info

**Key Concepts:** resolve(), expanduser(), exists(), is_file()

---

### Q5: File Organizer (5 minutes, Medium Difficulty)

Write `organize_files(source_dir)` that reads files from a directory and groups them by extension, printing a report. Use pathlib exclusively — no `os.path`.

**Key Concepts:** suffix, iterdir(), grouping by extension
