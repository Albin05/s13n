## Question Bank: Read JSON Files and Parse Data

---

### Q1: Basic JSON Reading (3 minutes, Low Difficulty)

Write a program that reads a JSON file containing a list of users and prints each user's name and email.

**Key Concepts:** json.load(), iterating JSON arrays

---

### Q2: Nested JSON Access (3 minutes, Low Difficulty)

Given a JSON file with nested structure (user with address, preferences), safely extract deeply nested values using `.get()` chains. Handle missing keys gracefully.

**Key Concepts:** Nested dict access, safe navigation

---

### Q3: JSON API Response Parser (5 minutes, Medium Difficulty)

Write `parse_response(json_file)` that reads a JSON API response with status and data fields, extracts the data array, filters by a condition, and returns processed results.

**Key Concepts:** Real-world JSON structure, filtering

---

### Q4: Config from JSON (5 minutes, Medium Difficulty)

Write `load_config(filename, defaults)` that reads a JSON config file, merges with default values (defaults for missing keys), and validates required fields exist.

**Key Concepts:** JSON + dict merging, validation

---

### Q5: JSON Data Aggregator (5 minutes, Medium Difficulty)

Read multiple JSON files containing sales data, aggregate totals by category, and print a summary report with totals and averages per category.

**Key Concepts:** Multiple JSON files, aggregation
