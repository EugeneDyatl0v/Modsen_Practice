import numpy as np
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image
from helpers import model

def extract_features(image_path):
    """
        Extract features from an image using a pre-trained VGG16 model.

        Args:
            image_path (str): Path to the image file.

        Returns:
            np.ndarray: Flattened feature vector extracted from the image.
    """
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
