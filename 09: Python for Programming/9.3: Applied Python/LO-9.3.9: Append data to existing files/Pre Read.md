# Pre-Read: Append to Files

## Introduction

**Append mode** adds data to the end of files without destroying existing content! This is how log files, transaction records, and event streams work - **safe incremental storage** that preserves history. Append mode is **additive persistence**!

### Why Append Mode Matters

**Problem**: Write mode destroys previous data:
```python
# DANGER - only last write survives!
for i in range(5):
    with open("data.txt", "w") as f:
        f.write(f"{i}\n")  # Overwrites!
# File contains only: 4
```

**Solution**: Append mode accumulates data:
```python
# SAFE - all writes preserved!
for i in range(5):
    with open("data.txt", "a") as f:
        f.write(f"{i}\n")  # Adds to end!
# File contains: 0, 1, 2, 3, 4
```

**This is incremental writing** - data accumulates, never deleted!

### Real-World Analogy

**Append mode like diary**:
- **Write mode**: Rip out all pages, write new page (destructive!)
- **Append mode**: Add new page to end (preserves history)
**Your log file is your program's diary!**

---

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
