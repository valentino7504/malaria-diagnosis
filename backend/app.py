import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
from flask import request, jsonify
from config import app
from utils import predict_image, preprocess_image


@app.route("/predict", methods=["POST"])
def predict():
    """
    'predict' route of the api used to submit input images

    Returns:
    - flask.Response: JSON of the prediction.
    """
    if "smear_image" not in request.files:
        return "Error"
    else:
        smear_image = request.files.getlist("smear_image")[0]
        img_array = preprocess_image(smear_image)
        prediction = predict_image(img_array)
        return jsonify(prediction)


if __name__ == "__main__":
    app.run(debug=True)
