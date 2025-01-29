import unittest
from unittest.mock import patch
from budget_tracker import main

# test_budget_tracker.py


class TestBudgetTracker(unittest.TestCase):

    @patch('builtins.input', side_effect=[5000, 300, 200, 150, 100, 50])
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Welcome to the Personal Budget Tracker")
        mock_print.assert_any_call("Your remaining budget is $4200.0")

if __name__ == "__main__":
    unittest.main()