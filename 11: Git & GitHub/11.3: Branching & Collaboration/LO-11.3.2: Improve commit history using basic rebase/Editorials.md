## **Q1. Why does rebase generate new commit IDs, and why does this matter?**

### **Problem Description**

Developers often notice that commit hashes change after performing a rebase.

### **Objective**

Explain why rebase creates new commit IDs and why this behavior is important.

### **Hint**

Think about history rewriting and commit metadata.

### **Short Explanation**

Rebase rewrites commit history, which results in new commit hashes.

### **Detailed Explanation**

In **Git**, each commit ID is generated based on its content and its parent commit. During a rebase, commits are replayed on top of a new base, changing their parent references. This causes Git to generate **new commit IDs**. This matters because rewriting history on shared branches can break collaboration, as other developers may already rely on the old commit history.

### **Constraints / Edge Cases (Optional)**

- Safe only on local or private branches
- Requires force push if already pushed

---

## **Q2. When is rebase safer and more appropriate than merge?**

### **Problem Description**

Teams must choose between merge and rebase when synchronizing branches.

### **Objective**

Identify a real-world scenario where rebase is the better choice.

### **Hint**

Think about keeping history clean before integration.

### **Short Explanation**

Rebase is safer when updating a feature branch with the latest main branch changes.

### **Detailed Explanation**

Rebase is most appropriate when a developer wants to **update their feature branch with the latest changes from `main`** before creating a Pull Request. Rebasing keeps the commit history linear and clean without introducing merge commits. Since the feature branch is typically private at this stage, rewriting history does not affect other collaborators.

### **Constraints / Edge Cases (Optional)**

- Should not be used on shared branches
- Conflicts may still occur during rebase

---

## **Q3. Rebase a Feature Branch onto Main (No Conflicts)**

### **Problem Description**

Feature branches can fall behind the main branch as new commits are added.

### **Objective**

Demonstrate how to rebase a feature branch onto main and verify linear history.

### **Hint**

Replay feature commits on top of the latest main branch.

### **Short Explanation**

Rebasing moves feature commits on top of the latest main branch.

### **Detailed Explanation**

```bash
mkdir rebase-demo
cd rebase-demo
git init

echo "Initial content" > app.txt
git add app.txt
git commit -m "Initial commit on main"

git switch -c feature-login
echo "Login feature work" >> app.txt
git add app.txt
git commit -m "Add login feature"

git switch main
echo "Main branch update" >> app.txt
git add app.txt
git commit -m "Update app on main"

git switch feature-login
git rebase main
git log --oneline --graph
```

After rebasing, the feature branch commits appear **after** the latest main commit, creating a clean, linear history.

### **Constraints / Edge Cases (Optional)**

- Conflicts may arise if files overlap
- Commit hashes will change after rebase

---

## **Q4. Handle a Rebase Conflict**

### **Problem Description**

Conflicts can occur when rebasing branches that modify the same lines.

### **Objective**

Demonstrate how to resolve or abort a rebase safely.

### **Hint**

Use rebase control commands to proceed or stop.

### **Short Explanation**

Rebase conflicts require manual resolution before continuing.

### **Detailed Explanation**

```bash
git switch -c feature-ui
echo "UI change" >> app.txt
git add app.txt
git commit -m "Update UI"

git switch main
echo "Conflicting main change" >> app.txt
git add app.txt
git commit -m "Main conflicting change"

git switch feature-ui
git rebase main

# Resolve conflict in app.txt manually
git add app.txt
git rebase --continue

# If you want to cancel rebase completely
git rebase --abort
```

During conflict resolution, conflict markers must be removed and the correct content finalized before continuing the rebase.

### **Constraints / Edge Cases (Optional)**

- Forgetting `git rebase --continue` will pause the process
- Aborting restores branch to pre-rebase state

---
