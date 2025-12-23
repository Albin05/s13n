## **Q1. When should you use `git restore --staged file.txt`?**

### **Problem Description**

Sometimes a file is accidentally staged, but you are not ready to commit it yet.

### **Objective**

Explain the correct scenario for using `git restore --staged`.

### **Hint**

Think about undoing staging, not deleting changes.

### **Short Explanation**

This command is used to remove a file from the staging area while keeping its changes.

### **Detailed Explanation**

`git restore --staged file.txt` is used when a file has been added to the staging area by mistake. It moves the file back to the working directory without discarding any edits. This is helpful when you want to reorganize commits or stage files selectively without losing work.

### **Constraints / Edge Cases (Optional)**

- Does not delete file changes
- Affects only the staging area, not commits

---

## **Q2. Why is it unsafe to use `git commit --amend` after pushing to a shared remote?**

### **Problem Description**

Developers may try to edit commit history even after sharing it with others.

### **Objective**

Explain the risk of amending pushed commits.

### **Hint**

Think about rewritten history and collaboration.

### **Short Explanation**

Amending a pushed commit rewrites history and can disrupt teammates’ work.

### **Detailed Explanation**

Using `git commit --amend` after pushing rewrites the commit hash, causing the local history to differ from the remote repository. Teammates who already pulled the original commit may face merge conflicts or broken histories. This can lead to confusion, forced resets, and loss of work, making amend unsafe in shared branches.

### **Constraints / Edge Cases (Optional)**

- Safe only on private or unshared branches
- Requires force push to update remote

---

## **Q3. Discard changes only in `nav.js`**

### **Problem Description**

You want to remove changes from one file while keeping edits in others.

### **Objective**

Discard changes selectively from a single file.

### **Hint**

Restore only the required file.

### **Short Explanation**

Git allows discarding changes from individual files.

### **Detailed Explanation**

**Command:**

```bash
git restore nav.js
```

This discards changes in `nav.js` and restores it to the last committed version, while keeping edits in `home.js` and `styles.css` intact.

### **Constraints / Edge Cases (Optional)**

- Changes in `nav.js` cannot be recovered unless stashed or committed
- Works only for uncommitted changes

---

## **Q4. Unstage all files after accidental `git add .`**

### **Problem Description**

All files were staged accidentally, but edits should be preserved.

### **Objective**

Remove all files from staging safely.

### **Hint**

Unstage everything at once.

### **Short Explanation**

You can unstage all files without deleting changes.

### **Detailed Explanation**

**Command:**

```bash
git restore --staged .
```

This removes all files from the staging area while keeping their modifications in the working directory.

### **Constraints / Edge Cases (Optional)**

- Does not affect committed files
- Safer than resetting hard

---

## **Q5. Workflow: Modify, Stage, Amend Commit Message, Add Missing File**

### **Problem Description**

A commit was made too early with a wrong message and missing file.

### **Objective**

Correct the last commit safely using amend.

### **Hint**

Stage files first, then amend.

### **Short Explanation**

`git commit --amend` updates the last commit.

### **Detailed Explanation**

**Commands (in order):**

```bash
# Modify dashboard.js
git add dashboard.js

# Add missing file
git add auth.js

# Amend commit message and include auth.js
git commit --amend -m "Update dashboard logic"
```

This updates the previous commit with the correct message and includes `auth.js`.

### **Constraints / Edge Cases (Optional)**

- Should not be used after pushing
- Only amends the most recent commit

---

## **Q6. Full Workflow: Create, Commit, Modify, Restore**

### **Problem Description**

A file was modified after committing, but changes need to be discarded.

### **Objective**

Restore a file to its last committed state.

### **Hint**

Use restore for working directory cleanup.

### **Short Explanation**

Git can revert files back to the last commit.

### **Detailed Explanation**

```bash
echo "console.log('Profile loaded');" > profile.js
git add profile.js
git commit -m "Add profile module"

# Modify the file
echo "console.log('Extra log');" >> profile.js

# Discard changes
git restore profile.js
```

This returns `profile.js` to the state of the last commit.

### **Constraints / Edge Cases (Optional)**

- Discarded changes cannot be recovered
- Does not affect commit history

---

## **Q7. Workflow with Unstage + Amend**

### **Problem Description**

A file was staged too early, edited again, and committed with a wrong message.

### **Objective**

Demonstrate unstage, recommit, and amend workflow.

### **Hint**

Unstage → edit → stage → commit → amend.

### **Short Explanation**

Git supports flexible correction before pushing.

### **Detailed Explanation**

```bash
echo "const settings = {};" > settings.js
git add settings.js

# Unstage to edit again
git restore --staged settings.js

# Make more edits
echo "settings.theme = 'dark';" >> settings.js

git add settings.js
git commit -m "Wrong message"

# Add missing file
echo "const defaults = {};" > defaults.js
git add defaults.js

# Amend commit
git commit --amend -m "Add settings file"
```

This results in a single corrected commit containing both files.

### **Constraints / Edge Cases (Optional)**

- Unsafe after pushing to shared branches
- Amend only affects the latest commit

---
