# Pre-Read: Write JSON Files

## Saving Python Data as JSON

Convert Python dictionaries and lists to JSON:

```python
import json

data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "JavaScript"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)
```

## Pretty Printing

```python
# Without indent (compact)
{"name":"Alice","age":25}

# With indent (readable)
{
  "name": "Alice",
  "age": 25
}
```

## What Can Be Saved?

✅ Dictionaries, Lists, Strings, Numbers, Booleans, None
❌ Functions, Classes, File objects

## Why Save as JSON?

1. **Configuration files**: Store settings
2. **Data exchange**: Send data between programs
3. **APIs**: Standard format for web services
