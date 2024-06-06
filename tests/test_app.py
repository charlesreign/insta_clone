from unittest.mock import patch
import pytest


import random

def get_random_element(my_list):
    return random.choice(my_list)


def test_get_random_element():
    test_list = [1, 2, 3, 4, 5]
    expected_choice = 3  # This is the value that we expect `random.choice` to return

    # Patch `random.choice` to return `expected_choice`
    with patch('random.choice', return_value=expected_choice) as mock_choice:
        result = get_random_element(test_list)

        # Check the result
        assert result == "Hello"

        # Ensure `random.choice` was called exactly once with `test_list`
        # mock_choice.assert_called_once_with(test_list)