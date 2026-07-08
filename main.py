from pawpal_system import Owner, Pet, Task, Scheduler

def run_demo():
    # 1. Initialize our Owner
    owner = Owner(name="Alex", email="alex@example.com")

    # 2. Add two distinct pets
    biscuit = Pet(name="Biscuit", species="Golden Retriever", age=3)
    luna = Pet(name="Luna", species="Siamese Cat", age=2)
    
    owner.add_pet(biscuit)
    owner.add_pet(luna)

    # 3. Inject tasks across the pets with varying properties
    biscuit.add_task(Task(name="Morning Walk", duration_mins=30, priority="High"))
    biscuit.add_task(Task(name="Brush Fur", duration_mins=15, priority="Low"))
    biscuit.add_task(Task(name="Dog Park Run", duration_mins=45, priority="Medium"))
    
    luna.add_task(Task(name="insulin Shot", duration_mins=10, priority="High"))
    luna.add_task(Task(name="Clean Litter Box", duration_mins=10, priority="Medium"))

    # 4. Initialize Scheduler with a maximum 75-minute limit constraint
    scheduler = Scheduler(max_time_budget_mins=75)
    daily_plan = scheduler.generate_daily_plan(owner)

    # 5. Output beautiful scannable results
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