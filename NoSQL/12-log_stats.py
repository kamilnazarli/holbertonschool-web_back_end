#!/usr/bin/env python3
'''
To provide some stats about Nginx logs stored in MongoDB
'''

import pymongo
from pymongo import MongoClient
connection = MongoClient()
db = connection.logs
print("{} logs".format(db.nginx.count()))
print("Methods:")
method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for i in method:
    print("method {}: {}".format(i, db.nginx.count(('method': i))))
print("{} {}".format(db.nginx.count({'method': 'GET'}, {'path' : '/status'})))
