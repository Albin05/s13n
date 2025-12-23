# Post-Class Quiz: Work with Datetime Module

## Q1: What's the difference between date.today() and datetime.now()?
A) No difference
B) date.today() returns only date, datetime.now() returns date and time
C) datetime.now() is faster

<details><summary>Answer</summary>
B) date.today() returns only date, datetime.now() returns date and time

Explanation: `date.today()` returns a date object with year, month, and day. `datetime.now()` returns a datetime object with year, month, day, hour, minute, second, and microsecond.
</details>

## Q2: What class represents a duration between two dates?
A) duration
B) timedelta
C) timespan

<details><summary>Answer</summary>
B) timedelta

Explanation: The `timedelta` class represents a duration or difference between two dates or times. It's used for date arithmetic.
</details>

## Q3: How do you add 7 days to a date?
A) date + 7
B) date.add_days(7)
C) date + timedelta(days=7)

<details><summary>Answer</summary>
C) date + timedelta(days=7)

Explanation: Use timedelta to perform date arithmetic: `new_date = old_date + timedelta(days=7)`.
</details>

## Q4: What does strftime() do?
A) Parse a string into a datetime
B) Format a datetime as a string
C) Get string representation of time

<details><summary>Answer</summary>
B) Format a datetime as a string

Explanation: `strftime()` (string format time) converts a datetime object to a string with a specified format. Use `strptime()` for the reverse (parse string to datetime).
</details>

## Q5: What does datetime.weekday() return for Monday?
A) 0
B) 1
C) "Monday"

<details><summary>Answer</summary>
A) 0

Explanation: `weekday()` returns 0 for Monday, 1 for Tuesday, ..., 6 for Sunday. This is useful for identifying weekdays vs weekends.
</details>
