from Text_Summarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from Text_Summarizer.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from Text_Summarizer.pipeline.stage04_model_train import ModelTrainingPipeline
from Text_Summarizer.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline
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
        logging.exception(e)
        raise e

STAGE_NAME = 'Data Transformation Stage'

try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise e



STAGE_NAME = "Model Training Stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    model_train = ModelTrainingPipeline()
    model_train.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
            logging.exception(e)
            raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    model_train = ModelEvaluationTrainingPipeline()
    model_train.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
            logging.exception(e)
            raise e