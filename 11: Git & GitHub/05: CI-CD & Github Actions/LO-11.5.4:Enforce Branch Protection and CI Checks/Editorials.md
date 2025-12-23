## **Q4. Why CI alone is not sufficient without branch protection in collaborative projects**

### **Problem Description**

Continuous Integration (CI) can automatically test code, but it does not inherently control human actions during merging.

### **Objective**

Explain why CI by itself cannot guarantee code quality in team-based repositories.

### **Hint**

Think about human behavior and the option to “Merge anyway”.

### **Short Explanation**

CI provides feedback, but without branch protection, developers can still merge failing code.

### **Detailed Explanation**

CI pipelines run tests and checks and report results, but they act only as **advisors** if branch protection is not enabled. In collaborative projects, a developer may ignore failed CI results and manually merge code into the main branch. This defeats the purpose of automation and can introduce broken or unstable code. Branch protection is required to enforce CI results and prevent human errors or shortcuts.

### **Constraints / Edge Cases (Optional)**

- Small personal projects may rely only on CI
- Emergency hotfixes may temporarily bypass rules (with admin override)

---

## **Q5. How branch protection converts CI from “advice” into “law”**

### **Problem Description**

CI reports pass/fail status, but enforcement depends on repository rules.

### **Objective**

Explain how branch protection enforces CI results during merges.

### **Hint**

Focus on merge permissions and enforcement.

### **Short Explanation**

Branch protection makes CI checks mandatory before allowing a merge.

### **Detailed Explanation**

In **GitHub**, branch protection allows repository owners to mark CI checks as **required status checks**. Once enabled, GitHub blocks the merge button until all required CI workflows pass successfully. This transforms CI from a suggestion into a strict rule—code cannot enter the protected branch unless it meets quality standards. As a result, every merge into `main` is guaranteed to be tested and validated.

### **Constraints / Edge Cases (Optional)**

- Admins may have override permissions
- Incorrectly configured checks can block valid merges

---

## **Q6. Implementation Task 1 Editorial: Enforcing CI Before Merge (CI Failure Case)**

### **Problem Description**

Teams must ensure that failing code cannot be merged into the main branch.

### **Objective**

Demonstrate how branch protection blocks merging when CI fails.

### **Hint**

Intentionally fail the CI workflow and observe merge behavior.

### **Short Explanation**

A failing CI workflow combined with branch protection prevents code from being merged.

### **Detailed Explanation**

In this task, a repository is configured with a GitHub Actions workflow that runs on Pull Requests to `main` and intentionally fails. Branch protection rules are enabled to require Pull Requests and passing CI checks. When a feature branch Pull Request is opened, the CI workflow fails, and GitHub disables the merge button. This clearly demonstrates how branch protection enforces CI results and protects the main branch from unstable code.

### **Constraints / Edge Cases (Optional)**

- CI must be selected explicitly as a required check
- Cached or skipped workflows may cause confusion

---

## **Q7. Implementation Task 2 Editorial: Successful CI → Allowed Merge**

### **Problem Description**

Teams need proof that branch protection still allows progress when code is correct.

### **Objective**

Show that passing CI enables merging into a protected branch.

### **Hint**

Ensure the workflow completes successfully.

### **Short Explanation**

When CI passes, branch protection allows the merge into the main branch.

### **Detailed Explanation**

In this task, a repository is set up with a successful program and a GitHub Actions workflow that passes all checks on Pull Requests. Branch protection rules require CI to pass before merging. After opening a Pull Request from a feature branch, the CI workflow runs and completes successfully. GitHub then enables the merge button, allowing the Pull Request to be merged into `main`. This confirms that branch protection enforces quality without blocking valid contributions.

### **Constraints / Edge Cases (Optional)**

- Re-running CI may be needed after code updates
- Multiple required checks must all pass

---
