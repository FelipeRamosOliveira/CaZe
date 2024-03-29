import warnings
from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
import pickle

warnings.filterwarnings("ignore", category=FutureWarning)
model = pickle.load(open(f'volume/model_V1.pkl', 'rb'))

# API SERVICE
app = Flask(__name__)

# GET STATUS
@app.route("/", methods=["GET"]) 
def status():
    return jsonify({"status": "ativo"})

# GET MODEL DETAILS
@app.route("/details", methods=["GET"])
def details():
    return jsonify({"model details": str(model)})

# POST MODEL PREDICT
@app.route("/predict", methods=["POST"]) 
def predict():
    body = request.json
    input = pd.DataFrame(body, index=[0])
    predict = model.predict(input)[0]
    return jsonify({"house value": str(predict)})







if __name__ == "__main__":
    app.run(debug=True)
