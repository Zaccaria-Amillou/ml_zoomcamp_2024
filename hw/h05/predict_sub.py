# Packages
import pickle

# load the model
with open('dv.bin', 'rb') as f_dv:
    dv = pickle.load(f_dv)

with open('model1.bin', 'rb') as f_model:
    model = pickle.load(f_model)

# define the client data 
client = {
    "job" : "management",
    "duration" : 400,
    "poutcome" : "success"
}

# Transform the client data using the DictVectorizer
X = dv.transform([client])

# Get the probability of subscription
probability = model.predict_proba(X)[0,1]

# Print the result
print(f"Probability of subscription : {probability:.2f}")
