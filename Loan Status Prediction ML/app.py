# Import necessary modules
from flask import Flask, request, render_template
import pickle
import numpy as np

# Create a Flask application instance
app = Flask(__name__, template_folder='.')

# Load the trained model
with open("loan_status_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define a route for the homepage
@app.route("/")
def home():
    return render_template("index.html") # Render the index.html template

# Define a route for making predictions
@app.route("/predict", methods=["POST"])
def predict():
    # Get input data from the form
    gender = int(request.form["gender"])
    married = int(request.form["married"])
    dependents = int(request.form["dependents"])
    education = int(request.form["education"])
    self_employed = int(request.form["self_employed"])
    applicant_income = float(request.form["applicant_income"])
    coapplicant_income = float(request.form["coapplicant_income"])
    loan_amount = float(request.form["loan_amount"])
    loan_amount_term = float(request.form["loan_amount_term"])
    credit_history = float(request.form["credit_history"])
    property_area = int(request.form["property_area"])

    # Combine inputs into a single list
    input_data = np.asarray([[gender, married, dependents, education, self_employed, applicant_income,
                              coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area]])

    # Make a prediction using the model
    prediction = model.predict(input_data)

    # Determine the output message
    if prediction[0] == 0:
        prediction_text = 'Unfortunately, the loan application is likely to be rejected.'
    else:
        prediction_text = 'Congratulations! The loan application is likely to be approved.'

    # Pass the prediction value to the template
    return render_template("index.html", prediction=prediction_text)

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True) # Run the application in debug mode for development
