import pytest
from helpers.hashing import calculate_image_hashes
from PIL import Image
import numpy as np


def test_calculate_image_hashes():
    """
        Test the calculate_image_hashes function to ensure it correctly calculates hashes for images.

        Scenario:
        - A dummy image is created and stored in a dictionary with a dummy path.
        - The function should return a dictionary containing the hash of the image.
        - The hash value for the dummy path should not be None.
    """
    img = Image.fromarray(np.zeros((100, 100), dtype=np.uint8))
    images = {'dummy_path': img}
    hashes = calculate_image_hashes(images, method='phash')
    assert 'dummy_path' in hashes
    assert hashes['dummy_path'] is not None
