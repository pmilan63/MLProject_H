import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

import pandas as pd
from dotenv import load_dotenv
load_dotenv()

 # Importing psycopg2 to connect to PostgreSQL
import psycopg2

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