# **Q4. What is the purpose of setting an upstream branch using `git push -u`?**

### **1. Title**

Understanding Upstream Branch Configuration

### **2. Problem Description**

Explain why developers set an upstream branch and how it helps in daily Git workflows.

### **3. Objective**

Understand the relationship between a local branch and its corresponding remote branch.

### **4. Hint**

Think about why repeated `git push origin main` is inconvenient.

### **5. Short Explanation**

Setting an upstream branch links a local branch to a remote branch, allowing simpler push and pull commands.

### **6. Detailed Explanation**

When a branch is pushed for the first time using:

```bash
git push -u origin main
```

Git establishes a tracking relationship between the local branch (`main`) and the remote branch (`origin/main`).
After this linkage:

- `git push` knows where to send commits
- `git pull` knows where to fetch updates from
- Developers avoid repeating remote and branch names

This reduces errors and improves workflow efficiency, especially in team environments.

### **7. Constraints / Edge Cases (optional)**

Upstream configuration applies per branch; new branches require their own upstream setup.

---

# **Q5. Explain the difference between `git fetch` and `git pull`. Why is `fetch` safer?**

### **1. Title**

Fetch vs Pull in Git Synchronization

### **2. Problem Description**

Differentiate between fetching changes and pulling changes from a remote repository.

### **3. Objective**

Understand safe synchronization practices when working with shared repositories.

### **4. Hint**

Consider what happens to your current branch after each command.

### **5. Short Explanation**

`git fetch` only downloads updates, while `git pull` downloads and merges them immediately.

### **6. Detailed Explanation**

- `git fetch` retrieves new commits from the remote repository and updates remote-tracking branches, but **does not modify** the current local branch.
- `git pull` performs two actions:

  ```text
  git pull = git fetch + git merge
  ```

Because `git fetch` does not merge automatically, it allows developers to inspect incoming changes before integrating them.
This makes fetch safer, especially when working on critical branches like `main`.

### **7. Constraints / Edge Cases (optional)**

After fetching, a manual merge or rebase is still required to integrate changes.

---

# **Q6. Local to Remote Workflow (First Push)**

### **1. Title**

Connecting a Local Repository to a Remote and Pushing Code

### **2. Problem Description**

Perform a complete workflow to connect a local repository to GitHub and push the first commit.

### **3. Objective**

Practice initializing a project locally and synchronizing it with a remote repository.

### **4. Hint**

Follow the order: initialize → commit → connect remote → push.

### **5. Short Explanation**

A local repository is created, connected to GitHub using `origin`, and pushed with an upstream branch.

### **6. Detailed Explanation**

```bash
# Create local repository
mkdir remote-demo
cd remote-demo
git init

# Create file and commit
echo "# Remote Demo" > README.md
git add README.md
git commit -m "Initial commit"

# Connect to remote repository
git remote add origin <remote-repository-url>

# Push and set upstream
git push -u origin main
```

This workflow establishes GitHub as the remote source of truth and links the local branch to the remote branch.

### **7. Constraints / Edge Cases (optional)**

If the remote repository already contains commits, a pull may be required before pushing.

---

# **Q7. Feature Branch → Push → Pull Request → Merge**

### **1. Title**

Feature Branch Development with Pull Request Workflow

### **2. Problem Description**

Create a feature branch, push changes to GitHub, raise a Pull Request, and merge it into `main`.

### **3. Objective**

Understand professional collaboration using branches and Pull Requests.

### **4. Hint**

All development happens in a feature branch, not directly on `main`.

### **5. Short Explanation**

Changes are developed in isolation, reviewed via a Pull Request, and merged safely into `main`.

### **6. Detailed Explanation**

```bash
# Clone repository (if required)
git clone <repo-url>
cd remote-demo

# Create and switch to feature branch
git checkout -b feature-update

# Modify file
echo "Additional documentation" >> README.md

# Commit changes
git add README.md
git commit -m "Update README with feature info"

# Push branch
git push origin feature-update
```

**Remote (GitHub) steps:**

1. Open Pull Request: `feature-update → main`
2. Review changes
3. Merge Pull Request
4. Delete feature branch

This ensures stable main branch and reviewed changes.

### **7. Constraints / Edge Cases (optional)**

Merge conflicts may occur if `main` has diverged.

---

# **Q8. Collaboration Workflow with Pull Requests (Collaborator or Solo)**

### **1. Title**

Pull Request Workflow with Access Control

### **2. Problem Description**

Simulate a real collaboration scenario where changes are contributed and merged through Pull Requests.

### **3. Objective**

Understand how access control and PR-based collaboration work in real projects.

### **4. Hint**

Think in terms of “contributor submits” and “maintainer merges”.

### **5. Short Explanation**

Contributors push changes via branches and Pull Requests, while authorized users review and merge them.

### **6. Detailed Explanation**

**Option A — With Collaborator:**

- Owner adds collaborator with write access
- Collaborator clones repo and creates a branch
- Collaborator commits and pushes changes
- Collaborator opens a Pull Request
- Owner reviews and merges the PR

**Option B — Solo Simulation:**

```bash
git checkout -b collab-feature
echo "Collaboration content" > collab.txt
git add collab.txt
git commit -m "Add collab file"
git push origin collab-feature
```

**Remote steps:**

- Open PR from `collab-feature → main`
- Merge PR
- Delete branch

This models real-world contribution and approval flows even without a second person.

### **7. Constraints / Edge Cases (optional)**

- Merge permissions are required to complete PRs
- Repository rules may block merging without reviews

---
