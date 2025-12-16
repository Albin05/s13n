# **Undoing Working Directory Changes — `git restore` (3 minutes)**

“Sometimes you make edits you didn’t intend, or you break something and want to go back to the last clean version. Git allows you to safely discard uncommitted changes without affecting your work history.”

“Before we start, modify a file. Open `app.js`, add some random text, and save it.”

“Check what Git sees:”

```bash
git status
```

“You should see `modified: app.js`.
Now watch what happens when we restore it back to the last committed version.”

```bash
git restore app.js
```

“Open the file again — everything is back to the committed state.
That’s how you safely throw away unwanted edits.”

---

### **Now repeat the same flow with two more examples (5 minutes)**

**Example 2 — Another Single File**

1. “Open `index.html`, make an obvious change, save it.”

2. “Run `git status` to see the modification.”

3. “Undo it using:”

   ```bash
   git restore index.html
   ```

4. “Verify the file is back to normal.”

---

**Example 3 — Restore Entire Project**

1. “Modify _two_ different files in the project.”

2. “Run `git status`.”

3. “Now restore everything at once:”

   ```bash
   git restore .
   ```

4. “Observe that all local edits are gone.”

---

# **Unstaging Changes — `git reset` or `git restore --staged` (3 minutes)**

“There are times you add files to staging that shouldn’t be part of the next commit. Git lets you pull them back safely without losing the changes.”

“Let’s try it together. Edit `config.js`, save it, and stage it:”

```bash
git add config.js
```

“Check its status:”

```bash
git status
```

“It’s staged. Now unstage it while keeping the edits intact:”

```bash
git reset config.js
```

OR

```bash
git restore --staged config.js
```

“Run `git status` again — notice the file is now only modified, not staged.”

---

### **Repeat same flow with two more examples (5 minutes)**

**Example 2 — Using reset**

1. “Edit `styles.css`. Save it.”

2. “Stage it: `git add styles.css`”

3. “Unstage it:”

   ```bash
   git reset styles.css
   ```

4. “Confirm edits are still present.”

---

**Example 3 — Unstage Everything**

1. “Stage a bunch of files together:”

   ```bash
   git add .
   ```

2. “Now remove _all_ files from staging:”

   ```bash
   git reset
   ```

3. “Check with `git status` — everything should be back to modified state.”

---

# **Updating the Last Commit — `git commit --amend` (3 minutes)**

“Sometimes you commit too early—maybe you forgot a file or made a typo in the message. Git lets you update the most recent commit before pushing it.”

“Let’s try this. Make a commit with a deliberate mistake in the message:”

```bash
git commit -m "Addd login page"
```

“Now fix the commit message:”

```bash
git commit --amend -m "Add login page"
```

“Notice the new commit replaces the old one with a corrected message.”

---

### **Adding missing files to the last commit (3 minutes)**

1. “Create or edit `validation.js`.”

2. “Stage it:”

   ```bash
   git add validation.js
   ```

3. “Now update the previous commit contents:”

   ```bash
   git commit --amend
   ```

4. “Explain: this rewrites the last commit with both message and files fixed.”

---

### **Repeat same flow with two more examples (5 minutes)**

**Example 2 — Fix wrong commit message**

1. “Make another commit with a bad message.”
2. “Correct it using:”

   ```bash
   git commit --amend -m "Corrected commit message"
   ```

---

**Example 3 — Add a missing test file**

1. “Create or update `login.test.js`.”
2. “Stage it: `git add login.test.js`”
3. “Amend the previous commit:”

   ```bash
   git commit --amend
   ```

---

# **Closing Demonstration — Choosing the Correct Undo Action (7 minutes)**

“Now we will practice selecting the right command based on the situation.
Follow along with this scenario-based flow.”

### **Scenario A — You want to discard edits**

```bash
git restore <file>
```

### **Scenario B — You staged something accidentally**

```bash
git reset <file>
```

### **Scenario C — You want to fix the last commit**

```bash
git commit --amend
```

After describing each, ask students:

**“Repeat each scenario using different files in your project. You must execute all three flows again with your own examples.”**
