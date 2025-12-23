To understand how Git tracks project changes, you must learn how files move through Git's **three core areas** and how commands like `add`, `status`, `commit`, `log`, and `diff` help you manage versions efficiently.

---

# **1. Git File Lifecycle — The 3-Area Model**

<image src="https://coding-platform.s3.amazonaws.com/dev/lms/tickets/07d42e41-6c25-4883-8b81-04fcc2c94420/UMQizQ3zQGscDIJV.png" width="500px">

<image src = "https://coding-platform.s3.amazonaws.com/dev/lms/tickets/a73fee3f-caa3-4940-a088-4c8b9ed67a4f/EYu3AONtxsf2yZtI.png" width="500px" >

Git manages files through **three logical locations**:

## **A. Working Directory (Workspace)**

This is your project folder on your machine.

Contains:

- New files
- Edited files
- Deleted files

Git **does NOT track** anything here until you stage it.

---

## **B. Staging Area (Index)**

Temporary holding area before committing.

Purpose:

- Prepare a clean snapshot
- Select _which_ files should go into the next commit
- Avoid committing unwanted changes

Files enter staging using:

```bash
git add <file>
```

---

## **C. Local Repository**

Stores **commits**, which are _permanent snapshots_ of your project.

Once committed:

- Changes become part of history
- A unique commit ID is generated
- You can revert or compare later

---

# **2. Checking the Current State — `git status`**

Use this command constantly.

```bash
git status
```

It tells you:

- Which files changed
- Which are staged
- Which are unstaged
- Whether your branch is ahead/behind

Example output:

```bash
Changes not staged for commit:
  modified: index.html

Changes to be committed:
  new file: style.css
```

---

# **3. Adding Files to Staging — `git add`**

### **Add a single file**

```bash
git add file.txt
```

### **Add multiple files**

```bash
git add file1.js file2.js
```

### **Add everything in the folder**

```bash
git add .
```

### **Add only modified files (not deleted/new)**

```bash
git add -u
```

Purpose of staging:

- Gives control
- Lets you commit only what you need
- Helps create clean, logical commits

---

# **4. Creating a Commit — `git commit`**

A **commit** is a permanent snapshot of staged changes.

### Basic commit:

```bash
git commit -m "Meaningful commit message"
```

### Commit messages MUST:

- Start with a verb → _Add, Update, Fix, Remove_
- Be short but descriptive
- Use present tense
- Avoid vague words like “changes”, “fixes”, “stuff”

### Examples of good messages:

- `Add navbar component`
- `Fix login validation issue`
- `Update README with setup instructions`

Bad examples:

- `done task`
- `changes made`
- `final commit`

---

# **5. Viewing Commit History — `git log`**

See full commit details:

```bash
git log
```

Shows:

- Commit ID
- Author
- Date
- Commit message

### Condensed view:

```bash
git log --oneline
```

Example:

```bash
a1b2c3d Add user login API
f4e5d6a Setup project structure
```

Perfect for quick history checks.

---

# **6. Comparing Changes — `git diff`**

Git provides powerful comparison tools.

---

## **A. Compare working directory vs staging area**

```bash
git diff
```

Shows **unstaged** edits.

---

## **B. Compare staging area vs last commit**

```bash
git diff --staged
```

Shows what you’re _about to commit_.

---

## **C. Compare two commits**

```bash
git diff <commit1> <commit2>
```

---

## How to read diff output:

```bash
- lines removed
+ lines added
```

Diffs help you review before committing.

---

# **7. Full Workflow Example**

### Step-by-step:

1. Edit a file
2. Check status

   ```bash
   git status
   ```

3. Stage it

   ```bash
   git add app.js
   ```

4. Review staged changes

   ```bash
   git diff --staged
   ```

5. Commit it

   ```bash
   git commit -m "Add route handler for login"
   ```

6. View commit history

   ```bash
   git log --oneline
   ```

---

# **8. Summary Table**

| Area / Command        | Purpose                         | When to Use                  |
| --------------------- | ------------------------------- | ---------------------------- |
| **Working Directory** | Where edits happen              | Anytime you modify files     |
| **Staging Area**      | Prepare changes for commit      | When changes are ready       |
| **Repository**        | Permanent version history       | After commit                 |
| `git status`          | View current file states        | Frequently                   |
| `git add`             | Move changes to staging         | Before committing            |
| `git commit`          | Save staged changes permanently | After reviewing              |
| `git log`             | See history                     | After commits                |
| `git diff`            | Compare changes                 | Before staging or committing |

---
