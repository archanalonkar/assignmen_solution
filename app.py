from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
import pickle
from src.ml_proj.pipeline.prediction import PredictionPipeline

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained encoding and scaling models
# scaler = pickle.load(open("artifacts\data_validation\scaler.pkl", "rb"))
# encoder = pickle.load(open("artifacts\data_validation\label_encoder.pkl", "rb"))


with open('artifacts\data_validation\scaler.pkl','rb') as f:
    scaler = pickle.load(f)


@app.route("/", methods=["GET"])
def homePage():
    return render_template("index.html")

@app.route("/train", methods=["GET"])
def training():
    os.system("python main.py")
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        try:

            cat_cols = ['gender','has_dependents','marital_status','region','employment_type']
            num_cols = ['age','salary','tenure_years'] 
            
            d = dict(request.form.lists())
            df= pd.DataFrame(d) 


            for col in df.columns:
                if col in cat_cols:
                    with open(f'artifacts\\data_validation\\{col}_encoder.pkl','rb') as f:
                        encoder = pickle.load(f)
                        df[col] = encoder.transform(df[col])

            with open(f'artifacts\\data_validation\\scaler.pkl','rb') as f:
                        scaler = pickle.load(f)

            df[num_cols] =  scaler.transform(df[num_cols])
            
            


            with open('artifacts\\model_trainer\\logistic_regression_model.pkl','rb') as f:
                 model = pickle.load(f)
            pred = model.predict(df.values)


            result = 'Not Enrolled 'if pred == 0 else 'Enrolled'

        

            return render_template("results.html", prediction=result)

        except Exception as e:
            print("Error:", e)
            return render_template("results.html", prediction=f"Error: {str(e)}")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
