import pytest
from helpers.feature_extraction import extract_features
import numpy as np
from PIL import Image
import os
from tests import IMAGE_PATH, TEST_DIR


def setup_module(module):
    """
        Setup function to create a directory and save a test image.

        Parameters:
        module: The module that calls this setup function.
    """
    os.makedirs(TEST_DIR, exist_ok=True)
    img = Image.new('RGB', (100, 100))
    img.save(IMAGE_PATH)


def test_extract_features():
    """
        Test the extract_features function to ensure it correctly extracts features from an image.

        Scenario:
        - A test image is created and saved in the setup.
        - The function should return a non-null, non-empty NumPy array of features.
    """
    features = extract_features(IMAGE_PATH)
    assert features is not None
    assert isinstance(features, np.ndarray)
    assert features.shape[0] > 0
