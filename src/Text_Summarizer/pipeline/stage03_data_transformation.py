from    Text_Summarizer.config.configuration import ConfigurationManager
from Text_Summarizer.conponents.data_transformation import DataTransformation
from Text_Summarizer.logging import logging


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()