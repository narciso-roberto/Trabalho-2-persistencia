import os
from dotenv import load_dotenv
import asyncio 
from motor.motor_asyncio import AsyncIOMotorClient 

load_dotenv()

uri = os.getenv("MONGOURL")
client = AsyncIOMotorClient(uri) 
db = client.test_database 
collection = db.test_collection 

