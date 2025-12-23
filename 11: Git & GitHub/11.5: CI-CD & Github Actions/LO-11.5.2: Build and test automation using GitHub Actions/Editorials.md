## **Q1. Why is it considered a best practice to restrict CI workflows to the `main` branch in team projects?**

### **Problem Description**

In team projects, multiple feature and experimental branches are created, often containing incomplete or unstable code.

### **Objective**

Explain why CI workflows are commonly restricted to run only on the `main` branch.

### **Hint**

Think about stability, cost, and signal vs noise.

### **Short Explanation**

Restricting CI to `main` ensures automation runs only on stable, production-relevant code.

### **Detailed Explanation**

In collaborative environments, feature branches may contain work-in-progress changes that are not ready for validation. Running CI on every branch can waste resources and produce misleading failures. By restricting CI workflows to the `main` branch, teams ensure that automation validates only code that has been reviewed and integrated, keeping CI results meaningful, cost-effective, and focused on release-quality code.

### **Constraints / Edge Cases (Optional)**

- Some teams enable CI on feature branches for early feedback
- Large projects may use selective branch rules instead of only `main`

---

## **Q2. How GitHub Actions integrates with Pull Requests to prevent unstable code from being merged**

### **Problem Description**

Merging untested or failing code into the main branch can break builds and affect all collaborators.

### **Objective**

Explain how GitHub Actions works with Pull Requests to protect the main branch.

### **Hint**

Think about triggers, automated checks, and merge blocking.

### **Short Explanation**

GitHub Actions runs automated checks on Pull Requests and blocks merges if they fail.

### **Detailed Explanation**

In **GitHub**, GitHub Actions workflows can be triggered when a Pull Request is created or updated. These workflows run automated tasks such as builds, tests, and linting. When branch protection rules mark these workflows as required checks, GitHub disables the merge button if any check fails. This ensures that only verified, stable code can be merged into the `main` branch.

### **Constraints / Edge Cases (Optional)**

- Required checks must be configured correctly
- Admin overrides can bypass protections if enabled

---

## **Q3. Implementation Task Editorial: Direct Push Trigger on Main Branch**

### **Problem Description**

Some workflows need to run automatically when code is pushed directly to the main branch.

### **Objective**

Demonstrate a CI workflow that triggers on direct pushes to `main` and executes a program.

### **Hint**

Use a `push` trigger filtered to the `main` branch.

### **Short Explanation**

A push-based workflow ensures automation runs immediately on updates to `main`.

### **Detailed Explanation**

In this task, a repository is created with a simple even–odd checking program written in any language. A GitHub Actions workflow is configured to trigger on `push` events to the `main` branch. The workflow sets up the required runtime environment and executes the program. When code is pushed directly to `main`, the workflow runs automatically and prints output in the action logs, confirming successful automation.

### **Constraints / Edge Cases (Optional)**

- Direct pushes are often disabled in real projects using branch protection
- Runtime setup depends on the chosen programming language

---

## **Q4. Implementation Task Editorial: Feature Branch → Pull Request → Main Branch Trigger**

### **Problem Description**

Teams need to clearly understand how branch-specific triggers affect CI execution.

### **Objective**

Demonstrate that workflows restricted to `main` do not run on feature branches but run after merging.

### **Hint**

Observe workflow behavior before and after merge.

### **Short Explanation**

Branch-restricted workflows ignore feature branch pushes and run only when code reaches `main`.

### **Detailed Explanation**

In this task, a vowel-counting program is developed in a feature branch. The GitHub Actions workflow is configured to trigger only on pushes to `main`. As a result, pushing code to the feature branch does not start the workflow. When a Pull Request is raised and merged into `main`, the merge commit triggers the workflow, and the program executes successfully. This demonstrates safe, controlled CI execution aligned with team workflows.

### **Constraints / Edge Cases (Optional)**

- Squash or rebase merges still trigger workflows on `main`
- Manual re-runs may confuse first-time observations
