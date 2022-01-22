import pymongo
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

_DB = 'mongodb+srv://Andrew:<password>@cluster0.vucxs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

# use PyMongo driver to connect to Atlas cluster
client = MongoClient(_DB)

# create db on your cluster
db = client.gettingStarted

# create a new collection for database
assistant = db.assistant
