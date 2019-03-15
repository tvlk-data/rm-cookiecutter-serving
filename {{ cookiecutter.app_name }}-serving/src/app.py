import os

from flask import Flask, request
from src.model import TrainedModel

MODEL_PATH = "./saved_model"
MODEL_INFO_PATH = "./info.yaml"

app = Flask(__name__)
trainedModel = TrainedModel(MODEL_PATH)

# get the predicted result from the model
@app.route('/predict', methods=['POST'])
def predict():
    try:
        return trainedModel.predict(request)
    except AttributeError:
        return "[WARNING] 'predict' method has not been implemented in the wrapper"

# check the server status
@app.route('/health')
def health():
    return "200 OK"

# get the metadata of the model
@app.route('/info')
def info():
    try:
        return trainedModel.info()
    except AttributeError:
        try:
            with open(MODEL_INFO_PATH, 'r') as infoFile:
                data=infoFile.read().replace('\n','<br>')
                return data
        except (OSError, IOError) as e:
            return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)