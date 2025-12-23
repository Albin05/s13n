# **Q4. What is the purpose of the Staging Area in Git?**

### **1. Title**

Purpose of the Staging Area (Index)

### **2. Problem Description**

Explain why Git uses a staging area instead of committing directly from the working directory.

### **3. Objective**

Understand how staging provides controlled, clean commits.

### **4. Hint**

Think of the staging area as a “pre-commit review zone.”

### **5. Short Explanation**

The staging area lets developers choose which changes go into the next commit, enabling clean and meaningful snapshots.

### **6. Detailed Explanation**

The Git staging area (index) is a temporary space where changes are prepared before being committed.
It allows the developer to:

* Select specific files for the commit
* Avoid committing unwanted edits
* Group related changes into logical commits
* Preview changes before making them permanent

This improves version control clarity and reduces commit noise.

### **7. Constraints / Edge Cases**

If nothing is staged, `git commit` will do nothing (unless using `-a`).

---

# **Q5. Explain the difference between `git diff` and `git diff --staged`.**

### **1. Title**

Comparing Working Directory, Staging Area, and Commits

### **2. Problem Description**

Distinguish between unstaged change comparison and staged change comparison.

### **3. Objective**

Understand how Git compares different areas.

### **4. Hint**

Ask yourself: "What am I comparing—unstaged or staged changes?"

### **5. Short Explanation**

* `git diff` → working directory vs staging area
* `git diff --staged` → staging area vs last commit

### **6. Detailed Explanation**

`git diff` shows what you’ve edited but **not** staged.
Example: You changed a file but did NOT run `git add`.

`git diff --staged` shows what is staged and ready for the next commit.
Example: After running `git add`, this command previews the commit contents.

### **7. Constraints / Edge Cases**

If nothing is staged, `git diff --staged` shows nothing.

---

# **Q6. Commit only changes from `index.html` while ignoring `style.css`**

### **1. Title**

Selective Staging and Committing

### **2. Problem Description**

Only one of the modified files should be committed.

### **3. Objective**

Practice staging specific files and making targeted commits.

### **4. Hint**

Use `git add` only on the file intended for commit.

### **5. Short Explanation**

You must stage only `index.html`, verify it, and commit it.

### **6. Detailed Explanation**

Steps:

1. **Check file states**

```bash
git status
```

This confirms which files were modified.

2. **Stage only index.html**

```bash
git add index.html
```

`style.css` remains unstaged.

3. **Review staged changes**

```bash
git diff --staged
```

Ensures only desired changes will be committed.

4. **Commit with proper message**

```bash
git commit -m "Update homepage layout"
```

This workflow reinforces selective and clean committing.

### **7. Constraints / Edge Cases**

If you accidentally added everything (`git add .`), you’d need to unstage files using:

```bash
git restore --staged <file>
```

---

# **Q7. Compare two commits (`a1b2c3d` and `f4e5d6a`)**

### **1. Title**

Comparing Commit Snapshots

### **2. Problem Description**

Find the command to see differences between two commits.

### **3. Objective**

Practice commit-level diff comparison.

### **4. Hint**

Use the diff command with two commit hashes.

### **5. Short Explanation**

`git diff <commit1> <commit2>` compares snapshots.

### **6. Detailed Explanation**

Git allows comparing any two commits directly:

```bash
git diff a1b2c3d f4e5d6a
```

This shows lines added, removed, or modified between those commits.

### **7. Constraints / Edge Cases**

Commit order matters: `git diff oldCommit newCommit` shows forward changes.

---

# **Q8. Show compact one-line commit history**

### **1. Title**

Viewing Condensed Commit Logs

### **2. Problem Description**

Identify the command to display a short history.

### **3. Objective**

Learn how to quickly inspect commit history.

### **4. Hint**

Think “log, but shorter.”

### **5. Short Explanation**

Use `git log --oneline`.

### **6. Detailed Explanation**

This command displays each commit in a single line:

```bash
git log --oneline
```

Sample output:

```
f4e5d6a Add utils.js and update app.js
a1b2c3d Add initial app.js file
```

This is widely used for debugging, reviews, and branching decisions.

### **7. Constraints / Edge Cases**

Shows only the local repository history unless combined with other flags.

---

# **Q9. Full Workflow: Folder creation → files → edits → staged commits**

### **1. Title**

End-to-End Git Workflow Practice

### **2. Problem Description**

Perform an entire Git workflow: creating files, staging, committing, and updating.

### **3. Objective**

Develop hands-on experience executing essential Git operations.

### **4. Hint**

Follow the sequence: create → initialize → add → commit → modify → commit.

### **5. Short Explanation**

You create two files, commit one, update both, and commit again.

### **6. Detailed Explanation**

**Commands:**

```bash
mkdir project-demo
cd project-demo

echo "console.log('Hello World');" > app.js

git init
git add app.js
git commit -m "Add initial app.js file"

echo "function sum(a,b){ return a+b }" > utils.js

echo "console.log('App updated');" >> app.js

git add .
git commit -m "Add utils.js and update app.js"
```

What this demonstrates:

* Initializing a repository
* Making initial commits
* Adding new files
* Updating existing files
* Making grouped commits

A complete real-life workflow.

### **7. Constraints / Edge Cases**

If you mistakenly overwrite files using `>`, use `>>` for appending.

---

# **Q10. Diff Analysis Across the Workflow**

### **1. Title**

Comparing Working Directory, Staged Changes, and Commits

### **2. Problem Description**

Identify commands to compare changes in different Git areas.

### **3. Objective**

Improve understanding of Git diff operations across the entire project lifecycle.

### **4. Hint**

Remember the three comparisons: WD → Staging, Staging → Commit, Commit → Commit.

### **5. Short Explanation**

Use:

* `git diff`
* `git diff --staged`
* `git diff <commit1> <commit2>`
* `git log --oneline`

### **6. Detailed Explanation**

1. **Working directory vs staging area**

```bash
git diff
```

2. **Staged changes vs last commit**

```bash
git diff --staged
```

3. **Compare initial commit and second commit**
   First get commit IDs:

```bash
git log --oneline
```

Then compare:

```bash
git diff <commit1> <commit2>
```

4. **View compact history**

```bash
git log --oneline
```

This gives a complete change-tracking overview.

### **7. Constraints / Edge Cases**

If no changes exist, diff commands return empty outputs.
