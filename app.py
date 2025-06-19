from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig

from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_transformation import DataTransformationConfig

from src.mlproject.components.model_trainer import ModelTrainer
from src.mlproject.components.model_trainer import ModelTrainerConfig


if __name__ == "__main__":
    logging.info("Starting the application...")
    
    try:
        data_ingestion = DataIngestion() 
        # data_ingestion_config = DataIngestionConfig()

        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        # data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))

    except Exception as e:
        logging.info("divided by zero error.")
        raise CustomException(e, sys) from e
