from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

# Initialize the Flask app
app = Flask(__name__)

# Load your trained model and the LabelEncoder
model = joblib.load('crop_recommendation_model.pkl')

# Load the saved LabelEncoder
le = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form (JSON payload)
        data = request.json
        input_data = np.array([[
            data['N'], data['P'], data['K'],
            data['temperature'], data['humidity'],
            data['ph'], data['rainfall']
        ]])

        # Make the prediction
        prediction = model.predict(input_data)
        predicted_crop = le.inverse_transform(prediction)  # Convert to crop name

        return jsonify({'crop': predicted_crop[0]})

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
