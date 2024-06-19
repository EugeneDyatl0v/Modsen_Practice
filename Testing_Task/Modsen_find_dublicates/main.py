from helpers import (
    calculate_image_hashes,
    display_duplicates,
    find_duplicates,
    load_images_from_folder, extract_features
)


def find_duplicates_app(folder1, folder2=None, method='phash', use_nn=False, threshold=0.9):
    images1 = load_images_from_folder(folder1)
    hashes1 = calculate_image_hashes(images1, method=method)
    feature_vectors = None

    if use_nn:
        feature_vectors = {path: extract_features(path) for path in images1.keys()}
        if folder2:
            images2 = load_images_from_folder(folder2)
            hashes2 = calculate_image_hashes(images2, method=method)
            combined_hashes = {**hashes1, **hashes2}
            feature_vectors.update({path: extract_features(path) for path in images2.keys()})
        else:
            combined_hashes = hashes1
    else:
        if folder2:
            images2 = load_images_from_folder(folder2)
            hashes2 = calculate_image_hashes(images2, method=method)
            combined_hashes = {**hashes1, **hashes2}
        else:
            combined_hashes = hashes1

    duplicates = find_duplicates(combined_hashes, feature_vectors=feature_vectors, threshold=threshold)
    display_duplicates(duplicates)
    return duplicates


if __name__ == '__main__':
    # Define the folders containing the images
    folder1 = 'images/Lilly'
    folder2 = 'images/Lotus'

    # Find and display duplicates
    duplicates = find_duplicates_app(folder1, folder2, method='phash', use_nn=True, threshold=0.9)

    # Print the duplicate pairs
    for dup in list(set(duplicates)):
        print(f"Duplicate found: {dup[0]} and {dup[1]}")