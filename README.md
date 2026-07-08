# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
==================================================
🐾 PAWPAL+ DAILY SCHEDULE FOR ALEX 🐾
⏱️  Time Budget: 75 mins
==================================================
1. ⏳ [High]   Morning Walk (30 mins)
2. ⏳ [High]   insulin Shot (10 mins)
3. ⏳ [Medium] Clean Litter Box (10 mins)
4. ⏳ [Low]    Brush Fur (15 mins)
--------------------------------------------------
📊 Summary: Scheduled 4 tasks total | Time Used: 65/75 mins
==================================================

## 🧪 Testing PawPal+

python -m pytest

Task Recurrence Engine: Verifies timedelta date advancement when cycling daily or weekly tasks.

Chronological Sorting: Ensures items align sequentially based on string time splits.

Conflict Isolation: Confirms overlap warnings trigger safely on duplicate timestamps.

Empty State Handling: Ensures an owner with an unconfigured pet safely resolves to an empty plan rather than throwing a runtime crash.

========================== test session starts ===========================
platform win32 -- Python 3.12.4, pytest-7.4.4, pluggy-1.0.0
rootdir: C:\Users\ajaas\AI100\ai110-module2show-pawpal-starter
plugins: anyio-4.2.0
collected 4 items                                                         

tests\test_pawpal.py ....                                           [100%]

=========================== 4 passed in 0.05s ============================
```
Confidence Level - 4

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Automatically organizes tasks chronologically using an optimized `lambda` key on their start times. |
| Filtering | `Scheduler.filter_tasks()` | Allows isolating specific tasks out of the pool by custom attributes like completion status or pet name. |
| Conflict handling | `Scheduler.detect_conflicts()` | Scans scheduled items, computes execution windows from durations, and prints clear warning alerts for overlapping times. |
| Recurring tasks | `Task.mark_complete()` | Detects frequency tiers ("Daily"/"Weekly") and uses Python's `timedelta` to automatically instantiate the next occurrence. |

## 📸 Demo Walkthrough

### Main Features Implemented
1. **Chronological Sorting by Time:** Formats and orders daily plans based on explicit task start times (`HH:MM`).
2. **Interactive Conflict Warnings:** Alerts pet owners if tasks for their pets overlap in execution time slots.
3. **Automated Task Recurrence:** Gracefully calculates and spawns the next occurrence date whenever daily or weekly events finish.

### Example User Workflow
1. **Define Owner & Pet Metadata:** Input profile information dynamically inside the application UI.
2. **Inject Tasks with Varied Timestamps:** Add specific routines (e.g., a high-priority "Morning Walk" at `08:00` and "Feed Breakfast" at `08:00`).
3. **Build and Optimize Schedule:** Click **Generate schedule**. The app displays an overlap alert message and arranges the valid agenda chronologically.

### Verified CLI Output Tracking (`main.py`)
```text
⚠️ Conflict: 'Morning Walk' overlaps with 'Feed Breakfast' around 08:00.
==================================================
🐾 PAWPAL+ DAILY SCHEDULE FOR ALEX 🐾
⏱️  Time Budget: 75 mins
==================================================
1. ⏳ [High]   Morning Walk (30 mins)
2. ⏳ [High]   Feed Breakfast (15 mins)
3. ⏳ [High]   insulin Shot (10 mins)
4. ⏳ [Medium] Clean Litter Box (10 mins)
--------------------------------------------------
📊 Summary: Scheduled 4 tasks total | Time Used: 65/75 mins
==================================================