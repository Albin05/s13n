## 1. Tools Available for Source Code Management

Software teams need tools to manage changing code.
Several tools are used in the industry:

| Tool Name          | Description                                  | Nature of System  |
| ------------------ | -------------------------------------------- | ----------------- |
| SVN (Subversion)   | Single central repository for the whole team | Centralized       |
| Perforce           | Enterprise-scale repository system           | Centralized       |
| Mercurial          | Distributed system similar to Git            | Distributed       |
| Git                | Distributed, fast, widely adopted versioning | Distributed       |
| Azure DevOps / TFS | Microsoft ecosystem for repo + project mgmt  | Centralized/Cloud |

While multiple tools exist, real-world usage shows a clear preference.

---

## 2. Why Git is Most Widely Used

Git became the industry standard for the following reasons:

* Works even **without internet**
* Every developer has a **full copy of history**
* Operations like commits and comparisons are **very fast**
* Branching and merging support is **strong**
* More secure with **built-in integrity checks**
* Large open-source ecosystem and community adoption
* Integrates with cloud services like GitHub, GitLab, Bitbucket

Git allows safe experimentation and easy teamwork for any scale of project.

---

## 3. What is Git?
![Git](https://git-scm.com/images/logos/logomark-orange@2x.png)

Git is a **local command-line tool** used for:

* Tracking every change in a project
* Recording versions through commits
* Creating branches to try new ideas safely
* Merging contributions in a structured way

Git manages version control on **your machine**.

---

## 4. What is GitHub?
<image src='https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png' width="300px" >

GitHub is a **cloud platform** that stores repositories online and enables teamwork.

Purpose:

* Backup of your project on the server
* Collaboration with teammates
* Pull requests, code review, issue tracking, and CI/CD
* Display contribution history on developer profiles

| Aspect           | Git                        | GitHub                  |
| ---------------- | -------------------------- | ----------------------- |
| Runs where?      | Local system               | Cloud website           |
| Internet needed? | No                         | Yes                     |
| Purpose          | Version history management | Collaboration + Hosting |

Git works independently.
GitHub enhances Git for team use.

---

## 5. Create GitHub Account (Before Git Setup)

Students must create their profile using:

* Full **professional name**
* Same email to be used in Git config

Reason:
Commit authorship must match GitHub identity, otherwise contributions may not reflect properly.

Steps:
[Signup In Git](https://github.com/signup)
* Sign up on GitHub official website
* Verify email
* Choose a clear username (prefer full name if available)

---

## 6. Install Git

Install Git on your operating system.

### Windows

* Download installer from official Git website
* Proceed with **default recommended** options
* Git Bash terminal will be installed

### macOS

Using Homebrew:

```bash
brew install git
```

Or:

```bash
xcode-select --install
```

### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install git
```

Verify installation:

```bash
git --version
```

![Git Version](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/ee796583-5e7f-48c7-86d6-585278c363f2/CGnV2pb3SKxRvGEh.png)

---

## 7. Basic Git Setup (After GitHub Account)

Configure Git to match your GitHub identity:

```bash
git config --global user.name "Exact GitHub Name"
git config --global user.email "YourGitHubEmail@example.com"
```

Check saved settings:

```bash
git config --list
```

Why required?

| Without Setup               | With Setup                              |
| --------------------------- | --------------------------------------- |
| Commits show unknown author | Profile contributions counted correctly |
| Confusion in team tracking  | Clear ownership                         |
| Harder debugging history    | Proper accountability                   |

This setup is mandatory even for **local-only work**.

---




