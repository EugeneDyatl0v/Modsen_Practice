from helpers.hashing import calculate_image_hashes
from helpers.ui import display_duplicates
from helpers.duplicates_finder import find_duplicates
from helpers.image_loader import load_images_from_folders
from helpers.feature_extraction import extract_features


def find_duplicates_app(folders, method='phash', use_nn=False, threshold=0.9):
    """
        Find and display duplicate images from multiple folders.

        Args:
            folders (list): List of folder paths containing images.
            method (str): Hashing method to use ('phash', 'dhash', 'whash', 'ahash').
            use_nn (bool): Use neural network for feature extraction if True.
            threshold (float): Threshold for cosine similarity to consider images as duplicates.

        Returns:
            list: List of tuples containing paths of duplicate images.
    """
    images = load_images_from_folders(folders)
    hashes = calculate_image_hashes(images, method=method)
    feature_vectors = None

    if use_nn:
        feature_vectors = {path: extract_features(path) for path in
                           images.keys()}

    duplicates = find_duplicates(hashes, feature_vectors=feature_vectors,
                                 threshold=threshold)
    display_duplicates(duplicates)
    return duplicates


def render_main(folders):
    duplicates = find_duplicates_app(folders, method='phash', use_nn=True,
                                     threshold=0.9)

    for dup in list(set(duplicates)):
        print(f"Duplicate found: {dup[0]} and {dup[1]}")


if __name__ == '__main__':
    folders = ['images/Lilly', 'images/Lotus', 'images/test_folder_1']
    render_main(folders)

