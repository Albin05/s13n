### **1. Start with an Ideal Scenario Activity (5 minutes)**

- Present a real-world team setup:

  - Developer 1 works on a **new feature**
  - Developer 2 works on another **new feature**
  - Developer 3 works on a **critical bug fix**
  - Developer 4 works on an **experimental change**

- State that all developers are modifying the **same project**, sometimes even the **same file**.
- Ask guiding questions:

  - Can all developers push their changes directly to `main`?
  - If all changes are pushed together, which code should be accepted?
  - What happens if one feature is incomplete?
  - What if the experiment breaks the application?
  - Can the bug fix be released alone?

- Highlight that:

  - Direct work on `main` mixes unrelated changes
  - Risk of breaking stable code is high
  - Parallel development becomes unsafe

- Conclude the activity by stating the need for a system that allows:

  - Independent work
  - Selective acceptance of changes
  - Protection of stable code

---

### **2. Connect the Activity to the Need for Branching (3 minutes)**

- Explain that in professional development:

  - `main` represents stable, production-ready code
  - New features, fixes, and experiments should not disturb stability

- State that Git provides **branching** to solve this exact problem.
- Emphasize isolation as the core idea behind branching.

---

### **3. Introduce the Concept of a Branch (3 minutes)**

- Define a branch as an independent line of development.
- Mention that:

  - Each branch has its own commit history
  - Changes in one branch do not affect others
  - `main` is the default stable branch

- Reinforce that branching allows parallel work without conflict.

---

### **4. Explain Isolated Development Using Branches (4 minutes)**

- Describe how branches allow:

  - Feature development without risk
  - Bug fixes without blocking other work
  - Experiments without fear of failure

- Relate back to the opening activity:

  - Each developer can work on a separate branch
  - Only completed and approved work is later integrated

- Establish the idea that each branch behaves like a separate workspace.

---

### **5. Demonstrate Viewing Existing Branches (3 minutes)**

- Ask learners to list local branches using:

  ```bash
  git branch
  ```

- Explain the meaning of:

  - Branch list
  - `*` indicating the current branch

- Reinforce awareness of the current working branch before making changes.

---

### **6. Demonstrate Creating a Branch (4 minutes)**

- Show how to create a branch without switching:

  ```bash
  git branch feature-login
  ```

- Emphasize:

  - Branch is created
  - Current working branch remains unchanged

- Encourage learners to verify branch creation using `git branch`.

---

### **7. Demonstrate Switching Between Branches (5 minutes)**

- Show how to switch to an existing branch:

  ```bash
  git switch feature-login
  ```

  or

  ```bash
  git checkout feature-login
  ```

- Explain that:

  - All new work now belongs to the selected branch
  - Context switches entirely to that branch

---

### **8. Demonstrate Creating and Switching in One Step (4 minutes)**

- Introduce the combined command:

  ```bash
  git checkout -b feature-signup
  ```

  or

  ```bash
  git switch -c feature-signup
  ```

- Mention that this is the most common workflow in real projects.

---

### **9. Working Inside an Isolated Branch (5 minutes)**

- Demonstrate a typical workflow:

  - Switch to a branch
  - Modify or create files
  - Stage changes
  - Commit changes

  ```bash
  git switch feature-login
  git add login.js
  git commit -m "Add login form UI"
  ```

- Switch back to `main`:

  ```bash
  git switch main
  ```

- Reinforce that:

  - Changes made in the branch are not present in `main`
  - Isolation is preserved

---

### **10. Student Practice — Repeat Isolation (6 minutes)**

- Ask learners to perform the following twice:

  1. Create a new branch
  2. Switch to the branch
  3. Make a small change
  4. Commit the change
  5. Switch back to `main`

- Suggested branch purposes:

  - Bug fix
  - Experimental change

---

### **11. Introduce Branch Naming Conventions (3 minutes)**

- Present recommended naming patterns:

  - `feature-login`
  - `bugfix-navbar`
  - `hotfix-payment-issue`
  - `experiment-ui-layout`

- State naming rules:

  - Lowercase
  - Hyphen-separated
  - Purpose-driven

- Warn against generic names like `test`, `new`, `temp`.

---

### **12. Demonstrate Deleting Branches (4 minutes)**

- Explain that branches are temporary.

- Show safe deletion:

  ```bash
  git branch -d feature-login
  ```

- Explain force deletion for unused or abandoned branches:

  ```bash
  git branch -D experiment-old-ui
  ```

---

### **13. Branch Cleanup Best Practices (3 minutes)**

- Explain importance of cleanup:

  - Avoid clutter
  - Reduce confusion
  - Prevent outdated work

- Show recommended cleanup flow:

  ```bash
  git switch main
  git branch -d feature-login
  ```

---

### **14. Explain Branch Lifecycle (3 minutes)**

- Walk through the lifecycle stages:

  - Branch creation
  - Active development
  - Merge into main (next topic)
  - Branch deletion

- Mention this lifecycle is followed in professional teams.

---

### **15. Conclude with Key Takeaways (2 minutes)**

- Reinforce:

  - One task per branch
  - `main` must remain stable
  - Branches enable parallel development
  - Cleanup is mandatory

- Transition statement:

---
