from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model


base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)