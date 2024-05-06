"""
Utility functions for the web app
"""
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
from config import loaded_model
from flask import jsonify


prediction_classes = {
    0: "Parasitized",
    1: "Uninfected"
}


def preprocess_image(image) -> np.array:
    """
    Preprocesses the input image for prediction.

    Parameters:
    - image (PIL.Image): The input image to be preprocessed.

    Returns:
    - np.array: The preprocessed image as a NumPy array.
    """
    image = Image.open(image).convert("RGB").resize((224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image


def predict_image(image: np.array) -> str:
    """
    Predicts the class label of an input image using the loaded model.

    Parameters:
    - image (np.array): The preprocessed image as a NumPy array.

    Returns:
    - str: The predicted class label of the input image.
    """
    prediction = loaded_model.predict(image, verbose=0)[0]
    predicted_label = prediction_classes[np.argmax(prediction)]
    return {
        "prediction": predicted_label,
        "parasitized": round(float(prediction[0]), 6),
        "uninfected": round(float(prediction[1]), 6)
    }
