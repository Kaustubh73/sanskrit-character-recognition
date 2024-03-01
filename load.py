import cv2
import os
import numpy as np
from tensorflow.keras.models import Sequential, save_model, load_model
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical, plot_model
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import CategoricalAccuracy
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau

vowels = {
            'अ': 'a',
            'आ': 'ā',
            'इ': 'i',
            'ई': 'ī',
            'उ': 'u',
            'ऊ': 'ū',
            'ऋ': 'ṛ',
            'ॠ': 'ṝ',
            'ऌ': 'ḷ',
            'ॡ': 'ḹ',
            'ए': 'e',
            'ऐ': 'ai',
            'ओ': 'o',
            'औ': 'au'
        }

# def preprocess_image(image_path, target_size=(32, 32), save_path=None):
#     img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale
#     img = cv2.resize(img, target_size)  # Resize the image
#     img = img.astype('float32') / 255.0  # Normalize pixel values to be between 0 and 1

#     if save_path is not None:
#         os.makedirs(os.path.dirname(save_path), exist_ok=True)
#         cv2.imwrite(save_path, (img * 255).astype(np.uint8))
#         print(save_path)

#     return img

# def load_data(data_directory, save_directory=None):
#     images = []
#     labels = []
#     for character_folder in os.listdir(data_directory):
#         character_path = os.path.join(data_directory, character_folder)
#         for image_file in os.listdir(character_path):
#             image_path = os.path.join(character_path, image_file)
#             # print(image_path)
#             # Set the save path for the preprocessed image
#             if save_directory is not None:
#                 save_path = os.path.join(save_directory, character_folder, image_file)
#                 # print(save_path)
#             else:
#                 save_path = None

#             img = preprocess_image(image_path, save_path=save_path)
#             images.append(img)
#             labels.append(character_folder)

#     return np.array(images), np.array(labels)
# Example usage:
data_directory = "my_data"
save_directory = "preprocessed"
images, labels = load_data(data_directory, save_directory)


cnn = Sequential()
cnn.add(Conv2D(filters=32, kernel_size=(3, 3), padding='same', strides=(1,1), activation='relu', input_shape=(32, 32, 1)))
cnn.add(Dropout(.2))
cnn.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
cnn.add(Conv2D(filters=64, kernel_size=(3, 3), padding='same', strides=(1,1), activation='relu'))
cnn.add(Dropout(.2))
cnn.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
cnn.add(Flatten())
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dropout(.5))
cnn.add(Dense(units=10, activation='softmax'))

plot_model(cnn, show_shapes=True, show_layer_activations=True, show_layer_names=False)