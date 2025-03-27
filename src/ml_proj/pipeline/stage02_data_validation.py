from src.ml_proj.config.configuration import ConfigurationManager
from src.ml_proj.components.data_validation import DataValidation, DataPreprocessing
from src.ml_proj import logger
import pandas as pd
import os

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
   
        config = ConfigurationManager()

        data_validation_config = config.get_data_validation_config()

        # Load dataset
        df = pd.read_csv(data_validation_config.unzip_data_dir)
        print(df.shape)
        # Data preprocessing
        data_preprocessor = DataPreprocessing(df,data_validation_config)

        # Encode categorical columns
        data_preprocessor.encode_categorical_columns()

        # Scale numerical features
        features_to_scale = ["age", "salary", "tenure_years"]
        data_preprocessor.scale_features(features_to_scale)

        # Data validation
        data_validation = DataValidation(config=data_validation_config)
        validation_passed = data_validation.validate_all_columns()

        # Save the preprocessed file in the validation folder
        preprocessed_save_path = os.path.join(config.config.data_validation.validation_dir, "preprocessed_data.csv")
        data_preprocessor.save_preprocessed_data(preprocessed_save_path)
    

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e