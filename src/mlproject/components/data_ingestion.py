# Postgres --> Traiun-test-split ---> datase

import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

import pandas as pd

from dataclasses import dataclass
from src.mlproject.utils import read_postgres_data

from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try:
            # Reading Code
            # df= read_postgres_data()
            df=pd.read_csv(os.path.join('notebook/data','stud.csv'))
            
            logging.info("Reading data from PostgreSQL database")
             
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            train_set,test_set= train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
        
            logging.info("Data ingestion completed successfully")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e, sys) from e
            logging.error(f"Error in data ingestion: {e}")
            