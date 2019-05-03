import os

from flask import Flask, request
from src.app_common import app, invalid_input, invalid_process, \
    HTTP_OK, HTTP_INTERNAL_SERVER_ERROR, HTTP_BAD_REQUEST
from src.model import TrainedModel
from util.stackdriver import monitor


MODEL_PATH = "./saved_model"
app = Flask(__name__)


# get the predicted result from the model
@app.route('/predict', methods=['POST'])
@monitor('predict')
def predict():
    try:
        return trainedModel.predict(request)
    except AttributeError:
        return invalid_process(
            "[WARNING] 'predict' method has not been implemented in the wrapper")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)