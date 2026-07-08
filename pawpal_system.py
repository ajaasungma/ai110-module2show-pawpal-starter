from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    """Represents a standalone care action with duration and priority metrics."""
    name: str
    duration_mins: int
    priority: str  # e.g., "High", "Medium", "Low"
    is_completed: bool = False

    def mark_complete(self) -> None:
        """Flags the task instance as successfully completed."""
        self.is_completed = True


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


@dataclass
class Scheduler:
    """Handles algorithmic constraints and aggregates tasks into an optimized daily plan."""
    max_time_budget_mins: int

    def generate_daily_plan(self, owner: "Owner") -> List[Task]:
        """
        Retrieves all tasks from an owner's pets, sorts them by priority,
        and fits them within the allocated daily maximum time budget.
        """
        # Collect all tasks across all pets
        all_tasks = owner.get_all_tasks()
        
        # Priority weight map for clear deterministic sorting
        priority_weights = {"High": 1, "Medium": 2, "Low": 3}
        
        # Sort primarily by priority tier, and secondarily by duration (shortest first)
        sorted_tasks = sorted(
            all_tasks, 
            key=lambda t: (priority_weights.get(t.priority, 4), t.duration_mins)
        )
        
        scheduled_tasks = []
        accumulated_time = 0
        
        for task in sorted_tasks:
            if accumulated_time + task.duration_mins <= self.max_time_budget_mins:
                scheduled_tasks.append(task)
                accumulated_time += task.duration_mins
                
        return scheduled_tasks


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