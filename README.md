# Credit Card Fraud Detection System

## Overview

This project is a machine learning-based web application that detects fraudulent credit card transactions using a Logistic Regression model. It provides a simple and interactive interface to input transaction details and get instant predictions.

---

## Features

* Real-time fraud prediction (Fraud / Legitimate)
* Interactive UI built using Streamlit
* Uses PCA-based features (V1–V28)
* Fast and lightweight model integration using Joblib
* Clean and modern user interface

---

## Tech Stack

* Language: Python
* Libraries:

  * NumPy
  * Scikit-learn (Logistic Regression)
  * Joblib
  * Streamlit

---

## Dataset Information

* Dataset used: Credit Card Fraud Detection Dataset (Kaggle)
* The dataset contains anonymized transaction data
* Features V1–V28 are generated using PCA (Principal Component Analysis) for privacy
* Includes:

  * Time
  * Amount
  * PCA features (V1–V28)
  * Class (0 = Legitimate, 1 = Fraud)

Dataset Link: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

---

## How It Works

1. User enters transaction details (Amount, Time, selected PCA features)
2. Input is converted into model-compatible format
3. Model predicts whether transaction is:

   * Fraudulent
   * Legitimate
4. Result is displayed instantly on UI

---

## Setup Instructions

1. Clone the repository:

   ```
   git clone https://github.com/your-username/credit-card-fraud-detection.git
   ```

2. Navigate to project folder:

   ```
   cd credit-card-fraud-detection
   ```

3. Install required libraries:

   ```
   pip install streamlit numpy scikit-learn joblib
   ```

4. Run the application:

   ```
   python -m streamlit run app.py
   ```

---

## Learning Outcomes

* Understanding of classification models (Logistic Regression)
* Working with PCA-based datasets
* Model deployment using Streamlit
* Integration of ML model with frontend
* Version control using Git and GitHub

##
