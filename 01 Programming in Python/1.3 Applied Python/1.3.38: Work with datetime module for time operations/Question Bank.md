# Question Bank: Work with Datetime Module

## Problem 1 (Easy)

**Title:** Days Until Event

**Problem Statement:**
Write a function `days_until(target_date)` that takes a date object and returns the number of days from today until that date.

**Input Format:**
A date object representing a future date.

**Output Format:**
Integer number of days.

**Sample Usage:**
```python
from datetime import date

new_year = date(2025, 1, 1)
days = days_until(new_year)
print(f"Days until New Year: {days}")
```

**Constraints:**
- Use date.today()
- Calculate difference in days

---

## Problem 2 (Easy)

**Title:** Format Date

**Problem Statement:**
Write a function `format_date_readable(date_obj)` that takes a date object and returns it formatted as "Month Day, Year" (e.g., "December 01, 2024").

**Input Format:**
A date object.

**Output Format:**
String in format "Month Day, Year".

**Sample Usage:**
```python
from datetime import date

today = date.today()
formatted = format_date_readable(today)
print(formatted)  # "December 01, 2024"
```

**Constraints:**
- Use strftime()
- Format: "%B %d, %Y"

---

## Problem 3 (Medium)

**Title:** Age Calculator

**Problem Statement:**
Write a function `calculate_age(birth_date)` that takes a date object representing a birth date and returns the person's age in years. Account for whether the birthday has occurred this year.

**Input Format:**
A date object representing birth date.

**Output Format:**
Integer age in years.

**Sample Usage:**
```python
from datetime import date

birthday = date(1990, 5, 15)
age = calculate_age(birthday)
print(f"Age: {age}")
```

**Constraints:**
- Consider if birthday has passed this year
- Return integer age

---

## Problem 4 (Medium)

**Title:** Business Days Calculator

**Problem Statement:**
Write a function `count_business_days(start_date, end_date)` that counts the number of weekdays (Monday-Friday) between two dates, inclusive.

**Input Format:**
Two date objects (start and end).

**Output Format:**
Integer count of business days.

**Sample Usage:**
```python
from datetime import date

start = date(2024, 12, 1)  # Sunday
end = date(2024, 12, 7)    # Saturday
count = count_business_days(start, end)
print(f"Business days: {count}")  # 5
```

**Constraints:**
- Exclude weekends (Saturday and Sunday)
- Include both start and end dates if they're weekdays
- Use weekday() method (0=Monday, 6=Sunday)

---

## Problem 5 (Hard)

**Title:** Meeting Scheduler

**Problem Statement:**
Create a class `MeetingScheduler` that manages meeting schedules. It should:
- Store meetings with datetime objects
- Check for scheduling conflicts
- List upcoming meetings
- Calculate time until next meeting

**Requirements:**
```python
class MeetingScheduler:
    def __init__(self):
        # Initialize empty meeting list

    def add_meeting(self, title, meeting_time):
        # Add meeting if no conflict
        # Raise ValueError if conflict exists

    def has_conflict(self, meeting_time, duration_minutes=60):
        # Check if proposed time conflicts with existing meetings

    def get_upcoming_meetings(self):
        # Return list of meetings that haven't occurred yet

    def time_until_next_meeting(self):
        # Return timedelta to next meeting, or None if no meetings
```

**Sample Usage:**
```python
from datetime import datetime, timedelta

scheduler = MeetingScheduler()
scheduler.add_meeting("Team Standup", datetime(2024, 12, 1, 10, 0))
scheduler.add_meeting("Client Call", datetime(2024, 12, 1, 14, 30))

# Should raise ValueError (conflicts with 10:00 meeting)
# scheduler.add_meeting("Review", datetime(2024, 12, 1, 10, 30))

upcoming = scheduler.get_upcoming_meetings()
time_to_next = scheduler.time_until_next_meeting()
```

**Constraints:**
- Store meetings as dictionaries with title and time
- Assume meetings are 1 hour by default
- Handle past meetings appropriately
