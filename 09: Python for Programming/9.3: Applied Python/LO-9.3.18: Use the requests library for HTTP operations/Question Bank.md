## Question Bank: Use the Requests Library

---

### Q1: Basic GET Request (3 minutes, Low Difficulty)
Write code to make a GET request to a public API, check the status code, and print the JSON response. Handle connection errors.

**Key Concepts:** requests.get, status_code, json()

---

### Q2: Query Parameters (3 minutes, Low Difficulty)
Make a GET request with query parameters using the `params` dict. Print the full URL that was requested.

**Key Concepts:** params dict, response.url

---

### Q3: POST Request (5 minutes, Medium Difficulty)
Send a POST request with JSON data. Set headers including Content-Type and Authorization. Check response and handle errors.

**Key Concepts:** requests.post, json=, headers=

---

### Q4: API Data Fetcher (5 minutes, Medium Difficulty)
Write a function that fetches paginated data from an API, handling pagination until all data is collected. Include retry logic for failed requests.

**Key Concepts:** Pagination, retry pattern

---

### Q5: Mini API Client (5 minutes, Medium Difficulty)
Build a class `APIClient` with methods for GET, POST, PUT, DELETE. Include base_url, default headers, timeout, and error handling.

**Key Concepts:** Class-based API client
