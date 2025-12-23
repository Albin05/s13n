## 1. **Set Context — Why This Topic Is Critical (3 minutes)**

- “Open the same GitHub repository we’ve been using.”
- “Keep the **Actions** tab and **Pull Requests** tab visible.”

**Say clearly:**

> “We now have CI pipelines running automatically.”

Pause and ask the class:

> “But here’s a serious question —
> what stops someone from merging broken code anyway?”

---

**Explain the gap:**

> “CI alone only _reports_ problems.
> It does **not stop humans from ignoring them**.”

Transition line (important):

> “This is why **Branch Protection** exists.”

---

## 2. **Why Branch Protection Is Needed (4 minutes)**

Explain with real project behavior:

- Multiple developers
- Different experience levels
- Time pressure
- Deadlines

Say firmly:

> “Without rules, quality depends on discipline.
> Discipline always breaks under pressure.”

---

### Problems Without Branch Protection

Explain one by one:

- Direct pushes to `main`
- CI failures ignored
- Bugs reach shared branch
- Entire team affected

Say clearly:

> “Branch protection moves responsibility
> from _people_ to _systems_.”

---

## 3. **What Is Branch Protection? (3 minutes)**

Explain conceptually first:

> “Branch Protection is a **repository-level rule system**.”

What it does:

- Protects important branches (`main`)
- Enforces PR-based workflow
- Forces CI checks to pass

---

**Key statement (say slowly):**

> “Branch protection converts CI
> from **advice** into **law**.”

---

## 4. **What Is CI Enforcement? (3 minutes)**

Explain in simple terms:

> “CI Enforcement means:
> _You cannot merge unless automation says OK_.”

Explain outcomes:

- Main branch always stable
- No accidental merges
- No shortcuts

---

**Important mindset shift:**

> “With enforcement, speed never beats quality.”

---

## 5. **Typical Failure Without Branch Protection (3 minutes)**

Tell a short story:

> “CI fails.
> Developer clicks _Merge anyway_.
> Broken code enters `main`.
> Everyone pulls broken code.”

Pause.

Say firmly:

> “CI/CD becomes meaningless without enforcement.”

---

## 6. **Common Branch Protection Rules (5 minutes)**

### Explain Before Showing UI

> “GitHub lets us enforce multiple rules.
> We don’t need all of them — just the right ones.”

---

### **Rule 1 — Require Pull Request Before Merging**

Explain:

- Blocks direct push to `main`
- All changes go through PRs

Say:

> “This rule alone eliminates 80% of mistakes.”

---

### **Rule 2 — Require Status Checks to Pass**

Explain:

- CI must succeed
- Merge button stays disabled if CI fails

Say clearly:

> “This is the most important rule.”

---

### **Rule 3 — Require Branch to Be Up to Date (Optional)**

Explain briefly:

- Ensures latest `main`
- Avoids outdated merges

---

**Teaching recommendation:**

> “For students, rules 1 and 2 are mandatory.
> Others are optional.”

---

## 7. **How Branch Protection Works with GitHub Actions (4 minutes)**

Explain the flow slowly:

1. PR opened
2. GitHub Actions runs CI
3. CI reports pass/fail
4. Branch protection checks result
5. Merge allowed only if pass

---

**Important clarification:**

> “Branch protection does **not run CI**.
> It only **enforces CI results**.”

---

## 8. **Live Setup — Branch Protection (Step-by-Step) (8 minutes)**

### **Step 1 — Open Branch Settings**

- Repository → **Settings**
- Click **Branches**

Say:

> “All enforcement rules live here.”

---

### **Step 2 — Add Rule**

- Click **Add branch protection rule**
- Branch name pattern:

```
main
```

Explain:

> “This applies rules only to `main`.”

---

### **Step 3 — Enable Core Rules**

Tick these options (explain each as you click):

- ✅ Require a pull request before merging
- ✅ Require status checks to pass before merging

Select the CI workflow:

- (JS batch) → `JS Palindrome Check`
- (Python batch) → `Python CI`

(Optional):

- ✅ Require branch to be up to date

Click **Save**.

---

## 9. **What Changes After Enabling Protection? (4 minutes)**

Explain clearly:

- Direct push to `main` ❌ blocked
- Merge button disabled ❌
- CI must pass ✅

Say:

> “There is no override button.
> GitHub enforces this strictly.”

---

## 10. **Understanding Required Status Checks (4 minutes)**

Explain carefully:

> “A status check is the **result of a CI job**.”

Important rules:

- Fail → merge blocked
- Skipped → merge blocked
- Not run → merge blocked

Say clearly:

> “Only a green check allows merge.”

---

## 11. **CI Enforcement via Pull Requests (5 minutes)**

Walk through standard workflow verbally:

1. Create feature branch
2. Push changes
3. Open PR to `main`
4. CI runs automatically
5. Fix issues if CI fails
6. Merge only after success

Say:

> “This is not optional.
> This is **industry standard**.”

---

## 12. **What Happens When CI Fails? (4 minutes)**

Explain PR behavior:

- ❌ shown on PR
- Merge disabled
- Error logs visible

Developer must:

- Fix code
- Push again
- CI reruns automatically

Say clearly:

> “You don’t negotiate with CI.
> You satisfy it.”

---

## 13. **Branch Protection with Secrets & Env Variables (3 minutes)**

Explain connection:

> “If a required secret is missing,
> CI fails.”

Result:

- Merge blocked
- Insecure or incomplete setup prevented

Say:

> “Branch protection protects not just code,
> but **configuration security**.”

---

## 14. **Common Beginner Mistakes (3 minutes)**

Explain each briefly:

- CI enabled but not enforced ❌
- Direct push to `main` ❌
- Ignoring failed checks ❌
- Forgetting required status checks ❌
- Trusting local testing only ❌

Say:

> “Branch protection removes human error by design.”

---

## 15. **When Branch Protection Must Be Used (Final Emphasis – 3 minutes)**

Say firmly:

> “If more than one person works on a repo —
> branch protection is mandatory.”

> “If CI exists —
> enforcement must exist.”

---
