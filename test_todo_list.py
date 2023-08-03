import unittest
from unittest.mock import patch
from io import StringIO
from todo_list import add_task, view_tasks, mark_completed, edit_task, delete_task

class TestToDoListApp(unittest.TestCase):

    def test_add_task(self):
        todo_list = []
        with patch('builtins.input', side_effect=['Task 1']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                add_task(todo_list)
                self.assertEqual(todo_list, [{'task': 'Task 1', 'completed': False}])
                self.assertEqual(mock_stdout.getvalue().strip(), "Task added successfully!")

if __name__ == '__main__':
    unittest.main()

