# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://manoharkillamsetti:z9BBDm3onYTeUf5Q@cluster0.9zgxw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

import os, sys, json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
# print(MONGO_DB_URL)
ca = certifi.where()

class NetworkDataExtract():
  def __init__(self):
    try:
      pass
    except Exception as e:
      raise NetworkSecurityException(e,sys)
    
  def csv_to_json_convertor(self,file_path):
    try:
      data = pd.read_csv(file_path)
      data.reset_index(drop=True, inplace=True)
      records = list(json.loads(data.T.to_json()).values())
      return records
    except Exception as e:
      raise NetworkSecurityException(e,sys)   
    
  def insert_data_mongodb(self, records,database, collection):
    try:
      self.database = database
      self.collection =collection
      self.records = records

      self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
      self.database = self.mongo_client[self.database]
      self.collection = self.database[self.collection]
      self.collection.insert_many(self.records)
      return(len(self.records))
    except Exception as e:
      raise NetworkSecurityException(e,sys)
    
if __name__ == '__main__':
  FILE_PATH = 'Network_Data\phisingData.csv'
  DATABASE ='network'
  COLLECTION = 'networkData'
  networkobj = NetworkDataExtract()
  records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
  print(records)
  no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
  print(no_of_records)