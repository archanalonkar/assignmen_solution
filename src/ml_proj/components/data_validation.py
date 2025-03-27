import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os
from src.ml_proj import logger
from src.ml_proj.entity.config_entity import DataValidationConfig



class DataPreprocessing:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def encode_categorical_columns(self):
        try:
            categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
            encoder = LabelEncoder()

            for col in categorical_cols:
                self.df[col] = encoder.fit_transform(self.df[col])

            logger.info("Categorical columns encoded successfully.")
        except Exception as e:
            logger.error(f"Error encoding categorical columns: {e}")
            raise e

    def scale_features(self, features: list):
        
        try:
            scaler = StandardScaler()
            self.df[features] = scaler.fit_transform(self.df[features])

            logger.info(f"Features {features} scaled successfully.")
        except Exception as e:
            logger.error(f"Error scaling features: {e}")
            raise e

class DataValidation:
    def __init__(self, config=DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        except Exception as e:
            raise e