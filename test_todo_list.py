# test_todo_list.py
import unittest
from todo_list import add_task

class TestToDoList(unittest.TestCase):
    def test_add_task(self):
        todo_list = []
        add_task(todo_list)  # Corrected the function call
        self.assertEqual(len(todo_list), 1)
        self.assertEqual(todo_list[0]["task"], "Test Task")
        self.assertFalse(todo_list[0]["completed"])

if __name__ == "__main__":
    unittest.main()

