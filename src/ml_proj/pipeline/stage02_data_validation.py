from src.ml_proj.config.configuration import ConfigurationManager
from src.ml_proj.components.data_validation import DataValidation, DataPreprocessing
from src.ml_proj import logger
import pandas as pd

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        # Data preprocessing
        df = pd.read_csv(config.config.data_validation.unzip_data_dir)  # Load your dataframe
        data_preprocessor = DataPreprocessing(df)

        # Encode categorical columns
        data_preprocessor.encode_categorical_columns()

        # Scale numerical features
        features_to_scale = ["age", "salary", "tenure_years"]
        data_preprocessor.scale_features(features_to_scale)
        # Data validation
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

    

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e