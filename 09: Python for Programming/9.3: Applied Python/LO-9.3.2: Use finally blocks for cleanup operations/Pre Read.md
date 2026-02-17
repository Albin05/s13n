## Pre-Read: Use finally Blocks for Cleanup


---

## Introduction

The `finally` block guarantees that cleanup code executes **no matter what** - even if exceptions occur or early returns happen. This prevents **resource leaks**: files left open, database connections not closed, memory not freed. `finally` is your **cleanup guarantee**!

### Why Guaranteed Cleanup Matters

**The resource leak problem**: Cleanup might be skipped:
```python
# DANGEROUS - many ways to skip cleanup!
file = open("log.txt", "w")
file.write(data)  # Exception here?
return True  # Early return?
file.close()  # Might not execute!
```

**Solution**: `finally` ALWAYS executes:
```python
# SAFE - cleanup guaranteed!
file = open("log.txt", "w")
try:
    file.write(data)
    return True  # Even with return...
finally:
    file.close()  # ...this STILL runs!
```

**This is deterministic cleanup** - you control exactly when resources are released!

### Real-World Analogy

**Finally block like locking your door**:
- **Try**: Leave house for errands
- **Success**: Complete all errands
- **Emergency**: Get called back early
- **Finally**: Lock door when you return (ALWAYS)
**Door gets locked whether you finished errands or not!**

### The Modern Alternative

Python's `with` statement is cleaner for common cases:
```python
# Using with (preferred)
with open("data.txt") as file:
    data = file.read()  # Auto-closed!

# Equivalent to:
file = open("data.txt")
try:
    data = file.read()
finally:
    file.close()
```

**Use `with` when possible, `finally` for custom cleanup!**

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
