## **Q1. Why CI alone is not sufficient without branch protection in collaborative projects**

### **Problem Description**

CI pipelines can detect failing tests or broken builds, but they do not automatically control developer actions.

### **Objective**

Explain why CI by itself cannot guarantee code quality in collaborative environments.

### **Hint**

Think about human behavior and the option to “Merge anyway”.

### **Short Explanation**

CI provides feedback, but without enforcement, developers can still merge failing code.

### **Detailed Explanation**

In collaborative projects, CI pipelines run checks and report results, but they act only as **advisory signals** if branch protection is not enabled. A developer can ignore failed CI checks and still merge code into the main branch using manual overrides or direct pushes. This human factor makes CI alone unreliable for maintaining stability. Without branch protection, automation lacks authority.

### **Constraints / Edge Cases (Optional)**

- Small personal projects may rely only on CI
- Admin users can still bypass safeguards if allowed

---

## **Q2. How branch protection converts CI from “advice” into “law”**

### **Problem Description**

CI produces pass/fail results, but enforcement depends on repository rules.

### **Objective**

Explain how branch protection enforces CI results during merges.

### **Hint**

Focus on merge permissions and required checks.

### **Short Explanation**

Branch protection makes CI checks mandatory before merging.

### **Detailed Explanation**

In **GitHub**, branch protection allows repository owners to mark CI workflows as **required status checks**. When enabled, GitHub disables the merge button until all required checks pass. This means developers cannot merge code—even intentionally—unless CI succeeds. As a result, CI moves from being a recommendation to a strictly enforced rule.

### **Constraints / Edge Cases (Optional)**

- Misconfigured required checks can block valid merges
- Admin override permissions may weaken enforcement

---

## **Q3. Implementation Task 1 Editorial: Enforcing CI Before Merge (Failure Case)**

### **Problem Description**

Teams must prevent unstable or failing code from entering the main branch.

### **Objective**

Demonstrate how branch protection blocks merging when CI fails.

### **Hint**

Intentionally fail CI and observe merge behavior.

### **Short Explanation**

A failing CI workflow combined with branch protection blocks the merge.

### **Detailed Explanation**

In this task, a repository is configured with a GitHub Actions workflow that runs on `pull_request` to `main` and intentionally fails. Branch protection rules require Pull Requests and passing status checks. When a feature branch Pull Request is opened, the CI workflow fails, and GitHub disables the merge button while clearly indicating that required checks are not passing. This proves that branch protection actively enforces CI results.

### **Constraints / Edge Cases (Optional)**

- CI workflow must be selected explicitly as a required check
- Cached or skipped workflows may cause confusion

---

## **Q4. Implementation Task 2 Editorial: Successful CI → Allowed Merge**

### **Problem Description**

Enforcement should not block progress when code is correct.

### **Objective**

Show that passing CI enables merging into a protected branch.

### **Hint**

Ensure the workflow completes successfully.

### **Short Explanation**

When CI passes, branch protection allows the merge.

### **Detailed Explanation**

In this task, a repository is set up with a program and a CI workflow that completes successfully on Pull Requests. Branch protection rules require passing status checks before merging. After raising a Pull Request from a feature branch, the CI workflow runs and passes. GitHub then enables the merge button, allowing the Pull Request to be merged into `main`. This confirms that branch protection enforces quality without blocking valid changes.

### **Constraints / Edge Cases (Optional)**

- All required checks must pass, not just one
- Re-running CI may be required after updates
