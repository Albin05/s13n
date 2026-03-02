# Write JSON Files

## Write JSON Files

Converting Python data structures to JSON and saving to files

---

<div align="center">

![Python JSON File Write json.dump() Serialize](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/.jpg)

*Writing JSON serializes a nested tree structure of data into a formatted text file*

</div>

---
### Key Concepts

Writing JSON files allows you to:
- Save configuration settings
- Store application data persistently
- Export data for other applications
- Create API-compatible data formats

### Core Principles

**Important functions**: `json.dump()`, `json.dumps()`, converting Python dicts/lists to JSON

### Syntax and Usage

```python
import json

# Write to file
data = {"name": "Alice", "age": 25}
with open('data.json', 'w') as file:
    json.dump(data, file)  # Converts Python dict to JSON and writes to file

# Convert to JSON string
json_string = json.dumps(data)  # Converts to JSON string
json_pretty = json.dumps(data, indent=4)  # Pretty-printed JSON
```

### Practical Examples

#### Example 1: Writing Simple JSON File

```python
import json

# Create user data
user_data = {
    "username": "alice_2024",
    "email": "alice@example.com",
    "age": 28,
    "is_active": True,
    "hobbies": ["reading", "gaming", "photography"],
    "address": {
        "street": "123 Main St",
        "city": "Boston",
        "zipcode": "02101"
    }
}

# Write to JSON file
with open('user_profile.json', 'w') as file:
    json.dump(user_data, file, indent=4)

print("User profile saved to user_profile.json")

# Read it back to verify
with open('user_profile.json', 'r') as file:
    loaded_data = json.load(file)

print(f"Loaded username: {loaded_data['username']}")
print(f"Loaded hobbies: {loaded_data['hobbies']}")

# Output:
# User profile saved to user_profile.json
# Loaded username: alice_2024
# Loaded hobbies: ['reading', 'gaming', 'photography']
```

#### Example 2: Saving Configuration Settings

```python
import json

class ConfigManager:
    """Manage application configuration with JSON"""

    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from file or create default"""
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Return default configuration
            return {
                "app_name": "MyApp",
                "version": "1.0.0",
                "debug": False,
                "database": {
                    "host": "localhost",
                    "port": 5432
                },
                "features": {
                    "auto_save": True,
                    "dark_mode": False
                }
            }

    def save_config(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4, sort_keys=True)
        print(f"Configuration saved to {self.config_file}")

    def update_setting(self, section, key, value):
        """Update a configuration setting"""
        if section in self.config:
            self.config[section][key] = value
            self.save_config()
            print(f"Updated {section}.{key} = {value}")
        else:
            print(f"Section '{section}' not found")

    def get_setting(self, section, key, default=None):
        """Get a configuration setting"""
        return self.config.get(section, {}).get(key, default)

# Usage
config = ConfigManager()

# Update settings
config.update_setting('features', 'dark_mode', True)
# Updated features.dark_mode = True
# Configuration saved to config.json

config.update_setting('database', 'port', 3306)
# Updated database.port = 3306
# Configuration saved to config.json

# Get settings
debug_mode = config.get_setting('app', 'debug', False)
print(f"Debug mode: {debug_mode}")
# Debug mode: False
```

# Usage
exporter = DataExporter()

# Add some records
exporter.add_record({"user_id": 1, "action": "login", "status": "success"})
exporter.add_record({"user_id": 1, "action": "view_page", "page": "dashboard"})
exporter.add_record({"user_id": 2, "action": "login", "status": "success"})
exporter.add_record({"user_id": 1, "action": "logout", "status": "success"})

# Export to JSON
exporter.export_to_json('user_activity.json')
# Exported 4 records to user_activity.json

exporter.export_summary('activity_summary.json')
# Summary exported to activity_summary.json
```

# Create students
students = [
    Student("Alice", "S001", date(2023, 9, 1)),
    Student("Bob", "S002", date(2023, 9, 1)),
    Student("Charlie", "S003", date(2024, 1, 15))
]

students[0].add_grade("Math", 95)
students[0].add_grade("Science", 88)
students[1].add_grade("Math", 78)
students[1].add_grade("English", 92)

# Convert to dict for JSON serialization
students_data = [s.to_dict() for s in students]

# Write with custom encoder
with open('students.json', 'w') as file:
    json.dump(students_data, file, cls=DateTimeEncoder, indent=4)

print("Students data saved with date formatting")

# Verify
with open('students.json', 'r') as file:
    loaded_students = json.load(file)

for student in loaded_students:
    print(f"{student['name']}: Enrolled on {student['enrollment_date']}")

# Output:
# Students data saved with date formatting
# Alice: Enrolled on 2023-09-01
# Bob: Enrolled on 2023-09-01
# Charlie: Enrolled on 2024-01-15
```

# Usage
manager = JSONBackupManager('important_data.json')

# Save some data
data1 = {"version": 1, "settings": {"theme": "light"}}
manager.save_data(data1, create_backup=False)
# Data saved to important_data.json

# Update data (creates backup)
data2 = {"version": 2, "settings": {"theme": "dark", "language": "en"}}
manager.save_data(data2, create_backup=True)
# Backup created: backups/important_data_20241201_123456.json
# Data saved to important_data.json

# List available backups
backups = manager.list_backups()
print(f"Available backups: {backups}")

# Restore if needed
if backups:
    manager.restore_backup(backups[0])
```

### Best Practices

1. **Use indent parameter**: Makes JSON files human-readable
2. **Handle encoding**: Use `ensure_ascii=False` for non-ASCII characters
3. **Sort keys**: Use `sort_keys=True` for consistent output
4. **Create backups**: Before overwriting important data
5. **Validate before writing**: Ensure data is serializable

### Common Mistakes

1. **Not using context managers**: Always use `with` statement
2. **Forgetting to close files**: Can lead to data loss
3. **Writing non-serializable objects**: Convert custom objects to dicts first
4. **Not handling errors**: Always catch exceptions when writing files

### JSON Serialization Options

```python
json.dump(data, file,
    indent=4,              # Pretty print with 4 spaces
    sort_keys=True,        # Sort dictionary keys
    ensure_ascii=False,    # Allow non-ASCII characters
    separators=(',', ': ')  # Custom separators
)
```

### Real-World Applications

- **Configuration management**: Storing app settings
- **Data persistence**: Saving user preferences and state
- **API data export**: Preparing data for external systems
- **Logging**: Structured log file output
- **Testing**: Creating test fixtures and mock data

### Key Takeaways

1. Use `json.dump(data, file)` to write JSON to files
2. Use `json.dumps(data)` to convert to JSON string
3. Use `indent` parameter for readable formatting
4. Always use context managers (`with` statement)
5. Convert custom objects to dicts before serialization
6. Handle exceptions to prevent data loss
7. Create backups before overwriting important files
