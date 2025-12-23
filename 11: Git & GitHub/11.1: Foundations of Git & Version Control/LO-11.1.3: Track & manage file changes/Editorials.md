## **Q1. Purpose of the Staging Area in Git**

### **Problem Description**

When files are modified in a project, not all changes may be ready to be permanently saved in version history.

### **Objective**

Explain why Git introduces a staging area between working files and commits.

### **Hint**

Think about control, review, and selective commits.

### **Short Explanation**

The staging area allows developers to select and review changes before committing them.

### **Detailed Explanation**

In **Git**, the staging area acts as a buffer between the working directory and the commit history. It lets developers decide exactly which changes should be included in the next commit. This helps create clean, meaningful commits and avoids accidentally committing incomplete or unrelated changes.

### **Constraints / Edge Cases (Optional)**

- Files not added to the staging area will not be committed
- Using `git add .` may stage unintended changes

---

## **Q2. Difference between `git diff` and `git diff --staged`**

### **Problem Description**

Developers often need to inspect changes at different stages of the Git workflow.

### **Objective**

Differentiate between unstaged changes and staged changes.

### **Hint**

One compares working directory changes, the other compares staged changes.

### **Short Explanation**

`git diff` shows unstaged changes, while `git diff --staged` shows staged changes.

### **Detailed Explanation**

`git diff` displays the differences between the **working directory** and the **staging area**, helping developers see what has been modified but not yet staged.
`git diff --staged` (or `git diff --cached`) shows the differences between the **staging area** and the **last commit**, allowing developers to review exactly what will be committed next.

### **Constraints / Edge Cases (Optional)**

- If nothing is staged, `git diff --staged` produces no output
- These commands do not show already committed changes

---

## **Q3. Committing Changes from Only `index.html`**

### **Problem Description**

Sometimes developers need to commit changes from only one file while leaving other changes uncommitted.

### **Objective**

Demonstrate selective staging and committing in Git.

### **Hint**

Stage only the required file.

### **Short Explanation**

Git allows committing changes from specific files only.

### **Detailed Explanation**

**Commands:**

```bash
git status
git add index.html
git diff --staged
git commit -m "Update homepage layout"
```

This sequence ensures that only `index.html` is staged and committed, while changes in `style.css` remain in the working directory.

### **Constraints / Edge Cases (Optional)**

- Forgetting `git add index.html` results in no changes committed
- Using `git add .` would stage both files

---

## **Q4. Checking Difference Between Two Commits**

### **Problem Description**

Developers may need to compare how the code changed between two specific points in history.

### **Objective**

Show how to compare two commits directly.

### **Hint**

Use commit hashes with the diff command.

### **Short Explanation**

Git can compare any two commits using their IDs.

### **Detailed Explanation**

**Command:**

```bash
git diff a1b2c3d f4e5d6a
```

This command shows all differences between the two specified commits, regardless of their order.

### **Constraints / Edge Cases (Optional)**

- Commit hashes must be valid and unique
- Large diffs may be difficult to read

---

## **Q5. Viewing Compact One-Line Commit History**

### **Problem Description**

Full commit logs can be long and difficult to scan quickly.

### **Objective**

Display a concise summary of commit history.

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

Each line contains a short commit hash and its commit message.

### **Constraints / Edge Cases (Optional)**

- Does not show author or timestamp
- Best for quick overviews

---

## **Q6. Complete Git Workflow: Creating Files and Making Commits**

### **Problem Description**

Understanding Git requires hands-on practice with the complete workflow.

### **Objective**

Demonstrate folder creation, file creation, staging, and committing.

### **Hint**

Follow the standard Git lifecycle step by step.

### **Short Explanation**

This task demonstrates a full Git workflow from initialization to multiple commits.

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

Git allows comparisons at different stages of development and history.

### **Objective**

Use appropriate Git commands to compare changes.

### **Hint**

Each comparison uses a different Git command.

### **Short Explanation**

Different Git commands compare changes at different workflow stages.

### **Detailed Explanation**

```bash
git diff
git diff --staged
git diff <initial_commit_hash> <second_commit_hash>
git log --oneline
```

- `git diff` → working directory vs staging area
- `git diff --staged` → staging area vs last commit
- `git diff commit1 commit2` → compare two commits
- `git log --oneline` → compact commit history

### **Constraints / Edge Cases (Optional)**

- Commit hashes must be accurate
- Large diffs may require paging

---
