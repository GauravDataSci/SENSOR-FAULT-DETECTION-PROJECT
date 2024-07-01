import pymongo
import certifi
import os
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY

ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
             #mongo_db_url = os.getenv(MONGODB_URL_KEY)
                mongo_db_url = "mongodb+srv://gkumardav:Indrajeet2222@cluster.3kmskua.mongodb.net/?retryWrites=true&w=majority&appName=CLUSTER"
                if mongo_db_url is None:
                    raise ValueError(f"Environment variable {MONGODB_URL_KEY} is not set")
                print(mongo_db_url)

                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            # Here you can log the error or add more context before raising it
            raise Exception(f"Failed to initialize MongoDBClient: {str(e)}")

# Example usage:
# Ensure you set the environment variable MONGODB_URL_KEY before using the class
# os.environ[MONGODB_URL_KEY] = "your_mongodb_url"
# db_client = MongoDBClient()
# I put the url directly as I was having issue while making the connection using :
#mongo_db_url = os.getenv(MONGODB_URL_KEY)
# Error was: MONGODB_URL_KEY IS NOT SET PROPERLY.
