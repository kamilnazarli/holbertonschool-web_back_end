#!/usr/bin/env python3
from pymongo import MongoClient
'''
To provide some stats about Nginx logs
'''

client = MongoClient('localhost', 27017)
db = client.logs
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
clc = db.nginx
def log_stats(mongo_collection):
    '''
    Docstring for log_stats

    :param mongo_collection: takes collection
    '''

    print("{} logs".format(clc.count_documents({})))
    print("Methods:")
    for method in methods:
        print("method {}: {}".format(method, mongo_collection.count_documents({"method": method})))
    print("{} status check".format(mongo_collection.count_documents({"method": "GET", "path": "/status"})))
if __name__ == "__main__":
    log_stats(clc)
