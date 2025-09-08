import unittest
from Users import Users
from tasks import TaskManager, Task

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.users = Users(filename="test_users.txt")
        self.users.users = {}

    def test_password_strength(self):
        self.assertTrue(self.users.is_strong_password("Abcdefg1"))
        self.assertFalse(self.users.is_strong_password("abc"))

    def test_add_and_verify_user(self):
        self.users.add_user("testuser", "Abcdefg1")
        self.assertTrue(self.users.verify_user("testuser", "Abcdefg1"))
        self.assertFalse(self.users.verify_user("testuser", "wrongpass"))

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tm = TaskManager()

    def test_add_task(self):
        self.tm.add_task("Task1", "Desc", "2025-09-08")
        self.assertEqual(len(self.tm.tasks), 1)

    def test_complete_task(self):
        self.tm.add_task("Task1", "Desc", "2025-09-08")
        self.tm.complete_task("Task1")
        self.assertTrue(self.tm.tasks[0].completed)

    def test_remove_completed(self):
        self.tm.add_task("Task1", "Desc", "2025-09-08")
        self.tm.complete_task("Task1")
        self.tm.remove_completed()
        self.assertEqual(len(self.tm.tasks), 0)

if __name__ == "__main__":
    unittest.main()