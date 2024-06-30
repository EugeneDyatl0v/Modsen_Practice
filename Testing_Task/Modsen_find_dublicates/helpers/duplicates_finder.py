import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def find_duplicates(hashes, feature_vectors=None, threshold=0.9):
    """
        Find duplicate images based on hashes and optional feature vectors.

        Args:
            hashes (dict): Dictionary with image paths as keys and hash values as values.
            feature_vectors (dict, optional): Dictionary with image paths as keys and feature vectors as values.
            threshold (float, optional): Threshold for cosine similarity to consider images as duplicates.

        Returns:
            list: List of tuples containing paths of duplicate images.
    """
    hash_dict = {}
    duplicates = []

    for path, hash_value in hashes.items():
        if hash_value in hash_dict:
            duplicates.append((hash_dict[hash_value], path))
        else:
            hash_dict[hash_value] = path

    if feature_vectors:
        paths = list(feature_vectors.keys())
        vectors = np.array(list(feature_vectors.values()))
        similarity_matrix = cosine_similarity(vectors)

        for i in range(len(paths)):
            for j in range(i + 1, len(paths)):
                if similarity_matrix[i, j] > threshold:
                    duplicates.append((paths[i], paths[j]))

    return duplicates