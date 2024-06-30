import imagehash


def calculate_image_hashes(images, method='phash'):
    """
        Calculate hashes for a collection of images.

        Args:
            images (dict): Dictionary with image paths as keys and PIL Image objects as values.
            method (str): Hashing method to use ('phash', 'dhash', 'whash', 'ahash').

        Returns:
            dict: Dictionary with image paths as keys and hash values as values.
    """
    hashes = {}
    for path, img in images.items():
        try:
            if method == 'phash':
                hash_value = imagehash.phash(img)
            elif method == 'dhash':
                hash_value = imagehash.dhash(img)
            elif method == 'whash':
                hash_value = imagehash.whash(img)
            elif method == 'ahash':
                hash_value = imagehash.average_hash(img)
            else:
                raise ValueError(f"Unknown hashing method: {method}")
            hashes[path] = hash_value
        except Exception as e:
            print(f"Error hashing image {path}: {e}")
    return hashes