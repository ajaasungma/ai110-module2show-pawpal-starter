from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_completion_and_recurrence():
    """Verify that completing a daily task generates a new instance for tomorrow."""
    base_date = datetime(2026, 7, 7, 12, 0)
    task = Task(name="Daily Feeding", duration_mins=10, priority="High", frequency="Daily", due_date=base_date)
    
    # Complete task and grab the auto-generated next instance
    next_task = task.mark_complete()
    
    assert task.is_completed is True
    assert next_task is not None
    assert next_task.name == "Daily Feeding"
    assert next_task.is_completed is False
    # Target date must advance exactly 1 day
    assert next_task.due_date == base_date + timedelta(days=1)


def test_chronological_sorting():
    """Verify tasks are accurately sorted from morning to night regardless of insertion order."""
    scheduler = Scheduler(max_time_budget_mins=120)
    
    t_afternoon = Task(name="Afternoon Play", duration_mins=30, priority="Medium", start_time_str="14:30")
    t_morning = Task(name="Morning Walk", duration_mins=30, priority="High", start_time_str="08:00")
    t_night = Task(name="Night Check", duration_mins=15, priority="Low", start_time_str="21:15")
    
    unordered_pool = [t_afternoon, t_morning, t_night]
    sorted_pool = scheduler.sort_by_time(unordered_pool)
    
    # Assert true sequential sorting order
    assert sorted_pool[0].start_time_str == "08:00"
    assert sorted_pool[1].start_time_str == "14:30"
    assert sorted_pool[2].start_time_str == "21:15"


def test_conflict_detection():
    """Verify that scheduling multiple tasks at identical times yields warnings."""
    scheduler = Scheduler(max_time_budget_mins=60)
    
    t1 = Task(name="Morning Feeding", duration_mins=15, priority="High", start_time_str="08:00")
    t2 = Task(name="Morning Walk", duration_mins=30, priority="High", start_time_str="08:00")
    t3 = Task(name="Afternoon Brush", duration_mins=10, priority="Low", start_time_str="15:00")
    
    warnings = scheduler.detect_conflicts([t1, t2, t3])
    
    # Should flag 1 conflict because t1 and t2 share the 08:00 slot
    assert len(warnings) == 1
    assert "Morning Feeding" in warnings[0]
    assert "Morning Walk" in warnings[0]


def test_empty_pet_edge_case():
    """Verify scheduler handles a pet with no tasks without crashing."""
    owner = Owner(name="Sam", email="sam@example.com")
    pet = Pet(name="Milo", species="Bird", age=1)
    owner.add_pet(pet)
    
    scheduler = Scheduler(max_time_budget_mins=60)
    plan = scheduler.generate_daily_plan(owner)
    
    assert plan == []