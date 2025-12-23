## 1. **Set Context — Where This Topic Fits (3 minutes)**

- “Open the same GitHub repository we’ve been using till now.”
- “Keep the **Actions tab** visible but don’t click yet.”

**Say clearly:**

> “Up to now, we have focused on **planning and collaboration**:
>
> - Issues plan the work
> - Boards track progress
> - Commits and PRs track code changes
> - CI/CD explained _why_ automation is needed”

Pause and ask:

> “But how do we actually **run code automatically** when someone pushes changes?”

---

**Transition statement (important):**

> “This is where **GitHub Actions** comes into the picture.
> GitHub Actions allows us to **execute code automatically and see results**, every time code changes.”

---

## 2. **What is GitHub Actions? (Conceptual – 4 minutes)**

Before showing any code:

> “GitHub Actions is GitHub’s **built-in automation engine**.”

Explain what it can do:

- Run programs
- Execute logic
- Print output
- Detect failures
- Remove manual checking

---

**Very important clarification (say slowly):**

> “GitHub Actions does **not** understand JavaScript or Python.
> It only runs the **commands we give it**.”

> “Think of it as a robot that follows instructions exactly.”

---

## 3. **Understanding YAML — Only What We Need (4 minutes)**

### Show a Small YAML Snippet

```yaml
name: Sample Workflow
on: push
jobs:
  demo-job:
    runs-on: ubuntu-latest
```

**Explain verbally:**

- YAML is a configuration language
- Indentation is critical
- No logic, only structure

Say clearly:

> “You do NOT need to master YAML.
> You only need to recognize the structure.”

---

## 4. **Anatomy of a GitHub Actions Workflow (4 minutes)**

Explain the three building blocks:

### Trigger (`on`)

> “Decides **when** automation runs”

### Job

> “Decides **where** it runs (machine & OS)”

### Steps

> “Decides **what commands** are executed”

---

**Mental model (say this):**

```
Event → Job → Steps → Console Output
```

---

## 5. **Workflow Triggers — Critical Concept (5 minutes)**

### Explain the Rule First

> “In real projects, automation should run
> **only when code reaches important branches**.”

---

### Show Trigger Example

```yaml
on:
  push:
    branches:
      - main
```

Explain:

- Push to `main` → workflow runs
- Push to feature branch → workflow does not run

---

### Pull Request Trigger (Explain Why)

```yaml
on:
  pull_request:
    branches:
      - main
```

Say clearly:

> “This ensures checks run **before merge**, not after damage is done.”

---

## 6. **Where GitHub Actions Files Live (2 minutes)**

State firmly:

> “GitHub Actions works only if files are placed correctly.”

Show path:

```
.github/
  workflows/
    ci.yml
```

Warn students:

- Wrong folder → no workflow
- Wrong extension → no workflow

---

## 7. **DEMO PATH SELECTION (Instructor Note – 1 minute)**

Say explicitly to the class:

> “Now I’ll demonstrate GitHub Actions using **ONE language**.
>
> - If this is a **Frontend / JS batch**, follow the **JavaScript demo**
> - If this is a **Backend / Python batch**, follow the **Python demo**”

> “The **concept and YAML structure remain identical**.”

---

# 🔹 DEMO OPTION A — JavaScript (Frontend / Fullstack Batches)

## 8A. **JavaScript Example — Custom Logic Demo (10 minutes)**

### **Explain the Goal**

> “We’ll write a simple program,
> run it automatically using GitHub Actions,
> and view output in logs.”

---

### **Project Structure (Show in Repo)**

```
src/
  palindrome.js
  test.js
```

Explain briefly what palindrome means.

---

### **Explain Code (Do Not Over-Explain)**

- `palindrome.js` → logic
- `test.js` → calls logic + prints output

Emphasize:

> “No frameworks.
> Just logic + console output.”

---

### **Explain Workflow YAML (Key Steps Only)**

```yaml
- Checkout code
- Setup Node.js
- Run node src/test.js
```

Say clearly:

> “GitHub Actions just runs `node src/test.js`
> exactly like your local terminal.”

---

### **Trigger the Workflow**

- Commit & push to `main`
- Go to **Actions tab**
- Open workflow run
- Expand logs

Say:

> “Every `console.log` appears here.
> This is how we debug automation.”

---

# 🔹 DEMO OPTION B — Python (Backend / Data Batches)

## 8B. **Python Example — Custom Logic Demo (10 minutes)**

### **Project Structure**

```
src/
  palindrome.py
  test.py
```

---

### **Explain the Logic Briefly**

- `palindrome.py` → function
- `test.py` → runs multiple cases

Say:

> “This is plain Python.
> No unittest, no pytest — just clarity.”

---

### **Explain Workflow YAML Differences**

Highlight only what changes:

```yaml
- Setup Python
- Run python src/test.py
```

Say clearly:

> “Same structure.
> Only runtime and command changed.”

---

### **Run & Show Logs**

- Push to `main`
- Open **Actions**
- View output

Say:

> “This output is your **CI console**.”

---

## 9. **Viewing Workflow Runs & Logs (4 minutes)**

### Walk Through Slowly

1. Repository → Actions
2. Select workflow
3. Click job
4. Expand steps

Explain:

> “This is how developers debug pipelines in real companies.”

---

## 10. **Generic CI Workflow Template (4 minutes)**

Show this and explain:

```yaml
name: CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build-and-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Run logic here"
```

Key statement (very important):

> “This structure stays the SAME for all languages.
> Only the commands change.”

---

## 11. **Using GitHub Actions Templates (5 minutes)**

### Demonstrate Live (UI-based)

- Actions tab
- Choose suggested template
- Click **Configure**
- Commit file

Say clearly:

> “Templates save time and prevent syntax errors.”

---

### Why Templates Matter

- Best practices
- Faster setup
- Beginner-friendly

---

## 12. **JS vs Python — What Actually Changes? (3 minutes)**

Explain the table verbally:

- YAML structure → same
- Triggers → same
- Jobs → same
- Runtime setup → different
- Command → different

---


