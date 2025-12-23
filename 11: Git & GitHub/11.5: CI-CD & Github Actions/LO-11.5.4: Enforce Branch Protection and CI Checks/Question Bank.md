### **Q1.** Explain why **CI alone is not sufficient** without branch protection in collaborative projects.

_Hint:_ Think about human behavior and “Merge anyway”.

---

### **Q2.** How does **branch protection convert CI from “advice” into “law”**?

_Hint:_ Consider merge permissions and enforcement.

---

## **Q3. Implementation Task 1: Enforcing CI Before Merge**

### **Problem Statement**

Demonstrate how **branch protection prevents merging code when CI fails**.

### **Requirements**

1. Create a GitHub repository named:

   ```
   github-branch-protection-ci-fail
   ```

2. Add a simple program (any language) that:

   - Prints a message like `"Running CI check"`

3. Create a GitHub Actions workflow that:

   - Runs on `pull_request` to `main`
   - **Intentionally fails** (for example: exit with error or throw exception)

4. Enable **branch protection** on `main`:

   - Require pull request before merging
   - Require status checks to pass
   - Select your CI workflow as required

5. Create a feature branch and raise a PR to `main`

### **What to Observe**

- CI fails ❌
- Merge button is **disabled**
- GitHub clearly shows required checks not passing

📌 **Submission**

- Repository link
- Screenshot of PR showing failed checks and blocked merge

> ⚠️ **Important Instructions**

> - It must be a **separate GitHub repository**
> - Any programming language may be used
> - GitHub Actions \*\*must be involved

---

## **Q4. Implementation Task 2: Successful CI → Allowed Merge**

### **Problem Statement**

Demonstrate how **branch protection allows merging only after CI passes**.

### **Requirements**

1. Create a new GitHub repository named:

   ```
   github-branch-protection-ci-pass
   ```

2. Write a simple program (any language) that:

   - Runs successfully
   - Prints a confirmation message

3. Create a GitHub Actions workflow that:

   - Runs on `pull_request` to `main`
   - Completes successfully

4. Enable **branch protection** on `main`:

   - Require pull request before merging
   - Require status checks to pass

5. Create a feature branch:

   - Push code
   - Raise a Pull Request to `main`

6. Merge the PR **only after CI passes**

### **What to Observe**

- CI passes ✅
- Merge button becomes enabled
- Merge into `main` is allowed

📌 **Submission**

- Repository link
- Screenshot of:

  - Successful CI checks
  - Enabled merge button
  - Merged PR

> ⚠️ **Important Instructions**

> - It must be a **separate GitHub repository**
> - Any programming language may be used
> - GitHub Actions **must be involved**

---
