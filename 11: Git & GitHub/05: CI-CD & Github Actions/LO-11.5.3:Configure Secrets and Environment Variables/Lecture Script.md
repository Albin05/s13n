## 1. **Set Context — Why This Topic Matters (3 minutes)**

- “Open the same GitHub repository we’ve been using.”
- “Keep the **Actions** tab and **Settings** tab visible.”

**Say clearly:**

> “So far, we have automated **running code** using GitHub Actions.”

> “But real applications don’t run with hardcoded values.”

Pause and ask the class:

> “Where do API keys, database passwords, and tokens come from?”

---

**State the problem firmly:**

> “If we put sensitive values directly in:
>
> - source code
> - YAML workflow files

> they become **visible, permanent, and dangerous**.”

---

**Transition statement (important):**

> “To solve this, GitHub gives us **Environment Variables** and **Secrets**.”

---

## 2. **Why Secrets & Environment Variables Are Needed (4 minutes)**

Explain with real-world examples:

- API keys
- DB URLs
- Tokens
- Environment flags

Say clearly:

> “Configuration must live **outside the code**.”

Explain benefits:

- Safer repositories
- Same code, different environments
- No risky commits

---

## 3. **Environment Variables vs Secrets — Critical Distinction (5 minutes)**

### Explain Before Showing Any UI

> “These two look similar, but they solve **different problems**.”

---

### **Environment Variables**

Explain slowly:

- Non-sensitive
- Control behavior
- Can appear in logs

Examples (say aloud):

- `APP_ENV=development`
- `FEATURE_FLAG=true`

---

### **Secrets**

Explain firmly:

- Sensitive
- Encrypted by GitHub
- Automatically masked in logs

Examples:

- API keys
- Passwords
- Tokens

---

### **Rule of Thumb (Say This Clearly)**

> “If leaking the value is dangerous → **Secret**
> Otherwise → **Environment Variable**”

---

## 4. **Where Secrets & Variables Fit in CI/CD (3 minutes)**

Explain conceptually:

> “Secrets and environment variables are injected
> **at runtime**, not during coding.”

They allow:

- Secure pipelines
- Configurable behavior
- No code changes for config updates

---

## 5. **Environment Variables in GitHub Actions — 3 Levels (6 minutes)**

### **Explain the Idea First**

> “Environment variables can exist at different scopes.”

---

### **5.1 Workflow-Level Variables**

Show snippet and explain:

```yaml
env:
  APP_ENV: development
```

> “Available everywhere.”

---

### **5.2 Job-Level Variables**

```yaml
jobs:
  demo:
    env:
      APP_ENV: staging
```

> “Only inside this job.”

---

### **5.3 Step-Level Variables**

```yaml
- name: Print env
  env:
    APP_ENV: production
  run: echo "Env is $APP_ENV"
```

> “Most specific scope.”

---

## 6. **Adding Secrets in GitHub UI (Live Demo – 6 minutes)**

### **Do This Slowly on Screen**

1. Repository → **Settings**
2. **Secrets and variables**
3. **Actions**
4. Click **New repository secret**

Fill in live:

- Name: `DUMMY_API_KEY`
- Value: `my-secret-key-123`

Click **Save**.

---

**Say clearly:**

> “Secrets are **never written in code**.
> They live only in GitHub’s encrypted storage.”

---

## 7. **Using Environment Variables & Secrets in Workflows (5 minutes)**

### **Show Workflow Snippet**

```yaml
env:
  APP_ENV: development
```

Explain:

> “This is safe configuration.”

---

### **Using Secrets**

```yaml
env:
  API_KEY: ${{ secrets.DUMMY_API_KEY }}
```

Say firmly:

> “This is the **only correct way** to use secrets.”

---

📌 Important emphasis:

> “Even if you try to print a secret,
> GitHub will mask it as `***`.”

---

## 8. **DEMO PATH SELECTION (Instructor Callout – 1 minute)**

Say clearly to students:

> “Now I’ll show how code **reads these values**.
>
> - JS / Frontend batch → JavaScript demo
> - Python / Backend batch → Python demo”

> “The idea is identical. Only syntax changes.”

---

# 🔹 DEMO OPTION A — JavaScript

## 9A. **Accessing Env & Secrets in JavaScript (6 minutes)**

Show code:

```js
console.log("Environment:", process.env.APP_ENV);
console.log("API Key exists:", process.env.DUMMY_API_KEY !== undefined);
```

Explain:

- `process.env` is Node’s environment map
- Never print the actual secret

Say clearly:

> “We check **existence**, not value.”

---

# 🔹 DEMO OPTION B — Python

## 9B. **Accessing Env & Secrets in Python (6 minutes)**

Show code:

```python
import os

print("Environment:", os.getenv("APP_ENV"))
print("API Key exists:", os.getenv("DUMMY_API_KEY") is not None)
```

Explain:

- `os.getenv()` safely reads variables
- Same rule: never print secrets

---

## 10. **End-to-End GitHub Actions Demo (JS or Python) (6 minutes)**

### Explain Before Running

> “Now we’ll run the workflow and see:
>
> - environment value printed
> - secret safely masked”

---

### Trigger Workflow

- Commit & push
- Open **Actions**
- Open workflow run
- Expand logs

Point out:

- Environment printed normally
- Secret never revealed

---

## 11. **Rerunning Workflows After Adding Secrets (4 minutes)**

### Address Common Confusion

> “Adding secrets does **not** rerun old workflows.”

---

### Show How to Rerun

1. Actions tab
2. Failed workflow
3. **Re-run jobs**

Say clearly:

> “This is one of the most common beginner mistakes.”

---

## 12. **Common Mistakes to Avoid (3 minutes)**

Read and explain briefly:

- Hardcoding secrets ❌
- Printing secrets ❌
- Committing `.env` files ❌
- Forgetting reruns ❌
- Using secrets for normal config ❌

---

## 13. **Security Best Practices (Final Emphasis – 3 minutes)**

Say firmly (slow pace):

> “Always assume CI logs are public.”

> “Secrets are powerful — treat them carefully.”

> “These rules are **mandatory in professional teams**.”

---
