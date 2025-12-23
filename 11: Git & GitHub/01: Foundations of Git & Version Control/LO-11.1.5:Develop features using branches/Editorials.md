# **Q4. What is meant by “isolated development” when using Git branches?**

### **1. Title**

Isolated Development Using Git Branches

### **2. Problem Description**

Explain the concept of isolated development and how branches enable it in Git.

### **3. Objective**

Understand how branches separate work streams and protect the stability of the main branch.

### **4. Hint**

Think about working on features or fixes without impacting production-ready code.

### **5. Short Explanation**

Isolated development means working on changes in a separate branch so that unfinished or risky code does not affect the stable codebase.

### **6. Detailed Explanation**

In Git, each branch represents an independent line of development.
When developers create a new branch (for example, a feature or bugfix branch), all commits made in that branch are isolated from the `main` branch.

This allows:

- Feature development without breaking stable code
- Bug fixes without blocking other work
- Experiments without risk

Only when the work is complete and verified is it merged back into `main`.

### **7. Constraints / Edge Cases (optional)**

Isolation exists only until a merge happens; poor merge practices can still introduce issues.

---

# **Q5. Why is branch cleanup considered a best practice in Git?**

### **1. Title**

Importance of Branch Cleanup

### **2. Problem Description**

Explain why unused or merged branches should be deleted regularly.

### **3. Objective**

Understand repository hygiene and long-term maintainability.

### **4. Hint**

Think about readability and confusion in large projects.

### **5. Short Explanation**

Branch cleanup prevents clutter and ensures developers work only with relevant branches.

### **6. Detailed Explanation**

Over time, repositories can accumulate many branches that are no longer needed.
If these branches are not deleted:

- Developers may accidentally work on outdated branches
- Branch lists become confusing
- Repository maintenance becomes harder

Deleting merged or unused branches keeps the repository clean, readable, and professional.

### **7. Constraints / Edge Cases (optional)**

Never delete active or unmerged branches unless absolutely certain they are no longer required.

---

# **Q6. Create a project and work using branches**

### **1. Title**

Creating and Using a Feature Branch

### **2. Problem Description**

Perform a complete workflow involving project setup, committing to `main`, creating a feature branch, and committing changes in isolation.

### **3. Objective**

Practice real-world branch creation, switching, and isolated commits.

### **4. Hint**

Follow the sequence: initialize → commit → branch → switch → commit.

### **5. Short Explanation**

You initialize a project, make an initial commit on `main`, then create a feature branch and commit changes separately.

### **6. Detailed Explanation**

```bash
# Create project folder and initialize Git
mkdir branch-demo
cd branch-demo
git init

# Create file and commit on main
echo "Initial content" > app.txt
git add app.txt
git commit -m "Initial commit on main"

# Create and switch to feature branch
git branch feature-update
git switch feature-update

# Modify file and commit in feature branch
echo "Feature update content" >> app.txt
git add app.txt
git commit -m "Update app.txt in feature branch"

# Switch back to main
git switch main
```

This workflow demonstrates how changes in `feature-update` remain isolated from `main`.

### **7. Constraints / Edge Cases (optional)**

Switching branches with uncommitted changes may be blocked unless changes are committed or stashed.

---

# **Q7. Merge a feature branch and clean it up**

### **1. Title**

Merging a Branch and Performing Cleanup

### **2. Problem Description**

Merge a completed feature branch into `main` and delete it afterward.

### **3. Objective**

Understand the final stages of a branch lifecycle: merge and cleanup.

### **4. Hint**

Merging always happens into the currently checked-out branch.

### **5. Short Explanation**

You merge the feature branch into `main` and then delete it to keep the repository clean.

### **6. Detailed Explanation**

```bash
# Ensure you are on main
git switch main

# Merge the feature branch
git merge feature-update

# Delete the merged branch
git branch -d feature-update

# Verify remaining branches
git branch
```

After merging, the feature’s work becomes part of `main`, and deleting the branch prevents clutter.

### **7. Constraints / Edge Cases (optional)**

- If the branch is not fully merged, Git will block deletion unless `-D` is used.
- Merge conflicts may occur if the same files were changed differently.

---
