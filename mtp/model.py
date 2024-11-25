import pickle
import re
from sklearn.feature_extraction import DictVectorizer

# Load the DictVectorizer
vectorizer_filename = 'vectorizer.pkl'
with open(vectorizer_filename, 'rb') as file:
    vectorizer = pickle.load(file)

# Load the model
model_filename = 'model.pkl'
with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

# Function to sanitize file names
def sanitize_filename(name):
    return re.sub(r'[^\w\-_\. ]', '_', name)

def preprocess_input(input_data):
    # Normalize column names
    input_data_normalized = [{k.lower().replace(' ', '_'): v for k, v in item.items()} for item in input_data]
    
    # Vectorize the input data
    input_vectorized = vectorizer.transform(input_data_normalized)
    
    return input_vectorized

def predict(input_data):
    # Ensure input_data is a list of dictionaries
    if not isinstance(input_data, list) or not all(isinstance(item, dict) for item in input_data):
        raise ValueError("Input data must be a list of dictionaries")
    
    # Preprocess the input data
    input_data_preprocessed = preprocess_input(input_data)
    
    # Make prediction
    raw_prediction = loaded_model.predict(input_data_preprocessed)
    
    # Debug: Print raw predictions
    print(f"Raw predictions: {raw_prediction}")
    
    # Post-process the prediction to ensure it is in the range of 1 to 5
    prediction = [max(1, min(5, round(pred))) for pred in raw_prediction]
    
    # Debug: Print post-processed predictions
    print(f"Post-processed predictions: {prediction}")
    
    return prediction