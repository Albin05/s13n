
To work confidently with Git, you must understand how to safely **undo mistakes** at different stages of the file lifecycle. Git provides commands to revert working directory changes, unstage staged changes, and modify the latest commit without losing control of your project history.

---

# **1. Undoing Working Directory Changes — `git restore`**


![Git Restore](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/a0520db6-384b-4a0e-baf9-7abc56bb0d7b/rRcGtpdhLbJIJfta.png)

The `git restore` command discards uncommitted edits and restores the file back to the version from the last commit.

---

## **A. Restore a single file**

```bash
git restore file.txt
```

### Example

You mistakenly edited `config.js` and want to revert to last committed version:

```bash
git restore config.js
```

This removes all your local (uncommitted) edits in that file.

---

## **B. Restore multiple files**

```bash
git restore file1.js file2.js
```

### Example

You modified multiple component files accidentally:

```bash
git restore Header.js Footer.js
```

---

## **C. Restore everything in the working directory**

```bash
git restore .
```

### Example

You want to discard all uncommitted changes across the project:

```bash
git restore .
```

This resets all files back to the previous commit.

---

### What this does

* Removes uncommitted edits
* Does not change staging area
* Returns file(s) to last committed state

### Use when:

* You made unintended or incorrect edits
* You want a clean working directory

---

# **2. Unstage Changes — `git reset` or `git restore --staged`**



Staged changes can be safely moved back to the working directory without deleting edits.

---

## **A. Unstage a single file using reset**

```bash
git reset file.txt
```

### Example

You accidentally staged a large log file:

```bash
git reset debug.log
```

The file remains modified but is no longer staged.

---

## **B. Unstage a single file using restore**

```bash
git restore --staged file.txt
```

### Example

You added `index.js` but want to remove it from staging:

```bash
git restore --staged index.js
```

Equivalent to `git reset index.js`.

---

## **C. Unstage everything**

```bash
git reset
```

### Example

You staged many files but want a clean slate again:

```bash
git reset
```

All files move back to working directory with edits intact.

---

### What this does

* Removes files from staging
* Does not delete modifications
* Lets you stage again selectively

---

# **3. Amending the Last Commit — `git commit --amend`**

Sometimes corrections are required after making a commit. Git allows modifying the most recent commit.

---

## **A. Change the last commit message**

```bash
git commit --amend -m "Correct message"
```

### Example

You wrote:

```bash
git commit -m "Addd login page"
```

Fix it:

```bash
git commit --amend -m "Add login page"
```

---

## **B. Add missing changes to the last commit**

Stage missing files:

```bash
git add styles.css
```

Then amend:

```bash
git commit --amend
```

### Example

You forgot to include `validation.js` in the latest commit:

```bash
git add validation.js
git commit --amend
```

The previous commit now includes this file.

---

### What this does

* Rewrites the last commit
* Updates commit message or contents
* Generates a new commit ID

### Important

* Safe only before pushing
* Avoid rewriting public/shared history

---

# **4. Understanding File Lifecycle When Undoing Changes**



Undo commands behave differently depending on the file’s position in Git’s lifecycle.

| Stage             | Action Type        | Correct Command                                         |
| ----------------- | ------------------ | ------------------------------------------------------- |
| Working Directory | Discard edits      | `git restore file.txt`                                  |
| Staging Area      | Unstage file       | `git restore --staged file.txt` or `git reset file.txt` |
| Repository        | Modify last commit | `git commit --amend`                                    |

---

# **5. Common Mistake Scenarios and Solutions**

## **A. “I made changes but want to discard them.”**

```bash
git restore file.txt
```

### Example

You accidentally removed important lines in `app.js`:

```bash
git restore app.js
```

---

## **B. “I added files by mistake.”**

```bash
git reset file.txt
```

### Example

You staged temporary backup files:

```bash
git reset backup-old.js
```

---

## **C. “I forgot to include something in the last commit.”**

```bash
git add missing.js
git commit --amend
```

### Example

You forgot to add test cases:

```bash
git add login.test.js
git commit --amend
```

---

## **D. “My commit message is incorrect.”**

```bash
git commit --amend -m "Refactor authentication module"
```

---

## **E. “I want to review my changes before undoing anything.”**

Working directory diff:

```bash
git diff
```

Staged diff:

```bash
git diff --staged
```

### Example

To check what you added before committing:

```bash
git diff --staged
```

---

# **6. Summary Table**

| Command                | Purpose                           | Stage Affected    |
| ---------------------- | --------------------------------- | ----------------- |
| `git restore file`     | Discard working directory changes | Working Directory |
| `git restore --staged` | Unstage changes                   | Staging Area      |
| `git reset file`       | Unstage changes (alternative)     | Staging Area      |
| `git commit --amend`   | Modify last commit                | Repository        |
| `git diff`             | View unstaged changes             | Working Directory |
| `git diff --staged`    | View staged snapshot              | Staging Area      |

---


