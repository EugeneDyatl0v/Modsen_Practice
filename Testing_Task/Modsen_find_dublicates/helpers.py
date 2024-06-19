import os
import imagehash
import matplotlib.pyplot as plt
from PIL import Image, UnidentifiedImageError
import numpy as np
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from sklearn.metrics.pairwise import cosine_similarity

# Load VGG16 model for feature extraction
base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)


def load_images_from_folder(folder):
    images = {}
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            img_path = os.path.join(folder, filename)
            try:
                img = Image.open(img_path)
                images[img_path] = img
            except (UnidentifiedImageError, IOError) as e:
                print(f"Error loading image {img_path}: {e}")
    return images


def calculate_image_hashes(images, method='phash'):
    hashes = {}
    for path, img in images.items():
        try:
            if method == 'phash':
                hash_value = imagehash.phash(img)
            else:
                raise ValueError(f"Unknown hashing method: {method}")
            hashes[path] = hash_value
        except Exception as e:
            print(f"Error hashing image {path}: {e}")
    return hashes


def extract_features(image_path):
    try:
        img = image.load_img(image_path, target_size=(224, 224))
        img_data = image.img_to_array(img)
        img_data = np.expand_dims(img_data, axis=0)
        img_data = preprocess_input(img_data)
        features = model.predict(img_data)
        return features.flatten()
    except Exception as e:
        print(f"Error extracting features from image {image_path}: {e}")
        return None


def find_duplicates(hashes, feature_vectors=None, threshold=0.9):
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


def display_duplicates(duplicates, output_folder='output'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, dup in enumerate(list(set(duplicates))):
        try:
            img1 = Image.open(dup[0])
            img2 = Image.open(dup[1])
            fig, axes = plt.subplots(1, 2, figsize=(10, 5))
            axes[0].imshow(img1)
            axes[0].set_title(f'Duplicate 1: {dup[0]}')
            axes[0].axis('off')
            axes[1].imshow(img2)
            axes[1].set_title(f'Duplicate 2: {dup[1]}')
            axes[1].axis('off')
            plt.savefig(os.path.join(output_folder, f'duplicate_{i}.png'))
            plt.close(fig)
        except Exception as e:
            print(f"Error displaying duplicates {dup[0]} and {dup[1]}: {e}")
