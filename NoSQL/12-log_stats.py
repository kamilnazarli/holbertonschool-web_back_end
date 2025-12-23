#!/usr/bin/env python3
'''
To provide some stats about Nginx
'''

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.logs
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
clc = db.nginx
def log_stats(mongo_collection):
    '''
    Docstring for log_stats

    :param mongo_collection: takes collection
    '''

    print("Methods:")
    for method in methods:
        print("method {}: {}".format(method, mongo_collection.count_documents({"method": method})))
    print("{} status check".format(mongo_collection.count_documents({"path": "/status"})))
log_stats(clc)
