from flask import Flask, render_template, request
import joblib
import pandas as pd
app = Flask(__name__)
# Load your trained model
model = joblib.load('house_price_prediction_model.pkl')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():
    try:
        # Get form data
        location = request.form['location']
        sqft = int(request.form['total_sqft'])
        bhk = int(request.form['BHK'])
        bath = int(request.form['bath'])

        # Convert input into a DataFrame
        input_data = pd.DataFrame([[location, sqft, bhk, bath]], 
                                  columns=['location', 'total_sqft', 'BHK', 'bath'])

        # Make prediction
        prediction = model.predict(input_data)
        predicted_price = round(prediction[0], 2)

        # Render result
        return render_template('index.html', predicted_price=predicted_price)

    except Exception as e:
        print(f"Error: {e}")
        return "Something went wrong!"
if __name__ == '__main__':
    app.run(debug=True)
