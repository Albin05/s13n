# Lecture Notes: Write JSON Files

## Write JSON Files

Converting Python data structures to JSON and saving to files


---

<div align="center">

![Python JSON File Write json.dump() Serialize](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.13.jpg)

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

#### Example 3: Exporting Data Collection

```python
import json
from datetime import datetime

class DataExporter:
    """Export collected data to JSON files"""

    def __init__(self):
        self.data = []

    def add_record(self, record):
        """Add a record with timestamp"""
        record['timestamp'] = datetime.now().isoformat()
        self.data.append(record)

    def export_to_json(self, filename, pretty=True):
        """Export all data to JSON file"""
        try:
            with open(filename, 'w') as file:
                if pretty:
                    json.dump(self.data, file, indent=4, ensure_ascii=False)
                else:
                    json.dump(self.data, file)

            print(f"Exported {len(self.data)} records to {filename}")
            return True
        except Exception as e:
            print(f"Error exporting data: {e}")
            return False

    def export_summary(self, filename):
        """Export summary statistics"""
        summary = {
            "total_records": len(self.data),
            "export_date": datetime.now().isoformat(),
            "first_record": self.data[0] if self.data else None,
            "last_record": self.data[-1] if self.data else None
        }

        with open(filename, 'w') as file:
            json.dump(summary, file, indent=4)

        print(f"Summary exported to {filename}")

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

#### Example 4: Custom JSON Encoder for Complex Objects

```python
import json
from datetime import datetime, date

class DateTimeEncoder(json.JSONEncoder):
    """Custom JSON encoder for datetime objects"""

    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

class Student:
    """Student class with custom JSON serialization"""

    def __init__(self, name, student_id, enrollment_date):
        self.name = name
        self.student_id = student_id
        self.enrollment_date = enrollment_date
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def to_dict(self):
        """Convert student to dictionary"""
        return {
            "name": self.name,
            "student_id": self.student_id,
            "enrollment_date": self.enrollment_date,
            "grades": self.grades
        }

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

#### Example 5: Backup and Versioning

```python
import json
import os
from datetime import datetime
import shutil

class JSONBackupManager:
    """Manage JSON files with backup and versioning"""

    def __init__(self, filename):
        self.filename = filename
        self.backup_dir = 'backups'

        # Create backup directory if it doesn't exist
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def create_backup(self):
        """Create a backup of the current file"""
        if not os.path.exists(self.filename):
            return False

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f"{self.filename.replace('.json', '')}_{timestamp}.json"
        backup_path = os.path.join(self.backup_dir, backup_name)

        shutil.copy2(self.filename, backup_path)
        print(f"Backup created: {backup_path}")
        return backup_path

    def save_data(self, data, create_backup=True):
        """Save data with optional backup"""
        # Create backup before overwriting
        if create_backup and os.path.exists(self.filename):
            self.create_backup()

        # Save new data
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Data saved to {self.filename}")

    def load_data(self):
        """Load data from file"""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return None

    def list_backups(self):
        """List all backups"""
        backups = [f for f in os.listdir(self.backup_dir)
                  if f.endswith('.json')]
        return sorted(backups, reverse=True)

    def restore_backup(self, backup_name):
        """Restore from a specific backup"""
        backup_path = os.path.join(self.backup_dir, backup_name)

        if not os.path.exists(backup_path):
            print(f"Backup {backup_name} not found")
            return False

        shutil.copy2(backup_path, self.filename)
        print(f"Restored from {backup_name}")
        return True

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
