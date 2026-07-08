from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_completion():
    """Verify that calling mark_complete() actually changes the task's status."""
    task = Task(name="Evening Feeding", duration_mins=10, priority="High")
    assert task.is_completed is False
    
    task.mark_complete()
    assert task.is_completed is True


def test_task_addition_to_pet():
    """Verify that adding a task to a Pet increases that pet's task count."""
    pet = Pet(name="Milo", species="Parrot", age=4)
    assert len(pet.tasks) == 0
    
    pet.add_task(Task(name="Clean Cage", duration_mins=20, priority="Medium"))
    assert len(pet.tasks) == 1
    assert pet.tasks[0].name == "Clean Cage"

