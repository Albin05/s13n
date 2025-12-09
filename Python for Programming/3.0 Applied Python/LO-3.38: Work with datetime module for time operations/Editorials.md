# Editorials: Work with Datetime Module

## Problem 1: Days Until Event

```python
from datetime import date

def days_until(target_date):
    today = date.today()
    diff = target_date - today
    return diff.days

# Test
new_year = date(2025, 1, 1)
days = days_until(new_year)
print(f"Days until New Year: {days}")
```

### Explanation
Subtract today's date from target date to get timedelta, then access days attribute.

---

## Problem 2: Format Date

```python
from datetime import date

def format_date_readable(date_obj):
    return date_obj.strftime("%B %d, %Y")

# Test
today = date.today()
formatted = format_date_readable(today)
print(formatted)
```

### Explanation
Use strftime with format codes: %B (full month), %d (day), %Y (year with century).

---

## Problem 3: Age Calculator

```python
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year

    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

# Test
birthday = date(1990, 5, 15)
age = calculate_age(birthday)
print(f"Age: {age}")
```

### Explanation
Calculate initial age by year difference. Subtract 1 if birthday hasn't occurred this year by comparing month and day tuples.

---

## Problem 4: Business Days Calculator

```python
from datetime import date, timedelta

def count_business_days(start_date, end_date):
    count = 0
    current = start_date

    while current <= end_date:
        # weekday() returns 0-6, where 5=Saturday, 6=Sunday
        if current.weekday() < 5:  # Monday-Friday
            count += 1
        current += timedelta(days=1)

    return count

# Test
start = date(2024, 12, 1)
end = date(2024, 12, 7)
count = count_business_days(start, end)
print(f"Business days: {count}")
```

### Explanation
Iterate through each day from start to end. Count days where weekday() returns 0-4 (Monday-Friday). Skip weekends (5-6).

---

## Problem 5: Meeting Scheduler

```python
from datetime import datetime, timedelta

class MeetingScheduler:
    def __init__(self):
        self.meetings = []

    def add_meeting(self, title, meeting_time):
        if self.has_conflict(meeting_time):
            raise ValueError(f"Meeting at {meeting_time} conflicts with existing meeting")

        self.meetings.append({
            "title": title,
            "time": meeting_time
        })
        # Keep meetings sorted
        self.meetings.sort(key=lambda m: m["time"])

    def has_conflict(self, meeting_time, duration_minutes=60):
        meeting_end = meeting_time + timedelta(minutes=duration_minutes)

        for meeting in self.meetings:
            existing_start = meeting["time"]
            existing_end = existing_start + timedelta(minutes=duration_minutes)

            # Check if times overlap
            if (meeting_time < existing_end and meeting_end > existing_start):
                return True

        return False

    def get_upcoming_meetings(self):
        now = datetime.now()
        return [m for m in self.meetings if m["time"] > now]

    def time_until_next_meeting(self):
        upcoming = self.get_upcoming_meetings()
        if not upcoming:
            return None

        next_meeting = upcoming[0]
        now = datetime.now()
        return next_meeting["time"] - now

# Test
scheduler = MeetingScheduler()
scheduler.add_meeting("Team Standup", datetime(2024, 12, 1, 10, 0))
scheduler.add_meeting("Client Call", datetime(2024, 12, 1, 14, 30))

try:
    scheduler.add_meeting("Review", datetime(2024, 12, 1, 10, 30))
except ValueError as e:
    print(f"Error: {e}")

upcoming = scheduler.get_upcoming_meetings()
print(f"Upcoming meetings: {len(upcoming)}")
```

### Explanation
- `add_meeting`: Checks for conflicts before adding, keeps meetings sorted
- `has_conflict`: Checks if new meeting time overlaps with any existing meeting
- `get_upcoming_meetings`: Filters meetings that are in the future
- `time_until_next_meeting`: Calculates timedelta to next upcoming meeting
