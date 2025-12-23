### **Q1. When should you use `git restore --staged file.txt`?**

(Write 2–3 lines explaining the correct scenario.)

---

### **Q2. Why is it unsafe to use `git commit --amend` after pushing your commit to a shared remote?**

(Explain in one short paragraph.)

---

### **Q3. You edited `home.js`, `nav.js`, and `styles.css`.**

- You want to discard changes only in `nav.js` but keep edits in other files.
  Write the exact Git command(s).

---

### **Q4. You accidentally staged 10 files using `git add .`, but you want to unstage all of them without deleting your actual edits.**

- Write the command(s) to fix this.

---

### **Q5. Complete the following workflow:**

1. Modify `dashboard.js`
2. Stage the file
3. Realize you need to change the commit message of your last commit
4. Fix the commit message to: **"Update dashboard logic"**
5. Add a missing file `auth.js` into that same commit

Write all the commands in order.

---

### **Q6. Full Workflow: Create, Commit, Modify, Restore**

**Task:**
Perform the following steps with exact Git commands:

1. Create a new file named **profile.js**
2. Add a simple console log inside it
3. Stage and commit it with message **"Add profile module"**
4. Modify the file by adding another console log
5. Decide you want to discard the new changes and return the file to the last committed version
6. Write all the Git commands in order

---

### **Q7. Workflow with Unstage + Amend**

**Task:**
Follow these steps and write all required commands:

1. Create a file **settings.js**
2. Add some settings-related code
3. Stage the file
4. Realize you staged it too early and need to edit it again — unstage the file
5. Make additional edits
6. Stage it again and commit
7. Immediately realize the commit message is wrong — update the commit message to **"Add settings file"**
8. Add a missing file **defaults.js** into the same commit using amend

Write the full sequence of Git commands from start to finish.
