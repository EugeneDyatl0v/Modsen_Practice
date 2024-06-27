import os
from PIL import Image, UnidentifiedImageError


def load_images_from_folders(folders):
    """
        Load images from multiple folders.

        Args:
            folders (list): List of folder paths.

        Returns:
            dict: Dictionary with image paths as keys and PIL Image objects as values.
    """
    images = {}
    for folder in folders:
        for filename in os.listdir(folder):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                img_path = os.path.join(folder, filename)
                try:
                    img = Image.open(img_path)
                    images[img_path] = img
                except (UnidentifiedImageError, IOError) as e:
                    print(f"Error loading image {img_path}: {e}")
    return images
