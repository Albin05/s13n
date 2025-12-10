# PM - 1.4: Identify Underlying Needs (Beyond What Users Say)

# **Editorials.md**

## **Q1. Distinguish between a user’s stated need and the underlying need in this quote: “I just want a faster report export.”**

### **Problem Description**

Learners must interpret the quote and explain what the stated request is and what the likely underlying needs (motivations, anxieties, constraints) might be. This tests whether the learner can move from surface-level requests to root causes.

### **Objective**

To evaluate whether learners can **extract underlying needs** from a simple user statement and articulate possible hypotheses that explain the behaviour.

### **Hint**

Ask “why” multiple times, look for evidence of context (deadlines, trust, workflows), and consider emotional or social drivers beyond speed.

### **Short Explanation**

Stated need = “faster report export.” Underlying needs could include reliability, predictability, meeting deadlines, or avoiding manual workarounds.

### **Detailed Explanation**

A direct interpretation of the quote focuses on performance: reduce export latency. A deeper analysis looks at why the user wants speed:

- **Functional need:** They must deliver reports quickly to stakeholders (deadline pressure).
- **Trust/Quality need:** Current exports may fail intermittently, leading users to retry or use manual alternatives—so perceived reliability matters.
- **Workflow need:** Exporting might be part of a longer manual process; speed matters only if it removes manual steps.
- **Emotional/social need:** The user may feel judged if reports are late, motivating a desire for faster exports.

A robust response should articulate at least two plausible underlying needs, explain why they might be true, and suggest ways to validate them (e.g., ask about frequency of exports, observe workflow, check error logs).

### **Constraints / Edge Cases**

- The user might be conflating causes: “faster” could be shorthand for “less error-prone.”
- Not every speed complaint requires engineering: sometimes UX clarifications or retry indicators fix perception.
- Avoid overgeneralizing from one quote—use it as a hypothesis to validate.

---

## **Q2. Given this interview transcript excerpt, identify symptoms, likely root causes, and two follow-up questions you would ask.**

**Transcript excerpt:** “I usually download spreadsheets and then manually copy rows into another tool. It’s annoying, but it’s faster than waiting for the app.”

### **Problem Description**

Learners must parse a real-world excerpt: classify observed behaviours (symptoms), propose root causes, and craft targeted follow-ups to verify hypotheses.

### **Objective**

To assess learners’ ability to **map behaviour → symptom → root cause** and design effective follow-up questions.

### **Hint**

Look for workarounds (manual copy), emotional cues (“annoying”), and assumptions about speed (“faster than waiting for the app”).

### **Short Explanation**

Symptom: manual copying; Root causes: performance, export reliability, integration gaps, or poor automation; Follow-ups should probe frequency, impact, and alternatives.

### **Detailed Explanation**

**Symptoms identified:**

- Repeated manual copying suggests the product does not support a smooth export-to-tool integration.
- The user prefers manual steps despite extra effort, indicating trust or perception issues.

**Possible root causes:**

1. **Performance or reliability:** Exports may be slow or fail, so manual steps are faster in practice.
2. **Missing integration:** The product lacks a direct integration with the user’s downstream tool.
3. **Poor UX for data transfer:** Export format or labeling may require cleaning before import, so copying is easier.

**Follow-up questions (two examples):**

1. “How often do you export and copy data — daily, weekly?” (validates frequency and impact)
2. “What would happen if export was instant but required a cleanup step — would you still use it?” (tests whether speed alone solves the problem or whether format/cleanup is the blocker)

**Validation methods:** analytics for export frequency, session replay for export flows, and a quick usability test of the export/import flow.

### **Constraints / Edge Cases**

- Users sometimes rationalize workarounds; observed behaviour is more reliable than stated reasons.
- One-off issues (a single outage) may produce persistent workarounds; confirm if the behaviour is habitual.

---

## **Q3. Create a short research plan (3–4 steps) to validate an underlying need you hypothesised from a support ticket that says: “Reports keep failing; I have to manually recompute them.”**

### **Problem Description**

Learners must propose a compact, actionable plan to validate the hypothesis that the user’s underlying need is reliability and predictable automation.

### **Objective**

To test the learner’s ability to design **practical validation steps** that move from hypothesis to evidence.

### **Hint**

Combine qualitative & quantitative methods; think about low-effort experiments and observable metrics.

### **Short Explanation**

A good plan mixes data review, targeted interviews, lightweight experiments, and metrics monitoring.

### **Detailed Explanation**

**Hypothesis:** The user’s underlying need is a *reliable, automated reporting pipeline* rather than occasional speed improvements.

**3–4 step research plan:**

1. **Log & analytics check (quantitative):** Analyze export/failure logs for frequency, error types, and affected user segments. Metric: failure rate (%) over past 30 days.
2. **Targeted follow-up interviews (qualitative):** Interview 5–8 users who reported failures to discover the impact, workarounds, and acceptable tolerances. Questions: “When a report fails, what do you do next?” and “How does it affect your work?”
3. **Session replay + workflow observation:** Watch a handful of sessions when users perform exports to observe actual retries, time taken, and alternate flows.
4. **Small experiment / alert improvement (quick win):** Implement an interim fix (e.g., clearer error message with retry guidance or scheduled retry) for a subset and measure if manual recomputation drops. Metric: manual recomputation events per user per week.

**Expected outcomes:** Confirm whether failure frequency or nature (e.g., timeout vs. formatting error) drives recomputation; quantify the impact; identify which fix (engineering vs. UX) is appropriate.

### **Constraints / Edge Cases**

- Data access limitations may delay log analysis.
- Users may have different downstream workflows—one-size-fits-all automation may not apply.

---

# **Info.md**

## **Pre-Read & Lecture Notes Duration**

| Item | Duration |
| --- | --- |
| Pre-Read | 15 minutes |
| Lecture Notes | 25 minutes |

---

## **Assignment Problems Duration Table**

| Problem Code | Duration to Solve | Difficulty | Prerequisite LOs | Bloom Tag |
| --- | --- | --- | --- | --- |
| Q1 | 10 minutes | Low | LO-1.1 | Understand |
| Q2 | 20 minutes | Medium | LO-1.3 | Analyze |
| Q3 | 25 minutes | Medium–High | LO-1.3, LO-1.4 | Apply |

> Note: "Prerequisite LOs" refer to earlier discovery & interview LOs (e.g., designing interview questions and JTBD basics).
> 

---

# **Pre Read.md**

Users frequently express surface-level requests that mask deeper motivations. Recognizing underlying needs prevents misdirected engineering effort and leads to solutions that reduce user friction and produce real impact.

**Key concepts to read briefly (15 mins):**

- Symptom vs. root cause distinction (5 mins)
- Common drivers of behaviour: functional, emotional, social, contextual (5 mins)
- Quick frameworks: 5 Whys, JTBD forces, behaviour traceback (5 mins)

**Examples:**

- Stated: “I need more filters.”
    
    Underlying: users can’t find results due to poor search ranking → they need discoverability and relevance.
    
- Stated: “Make onboarding faster.”
    
    Underlying: users are uncertain about next steps → they need clearer cues and progressive disclosure.
    

**Illustration (description only):**

*Diagram: user quote → observed behaviour → hypothesis → validation method.*

**Suggested short reads/videos:**

- Article on Jobs-to-be-Done basics
- Video: “How to ask follow-ups that reveal real needs”

---

# **Lecture Script.md**

---

## **Topic 1: Introduction — Why Stated Wants Can Mislead**

Start with a real-world anecdote: a team built a “speed” improvement, but adoption didn’t change because the real issue was trust/formatting.

Explain the cost of solving symptoms: wasted dev cycles, frustrated users, and missed opportunities.

**Talking points**

- People often state immediate desires (speed, filters) that are proxies for deeper needs.
- Distinguish between **what** users ask for and **why** they ask for it.

**Expected Duration:** 6 minutes

**Visual aid (description only):**

*Flowchart: User quote → Possible interpretations → Validation step*

---

## **Topic 2: Four Lenses to Interpret Behaviour (Functional, Emotional, Social, Contextual)**

Explain each lens with examples:

- **Functional:** What job do they want to complete? (e.g., export reports)
- **Emotional:** How do they feel? (e.g., anxious, confident, embarrassed)
- **Social:** How do peer expectations or reporting structures influence behaviour? (e.g., manager scrutiny)
- **Contextual:** Environmental constraints (internet, device, workflow).

**Interactive prompt:** Give learners 2 quotes and ask them to identify which lens is likely dominant.

**Expected Duration:** 10 minutes

---

## **Topic 3: Frameworks & Techniques to Discover Underlying Needs**

Cover practical techniques with examples and scripts:

1. **5 Whys** — demonstrate on a short quote.
2. **JTBD forces map** — show pushes, pulls, anxieties, habits.
3. **Behaviour Traceback** — start from what the user does (e.g., manual copy) and trace backward to find triggers.
4. **Hypothesis + Validation Matrix** — quick mapping of assumptions to evidence-gathering methods.

**Demo activity:** Walk through a 5-Why on the “faster export” quote.

**Expected Duration:** 15 minutes

---

## **Topic 4: Writing Non-leading Follow-ups to Validate Hypotheses**

Show phrasing examples:

- Poor: “So you want a faster export because the app is slow, right?”
- Better: “Can you walk me through the last time you exported a report?”
- Best: “When you export reports, what happens next in your workflow?”

**Practice:** Pair activity — convert 5 leading questions into open follow-ups.

**Expected Duration:** 10 minutes

---

## **Topic 5: Designing Lightweight Validation Plans**

Teach a 3-step validation approach: observe → interview → quick experiment.

- **Observe:** Logs, session replay, analytics
- **Interview:** targeted follow-ups focusing on frequency, impact, and alternatives
- **Experiment:** small UX fix or flag for engineering to test changes

**Example plan:** verify whether export failures cause recomputation (see Editorials Q3).

**Expected Duration:** 12 minutes

---

# **Lecture Notes.md**

- **Core idea:** Users’ stated wants often mask deeper needs; identify and validate those before building.
- **Symptom vs. root cause:** Symptoms are user actions/complaints; root causes are motivations or constraints.
- **Four interpretive lenses:** functional, emotional, social, contextual.
- **Key methods:** 5 Whys, JTBD forces, behaviour traceback, hypothesis-validation matrix.
- **Follow-up question style:** open, non-leading, context-focused (“Tell me about the last time…”, “What did you do next?”).
- **Data sources for validation:** logs (failure/error rates), analytics (event funnels), session replays, targeted interviews.
- **Validation heuristics:** gather at least 3 independent signals before deciding.
- **Quick wins:** sometimes UX/feedback adjustments change behaviour without heavy engineering (e.g., clearer error messaging, progress indicators).

**Illustration (description only):**

*A multi-row table mapping typical stated needs → likely underlying needs → validation methods.*

---

# **Post-class Quiz.md**

### **Q1. Which question is the best open-ended follow-up to discover an underlying need?**

A. “So the export is slow, right?”

B. “Can you describe the last time you exported a report and what happened next?”

C. “Would a faster export solve it?”

D. “How much faster in seconds do you want the export to be?”

E. Topic not covered in class

**Correct Answer:** B

---

### **Q2. A user says they prefer downloading CSVs and manually cleaning them. Which of the following is the strongest hypothesis?**

A. They dislike the CSV format.

B. They don't trust automated exports.

C. They want more filters.

D. They like manual work.

E. Topic not covered in class

**Correct Answer:** B

---

### **Q3. You observe a recurring manual recomputation event in analytics. What should you do first?**

A. Immediately increase server capacity.

B. Interview affected users to understand why recomputation happens.

C. Remove the export feature.

D. Build an automated recomputation job.

E. Topic not covered in class

**Correct Answer:** B

---

# **Question Bank.md**

### **Bloom: Remember**

1. Define “stated need” vs. “underlying need.”
2. List the four interpretive lenses used to analyze user behaviour.

---

### **Bloom: Understand**

1. Explain why a workaround (e.g., manual copy) is a strong signal of an underlying need.
2. Describe how emotional drivers can affect product adoption.

---

### **Bloom: Apply**

1. Given this quote: “I always open the app twice because it sometimes hangs,” describe three possible underlying needs and how you would begin validating each.
2. Convert the solution request “Add advanced filters” into at least two different problem statements using the problem template (user → goal → obstacle → impact).

---

### **Bloom: Analyze**

1. You find 20 support tickets saying “exports failed.” Analyze what additional quantitative and qualitative data you need to prioritize fixes and explain why.
2. Compare two seemingly similar user complaints and determine how to cluster them into one underlying problem or treat as separate issues.

---

### **Bloom: Evaluate**

1. Evaluate this course of action: “We will add server capacity to make exports faster.” What evidence do you need before approving this technical investment?
2. Given two hypotheses about why users recompute reports (A: exports fail 8% of the time; B: exported format requires post-processing), decide which to pursue first and justify your choice.

---

### **Bloom: Create**

1. Design a 4-step research plan to validate whether users who manually recompute reports do so because of reliability issues or because of integration gaps. Include metrics, interview questions, and a small experiment.
2. Draft five non-leading follow-up questions you would ask in an interview when a user says, “I don’t use the built-in reports — I download and clean them myself.”

---