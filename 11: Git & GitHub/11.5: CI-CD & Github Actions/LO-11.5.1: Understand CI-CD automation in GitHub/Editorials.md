## **Q1. Why manual testing alone is not sufficient in real-world collaborative software projects**

### **Problem Description**

In real-world projects, multiple developers work on the same codebase and make frequent changes, increasing the risk of defects.

### **Objective**

Explain why relying only on manual testing is inadequate in collaborative software development.

### **Hint**

Think about scale, speed, and when bugs are discovered.

### **Short Explanation**

Manual testing cannot keep up with frequent changes and multiple contributors.

### **Detailed Explanation**

In collaborative projects, code changes happen frequently and often in parallel. Manual testing is slow, repetitive, and prone to human error, making it difficult to test every change consistently. Bugs may be detected very late in the development cycle, increasing fixing cost and risk. Automated tests in CI pipelines provide fast, repeatable validation for every change, which manual testing alone cannot achieve.

### **Constraints / Edge Cases (Optional)**

- Manual testing is still useful for exploratory and UX testing
- Automation requires initial setup effort

---

## **Q2. Difference between Continuous Delivery and Continuous Deployment**

### **Problem Description**

The terms Continuous Delivery and Continuous Deployment are often confused, though they represent different release strategies.

### **Objective**

Clearly differentiate between Continuous Delivery and Continuous Deployment.

### **Hint**

Focus on automation level and human involvement.

### **Short Explanation**

Continuous Delivery prepares code for release, while Continuous Deployment releases it automatically.

### **Detailed Explanation**

In **Continuous Delivery**, every code change is automatically built and tested, and the application is always kept in a deployable state. However, a **manual approval step** is required to deploy to production.
In **Continuous Deployment**, there is no manual intervention—every change that passes all automated tests is **automatically deployed to production**. Continuous Deployment requires very high confidence in test coverage and system stability.

### **Constraints / Edge Cases (Optional)**

- Continuous Deployment is risky without strong automated testing
- Regulatory environments often require manual approval

---

## **Q3. How CI/CD pipelines protect the main branch when using Pull Requests**

### **Problem Description**

Unverified code merged into the main branch can break builds and affect all users.

### **Objective**

Explain how CI/CD pipelines enforce quality before code reaches the main branch.

### **Hint**

Think about triggers, checks, and merge rules.

### **Short Explanation**

CI/CD pipelines validate Pull Requests and block merging if checks fail.

### **Detailed Explanation**

In **GitHub**, CI/CD pipelines are triggered when a Pull Request is created or updated. These pipelines run automated checks such as builds, tests, and linting. Branch protection rules can mark these checks as mandatory. If any required check fails, GitHub disables the merge option, preventing unstable or broken code from entering the main branch and keeping it stable.

### **Constraints / Edge Cases (Optional)**

- Incorrectly configured checks may block valid merges
- Admin overrides can bypass protections if enabled
