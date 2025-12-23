## **Q1. Purpose of the Staging Area in Git**

### **Problem Description**

When files are modified, not all changes may be ready to be saved permanently.

### **Objective**

Explain why Git uses a staging area between working directory and commit history.

### **Hint**

Think of selective commits and review before saving history.

### **Short Explanation**

The staging area allows developers to choose which changes should be included in the next commit.

### **Detailed Explanation**

The **staging area** in **Git** acts as an intermediate step between the working directory and the repository history. It enables developers to review, organize, and selectively add changes before committing. This prevents accidental commits and allows precise control over what gets recorded in the project history.

### **Constraints / Edge Cases (Optional)**

- Files not staged will not be committed
- Overusing `git add .` may stage unintended changes

---

## **Q2. Difference between `git diff` and `git diff --staged`**

### **Problem Description**

Developers often need to compare changes at different stages of the Git workflow.

### **Objective**

Differentiate between working directory changes and staged changes.

### **Hint**

One compares unstaged changes, the other staged changes.

### **Short Explanation**

`git diff` shows unstaged changes, while `git diff --staged` shows staged changes.

### **Detailed Explanation**

`git diff` displays differences between the **working directory** and the **staging area**, helping developers see what is modified but not yet staged.
`git diff --staged` (or `git diff --cached`) shows differences between the **staging area** and the **last commit**, allowing developers to review exactly what will be committed.

### **Constraints / Edge Cases (Optional)**

- If nothing is staged, `git diff --staged` shows no output
- Committed changes are not shown by either command

---

## **Q3. Committing Changes from Only One File**

### **Problem Description**

Sometimes only specific file changes should be committed.

### **Objective**

Demonstrate selective staging and committing.

### **Hint**

Stage only the required file.

### **Short Explanation**

Git allows committing changes from individual files selectively.

### **Detailed Explanation**

**Commands:**

```bash
git status
git add index.html
git diff --staged
git commit -m "Update homepage layout"
```

This workflow ensures that only `index.html` is staged and committed, while changes in `style.css` remain uncommitted.

### **Constraints / Edge Cases (Optional)**

- Forgetting to stage the file will result in no changes committed
- `git add .` would stage both files unintentionally

---

## **Q4. Checking Difference Between Two Commits**

### **Problem Description**

Developers may need to compare changes across different points in history.

### **Objective**

Show how to compare two commits directly.

### **Hint**

Use commit hashes with `git diff`.

### **Short Explanation**

Git allows comparison between any two commits using their IDs.

### **Detailed Explanation**

**Command:**

```bash
git diff a1b2c3d f4e5d6a
```

This command shows all differences between the two specified commits, regardless of their order in history.

### **Constraints / Edge Cases (Optional)**

- Large diffs may be difficult to read
- Short commit hashes must still be unique

---

## **Q5. Viewing Compact One-Line Commit History**

### **Problem Description**

Full commit logs can be lengthy and hard to scan quickly.

### **Objective**

Show how to view a concise commit history.

### **Hint**

Use a log option for compact output.

### **Short Explanation**

Git provides a one-line summary view of commits.

### **Detailed Explanation**

**Command:**

```bash
git log --oneline
```

**Expected Output Style:**

```
f4e5d6a Add utils.js and update app.js
a1b2c3d Add initial app.js file
```

Each line shows a short commit hash and commit message.

### **Constraints / Edge Cases (Optional)**

- Does not show author or timestamp
- Best used for quick overview

---

## **Q6. Complete Git Workflow: Folder, Files, Changes, and Commits**

### **Problem Description**

Understanding Git requires practicing the complete workflow from project creation to multiple commits.

### **Objective**

Demonstrate end-to-end Git usage.

### **Hint**

Follow the standard Git lifecycle.

### **Short Explanation**

This workflow covers initialization, staging, and committing multiple changes.

### **Detailed Explanation**

```bash
mkdir project-demo
cd project-demo

echo "console.log('Hello from app');" > app.js

git init
git add app.js
git commit -m "Add initial app.js file"

echo "console.log('Utility file');" > utils.js
echo "console.log('Another log');" >> app.js

git add app.js utils.js
git commit -m "Add utils.js and update app.js"
```

### **Constraints / Edge Cases (Optional)**

- Git must be initialized before staging
- Untracked files must be added explicitly

---

## **Q7. Comparing Changes Across the Git Workflow**

### **Problem Description**

Developers need to compare changes at different stages of Git history.

### **Objective**

Use appropriate diff and log commands for comparison.

### **Hint**

Each comparison uses a different Git command.

### **Short Explanation**

Git provides different diff commands for each workflow stage.

### **Detailed Explanation**

```bash
git diff
git diff --staged
git diff <initial_commit_hash> <second_commit_hash>
git log --oneline
```

- `git diff` → working directory vs staging
- `git diff --staged` → staging vs last commit
- `git diff commit1 commit2` → history comparison
- `git log --oneline` → compact history

### **Constraints / Edge Cases (Optional)**

- Commit hashes must be correct
- Large diffs may need paging tools

---
