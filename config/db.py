from pymongo import MongoClient
import certifi
MONGO_URI = "mongodb+srv://----------------------.mongodb.net"

conn = MongoClient(MONGO_URI,tlsCAFile=certifi.where())