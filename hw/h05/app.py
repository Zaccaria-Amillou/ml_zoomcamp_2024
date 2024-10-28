# Import packages
from flask import Flask, request, jsonify
import pickle

# Load the model
with open("dv.bin", "rb") as f_dv:
    dv = pickle.load(f_dv)

with open("model1.bin","rb") as f_model:
    model = pickle.load(f_model)

# initialize Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    #get the client data from the request
    client = request.get_json()

    # Transform the client data using the DictVectorizer
    X = dv.transform([client])

    # Calculate the probability
    probability = model.predict_proba(X)[0,1]

    # Return the result as JSON 
    result = {"Subscription probability" : probability}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
