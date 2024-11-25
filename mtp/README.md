# Telephone User Behavior Class Prediction App

This is a Flask web application that predicts user behavior class based on various input features. The application uses a machine learning model trained with scikit-learn. We experimented with different models and ultimately chose a Random Forest classifier for its superior performance.

## Project Introduction

This dataset downloaded from Kaggle, provides a comprehensive analysis of mobile device usage patterns and user behavior classification. It contains 700 samples of user data, including metrics such as app usage time, screen-on time, battery drain, and data consumption. Each entry is categorized into one of five user behavior classes, ranging from light to extreme usage, allowing for insightful analysis and modeling.

### Key Features:

- **User ID:** Unique identifier for each user.
- **Device Model:** Model of the user's smartphone.
- **Operating System:** The OS of the device (iOS or Android).
- **App Usage Time:** Daily time spent on mobile applications, measured in minutes.
- **Screen On Time:** Average hours per day the screen is active.
- **Battery Drain:** Daily battery consumption in mAh.
- **Number of Apps Installed:** Total apps available on the device.
- **Data Usage:** Daily mobile data consumption in megabytes.
- **Age:** Age of the user.
- **Gender:** Gender of the user (Male or Female).
- **User Behavior Class:** Classification of user behavior based on usage patterns (1 to 5).

## Features

- Input form for user data
- Prediction of user behavior class
- Example data autofill

## Project Structure
```
├── app.py
├── model.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── templates/
│   ├── index.html
│   ├── result.html
│
└── static/
    └── styles.css
```

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerization)

### Installation

1. Clone the repository:
```
   git clone https://github.com/Zaccaria-Amillou/ml_zoomcamp_2024/tree/main/mtp.git
   cd your_project
```
2. Create a virtual environment and activate it:
```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install the dependencies:
```
   pip install -r requirements.txt
```
4. Run the Flask application:
```
   python app.py
```
5. Open your web browser and go to http://127.0.0.1:5000/.

### Using Docker

1. Build the Docker image:
```
   docker-compose build
```
2. Run the Docker container:
```
   docker-compose up
```
3. Open your web browser and go to http://127.0.0.1:5000/.

## Usage

1. Open the web application in your browser.
2. Fill in the form with the required data or click "Fill Example Data" to autofill the form.
3. Click "Predict" to get the prediction result.

