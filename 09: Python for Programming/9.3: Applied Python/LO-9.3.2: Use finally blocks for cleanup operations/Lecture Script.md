## Lecture Script: Use finally Blocks for Cleanup

**Duration:** 12 minutes

---

### Hook (2 minutes)

You open a file, process data, then close it:

```python
f = open("data.txt")
data = f.read()
process(data)  # What if this crashes?
f.close()      # This NEVER runs!
```

If `process()` raises an exception, `f.close()` is skipped. The file stays open. Resources leak.

```python
f = open("data.txt")
try:
    data = f.read()
    process(data)
finally:
    f.close()  # ALWAYS runs, crash or not!
```

`finally` is your guarantee that cleanup code **always executes**.

---

### Section 1: finally Basics (3 minutes)

```python
try:
    print("Trying...")
    result = 10 / 0
except ZeroDivisionError:
    print("Error caught!")
finally:
    print("Finally runs!")

# Output: Trying... → Error caught! → Finally runs!
```

**The guarantee:** `finally` runs whether:
- The try block succeeds
- An exception is caught
- An exception is NOT caught (finally runs, then error propagates)

---

### Section 2: finally Without except (2 minutes)

```python
try:
    result = some_operation()
finally:
    cleanup()  # Always runs
```

You don't need `except` to use `finally`. This pattern ensures cleanup even if the error propagates up.

---

### Section 3: Common Use Cases (3 minutes)

**File handling:**
```python
f = open("data.txt")
try:
    data = f.read()
finally:
    f.close()
```

**Network connections:**
```python
conn = database.connect()
try:
    conn.execute("SELECT ...")
finally:
    conn.close()
```

**Locks:**
```python
lock.acquire()
try:
    shared_resource.modify()
finally:
    lock.release()
```

---

### Section 4: finally with return (1 minute)

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Division attempted")

result = divide(10, 3)  # Prints "Division attempted", returns 3.33
result = divide(10, 0)  # Prints "Division attempted", returns None
```

Even `return` doesn't skip `finally`!

---

### Summary (1 minute)

1. `finally` **always** runs — no exceptions (pun intended)
2. Use it for cleanup: closing files, connections, releasing resources
3. Works with or without `except`
4. Even `return` doesn't skip `finally`
5. Modern Python: prefer `with` statements over manual try-finally for files
