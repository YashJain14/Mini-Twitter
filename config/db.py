from pymongo import MongoClient
import certifi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB URI from the environment
MONGODB_URI = os.getenv("MONGODB_URI")

# Connect to MongoDB
conn = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())
