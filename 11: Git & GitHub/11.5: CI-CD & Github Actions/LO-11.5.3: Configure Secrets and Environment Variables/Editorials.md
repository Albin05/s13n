## **Q1. Difference between environment variables and secrets in GitHub Actions**

### **Problem Description**

Workflows require configuration values, but not all values have the same sensitivity or security risk.

### **Objective**

Explain the difference between environment variables and secrets with real-world examples.

### **Hint**

Consider visibility, usage purpose, and security impact.

### **Short Explanation**

Environment variables store non-sensitive configuration, while secrets store sensitive data that must be protected.

### **Detailed Explanation**

In **GitHub Actions**, **environment variables** are used for general configuration values that are safe to expose in logs or workflow files.
_Example:_ `APP_ENV=production` or `LOG_LEVEL=debug`.

**Secrets** are designed for sensitive information such as passwords, tokens, or API keys. They are encrypted, hidden from logs, and masked automatically if accidentally printed.
_Example:_ `DATABASE_PASSWORD` or `API_KEY`.

### **Constraints / Edge Cases (Optional)**

- Secrets should never be intentionally logged
- Environment variables are visible in workflow definitions

---

## **Q2. Why workflows must be rerun manually after adding or updating secrets**

### **Problem Description**

Developers often expect newly added secrets to be available immediately in running workflows.

### **Objective**

Explain why GitHub Actions requires rerunning workflows after secret updates.

### **Hint**

Think about when secrets are injected into workflows.

### **Short Explanation**

Secrets are loaded only when a workflow run starts.

### **Detailed Explanation**

GitHub Actions injects secrets into the workflow environment **at the start of a workflow run**. If a secret is added or updated after a workflow has already started, the running job cannot access the new value. Rerunning the workflow ensures it restarts cleanly and securely loads the updated secrets, maintaining predictable behavior and security.

### **Constraints / Edge Cases (Optional)**

- Cancelled workflows must be restarted
- Scheduled or manual triggers are commonly used after updates

---

## **Q3. Implementation Task 1 Editorial: Using Environment Variables in GitHub Actions**

### **Problem Description**

Applications often need environment-based configuration without modifying source code.

### **Objective**

Demonstrate how to define and read environment variables in a GitHub Actions workflow.

### **Hint**

Define the variable in the workflow and read it in the program.

### **Short Explanation**

Environment variables enable dynamic configuration during CI runs.

### **Detailed Explanation**

In this task, a repository is created with a program that reads the `APP_ENV` environment variable and prints its value. The GitHub Actions workflow defines `APP_ENV` and triggers on pushes to `main`. When the workflow runs, the program reads the variable from the runtime environment and prints it in the logs, confirming correct environment variable usage.

### **Constraints / Edge Cases (Optional)**

- Variable names are case-sensitive
- Missing variables may cause runtime errors

---

## **Q4. Implementation Task 2 Editorial: Using Secrets Securely in GitHub Actions**

### **Problem Description**

Automation workflows often need sensitive credentials without exposing them.

### **Objective**

Demonstrate secure usage of GitHub Secrets in a CI workflow.

### **Hint**

Check for the presence of the secret, not its value.

### **Short Explanation**

Secrets allow workflows to use sensitive data without revealing it.

### **Detailed Explanation**

In this task, a repository secret named `DUMMY_API_KEY` is added in GitHub settings. The program reads the secret at runtime and checks whether it exists, printing only a confirmation message such as `Secret exists: true`. The GitHub Actions workflow passes the secret securely to the program. Even if a secret is accidentally echoed, GitHub masks it in logs, ensuring sensitive values remain protected.

### **Constraints / Edge Cases (Optional)**

- Secrets are not available to workflows from untrusted forks
- Printing secrets directly is discouraged despite masking
