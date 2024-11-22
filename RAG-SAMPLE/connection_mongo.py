
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def connect():
    load_dotenv()
    uri = "mongodb+srv://newmaharshihello:RCBFOtJ0Xaffon9a@clusterrag.c26rv.mongodb.net/?retryWrites=true&w=majority&appName=ClusterRAG"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    connect()
