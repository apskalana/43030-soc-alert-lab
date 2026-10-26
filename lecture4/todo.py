"""Lecture 4 UTS GitHub Projects task-management example."""
from dataclasses import dataclass

@dataclass
class Task:
    title: str
    status: str = "ToDo"
    def mark_completed(self):
        self.status = "Done"
    @property
    def completed(self):
        return self.status == "Done"
    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"

class TaskPool:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        if not isinstance(task, Task):
            raise TypeError("Expected Task")
        self.tasks.append(task)
    def populate(self):
        self.tasks = [Task(title) for title in (
            "Read project scenario", "Develop task manager", "Write unit tests",
            "Build Docker image", "Configure GitHub Actions", "Capture portfolio evidence"
        )]
        for task in self.tasks[:3]:
            task.mark_completed()
    def get_open_tasks(self):
        return [task for task in self.tasks if not task.completed]
    def get_done_tasks(self):
        return [task for task in self.tasks if task.completed]

def main():
    pool = TaskPool()
    pool.populate()
    print("ToDo Tasks:")
    for task in pool.get_open_tasks():
        print(f"- {task.title}")
    print("Done Tasks:")
    for task in pool.get_done_tasks():
        print(f"- {task.title}")

if __name__ == "__main__":
    main()
