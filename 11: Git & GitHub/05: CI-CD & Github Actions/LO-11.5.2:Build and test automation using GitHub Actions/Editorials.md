## **Q4. Why is it considered a best practice to restrict CI workflows to the `main` branch in team projects?**

### **Problem Description**

In team-based development, multiple branches are created for features, experiments, and fixes. Running CI on every branch can lead to unnecessary executions and noise.

### **Objective**

Explain why CI workflows are commonly restricted to the `main` branch in collaborative projects.

### **Hint**

Think about stability, cost, and signal-to-noise ratio.

### **Short Explanation**

Restricting CI to the `main` branch ensures that automation validates only production-ready or near-production code.

### **Detailed Explanation**

In team projects, feature branches may contain incomplete or experimental code. If CI workflows run on every branch, it can consume resources unnecessarily and produce confusing results. By restricting workflows to the `main` branch, teams ensure that CI runs only when code is integrated and expected to be stable. This practice improves reliability, reduces cost, and keeps CI feedback focused on code that truly matters for releases.

### **Constraints / Edge Cases (Optional)**

- Some teams run CI on feature branches for early feedback
- Large projects may use selective branch rules instead of only `main`

---

## **Q5. How GitHub Actions integrates with Pull Requests to prevent unstable code from being merged**

### **Problem Description**

Merging untested or broken code into the main branch can destabilize the entire project.

### **Objective**

Explain how **GitHub Actions** works with Pull Requests to protect code quality.

### **Hint**

Focus on triggers, checks, and merge restrictions.

### **Short Explanation**

GitHub Actions automatically validates Pull Requests and blocks merging if checks fail.

### **Detailed Explanation**

When a Pull Request is created or updated, GitHub Actions can automatically trigger workflows such as build, test, or lint jobs. These workflows report their status back to the Pull Request as checks. If any required check fails, GitHub prevents the Pull Request from being merged into the `main` branch. This ensures that only code passing all automated validations becomes part of the stable codebase.

### **Constraints / Edge Cases (Optional)**

- Required checks must be configured in branch protection rules
- Misconfigured workflows may give false positives or negatives

---

## **Q6. Implementation Task Editorial: Direct Push Trigger on Main Branch**

### **Problem Description**

Teams need automation that runs immediately when code is pushed directly to the main branch.

### **Objective**

Demonstrate how a GitHub Actions workflow can be triggered on direct pushes to `main` and execute a program.

### **Hint**

Focus on `push` triggers and branch filtering.

### **Short Explanation**

A push-based workflow ensures that any direct update to the main branch is automatically validated or executed.

### **Detailed Explanation**

In this task, a repository is created with a simple even–odd program written in any language. A GitHub Actions workflow is configured using a `push` trigger limited to the `main` branch. When code is pushed directly to `main`, the workflow sets up the required runtime and executes the program. The workflow logs act as proof that automation ran successfully and produced the expected output.

### **Constraints / Edge Cases (Optional)**

- Direct pushes may be disabled in real projects using branch protection
- Runtime setup depends on the chosen programming language

---

## **Q7. Implementation Task Editorial: Feature Branch → Pull Request → Main Branch Trigger**

### **Problem Description**

Teams must clearly understand how branch-specific triggers affect CI execution.

### **Objective**

Demonstrate that workflows restricted to `main` do not run on feature branches but run after merging via Pull Requests.

### **Hint**

Observe workflow behavior before and after merge.

### **Short Explanation**

Workflows configured for `main` ignore feature branch pushes and run only when code reaches the main branch.

### **Detailed Explanation**

In this task, a vowel-counting program is developed in a feature branch. Since the GitHub Actions workflow is configured to trigger only on pushes to `main`, pushing code to the feature branch does not start the workflow. Once a Pull Request is raised and merged into `main`, the merge commit triggers the workflow. This clearly demonstrates branch-based control in GitHub Actions and reinforces safe integration practices.

### **Constraints / Edge Cases (Optional)**

- Squash vs merge commits may affect commit history but not triggers
- Manual re-runs may confuse initial observations
