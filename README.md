# assignmen_solution


## Workflows

### 1. Update config.yaml
- Modify the configuration file as per your project requirements. This may include settings for paths, parameters, and other configurations needed for the project.

### 2. Update schema.yaml
- Make necessary changes to the schema file, which defines the structure of your dataset, column types, and other data-related configurations.

### 3. Update params.yaml
- Adjust the parameters in this file to fit your project’s requirements. This could include hyperparameters for training models, evaluation metrics, and other related settings.

### 4. Update the entity
- Modify any entities in the project based on the needs of your pipeline (e.g., features, target variables, or additional attributes in your dataset).

### 5. Update the configuration manager in `src/config`
- Make changes to the configuration manager to ensure proper integration with the updated files (e.g., loading configurations from YAML files).

### 6. Update the components
- Ensure that the components of the project (data validation, data preprocessing, feature engineering, etc.) are updated to work with the latest version of your configuration and schema.

### 7. Update the pipeline
- Adjust the pipeline to ensure it reflects any changes made in the configuration, schema, or components. This will ensure the correct flow of data through the various stages.

### 8. Update `main.py`
- Make necessary adjustments to the `main.py` script that controls the execution of your machine learning pipeline. This may include importing components and running the pipeline steps.

### 9. Update `app.py`
- Modify the Flask app (`app.py`) to handle user input, run predictions, and return results as needed. Ensure all routes and logic are working as expected.

## How to Run?

### STEPS:

### Step 1: Clone the repository
Clone the repository to your local machine:

---
git clone https://github.com/archanalonkar/assignmen_solution.git
-----
### Step 2: Create a Conda environment

After opening the repository, create a Conda environment with Python 3.10.16:

conda create -n assignmen_solution python=3.10.16 -y
conda activate assignmen_solution
----
### Step 3: Install the requirements

Install the necessary dependencies using the requirements.txt file:

pip install -r requirements.txt
----
### Step 4: Run the Flask app

Finally, run the following command to start the Flask app:

python app.py

Once the app is running, open your browser and go to http://localhost:8080 to interact with the application.
-----

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


### dagshub

[dagshub](https://dagshub.com/dashboard)

MLFLOW_TRACKING_URI=https://dagshub.com/PranavUikey/ml_complete_proj.mlflow
MLFLOW_TRACKING_USERNAME= PranavUikey
MLFLOW_TRACKING_PASSWORD=b164a979bd8248b638f9af447e9b059ea588b82a
python script.py

Run this to export as env variables:

export MLFLOW_TRACKING_URI=https://dagshub.com/archanalonkar/assignmen_solution.mlflow

export MLFLOW_TRACKING_USERNAME=archanalonkar 

export MLFLOW_TRACKING_PASSWORD=99d5c2ca62fdceb37551730c817faa20a64b99
