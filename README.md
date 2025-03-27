# assignmen_solution


## Workflows

### 1. Update config.yaml

### 2. Update schema.yaml

### 3. Update params.yaml

### 4. Update the entity

### 5. Update the configuration manager in `src/config`

### 6. Update the components

### 7. Update the pipeline

### 8. Update `main.py`

### 9. Update `app.py`

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
