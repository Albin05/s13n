## 1. Why Secrets & Environment Variables Are Needed

In real-world software projects, applications rarely run with **hardcoded values**.
They usually depend on configuration such as:

- API keys
- Database URLs
- Tokens
- Environment flags (dev, staging, prod)

If such values are written directly inside:

- Source code
- GitHub Actions YAML files

they become:

- Visible to everyone
- Accidentally committed
- A serious security risk

To solve this, GitHub provides **Environment Variables** and **Secrets**, which allow us to:

- Keep configuration outside the code
- Secure sensitive values
- Change behavior without modifying source files

---

## 2. Environment Variables vs Secrets (Very Important Difference)

Although they look similar, **they serve different purposes**.

### Environment Variables

- Used for **non-sensitive configuration**
- Can be safely visible in logs
- Control how the application behaves

Examples:

- `APP_ENV=development`
- `LOG_LEVEL=debug`
- `FEATURE_X_ENABLED=true`

---

### Secrets

- Used for **sensitive data**
- Encrypted by GitHub
- Automatically **masked in logs**
- Never printed in plain text

Examples:

- `API_KEY`
- `DATABASE_PASSWORD`
- `ACCESS_TOKEN`

---

### Quick Comparison

| Aspect       | Environment Variable      | Secret                   |
| ------------ | ------------------------- | ------------------------ |
| Purpose      | Configuration             | Security                 |
| Visibility   | Can appear in logs        | Masked in logs           |
| Stored where | Workflow/YAML or Settings | GitHub encrypted storage |
| Use case     | App behavior              | Credentials              |

👉 **Rule of thumb**:
If leaking the value is dangerous → use **Secret**
Otherwise → use **Environment Variable**

---

## 3. Where Secrets & Variables Fit in CI/CD

Secrets and environment variables are used **during workflow execution**, not during coding.

They allow:

- Same code to run in different environments
- CI pipelines to stay secure
- Configuration changes without new commits

This is a **core professional CI/CD concept**.

---

## 4. Adding Environment Variables in GitHub Actions

Environment variables can be defined at **three levels**.

---

### 4.1 Workflow-Level Environment Variables

Available to **all jobs and steps**.

```yaml
env:
  APP_ENV: development
  FEATURE_FLAG: true
```

---

### 4.2 Job-Level Environment Variables

Available only to a specific job.

```yaml
jobs:
  run-job:
    runs-on: ubuntu-latest
    env:
      APP_ENV: staging
```

---

### 4.3 Step-Level Environment Variables

Available only inside one step.

```yaml
- name: Print environment
  run: echo "Environment is $APP_ENV"
  env:
    APP_ENV: production
```

---

## 5. How to Add Secrets in GitHub Repository

Secrets are added **through the GitHub UI**, not in code.

### Steps to Add a Repository Secret

1. Open your **GitHub repository**
2. Go to **Settings**
3. Click **Secrets and variables → Actions**
4. Under **Secrets**, click **New repository secret**
5. Enter:

   - **Name**: `DUMMY_API_KEY`
   - **Value**: `my-secret-key-123`

6. Click **Save**

Once saved, the secret is available to all workflows.

---

## 6. Using Environment Variables & Secrets in Workflows

### Example Workflow Snippet

```yaml
name: Env and Secrets Demo

on:
  push:
    branches:
      - main

jobs:
  demo:
    runs-on: ubuntu-latest

    env:
      APP_ENV: development

    steps:
      - name: Use environment variable
        run: echo "App Environment: $APP_ENV"

      - name: Use secret
        env:
          API_KEY: ${{ secrets.DUMMY_API_KEY }}
        run: echo "API key is configured"
```

📌 Note:

- The actual secret value is **never printed**
- GitHub replaces it with `***` if accidentally logged

---

## 7. Accessing Environment Variables & Secrets in JavaScript

### JavaScript Example

```js
console.log("Environment:", process.env.APP_ENV);
console.log("API Key exists:", process.env.DUMMY_API_KEY !== undefined);
```

Use case:

- Confirm the variable exists
- Never print the secret value itself

---

## 8. Accessing Environment Variables & Secrets in Python

### Python Example

```python
import os

print("Environment:", os.getenv("APP_ENV"))
print("API Key exists:", os.getenv("DUMMY_API_KEY") is not None)
```

This confirms correct configuration without exposing sensitive data.

---

## 9. Practical End-to-End Example (JS)

```yaml
name: JS Env Secret Demo

on:
  push:
    branches:
      - main

jobs:
  js-job:
    runs-on: ubuntu-latest

    env:
      APP_ENV: development

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 18

      - name: Run script
        env:
          DUMMY_API_KEY: ${{ secrets.DUMMY_API_KEY }}
        run: node src/test.js
```

Console output will show:

- Environment value
- Confirmation that secret exists
- Secret value masked

---

## 10. Practical End-to-End Example (Python)

```yaml
name: Python Env Secret Demo

on:
  push:
    branches:
      - main

jobs:
  python-job:
    runs-on: ubuntu-latest

    env:
      APP_ENV: development

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Run script
        env:
          DUMMY_API_KEY: ${{ secrets.DUMMY_API_KEY }}
        run: python src/test.py
```

---

## 11. Rerunning GitHub Actions After Adding Secrets or Variables

A very common beginner confusion is:

> “I added a secret, but the workflow already failed. What now?”

### Important Rule

GitHub Actions **does not automatically rerun workflows** when secrets or variables are added.

You must **rerun the job manually**.

---

### How to Rerun a Workflow

1. Go to **Actions** tab
2. Click the failed workflow run
3. Click **Re-run jobs**
4. Choose:

   - Re-run all jobs
   - Re-run failed jobs

The workflow will now run with the **new secrets and variables**.

---

## 12. Common Mistakes to Avoid

- ❌ Hardcoding secrets in code
- ❌ Printing secret values in logs
- ❌ Committing `.env` files
- ❌ Forgetting to rerun workflows after adding secrets
- ❌ Using secrets for non-sensitive config

---

## 13. Security Best Practices (Must Remember)

- Always assume CI logs are public
- Never expose secrets in `echo` or `print`
- Use environment variables for configuration
- Use secrets only for sensitive data
- Rotate secrets if compromised

These practices are **mandatory in professional environments**.

---
