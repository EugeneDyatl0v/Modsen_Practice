import pytest
from helpers.duplicates_finder import find_duplicates


def test_find_duplicates():
    """
        Test the find_duplicates function to ensure it correctly identifies duplicate files based on their hashes.

        Scenario:
        - Two file paths are provided with the same hash value.
        - The function should return a list containing one tuple of these file paths as duplicates.
    """
    hashes = {'path1': 'hash1', 'path2': 'hash1'}
    duplicates = find_duplicates(hashes)
    assert len(duplicates) == 1
    assert duplicates[0] == ('path1', 'path2')
