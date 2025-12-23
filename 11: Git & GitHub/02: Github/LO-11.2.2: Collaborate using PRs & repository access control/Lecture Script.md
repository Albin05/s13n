### **1. Introduce the Need for a Remote Repository (3 minutes)**

- Begin by recalling previous sessions:

  - Git manages code locally
  - Collaboration requires a shared location

- State that team collaboration begins only when a **remote repository** exists.
- Explain that a remote repository:

  - Hosts project code centrally
  - Defines ownership
  - Enforces collaboration rules

- Emphasize that:

  - Initially, the repository exists only on GitHub
  - No local machine is connected yet

- Establish the remote repository as the **single source of truth**.

---

### **2. Demonstrate Creating a Remote Repository (Manual Demo – 5 minutes)**

- Open GitHub in the browser.
- Walk through the repository creation process:

  - Repository name
  - Visibility (public/private)
  - Description

- Explain that at this point:

  - The repository exists only on GitHub
  - No code is present locally
  - Access rules are controlled remotely

- Do not connect any local repository yet.

---

### **3. Demonstrate Cloning a Remote Repository (Manual Demo – 5 minutes)**

- Explain that cloning creates a local working copy of the remote repository.
- Demonstrate cloning using a repository URL.
- Highlight what cloning achieves:

  - Project files are downloaded
  - Full commit history is copied
  - A remote named `origin` is automatically configured

- Reinforce that:

  - Developers now work locally
  - The remote remains the shared reference point

---

### **4. Demonstrate Connecting an Existing Local Repository to a Remote (Manual Demo – 5 minutes)**

- Present a scenario where:

  - Project was started locally
  - Remote repository was created later

- Demonstrate linking the local repository to GitHub using:

  - Remote registration

- Explain that this step:

  - Registers the remote
  - Names it `origin` by convention
  - Does not push code automatically

- Clarify that:

  - Local and remote are connected
  - They are not synchronized yet

---

### **5. Demonstrate Pushing Code to the Remote (Manual Demo – 5 minutes)**

- Explain pushing as the act of transferring local commits to the remote.
- Demonstrate pushing the local `main` branch to GitHub.
- Highlight that pushing:

  - Uploads commits
  - Updates the remote branch
  - Makes changes visible to collaborators

- Reinforce that:

  - Pushing is explicit
  - Nothing is shared without intent

---

### **6. Demonstrate Upstream Branch Concept (Manual Demo – 4 minutes)**

- Explain that the first push usually establishes a long-term relationship.
- Demonstrate pushing with upstream configuration.
- Explain that upstream configuration:

  - Links local branch to remote branch
  - Simplifies future push and pull commands

- Emphasize reduced repetition and fewer mistakes in daily workflows.

---

### **7. Demonstrate Pull vs Fetch (Manual Demo – 6 minutes)**

- Introduce the need to receive updates from the remote.
- Demonstrate fetching:

  - Changes are downloaded
  - Local branches remain unchanged

- Explain fetch as a safe inspection step.
- Demonstrate pulling:

  - Changes are fetched
  - Immediately merged into the current branch

- Reinforce the conceptual model:

  - Pull = Fetch + Merge

- Stress that understanding this distinction prevents unintended merges.

---

### **8. Demonstrate Collaboration Using Branches (Manual Demo – 5 minutes)**

- Explain that professional teams do not push directly to `main`.
- Demonstrate:

  - Creating a feature branch
  - Pushing the branch to the remote

- Explain that:

  - Each branch represents isolated work
  - Shared branches remain stable

- Prepare learners for Pull Requests.

---

### **9. Demonstrate Pull Requests (Manual Demo – 7 minutes)**

- Open GitHub and show the Pull Request interface.
- Demonstrate:

  - Selecting source and target branches
  - Writing PR title and description

- Explain that a Pull Request:

  - Requests integration of changes
  - Initiates review and discussion
  - Controls when code is merged

- Conclude the hands-on portion here.
- State clearly:

  - All further concepts will be explained theoretically.

---

## **Theoretical Explanation (No Live Demo from This Point)**

---

### **10. Explain Pull Requests as a Collaboration Contract (4 minutes)**

- Describe Pull Requests as a formal agreement to merge changes.
- Explain that PRs:

  - Document what was changed and why
  - Record discussions permanently
  - Provide approval control

- Emphasize that:

  - PRs exist only on the remote platform
  - Local Git has no concept of PRs

---

### **11. Explain Repository Access Control (5 minutes)**

- Introduce the idea that:

  - A remote repository is a shared resource
  - Not everyone should have full access

- Explain access control as the system that defines:

  - Who can push
  - Who can review
  - Who can merge
  - Who can manage settings

- Emphasize enforcement at the remote level only.

---

### **12. Explain Why Access Control Is Essential (4 minutes)**

- Describe risks without access control:

  - Production breakage
  - Accidental deletions
  - No accountability

- Explain benefits with access control:

  - Protected main branch
  - Mandatory reviews
  - Clear responsibilities

- Reinforce access control as the foundation of safe collaboration.

---

### **13. Explain Role-Based Access Types (5 minutes)**

- Describe GitHub roles conceptually:

  - Read
  - Write
  - Maintain
  - Admin

- Explain that:

  - Each role allows specific actions
  - Restrictions are intentional
  - Risk is minimized through limitation

---

### **14. Explain How Access Control Is Enforced (4 minutes)**

- Explain enforcement logic:

  - Identity check
  - Role validation
  - Action authorization

- Provide conceptual examples:

  - Push blocked due to missing permission
  - Merge blocked due to insufficient role
  - Settings blocked without admin access

---

### **15. Explain Adding and Managing Collaborators (4 minutes)**

- Walk through the collaborator management process conceptually:

  - Invitation
  - Permission assignment
  - Acceptance

- Explain that:

  - Access can be modified or revoked
  - Changes take effect immediately

- Reinforce protection against outdated access.

---

### **16. Explain Access Control Impact on Pull Requests (4 minutes)**

- Explain how permissions influence PRs:

  - Who can open PRs
  - Who can approve
  - Who can merge

- Reinforce separation of:

  - Contribution
  - Decision-making

- Emphasize stability of shared branches.

---

### **17. Walk Through End-to-End Collaboration Flow (3 minutes)**

- Present the complete lifecycle:

  1. Remote repository creation
  2. Role assignment
  3. Cloning
  4. Branch creation
  5. Local commits
  6. Push to remote
  7. Pull Request creation
  8. Review and approval
  9. Merge
  10. Synchronization

- Reinforce governance by remote access rules.

---
