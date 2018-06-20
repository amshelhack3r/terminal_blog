import pymongo


class Database(object):
    # mongodb localhost and port to connect
    uri = "mongodb://127.0.0.1:27017"
    DATABASE = None
    # define the client

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE = client['terminal_blog']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
