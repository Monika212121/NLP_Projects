from TextSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
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
