# Lecture Notes: Use the requests Library

## Use the requests Library

Making HTTP requests to interact with web APIs


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---

## Introduction

The `requests` library implements **HTTP client functionality** - talking to web servers using the internet's protocol! HTTP is how browsers fetch web pages, but `requests` lets Python programs interact with **web APIs** programmatically. This is **HTTP for humans** - the tagline emphasizes simplicity!

### Why requests is Revolutionary

**Before requests** (urllib): Complex, verbose, frustrating:
```python
# urllib - painful!
import urllib.request
req = urllib.request.Request('http://api.com/data')
response = urllib.request.urlopen(req)
data = response.read().decode('utf-8')
# So much boilerplate!
```

**With requests**: Simple, elegant, Pythonic:
```python
# requests - beautiful!
import requests
response = requests.get('http://api.com/data')
data = response.json()
# Two lines!
```

**This is API ergonomics** - making common tasks trivially easy!

### Historical Context

**requests created by Kenneth Reitz** (2011) to simplify HTTP in Python. Became **most downloaded Python package** - over 1 billion downloads! Motto: "**HTTP for Humans**" - emphasizing usability.

**Why needed?** Python's built-in `urllib` is powerful but complex. `requests` provides **beautiful API** - simple methods, automatic JSON handling, session management. **Developer happiness matters!**

**REST APIs**: `requests` designed for **RESTful** APIs (Roy Fielding, 2000). REST uses HTTP methods (GET/POST/PUT/DELETE) to manipulate resources. JSON became standard format - `requests` handles it natively!

### Real-World Analogies

**HTTP like postal service**:
- **GET**: Request information ("send me catalog")
- **POST**: Send new data ("here's my order")
- **PUT**: Update existing ("change my address")
- **DELETE**: Remove data ("cancel subscription")
**requests is your postal worker!**

**Or like restaurant ordering**:
```python
# GET menu
menu = requests.get('https://restaurant.api/menu')

# POST order
order = {'item': 'pizza', 'size': 'large'}
receipt = requests.post('https://restaurant.api/orders', json=order)

# Check order status
status = requests.get(f'https://restaurant.api/orders/{receipt.json()["id"]}')
```

**Or like library requests**:
- **GET**: Borrow book (retrieve data)
- **POST**: Suggest new book (create data)
- **PUT**: Update book review (modify data)
- **DELETE**: Remove hold (delete data)
**Web APIs work like library systems!**

---
### Key Concepts

The requests library allows you to:
- Make HTTP requests (GET, POST, PUT, DELETE)
- Interact with RESTful APIs
- Send and receive JSON data
- Handle authentication
- Download files from the web

### Core Principles

**HTTP methods**: GET (retrieve), POST (create), PUT (update), DELETE (remove)
**Key functions**: `requests.get()`, `requests.post()`, `response.json()`, `response.status_code`

### Installation

```bash
pip install requests
```

### Syntax and Usage

```python
import requests

# GET request
response = requests.get('https://api.example.com/data')
print(response.status_code)  # 200
data = response.json()       # Parse JSON response

# POST request
payload = {'key': 'value'}
response = requests.post('https://api.example.com/data', json=payload)

# With parameters
params = {'search': 'python', 'limit': 10}
response = requests.get('https://api.example.com/search', params=params)
```

### Practical Examples

#### Example 1: Basic GET Request

```python
import requests

# Make GET request
response = requests.get('https://api.github.com')

# Check response
print(f"Status code: {response.status_code}")  # 200 = success
print(f"Content type: {response.headers['content-type']}")

# Get JSON data
data = response.json()
print(f"\nAPI endpoints available:")
for key, url in list(data.items())[:5]:
    print(f"  {key}: {url}")

# Output:
# Status code: 200
# Content type: application/json; charset=utf-8
#
# API endpoints available:
#   current_user_url: https://api.github.com/user
#   current_user_authorizations_html_url: https://github.com/settings/connections/applications{/client_id}
#   ...
```

#### Example 2: GET with Parameters

```python
import requests

# Search GitHub repositories
params = {
    'q': 'python',
    'sort': 'stars',
    'order': 'desc',
    'per_page': 5
}

response = requests.get(
    'https://api.github.com/search/repositories',
    params=params
)

if response.status_code == 200:
    data = response.json()
    print(f"Total repositories found: {data['total_count']:,}\n")

    print("Top 5 Python repositories:")
    for repo in data['items']:
        print(f"  ⭐ {repo['stargazers_count']:,} - {repo['full_name']}")
        print(f"     {repo['description'][:80]}...")
        print()

# Output:
# Total repositories found: 5,234,567
#
# Top 5 Python repositories:
#   ⭐ 180,234 - vinta/awesome-python
#      A curated list of awesome Python frameworks, libraries, software and res...
#   ...
```

#### Example 3: POST Request with JSON

```python
import requests

# API endpoint for testing POST requests
url = 'https://httpbin.org/post'

# Data to send
user_data = {
    'username': 'alice',
    'email': 'alice@example.com',
    'age': 28,
    'active': True
}

# Send POST request with JSON data
response = requests.post(url, json=user_data)

print(f"Status: {response.status_code}")

# The server echoes back what we sent
result = response.json()
print(f"\nSent data:")
print(f"  Username: {result['json']['username']}")
print(f"  Email: {result['json']['email']}")
print(f"  Age: {result['json']['age']}")

# Output:
# Status: 200
#
# Sent data:
#   Username: alice
#   Email: alice@example.com
#   Age: 28
```

#### Example 4: Error Handling and Timeouts

```python
import requests
from requests.exceptions import RequestException, Timeout, HTTPError

class APIClient:
    """Wrapper for making API requests with error handling"""

    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.timeout = timeout

    def get(self, endpoint, params=None):
        """Make GET request with error handling"""
        url = f"{self.base_url}/{endpoint}"

        try:
            response = requests.get(
                url,
                params=params,
                timeout=self.timeout
            )

            # Raise exception for bad status codes (4xx, 5xx)
            response.raise_for_status()

            return response.json()

        except Timeout:
            print(f"Request timed out after {self.timeout}s")
            return None

        except HTTPError as e:
            print(f"HTTP error occurred: {e}")
            print(f"Status code: {response.status_code}")
            return None

        except RequestException as e:
            print(f"Error making request: {e}")
            return None

    def post(self, endpoint, data):
        """Make POST request with error handling"""
        url = f"{self.base_url}/{endpoint}"

        try:
            response = requests.post(
                url,
                json=data,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()

        except Exception as e:
            print(f"Error: {e}")
            return None

# Usage
client = APIClient('https://api.github.com')

# Get user info
user = client.get('users/torvalds')
if user:
    print(f"User: {user['name']}")
    print(f"Followers: {user['followers']:,}")
    print(f"Public repos: {user['public_repos']}")

# Output:
# User: Linus Torvalds
# Followers: 123,456
# Public repos: 15
```

#### Example 5: Working with Headers and Authentication

```python
import requests
from requests.auth import HTTPBasicAuth

class GitHubAPI:
    """GitHub API client with authentication"""

    def __init__(self, token=None):
        self.base_url = 'https://api.github.com'
        self.headers = {
            'Accept': 'application/vnd.github.v3+json'
        }

        if token:
            self.headers['Authorization'] = f'token {token}'

    def get_user(self, username):
        """Get user information"""
        url = f"{self.base_url}/users/{username}"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        return None

    def get_repo(self, owner, repo):
        """Get repository information"""
        url = f"{self.base_url}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        return None

    def get_rate_limit(self):
        """Check API rate limit"""
        url = f"{self.base_url}/rate_limit"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            core = data['rate']
            return {
                'limit': core['limit'],
                'remaining': core['remaining'],
                'reset_time': core['reset']
            }
        return None

# Usage (without token for public data)
api = GitHubAPI()

# Get user info
user = api.get_user('octocat')
if user:
    print(f"User: {user['name']}")
    print(f"Bio: {user['bio']}")
    print(f"Location: {user['location']}")

# Get repo info
repo = api.get_repo('psf', 'requests')
if repo:
    print(f"\nRepo: {repo['full_name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']:,}")
    print(f"Language: {repo['language']}")

# Check rate limit
limit = api.get_rate_limit()
if limit:
    print(f"\nAPI Rate Limit:")
    print(f"  Limit: {limit['limit']} requests/hour")
    print(f"  Remaining: {limit['remaining']}")

# Output:
# User: The Octocat
# Bio: None
# Location: San Francisco
#
# Repo: psf/requests
# Description: A simple, yet elegant, HTTP library.
# Stars: 51,234
# Language: Python
#
# API Rate Limit:
#   Limit: 60 requests/hour
#   Remaining: 58
```

### Common HTTP Status Codes

```python
# Success codes (2xx)
200  # OK - Request succeeded
201  # Created - Resource created successfully
204  # No Content - Success, no response body

# Client error codes (4xx)
400  # Bad Request - Invalid request
401  # Unauthorized - Authentication required
403  # Forbidden - No permission
404  # Not Found - Resource doesn't exist
429  # Too Many Requests - Rate limit exceeded

# Server error codes (5xx)
500  # Internal Server Error
503  # Service Unavailable
```

### Best Practices

1. **Always handle errors**: Use try/except for network requests
2. **Set timeouts**: Prevent requests from hanging forever
3. **Use sessions**: For multiple requests to same host
4. **Respect rate limits**: Don't spam APIs
5. **Use HTTPS**: For secure communication
6. **Handle status codes**: Check `response.status_code`
7. **Close resources**: Use context managers or sessions

### Common Mistakes

1. **Not checking status codes**: Always verify request succeeded
2. **No timeout**: Requests can hang indefinitely
3. **Hardcoding credentials**: Use environment variables
4. **Not handling exceptions**: Network requests can fail
5. **Making too many requests**: Respect API rate limits

### Session Usage

```python
import requests

# Create session for multiple requests
session = requests.Session()
session.headers.update({'User-Agent': 'MyApp/1.0'})

# All requests use same session
response1 = session.get('https://api.example.com/users')
response2 = session.get('https://api.example.com/posts')

# Close session
session.close()

# Or use context manager
with requests.Session() as session:
    response = session.get('https://api.example.com/data')
    # Session automatically closed
```

### Key Takeaways

1. `requests` is the standard library for HTTP in Python
2. Use `requests.get()` for GET requests
3. Use `requests.post()` for sending data
4. Check `response.status_code` for success (200-299)
5. Use `response.json()` to parse JSON responses
6. Always handle exceptions and timeouts
7. Respect API rate limits and terms of service
