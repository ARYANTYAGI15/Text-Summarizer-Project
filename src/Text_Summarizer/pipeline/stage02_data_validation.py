from    Text_Summarizer.config.configuration import ConfigurationManager
from Text_Summarizer.conponents.data_validation import DataValiadtion
from Text_Summarizer.logging import logging


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()