from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_validation import DataValidation
from TextSummarizer.logging import logger



class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        configM = ConfigurationManager()
        data_validation_config = configM.get_data_validation_config()
        data_validation_obj = DataValidation(config = data_validation_config)
        data_validation_obj.validate_all_files_exist()


