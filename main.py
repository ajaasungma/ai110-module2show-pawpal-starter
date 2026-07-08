from pawpal_system import Owner, Pet, Task, Scheduler

def run_demo():
    # 1. Initialize our Owner
    owner = Owner(name="Alex", email="alex@example.com")
    
    # 2. Add distinct pets
    mochi = Pet(name="Mochi", species="Dog", age=2)
    biscuit = Pet(name="Biscuit", species="Golden Retriever", age=3)
    luna = Pet(name="Luna", species="Siamese Cat", age=2)
    
    owner.add_pet(mochi)
    owner.add_pet(biscuit)
    owner.add_pet(luna)

    # 3. Inject tasks across pets with distinct start times to prevent accidental 00:00 warnings
    biscuit.add_task(Task(name="Brush Fur", duration_mins=15, priority="Low", start_time_str="10:00"))
    biscuit.add_task(Task(name="Dog Park Run", duration_mins=45, priority="Medium", start_time_str="14:00"))
    
    luna.add_task(Task(name="insulin Shot", duration_mins=10, priority="High", start_time_str="07:00"))
    luna.add_task(Task(name="Clean Litter Box", duration_mins=10, priority="Medium", start_time_str="19:00"))

    # Update main.py with two tasks at the same time to test conflict logic
    task1 = Task(name="Morning Walk", duration_mins=30, priority="High", start_time_str="08:00")
    task2 = Task(name="Feed Breakfast", duration_mins=15, priority="High", start_time_str="08:00")
    mochi.add_task(task1)
    mochi.add_task(task2)

    # 4. Verify that your Scheduler correctly identifies and prints a warning
    scheduler = Scheduler(max_time_budget_mins=75)
    all_tasks = owner.get_all_tasks()
    warnings = scheduler.detect_conflicts(all_tasks)

    # Print out conflict results to verify
    for warning in warnings:
        print(warning)

    # 5. Generate daily plan based on constraints and priorities
    daily_plan = scheduler.generate_daily_plan(owner)

    # 6. Output beautiful scannable results
    print("=" * 50)
    print(f"🐾 PAWPAL+ DAILY SCHEDULE FOR {owner.name.upper()} 🐾")
    print(f"⏱️  Time Budget: {scheduler.max_time_budget_mins} mins")
    print("=" * 50)
    
    total_scheduled_time = 0
    for idx, task in enumerate(daily_plan, start=1):
        status_icon = "✅" if task.is_completed else "⏳"
        priority_badge = f"[{task.priority}]".ljust(8)
        print(f"{idx}. {status_icon} {priority_badge} {task.name} ({task.duration_mins} mins)")
        total_scheduled_time += task.duration_mins
        
    print("-" * 50)
    print(f"📊 Summary: Scheduled {len(daily_plan)} tasks total | Time Used: {total_scheduled_time}/{scheduler.max_time_budget_mins} mins")
    print("=" * 50)

if __name__ == "__main__":
    run_demo()