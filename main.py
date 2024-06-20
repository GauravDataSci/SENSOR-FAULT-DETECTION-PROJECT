"""
----------------------------------------------------------------------------------
THIS IS THE CODE TO TEST WHETHER OUR MONGO_DB_CONNECTION IS SET CORRECTLY OR NOT
-----------------------------------------------------------------------------------
from sensor.configuration.mongo_db_connection import MongoDBClient

if __name__ =='__main__':
    mongodb_client = MongoDBClient()
    print("collection name:",mongodb_client.database.list_collection_names())
"""

