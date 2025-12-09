# Pre-Read: Work with Datetime Module

## The datetime Module

Python's datetime module provides classes for working with dates and times:

```python
from datetime import datetime, date, time

# Get current date and time
now = datetime.now()
print(now)  # 2024-12-01 15:30:45.123456

# Get current date only
today = date.today()
print(today)  # 2024-12-01

# Create specific date
birthday = date(1990, 5, 15)
print(birthday)  # 1990-05-15
```

## Date Operations

```python
from datetime import date, timedelta

# Create dates
date1 = date(2024, 12, 1)
date2 = date(2024, 12, 25)

# Calculate difference
diff = date2 - date1
print(f"Days until Christmas: {diff.days}")  # 24

# Add days
next_week = date1 + timedelta(days=7)
print(next_week)  # 2024-12-08
```

## Formatting Dates

```python
from datetime import datetime

now = datetime.now()

# Format as string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # 2024-12-01 15:30:45

# Parse from string
date_string = "2024-12-25"
christmas = datetime.strptime(date_string, "%Y-%m-%d")
print(christmas)  # 2024-12-25 00:00:00
```
