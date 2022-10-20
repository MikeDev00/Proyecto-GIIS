import pymongo


conn_str ="mongodb+srv://admin:1234@giis.lszcdmn.mongodb.net/?retryWrites=true&w=majority"
try:
    client = pymongo.MongoClient('conn_str')
except Exception:
    print("Error: " + Exception)


myDb = client['GIIS']

print(client.list_database_names())
