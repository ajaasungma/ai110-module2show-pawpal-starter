# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- **Briefly describe your initial UML design.**
The initial design focuses on an object-oriented approach to manage pet care routines dynamically with responsibilities separated across 4 classes.

- **What classes did you include, and what responsibilities did you assign to each?**
Included 4 classes:
* **Owner:** It holds user profile information and manages a collection of pets and overall schedules.
* **Pet:** Encapsulates core pet profiles like name, species, age, and special care notes.
* **Task:** It acts as a pure data container tracking the activity name, time required (duration), urgency (priority), and status.
* **Scheduler:** It takes a pool of tasks and an owner's total time budget constraint to sort, filter, and produce an optimized daily agenda.

**b. Design changes**

- **Did your design change during implementation?**
Yes, the design changed slightly.

- **If yes, describe at least one change and why you made it.**
I added explicit `start_time_str` and `frequency` attributes to the `Task` class. This change was necessary so the scheduler could sort tasks chronologically and automatically calculate the next due date for recurring tasks.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- **What constraints does your scheduler consider (for example: time, priority, preferences)?**
The scheduler considers the maximum daily time budget (in minutes), the urgency priority tier (High, Medium, Low), and exact start times.

- **How did you decide which constraints mattered most?**
I decided that the overall time budget and task priorities mattered most. If an owner only has 60 minutes, high-priority care tasks must happen first, even if lower-priority tasks get left out.

**b. Tradeoffs**

- **Describe one tradeoff your scheduler makes.**
The conflict engine flags exact starting time overlaps but does not calculate full mathematical calendar collisions for overlapping durations.

- **Why is that tradeoff reasonable for this scenario?**
This tradeoff is reasonable because pet owners usually schedule tasks at specific block times (like 08:00 or 12:00) rather than back-to-back continuous minutes. It keeps the code simple and easy to read.

---

## 3. AI Collaboration

**a. How you used AI**

- **How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?**
I used AI to brainstorm the initial class structure, generate the Mermaid UML code, write basic code skeletons, and draft unit tests.

- **What kinds of prompts or questions were most helpful?**
Prompts that asked for specific, simple solutions were best, such as: *"How can I sort a list of tasks by a string time formatted as HH:MM using a lambda key?"*

**b. Judgment and verification**

- **Describe one moment where you did not accept an AI suggestion as-is.**
The AI suggested using a complex calendar library and datetime formatting to calculate conflicts. I rejected it because it made the code messy.

- **How did you evaluate or verify what the AI suggested?**
I evaluated it by testing a simpler solution using string manipulation and raw minutes from midnight. It proved that basic arithmetic was enough for this small app.

---

## 4. Testing and Verification

**a. What you tested**

- **What behaviors did you test?**
I tested task completion status changes, adding tasks to a pet, sorting tasks from morning to night, and finding duplicate time conflicts.

- **Why were these tests important?**
These tests were important to ensure that the app’s logic actually worked behind the scenes without crashing the visual Streamlit interface.

**b. Confidence**

- **How confident are you that your scheduler works correctly?**
I am highly confident because all core scenarios pass our automated test suite cleanly.

- **What edge cases would you test next if you had more time?**
If I had more time, I would test leap years for recurring tasks and invalid time string inputs (like letters instead of numbers).

---

## 5. Reflection

**a. What went well**

- **What part of this project are you most satisfied with?**
I am most satisfied with how cleanly the backend logic transfers data directly into the visual Streamlit tables and alerts.

**b. What you would improve**

- **If you had another iteration, what would you improve or redesign?**
I would add a toggle button in the UI to let users easily delete tasks or manually edit details after adding them.

**c. Key takeaway**

- **What is one important thing you learned about designing systems or working with AI on this project?**
I learned that the human developer must always act as the lead architect. AI can write code quickly, but you must keep it simple and keep it under control.