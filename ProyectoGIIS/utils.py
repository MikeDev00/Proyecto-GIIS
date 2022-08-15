import pymongo
from pymongo import MongoClient

conn_str ="mongodb+srv://'Proyecto GIIS':123$5678@db-giis.dfbdpjx.mongodb.net/?retryWrites=true&w=majority"
try:
    client = pymongo.MongoClient('conn_str')
except Exception:
    print("Error: " + Exception)


db = client['DB-GIIS']

print(client.list_database_names())
