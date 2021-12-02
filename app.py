# Import libraries
from flask import Flask, request, jsonify
from utils import cleaned_df
from utils import check_for_token
import pickle
import json
import pandas as pd

app = Flask(__name__)
# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/api', methods=['POST'])
def predict():
    if check_for_token(request) == False:
        return "Unauthorized", 401
    else:
        # Get the data from the POST request.
        input = request.get_json(force=True)
        model_data = pd.DataFrame(input)[[
            'sign_in_count',
            'personal_url',
            'about',
            'avatar',
            'extended_data',
            'followers_count',
            'following_count',
            'invitations_count',
            'failed_attempts',
            'admin']]
        cleaned_data = cleaned_df(model_data)
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict_proba(cleaned_data)[:, 1]
        for index,element in enumerate(input):
            element['spam_probability'] = round(float(prediction[index]),4)
        return jsonify(input)
if __name__ == '__main__':
    app.run()