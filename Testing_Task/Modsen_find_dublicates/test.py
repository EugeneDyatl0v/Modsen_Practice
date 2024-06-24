import os
import pytest
from main import find_duplicates_app

# Create test directories and images
TEST_DIR = 'images'
FOLDER1 = os.path.join(TEST_DIR, 'test_folder_1')
FOLDER2 = os.path.join(TEST_DIR, 'test_folder_2')


def setup_module(module):
    os.makedirs(FOLDER1, exist_ok=True)
    os.makedirs(FOLDER2, exist_ok=True)


@pytest.mark.parametrize("method,use_nn,threshold", [
    ('phash', True, 0.9),
    ('dhash', False, 0.9),
    ('whash', True, 0.9),
    ('ahash', False, 0.9),
    ('chash', False, 0.9),
])
def test_find_duplicates_app(method, use_nn, threshold):
    duplicates = find_duplicates_app(FOLDER1, FOLDER2, method=method,
                                     use_nn=use_nn, threshold=threshold)
    assert isinstance(duplicates, list)
    if use_nn:
        assert all(
            isinstance(dup, tuple) and len(dup) == 2 for dup in duplicates
        )


def test_find_duplicates_with_single_folder():
    duplicates = find_duplicates_app(FOLDER1, method='phash', use_nn=True,
                                     threshold=0.9)
    assert isinstance(duplicates, list)


def test_no_duplicates_found():
    # Create distinct images that should not be duplicates
    # Add distinct images to FOLDER1 and FOLDER2
    duplicates = find_duplicates_app(FOLDER1, FOLDER2, method='phash',
                                     use_nn=False, threshold=0.9)
    assert len(duplicates) == 0
