"""Course-aligned unit tests for Task and TaskPool."""
import unittest
from todo import Task, TaskPool

class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.pool = TaskPool()
    def test_add_task(self):
        self.pool.add_task(Task("Investigate alert"))
        self.assertEqual(len(self.pool.tasks), 1)
    def test_get_open_tasks(self):
        self.pool.populate()
        self.assertEqual(len(self.pool.get_open_tasks()), 3)
        self.assertTrue(all(t.status == "ToDo" for t in self.pool.get_open_tasks()))
    def test_get_done_tasks(self):
        self.pool.populate()
        self.assertEqual(len(self.pool.get_done_tasks()), 3)
        self.assertTrue(all(t.completed for t in self.pool.get_done_tasks()))
    def test_complete_task(self):
        task = Task("Test")
        task.mark_completed()
        self.assertEqual(task.status, "Done")

if __name__ == "__main__":
    unittest.main(verbosity=2)
