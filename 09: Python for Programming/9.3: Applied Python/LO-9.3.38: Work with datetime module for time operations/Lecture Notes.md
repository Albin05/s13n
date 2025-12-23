# Lecture Notes: Work with Datetime Module

## The datetime Module

Python's datetime module provides classes for manipulating dates and times in both simple and complex ways.


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---
### Main Classes

```python
from datetime import datetime, date, time, timedelta

# datetime: Date and time combined
now = datetime.now()
print(now)  # 2024-12-01 15:30:45.123456

# date: Just the date (year, month, day)
today = date.today()
print(today)  # 2024-12-01

# time: Just the time (hour, minute, second, microsecond)
current_time = datetime.now().time()
print(current_time)  # 15:30:45.123456

# timedelta: Duration/difference between dates or times
one_week = timedelta(days=7)
print(one_week)  # 7 days, 0:00:00
```

## Creating Date and Time Objects

```python
from datetime import datetime, date, time

# Create specific date
birthday = date(1990, 5, 15)
print(birthday)  # 1990-05-15

# Create specific datetime
meeting = datetime(2024, 12, 25, 10, 30, 0)
print(meeting)  # 2024-12-25 10:30:00

# Create specific time
alarm = time(7, 30, 0)
print(alarm)  # 07:30:00

# Current date and time
now = datetime.now()
today = date.today()
```

## Accessing Date Components

```python
from datetime import datetime

now = datetime.now()

# Access individual components
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
print(f"Microsecond: {now.microsecond}")

# Day of week (0=Monday, 6=Sunday)
print(f"Weekday: {now.weekday()}")

# Day of week name
print(f"Day name: {now.strftime('%A')}")
```

## Date Arithmetic with timedelta

```python
from datetime import date, datetime, timedelta

today = date.today()

# Add days
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
next_month = today + timedelta(days=30)

print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")
print(f"Next week: {next_week}")

# Subtract days
yesterday = today - timedelta(days=1)
last_week = today - timedelta(weeks=1)

# Time arithmetic
now = datetime.now()
in_two_hours = now + timedelta(hours=2)
thirty_mins_ago = now - timedelta(minutes=30)

print(f"In 2 hours: {in_two_hours}")
print(f"30 minutes ago: {thirty_mins_ago}")

# Complex duration
duration = timedelta(
    days=7,
    hours=3,
    minutes=30,
    seconds=45
)
future = now + duration
print(f"Future time: {future}")
```

## Calculating Date Differences

```python
from datetime import date, datetime

# Date differences
start_date = date(2024, 1, 1)
end_date = date(2024, 12, 31)

difference = end_date - start_date
print(f"Days in 2024: {difference.days}")  # 365

# Datetime differences
start_time = datetime(2024, 12, 1, 9, 0, 0)
end_time = datetime(2024, 12, 1, 17, 30, 0)

work_duration = end_time - start_time
print(f"Work hours: {work_duration}")  # 8:30:00
print(f"Total seconds: {work_duration.total_seconds()}")  # 30600.0
```

## Real-World Examples

### Example 1: Age Calculator

```python
from datetime import date

def calculate_age(birth_date):
    """Calculate age from birth date"""
    today = date.today()
    age = today.year - birth_date.year

    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

# Test
birthday = date(1990, 5, 15)
age = calculate_age(birthday)
print(f"Age: {age} years old")

def days_until_birthday(birth_date):
    """Calculate days until next birthday"""
    today = date.today()
    next_birthday = date(today.year, birth_date.month, birth_date.day)

    # If birthday already passed this year, use next year
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

    days_left = (next_birthday - today).days
    return days_left

birthday = date(1990, 12, 25)
days = days_until_birthday(birthday)
print(f"Days until birthday: {days}")
```

### Example 2: Event Countdown

```python
from datetime import datetime, timedelta

class EventCountdown:
    """Countdown to an event"""

    def __init__(self, event_name, event_date):
        self.event_name = event_name
        self.event_date = event_date

    def time_remaining(self):
        """Calculate time remaining"""
        now = datetime.now()
        diff = self.event_date - now

        if diff.total_seconds() < 0:
            return f"{self.event_name} has already passed"

        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

    def is_today(self):
        """Check if event is today"""
        return self.event_date.date() == datetime.now().date()

# Usage
new_year = EventCountdown("New Year 2025", datetime(2025, 1, 1, 0, 0, 0))
print(new_year.time_remaining())

christmas = EventCountdown("Christmas", datetime(2024, 12, 25, 0, 0, 0))
print(f"Is Christmas today? {christmas.is_today()}")
```

### Example 3: Working Hours Calculator

```python
from datetime import datetime, time, timedelta

def calculate_work_hours(clock_in, clock_out, break_minutes=60):
    """Calculate work hours with break deduction"""
    # Calculate total time
    total_time = clock_out - clock_in

    # Deduct break
    work_time = total_time - timedelta(minutes=break_minutes)

    # Convert to hours
    hours = work_time.total_seconds() / 3600

    return hours

# Usage
clock_in = datetime(2024, 12, 1, 9, 0, 0)
clock_out = datetime(2024, 12, 1, 17, 30, 0)

hours_worked = calculate_work_hours(clock_in, clock_out)
print(f"Hours worked: {hours_worked:.2f}")  # 7.50

def calculate_weekly_hours(timesheet):
    """Calculate total weekly hours"""
    total_hours = 0

    for day, times in timesheet.items():
        clock_in = times["in"]
        clock_out = times["out"]
        daily_hours = calculate_work_hours(clock_in, clock_out)
        total_hours += daily_hours
        print(f"{day}: {daily_hours:.2f} hours")

    return total_hours

# Weekly timesheet
week = {
    "Monday": {
        "in": datetime(2024, 12, 2, 9, 0, 0),
        "out": datetime(2024, 12, 2, 17, 0, 0)
    },
    "Tuesday": {
        "in": datetime(2024, 12, 3, 9, 0, 0),
        "out": datetime(2024, 12, 3, 18, 0, 0)
    },
    "Wednesday": {
        "in": datetime(2024, 12, 4, 8, 30, 0),
        "out": datetime(2024, 12, 4, 17, 30, 0)
    }
}

total = calculate_weekly_hours(week)
print(f"\nTotal hours this week: {total:.2f}")
```

### Example 4: Date Formatting

```python
from datetime import datetime

now = datetime.now()

# Common format strings
print(f"Full: {now.strftime('%Y-%m-%d %H:%M:%S')}")
# 2024-12-01 15:30:45

print(f"Date only: {now.strftime('%Y-%m-%d')}")
# 2024-12-01

print(f"Time only: {now.strftime('%H:%M:%S')}")
# 15:30:45

print(f"US format: {now.strftime('%m/%d/%Y')}")
# 12/01/2024

print(f"Readable: {now.strftime('%B %d, %Y')}")
# December 01, 2024

print(f"With day: {now.strftime('%A, %B %d, %Y')}")
# Sunday, December 01, 2024

print(f"12-hour: {now.strftime('%I:%M %p')}")
# 03:30 PM

# Common format codes:
# %Y - Year with century (2024)
# %m - Month as number (12)
# %d - Day of month (01)
# %H - Hour 24-hour (15)
# %I - Hour 12-hour (03)
# %M - Minute (30)
# %S - Second (45)
# %p - AM/PM
# %A - Full weekday name (Monday)
# %a - Short weekday name (Mon)
# %B - Full month name (December)
# %b - Short month name (Dec)
```

### Example 5: Parsing Date Strings

```python
from datetime import datetime

# Parse different date formats
date_strings = [
    ("2024-12-01", "%Y-%m-%d"),
    ("12/01/2024", "%m/%d/%Y"),
    ("01-Dec-2024", "%d-%b-%Y"),
    ("December 01, 2024", "%B %d, %Y"),
    ("2024-12-01 15:30:45", "%Y-%m-%d %H:%M:%S")
]

for date_str, format_str in date_strings:
    parsed = datetime.strptime(date_str, format_str)
    print(f"{date_str} -> {parsed}")

def parse_flexible_date(date_string):
    """Try to parse date with multiple formats"""
    formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%B %d, %Y",
        "%Y-%m-%d %H:%M:%S"
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue

    raise ValueError(f"Could not parse date: {date_string}")

# Test
dates_to_parse = ["2024-12-01", "12/01/2024", "December 01, 2024"]
for date_str in dates_to_parse:
    parsed = parse_flexible_date(date_str)
    print(f"Parsed '{date_str}' as {parsed}")
```

## Comparing Dates

```python
from datetime import date, datetime

# Date comparison
date1 = date(2024, 12, 1)
date2 = date(2024, 12, 25)

print(date1 < date2)  # True
print(date1 == date2)  # False
print(date1 > date2)  # False

# Find earliest/latest date
dates = [
    date(2024, 1, 1),
    date(2024, 6, 15),
    date(2024, 12, 31)
]

earliest = min(dates)
latest = max(dates)
print(f"Earliest: {earliest}")
print(f"Latest: {latest}")

# Check if date is in range
target_date = date(2024, 7, 4)
start_date = date(2024, 1, 1)
end_date = date(2024, 12, 31)

if start_date <= target_date <= end_date:
    print("Date is within range")
```

## Working with Weekdays

```python
from datetime import date, timedelta

def get_next_weekday(start_date, weekday):
    """
    Get next occurrence of a weekday
    weekday: 0=Monday, 1=Tuesday, ..., 6=Sunday
    """
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

today = date.today()
next_friday = get_next_weekday(today, 4)  # 4 = Friday
print(f"Next Friday: {next_friday}")

def is_weekend(date_obj):
    """Check if date is weekend"""
    return date_obj.weekday() >= 5  # Saturday=5, Sunday=6

def count_weekdays(start_date, end_date):
    """Count weekdays between two dates"""
    count = 0
    current = start_date

    while current <= end_date:
        if not is_weekend(current):
            count += 1
        current += timedelta(days=1)

    return count

start = date(2024, 12, 1)
end = date(2024, 12, 31)
weekdays = count_weekdays(start, end)
print(f"Weekdays in December: {weekdays}")
```

## Key Takeaways

1. **datetime module**: Provides date, time, datetime, and timedelta classes
2. **datetime.now()**: Get current date and time
3. **date.today()**: Get current date
4. **timedelta**: Represent duration, use for arithmetic
5. **strftime()**: Format datetime as string
6. **strptime()**: Parse string as datetime
7. **Date arithmetic**: Add/subtract using timedelta
8. **Common operations**: Age calculation, countdowns, work hours
