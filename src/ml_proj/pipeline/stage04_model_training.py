from src.ml_proj.config.configuration import ConfigurationManager
from src.ml_proj.components.model_training import ModelTrainer
from src.ml_proj import logger



STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        
        config = ConfigurationManager()
        logistic_regression_config = config.get_logistic_regression_config()
        model_trainer = ModelTrainer(config=logistic_regression_config)
        model_trainer.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e