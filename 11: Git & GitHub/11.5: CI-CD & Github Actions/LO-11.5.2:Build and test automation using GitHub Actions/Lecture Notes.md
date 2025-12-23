
## 1. Where This Topic Fits in the Overall GitHub Workflow

So far, you have learned how teams manage work and collaboration using GitHub:

* **Issues & Milestones** to plan and track tasks
* **Project Boards** to visualize progress
* **Commits & Pull Requests** to manage code changes
* **CI/CD concepts** to understand why automation is needed

All these practices answer:

* *What work needs to be done?*
* *Who is doing it?*
* *What code was changed?*

However, one very important question still remains:

> **How do we make sure the code works every time someone pushes changes?**

This is where **GitHub Actions** comes in.
It allows us to automatically **run code, verify logic, and view results** whenever changes are made.

---

## 2. What is GitHub Actions? (Conceptual Overview)

**GitHub** Actions is GitHub’s built-in **automation and CI/CD system**.

Using GitHub Actions, you can:

* Automatically run programs
* Validate logic
* Print output to console
* Detect errors early
* Avoid manual checking

A key idea to remember is:

> GitHub Actions does not understand your programming language.
> It only executes the commands you tell it to run.

All automation rules are defined using a **YAML configuration file** stored inside the repository.

---

## 3. Understanding YAML (Only What You Need)

YAML is a **configuration language**, not a programming language.

It is used in GitHub Actions to:

* Define triggers
* Define jobs
* Define steps

Important basics:

* Indentation matters
* Uses key–value structure
* Easy to read if formatting is correct

Example:

```yaml
name: Sample Workflow
on: push
jobs:
  demo-job:
    runs-on: ubuntu-latest
```

You do **not** need deep YAML knowledge to use GitHub Actions effectively.

---

## 4. Anatomy of a GitHub Actions Workflow

Every GitHub Actions workflow has **three core parts**:

### Trigger (`on`)

Defines **when** the workflow should run.

### Job

Defines **where** the workflow runs (operating system and environment).

### Steps

Defines **what commands** should be executed.

A simple mental model is:

```
Event → Job → Steps → Console Output
```

---

## 5. Workflow Triggers (Very Important Concept)

Triggers decide **when automation runs**.

A common real-world rule is:

* Run automation **only when code reaches the main branch**

Example:

```yaml
on:
  push:
    branches:
      - main
```

This means:

* Pushes to `main` → workflow runs
* Pushes to other branches → workflow does NOT run

You can also trigger workflows on Pull Requests:

```yaml
on:
  pull_request:
    branches:
      - main
```

This protects the project by ensuring checks run **before merging**.

---

## 6. Where GitHub Actions Files Live

GitHub Actions workflows must be stored in this exact path:

```
.github/
  workflows/
    ci.yml
```

If:

* Folder name is wrong
* File extension is not `.yml` or `.yaml`

➡️ GitHub Actions will **not detect the workflow**.

---

## 7. JavaScript Example (Custom Logic, No Testing Framework)

### Goal

* Create a `checkPalindrome` function
* Call it from another file
* Run custom test cases
* View output in GitHub Actions logs

---

### JavaScript Project Structure

```
src/
  palindrome.js
  test.js
```

#### `palindrome.js`

```js
function checkPalindrome(word) {
  const reversed = word.split('').reverse().join('');
  return word === reversed;
}

module.exports = checkPalindrome;
```

#### `test.js`

```js
const checkPalindrome = require('./palindrome');

const testCases = ["madam", "racecar", "hello", "level", "world"];

testCases.forEach(word => {
  const result = checkPalindrome(word);
  console.log(`Word: ${word} | Palindrome: ${result}`);
});
```

This approach avoids frameworks and keeps automation **easy to understand**.

---

### GitHub Actions Workflow for JavaScript

```yaml
name: JS Palindrome Check

on:
  push:
    branches:
      - main

jobs:
  js-ci:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 18

      - name: Run palindrome tests
        run: node src/test.js
```

All `console.log` output is visible in:
**GitHub → Actions → Workflow Run → Logs**

---

## 8. Python Example (Custom Logic, No Testing Framework)

### Python Project Structure

```
src/
  palindrome.py
  test.py
```

#### `palindrome.py`

```python
def check_palindrome(word):
    return word == word[::-1]
```

#### `test.py`

```python
from palindrome import check_palindrome

test_cases = ["madam", "racecar", "hello", "level", "python"]

for word in test_cases:
    result = check_palindrome(word)
    print(f"Word: {word} | Palindrome: {result}")
```

---

### GitHub Actions Workflow for Python

```yaml
name: Python Palindrome Check

on:
  push:
    branches:
      - main

jobs:
  python-ci:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Run palindrome tests
        run: python src/test.py
```

The `print()` output is shown directly in the workflow logs.

---

## 9. Viewing Workflow Runs and Console Logs

To view results:

1. Open the repository
2. Click the **Actions** tab
3. Select a workflow run
4. Click the job name
5. Expand steps to see console output

This is how developers **debug CI pipelines** in real projects.

---

## 10. One Typical GitHub Actions YAML File (Generic Template)

The following workflow structure covers **most CI use cases**:

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build-and-check:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup runtime
        run: echo "Setup language/runtime here"

      - name: Run application logic
        run: echo "Run build or tests here"

      - name: Print completion message
        run: echo "CI pipeline completed successfully"
```

Key idea:

> **This structure stays the same for all languages.
> Only the commands change.**

---

## 11. Using GitHub Actions Templates (No Manual YAML Needed)

![Image](https://images.prismic.io/hatica/fad50f4b-8645-41ee-8e23-bacf2bfea3d6_git-workflow-2.png?auto=compress%2Cformat\&h=815\&rect=0%2C0%2C1319%2C896\&w=1200\&utm_source=chatgpt.com)

![Image](https://docs.github.com/assets/cb-71777/images/help/repository/actions-quickstart-commit-new-file.png?utm_source=chatgpt.com)

![Image](https://user-images.githubusercontent.com/1865328/86147571-2de93700-babf-11ea-8a08-e4beffd3abe9.png?utm_source=chatgpt.com)

GitHub provides **ready-made workflow templates**, so beginners do not need to write YAML from scratch.

### How to Use Templates

1. Open your repository
2. Go to the **Actions** tab
3. GitHub suggests templates based on your project
4. Choose a template (Node.js, Python, etc.)
5. Click **Configure**
6. GitHub auto-generates the workflow file
7. Commit the file

Once committed, the workflow becomes active immediately.

---

### Why Templates Are Useful

* Reduce syntax errors
* Follow best practices
* Faster setup
* Easy to customize later

Most developers start with templates and **modify them gradually**.

---

## 12. What Changes Between JavaScript and Python?

| Aspect             | Same | Different |
| ------------------ | ---- | --------- |
| YAML structure     | ✅    | ❌         |
| Triggers           | ✅    | ❌         |
| Jobs & steps       | ✅    | ❌         |
| Runtime setup      | ❌    | ✅         |
| Command to execute | ❌    | ✅         |

Main takeaway:

> GitHub Actions is **language-independent**.

---



