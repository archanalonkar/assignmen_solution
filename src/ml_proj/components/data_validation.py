import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os
import numpy as np
from src.ml_proj import logger
from src.ml_proj.entity.config_entity import DataValidationConfig



class DataPreprocessing:
    def __init__(self, df: pd.DataFrame, config: DataValidationConfig):
        self.config = config
        self.df = df
        self.encoder = None  # To store the fitted LabelEncoder
        self.scaler = None   # To store the fitted StandardScaler

    def drop_employee_id(self):
        if 'employee_id' in self.df.columns:
            self.df.drop(columns=['employee_id'], inplace=True)
            logger.info("Dropped Employee ID column.")

    def encode_categorical_columns(self):
        
        try:
            categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
            encoder = LabelEncoder()

            for col in categorical_cols:
                self.df[col] = encoder.fit_transform(self.df[col])

            logger.info("Categorical columns encoded successfully.")

            # Save the encoder as .pkl file
            encoder_save_path = os.path.join(self.config.root_dir, "label_encoder.pkl")
            joblib.dump(self.encoder, encoder_save_path)
            logger.info(f"LabelEncoder saved at: {encoder_save_path}")
        except Exception as e:
            logger.error(f"Error encoding categorical columns: {e}")
            raise e

    def scale_features(self, features: list):
        
        try:
            scaler = StandardScaler()
            self.df[features] = scaler.fit_transform(self.df[features])

            logger.info(f"Features {features} scaled successfully.")

            # Save the scaler as .pkl file
            scaler_save_path = os.path.join(self.config.root_dir, "scaler.pkl")
            joblib.dump(self.scaler, scaler_save_path)
            logger.info(f"StandardScaler saved at: {scaler_save_path}")
        except Exception as e:
            logger.error(f"Error scaling features: {e}")
            raise e

    def save_preprocessed_data(self, save_path):
        
        try:
            # Ensure the directory exists before saving
            save_dir = os.path.dirname(save_path)
            os.makedirs(save_dir, exist_ok=True)  # Create directory if it doesn't exist

            # Save the preprocessed CSV
            self.df.to_csv(save_path, index=False)

            logger.info(f"Preprocessed data successfully saved at: {save_path}")
            print(f"✅ File saved at: {save_path}")  # Debugging output
        except Exception as e:
            logger.error(f"Error saving preprocessed data: {e}")
            raise e

class DataValidation:
    def __init__(self, config=DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        
        try:
            validation_status = True  # Default to True

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    break  # Stop checking further

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status
        except Exception as e:
            raise e