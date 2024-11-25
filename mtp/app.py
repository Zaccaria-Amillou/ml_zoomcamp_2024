from flask import Flask, request, jsonify, render_template
import pandas as pd
from model import predict

# Define the expected structure of the input data
categorical_features = ['device_model', 'operating_system', 'gender']
numerical_features = [
    'app_usage_time_(min/day)',
    'screen_on_time_(hours/day)',
    'battery_drain_(mah/day)',
    'number_of_apps_installed',
    'data_usage_(mb/day)',
    'age'
]

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    # Get form data
    form_data = request.form.to_dict()
    
    # Convert form data to the required format
    input_data = [{k: v for k, v in form_data.items()}]
    
    # Ensure the input data has the correct columns
    for feature in categorical_features + numerical_features:
        if feature not in input_data[0]:
            return jsonify({'error': f'Missing feature: {feature}'}), 400
    
    # Make prediction
    prediction = predict(input_data)
    
    # Return prediction as JSON
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)