## 1. **Connect With the Previous Topics (3 minutes)**

- “Open the same GitHub repository we’ve been using.”
- “Keep **Issues**, **Project Board**, and **Pull Requests** tabs visible.”

**Say clearly:**

> “So far, we have learned how to **organize work** and **collaborate**:
>
> - Issues define _what_ to do
> - Boards show _where_ the work is
> - Commits and PRs show _what code changed_”

Pause and ask the class:

> “But one very important question is still unanswered.”

---

**State the problem clearly:**

> “How do we know the code being added is:
>
> - correct?
> - not breaking existing features?
> - safe to merge?”

**Transition line (very important):**

> “In real companies, we don’t _trust_ code —
> we **verify it automatically**.”

---

## 2. **Introduce CI/CD (Conceptual – 5 minutes)**

### Explain Before Any Tooling

> “CI/CD is not a tool.
> It is a **practice** supported by automation.”

Write on board / say slowly:

- CI → Continuous Integration
- CD → Continuous Delivery / Deployment

---

### Explain the Core Idea

> “Instead of testing everything at the end,
> we test **every time code changes**.”

Explain outcomes:

- Errors caught early
- Less stress before release
- Teams can work in parallel safely

---

## 3. **Why CI/CD Is Needed (4 minutes)**

### Tell a Realistic Scenario

> “Imagine 5 developers pushing code every day.
> Everyone says — _it works on my machine_.”

Explain what usually happens:

- Bugs appear late
- Debugging becomes expensive
- Confidence drops

---

### CI/CD as a Safety Net

> “CI/CD acts like a **gatekeeper**.
> If something breaks — it stops the code.”

Say clearly:

> “No human discipline can match automation discipline.”

---

## 4. **Continuous Integration (CI) Explained (5 minutes)**

### Explain CI in Simple Language

> “Continuous Integration means:
>
> - Push code frequently
> - Let machines validate it immediately”

Explain what runs automatically:

- Build
- Tests
- Quality checks

---

### Emphasize the Goal

> “The **main branch must always be stable**.”

Explain problems CI prevents:

- Broken builds
- Last-minute surprises
- Long debugging sessions

---

## 5. **Continuous Delivery vs Continuous Deployment (4 minutes)**

### Explain Slowly and Clearly

**Continuous Delivery:**

> “Code is always ready.
> Humans decide _when_ to deploy.”

**Continuous Deployment:**

> “Code deploys automatically after checks pass.”

---

### Teaching Decision

> “For student projects and beginners,
> **Continuous Delivery is the correct choice**.”

Reason:

- Safer
- More control
- Easier to understand

---

## 6. **What Is a CI/CD Pipeline? (5 minutes)**

### Conceptual Explanation

> “A pipeline is a **sequence of automated steps**.”

Explain key rule:

> “If one step fails — the pipeline stops.”

---

### Why Pipelines Matter

- Enforce rules automatically
- Remove human forgetfulness
- Maintain consistency

Say clearly:

> “Pipelines replace assumptions with guarantees.”

---

## 7. **CI/CD in GitHub — GitHub Actions (5 minutes)**

### Introduce the Tool

> “GitHub provides CI/CD using **GitHub Actions**.”

Explain advantages:

- Built into GitHub
- No extra setup tools
- Integrated with PRs and issues

---

### Show the Actions Tab

- Click **Actions** tab in the repository
- Do **not** create workflow yet

Say:

> “This is where automation lives.”

---

## 8. **Triggers — When Does Automation Run? (4 minutes)**

### Explain Triggers Conceptually

> “A trigger decides _when_ the pipeline starts.”

Common triggers:

- Push to a branch
- Open a Pull Request
- Update a Pull Request

---

### Example Explanation

> “You open a PR → pipeline runs
> You push new code → pipeline runs again”

Emphasize:

> “Developers don’t start pipelines.
> **Actions do**.”

---

## 9. **Pipeline Stages Explained Clearly (8 minutes)**

Explain slowly, one stage at a time.

---

### **Stage 1 — Build**

> “First, the project must build.”

Explain tasks:

- Install dependencies
- Compile if needed
- Prepare app

Say clearly:

> “If build fails, nothing else matters.”

---

### **Stage 2 — Test**

> “Now we verify behavior.”

Explain:

- Automated tests
- Logic validation
- Regression protection

Say:

> “Tests answer one question:
> _Does the code do what it should?_”

---

### **Stage 3 — Quality Checks**

> “This stage checks **how the code is written**.”

Examples:

- Linting
- Formatting
- Static analysis

Say clearly:

> “Working code with poor quality
> becomes unmaintainable code.”

---

### **Stage 4 — Deployment (Optional)**

Explain carefully:

- Often skipped in learning
- Focus on CI first
- Deployment can come later

---

## 10. **CI/CD and Pull Requests (5 minutes)**

### Show a Pull Request Page

Explain what happens automatically:

- Pipeline runs
- Checks appear on PR
- Pass / Fail indicators shown

---

### Important Rule

> “If checks fail —
> **the PR must not be merged**.”

Say firmly:

> “This rule protects the entire team.”

---

## 11. **How CI/CD Completes the GitHub Workflow (4 minutes)**

Walk through verbally:

1. Issue defines work
2. Board tracks progress
3. Commit records changes
4. PR reviews code
5. CI/CD validates automatically

Say:

> “Each step reinforces the next.”

---

## 12. **Benefits of CI/CD (3 minutes)**

Summarize verbally:

- Faster feedback
- Fewer bugs
- Consistent standards
- Less manual effort
- Higher confidence

---
