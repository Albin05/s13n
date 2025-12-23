# Pre-Read: Append to Files

## What is Append Mode?

Append mode adds data to the end of a file without erasing existing content.

```python
# Write mode - OVERWRITES file
with open("data.txt", "w") as f:
    f.write("New data\n")

# Append mode - ADDS to end
with open("data.txt", "a") as f:
    f.write("More data\n")
```

## Why Use Append?

1. **Log files**: Add new log entries
2. **Data collection**: Add new records over time
3. **Preserve history**: Keep existing data

## Basic Example

```python
# First write
with open("log.txt", "a") as f:
    f.write("User logged in at 10:00\n")

# Later append
with open("log.txt", "a") as f:
    f.write("User logged out at 11:00\n")

# File now contains both lines!
```

## What's Next?
- Append mode syntax
- Practical applications
- Comparing modes
- Best practices
