## Pre-Read: Use finally Blocks for Cleanup

**Duration:** 5 minutes

---

### The Problem

What if your code crashes before cleanup happens?

```python
file = open("data.txt")
data = file.read()
process(data)    # If this crashes...
file.close()     # ...this never runs!
```

---

### The Solution: finally

```python
file = open("data.txt")
try:
    data = file.read()
    process(data)
finally:
    file.close()  # ALWAYS runs!
```

`finally` guarantees the cleanup code executes whether the try block succeeds or fails.

---

### When Does finally Run?

- Try succeeds → finally runs
- Exception caught → finally runs
- Exception NOT caught → finally runs, then error propagates
- Return statement in try → finally STILL runs

---

### Key Takeaway

Use `finally` whenever you need guaranteed cleanup — closing files, database connections, releasing locks, or stopping timers.
