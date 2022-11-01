import pymongo


conn_str = "mongodb://admin:mongoadmin@database1:27017/?authMechanism=DEFAULT&authSource=admin" 
try:
    client = MongoClient('conn_str')
except Exception:
    print("Error: " + Exception)


myDb = client['GIIS']

print(client.list_database_names())
