# Loan Status Prediction

This repository contains the code and resources for a Loan Status Prediction project. The goal of this project is to predict whether a loan application will be approved or rejected based on various input features.

## Project Overview

This project is a machine learning-based application that uses a trained model to predict the loan status based on various factors such as the applicant's income, loan amount, credit history, and more. The model was trained using a dataset containing historical loan application data.

### Key Features:

- **User Input Form:** A user-friendly HTML form to input data such as gender, marital status, income, loan amount, etc.
- **Prediction Engine:** A machine learning model that processes the input data and predicts whether the loan application will be approved or rejected.
- **Web Interface:** A Flask-based web application that hosts the prediction model and provides a simple interface for users to input data and receive predictions.

## Files in this Repository

- **`loan-status-prediction.ipynb`:** The Jupyter Notebook containing the data exploration, preprocessing, and model training code.
- **`loan_status_model.pkl`:** The serialized model file generated after training.
- **`app.py`:** The Flask application code that serves the model and renders the web interface.
- **`index.html`:** The HTML file for the user input form.
- **`requirements.txt`:** A list of Python dependencies required to run the project.
- **`README.md`:** This README file.

## How to Run the Project

### Prerequisites

- Python 3.7 or higher
- Flask
- Pickle
- Numpy

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pahinithi/Loan-Status-Prediction-using-Machine-Learning.git
   ```
2. Navigate to the project directory:
   ```bash
   cd loan-status-prediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000/` to access the application.

### Usage

- Enter the required information in the input form.
- Click on "Predict" to get the prediction of the loan status.

### Model Explanation

The model is a binary classifier trained to predict whether a loan will be approved or not based on various features. The model was trained using a Support Vector Machine (SVM) Algorithm and achieved an accuracy of **79.86%** on the training data and **83.33%** on the test data.

### Dataset

The dataset used for this project contains features such as gender, marital status, income, loan amount, credit history, etc

## Project Structure

- `loan-status-prediction.ipynb`: Contains all the code related to data preprocessing, model training, and evaluation.
- `app.py`: The backend Flask application that handles user requests and serves predictions.
- `index.html`: The frontend HTML page where users can input their data.
- `loan_status_model.pkl`: The saved machine learning model.
- `requirements.txt`: Contains the list of packages required to run this project.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue with your suggestions.

## License

This project is licensed under the MIT License.

## Contact

For any questions or inquiries, please contact me at [nithilan32@gmail.com](mailto:nithilan32@gmail.com).

