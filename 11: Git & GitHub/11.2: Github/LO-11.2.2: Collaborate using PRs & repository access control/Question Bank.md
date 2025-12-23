
### **Q1. What is the purpose of setting an upstream branch using `git push -u`?**

(Answer in 2–3 lines.)

---

### **Q2. Explain the difference between `git fetch` and `git pull`. Why is `fetch` considered safer?**

(Answer briefly.)

---

## **Implementation-Based Questions (Submission Required)**

> ⚠️ **Submission Instruction (for Q6, Q7, Q8):**
> Submit the **GitHub repository link** showing commit history, branches, and merged Pull Requests.

---

### **Q3. Local to Remote Workflow (First Push)**

**Task:**
Perform the following steps and submit the repository link:

1. Create a new local repository named **remote-demo**
2. Create a file **README.md** and add some content
3. Commit the file with message **"Initial commit"**
4. Create a remote repository on GitHub
5. Connect the local repository to GitHub using `origin`
6. Push the code to GitHub and set the upstream branch

**Expected Evidence:**

- GitHub repo exists
- `main` branch contains at least one commit

---

### **Q4. Feature Branch → Push → Pull Request → Merge**

**Task:**
Using the repository from Q6, perform the following:

1. Clone the repository (if not already cloned)
2. Create a new branch named **feature-update**
3. Modify **README.md** by adding more content
4. Commit the changes with a meaningful message
5. Push the branch to GitHub
6. Raise a Pull Request from **feature-update → main**
7. Merge the Pull Request
8. Delete the feature branch after merge

**Submission:**

- GitHub repository link
- Pull Request must be visible and merged

---

### **Q5. Collaboration Workflow with Pull Requests**

**Task:**
Perform **one of the following two approaches** (based on availability):

---

#### **Option A: With Collaborator (Preferred)**

1. Add a collaborator to your GitHub repository (Write access)
2. Collaborator clones the repository
3. Collaborator creates a new branch **collab-feature**
4. Collaborator adds a file **collab.txt**, commits, and pushes
5. Collaborator raises a Pull Request to `main`
6. You review and merge the collaborator’s Pull Request

---

#### **Option B: Solo Simulation (If No Collaborator Available)**

1. Create a new branch **collab-feature**
2. Add a file **collab.txt** and commit changes
3. Push the branch to GitHub
4. Raise a Pull Request from **collab-feature → main**
5. Merge the Pull Request yourself

---

**Submission:**

- GitHub repository link
- At least one merged Pull Request must be visible
