## **Q4. Difference between environment variables and secrets in GitHub Actions**

### **Problem Description**

Workflows often require configuration values such as environment names, flags, or credentials, but not all values have the same security sensitivity.

### **Objective**

Explain the difference between **environment variables** and **secrets** in **GitHub Actions**, with real-world examples.

### **Hint**

Think about visibility, security risk, and usage purpose.

### **Short Explanation**

Environment variables store non-sensitive configuration, while secrets store sensitive data that must be protected.

### **Detailed Explanation**

**Environment variables** are used for general configuration values that are safe to expose in logs, such as application mode or feature flags.
_Example:_ `APP_ENV=production` helps the application decide whether it is running in development or production.

**Secrets** are designed for sensitive values like passwords, API keys, or tokens. They are encrypted by GitHub and automatically masked in workflow logs.
_Example:_ `DATABASE_PASSWORD` or `API_KEY` must be stored as secrets to prevent unauthorized access if logs or workflows are exposed.

### **Constraints / Edge Cases (Optional)**

- Secrets should never be logged or echoed directly
- Environment variables are visible in workflow definitions and logs

---

## **Q5. Why workflows must be rerun manually after adding or updating secrets**

### **Problem Description**

Developers often expect newly added or updated secrets to be available immediately in running workflows.

### **Objective**

Explain why GitHub Actions requires workflows to be rerun to use updated secrets.

### **Hint**

Consider when secrets are injected into workflows.

### **Short Explanation**

Secrets are loaded only at workflow start time, not during execution.

### **Detailed Explanation**

In GitHub Actions, secrets are injected into the workflow environment **only when a workflow run starts**. If a secret is added or modified after a workflow has already begun, that running workflow cannot access the new value. Re-running the workflow ensures it starts fresh and securely loads the latest secret values. This design prevents unpredictable behavior and maintains security consistency.

### **Constraints / Edge Cases (Optional)**

- Cancelled workflows must be restarted manually
- Scheduled or manual triggers are often used after secret updates

---

## **Q6. Implementation Task 1 Editorial: Using Environment Variables in GitHub Actions**

### **Problem Description**

Applications often behave differently based on environment (development, staging, production), which must be configurable without changing code.

### **Objective**

Demonstrate how to pass and read environment variables in a GitHub Actions workflow.

### **Hint**

Define the variable in the workflow and read it inside the program.

### **Short Explanation**

Environment variables allow dynamic configuration of applications during CI runs.

### **Detailed Explanation**

In this task, a repository is created with a program that reads the `APP_ENV` environment variable and prints its value. The GitHub Actions workflow defines `APP_ENV` directly in the workflow configuration and triggers on pushes to the `main` branch. When the workflow runs, the program reads the variable from the runtime environment and prints it to the logs, confirming successful environment-based configuration.

### **Constraints / Edge Cases (Optional)**

- Variable names are case-sensitive
- Missing environment variables may cause runtime errors

---

## **Q7. Implementation Task 2 Editorial: Using Secrets Securely in GitHub Actions**

### **Problem Description**

Sensitive credentials must be used in automation without exposing them in source code or logs.

### **Objective**

Demonstrate secure usage of GitHub Secrets in a CI workflow.

### **Hint**

Check for existence of the secret, not its value.

### **Short Explanation**

Secrets allow workflows to use sensitive data securely without revealing it.

### **Detailed Explanation**

In this task, a repository secret named `DUMMY_API_KEY` is created in GitHub settings. The program reads this secret at runtime and checks whether it exists, printing only a confirmation message such as `Secret exists: true`. The GitHub Actions workflow passes the secret securely to the program. Even if accidentally echoed, GitHub automatically masks secret values in logs, ensuring sensitive information is never exposed.

### **Constraints / Edge Cases (Optional)**

- Secrets are not available to workflows triggered from untrusted forks
- Printing secrets directly is discouraged despite masking
