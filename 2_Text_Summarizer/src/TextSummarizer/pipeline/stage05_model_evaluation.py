from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.model_evaluation import ModelEvaluation
from TextSummarizer.logging import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        configM = ConfigurationManager()
        model_evaluation_config = configM.get_model_evaluation_config()
        model_evaluation_obj = ModelEvaluation(config = model_evaluation_config)
        model_evaluation_obj.evaluate()

