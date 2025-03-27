
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import joblib
import os
import pandas as pd
from src.ml_proj import logger


class LogisticRegressionConfig:
    def __init__(self, root_dir, train_data_path, test_data_path, model_name, param_grid, cv_folds, scoring_metric, target_column):
        self.root_dir = root_dir
        self.train_data_path = train_data_path
        self.test_data_path = test_data_path
        self.model_name = model_name
        self.param_grid = param_grid
        self.cv_folds = cv_folds
        self.scoring_metric = scoring_metric
        self.target_column = target_column

class ModelTrainer:
    def __init__(self, config: LogisticRegressionConfig):
        self.config = config

    def train(self):
        # Read training and testing data
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        # Separate features (X) and target (y)
        train_x = train_df.drop([self.config.target_column], axis=1)
        test_x = test_df.drop([self.config.target_column], axis=1)
        train_y = train_df[[self.config.target_column]]
        test_y = test_df[[self.config.target_column]]

        # Create Logistic Regression model
        model = LogisticRegression()

        # Set up GridSearchCV for hyperparameter tuning
        grid_search = GridSearchCV(
            model, 
            self.config.param_grid, 
            cv=self.config.cv_folds, 
            scoring=self.config.scoring_metric
        )

        # Fit the model to the training data
        grid_search.fit(train_x, train_y)

        # Get the best model from GridSearchCV
        best_model = grid_search.best_estimator_

        # Save the trained model
        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(best_model, model_path)
        logger.info(f"Model saved at: {model_path}")