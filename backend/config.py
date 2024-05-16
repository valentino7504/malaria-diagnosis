"""
Create Flask app, define CORS and load up the model
"""
from flask import Flask
from flask_cors import CORS
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
from tensorflow.keras.models import load_model


app = Flask(__name__)
CORS(app)
loaded_model = load_model(
    "./mobilenet_model/malaria_diagnosis_mobilenetv3Small.keras"
)
