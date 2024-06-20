import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
import os

ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise ValueError(f"Environment variable {MONGODB_URL_KEY} is not set")

                print(f"MongoDB URL: {mongo_db_url}")  # Debugging line

                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name

        except Exception as e:
            raise e

from sensor.configuration.mongo_db_connection import MongoDBClient

if __name__ == '__main__':
    try:
        mongodb_client = MongoDBClient()
        print("Collection names:", mongodb_client.database.list_collection_names())
    except Exception as e:
        print(f"An error occurred: {e}")
