import os
import pytest
from main import find_duplicates_app
from tests import FOLDER1, FOLDER2, FOLDER3


def setup_module(module):
    """
        Setup function to create directories for testing.

        Parameters:
        module: The module that calls this setup function.
    """
    os.makedirs(FOLDER1, exist_ok=True)
    os.makedirs(FOLDER2, exist_ok=True)
    os.makedirs(FOLDER3, exist_ok=True)


@pytest.mark.parametrize("method,use_nn,threshold", [
    ('phash', True, 0.9),
    ('dhash', False, 0.9),
    ('whash', True, 0.9),
    ('ahash', False, 0.9),
    ('chash', False, 0.9),
])
def test_find_duplicates_app(method, use_nn, threshold):
    """
        Test the find_duplicates_app function with various methods, neural network usage, and thresholds.

        Parameters:
        method (str): The hashing method to use ('phash', 'dhash', 'whash', 'ahash', 'chash').
        use_nn (bool): Whether to use a neural network for duplicate detection.
        threshold (float): The threshold for duplicate detection.
    """
    duplicates = find_duplicates_app([FOLDER1, FOLDER2, FOLDER3], method=method,
                                     use_nn=use_nn, threshold=threshold)
    assert isinstance(duplicates, list)
    if use_nn:
        assert all(
            isinstance(dup, tuple) and len(dup) == 2 for dup in duplicates
        )


def test_find_duplicates_with_single_folder():
    """
        Test the find_duplicates_app function with a single folder.

        Scenario:
        - The function should return a list of duplicates (if any) within the single folder.
    """
    duplicates = find_duplicates_app([FOLDER1], method='phash', use_nn=True,
                                     threshold=0.9)
    assert isinstance(duplicates, list)


def test_no_duplicates_found():
    """
        Test the find_duplicates_app function when no duplicates are expected.

        Scenario:
        - The function should return an empty list when no duplicates are found.
    """
    duplicates = find_duplicates_app([FOLDER1, FOLDER2, FOLDER3], method='phash',
                                     use_nn=False, threshold=0.9)
    assert len(duplicates) == 0
