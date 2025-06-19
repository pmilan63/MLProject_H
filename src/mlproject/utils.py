import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

import pandas as pd
from dotenv import load_dotenv
load_dotenv()

 # Importing psycopg2 to connect to PostgreSQL
import psycopg2

import pickle
import numpy as np

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score


host= os.getenv("host")
port= os.getenv("port")
database= os.getenv("database")
user= os.getenv("user")
password= os.getenv("password")


def read_postgres_data():
   logging.info("Reading data from PostgreSQL database Started")
   try:
         
         # Establishing the connection
         conn = psycopg2.connect(
              host=host,
              port=port,
              database=database,
              user=user,
              password=password
         )
         logging.info("Connection to PostgreSQL database established successfully",conn)
         
         # Reading data from a table named 'your_table_name'
         query = "SELECT * FROM Students"
         df = pd.read_sql_query(query, conn)
         print(df.head())
         
         # Closing the connection
         conn.close()
         
         logging.info("Reading data from PostgreSQL database completed")
         return df
     
   except Exception as e:
       raise CustomException(e, sys) from e
       logging.error(f"Error in reading data from PostgreSQL: {e}")
       
def save_object(file_path, obj):
      try:
          dir_path = os.path.dirname(file_path)
          os.makedirs(dir_path, exist_ok=True)
          
          with open(file_path, 'wb') as file_obj:
              pickle.dump(obj, file_obj)
              
          logging.info(f"Object saved at {file_path}")
      except Exception as e:
          logging.error(f"Error saving object at {file_path}: {e}")
          raise CustomException(e, sys) from e
      

def evaluate_models(X_train, y_train, X_test, y_test, models,param):
    try:
        report = {}
        
        for i in range(len(list(models))):
            model= list(models.values())[i]
            
            para= param[list(models.keys())[i]]
            
            gs=GridSearchCV(model,para,cv=3)
            gs.fit(X_train, y_train)
            
            model.set_params(**gs.best_params_)

            model.fit(X_train, y_train)
            
            y_train_pred = model.predict(X_train)
            
            y_test_pred = model.predict(X_test)
            
            train_model_score = r2_score(y_train, y_train_pred)
            
            test_model_score = r2_score(y_test, y_test_pred)
            
            report[list(models.keys())[i]] = test_model_score
            
        return report
    except Exception as e:
        raise CustomException(e, sys) from e