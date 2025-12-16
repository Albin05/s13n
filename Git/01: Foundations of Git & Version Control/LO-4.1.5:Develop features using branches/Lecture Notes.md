# **1. Ideal Scenario — Why Branching is Needed**

Consider a real-world development setup:

- A stable application exists on the `main` branch
- A new feature needs to be developed
- A bug fix must be applied urgently
- Another change is experimental

If all work happens directly on `main`:

- Incomplete features can break the application
- Bugs may reach production
- Parallel work becomes risky
- Code history becomes difficult to manage

Branching solves this problem by isolating work.

---

# **2. What is a Branch in Git**

A **branch** is a lightweight pointer to a commit that represents an independent line of development.

- Each branch has its own commit history
- Changes in one branch do not affect others
- `main` is the default stable branch

---

# **3. Isolated Development Using Branches**

Branches provide isolation between different types of work.

Benefits:

- Feature development without risk
- Bug fixes without blocking others
- Experiments without fear
- Stable and clean `main` branch

Each branch acts like a separate workspace.

---

# **4. Viewing Existing Branches — `git branch`**

List all local branches:

```bash
git branch
```

The current branch is marked with `*`.

### Example output:

```bash
* main
  feature-login
  bugfix-header
```

---

# **5. Creating Branches — `git branch`**

Create a new branch without switching to it:

```bash
git branch feature-login
```

### Example

```bash
git branch feature-login
```

- Branch is created
- You remain on `main`

---

# **6. Switching Branches — `git checkout` / `git switch`**

## **A. Switch to an existing branch**

```bash
git checkout feature-login
```

or:

```bash
git switch feature-login
```

### Example

```bash
git switch feature-login
```

All new work now belongs to `feature-login`.

---

## **B. Create and switch in one command**

```bash
git checkout -b feature-signup
```

or:

```bash
git switch -c feature-signup
```

### Example

```bash
git checkout -b feature-signup
```

---

# **7. Working in an Isolated Branch**

Once inside a branch:

- Edit files
- Stage changes
- Commit changes

### Example workflow:

```bash
git switch feature-login
git add login.js
git commit -m "Add login form UI"
```

These changes are isolated from `main`.

---

# **8. Branch Naming Conventions**

Clear naming improves collaboration and maintenance.

## **Recommended patterns**

| Purpose    | Example Branch Name    |
| ---------- | ---------------------- |
| Feature    | `feature-login`        |
| Bug Fix    | `bugfix-navbar`        |
| Hotfix     | `hotfix-payment-issue` |
| Experiment | `experiment-ui-layout` |

### Rules:

- Use lowercase letters
- Use hyphens
- Avoid generic names like `test`, `new`, `temp`

---

# **9. Deleting Branches — `git branch -d`**

Once a branch has served its purpose, it should be deleted.

## **A. Delete a merged branch (safe)**

```bash
git branch -d feature-login
```

### Example

```bash
git branch -d feature-login
```

Deletes the branch only if it is fully merged.

---

## **B. Force delete an unmerged branch**

```bash
git branch -D experiment-old-ui
```

### Example

```bash
git branch -D experiment-old-ui
```

Use only when the branch is no longer needed.

---

# **10. Branch Cleanup (Best Practices)**

Branch cleanup keeps the repository manageable and readable.

Why cleanup is important:

- Avoids clutter
- Reduces confusion
- Prevents working on outdated branches
- Keeps branch list meaningful

## **Recommended cleanup process**

1. Merge branch into `main`
2. Delete the local branch
3. Ensure no unused branches remain

### Example cleanup flow:

```bash
git switch main
git branch -d feature-login
```

---

# **11. Understanding Branch Lifecycle**

| Stage              | Description                    |
| ------------------ | ------------------------------ |
| Branch creation    | New line of development begins |
| Active development | Commits added in isolation     |
| Merge (next topic) | Changes integrated into main   |
| Cleanup            | Branch deleted after use       |

This lifecycle is followed in professional projects.

---

# **12. Summary Table**

| Command                  | Purpose                    |
| ------------------------ | -------------------------- |
| `git branch`             | List all local branches    |
| `git branch <name>`      | Create a branch            |
| `git checkout <name>`    | Switch to a branch         |
| `git checkout -b <name>` | Create and switch branch   |
| `git switch <name>`      | Switch branch (modern)     |
| `git switch -c <name>`   | Create and switch (modern) |
| `git branch -d <name>`   | Delete merged branch       |
| `git branch -D <name>`   | Force delete branch        |

---

# **13. Key Takeaway**

Branches enable safe, parallel, and structured development.
Equally important is **branch cleanup**, which ensures repositories remain clean and maintainable.

---
