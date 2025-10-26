from TextSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f">>>>>>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
    data_ingestion_obj = DataIngestionTrainingPipeline()
    data_ingestion_obj.main()
    logger.info(f">>>>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<")


except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "DATA VALIDATION STAGE"

try:
    logger.info(f">>>>>>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
    data_validation_obj = DataValidationTrainingPipeline()
    data_validation_obj.main()
    logger.info(f">>>>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<")


except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "DATA TRANSFORMATION STAGE"

try:
    logger.info(f">>>>>>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
    data_transformation_obj = DataTransformationTrainingPipeline()
    data_transformation_obj.main()
    logger.info(f">>>>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<")


except Exception as e:
    logger.exception(e)
    raise e