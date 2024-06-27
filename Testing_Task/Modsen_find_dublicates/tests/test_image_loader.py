import os
import pytest
from helpers.image_loader import load_images_from_folders
from PIL import Image
from tests import FOLDER1, FOLDER2


def setup_module(module):
    """
        Setup function to create directories and save test images.

        Parameters:
        module: The module that calls this setup function.
    """
    os.makedirs(FOLDER1, exist_ok=True)
    os.makedirs(FOLDER2, exist_ok=True)
    img = Image.new('RGB', (100, 100))
    img.save(os.path.join(FOLDER1, 'test_image_1.jpg'))
    img.save(os.path.join(FOLDER2, 'test_image_2.jpg'))


def test_load_images_from_folders():
    """
        Test the load_images_from_folders function to ensure it correctly loads images from specified folders.

        Scenario:
        - Test folders and images are created in the setup.
        - The function should return a dictionary containing the loaded images.
        - The dictionary should contain entries for all images, and all values should be instances of Image.Image.
    """
    images = load_images_from_folders([FOLDER1, FOLDER2])
    assert len(images) > 0
    assert all(isinstance(img, Image.Image) for img in images.values())
