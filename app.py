import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

# Step 2: Check if Owner already exists in the "vault" of session state before creating a new one
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", email="jordan@example.com")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Reference our persisted owner from the state vault
owner = st.session_state.owner

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value= owner.name)
owner.name = owner_name

pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
# 1. Ensure the pet exists on our owner object
    existing_pets = [p for p in owner.pets if p.name == pet_name]
    if existing_pets:
        current_pet = existing_pets[0]
    else:
        current_pet = Pet(name=pet_name, species=species, age=2)
        owner.add_pet(current_pet)
    
    # 2. Create the backend Task object and add it to the pet
    new_task = Task(name=task_title, duration_mins=int(duration), priority=priority)
    current_pet.add_task(new_task)

    st.session_state.tasks.append(
        {"title": task_title, "duration_minutes": int(duration), "priority": priority}
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
# Create the scheduler engine with a fixed 60-minute time budget constraint
    scheduler = Scheduler(max_time_budget_mins=60)
    
    # Call our backend calculation method
    optimized_plan = scheduler.generate_daily_plan(owner)
    
    st.success("Generated Plan:")
    for task in optimized_plan:
        st.write(f"- **[{task.priority}]** {task.name} ({task.duration_mins} mins)")
