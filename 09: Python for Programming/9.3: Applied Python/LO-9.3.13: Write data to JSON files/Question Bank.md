## Question Bank: Write Data to JSON Files

---

### Q1: Basic JSON Writing (3 minutes, Low Difficulty)

Create a dictionary and save it to a JSON file with indent=2. Read it back and verify the contents match.

**Key Concepts:** json.dump(), indent parameter

---

### Q2: List to JSON (3 minutes, Low Difficulty)

Convert a list of student dictionaries to JSON with sorted keys and proper indentation. Read back and print each student.

**Key Concepts:** json.dump(), sort_keys

---

### Q3: Data Collector (5 minutes, Medium Difficulty)

Write a function that loads existing JSON data (if file exists), appends new entries, and saves back. This is the read-modify-write pattern.

**Key Concepts:** Read-modify-write JSON pattern

---

### Q4: JSON Transformer (5 minutes, Medium Difficulty)

Write `transform_json(input_file, output_file, transform_fn)` that reads JSON, applies a transformation function to each item in the array, and writes the result.

**Key Concepts:** Higher-order functions, JSON pipeline

---

### Q5: Settings Manager (5 minutes, Medium Difficulty)

Build a Settings class that loads from JSON on init, provides get/set methods, and saves back to file. Handle missing file by creating with defaults.

**Key Concepts:** Class-based JSON management
