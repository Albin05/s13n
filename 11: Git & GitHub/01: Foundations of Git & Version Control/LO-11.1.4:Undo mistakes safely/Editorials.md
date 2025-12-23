# **Q3. When should you use `git restore --staged file.txt`?**

### **1. Title**

Unstaging a File Without Losing Edits

### **2. Problem Description**

Explain when it is appropriate to remove a file from the staging area using `git restore --staged`.

### **3. Objective**

Understand how to safely unstage changes without deleting modifications in the working directory.

### **4. Hint**

Think of situations where the file is staged but not yet ready to commit.

### **5. Short Explanation**

Use `git restore --staged file.txt` when a file is staged accidentally and you want to keep your edits but remove it from the staging area.

### **6. Detailed Explanation**

When you run `git add file.txt`, the file moves into the staging area.
If you realize that you staged it too early or want to modify it further before committing, you can remove it from staging using:

```bash
git restore --staged file.txt
```

This does **not** delete your changes. It only removes the file from staging so it returns to the working directory state.

### **7. Constraints / Edge Cases**

- Does not work on deleted files unless combined with additional flags.
- Will not discard edits—only unstages them.

---

# **Q4. Why is it unsafe to use `git commit --amend` after pushing?**

### **1. Title**

Risks of Amending a Published Commit

### **2. Problem Description**

Explain why using `git commit --amend` after pushing may create issues for other developers.

### **3. Objective**

Understand the dangers of rewriting public Git history.

### **4. Hint**

Consider what happens when commit IDs change on a shared remote.

### **5. Short Explanation**

Amending a pushed commit rewrites its commit ID, causing conflicts for collaborators who have already pulled the original version.

### **6. Detailed Explanation**

`git commit --amend` replaces the last commit with a new one, generating a new commit ID.
If that commit has already been pushed to a shared remote (e.g., GitHub), other teammates may still have the old commit in their history.
When they pull, their history will conflict with yours, causing errors and forcing manual resolution.

This disrupts collaborative workflows and can corrupt the shared history.

### **7. Constraints / Edge Cases**

- Safe only for **local commits** or commits in personal feature branches not yet shared.
- Avoid using on `main`, `master`, or any published branch.

---

# **Q5. Discard changes in only `nav.js`**

### **1. Title**

Restoring a Single File While Keeping Other Edits

### **2. Problem Description**

User wants to discard changes in one file (`nav.js`) but preserve work done in other files.

### **3. Objective**

Practice selective restoration of working directory changes.

### **4. Hint**

Use the restore command only on the file you want to revert.

### **5. Short Explanation**

Use `git restore nav.js` to revert that file to the last committed version.

### **6. Detailed Explanation**

Git lets you selectively discard uncommitted changes using:

```bash
git restore nav.js
```

This command restores only `nav.js` to its previous committed state, without affecting `home.js` or `styles.css`.
It is safe because it only affects the working directory and does not modify staged or committed history.

### **7. Constraints / Edge Cases**

- Only discards uncommitted edits.
- Cannot restore changes that were never committed unless using more advanced recovery commands.

---

# **Q6. Unstage all files without deleting edits**

### **1. Title**

Undoing Accidental Bulk Staging

### **2. Problem Description**

You staged many files accidentally using `git add .` and want to unstage all of them safely.

### **3. Objective**

Learn how to reset the staging area while keeping working directory changes.

### **4. Hint**

Use `git reset` without specifying a file.

### **5. Short Explanation**

Run `git reset` to move all staged files back to the working directory while preserving edits.

### **6. Detailed Explanation**

When all files are staged accidentally:

```bash
git add .
```

You can unstage everything using:

```bash
git reset
```

This command clears the staging area but does **not** discard your work.
All modified files remain edited in the working directory, ready for selective staging again.

### **7. Constraints / Edge Cases**

- Does not affect commit history.
- Does not delete or overwrite working directory edits.

---

# **Q7. Full Workflow Using Amend and Add**

### **1. Title**

Fixing a Commit Message and Adding Missing Files

### **2. Problem Description**

Perform a workflow where a file is modified, staged, committed incorrectly, and corrected with amendments.

### **3. Objective**

Practice commit message correction and adding missing files using `--amend`.

### **4. Hint**

Think in two parts:

1. Stage and commit
2. Amend message and add missing file

### **5. Short Explanation**

Amend updates the last commit, allowing correction of message and inclusion of missing files.

### **6. Detailed Explanation**

Full solution:

```bash
# 1. Modify dashboard.js
# (editing happens in the editor)

# 2. Stage the file
git add dashboard.js

# 3 & 4. Fix last commit message
git commit --amend -m "Update dashboard logic"

# 5. Add missing file and include it in the same commit
git add auth.js
git commit --amend
```

The commit ID is rewritten, but logically it becomes one corrected commit containing both files.

### **7. Constraints / Edge Cases**

- Unsafe on pushed commits.
- Amending rewrites commit history.

---

# **Q8. Create → Commit → Modify → Restore**

### **1. Title**

Creating a File, Committing It, Then Restoring Changes

### **2. Problem Description**

Perform a workflow involving creation, modification, and discarding edits using `git restore`.

### **3. Objective**

Understand how to roll back working directory changes safely.

### **4. Hint**

Use `git restore` on the file after modifying it.

### **5. Short Explanation**

You commit the file, modify it, then use restore to discard post-commit changes.

### **6. Detailed Explanation**

Commands:

```bash
# 1. Create file
echo "console.log('Profile loaded')" > profile.js

# 2. (Already added via echo)

# 3. Stage and commit
git add profile.js
git commit -m "Add profile module"

# 4. Modify the file
echo "console.log('Profile updated')" >> profile.js

# 5. Discard the new modifications
git restore profile.js
```

This returns the file to the exact state of the last commit.

### **7. Constraints / Edge Cases**

- Only discards uncommitted changes.
- Cannot recover overwritten changes unless using Git reflog.

---

# **Q9. Unstage → Edit → Commit → Amend Workflow**

### **1. Title**

Complete Workflow Demonstrating Unstaging and Amending

### **2. Problem Description**

Perform several actions: creating, staging, unstaging, editing, committing, and amending.

### **3. Objective**

Build confidence in correcting mistakes at both staging and commit levels.

### **4. Hint**

Use `git restore --staged` or `git reset` to unstage, and `git commit --amend` to fix commits.

### **5. Short Explanation**

You create a file, mistakenly stage it, unstage it, edit more, commit it, then amend message and include another file.

### **6. Detailed Explanation**

Full sequence:

```bash
# 1. Create file
echo "const settings = {};" > settings.js

# 2. Code added via echo

# 3. Stage file
git add settings.js

# 4. Unstage it
git restore --staged settings.js
# OR
git reset settings.js

# 5. Edit again
echo "settings.theme = 'dark';" >> settings.js

# 6. Stage and commit
git add settings.js
git commit -m "Initial commit message"

# 7. Fix commit message
git commit --amend -m "Add settings file"

# 8. Add missing file to same commit
echo "export const defaults = {};" > defaults.js
git add defaults.js
git commit --amend
```

This results in a single corrected commit containing both files.

### **7. Constraints / Edge Cases**

- Amending after pushing is dangerous.
- Unstaging does not delete changes.

---
