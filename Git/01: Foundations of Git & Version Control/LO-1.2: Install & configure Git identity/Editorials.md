# Q2. Define what Git is in the context of version control.

## 1. Title

Definition of Git in Version Control

## 2. Problem Description

Students must provide a clear definition of Git and its role within version control systems.

## 3. Objective

To assess understanding of Git as a distributed version control tool.

## 4. Hint

Focus on Git as software that tracks and manages changes.

## 5. Short Explanation

Git is a distributed version control system that tracks file changes and supports collaboration.

## 6. Detailed Explanation

Git is an open-source distributed version control system designed to track changes in source code during software development.
Key characteristics:

- Stores full repository copies on every machine
- Tracks history of changes through commits
- Allows multiple developers to work in parallel
- Supports branching, merging, and reverting changes

Git ensures safe collaboration and maintains complete version history.

## 7. Constraints / Edge Cases

Definition should address _what Git is_ and _its purpose_, not GitHub.

---

# Q3. Describe the main difference between Git and GitHub.

## 1. Title

Difference Between Git and GitHub

## 2. Problem Description

Students must explain how Git and GitHub differ in purpose.

## 3. Objective

To ensure understanding of tool vs. platform distinctions.

## 4. Hint

One is a local version control tool; one is an online hosting platform.

## 5. Short Explanation

Git is a version control system; GitHub is a cloud platform for hosting Git repositories.

## 6. Detailed Explanation

Git is software installed on a computer that manages version history, commits, branches, and merges locally.
GitHub is a web-based service that stores Git repositories online, enabling features like:

- Remote backup
- Pull requests
- Issue tracking
- Team collaboration

Thus, Git handles version control, while GitHub provides cloud-based repository hosting and collaboration tools.

## 7. Constraints / Edge Cases

Students must differentiate purpose, not just functionality.

---

# Q4. Summarise why having the same name and email in Git and GitHub matters.

## 1. Title

Importance of Matching Git and GitHub Identity

## 2. Problem Description

Students must explain why Git’s local identity should match GitHub’s profile.

## 3. Objective

To understand identity mapping between local commits and GitHub contributions.

## 4. Hint

Think about commit authorship and contribution tracking.

## 5. Short Explanation

Matching identity ensures commits appear under the correct GitHub user.

## 6. Detailed Explanation

Git uses the local username and email configured through:

```
git config --global user.name
git config --global user.email
```

GitHub identifies commit authors based on email.
If Git’s email does not match GitHub’s verified email:

- Commits show as “Unknown Author”
- Contributions do not appear in activity graphs
- Ownership of commits becomes unclear

Matching identity ensures proper attribution and transparency.

## 7. Constraints / Edge Cases

GitHub requires the email to be verified on the account.

---

# Q5. Differentiate between centralized and distributed version control systems with one real-world advantage of each.

## 1. Title

Comparison of Centralized vs Distributed VCS

## 2. Problem Description

Students must explain differences and advantages of each model.

## 3. Objective

To analyse VCS architectures.

## 4. Hint

Think about where history is stored and how teams work.

## 5. Short Explanation

Centralized VCS has one main server; Distributed VCS stores full copies on every machine.

## 6. Detailed Explanation

Centralized VCS (e.g., SVN):

- All version history is stored on a central server
- Developers must stay connected to commit or update
- Advantage: Simple and easy to manage in small teams

Distributed VCS (e.g., Git):

- Every developer has a full copy of the repository
- Supports offline work and faster operations
- Advantage: No single point of failure; safer and more flexible

This architectural difference affects speed, reliability, and workflow.

## 7. Constraints / Edge Cases

Comparison must include _one advantage for each_.

---

# Q6. GitHub requires internet while Git does not. Evaluate whether it is still necessary to use GitHub in a software team and justify your answer.

## 1. Title

Importance of GitHub in Team Collaboration

## 2. Problem Description

Students must evaluate GitHub’s role despite Git's offline capability.

## 3. Objective

To judge the necessity of GitHub in modern team workflows.

## 4. Hint

Think collaboration, backup, and workflow management.

## 5. Short Explanation

Yes, GitHub is still necessary because it enables cloud-based collaboration and centralized repository access.

## 6. Detailed Explanation

While Git works offline and manages code locally, GitHub adds essential teamwork features:

- Central repository accessible by the entire team
- Pull requests for code review
- Issue tracking and project management tools
- Cloud backups preventing data loss
- Seamless CI/CD integrations (Actions, Pipelines)

Teams benefit from transparency, shared access, and coordinated development workflows.
Thus, GitHub remains essential even though Git does not require internet.

## 7. Constraints / Edge Cases

Students may argue optionality for solo developers, but must still justify.

---

# Q7. You installed Git but commits show “Unknown Author” in GitHub. Apply your knowledge to solve the issue.

## 1. Title

Fixing Unknown Author Issue in Git Commits

## 2. Problem Description

Students must apply Git configuration knowledge to fix author identity problems.

## 3. Objective

To test practical usage of Git identity configuration.

## 4. Hint

Think about `git config` commands.

## 5. Short Explanation

Configure name and email using global Git config commands.

## 6. Detailed Explanation

The “Unknown Author” issue occurs when Git lacks valid user identity settings or when the email doesn't match a verified GitHub email.

To fix:

```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

Then verify:

```
git config --global --list
```

Ensure the email matches one added and verified in GitHub.
After this, future commits correctly map to the GitHub user.

## 7. Constraints / Edge Cases

Past commits will not update automatically—students should understand identity affects only future commits.

---
