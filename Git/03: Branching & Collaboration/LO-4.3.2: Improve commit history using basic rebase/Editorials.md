# **Q4. Why does rebase generate new commit IDs, and why does this matter?**

### **1. Title**

Commit ID Changes During Rebase

### **2. Problem Description**

Explain why commit hashes change after a rebase operation and why this behavior is significant.

### **3. Objective**

Understand how rebase rewrites history and its implications in collaborative workflows.

### **4. Hint**

Think about what happens to commits when they are “replayed”.

### **5. Short Explanation**

Rebase creates new commit IDs because it reapplies commits on a new base, effectively creating new commits.

### **6. Detailed Explanation**

In Git, a commit ID (hash) is generated based on the commit’s content **and its parent commit**.
During a rebase, Git temporarily removes the feature branch commits, updates the branch to point to a new base (usually the latest `main`), and then reapplies those commits one by one.

Because the parent commit changes, Git generates **new commit IDs**, even if the code changes look identical.
This matters because rewriting commit history can cause problems if the branch has already been shared with others.

### **7. Constraints / Edge Cases (optional)**

Rebasing shared or already-pushed branches can lead to conflicts and duplicated commits for collaborators.

---

# **Q5. In what real-world scenario is rebase safer and more appropriate than merge?**

### **1. Title**

Choosing Rebase Over Merge in Practice

### **2. Problem Description**

Identify a practical situation where rebase is a better choice than merge.

### **3. Objective**

Understand the intended and safe use cases of rebase in real projects.

### **4. Hint**

Focus on keeping history clean before integrating changes.

### **5. Short Explanation**

Rebase is safest when updating a personal feature branch with the latest changes from `main` before merging.

### **6. Detailed Explanation**

A common real-world scenario is when a developer works on a feature branch while `main` continues to evolve.
Before opening a Pull Request, the developer wants their branch to be based on the latest `main`.

Using rebase:

- Updates the feature branch cleanly
- Avoids unnecessary merge commits
- Results in a linear, readable history

This is safe because the branch is still private and owned by a single developer.

### **7. Constraints / Edge Cases (optional)**

Rebase should be avoided on shared branches or after the branch has been pushed and used by others.

---

# **Q6. Rebase a Feature Branch onto Main (No Conflicts)**

### **1. Title**

Basic Rebase Workflow Without Conflicts

### **2. Problem Description**

Perform a clean rebase of a feature branch onto the latest `main` branch.

### **3. Objective**

Practice rebasing to maintain a linear commit history.

### **4. Hint**

Ensure commits on the feature branch do not overlap with changes on `main`.

### **5. Short Explanation**

Rebase reapplies feature branch commits on top of the updated `main` branch.

### **6. Detailed Explanation**

```bash
# Create repository
mkdir rebase-demo
cd rebase-demo
git init

# Initial commit on main
echo "Base content" > app.txt
git add app.txt
git commit -m "Initial commit on main"

# Create feature branch
git checkout -b feature-login
echo "Login feature" >> app.txt
git add app.txt
git commit -m "Add login feature"

# Update main branch
git checkout main
echo "Main branch update" >> app.txt
git add app.txt
git commit -m "Update app on main"

# Rebase feature branch onto main
git checkout feature-login
git rebase main
```

After this, the commit history becomes linear, and the feature branch appears as if it started from the latest `main`.

### **7. Constraints / Edge Cases (optional)**

If changes overlap, conflicts may occur and must be resolved before continuing.

---

# **Q7. Handle a Rebase Conflict**

### **1. Title**

Resolving Conflicts During Rebase

### **2. Problem Description**

Create and resolve a conflict while rebasing a feature branch.

### **3. Objective**

Develop confidence in handling rebase conflicts and recovery commands.

### **4. Hint**

Conflicts arise when the same lines are modified differently in two branches.

### **5. Short Explanation**

During rebase, Git pauses when conflicts occur and requires manual resolution.

### **6. Detailed Explanation**

```bash
# Create conflict scenario
git checkout -b feature-ui
echo "Conflicting change" > app.txt
git add app.txt
git commit -m "UI update"

git checkout main
echo "Different main change" > app.txt
git add app.txt
git commit -m "Main update"

# Start rebase
git checkout feature-ui
git rebase main
```

When a conflict occurs:

1. Git pauses and marks conflicted files
2. Open the file and remove conflict markers
3. Decide the correct final content
4. Stage the resolved file

   ```bash
   git add app.txt
   ```

5. Continue the rebase

   ```bash
   git rebase --continue
   ```

To cancel the rebase:

```bash
git rebase --abort
```

### **7. Constraints / Edge Cases (optional)**

Incorrect conflict resolution can silently introduce bugs; testing after rebase is essential.
