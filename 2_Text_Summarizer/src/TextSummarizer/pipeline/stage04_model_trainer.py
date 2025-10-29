from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.model_trainer import ModelTrainer
from TextSummarizer.logging import logger


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        configM = ConfigurationManager()
        model_trainer_config = configM.get_model_trainer_config()
        model_trainer_obj = ModelTrainer(config = model_trainer_config)
        model_trainer_obj.train() 

