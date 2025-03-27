# Machine Learning Pipeline

## 1. Data Preprocessing

### Label Encoding applied to categorical features:
- **gender**
- **marital_status**
- **employment_type**
- **region**
- **has_dependents**

### Scaling applied to numerical features:
- **age**
- **salary**
- **tenure_years**

## 2. Model Training

- **Algorithm Used**: Logistic Regression
- **Training Process**: The model is trained on the preprocessed dataset and saved as `model.pkl` for later use.

## 3. Deployment

- A Flask web application (`app.py`) is used to serve the model.
- Users input employee details through a web interface (`index.html`).
- Predictions are displayed on the results page (`result.html`).

## 4. Model Evaluation

The model is evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**


## 5. Future Improvements

- Experiment with advanced models like Random Forest and XGBoost.
- Deploy the model using cloud services like AWS/GCP.
