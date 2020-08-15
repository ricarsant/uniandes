from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Establishing a Connection
client = MongoClient('localhost', 27017)

def ConsultarMovies(idMovie):
    dbh = client["TALLER3"]
    collection = dbh['movies']
    movie_doc = collection.find({"_id":idMovie})
    return movie_doc