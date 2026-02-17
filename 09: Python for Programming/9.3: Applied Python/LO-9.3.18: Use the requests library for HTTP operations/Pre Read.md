## Pre-Read: Use The Requests Library For Http Operations


---

### The Requests Library

The most popular Python library for HTTP requests:

```python
import requests
response = requests.get("https://api.example.com/users")
data = response.json()
```

Install with: `pip install requests`

---

### Key Points

- `requests.get(url)` fetches data
- `response.json()` parses JSON
- Always handle errors and timeouts
