from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional

@dataclass
class Task:
    """Represents a standalone care action with duration, priority, timing, and frequency."""
    name: str
    duration_mins: int
    priority: str  # "High", "Medium", "Low"
    start_time_str: str = "00:00"  # Format: "HH:MM"
    frequency: str = "Once"  # "Once", "Daily", "Weekly"
    due_date: datetime = field(default_factory=datetime.now)
    is_completed: bool = False

    def mark_complete(self) -> Optional['Task']:
        """
        Flags the task as complete. If it's a recurring task ("Daily" or "Weekly"),
        it automatically returns a new uncompleted Task instance scheduled for the next interval.
        """
        self.is_completed = True
        
        if self.frequency == "Daily":
            next_due = self.due_date + timedelta(days=1)
            return Task(name=self.name, duration_mins=self.duration_mins, priority=self.priority, 
                        start_time_str=self.start_time_str, frequency=self.frequency, due_date=next_due)
        elif self.frequency == "Weekly":
            next_due = self.due_date + timedelta(weeks=1)
            return Task(name=self.name, duration_mins=self.duration_mins, priority=self.priority, 
                        start_time_str=self.start_time_str, frequency=self.frequency, due_date=next_due)
        return None


@dataclass
class Pet:
    """Holds information regarding an individual pet profile and its specific tasks."""
    name: str
    species: str
    age: int
    special_notes: str = ""
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Associates a new care task directly to this pet profile."""
        self.tasks.append(task)


class Owner:
    """The central profile that manages pets and provides a consolidated view of tasks."""
    def __init__(self, name: str, email: str):
        self.name: str = name
        self.email: str = email
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Associates a new pet profile with this owner."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Gathers and flattens all tasks across every registered pet profile."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append(task)
        return all_tasks


@dataclass
class Scheduler:
    """Handles sorting, filtering, and conflict identification across an owner's tasks."""
    max_time_budget_mins: int

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sorts a list of tasks chronologically by their 'HH:MM' start time string using a lambda function key."""
        return sorted(tasks, key=lambda t: [int(x) for x in t.start_time_str.split(":")])

    def filter_tasks(self, tasks: List[Task], pet_name: Optional[str] = None, status: Optional[bool] = None) -> List[Task]:
        """Filters a collection of tasks by a specific pet owner profile or by completion status."""
        filtered = tasks
        if status is not None:
            filtered = [t for t in filtered if t.is_completed == status]
        return filtered

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """
        Scans a list of tasks and evaluates chronological overlaps. 
        Returns a list of human-readable warnings if tasks overlap in time.
        """
        warnings = []
        sorted_tasks = self.sort_by_time(tasks)
        
        for i in range(len(sorted_tasks)):
            for j in range(i + 1, len(sorted_tasks)):
                t1 = sorted_tasks[i]
                t2 = sorted_tasks[j]
                
                # Convert times to minutes from midnight to calculate raw window overlaps
                h1, m1 = map(int, t1.start_time_str.split(":"))
                h2, m2 = map(int, t2.start_time_str.split(":"))
                
                start1 = h1 * 60 + m1
                end1 = start1 + t1.duration_mins
                
                start2 = h2 * 60 + m2
                
                # Check if task 2 starts before task 1 ends
                if start2 < end1:
                    warnings.append(f"⚠️ Conflict: '{t1.name}' overlaps with '{t2.name}' around {t2.start_time_str}.")
                    
        return warnings

    def generate_daily_plan(self, owner: Owner) -> List[Task]:
        """Retrieves all tasks across an owner's pet profiles and schedules them chronologically within budget."""
        all_tasks = owner.get_all_tasks()
        chronological_tasks = self.sort_by_time(all_tasks)
        
        scheduled_tasks = []
        accumulated_time = 0
        
        for task in chronological_tasks:
            if accumulated_time + task.duration_mins <= self.max_time_budget_mins:
                scheduled_tasks.append(task)
                accumulated_time += task.duration_mins
                
        return scheduled_tasks