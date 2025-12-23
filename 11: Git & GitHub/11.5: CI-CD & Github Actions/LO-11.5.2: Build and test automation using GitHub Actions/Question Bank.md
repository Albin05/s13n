### **Q1.** Why is it considered a best practice to **restrict CI workflows to the `main` branch** in team projects?

---

### **Q2.** Explain how **GitHub Actions integrates with Pull Requests** to prevent unstable code from being merged.

---

## 🛠️ **Section C: Implementation-Based Questions (Application Level)**

> ⚠️ **Important Instruction** > **Question 6 and Question 7 are completely independent**.
> Each question must use a **separate GitHub repository** and **separate workflow**.

---

## **Q3. Implementation Task: Direct Push Trigger on Main Branch**

### **Problem Statement**

Create a program that checks whether a number is **even or odd** and prints the result for multiple test cases.
The program must run automatically using **GitHub Actions when code is pushed directly to the `main` branch**.

### **Requirements**

1. Create a GitHub repository named:

   ```
   github-actions-even-odd
   ```

2. Write the program in **any programming language**
3. Create a GitHub Actions workflow that:

   - Triggers on `push` to `main`
   - Sets up the required runtime
   - Executes the program

4. Push code directly to `main` and verify:

   - Workflow runs successfully
   - Output appears in workflow logs

📌 **Submission**

- Repository link
- Screenshot of successful workflow run

---

## **Q4. Implementation Task: Feature Branch → Pull Request → Main Branch Trigger**

### **Problem Statement**

Create a program that **counts vowels in given words** and automate its execution using **GitHub Actions**, while demonstrating **branch-specific trigger behavior**.

### **Requirements**

1. Create a new GitHub repository named:

   ```
   github-actions-pr-workflow
   ```

2. Create a **feature branch**:

   ```
   feature/vowel-check
   ```

3. In the feature branch:

   - Write a program (any language) that counts vowels in multiple words
   - Commit and push the code to the feature branch

4. Ensure your GitHub Actions workflow is configured to:

   ```yaml
   on:
     push:
       branches:
         - main
   ```

5. Observe and confirm:

   - ❌ Pushing code to `feature/vowel-check` **does NOT trigger** GitHub Actions

6. Raise a **Pull Request** from `feature/vowel-check` to `main`
7. Merge the Pull Request into `main`
8. Observe and confirm:

   - ✅ Merging into `main` **triggers GitHub Actions**
   - Console output is visible in workflow logs

📌 **What to Observe & Report**

- Feature branch push → **No workflow run**
- Merge into `main` → **Workflow runs**

📌 **Submission**

- Repository link
- Screenshot of:

  - Feature branch push (no workflow run)
  - Workflow run after merge into `main`
  - Workflow logs showing vowel count output

---
