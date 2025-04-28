
from Text_Summarizer.entity import ModelTrainerConfig
from Text_Summarizer.config.configuration import ConfigurationManager
from Text_Summarizer.conponents.data_model_train import ModelTrainer




class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()