import os
from PIL import Image, UnidentifiedImageError
from concurrent.futures import ThreadPoolExecutor, as_completed


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


def load_images_from_folders_parallel(folders):
    """
        Load images from multiple folders in parallel.

        Args:
            folders (list): List of folder paths.

        Returns:
            dict: Dictionary with image paths as keys and PIL Image objects as values.
    """
    images = {}
    with ThreadPoolExecutor() as executor:
        futures = []
        for folder in folders:
            for filename in os.listdir(folder):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                    img_path = os.path.join(folder, filename)
                    futures.append(executor.submit(load_image, img_path))

        for future in as_completed(futures):
            img_path, img = future.result()
            if img:
                images[img_path] = img

    return images


def load_image(img_path):
    try:
        img = Image.open(img_path)
        return img_path, img
    except (UnidentifiedImageError, IOError) as e:
        print(f"Error loading image {img_path}: {e}")
        return img_path, None
