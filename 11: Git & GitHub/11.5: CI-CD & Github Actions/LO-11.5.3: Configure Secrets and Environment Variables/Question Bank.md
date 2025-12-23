### **Q1.** Explain the difference between **environment variables** and **secrets** in GitHub Actions, with one real-world example for each.

_Hint:_ Consider visibility, purpose, and security risk.

---

### **Q2.** Why does GitHub Actions require workflows to be **rerun manually** after adding or updating secrets?

_Hint:_ Think about workflow execution timing.

---

## **Q3. Implementation Task 1: Using Environment Variables in GitHub Actions**

### **Problem Statement**

Create a program that prints the **current application environment** using an **environment variable**, and automate its execution using GitHub Actions.

### **Requirements**

1. Create a GitHub repository named:

   ```
   github-actions-env-demo
   ```

2. Write a program (any language) that:

   - Reads an environment variable `APP_ENV`
   - Prints its value to the console

3. Create a GitHub Actions workflow that:

   - Triggers on `push` to `main`
   - Defines `APP_ENV` as an environment variable
   - Executes the program

4. Verify that:

   - The workflow runs successfully
   - The environment value appears in the logs

📌 **Submission**

- Repository link
- Screenshot of workflow logs showing `APP_ENV` output

> ⚠️ **Important Instruction**
> Use a **separate GitHub repository** and its **own GitHub Actions workflow**.
> Students may use **any programming language**.

---

## **Q4. Implementation Task 2: Using Secrets Securely in GitHub Actions**

### **Problem Statement**

Create a program that **checks whether a secret exists** (without printing its value) and automate it using GitHub Actions.

### **Requirements**

1. Create a GitHub repository named:

   ```
   github-actions-secrets-demo
   ```

2. Add a **repository secret** in GitHub:

   - **Name:** `DUMMY_API_KEY`
   - **Value:** Any random string

3. Write a program (any language) that:

   - Reads `DUMMY_API_KEY`
   - Prints a message confirming whether the secret exists (true/false)
   - **Does NOT print the secret value**

4. Create a GitHub Actions workflow that:

   - Triggers on `push` to `main`
   - Passes the secret to the program securely

5. Verify that:

   - Workflow runs successfully
   - Logs confirm the secret exists
   - Secret value is not visible in logs

📌 **Submission**

- Repository link
- Screenshot of workflow logs showing confirmation message
  > ⚠️ **Important Instruction**
  > Use a **separate GitHub repository** and its **own GitHub Actions workflow**.
  > Students may use **any programming language**.

---
