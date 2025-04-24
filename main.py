from Text_Summarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from Text_Summarizer.logging import logging


STAGE_NAME = "Data ingestion stage"

try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
