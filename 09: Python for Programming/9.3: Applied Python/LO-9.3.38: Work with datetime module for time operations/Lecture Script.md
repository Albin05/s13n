# Lecture Script: LO-9.3.38 Work with Datetime Module for Time Operations


### CS Theory Bite

> **Origin**: Time computation is notoriously complex — **leap years**, **time zones**, **daylight saving**, and the **Unix epoch** (Jan 1, 1970). The **Y2K bug** and upcoming **Year 2038 problem** show the consequences of simplistic time handling.
>
> **Analogy**: The datetime module is like a **world clock** — it handles the complexity of calendars, time zones, and durations so you don't have to.
>
> **Why it matters**: Never implement date math manually — use datetime to avoid off-by-one errors, leap year bugs, and timezone disasters.


## [0:00-0:02] Hook (2 min)
**Say**: "How old are you in days? When's your next birthday? How many working hours this week? Time calculations are EVERYWHERE in software. Python's datetime module makes it simple: datetime.now(), timedelta(days=7), done! From age calculators to event countdowns to work hour tracking — master datetime, master time!"

**Demo**:
```python
from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(f"Right now: {now}")

# How many days until New Year?
new_year = datetime(2025, 1, 1)
days_left = (new_year - now).days
print(f"Days until New Year: {days_left}")

# One week from today
next_week = date.today() + timedelta(weeks=1)
print(f"One week from now: {next_week}")
```

**Say**: "That's datetime power! Let's master it."

## [0:02-0:06] Creating Date and Time Objects (4 min)

**Say**: "Four main classes: date (just date), time (just time), datetime (both), and timedelta (duration)."

**Live Code**:
```python
from datetime import datetime, date, time

# Create specific date
birthday = date(1990, 5, 15)
print(f"Birthday: {birthday}")  # 1990-05-15

# Create specific datetime
meeting = datetime(2024, 12, 25, 10, 30, 0)
print(f"Meeting: {meeting}")  # 2024-12-25 10:30:00

# Create specific time
alarm = time(7, 30, 0)
print(f"Alarm: {alarm}")  # 07:30:00

# Current date and time
now = datetime.now()
today = date.today()
current_time = datetime.now().time()

print(f"Now: {now}")
print(f"Today: {today}")
print(f"Current time: {current_time}")

# Access components
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")

# Day of week (0=Monday, 6=Sunday)
print(f"Weekday: {now.weekday()}")
print(f"Day name: {now.strftime('%A')}")
```

**Point out**: "datetime.now() gives current moment. date.today() gives just the date!"

**Emphasize**: "Year, month, day parameters are REQUIRED. Hour, minute, second are optional!"

## [0:06-0:10] Date Arithmetic with timedelta (4 min)

**Say**: "timedelta represents a duration. Add or subtract it from dates!"

**Live Code**:
```python
from datetime import date, datetime, timedelta

today = date.today()
print(f"Today: {today}")

# Add days
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
next_month = today + timedelta(days=30)

print(f"Tomorrow: {tomorrow}")
print(f"Next week: {next_week}")
print(f"Next month: {next_month}")

# Subtract days
yesterday = today - timedelta(days=1)
last_week = today - timedelta(weeks=1)

print(f"Yesterday: {yesterday}")
print(f"Last week: {last_week}")

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
print(f"7 days, 3:30:45 from now: {future}")
```

**Say**: "timedelta can take days, weeks, hours, minutes, seconds, microseconds!"

## [0:10-0:13] Calculating Date Differences (3 min)

**Say**: "Subtract two dates to get the duration between them."

**Live Code**:
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
print(f"Work time: {work_duration}")  # 8:30:00
print(f"Total seconds: {work_duration.total_seconds()}")  # 30600.0

# Convert to hours
hours = work_duration.total_seconds() / 3600
print(f"Hours worked: {hours:.2f}")  # 8.50

# Age calculation
birth_date = date(1990, 5, 15)
today = date.today()
age_days = (today - birth_date).days
age_years = age_days // 365
print(f"Age: {age_years} years ({age_days} days)")
```

**Point out**: "Subtracting dates returns a timedelta. Use .days, .seconds, .total_seconds()!"

## [0:13-0:16] Real-World Example: Age Calculator (3 min)

**Say**: "Calculate exact age and days until next birthday."

**Live Code**:
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

def days_until_birthday(birth_date):
    """Calculate days until next birthday"""
    today = date.today()
    next_birthday = date(today.year, birth_date.month, birth_date.day)

    # If birthday already passed this year, use next year
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

    days_left = (next_birthday - today).days
    return days_left

# Test
birthday = date(1990, 5, 15)
age = calculate_age(birthday)
days = days_until_birthday(birthday)

print(f"Age: {age} years old")
print(f"Days until birthday: {days}")

# Another example
def is_birthday_today(birth_date):
    """Check if today is someone's birthday"""
    today = date.today()
    return (today.month, today.day) == (birth_date.month, birth_date.day)

if is_birthday_today(birthday):
    print("Happy Birthday!")
else:
    print(f"Not your birthday yet. {days} days to go!")
```

**Say**: "Birthday logic is tricky — handle year boundaries carefully!"

## [0:16-0:19] Real-World Example: Work Hours Calculator (3 min)

**Say**: "Track clock-in/clock-out times and calculate pay."

**Live Code**:
```python
from datetime import datetime, timedelta

def calculate_work_hours(clock_in, clock_out, break_minutes=60):
    """Calculate work hours with break deduction"""
    # Calculate total time
    total_time = clock_out - clock_in

    # Deduct break
    work_time = total_time - timedelta(minutes=break_minutes)

    # Convert to hours
    hours = work_time.total_seconds() / 3600

    return hours

# Single day
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

# Calculate pay
hourly_rate = 25.00
weekly_pay = total * hourly_rate
print(f"Weekly pay: ${weekly_pay:.2f}")
```

**Say**: "Perfect for time-tracking apps and payroll systems!"

## [0:19-0:21] Formatting Dates (2 min)

**Say**: "strftime() formats dates as strings. strptime() parses strings as dates."

**Live Code**:
```python
from datetime import datetime

now = datetime.now()

# Common format strings
print(f"ISO format: {now.strftime('%Y-%m-%d %H:%M:%S')}")
# 2024-12-01 15:30:45

print(f"US format: {now.strftime('%m/%d/%Y')}")
# 12/01/2024

print(f"Readable: {now.strftime('%B %d, %Y')}")
# December 01, 2024

print(f"With day: {now.strftime('%A, %B %d, %Y')}")
# Sunday, December 01, 2024

print(f"12-hour: {now.strftime('%I:%M %p')}")
# 03:30 PM

# Parse string as datetime
date_string = "2024-12-25"
parsed = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed: {parsed}")

# Parse with time
datetime_string = "12/25/2024 10:30 AM"
parsed = datetime.strptime(datetime_string, "%m/%d/%Y %I:%M %p")
print(f"Parsed datetime: {parsed}")
```

**Point out**: "Format codes: %Y=year, %m=month, %d=day, %H=hour(24), %I=hour(12), %M=minute, %S=second!"

## [0:21-0:23] Real-World Example: Event Countdown (2 min)

**Say**: "Build a countdown timer for upcoming events."

**Live Code**:
```python
from datetime import datetime

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

        return f"{days} days, {hours} hours, {minutes} minutes"

    def is_today(self):
        """Check if event is today"""
        return self.event_date.date() == datetime.now().date()

# Usage
new_year = EventCountdown("New Year 2025", datetime(2025, 1, 1, 0, 0, 0))
print(new_year.time_remaining())

christmas = EventCountdown("Christmas", datetime(2024, 12, 25, 0, 0, 0))
print(f"Is Christmas today? {christmas.is_today()}")

# Another example
def create_reminder(event_name, days_before):
    """Create reminder date"""
    from datetime import timedelta
    event_date = datetime(2024, 12, 25)
    reminder_date = event_date - timedelta(days=days_before)
    return reminder_date

reminder = create_reminder("Christmas", 7)
print(f"Set reminder for: {reminder.strftime('%B %d, %Y')}")
```

**Say**: "Perfect for birthday reminders, subscription renewals, project deadlines!"

## [0:23-0:24] Practice Challenge (1 min)

**Challenge**: "Calculate how many weekdays between two dates (exclude weekends)."

**Skeleton**:
```python
from datetime import date, timedelta

def count_weekdays(start_date, end_date):
    # TODO: Count only Monday-Friday
    pass

# Test
start = date(2024, 12, 1)
end = date(2024, 12, 31)
weekdays = count_weekdays(start, end)
print(f"Weekdays in December: {weekdays}")
```

**Solution** (show after 1 minute):
```python
def count_weekdays(start_date, end_date):
    count = 0
    current = start_date

    while current <= end_date:
        # Monday=0, Sunday=6. Weekdays are 0-4
        if current.weekday() < 5:
            count += 1
        current += timedelta(days=1)

    return count
```

## [0:24-0:25] Wrap-up (1 min)

**Key Points**:
1. **Main classes**: date, time, datetime, timedelta
2. **Current time**: datetime.now(), date.today()
3. **Arithmetic**: Use timedelta for adding/subtracting
4. **Differences**: Subtract dates to get timedelta
5. **Formatting**: strftime() to format, strptime() to parse

**Common Format Codes**:
- %Y: 4-digit year (2024)
- %m: 2-digit month (12)
- %d: 2-digit day (01)
- %H: 24-hour (15)
- %I: 12-hour (03)
- %M: minute (30)
- %S: second (45)
- %p: AM/PM
- %A: Full weekday (Monday)
- %B: Full month (December)

**Common Mistakes**:
- Forgetting that months/days start at 1, not 0
- Not handling year boundaries in birthday calculations
- Comparing date and datetime directly (use .date())
- Time zones (use pytz or zoneinfo for timezone-aware dates)

**Real-World Use Cases**:
- Age calculators
- Birthday reminders
- Work hour tracking
- Event countdowns
- Scheduling systems
- Subscription renewals
- Time-based triggers

**Advanced Topics** (beyond this course):
- Timezones: pytz, zoneinfo modules
- Relative dates: dateutil.relativedelta
- Business days: excludes weekends/holidays
- Recurring events: rrule from dateutil

**Closing**: "Time operations are everywhere in software! Master datetime for scheduling, reminders, time tracking, and more. Remember: datetime.now() for current time, timedelta for durations, strftime/strptime for formatting. Time to build!"
