from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_transformation import DataTransformation
from TextSummarizer.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        configM = ConfigurationManager()
        data_transformation_config = configM.get_data_transformation_config()
        data_transformation_obj = DataTransformation(config = data_transformation_config)
        data_transformation_obj.convert() 