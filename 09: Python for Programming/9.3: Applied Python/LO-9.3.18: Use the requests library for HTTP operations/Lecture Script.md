## Lecture Script: Use The Requests Library For Http Operations


---

### CS Theory Bite

> **Origin**: The **requests** library (Kenneth Reitz, 2011) replaced Python's verbose `urllib` with a human-friendly API. It's been downloaded over **1 billion times** — the most popular Python package for HTTP.
>
> **Analogy**: `requests.get()` is like **ordering food delivery** — specify what you want (URL), and the response arrives at your door.
>
> **Why it matters**: Modern software communicates over HTTP — requests is how Python talks to web APIs.



### Hook (2 minutes)

Your app needs data from a weather API, a payment gateway, and a user database — all over HTTP. The requests library makes this simple.

---

### Section 1: Basics (3 minutes)

```python
import requests

response = requests.get("https://api.example.com/data")
print(response.status_code)  # 200
print(response.json())       # Parsed JSON
```

---

### Section 2: Key Concepts (3 minutes)

**HTTP methods:**
```python
requests.get(url)      # Read data
requests.post(url)     # Create data
requests.put(url)      # Update data
requests.delete(url)   # Delete data
```

**Response object:**
```python
r.status_code  # 200, 404, 500...
r.json()       # Parse JSON body
r.text         # Raw text body
r.headers      # Response headers
```

---

### Section 3: Practical Usage (3 minutes)

```python
# Error handling
try:
    r = requests.get(url, timeout=5)
    r.raise_for_status()  # Raise for 4xx/5xx
    data = r.json()
except requests.ConnectionError:
    print("Network error")
except requests.Timeout:
    print("Request timed out")
except requests.HTTPError as e:
    print(f"HTTP error: {{e}}")
```

---

### Summary (1 minute)

1. `requests.get()` for fetching data
2. `response.json()` for JSON parsing
3. Always handle errors and set timeouts
4. Use `raise_for_status()` for error checking
