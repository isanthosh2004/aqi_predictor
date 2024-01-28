from flask import Flask, render_template, request
import pandas as pd

# Your existing code for data preprocessing, model training, and prediction here

app=Flask(__name__,template_folder='templates')

# Define route for index page
@app.route('/hello')
def index():
    return render_template('index.html')

# Define route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    input_datetime = pd.to_datetime(request.form['datetime'])
    predicted_aqi = predict_aqi(input_datetime)
    advice = advise_action(predicted_aqi)
    return render_template('result.html', predicted_aqi=predicted_aqi, advice=advice)

if __name__ == '__main__':
    app.run(debug=True)
